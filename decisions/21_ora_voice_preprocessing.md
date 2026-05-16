# 21 — ORA voice (A1) corpus: preprocessing strategy

**Status:** DECIDED
**Decided on:** 2026-05-13
**Decision:** **No pre-RAG transformation of comunicati (A1b). Section-split + tesi-alignment tagging for newsletters (A1c), no aggregation.** Comunicati are kept byte-identical as one file per position — they are already short, single-topic, citation-bearing, and party-voiced; any pre-processing (summarization, trimming) would introduce paraphrase risk on a high-trust tier without compensating retrieval gain. Newsletters are split along their `##` section headers into per-section files; each section receives a `tesi_alignment: NN` (or `null` + `corpus_status: exclude` for operational/logistics noise) so the retriever can group sections by topic at query time via metadata filter. **No theme-aggregation cards are produced.** Tesi (A1a) are unchanged — they remain the canonical retrievable unit they have always been.

---

## Locked configuration

| Item | Choice |
|---|---|
| Tesi (A1a) | Unchanged. Each tesi file is one retrievable unit. No preprocessing. |
| Comunicati (A1b) | Unchanged. Each comunicato file is one retrievable unit. No summarization, no trimming. Structural cleanup of obvious scrape artifacts (empty `###` headers, mid-sentence PDF line breaks) is permitted as a mechanical pass but is **not** content-altering. |
| Newsletter (A1c) — retrievable unit | The **section** is the retrievable unit, not the newsletter. A section is the text under a single `##` header within a newsletter file. |
| Newsletter section-split rule | Split mechanically on `##` headers. For newsletters without `##` structure (e.g. early administrative ones like `2025-09-23.md`), fall back to whole-file-as-one-section; if the whole file is operational, mark `corpus_status: exclude` and don't split further. |
| Newsletter section frontmatter | Inherits from parent newsletter (`date_published`, `gmail_thread_id`, `source_note`, `co_speakers`) + adds: `parent_newsletter: <yyyy-mm-dd>`, `section_index: <int>`, `section_title: <raw H2 text>`, `tesi_alignment: <int \| null>`, `section_speaker: <slug \| null>`, `content_hash: <sha256 of section body>`, `corpus_status: include \| exclude`. |
| Source newsletter files | `corpus_status: exclude` after section-split. Kept on disk as the substrate for re-running the splitter; not chunked or retrieved. |
| Tagging method | One LLM call per section. Prompt: "given this newsletter section, return the tesi number (2–21) it most aligns with, or `null` if operational/logistics, plus a `section_speaker` slug if the section is a named-member Q&A or quoted statement." Same prompt template every week. |
| Exclusion criterion | `corpus_status: exclude` for: congresso logistics, iscrizioni/candidature procedures, eventi della settimana, "iscrivetevi alla newsletter" promo, pure video-link dumps without commentary, "Team Drin Drin" signoffs. Sections containing a stated position OR a member Q&A OR a quoted member statement → `include`. |
| `section_speaker` semantics | When set, the section's attribution stays `party` (the newsletter published it as such) but the retriever knows a named member is speaking — honors §4 divergence rule at section granularity. |
| Re-classification trigger | Section files are immutable once produced. If the splitter or the tagger prompt is improved later, re-run the pipeline from the source newsletter files (`corpus_status: exclude` substrate). Per-section `content_hash` detects drift. |
| Aggregation | **None.** No theme-rollup cards. No quarterly digests. Grouping is metadata-driven at query time via `tesi_alignment` filter, not file-driven. |

---

## The question

After locking decision 19 (leaders → distilled topic profiles) and decision 20 (other-parties → opportunistic topic-aligned cards), what is the preprocessing strategy for the **ORA-side primary voice** tiers — comunicati (A1b) and newsletters (A1c)? Two sub-questions, sometimes treated together because they're the same tier family:
1. Should comunicati be summarized or trimmed before retrieval?
2. Should newsletter content be split, tagged, aggregated by theme, or left whole?

## Why it matters

- **Faithfulness ceiling (CLAUDE.md §2).** A1 is the *party's official voice*. Any preprocessing that paraphrases re-writes ORA's voice in Claude's voice and gets cited back as party position. The faithfulness bar is higher here than for Tier-3 (other-parties), where decision 20 spent the distillation budget anyway.
- **Update frequency.** Comunicati arrive event-triggered, newsletters arrive **weekly**. Decision 20's "one-shot per cycle, amortized cost is low" defense does not transfer — any per-cycle distillation pipeline runs ~52 times per year and becomes ongoing ingestion friction (§7).
- **Heterogeneous within-file content (newsletters only).** A newsletter mixes 4–6 unrelated items: policy positions, member interviews, operational announcements, video link dumps, event invites. Indexing the whole file as one A1c unit pollutes retrieval — a query about Iran returns chunks that also mention congresso reiscrizioni.
- **A1/A2 boundary inside newsletters.** "Intervista a Francesco Mercuri" sections are published as party content but the speaker is one member. §4's divergence rule requires section-level granularity to honor — file-level frontmatter alone (`co_speakers: [...]`) is not enough.
- **Chronology as signal.** Newsletters are a time series of party emphasis. The fact that Iran came up in six newsletters across six months is itself signal about salience and evolution. Aggregating across time collapses the dimension newsletters uniquely contribute.

