# 12 — Evaluation

**Status:** DECIDED (staged)
**Decided on:** 2026-05-14
**Decision:** **Staged eval design.** MVP eval (pre-approval) covers only what Riccardo can verify without political-substance expertise; full answer-content gold set deferred to post-approval, when party-substance experts (Boldrin/Forchielli/staff) can author it.

---

## The reframe that drove the decision

The original eval shape (hand-built 80-100 question gold set authored by Riccardo) was rejected for an honest reason: **Riccardo does not hold the political-substance expertise to verify whether the bot correctly represents ORA's positions.** He built the corpus; he's the architect; he's not the content authority on every party stance. Authoring "gold" answers he couldn't verify would generate noisy, possibly wrong reference data.

Compounded by: the MVP exists to demo for ORA leadership approval. The project may not continue. Investing 15 hours up front in an authored gold set is the wrong call given that uncertainty.

So eval is **staged**:
- **MVP (pre-approval):** ship with only what is verifiable without political-substance expertise. Be honest about the gap.
- **Production (post-approval):** the people who *can* author gold-content (party staff, leadership) take over that role. Decision 12 explicitly defers that work.

---

## Stage 1 — MVP / pre-approval eval (LOCKED)

Four components, none requiring political-substance expertise:

### 1. Adversarial / structural set (~25-30 questions)

About-the-bot, not about-the-corpus. Tests guardrail behaviors locked in decision 11 — verifiable purely by checking the bot's response pattern, no domain knowledge needed.

Coverage (approximate counts, Claude scaffolds, Riccardo approves):
- Loaded framing handling (11.A) — ~8 questions
- Roleplay refusal / chatbot transparency (11.B sub-branch 1) — ~5 questions
- Hypothetical-leader hedged inference (11.B sub-branch 2) — ~5 questions
- Prompt injection — user-side (11.C) — ~4 questions
- Prompt injection — content-side (11.C) — ~3 questions
- Default refusal trigger (no corpus answer) — ~3 questions
- Off-scope redirect (medical/legal/financial) — ~3 questions
- Date-beyond-corpus → web axis kicks in — ~3 questions

**Workflow:** Claude scaffolds ~30 candidate questions from decision 11's behaviors. Riccardo reviews, edits, approves. Authoring time: **~1-2 hours of Riccardo's time**.

**Pass criteria: 100%.** Adversarial failures are weaponizable; zero failures is the only acceptable bar.

### 2. Retrieval-correctness set (~30-40 questions)

Source-only, not answer-content. Riccardo doesn't need to know what the *answer* should be — he knows what *folder* the answer should come from. Tests retrieval + reranker without requiring substance verification.

Schema per entry:
```jsonl
{
  "query": "Cosa propone ORA sull'energia nucleare?",
  "expected_chunk_sources": ["manifesto/06-energia.md", "leaders/boldrin/profile/06-*"],
  "expected_tier_present": ["A1a"],
  "expected_tier_absent": [],
  "notes": "..."
}
```

Scoring: did the top-5 reranked chunks come from the expected source files / tier? **Readable from chunk_id metadata; no need to read the answer text.**

Coverage: ~one question per major topic (matching the 20 tesi + identity + key data topics) + a few cross-cutting / leader-disambiguation / comparison cases.

**Workflow:** Claude scaffolds from corpus structure. Riccardo verifies the source mappings are correct. Authoring time: **~2 hours of Riccardo's time**.

**Pass criteria: ≥90%** — retrieval will occasionally surface a related-but-not-listed chunk legitimately; near-misses are tolerable, gross misses are not.

This is the **cleanest signal** for the empirical comparison queued in decision 05 (Voyage vs Gemini embedder): retrieval-only eval directly measures what the embedder choice affects, and is fully unblocked by stage 1.

### 3. Structural runtime checks (no authoring; already running)

The guardrail layer from decision 11 emits passive faithfulness signal on every query, logged to Postgres per 11.E:
- `citation_strip` rate — how often did the deterministic post-check strip uncited claims?
- `verifier_fail` rate — how often did the Haiku verifier mark a claim `not_supported`?
- `regen_attempted` rate — how often did the pipeline have to regenerate?
- `refusal_triggered` rate — how often did the bot fall back to the default refusal phrase?
- Latency p50/p95 — does the system meet sub-second-before-generation + 1-2s end-to-end?

**No upfront authoring.** Trend-tracking these across demo sessions (and later, real traffic) tells us the bot's structural correctness without a gold set.

**Pass criteria:** tracked, not gated. Surface in weekly review per 11.E.

### 4. Demo showcase set (~10-15 questions)

Hand-picked by Riccardo to demonstrate capability across the four objectives (state / project / justify / compare). **Not graded by Riccardo** — graded by the demo audience (ORA leadership). They know if the bot misrepresents their positions; that's their expertise, not Riccardo's.

This converts "Riccardo grades 100 answers" into "the actual experts grade 10-15 answers in real time." Right people in the right role.

