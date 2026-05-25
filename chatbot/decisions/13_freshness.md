# 13 — Freshness / update strategy

**Status:** DECIDED (headline strategy); some sub-questions remain
**Decided on:** 2026-05-10
**Decision:**
- **Scheduled weekly job** via the existing `memory/scripts/run_weekly.{bat,py}` infrastructure (already in place: `scrape_news.py`, `scrape_comunicati.py`, `renumber_news.py`, `notify.py`).
- **Change detection** via `content_hash` (sha256 of body) in the unified frontmatter — avoids re-embedding unchanged docs.
- **Provenance** preserved on every doc: `source_url`, `date_published`, `date_scraped`. Raw fetched source must land in a sibling `_raw/` folder (mandatory cold archive).
- **File-naming convention:** files/folders starting with `_` are **ignored by the indexer**. Indexer reads only top-level `.md` in each corpus folder.
- **Long-term ingestion rule applies:** every structural choice in the freshness pipeline is judged against the 5-point checklist in CLAUDE.md §7 (new-doc-into-existing-bucket, schema accommodation, deletion detection, change detection, provenance).

**Still OPEN sub-decisions:**
- Full re-index cadence (incremental upserts only, or periodic full re-embed to absorb chunker/embedder upgrades)
- Deletion / staleness detection (currently scrapers only add, never reconcile)
- Manifesto-revision handling (keep old version with date stamp? replace?)
- Newsletter de-duplication policy (newsletters summarize prior comunicati — accept overlap, or dedupe at chunk level?)

**Rationale:** Weekly cadence aligns with the party's publication rhythm. The infrastructure already exists, so this choice is also lowest-friction. Decoupling change-detection from re-fetch (via content_hash) keeps embedding costs bounded as the corpus grows.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md` (corpus structure + scripts) and `feedback_long_term_ingestion.md` (the structural-choice checklist). See CLAUDE.md §5 (frontmatter schema, `_raw/`, `_` convention) and §7 (long-term ingestion rule).

## The question

The corpus is live. New newsletters arrive ~weekly. New press releases (comunicati) arrive irregularly. Manifesto sections occasionally get updated. **How does new content reach the chatbot's index, and how fast?**

## Why it matters for the ORA chatbot

- A bot that says "ORA's most recent statement on X is from 2025-09-23" when there's a 2026-03-08 newsletter on the exact topic looks broken.
- Election cycles, breaking news, and party congresses produce bursts of new material — exactly when users will ask the bot about them.
- Update workflows interact with chunking (decision 04 — same chunker must run on new docs), embedding (decision 05 — same model), and vector store (decision 06 — needs to support upserts).

## Options

### A — Manual re-index
- A script reprocesses everything on demand. Cheap, simple, slow.
- Risk: you forget to run it after a newsletter drops.

### B — Scheduled weekly job
- A cron / `run_weekly.bat` (already in `memory/scripts/`) scrapes new content and re-indexes incrementally.
- Aligns with newsletter cadence. Predictable.

### C — Event-driven (RSS / file-watcher / webhook)
- Detect new content in `memory/corpus/` and trigger ingestion automatically.
- Lowest latency to "freshness". More moving parts.

### D — Full re-index periodically + incremental in between
- Daily/weekly incremental upserts, monthly full re-index to catch drift (e.g., chunker improvements, metadata schema changes).
- Belt-and-braces. Good for production.

### E — Time-aware retrieval (no special update needed for the bot to behave well)
- Index everything with timestamps; the retrieval prompt instructs the LLM to prefer recent sources when relevant.
- Doesn't address the ingestion-pipeline question — pair with one of A–D.

## Sub-decisions baked in

- **Manifesto updates:** when a section is revised, do we keep the old version (and tell users "the manifesto was updated on X")? Or replace?
- **Newsletter de-duplication:** newsletters re-summarize past comunicati — do we ingest both, accepting overlap, or dedupe?
- **YouTube content:** new episodes drop weekly. Are transcripts auto-pulled (decision 14 / pipeline), or manually?

## What we'd need to know to choose

- How quickly does freshness matter — same day, same week, same month?
- Are you willing to maintain a scheduled job, or do you want a manual "I'll run it when I remember" workflow?
- Is there a deployment surface where stale answers would cause real harm (a public bot during election week)?

## Reference

- KB concept: `14_production_concerns.md`
- KB concept: `05_the_rag_pipeline.md`

## Observations
- `memory/scripts/run_weekly.bat` + `run_weekly.py` exist and target weekly cadence — current scaffolding is already pointed at option B.
- Newsletters: latest is `2026-05-10.md`. Today is 2026-05-11. So the pipeline is being used.