## Options considered

### Comunicati sub-decision

#### CA — Leave as-is ★ (chosen)
- ✓ Faithfulness preserved; numbered proposals stay verbatim.
- ✓ Citations and footnotes preserved (CPR comunicato has 24 footnotes load-bearing for objective 4).
- ✓ `content_hash` change-detection works cleanly (§8.1).
- ✓ Zero ingestion friction; new comunicati drop into the existing bucket.

#### CB — Light structural trimming (strip rhetorical preamble, keep proposals)
- ✗ Subjective ("what's rhetorical?"); risks deleting nuance.
- ✗ Adds a per-file curation step that grows linearly with corpus size.
- ✗ Whose voice did the trimming? — re-introduces the paraphrase problem.

#### CC — Summarize each comunicato into a position card
- ✗ Paraphrase on A1b tier — directly violates the faithfulness ceiling.
- ✗ Loses citations/footnotes used by objective 4.
- ✗ The comunicati ARE already digests of the party's position; summarizing summaries.

### Newsletter sub-decision

#### NA — Whole-file (one newsletter = one retrievable unit)
- ✗ A multi-topic file pollutes retrieval: a "what does ORA think about Iran?" query against `2026-01-10.md` pulls chunks mixed with Venezuela, Groenlandia, eventi della settimana.
- ✗ No place to hang `section_speaker` for Mercuri Q&A sections — §4 divergence rule unenforceable at this granularity.
- ✗ Operational/logistics content (congress logistics, "Team Drin Drin" signoffs) gets indexed as A1c policy content.

#### NB — Section-split + `tesi_alignment` metadata, no aggregation ★ (chosen)
- ✓ Each section is byte-identical to what ORA wrote; no paraphrase, no faithfulness cost.
- ✓ Operational sections excluded via `corpus_status: exclude` — same pattern as decision 19 used for leader dialogues.
- ✓ `tesi_alignment` filter at query time delivers the same user-facing retrieval shape as theme aggregation (decision 20 §77 established this as a first-class retrieval primitive).
- ✓ Chronology preserved at section granularity — supports §3 evolution flagging directly.
- ✓ `section_speaker` tag at section granularity honors §4 divergence rule.
- ✓ Weekly pipeline is bounded and stateless: split + tag the new newsletter only; yesterday's sections are never touched.
- ✗ More retrieval-time hits to rank (~85–140 retrievable sections vs ~28 whole-file units) — trivial at this scale.

#### NC — Full decision-20-style theme aggregation (cards per tesi, recomputed weekly)
- ✓ Maximum uniformity with leaders + other-parties.
- ✓ Single doc per tesi for cite-formatting symmetry.
- ✗ Recurring distillation cost: each weekly newsletter triggers re-merge into 3–5 tesi cards. ~260 LLM card-merge operations per year, each a potential drift point.
- ✗ Card `content_hash` churns every week on every card a new newsletter touches.
- ✗ Chronology collapses inside the card — the "six mentions in six months" signal becomes one stitched document.
- ✗ Directly violates §7's long-term ingestion rule (manual/LLM curation step per ingest forever).

#### ND — Time-windowed rollups (quarterly per-tesi rollups, sections stay raw)
- ✓ Bounds re-distillation to ~4×/year × N topics.
- ✗ Two-layer corpus (sections + rollups) introduces a precedence question: which is the citation source for objective 1 answers?
- ✗ Most of NC's value, none of NB's simplicity. **Deferred** — evolve toward ND only if eval (decision 12) shows NB lacks the synthesis-style retrieval the bot needs.

## Implications for adjacent decisions

