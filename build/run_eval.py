"""Run the MVP eval sets (decision 12 stage 1).

Three sets:
  - retrieval  → tests corpus_retrieve only (no Anthropic calls, essentially free)
  - adversarial → full pipeline per query (Anthropic + Voyage + Qdrant, ~$0.10/query)
  - showcase   → full pipeline; verbatim output for human review

Usage:
  python build/run_eval.py retrieval
  python build/run_eval.py adversarial
  python build/run_eval.py showcase
  python build/run_eval.py all
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import voyageai
from qdrant_client import QdrantClient

from agent.orchestrator import get_orchestrator
from agent.secrets import load_secrets
from agent.tools import corpus_retrieve, data_lookup


EVAL_DIR = Path(__file__).resolve().parent.parent / "evaluation"
RUNS_DIR = EVAL_DIR / "runs"


def _now_run_dir() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%S")
    h = hashlib.sha1(ts.encode()).hexdigest()[:6]
    d = RUNS_DIR / f"{ts}_{h}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _load_jsonl(path: Path) -> list[dict]:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


# ---------- RETRIEVAL ----------


def _resolve_set_path(set_name: str, override: str | None) -> Path:
    """Resolve which JSONL to read for a given set. CLI `--file <name>` overrides."""
    if override:
        # Allow bare name (resolved relative to EVAL_DIR) or full path
        candidate = EVAL_DIR / override
        if candidate.is_file():
            return candidate
        p = Path(override)
        if p.is_file():
            return p
    return EVAL_DIR / f"{set_name}_set.jsonl"


def run_retrieval(run_dir: Path, set_override: str | None = None) -> dict:
    """Retrieval-correctness eval — goes through the agent's planner stage so
    that tier filters and data-vs-corpus routing match real bot behavior.
    Cost: ~$0.01-0.02/query for the planner stage (Opus, ~1K tokens). No
    synthesis / verifier calls.
    """
    items = _load_jsonl(_resolve_set_path("retrieval", set_override))
    orch = get_orchestrator()

    results: list[dict] = []
    pass_count = 0
    t_start = time.time()

    for it in items:
        plan = orch.plan(it["query"], history=[])
        # Mirror what orchestrator.retrieve_parallel does: corpus + (maybe) data,
        # then merge so the eval looks at the full retrieval surface.
        tier_filters = plan.get("tier_filters") or None
        if plan.get("query_type") == "compare" and plan.get("comparison_parties"):
            tier_filters = list(set((tier_filters or []) + ["other-parties"]))

        resolved = plan.get("resolved_query") or it["query"]
        corpus_chunks = corpus_retrieve(
            resolved,
            qdrant=orch.qdrant, voyage=orch.voyage,
            tier_filter=tier_filters, top_k=10,
        )

        data_chunks: list = []
        if plan.get("is_empirical") and plan.get("data_metric"):
            try:
                data_chunks = data_lookup(
                    plan["data_metric"],
                    qdrant=orch.qdrant, voyage=orch.voyage, top_k=5,
                )
            except Exception:
                data_chunks = []

        chunks = corpus_chunks + data_chunks
        # Build the actuals
        retrieved_ids = [c.get("chunk_id", "") for c in chunks]
        retrieved_tiers = [c.get("tier") for c in chunks]
        tiers_set = set(retrieved_tiers)

        failures: list[str] = []
        # Required prefixes — at least one chunk with each prefix
        for prefix in it.get("expected_parent_id_prefixes") or []:
            if not any(cid.startswith(prefix) for cid in retrieved_ids):
                failures.append(f"missing prefix: {prefix}")
        # Required tiers
        for tier in it.get("expected_tier_present") or []:
            if tier not in tiers_set:
                failures.append(f"tier absent: {tier}")
        # Forbidden tiers
        for tier in it.get("expected_tier_absent") or []:
            if tier in tiers_set:
                failures.append(f"forbidden tier present: {tier}")

        passed = not failures
        if passed:
            pass_count += 1

        results.append({
            "id": it["id"],
            "category": it.get("category"),
            "query": it["query"],
            "planner_query_type": plan.get("query_type"),
            "planner_tier_filters": plan.get("tier_filters"),
            "effective_tier_filter": tier_filters,
            "passed": passed,
            "failures": failures,
            "retrieved_chunk_ids": retrieved_ids,
            "retrieved_tiers": retrieved_tiers,
            "expected_parent_id_prefixes": it.get("expected_parent_id_prefixes"),
            "expected_tier_present": it.get("expected_tier_present"),
            "expected_tier_absent": it.get("expected_tier_absent"),
        })

    out_path = run_dir / "retrieval_results.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    elapsed = time.time() - t_start
    summary = {
        "set": "retrieval",
        "total": len(items),
        "passed": pass_count,
        "failed": len(items) - pass_count,
        "pass_rate": pass_count / max(len(items), 1),
        "elapsed_s": round(elapsed, 1),
    }
    print(f"\nRetrieval: {pass_count}/{len(items)} passed ({summary['pass_rate']:.1%}) in {elapsed:.1f}s")
    if pass_count < len(items):
        print("Failures:")
        for r in results:
            if not r["passed"]:
                print(f"  [{r['id']}] {r['query'][:60]}")
                for f in r["failures"]:
                    print(f"      • {f}")
    return summary


# ---------- ADVERSARIAL ----------


def _check_substrings_any_of(text: str, candidates: list[str]) -> bool:
    t = text.lower()
    return any(c.lower() in t for c in candidates)


def _check_substrings_none_of(text: str, candidates: list[str]) -> list[str]:
    t = text.lower()
    return [c for c in candidates if c.lower() in t]


def run_adversarial(run_dir: Path, set_override: str | None = None) -> dict:
    items = _load_jsonl(_resolve_set_path("adversarial", set_override))
    orch = get_orchestrator()

    results: list[dict] = []
    pass_count = 0
    t_start = time.time()

    for it in items:
        result = orch.answer(it["query"], history=[])
        plan = result.plan or {}

        failures: list[str] = []

        # is_refusal expectation
        exp_refusal = bool(it.get("expected_refusal"))
        if exp_refusal != result.is_refusal:
            failures.append(f"expected_refusal={exp_refusal}, actual={result.is_refusal}")

        # refusal_reason
        exp_reason = it.get("expected_refusal_reason")
        if exp_reason and result.refusal_reason != exp_reason:
            failures.append(f"expected_refusal_reason={exp_reason!r}, actual={result.refusal_reason!r}")

        # query_type
        exp_qt = it.get("expected_query_type")
        if exp_qt and plan.get("query_type") != exp_qt:
            failures.append(f"expected_query_type={exp_qt!r}, actual={plan.get('query_type')!r}")

        # adversarial_flag
        exp_af = it.get("expected_adversarial_flag")
        if exp_af and plan.get("adversarial_flag") != exp_af:
            failures.append(f"expected_adversarial_flag={exp_af!r}, actual={plan.get('adversarial_flag')!r}")

        # must contain any of
        any_of = it.get("must_contain_any_of") or []
        if any_of and not _check_substrings_any_of(result.answer, any_of):
            failures.append(f"none of must_contain_any_of present: {any_of}")

        # must not contain
        not_of = it.get("must_not_contain") or []
        bad = _check_substrings_none_of(result.answer, not_of)
        if bad:
            failures.append(f"forbidden substrings present: {bad}")

        passed = not failures
        if passed:
            pass_count += 1

        results.append({
            "id": it["id"],
            "category": it.get("category"),
            "query": it["query"],
            "passed": passed,
            "failures": failures,
            "answer": result.answer,
            "is_refusal": result.is_refusal,
            "refusal_reason": result.refusal_reason,
            "plan_query_type": plan.get("query_type"),
            "plan_adversarial_flag": plan.get("adversarial_flag"),
            "elapsed_s": round(result.elapsed_seconds, 1),
        })

    out_path = run_dir / "adversarial_results.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    elapsed = time.time() - t_start
    summary = {
        "set": "adversarial",
        "total": len(items),
        "passed": pass_count,
        "failed": len(items) - pass_count,
        "pass_rate": pass_count / max(len(items), 1),
        "elapsed_s": round(elapsed, 1),
    }
    print(f"\nAdversarial: {pass_count}/{len(items)} passed ({summary['pass_rate']:.1%}) in {elapsed:.1f}s")
    if pass_count < len(items):
        print("Failures:")
        for r in results:
            if not r["passed"]:
                print(f"  [{r['id']}] {r['query'][:60]}")
                for f in r["failures"]:
                    print(f"      • {f}")
    return summary


# ---------- SHOWCASE ----------


def _collect_citations(r) -> dict[str, dict]:
    """Build {cited_id: {source_url, tier, attribution, label}} for an AnswerResult.

    Covers both corpus/data citations (resolved from retrieved_chunks + data_cards
    by chunk_id) and web citations (resolved from web_results by position →
    web:1, web:2...). Used by build/render_docx.py to render a "Fonti" section
    with hyperlinks at the end of each turn.
    """
    out: dict[str, dict] = {}
    cited = set(r.cited_chunk_ids or [])

    # Corpus + data chunks
    for c in (r.retrieved_chunks or []) + (r.data_cards or []):
        cid = c.get("chunk_id")
        if cid in cited:
            out[cid] = {
                "source_url": c.get("source_url") or "",
                "tier": c.get("tier") or "",
                "attribution": c.get("attribution") or "",
                "label": cid,
            }

    # Web results — keyed web:1, web:2... in the order they were emitted
    for i, w in enumerate(r.web_results or [], 1):
        wid = f"web:{i}"
        if wid in cited:
            out[wid] = {
                "source_url": w.get("source_url") or "",
                "tier": "web",
                "attribution": "web",
                "label": wid,
            }
    return out


def run_showcase(run_dir: Path, set_override: str | None = None) -> dict:
    """Showcase runner with INCREMENTAL writes — each query is appended to
    showcase_results.jsonl immediately, so a mid-run crash (e.g., credit
    limit) preserves all progress so far."""
    items = _load_jsonl(_resolve_set_path("showcase", set_override))
    orch = get_orchestrator()
    t_start = time.time()
    out_path = run_dir / "showcase_results.jsonl"
    out_path.write_text("", encoding="utf-8")  # truncate

    n_done = 0

    def _append(entry: dict) -> None:
        with out_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    for it in items:
        try:
            if "query_sequence" in it:
                history: list[dict] = []
                turns: list[dict] = []
                for q in it["query_sequence"]:
                    r = orch.answer(q, history=history)
                    turns.append({
                        "query": q,
                        "answer": r.answer,
                        "cited_chunk_ids": list(r.cited_chunk_ids),
                        "citations": _collect_citations(r),
                        "is_refusal": r.is_refusal,
                        "refusal_reason": r.refusal_reason,
                        "elapsed_s": round(r.elapsed_seconds, 1),
                    })
                    history.append({"role": "user", "content": q})
                    history.append({"role": "assistant", "content": r.answer})
                entry = {
                    "id": it["id"],
                    "category": it.get("category"),
                    "turns": turns,
                    "showcases": it.get("showcases"),
                    "audience_notes": it.get("audience_notes"),
                }
            else:
                r = orch.answer(it["query"], history=[])
                entry = {
                    "id": it["id"],
                    "category": it.get("category"),
                    "query": it["query"],
                    "answer": r.answer,
                    "cited_chunk_ids": list(r.cited_chunk_ids),
                    "citations": _collect_citations(r),
                    "is_refusal": r.is_refusal,
                    "refusal_reason": r.refusal_reason,
                    "elapsed_s": round(r.elapsed_seconds, 1),
                    "showcases": it.get("showcases"),
                    "audience_notes": it.get("audience_notes"),
                }
            _append(entry)
            n_done += 1
            print(f"  [{n_done}/{len(items)}] {it['id']} done")
        except Exception as e:
            print(f"  [{n_done+1}/{len(items)}] {it['id']} FAILED: {e!r}")
            _append({"id": it["id"], "category": it.get("category"), "error": str(e)[:300]})
            raise  # re-raise so the run halts on auth/credit issues

    elapsed = time.time() - t_start
    summary = {
        "set": "showcase",
        "total": len(items),
        "completed": n_done,
        "elapsed_s": round(elapsed, 1),
    }
    print(f"\nShowcase: {n_done}/{len(items)} queries written for human review in {elapsed:.1f}s")
    return summary


# ---------- main ----------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "set",
        choices=["retrieval", "adversarial", "showcase", "all"],
        help="Which eval set to run.",
    )
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        help="Override the default JSONL file name (relative to evaluation/ or absolute path).",
    )
    args = parser.parse_args()

    run_dir = _now_run_dir()
    print(f"Run dir: {run_dir}")

    summaries: list[dict] = []
    if args.set in ("retrieval", "all"):
        summaries.append(run_retrieval(run_dir, set_override=args.file))
    if args.set in ("adversarial", "all"):
        summaries.append(run_adversarial(run_dir, set_override=args.file))
    if args.set in ("showcase", "all"):
        summaries.append(run_showcase(run_dir, set_override=args.file))

    # Write summary
    summary_path = run_dir / "summary.md"
    lines = [f"# Eval run summary — {datetime.now(timezone.utc).isoformat()}\n"]
    for s in summaries:
        lines.append(f"## {s['set']}")
        for k, v in s.items():
            if k == "set":
                continue
            lines.append(f"- **{k}**: {v}")
        lines.append("")
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nSummary: {summary_path}")


if __name__ == "__main__":
    main()
