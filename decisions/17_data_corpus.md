# 17 — Data corpus (empirical evidence)

**Status:** DECIDED
**Decided on:** 2026-05-11
**Decision:**

- **Pre-ingest a curated `memory/corpus/data/` corpus as a *supplement* to live retrieval, not a replacement.** Live retrieval from §4 sources remains allowed for (a) very recent stats not yet captured, (b) drill-downs the bot doesn't have a card for, (c) verification.
- **Quality tier hierarchy (D1–D4):**
  - **D1 — Official statistics & central banks.** ISTAT, Eurostat, OECD, Banca d'Italia (statistical releases), MEF, MIMIT, ISS, ECB, IMF, World Bank, UN agencies, national statistical offices of other EU states (for comparison).
  - **D2 — Supranational / public research bodies.** Bruegel, CEPR, EU Commission JRC, ECB Working Papers, Banca d'Italia Temi di discussione & Questioni di economia e finanza, OECD Working Papers, IMF Working Papers.
  - **D3 — Peer-reviewed academic publications.** Italian or international journals; preprints only when the underlying paper is later peer-reviewed (record the published version when available).
  - **D4 — Reputable, bias-tagged think tanks.** Examples: Osservatorio Conti Pubblici Italiani (Cottarelli), Istituto Carlo Cattaneo, Fondazione Hume, Fondazione FEEM. Each D4 source carries an explicit `bias_tag` in frontmatter (e.g., `centrist`, `liberal`, `social-democratic`); the bot surfaces the bias when citing.
  - **Excluded:** general press (no original data), opinion outlets, partisan policy shops, advocacy NGOs publishing their own unaudited data, Confindustria/CGIL/etc. when functioning as lobbying voices. (When such a body publishes a clearly methodological empirical study, treat as D4 with explicit bias tag — do not auto-exclude.)
- **Scope: comprehensive across all 21 tesi areas** (20 present + `agricoltura` placeholder; see §8.3). Topic folders are created up-front; population is gradual.
- **Taxonomy: topic folders + stat-card units.**
  - **Topic folders** mirror the 21 tesi (canonical slug list below), with `_raw/` as a sibling at the `data/` root.
  - **Stat-cards:** one `.md` per metric × period × source. Body contains the number(s), methodology note, caveats from the original, and a one-paragraph plain-Italian gloss. Frontmatter carries full provenance.
  - **Cross-cutting stats** live under their *primary* topic and enumerate the others in `tags`. No duplication — single source of truth, content_hash stays stable.
- **`_raw/` cold archive organized by source agency, not by topic.** Provenance-shaped, because a single source PDF spawns many stat-cards across many topics.

**Posture on contradicting data (objective 3 — Justify):**
When empirical data is mixed or contradicts ORA's documented position, the bot **surfaces the tension explicitly**: cites the position (with tier label), cites the data (with quality tier and source), names the divergence. Never silently elide either side. This is the operationalization of *Justify* when justification cuts against the party.

**Rationale:**

- **Pre-ingest as supplement (not replacement):** live retrieval alone re-pays latency on every query, exposes us to upstream outages, and produces non-deterministic citations. Pre-ingesting the canonical stats most policy questions touch buys reliability and citation precision; live retrieval still handles freshness and long-tail asks. The two compose.
- **Tiered hierarchy parallels A1–A3:** mirrors §3's two-axis design — there's *whose voice* (authority) and *whose number* (quality). Keeping them parallel keeps the bot's citation language consistent ("Tesi 14 (A1a) + ISTAT 2024 (D1)").
- **Stat-cards over whole-report MDs:** the bot's data-retrieval tool should return *one empirical claim with provenance*, not a chunk of a 200-page report. Whole-report MDs reintroduce the hallucination surface RAG is meant to eliminate, because the agent ends up extracting numbers from prose. The §5 schema's `data_period` and `data_metric` are already per-stat fields — the schema implicitly endorses this model.
- **Topic folders over source folders:** the chatbot reasons by policy area, not by publishing agency. Topic is the retrieval axis; source is a filter (frontmatter).
- **Comprehensive scope:** half the value of the data corpus is *being able to cite for objective 3 across every position the party holds*. Partial coverage means uneven trustworthiness.
- **Contradicting-data posture:** intellectually honest, and the only posture compatible with objective 3 + the third-person encyclopedic voice (decision 16). The alternative — only citing data that supports ORA — would convert the bot from research assistant into advocacy tool and destroy the trust premise the whole project depends on.