- **Decision 04 (chunking, OPEN).** Comunicato chunking unit is the whole `.md` file (1–3 chunks of structure-aware segmentation, respecting `##` / `###` headers and keeping numbered proposals cohesive). Newsletter chunking unit is the section `.md` file (most sections fit in 1 chunk; longer sections may need 2). The chunker must respect `corpus_status: exclude` and skip those files entirely.
- **Decision 06 (vector store, OPEN).** A1 slice = ~20 tesi + ~26 comunicati + ~85–140 newsletter sections ≈ 130–185 retrievable units. Combined with the corpus-wide figures from decision 20 §76, total ORA-side ≈ 175–230 units. No driver of vector-store choice.
- **Decision 07 (retrieval strategy, OPEN).** `tesi_alignment` becomes a corpus-wide metadata primitive: a single filter on `tesi_alignment: 6` pulls Tesi 06 (A1a) + any comunicato categorized as Energia + any newsletter section tagged 6 + Boldrin/Forchielli profile 06 + other-parties profile-06 cards in one shot. The decision 20 §77 vision now extends across all four tiers.
- **Decision 10 (citation, DECIDED).** Newsletter section citations read as `[ORA, newsletter del 2026-01-10 — sezione "Iran"]`. When `section_speaker` is set: `[Francesco Mercuri (Consiglio Direttivo ORA), newsletter del 2026-01-10 — sezione "Piano di pace in Ucraina"]`. Distinguishable from the comunicato format `[ORA, comunicato — "<title>"]` and the tesi format `[ORA, Tesi NN — <slug>]`.
- **Decision 11 (guardrails, PARTIAL).** Refusal rule is unchanged. Section-level granularity lets the bot more accurately disambiguate "ORA's documented position" vs "a member's view published in the party newsletter" — the latter no longer surfaces under the party-position rubric without flagging.
- **Decision 13 (freshness, DECIDED).** Newsletter ingestion pipeline becomes: scrape → write canonical newsletter file (`corpus_status: exclude`) → split into section files → LLM-tag each section → indexer picks up new section files. Comunicati pipeline unchanged.
- **Decision 18 (audit, DECIDED).** Out of scope for v1 (data-corpus audit only). Newsletter section-tag drift (a section tagged tesi 6 but actually about tesi 11) is a v2 audit candidate alongside leader-card and party-card audits.
- **CLAUDE.md §5 schema.** New `type: newsletter_section` (parallel to `leader_topic_profile` and `party_topic_profile`). Existing `type: newsletter` stays for the source files (now `corpus_status: exclude`).

## Source mapping for newsletter section-split

Pipeline applied per newsletter file in `memory/corpus/ora-party/newsletter/`:

1. Read source `.md`. If `corpus_status: exclude` already set, skip.
2. Mechanical split on `##` headers. Fallback: if zero `##` headers, treat whole file as one section.
3. For each section: derive section frontmatter from parent + LLM tag call returning `(tesi_alignment, section_speaker, corpus_status)`.
4. Write section file as `newsletter-sections/<parent-date>__<NN-section-index>__<slug-from-h2>.md`.
5. Mutate source newsletter frontmatter: add `corpus_status: exclude` and `sections_extracted: <count>`.

Section-file naming detail (target — to confirm at implementation time):
- Slug derived from H2 text, normalized (lowercased, accents stripped, spaces → hyphens, truncated to ~40 chars).
- Example: `2026-01-10__01__verso-il-2026.md`, `2026-01-10__02__venezuela.md`, `2026-01-10__03__groenlandia-mercuri.md`, `2026-01-10__04__iran.md`, `2026-01-10__05__eventi-della-settimana.md` (last one `corpus_status: exclude`).

## Section frontmatter (target)

```yaml
---
id: <parent-date>__<section-index>__<slug>
type: newsletter_section
attribution: party
parent_newsletter: <yyyy-mm-dd>
section_index: <int>
section_title: "<raw H2 text>"
tesi_alignment: <int | null>          # 2-21 when aligned to a tesi; null otherwise
section_speaker: <slug | null>        # named member if section is Q&A or quoted statement
title: "<parent newsletter title> — <section title>"
date_published: <inherited from parent>
date_scraped: <inherited from parent>
gmail_thread_id: <inherited from parent>
source_note: <inherited from parent>
content_hash: <sha256 of section body>
corpus_status: include | exclude
---
```

## Structural cleanup performed alongside this decision

To be executed during section-split rollout (one-shot pipeline):

- For each of the 28 newsletter files: run splitter, write section files, mutate parent frontmatter to `corpus_status: exclude`.
- For each of the 26 comunicato files: optional mechanical cleanup of obvious PDF/scrape artifacts (empty `###` headers like the two in `cpr-extrema-ratio-migratoria.md` lines 18–20, mid-sentence line breaks). No content alteration. Recompute `content_hash` only on files actually touched.
- CLAUDE.md §5 stale notes about newsletters lacking frontmatter should be updated separately — newsletters already have frontmatter post the prior migration; this decision file is not the place to fix that.

## Riccardo's stated rationale (verbatim)

On comunicati:
> "agree"

On newsletters, after weighing aggregation against section-split with metadata tagging:
> "agree on section spearker. but what if we groupe the newseletters different subjects by theme?"
> "can you explain in simpler words option b? i would say that the process going forward should be as automatic as possible"
> "let's do that"

Interpretation locked: the deciding constraint was ongoing ingestion automation. Theme-aggregation (option NC) was rejected because it would require an LLM merge step every week and weekly content_hash churn on every theme card a new newsletter touches. Section-split + metadata tagging (option NB) was chosen because the weekly pipeline becomes a fixed two-step script (split + tag) over the newly-arrived newsletter only; older sections are never re-touched. The "grouping by theme" user-facing benefit is delivered at query time via metadata filter on `tesi_alignment`, not at file-creation time via static aggregation.
