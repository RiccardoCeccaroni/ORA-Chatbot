# 18 — Audit / verification agent

**Status:** DECIDED
**Decided on:** 2026-05-12
**Decision:** Build a periodic, advisory-only auditor — **LLM-driven, agentic** — that cross-checks every file in the data corpus against its upstream source and live web, classifies findings by severity, and writes a per-sweep report. Never modifies any corpus file.

---

## Locked configuration

| Fork | Choice | Why |
|------|--------|-----|
| F1 — **Scope** | Data corpus only (v1) | 78 stat-cards today, every card has a falsifiable claim + `source_url`. Highest signal-to-noise. v2 may extend to party corpus for URL-liveness. |
| F2 — **Verification method** | Source URL re-fetch **+** live web search, both performed by the LLM via tool use | They answer different questions ("is what I cited still accurate?" vs "is there something newer?"). Folding both into one agentic flow per card keeps reasoning coherent. |
| F3 — **Trigger** | On-demand v1 → scheduled v2 | Run manually 2–3 times. If reports surface things you act on, graduate to monthly cron via `run_weekly.bat` infra. Don't pre-pay for a schedule whose value is unproven. |
| F4 — **Output** | Per-run report at `_audit/YYYY-MM-DD-report.md` + end-of-run console summary | Persistent record + immediate signal. `_audit/` is indexer-ignored (CLAUDE.md §5 `_` rule). |
| F5 — **Implementation surface** | **Agentic LLM auditor with thin Python harness** (see below) | The work *is* judgment: reading heterogeneous sources (ISTAT pages, OECD PDFs, Eurostat tables) and matching them against stat-card claims. Deterministic parsers are brittle and source-specific. The LLM is the right tool for the substance; the harness only schedules and aggregates. |

---

## Why this needs its own decision

- **Architectural commitment.** A verifier subsystem touches retrieval rules (when do we trust the corpus vs the web?), the cost model (web search × N cards × cadence), and the persona ("never invent numbers" extends to "never trust a stale number we cited"). This belongs in `decisions/`, not in a script that accretes.
- **Plugs a known gap.** CLAUDE.md §7 drift #4: "No staleness / deletion detection in any existing scraper. They only add, never reconcile." The auditor is the reconcile half.
- **Composes with decision 17.** The data corpus stat-card model (`data_metric` + `data_period` + `source_url` + the cited number in body) was *designed* to be machine-verifiable. The auditor is the tool that exercises that property.
- **Composes with the contradiction posture (CLAUDE.md §4 + `feedback_data_contradictions_handling`).** When the auditor finds a discrepancy, the handling rule is already locked: never silently pick a side; address inline if methodologically explainable, otherwise ping Riccardo.

---

## F1 — Scope

### (a) Data corpus only ★

`memory/corpus/data/**/*.md` — currently 78 stat-cards across 21 topic folders.

- **Why this is high signal:** every stat-card carries a discrete, falsifiable claim (one metric, one period, one number) with a `source_url` pointing at a specific table or release. The audit is "does the source still say this number?" — binary, machine-checkable.
- **What it catches:** revised figures (ISTAT revises Q-on-Q), methodology changes, dead URLs, agency-side rebrands, newer releases superseding the cited period.
- **What it can't catch:** anything outside the data corpus.

### (b) Data + party corpus

Adds `ora-party/` (tesi, comunicati, newsletter, identity).