**Implications carried by this decision:**

1. **Persona patch (CLAUDE.md §4, Sourcing).** **APPLIED 2026-05-11** — see canonical wording below.
2. **Frontmatter schema patch (CLAUDE.md §5).** **APPLIED 2026-05-11** — `quality_tier` (required for `type=data`), `bias_tag` (required when `quality_tier=D4`), `source_doc` (free-text parent report title). See block below.
3. **`§9` table.** New row for decision 17 — flipped to DECIDED in the same edit as this file lands.
4. **Topic-slug taxonomy locked** — canonical list below.
5. **Extraction pipeline needed.** Raw report (PDF/HTML/CSV) → N stat-cards. Heavier upfront than dumping PDFs whole; payback in citation precision. Not yet designed.
6. **Agentic tool design.** The agent's `data_lookup` tool returns stat-cards (each a single empirical claim with full provenance), not retrieved chunks of larger documents. Filterable by topic, period, quality_tier, source.
7. **Frontmatter migration (§8.1) ordering.** Schema migration should run before mass data ingestion, so the data folder is born under the unified schema instead of needing its own re-migration later.

---

## Persona patch (APPLIED 2026-05-11 — canonical wording in CLAUDE.md §4)

Appended after the existing "**Data.**" bullet in §4 "Sourcing":

> - **Contradicting data.** The data tier (`memory/corpus/data/`) is the authoritative reasoner on empirical questions. When evidence across high-tier sources (D1, D2, well-supported D3) contradicts an empirical claim embedded in ORA's documented position, the bot **defers to the data**: cite the position [Tesi NN], cite the data (with quality tier and source), and name the divergence. **Carve empirical premise from values stance:** when a position rests on both an empirical claim and a values judgment, flag the tension on the premise without auto-invalidating the values dimension — the data alone doesn't adjudicate values choices. When evidence is genuinely mixed, present the mix honestly and label it as such. The bot does not defend an empirical claim the evidence body does not support.

**Why this wording (option B over the simpler "data wins"):** option A collapsed both layers and risked over-reach on positions whose values dimension survives an empirical correction. Option B (chosen) preserves "data is the referee" on empirical claims while leaving values judgments standing. See "Example phrasings" below.

### Example phrasings (illustrating the carve-out)

Positions in these examples are **hypothetical** — used to illustrate the answer pattern, not to assert ORA's actual stance.

**Empirical-only question** (e.g., "qual è il valore del sommerso?"):

> Secondo i dati ISTAT 2024 (D1), l'economia non osservata vale circa 180-200 miliardi di euro (~10-12% del PIL). ORA cita una cifra superiore [Tesi 19]; il dato ISTAT più recente è quello sopra.

**Position with both empirical premise and values stance** (e.g., "Cosa pensa ORA del reddito di cittadinanza?"):

> ORA si è espressa contro il reddito di cittadinanza [Tesi 14]. Tra le motivazioni: una preferenza per strumenti di sostegno legati al lavoro rispetto a trasferimenti incondizionati (scelta di policy), e una stima di forte disincentivo al lavoro (-10%+). I dati di INPS 2023 e Banca d'Italia 2024 (D1) indicano un effetto reale ma molto più contenuto (~2-4%). **La premessa empirica risulta sovrastimata**; la preferenza più ampia per strumenti work-related resta una scelta valoriale che i dati da soli non risolvono.

**Genuinely mixed evidence**:

> Sulla domanda X, l'evidenza è mista: studi A e B (D2/D3) trovano Y; studi C e D trovano Z. ORA si è schierata su [Tesi NN]. Non c'è un consenso empirico che adjudichi tra le posizioni.

---

## Frontmatter schema patch (APPLIED 2026-05-11 to CLAUDE.md §5)

The `# type=data only` block in §5 now reads:

```yaml
# type=data only
data_period: "2024" | "Q1 2025"
data_metric: "tasso di occupazione"
quality_tier: D1 | D2 | D3 | D4          # required for type=data
bias_tag: <orientation-slug>             # required when quality_tier=D4
source_doc: "<parent report title>"      # parent report (distinct from source_url which points to specific table/page)
```

**`source_doc` rationale:** free-text v1 — cheap to include, with two concrete uses: citation grouping ("ISTAT Rapporto Annuale 2025, tabelle 3 e 7") and finding sibling stats during ingestion. If title drift becomes a problem we promote to a structured registry later.

**Held back deliberately (not in v1):** `series_id` (time-series linking), `supersedes` / `superseded_by` (revision tracking), `unit` (%, EUR, persons), `geographic_scope` (Italy / EU / region). All four are non-breaking to add later — adding them prematurely costs every scraper and every migration step. Add on concrete need.

---

## Canonical topic slug list (locked)

Slugs strip the leading tesi number — the numbering is a manifesto ordering, not a topical one, and the data folder must be navigable without memorizing tesi numbers. One slug = one folder under `data/`.

| # | slug | tesi presence |
|---|------|---------------|
| 01 | `agricoltura` | **MISSING from manifesto (§8.3)** — folder created anyway; data ingestion proceeds independently |
| 02 | `comuni-province-regioni` | present |
| 03 | `cultura-sport-turismo` | present |
| 04 | `difesa` | present |
| 05 | `diritti-civili` | present |
| 06 | `energia-ambiente-sostenibilita` | present |
| 07 | `esteri-relazioni-internazionali` | present |
| 08 | `giustizia` | present |
| 09 | `governance-riforme-istituzionali-elettorali` | present |
| 10 | `immigrazione` | present |
| 11 | `infrastrutture-trasporti-mobilita` | present |
| 12 | `innovazione-crescita` | present |
| 13 | `istruzione` | present |
| 14 | `lavoro-politiche-sociali` | present |
| 15 | `pari-opportunita-inclusione` | present |
| 16 | `salute-servizi-sanitari` | present |
| 17 | `spesa-pubblica` | present |
| 18 | `sviluppo-economico-politica-industriale` | present |
| 19 | `tassazione-fiscalita` | present |
| 20 | `unione-europea` | present |
| 21 | `universita-ricerca` | present |

Final layout:

```
memory/corpus/data/
├── agricoltura/
├── comuni-province-regioni/
├── ...
├── universita-ricerca/
└── _raw/
    ├── istat/
    ├── eurostat/
    ├── oecd/
    ├── bankitalia/
    ├── mef/
    ├── iss/
    ├── ecb/
    └── ...
```

---

## Example stat-card

`memory/corpus/data/lavoro-politiche-sociali/tasso-occupazione-italia-2024.md`

```yaml
---
id: tasso-occupazione-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Tasso di occupazione, Italia, 15-64 anni, 2024"
data_metric: "tasso di occupazione 15-64"
data_period: "2024"
source_url: "https://dati.istat.it/Index.aspx?DataSetCode=DCCV_TAXOCCU1"
source_doc: "Rilevazione sulle forze di lavoro — ISTAT 2024"
date_published: "2025-02-28"
date_scraped: "2026-05-11"
content_hash: "sha256:..."
tags: [lavoro-politiche-sociali, sviluppo-economico-politica-industriale]
description: "Tasso di occupazione 15-64 anni in Italia, media annua 2024."
---

# Tasso di occupazione, Italia, 15-64 anni, 2024

**Valore:** 62,2% (media annua 2024).
**Confronto:** +0,9 p.p. rispetto al 2023; ~10 p.p. sotto la media UE-27.

## Metodologia
Rilevazione sulle forze di lavoro (RFL), ISTAT. Definizione armonizzata Eurostat (LFS).
Popolazione di riferimento: residenti 15-64 anni.

## Caveat
Il dato medio nasconde un gap di genere (uomini 70,4% / donne 53,5%) e un divario territoriale Nord/Sud (~20 p.p.).
```

---

## The question (recap)

