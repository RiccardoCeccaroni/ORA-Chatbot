"""Smoke test: realistic user questions against the live retrieval pipeline.

Run from project root with the .env file present:
    python tests/smoke_queries.py

Prints a compact per-question summary: top source_docs per bucket + a
~150-char preview. Useful as a sanity check on retrieval quality before
demoing to ORA management.
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path


def _load_env(path: Path = Path(".env")) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def _short(text: str, n: int = 140) -> str:
    text = " ".join(text.split())
    return text[:n] + ("…" if len(text) > n else "")


def _summarize_bucket(chunks: list[dict], label: str) -> None:
    if not chunks:
        print(f"  [{label}]: EMPTY")
        return
    print(f"  [{label}] {len(chunks)} chunks:")
    for c in chunks[:3]:
        src = c.get("source_doc") or c.get("extras", {}).get("source_doc") or "?"
        tier = c.get("tier") or "?"
        score = c.get("_rerank_score", "?")
        text = _short(c.get("text", ""))
        print(f"    - {src}  [tier={tier}, score={score}]")
        print(f"      \"{text}\"")


def run(topic: str, *, include_comparison: bool = False) -> None:
    from ora_mcp.retrieval import find_position

    print(f"\n{'=' * 70}")
    print(f"Q: {topic}")
    if include_comparison:
        print("   (include_comparison=True)")
    print("=" * 70)

    result = asyncio.run(find_position(
        topic,
        top_k_per_bucket=5,
        include_comparison=include_comparison,
    ))

    _summarize_bucket(result.get("official_party", []), "official_party")
    leaders = result.get("leader_views", {})
    _summarize_bucket(leaders.get("boldrin", []), "leader: boldrin")
    _summarize_bucket(leaders.get("forchielli", []), "leader: forchielli")
    _summarize_bucket(result.get("supporting_data", []), "supporting_data")
    if include_comparison:
        _summarize_bucket(result.get("comparison", []), "comparison")


def main() -> None:
    _load_env()
    if "QDRANT_URL" not in os.environ:
        print("ERROR: QDRANT_URL not set. Create .env at project root.")
        sys.exit(1)

    questions = [
        ("riforma fiscale ORA", False),
        ("posizione di ORA sulle pensioni", False),
        ("cosa farebbe ORA sull'immigrazione", False),
        ("ORA università ricerca innovazione", False),
        ("ORA matrimonio egualitario diritti civili", False),
        ("differenza tra ORA e Azione politica industriale", True),
    ]

    for q, cmp in questions:
        try:
            run(q, include_comparison=cmp)
        except Exception as e:
            print(f"FAILED on '{q}': {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
