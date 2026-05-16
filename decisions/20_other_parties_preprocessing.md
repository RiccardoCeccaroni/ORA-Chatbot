# 20 — Other-parties corpus: preprocessing into topic-aligned profiles

**Status:** DECIDED
**Decided on:** 2026-05-13
**Decision:** **Opportunistic topic-aligned distillation, per party, pooled across all sources.** For each of the 8 other parties (PD, M5S, FdI, Lega, FI, AVS, Azione, IV), the retrievable units are curated topic-aligned cards under `<party>/profile/`, distilled from that party's **pooled** corpus sources: the party's own programme(s) (2022 general + 2024 europee where present), the joint coalition programme(s) the party signed (CDX 2022, TP 2022, SUE 2024 as applicable), and the party's Italian Wikipedia page. **Cards are produced only where the pooled sources have substantive content** on a topic — no padding, no forced symmetry across parties. Each party also gets **one identity card** (`00-identita.md`) covering history, ideology, current leader, coalition affiliations, EU group. **Web search is allowed as a fallback** when the corpus is silent or fragmentary on a topic. Original source files (programmes + wiki + joint docs) are demoted to `corpus_status: exclude` (scaffolding) — they remain on disk as the substrate for re-distillation but are not chunked or retrieved.

---

## Locked configuration

| Item | Choice |
|---|---|
| Retrievable for other-parties | `<party>/profile/*.md` only |
| Card naming | Mirrors ORA tesi taxonomy: `NN-<slug>.md` for tesi 02–21, `00-identita.md` for the identity card, `altro--<slug>.md` for substantive off-tesi positions |
| Card content type | New frontmatter `type: party_topic_profile` (parallel to `leader_topic_profile` from decision 19) |
| Source pooling rule | Per party, all available sources are pooled before distillation: own programme(s) + signed joint coalition programme(s) + own Wikipedia page |
| Coalition joint docs | `corpus_status: exclude`. Their content reaches retrieval **only** via the member parties' profile cards. CDX 2022 → FdI/Lega/FI cards; TP 2022 → Azione/IV cards; SUE 2024 → IV cards |
| Originals (programmes + wiki) | `corpus_status: exclude` once distillation is complete. Kept on disk as `_raw/` substrate and for re-distillation if upstream changes |
| Gap policy | If a party has no substantive content on a topic, **no card is produced** — leaving a structural gap is the correct signal that "the party has not staked out this position" |
| Web-search fallback | Allowed when pooled corpus sources are silent or too fragmentary on a topic. Web-sourced quotes are tagged distinctly in the card (`source_type: web`) and cite the URL + fetch date. Hierarchy: party's own site → official press release → reputable interview/reportage. **Not** opinion journalism or third-party fact-checkers. |
| Card body format | Strict mirror of leader `profile/`: H1 title, `## Sintesi` (1–2 paragraph topic framer), `## Posizioni documentate` with numbered sub-positions, each containing verbatim source quotes formatted as `> «…» — *[source, date, link]*`. **No LLM-original prose** outside the Sintesi framer. |
| OCR-quality caveat | `lega-2024-europee.md` source is OCR'd with artifacts. Distilling Lega's 2024 EU positions will rely partly on the OCR cache and partly on web fallback for quote precision. |
| Production method | **One subagent per party** (8 parallel agents), each given a self-contained prompt with: the party's source file paths, the tesi taxonomy, the card-format spec, web-search permission, and the output target folder. Same prompt template for all 8 — only party-specific paths differ. |
| Re-distillation trigger | When a source's `content_hash` changes (upstream programme republished, wiki edited), the affected party's profile cards are re-generated. Audit deferred to v2. |

---

## The question

After scraping the other-parties corpus into 25 canonical source files (decision-of-record: §5 of CLAUDE.md, executed 2026-05-13), what is the **retrievable unit** that the chatbot's comparison engine (CLAUDE.md objective 4) consults? Treating each source programme as one retrieval target is the cheapest path but creates a structural asymmetry against ORA's fine-grained tesi-aligned corpus. Treating each tesi topic per party as a retrieval target requires distillation work but matches ORA's shape and makes comparison answers natively parallel.

## Why it matters

