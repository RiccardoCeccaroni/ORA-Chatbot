# 19 — Leader corpus: retrievable content unit

**Status:** DECIDED
**Decided on:** 2026-05-13
**Decision:** **Model B — distilled artifacts are the corpus, with redundancy pruned.** For leaders (A2 tier), the retrievable units are the curated topic-aligned files under `profile/` (both leaders) and the curated leader articles under `articles/` (Boldrin only). The per-leader **`dialogues/` files are demoted to scaffolding** (`corpus_status: exclude`) because their entire content has been absorbed into `profile/` — every substantive stance from a dialogue is already in the profile, verbatim-quoted with timestamp + YouTube URL preserved as a link-back citation. Solo interviews are **not** brought into the corpus. Primary sources — raw HTML bios, source audio + diarization, raw `.txt` transcripts — live in `_raw/` (per-leader) or `_raw/joint-dialogues/` (shared) and are not chunked.

---

## Locked configuration

| Item | Choice |
|---|---|
| Retrievable for leaders | `<leader>/profile/` (both leaders) · `boldrin/articles/` (Boldrin only — Forchielli has no comparable article corpus) |
| Excluded from retrieval (scaffolding) | `<leader>/dialogues/` — `corpus_status: exclude` set on all 18 files. **Not** retrievable; kept on disk for provenance and so the `aggregator.py` pipeline can re-run profile regeneration. Citation back to dialogues happens via the per-quote `https://youtu.be/...` link-backs already embedded in profile bodies. |
| Not retrievable (raw) | Anything under `_raw/` — bios HTML, joint-dialogue audio + diarization, raw `.txt` transcripts |
| Solo interviews | **Out of corpus.** The two raw `.txt` files in `YoutubeScripts/Michele/interviste/` and Forchielli's Congresso di Azione `.txt` are not curated and will not be ingested. No `<leader>/interviews/` folder will be created. |
| Joint-dialogue speaker-tagged transcripts | Stay in `memory/YoutubeScripts/Michele e Alberto/_speaker_tagged/` as scaffolding for the curation pipeline. Not corpus. |
| Bio HTMLs | Moved into `<leader>/_raw/bios/`. `profile/00-anagrafica-e-carriera.md` is the retrievable canonical biographical artifact. |
| Boldrin academic papers | Out of scope, deleted from `YoutubeScripts/Michele/papers/`. |
| nFA articles index stub | Deleted (`YoutubeScripts/Michele/nFA articles/_index.md`). Superseded by `boldrin/articles/`. |

---

## The question

What is the **content unit** that retrieval ingests for the A2 tier (leaders)? The leader folder contains a mix of (a) raw sources, (b) curated primary documents, and (c) distillations. Treating them all as corpus would flood retrieval with noisy, redundant signal; treating none of them as corpus would force the bot to re-derive at query time what curation already did. The decision is which subset of artifacts gets a `corpus_status: include` and gets chunked + embedded.

## Why it matters

- **Voice attribution risk (CLAUDE.md §4).** Distillations are *editorial summaries* of the leader's positions. Retrieving them means the bot cites a paraphrase, not the leader's exact words. The frontmatter is designed to flag this (`type: leader_topic_profile`, `transcript_quality: distilled`), but the bot's citation pill must communicate "this is a curated summary of Boldrin's views" not "this is what Boldrin said."
- **Retrieval cost / quality.** Boldrin's `articles/` alone is 125 documents spanning 2006–2014, opinionated and topically scattered. Indexing them all puts a lot of dated, off-policy signal into the retriever. Indexing only the distilled topic-aligned `profile/` files (26 for Boldrin, 21 for Forchielli) keeps the leader slice small and tesi-aligned.
- **Tesi alignment.** `profile/` filenames mirror tesi numbering (00–21 + `altro--*`). This is deliberate — it makes Tier-2 gap-filling clean: when the manifesto has no Tier-1 position on topic NN, retrieval reaches `<leader>/profile/NN-topic.md` directly. Indexing primary articles instead would require the retriever to re-discover this alignment for every query.
- **Asymmetry between leaders.** Boldrin has 125 articles, Forchielli has none scraped. Model B makes the leaders symmetrically retrievable through their `profile/` and `dialogues/` regardless of how much primary material each has.
- **Long-term ingestion (CLAUDE.md §7).** New leader content (a fresh interview, a new article) goes through the curation pipeline (`_curation/`) before becoming retrievable. The corpus boundary is the curation gate, not the scraper output.