Failures during the demo become signal for whether and how to continue.

---

## Stage 2 — Production / post-approval eval (DEFERRED)

Locks **only if the project is approved** for production. At that point:

- **Full gold set, ~80-100 questions, authored by party-substance experts** (Boldrin, Forchielli, or designated party staff). Distribution across the four objectives as in the original proposal: ~25 state / ~12 project / ~10 justify / ~15 compare / ~8 refusal / ~5 off-scope / ~5 leader-vs-party disambiguation.
- **6-dimension human scoring rubric:** faithfulness, attribution, citation completeness, persona, refusal correctness, comparison correctness (compare-questions only).
- **LLM-judge regression tracking** (Ragas-style) as supplementary trend signal, using Opus 4.7 as judge. Not source of truth.
- **Pass criteria:** ≥95% gold, 100% adversarial.
- **Cadence:** every architectural change; weekly during active dev; pre-deploy.

**Owner of the post-approval authoring:** TBD with leadership. Likely party staff with editorial sign-off from Boldrin/Forchielli.

---

## Empirical evals queued from earlier decisions — what unblocks when

| Comparison | Source decision | Unblocked at | Signal quality |
|---|---|---|---|
| Voyage vs Gemini embedder | #05 rationale 1 | **Stage 1** (retrieval-correctness set) | Strong — retrieval-only eval directly measures embedder quality |
| Opus 4.7 vs Sonnet 4.6 | #09 migration trigger | Stage 2 (full gold set) | Weak in stage 1 (structural-runtime only); strong in stage 2 |

Recommendation: stay on `claude-opus-4-7` for the MVP per decision 09; revisit Opus vs Sonnet only when stage-2 gold set exists. Run the Voyage-vs-Gemini comparison as soon as the stage-1 retrieval set is authored — it's a clean ~half-day experiment.

---

## Where eval lives

```
memory/eval/
├── adversarial_set.jsonl       # ~25-30 questions, stage 1
├── retrieval_set.jsonl         # ~30-40 questions, stage 1
├── showcase_set.jsonl          # ~10-15 demo questions, stage 1
├── gold_set.jsonl              # (stage 2 only) ~80-100 questions, post-approval
├── rubric.md                   # scoring criteria
└── runs/
    └── YYYY-MM-DD_<config-hash>/
        ├── answers.jsonl                # raw bot output for this config
        ├── scores_adversarial.jsonl     # automated pass/fail
        ├── scores_retrieval.jsonl       # automated source-match scoring
        ├── runtime_metrics.json         # aggregated from Postgres logs
        └── summary.md                   # per-category + aggregate
```

Directory created on first eval run, not pre-emptively.

---

## Cost summary (stage 1)

- Authoring time (Riccardo, one-shot): ~5 hours total across all three sets he touches
- Scaffolding time (Claude, one-shot): ~1-2 hours
- Per eval run cost: ~$2-4 in Opus 4.7 tokens (60-70 questions × ~$0.05/query at MVP density)
- Per eval run time: ~10-15 minutes wall-clock automated + demo-audience time for showcase set

This sits comfortably within the £5 MVP cap from decision 09 — a full stage-1 eval run is ~$3, leaving room for multiple iterations.

---

## Rationale

**The honest framing wins.** Decision 12's job is not to specify a "perfect" eval; it's to specify the **right eval given the actual situation**. The actual situation is: uncertain project, no political-substance authority on the engineer's side, real experts only enter post-approval. A staged design matches that structure. Forcing a stage-2-shaped eval onto stage-1 conditions would either produce noisy/wrong gold data or burn 15 hours that may never compound.

**What the locked design preserves:**
- Riccardo only authors what he can verify
- Real experts (leadership) play the right role at the right time (demo grading → post-approval authoring)
- Voyage-vs-Gemini comparison is unblocked, so decision 05's "queued empirical eval" can actually run
- Decision 11's structural checks (citation enforcement, Haiku verifier, logging) carry passive faithfulness signal without needing a gold set
- Demo path has *something* to point at — not nothing

**What the locked design accepts as gap:**
- Pre-approval, the bot's answer-content correctness is **not measured**. The structural checks catch egregious failures (uncited claims, miscited claims) but cannot catch a subtly-wrong attribution or a misrepresented party stance unless the demo audience flags it.
- Opus-vs-Sonnet comparison is delayed until stage 2.
- Trend-tracking across builds during MVP development relies on the runtime metrics + adversarial+retrieval pass rates, not on answer-content faithfulness scores.

---

## Reference

- KB concept: `09_evaluating_rag.md`
- Source: Es et al. 2023 (Ragas) in the parallel KB's `raw/`
- Source: Google DeepMind 2024 (FACTS) in the parallel KB's `raw/`
- Cross-references: #05 (embedder comparison gated here), #09 (Opus-vs-Sonnet comparison gated here), #11.E (runtime metrics source)

## Observations
*(populate during MVP demo runs and post-approval stage 2 authoring)*