- **Asymmetry against the ORA side.** ORA's manifesto is 20 tesi (avg ~28 KB each, single-topic). Leader profiles mirror this (decision 19 — `<leader>/profile/NN-<slug>.md`). Other-parties programmes are monolithic — Lega 2022 alone is 553 KB covering every topic. Naïve symmetric retrieval will return one tight tesi-aligned chunk for ORA and three scattered fragments from a sprawling PD programme. The bot's comparison answers will look lopsided.
- **Faithfulness and citation (CLAUDE.md §4).** "Always say which tier and which document — which tesi, which comunicato, which leader, which press piece, which web result." Card-form distillation makes citation pills natural: `[PD, profilo curato — Programma 2022, sez. 3.4]` vs scrambled chunk-citations.
- **Joint-doc duplication.** TP 2022 and SUE 2024 currently exist byte-identically in `coalitions/` and in each member's folder. Indexing the originals would multiply retrieval hits 3× for the same content. Pooling at distillation collapses this naturally — TP 2022's content reaches retrieval once, through each signatory's card, in topic-keyed form.
- **OCR quality recovery.** `lega-2024-europee.md` is 12 KB of artifact-laden OCR (Cyrillic intrusions, mashed words). Indexing it directly puts polluted tokens into the retriever. Distillation passes can selectively extract the substantive sentences and skip the slogan/header artifacts; web fallback can fill what the OCR mangled.
- **Long-lived product (CLAUDE.md §2).** Parties don't update programmes more often than every 4–5 years. Distillation is one-shot per cycle. The amortized cost is low.
- **Parallelism (Riccardo's directive, 2026-05-13):** "to speed up the process, i would create an agent for each party we have. same process for each." Eight parallel subagents producing ~100 cards total in one wall-clock pass, vs a sequential script that would take 8× longer.

## Options considered

### A — Chunk the raw files, no distillation
The 25 source `.md` files become retrieval targets directly. Standard chunker handles them.
- ✓ Cheapest path; zero preprocessing cost.
- ✗ Locks in the asymmetry against ORA's tesi-aligned shape.
- ✗ Joint-doc duplicates would need a retrieval-time dedup layer.
- ✗ Lega 2024 OCR artifacts enter the index unfiltered.
- ✗ No clean citation pill mapping ("PD on energy" is a chunk anywhere in 122 KB of PD programme text).

### B — Forced symmetric distillation (every party × every tesi)
8 parties × 20 tesi = 160 mandatory cards, plus identity. Each card is generated whether or not the source has content.
- ✗ Produces empty / padded cards for parties silent on a topic — manufactures false content to fill structural symmetry.
- ✗ Imposes ORA's taxonomy on parties that frame issues differently (e.g., PD's "transizione ecologica" forced into ORA's "energia" frame).
- ✗ Expensive without compensating quality gain.

### C — Opportunistic distillation, pooled per party ★ (chosen)
Per party, pool all available sources; iterate over the tesi taxonomy; produce a card only where pooled sources have substantive content; add `altro--*` cards for substantive non-tesi positions; allow web fallback for gaps. Decision 19's leader-profile pattern, applied to parties.
- ✓ Cards produced reflect actual party content — gaps are signal, not bug ("the party has not staked out this position").
- ✓ Native symmetry with ORA and leader corpora — all three tiers retrievable by tesi number.
- ✓ Joint-doc duplication collapses (TP 2022 quotes appear once, in each signatory's card).
- ✓ OCR pollution is contained — distillation extracts substantive quotes and skips artifacts; web fills what's mangled.
- ✓ Citation pills natural: `[PD, profilo — Programma 2022, sez. 3.4]`.
- ✗ Distillation cost (~100 cards via LLM); summarizer-drift risk — mitigated by the verbatim-quote-only body rule.
- ✗ Adds a regeneration step when sources update; audit of card-drift deferred to v2 (decision 18 set the audit precedent for data; leader & party audits are v2 candidates).

### D — Hybrid: opportunistic cards + raw also indexed
Cards as in C, **plus** the source programmes remain `corpus_status: include` for verbatim/fallback retrieval.
- ✓ Two-layer fidelity — cards for comparison-style answers, raw for verbatim quotes.
- ✗ Duplicates retrieval work; joint-doc dedup problem returns.
- **Deferred** — evolve toward D only if eval (decision 12) shows the cards lose nuance the bot needs for objective 1 (State) answers. For v1, C is enough.

## Implications for adjacent decisions

- **Decision 04 (chunking, OPEN).** Other-parties chunking unit is the `profile/*.md` card. Each card is small (5–15 KB) and topically bounded — likely 1–3 chunks per card. Raw programmes/wiki are not chunked.
- **Decision 06 (vector store, OPEN).** Other-parties slice = ~100 cards. Plus ORA manifesto (20) + leaders profile (~47) + ORA comunicati (~80) + newsletters (~52) = trivial scale; no driver of vector-store choice.
- **Decision 07 (retrieval strategy, OPEN).** Metadata filter on `tesi_number` becomes a first-class retrieval primitive: "user asks about energy → retrieve `tesi_number: 6` across ORA + leaders + other-parties in one shot, ranked." This pre-filter dramatically narrows candidate set and improves comparison-answer quality.
- **Decision 10 (citation, DECIDED).** Citation pills for other-parties read as `[<party>, profilo — <source>, <date>]` for corpus-sourced quotes and `[<party>, web — <url>, <fetch-date>]` for web-fallback quotes. Distinguishable in the UI.
- **Decision 11 (guardrails, PARTIAL).** Refusal rule unchanged ("ORA non ha una posizione documentata su questo" → also "<party> non ha una posizione documentata su questo" by symmetry, when card is absent for that party + topic).
- **Decision 13 (freshness, DECIDED).** Re-distillation triggered when a source `content_hash` changes. The mechanism is the same as decision 13's update path — only the trigger is new (source-hash-change as proxy for "stance may have evolved").
- **Decision 18 (audit, DECIDED).** Audit v1 is data-corpus-only. Party-card audit (detecting drift between a card's quotes and the party's current public position) is a v2 candidate alongside leader-card audit.
- **CLAUDE.md §4 sourcing rules.** The comparison engine (objective 4) gets a tesi-keyed corpus on the other-parties side, complementing live web search. The rule "Tier-3 (live web search) is the comparison engine" remains true at runtime; the curated other-parties corpus is the slow-moving floor it complements.
- **CLAUDE.md §5 schema.** New `type: party_topic_profile`. The schema is already extensible per the `<source-slug>` and `<party-slug>` attribution rules — no further schema migration needed beyond the type list.

## Source mapping for distillation (per-party pooled sources)

| Party | Own programmes | Joint doc(s) signed | Wikipedia | Notes |
|---|---|---|---|---|
| PD | pd-2022-programma, pd-2024-europee | — | pd-wikipedia | Standalone in both cycles |
| M5S | — | — | m5s-wikipedia | **Identity card only.** 2022 + 2024 programmes excluded (no fetchable canonical source). Cards beyond identity rely entirely on web fallback. |
| FdI | fdi-2022-programma, fdi-2024-europee | cdx-2022-programma | fdi-wikipedia | |
| Lega | lega-2022-programma, lega-2024-europee | cdx-2022-programma | lega-wikipedia | Lega 2024 source is OCR'd (low quality); web fallback expected to carry most 2024 EU content. |
| FI | fi-2022-programma, fi-2024-europee | cdx-2022-programma | fi-wikipedia | FI 2022 is OCR'd (acceptable quality). |
| AVS | avs-2022-programma, avs-2024-europee | — | avs-wikipedia | Standalone in both cycles |
| Azione | (no solo 2022) azione-2024-europee | tp-2022-programma | azione-wikipedia | 2022 content drawn entirely from TP joint doc |
| IV | (no solo 2022) (no solo 2024) | tp-2022-programma, sue-2024-programma | iv-wikipedia | All programmatic content drawn from joint docs |

## Card frontmatter (target)

```yaml
---
id: <party>--<topic-slug>           # e.g., pd--energia-ambiente-sostenibilita
type: party_topic_profile
attribution: <party-slug>           # pd | m5s | fdi | lega | fi | avs | azione | iv
topic_slug: <topic-slug>            # matches tesi slug, or altro--<slug>, or identita
tesi_number: <int>                  # 0 for identita, 2-21 for tesi, omit for altro--
tesi_aligned: true | false          # true when tesi_number is set
sources:
  programmes: [<source-id list>]    # e.g., [pd-2022-programma, pd-2024-europee]
  joint: [<joint-doc-id list>]      # e.g., [cdx-2022-programma]
  wikipedia: [<wiki-id list>]       # e.g., [pd-wikipedia]
  web: <int>                        # count of web-sourced quotes; absent if 0
date_compiled: YYYY-MM-DD
date_range: "YYYY-MM-DD to YYYY-MM-DD"  # range of source dates referenced
content_hash: <sha256-of-body>
corpus_status: include
---
```

## Structural cleanup performed alongside this decision

To be executed during distillation rollout (subagent-driven):

- For each of the 25 source `.md` files under `other-parties/`: add `corpus_status: exclude` to frontmatter (becomes scaffolding for the cards).
- Joint coalition docs in `coalitions/` likewise get `corpus_status: exclude`.
- Re-OCR `lega-2024-europee.pdf` is **not** gated on by this decision: distillation will use the existing 12 KB OCR cache plus web fallback for the 2024 EU material. If output quality is unacceptable, re-OCR and re-distill Lega cards only.
- Each subagent reports: cards produced, topics skipped (gap), web-fallback usage per card.

## Riccardo's stated rationale (verbatim)

> "i believe that not all the 19 decisions card could be adressed in each party. so probably we should try to summarise for what we have"
> "i would not do the differentiation on the 2022 or 2024, rather i would divide the information we have for each party, including any source we have, divided into the different subjects. … keeping of course one or two cards about the identity and general info of the party"
> "if you don't find any importatn information about any of the party, you are allowed to do a serach on the web. to speed up the process, i would create an agent for each party we have. same process for each"

Interpretation locked: "not all tesi topics will have content for every party — distill what's there. Pool 2022 and 2024 sources (and joint docs) per party — don't shard by election cycle. One or two identity cards per party for general info. Web fallback for gaps. One parallel agent per party, same process."