## Options considered

### A — Primary sources only
Index `articles/` + raw transcripts. `profile/` and `dialogues/` are internal scaffolding, not chunked.
- ✗ Drowns retrieval in 125 opinionated essays per leader.
- ✗ Loses the tesi-alignment work that profile/ already encodes.
- ✗ Distillation work becomes invisible to the bot.

### B — Distilled artifacts are the corpus ★ (chosen, pruned variant)
Index `profile/` for both leaders + `articles/` for Boldrin. `dialogues/` demoted to scaffolding; `interviews/` out entirely. Raw sources in `_raw/` are provenance only.
- ✓ Topic-aligned with tesi; clean Tier-2 gap-fill for objectives 1, 3, 4.
- ✓ Lean index (~47 profile docs across both leaders + 125 Boldrin articles).
- ✓ Asymmetric leaders work the same way through `profile/`.
- ✓ **Articles retained for Boldrin** as a depth-layer behind profile — 125 essays carry analytical reasoning that the profile's 5–10 representative quotes per topic cannot capture in full. Cited as `[Boldrin, articolo nFA, YYYY-MM-DD]` (Tier A2a personal voice).
- ✓ **Dialogues demoted** because they are fully absorbed into profile (`aggregator.py` docstring: profile sources are `nFA stance extracts + dialogue distillations` for Boldrin, `dialogue distillations only` for Forchielli). Every dialogue quote that mattered is in profile with a timestamped YouTube link-back; indexing dialogues separately would produce duplicate retrieval hits with no marginal information.
- ✗ Citations are to paraphrases in profile; attribution pill must say "curated summary" and surface the per-quote link-back. Mitigated by mandatory `type: leader_topic_profile` frontmatter.
- ✗ Distillation drift risk: if a leader publicly changes a stance, `profile/NN-topic.md` must be refreshed (re-run `aggregator.py`). Leader-corpus audit is currently out of scope (decision 18 F1 chose data-corpus-only for v1) — flag for v2.

### C — Both, with link-back
Distilled docs are retrievable AND carry pointers to specific source spans in primary materials. Bot retrieves the distillation, cites it, offers the underlying source on request.
- ✓ Dual-layer fidelity.
- ✗ Doubles ingestion plumbing; needs a span-anchoring mechanism not yet built.
- **Deferred:** evolve toward C if eval (decision 12) shows attribution complaints from users. For v1, B is enough.

**Recommendation taken:** B for v1, with C as a possible v2 once the eval framework can measure attribution-quality drift.

## Implications for adjacent decisions

- **Decision 04 (chunking):** the units to chunk for leaders are `profile/*.md` (typically short, topic-bounded — likely 1–3 chunks each), `dialogues/*.md` (medium-length distillations), `articles/*.md` (longer, opinionated — chunker must handle these as the largest leader unit). Raw transcripts and HTML bios do **not** need a chunking strategy because they're not chunked.
- **Decision 05/06 (embedding/vector store):** leader slice is bounded — ~50 profile docs + ~18 dialogue docs + 125 articles = ~190 docs across two leaders. Plus future interviews. Trivial scale.
- **Decision 07 (retrieval strategy):** Tier-2 gap-fill works cleanly because `profile/<NN>-topic.md` is keyed on tesi number. A simple tesi-number filter at retrieval time can implement the "fall through to leader when no Tier-1" rule.
- **Decision 10 (citation):** leader-slice citation pills must distinguish "Boldrin, articolo (2008)" from "Boldrin, profilo curato — Tesi 06". The `type` frontmatter already encodes this; citation rendering reads it.
- **Decision 18 (audit):** auditor v1 is data-corpus-only. Leader corpus audit (detecting when a distillation has drifted from the underlying primary material the leader has since updated) is a v2 candidate. Flag for revisit.
- **CLAUDE.md §7 drift item #1** ("Leader YouTube transcripts currently live in `memory/YoutubeScripts/`, not in `corpus/leaders/`"): partially resolved. The *distillations* are in the corpus, which is what gets retrieved. The *raw speaker-tagged transcripts* stay in YoutubeScripts as scaffolding by explicit Model-B design — they are not corpus. Drift item #1 should be reworded to reflect this: "joint-dialogue raw transcripts and solo-interview raw transcripts remain in YoutubeScripts/ as scaffolding for the curation pipeline; they enter the corpus only after distillation."