- **Degrades to URL liveness + content_hash diff.** Tesi state positions, not numbers. The auditor can check "does the upstream `source_url` still serve the same content the day we last hashed it" — but it can't say "is this position still ORA's official stance" without human judgment.
- **Useful but lower yield.** Mostly surfaces upstream-deletions and upstream-rewrites (drift #4 again).

### (c) Everything

Adds `leaders/`, `YoutubeScripts/`, `_raw/`. Same caveats as (b), even lower yield (leader posts and transcripts are rarely revised upstream).

**Recommendation: (a) for v1.** (b) is a reasonable v2 once (a) runs reliably and we know what the report ergonomics look like.

---

## F2 — Verification method

Two distinct checks, which catch different failure modes.

### Re-fetch the `source_url` (deterministic)

- Pull the URL, locate the cited metric/period in the response, compare to the number in the stat-card body.
- **Catches:** value revisions, dead URLs, agency-side moves (301 → new URL).
- **Limit:** ISTAT databrowser is user-driven CSV export (per `feedback_istat_sdmx_systematic`). Stat-card `source_url` often points at the metadata/landing page, not a fetchable CSV. For these, re-fetch can only check page liveness + maybe headline numbers; the gold-standard re-check requires Riccardo to re-export.

### Live web search (probabilistic)

- "Has the agency published a newer release for this metric?"
- **Catches:** stat-card cites 2024 figure; agency released 2025 update last month; auditor flags "newer release exists."
- **Limit:** noisy, costs per query, less reliable for narrow metrics with overlapping names.

### (c) Both ★

The two questions are different: "is what I cited still accurate?" vs "is there something more recent I should be citing?" Doing both, per card, is the only way to cover both. **In the LLM-driven design (F5), the model decides which checks to run per card and in what order** — both checks are tools it can invoke, not separate orchestrated stages. Web-search budget is bounded by the per-card tool-call cap — see §Costs below.

---

## F3 — Trigger

### (a) On-demand
You run a command, the auditor sweeps. Predictable cost, no surprises.

### (b) Scheduled
Weekly or monthly cron via existing `memory/scripts/run_weekly.bat` infra (decision 13). Predictable cadence, but commits to a recurring cost without first knowing whether the output is useful.

### (c) On-demand v1, scheduled v2 ★

Run manually for the first 2–3 sweeps. If the reports actually surface things you act on, graduate to scheduled (monthly is probably the right cadence — most D1 sources publish on quarterly+ release calendars; weekly would mostly produce empty reports). If reports are noise, kill the project before paying for a schedule.

**Monthly > weekly** because: ISTAT major releases follow quarterly/annual calendars; Eurostat similar; the marginal value of catching a revision within 1 week vs 4 weeks is small for a chatbot whose freshness floor is already "weekly via newsletters" (decision 13).

---

## F4 — Output

The auditor is **advisory only** — locked by the user request. Modifying corpus files is out of scope. The question is just where the advice lands.

### (a) Per-run report file ★
`memory/corpus/data/_audit/YYYY-MM-DD-report.md` — one file per sweep, frozen, never overwritten. Easy to diff sweeps over time, easy to archive. The `_audit/` prefix means the indexer ignores it (CLAUDE.md §5 `_` rule).

### (b) Single rolling log
One file, appended to. Less greppable, harder to diff sweeps.

### (c) Inline ping ★
Console summary at end of run: "N cards checked, K discrepancies — see [report path]". When run inside Claude Code, this lands in conversation context.

### Recommended bundle: (a) + (c).
Persistent record + immediate signal.

### Discrepancy report structure (proposed)

```markdown
# Audit report — 2026-05-12

**Cards swept:** 78 · **Discrepancies:** 7 · **Errors:** 1

## Critical (value mismatch)
- `lavoro-politiche-sociali/tasso-occupazione-italia-2024.md`
  - Stat-card cites: 62.2% (annual avg 2024)
  - Re-fetched ISTAT (today): 62.5% (revised 2026-04-15)
  - **Recommendation:** update card to 62.5%, note revision in body.

## Moderate (newer release available)
- `energia-ambiente-sostenibilita/mix-elettrico-italia-2021.md`
  - Stat-card period: 2021
  - Web search surfaced: Terna mix elettrico 2024 (published 2025-03)
  - **Recommendation:** consider ingesting the 2024 release; 2021 card may be retired or kept as historical reference.

## Informational
- `agricoltura/pac-sussidi-italia-2023-2027.md`: source_url redirected (200 → 301 → 200, final URL changed). Content match. Recommend updating source_url.

## Errors (auditor couldn't verify)
- `<card>`: source_url 404; manual investigation needed.
```

Three severity tiers — **critical** (number changed), **moderate** (newer release / methodology revised), **informational** (URL moved, agency rebrand) — match the existing contradiction-handling posture.

---

## F5 — Implementation surface

### Chosen: agentic LLM auditor with thin Python harness

The substance of auditing is **reading and judging**, not parsing. Stat-card sources are heterogeneous: ISTAT databrowser pages, Eurostat tables, OECD PDFs, IEA reports, Bruegel briefs, ISPRA spreadsheets. Each format would need its own parser, and even then "the cited number is X, the source now says Y" is often nuanced — methodology footnotes, unit changes, definitional shifts, revisions backdated to prior periods. This is judgment work. Hand it to the LLM.

**Architecture:**

```
audit_data.py (harness)
  │
  ├── glob memory/corpus/data/**/*.md          ← deterministic
  ├── load _audit/_manifest.json               ← skip recently-verified cards
  │
  ├── for each stat-card:
  │     │
  │     └── invoke agentic LLM loop:
  │           tools available:
  │             • web_search
  │             • fetch_url
  │             • read_card_body
  │
  │           system prompt: auditor persona + severity-tier rubric
  │                          + "never invent numbers" + "respect ISTAT databrowser limits"
  │
  │           user input: the stat-card frontmatter + body
  │
  │           expected output (structured JSON):
  │             {
  │               card_id, severity: critical|moderate|informational|verified|error,
  │               source_check: { url_status, cited_value_still_present, ... },
  │               newer_release_check: { found, candidate_url, candidate_period, ... },
  │               finding_text: <human-readable Italian summary>,
  │               recommendation: <suggested action — advisory only>,
  │               confidence: low|medium|high
  │             }
  │
  ├── aggregate findings → render markdown report
  ├── update _audit/_manifest.json (card_id, content_hash, last_audited_at, last_severity)
  └── print console summary
```

**Why this shape:**

- **The harness is thin on purpose.** It only does the things that don't need judgment: globbing files, sequencing API calls, writing JSON, rendering markdown. Adding logic here is a code smell — that logic belongs in the prompt or the rubric.
- **The LLM is the auditor.** It reads the card, decides which web searches to run, fetches what it needs, reasons about whether the source still supports the claim, and writes the finding. This is exactly the kind of multi-step reasoning agentic loops are for.
- **Structured output keeps the report deterministic** while the reasoning is free-form. The harness aggregates JSON, the LLM writes prose.
- **Same Claude model the chatbot will use.** Whatever generation model decision 09 lands on, the auditor uses it too — keeps tooling consolidated and prompt patterns transferable.
- **Manifest enables incremental sweeps.** Cards whose `content_hash` hasn't changed AND were verified in the last N days can be skipped. Sweep cost scales with corpus *growth*, not corpus *size*.

**Failure modes specific to LLM-driven auditing:**

1. **Hallucinated discrepancies** — LLM claims source says X when it says Y. Mitigations: structured output with `confidence` field; LLM must cite the specific snippet from the fetched source that supports the finding; low/medium confidence findings land in informational tier with a manual-review flag.
2. **Missed discrepancies** — LLM skims the source and misses a footnote-buried revision. Mitigations: rubric explicitly demands check of revision dates and methodology notes; spot-check sweeps manually for the first 2–3 runs to calibrate.
3. **Non-determinism across sweeps** — borderline case judged "moderate" today, "informational" tomorrow. Mitigations: low temperature; manifest records prior severity so re-classifications are visible as a delta in the next report.
4. **Cost drift** — agentic loops can balloon if the LLM keeps fetching. Mitigations: hard cap on tool calls per card (e.g., 5); manifest skips unchanged cards.

**Alternatives rejected:**

- **Pure deterministic Python** (originally floated): brittle per-source parsers, can't handle "methodology revised" cases at all, no path to nuance.
- **LLM as a last-resort judge** (originally recommended ★): underuses the model's strength. The bulk of the work *is* the kind of reading-and-comparing the model is best at.
- **Claude Code subagent (`/audit` slash command)**: nice ergonomics for one-off runs, but not schedulable, and each sweep would consume a full Claude Code conversation. Wrong shape for batch work.

---

## Costs (revised for LLM-driven design)

- 78 cards today; assume 200 in 6 months.
- Per card per sweep, agentic loop:
  - ~3–5 LLM calls (initial read, 1–3 tool-use turns for fetch/search, final finding emission)
  - ~2–4 tool invocations (web_search, fetch_url) — each with output tokens fed back into the next LLM call
  - rough total: ~30–80k tokens per card mostly cached on the system prompt + rubric
- Per-card cost: **~$0.05–0.20** at Claude Opus rates with prompt caching on the static parts. Cheaper with Haiku for first-pass triage if needed.
- **Monthly sweep over 200 cards (with manifest skipping unchanged cards): ~$10–40 worst case, less in steady state.**
- Higher than the original $1–2 estimate, but still trivial against the value of catching a wrong number in a public political bot.
- **Prompt caching is critical** — system prompt + rubric + severity-tier definitions go in the cache. The per-card variable content (the stat-card itself + tool outputs) is the only un-cached input.

---

## Implementation budget for v1

- **Harness:** ~150 lines of Python. File glob, JSON I/O, Anthropic SDK agentic loop, markdown rendering, manifest read/write.
- **Auditor prompt:** the bulk of the design work. Spans:
  - persona (advisory only, never modifies, never invents)
  - severity-tier rubric (critical / moderate / informational / verified / error)
  - tool-use protocol (when to web_search, when to fetch_url, hard cap)
  - structured output schema (JSON)
  - ISTAT databrowser handling (re-fetch is partial — flag for manual)
- **Rubric tests:** before scheduling, hand-pick 5–10 cards across topics (one ISTAT, one Eurostat, one think-tank, one with a known revision, one with a dead URL if findable) and run the auditor against them manually. Iterate the prompt until findings match Riccardo's own read of the same cards.

---

## What the auditor must NOT do

Locked constraints, regardless of which options win:

1. **Never modify any corpus file.** Advisory only.
2. **Never silently resolve a discrepancy.** Per `feedback_data_contradictions_handling`: address inline (if methodologically explainable) or escalate to Riccardo. Same rule applies to the auditor's reports.
3. **Never invent numbers.** If re-fetch parsing fails, the finding is "couldn't verify" (Error tier), not a guess.
4. **Never use bypass auth or scrape behind logins.** Stat-card sources are public by design.
5. **Respect ISTAT databrowser workflow.** For ISTAT cards whose `source_url` points to databrowser metadata pages: re-fetch checks liveness only; the value check is flagged "manual re-export needed" and lands in the informational tier. Do not attempt to programmatically replicate Riccardo's CSV export.

---

## Open follow-ups

- **Which web-search API?** Probably the same one the chatbot's live-context axis (§3) will use — pre-coordinate to avoid two integrations. Defer until decision on the chatbot's live retrieval is firmer.
- **How does the auditor know the "metric definition" of a card?** Currently `data_metric` is free-text in frontmatter. Re-fetch parsing needs to locate the same metric in the response — either by keyword match on `data_metric` or by a more structured field. May surface a need for `metric_canonical_id` later.
- **Caching layer for web-search results.** Recommended (cost), but where does the cache live? `_audit/_cache/`?
- **Auditor's own change log.** Should we keep a manifest of "card X was last successfully audited on Y" so partial sweeps are possible? Yes, lightweight `_audit/_manifest.json` keyed by `id` + `content_hash`.

---

## Reference

- CLAUDE.md §3 (retrieval design — live context axis informs the web-search half of the auditor), §4 (sourcing — contradiction posture extends to audit findings), §5 (frontmatter — `content_hash`, `source_url`, `_` indexer rule), §7 (drift #4 — this decision fills the gap).
- Decision 13 (freshness — auditor cadence may piggyback on `run_weekly.bat`).
- Decision 17 (data corpus — stat-card structure makes the auditor possible).
- Memory `feedback_istat_sdmx_systematic` — explains why ISTAT re-fetch is partial.
- Memory `feedback_data_contradictions_handling` — explains how findings must be surfaced.

## Observations

- The stat-card model from decision 17 was designed for machine verifiability. This decision cashes that property in.
- Auditor output (`_audit/*.md`) is itself documentation that the bot could one day cite ("the figure was revised on YYYY-MM-DD; previous value was X"). Not in v1, but the report format should remain parseable in case we want this.
- The advisory-only constraint is what makes this safe to ship without further architectural coupling. Once findings become auto-applied edits, this re-opens decision 13's "manifesto-revision handling" sub-question.

**Source of decision:** Claude Code session 2026-05-12 with Riccardo. Riccardo's framing prompt: "an agent that goes methodically and periodically to every folder and to every file here and cross-checks all the information present with data on the web... should not modify anything, just advising me." On the F5 fork specifically, Riccardo amended the initial Python-with-LLM-fallback recommendation to **LLM-driven** ("yes include the llm massively") — captured verbatim in the rationale above. This file *is* the canonical record.