How should the bot ground empirical claims — facts, numbers, comparisons — given §4's commitment to never invent numbers and to cite ISTAT/Bankitalia/MEF/Eurostat/ISS/OECD as primary sources?

The question is non-trivial because it intersects four things at once:
1. **Pre-ingest vs live retrieval** (§4 originally said live-only).
2. **Quality hierarchy for empirical sources** (separate from the authority hierarchy of §3).
3. **Unit of ingestion** (whole report vs stat-card).
4. **What the bot does when data contradicts ORA's stated position** (objective 3 with the gun pointed at the party).

## Why it matters for the ORA chatbot

- Objective 3 (Justify) is unbuildable without an empirical layer. The bot needs to motivate stances with data on empirical disputes.
- Objective 4 (Compare) needs comparable cross-party numbers — ORA spending policy vs PD spending policy is meaningless without a shared denominator.
- Hallucinated numbers are the single most reputation-destroying failure mode for a political bot. Stat-card precision + tiered citation is the structural defense.
- The "support OR contradict" posture is what separates a research assistant from a propaganda surface. This decision encodes that distinction.

## Options considered

### A — Live retrieval only (status quo per §4)
- Pros: zero pre-ingest work; always fresh.
- Cons: latency + cost on every query; non-deterministic citations; upstream outages break the bot; no pre-computed defense against contested numbers.

### B — Pre-ingest only (full data corpus, no live retrieval)
- Pros: deterministic, fast, fully offline-reasoning.
- Cons: stale on day one for any breaking stat; impossible to cover the long tail of policy-specific drill-downs comprehensively.

### C — Hybrid: pre-ingest core + live retrieval supplement *(chosen)*
- Pros: best of both. Canonical stats are pre-ingested as stat-cards with stable citations; live retrieval handles freshness and long-tail. Cost trade-off (§3) already accepted.
- Cons: two retrieval paths to maintain; the agent has to decide which to call.

### D — Document-level MDs vs stat-cards
Sub-question, independent of A/B/C. Stat-cards chosen for the reasons above.

## Open follow-ups

- ✅ ~~Apply persona patch to CLAUDE.md §4~~ — APPLIED 2026-05-11 (option B wording).
- ✅ ~~Apply schema patch to CLAUDE.md §5~~ — APPLIED 2026-05-11 (`quality_tier`, `bias_tag`, `source_doc`).
- **D4 think-tank shortlist** with explicit bias tags — needs a small research pass before any D4 source is ingested.
- **Extraction pipeline design** (raw → stat-cards) — separate decision/spec, not blocking on this one.
- **`data_lookup` tool design** for the agent — separate decision, but shape constrained by stat-card model.
- **Ordering with §8.1** — frontmatter migration runs *before* mass data ingestion, so the data folder is born clean.

## Reference

- CLAUDE.md §3 (retrieval design — two-axis), §4 (sourcing & persona), §5 (frontmatter schema).
- decision 03 (corpus trust hierarchy — A1/A2/A3 — parallel structure for D1–D4).
- decision 10 (citation format — visible source pills, tier-labeled).
- decision 16 (persona — third-person encyclopedic; constrains how "contradicting data" is phrased).
- KB concepts (Agentic_RAG wiki): `08_grounding_and_citation.md`, `15_political_chatbot_application.md`. Riccardo to confirm any additional relevant pages.

## Observations

- The §5 schema already includes `data_period`, `data_metric`, and `attribution: <agency-slug>` for `type=data` — implicit endorsement of the stat-card model.
- 01-agricoltura tesi missing (§8.3) but the data folder is not gated on tesi presence — agriculture data ingestion proceeds independently. When the tesi lands, attribution links resolve cleanly.
- `_raw/` cold archive at the `data/` root mirrors the §5 "every corpus subfolder has a sibling `_raw/`" rule, with the source-agency layout being the data-specific instantiation of that rule.
- This decision interacts with §8.1 (frontmatter migration): the new `quality_tier` / `bias_tag` / `source_doc` fields must be included in the migration target schema before mass data ingestion begins.

**Source of decision:** Claude Code session 2026-05-11 with Riccardo. Live conversation; this file *is* the canonical record.