## Structural cleanup performed alongside this decision

Executed 2026-05-13:

- `boldrin/{ilpost,rochester-alumni,washu-profile,wikipedia}.html` → `boldrin/_raw/bios/`
- `forchielli/{about-personal-site,wikipedia}.html` → `forchielli/_raw/bios/`
- `boldrin/_raw/_old-profilo.md`, `forchielli/_raw/_old-profilo.md` → deleted
- `leaders/_raw-joint/` → `leaders/_raw/joint-dialogues/` (renamed for consistency with the "every corpus subfolder has a sibling `_raw/`" rule from CLAUDE.md §5)
- `YoutubeScripts/Michele/nFA articles/` → deleted (superseded stub)
- `YoutubeScripts/Michele/papers/` → deleted (out of scope)
- All 18 `<leader>/dialogues/*.md` files → `corpus_status: exclude` added to frontmatter. Files remain on disk as scaffolding for `aggregator.py` regeneration; indexer (once built) reads `corpus_status: include` only and will skip them.
- `<leader>/interviews/` slot abandoned (per pruning decision); raw `.txt` interviews remain in `YoutubeScripts/` as scaffolding but are not slated for ingestion.

## What this decision does NOT settle

- **Drift detection for distillations.** If a leader publicly changes a stance, when and how is `profile/NN-topic.md` refreshed? `aggregator.py` re-runs are manual today. Decision 18 covers drift detection for data corpus only; leader-corpus drift is unowned. Revisit after data-corpus auditor runs prove the pattern.
- **Article-vs-profile retrieval blending.** With both `profile/` and Boldrin's `articles/` retrievable, the same Boldrin stance can return: (a) the profile chunk (curated, terse, with quote pointers) and (b) the article chunk (full essay, more depth). Both are valid Tier A2a; the question is how decision 07 ranks them and whether the bot prefers profile-first with article as drill-down. Belongs in decision 07.
- **What happens to dialogues if we ever rebuild profiles from richer raw transcripts.** Dialogues stay on disk specifically so the curation pipeline can be re-run. If profile regeneration ever moves to source the speaker-tagged transcripts directly (skipping the per-leader dialogue distillation step), the `dialogues/` files become true dead weight. Not yet — current pipeline still consumes them via `aggregator.py`.

## Reference

- CLAUDE.md §3 (authority axis — A2 tier), §4 (sourcing — leader-as-personal-view discipline), §5 (corpus layout, `_raw/` rule), §7 (drift #1).
- Decision 03 (corpus trust hierarchy — A1 > A2 > A3, this decision operationalizes how A2 is indexed).
- Decision 10 (citation — pill rendering must read `type` frontmatter to label distillations correctly).
- Decision 18 (audit — leader-corpus audit deferred to v2).

**Source of decision:** Claude Code session 2026-05-13 with Riccardo. Riccardo's framing: "make some order in the leader folder for the project, as we are approaching the phase to prepare everything for rag. the structure of the folder should be essential and coherent with the chatbot objectives." Model B chosen first after A / B / C trade-offs ("okay with option b"). After investigation revealed that `dialogues/` content is fully absorbed into `profile/` (confirmed by `aggregator.py:9-13` and by inspection of profile frontmatter showing source dialogue/article counts), Riccardo agreed to prune the retrievable set to `profile/ + articles/` and demote `dialogues/` to scaffolding via `corpus_status: exclude`. Solo interviews dropped from corpus.
