# 22 — Identity corpus: retrievable content unit

**Status:** DECIDED
**Decided on:** 2026-05-13
**Decision:** **Option 2 — one curated `identity.md` as the single retrievable unit; the three raw HTMLs become `_raw/` cold archive.** The `ora-party/identity/` folder previously held three raw HTMLs of mixed authority (party homepage, third-party press piece, Wikipedia article). They are demoted to `identity/_raw/` and replaced by one synthesized canonical Markdown card. The card speaks in the party's voice (drindrin homepage is the primary source) and uses Pagella Politica + Wikipedia as **facts-only cross-references** for objective verification of dates, governance structure, and biographical detail — not as retrievable corpus.

---

## Locked configuration

| Item | Choice |
|---|---|
| Retrievable for identity | A single file: `memory/corpus/ora-party/identity/identity.md`. Frontmatter: `type: identity`, `attribution: party`, `corpus_status: include`. |
| Excluded from retrieval (cold archive) | `identity/_raw/{drindrin-manifesto.html, pagellapolitica-nascita.html, wikipedia-ora.html}`. Not chunked, not embedded. Kept on disk for provenance and so the card can be re-derived if upstream sources change. |
| Primary source for the curated card | `_raw/drindrin-manifesto.html` (ORA's own homepage on `ora-italia.it`) — A1 voice. Substantive content and value statements are taken verbatim or near-verbatim from this source. |
| Cross-reference sources | `_raw/pagellapolitica-nascita.html` (press, Davide Leo, 13 Oct 2025) and `_raw/wikipedia-ora.html` (en.wikipedia "Ora!"). Used only to verify objective facts (founding dates, congress attendance, governance roles, biographical detail). **Not** quoted or paraphrased for value/position statements. |
| What goes in identity vs elsewhere | Identity holds *who-we-are* (founders, dates, governance, structure, membership, methodology, self-positioning). It does **not** hold *what-we-think-about-X* (those answers live in tesi A1a / comunicati A1b / newsletter sections A1c). |
| `attribution` value | `party` (extends the §5 enum value already used for tesi/comunicati/newsletter to this synthesized identity card). The §5 schema previously implied `<source-slug>` for `type: identity`; that wording was written when identity held one HTML per source. The Opt-2 single-card shape makes `party` the correct attribution. |
| `source_documents` frontmatter field | New per-doc field listing each raw file under `_raw/` with a `role` (`primary` / `cross-reference`) and a one-line `note`. Lets the future indexer + citation layer know that the card is synthesized and which raw artifacts back it. |
| `date_published` semantics for synthesized cards | Date the canonical card was authored/curated (`2026-05-13`), not a single upstream publication date. `date_scraped` reflects when the underlying raw HTMLs were fetched (`2026-05-10`). |
| Citation pill rendering | `[ORA, identità del partito]` (or equivalent). When the bot answers "Cosa è ORA?" / "Chi ha fondato ORA?" / "Quando è nato?" type questions, this card is the expected hit. |

---

## The question

The `ora-party/identity/` folder, before this decision, held three raw HTML files:

1. `drindrin-manifesto.html` — the homepage of `ora-italia.it`, i.e. ORA's own self-portrait. **A1 voice.**
2. `pagellapolitica-nascita.html` — a 13 Oct 2025 press piece by Davide Leo reporting from the Abano Terme founding congress. **A3 (press).**
3. `wikipedia-ora.html` — Wikipedia entry on "Ora!". **Tertiary; not slotted in §3 axis.**

Before any chunker/embedder runs, what should the retrievable unit for the identity slice be? Sub-questions:

1. Keep the three files separately, or synthesize?
2. If synthesized, what voice / which source dominates?
3. Where do the raw HTMLs live afterwards?
4. How does the `identity` slot fit into the §3 authority axis when one of its files (Wikipedia) doesn't fit any existing tier?

## Why it matters

- **Authority mixing inside one folder.** Decision 03 locked A1 / A2 / A3 as distinct authority slices. The three files mix A1 (party voice), A3 (press), and a tertiary (encyclopedic) layer that §3 has no slot for. Indexing them together would bury the authority axis the retrieval design rests on.
- **Format gap.** Everywhere else in the corpus the retrievable units are unified `.md` with the §5 frontmatter. Identity held only raw HTML — there was no canonical layer, just raw, which breaches the §5 raw → canonical MD → chunks/embeddings rule.
- **Missing `_raw/` cold archive.** §5 §7 mandates that every corpus subfolder has a sibling `_raw/`. Identity had only `_raw/`-grade content with no canonical sibling — the inverse of the rule.
- **§3 has no slot for Wikipedia.** Treating it as A3 inflates third-party press to encyclopedic encyclopedic tertiaries. Treating it as A1 is wrong. Treating it as live-web context is plausible but loses the static-snapshot value.
- **Identity ≠ position.** Users asking "Chi è ORA?" / "Quando è nato il partito?" / "Quanti aderenti ha?" need a different retrieval target than users asking "Cosa propone ORA su X?". Without a dedicated identity unit, retrieval would pull tesi or comunicati chunks that don't directly answer biographical/structural questions.
- **Decision 19 precedent.** For leaders, raw HTML bios were moved to `<leader>/_raw/bios/` and a single curated `profile/00-anagrafica-e-carriera.md` became the retrievable biographical unit. The same pattern applies cleanly to the party's identity slice.

## Options considered

### Option 1 — Drop identity from v1 corpus
Don't ingest any identity content. Identity questions get handled by (a) a system-prompt boilerplate (`"ORA è un partito centrista fondato nel 2024 da Boldrin e Forchielli…"`) + (b) live web search for anything richer.
- ✓ Zero ingestion friction; no preprocessing decisions.
- ✗ Trades a small, stable, valuable corpus slice for system-prompt brittleness and dependence on web search for very basic identity questions.
- ✗ "Chi è ORA?" is exactly the kind of question that should retrieve a single faithful card with citation, not a system-prompt platitude.

### Option 2 — One curated `identity.md`, three HTMLs to `_raw/` ★ (chosen)
A single A1-attributed canonical card synthesizes founders, founding dates, governance, congresses, membership figures, methodology, and self-positioning, taking content primarily from the drindrin homepage. Pagella + Wikipedia sit in `_raw/` as *facts-only* cross-references for the curator — they verify dates, biographical facts, governance roles, but they are **not** retrievable.
- ✓ Mirrors decision 19 (leaders → `profile/00-anagrafica-e-carriera.md`).
- ✓ One clean retrievable unit per "who is ORA?" question.
- ✓ Authority stays clean: card is A1 (party voice synthesized from party's own homepage). Press + Wikipedia don't pollute attribution.
- ✓ §3 Wikipedia gap dissolves — Wikipedia stays in `_raw/` as curator-only reference, no new tier needed.
- ✗ Paraphrase risk on a high-trust tier. Mitigations applied: substantive value statements quoted verbatim from drindrin; objective facts cross-verified across the three sources; the card's frontmatter `source_documents` block names each underlying artifact and its role.
- ✗ Drift: if drindrin updates its homepage or new biographical facts emerge (new vice-president, new headquarters), the card must be regenerated. Same drift category as decision 19's leader profiles; not unique to this decision.

### Option 3 — Separate canonicals per tier
Convert each HTML to its own `.md`, route to its proper tier home:
- `drindrin-self-portrait.md` → stays in `identity/` (A1, `type: identity`, `attribution: party`)
- `pagellapolitica-nascita.md` → moves to the AllNews / press folder (A3, `type: press_wrapper`)
- `wikipedia-ora.md` → either dropped or stays with `attribution: wikipedia` and a new tier label

- ✓ No authority-mixing, no paraphrase (each canonical stays byte-identical to source).
- ✗ Requires resolving the §3 Wikipedia gap explicitly (new tier label or new sub-axis).
- ✗ Forces the press tier to be designed *now*, before the broader AllNews pipeline is in place — premature commitment.
- ✗ Three separate retrievable units for "who is ORA?" queries; retrieval would return chunks scattered across press + tesi + identity, and the citation layer would need extra logic to compose them.

### Option 4 — Hybrid: drindrin in identity, Pagella to press, drop Wikipedia
Specific shape of Option 3. Wikipedia is left to the live-web axis (already trivially fetchable); Pagella belongs with the press scraper output; identity becomes a one-file folder containing only the drindrin self-portrait converted byte-identical to MD.

- ✓ Smallest viable footprint; no new tier needed.
- ✗ Throws away Wikipedia text already on disk.
- ✗ Same premature-press-tier problem as Option 3.
- ✗ The drindrin homepage is a *navigation page*, not a structured prose document — a byte-identical MD conversion would carry menu cruft, news ticker, member testimonials, and call-to-action blocks unrelated to identity. A small curation pass is needed regardless; if curation is happening anyway, Option 2's synthesis is the cleaner endpoint.

## Implications for adjacent decisions

- **Decision 03 (corpus trust hierarchy, DECIDED).** No change to the axis. The Wikipedia tier-gap is resolved structurally by relegating Wikipedia to `_raw/`. The §3 axis stays clean.
- **Decision 04 (chunking, OPEN).** Identity is a single short-to-medium `.md` file (~1.6k words). Chunker treats it as one document; structure-aware chunking on `##` section headers is the natural unit (`In sintesi`, `Fondatori`, `Cronologia di fondazione`, `Governance e struttura`, `Aderenti`, `Metodo e valori dichiarati`, `Posizionamento politico`, `I sei nodi`, `Le tre direttrici`, `Presenza territoriale ed elettorale`, `Comunicazione e canali ufficiali`, `Nota sulla denominazione`). Expected 4–8 chunks, depending on size budget.
- **Decision 06 (vector store, OPEN).** Identity adds 1 retrievable doc / ~4–8 chunks. Not a driver.
- **Decision 07 (retrieval strategy, OPEN).** The identity card is the canonical hit for "what is ORA / who founded it / when / how / how many members / what's their method" type queries. The retriever does not need a special routing rule — semantic similarity on these queries already points there cleanly. The card is short and topically coherent, so it should perform well under any reasonable retrieval setup.
- **Decision 08 (RAG paradigm, DECIDED — agentic).** No change. Identity is just another retrievable unit on the authority axis.
- **Decision 10 (citation, DECIDED).** Citation pill for identity hits reads `[ORA, identità del partito]` (analogous to `[ORA, Tesi NN — <slug>]` and `[ORA, comunicato — "<title>"]`). The card is attributed `party` and is the party speaking about itself; the pill should make clear this is the synthesized identity card, not a tesi.
- **Decision 11 (guardrails, PARTIAL).** No change. The card holds no policy positions; refusal rules unaffected.
- **Decision 13 (freshness, DECIDED).** New identity-relevant facts (a new vice-president, a new headquarters, an updated membership count) require regenerating the card by re-running the curation against an updated drindrin scrape. The trigger is event-based, not scheduled — there is no weekly identity pipeline. Drift category similar to decision 19's leader profiles.
- **Decision 17 (data corpus, DECIDED).** No change. Identity card cites membership figures with their date stamps (e.g. "~13,000 al maggio 2025"); empirical claims about the party itself (member count, demographic split) are sourced from the party's own and press reports and dated in the card body to prevent staleness from being invisible.
- **Decision 18 (audit, DECIDED).** Out of scope for v1. Identity-card drift (homepage updated, the card not) is a v2 audit candidate alongside leader-card and party-card audits.
- **Decision 19 (leader corpus unit, DECIDED).** This decision is the party-side analog. Same Model B pattern: curated artifact retrievable, raw sources in `_raw/`. Cross-reference rule symmetric.
- **Decision 20 (other-parties preprocessing, DECIDED).** No change. Other parties have their own `programme` documents and (eventually) topic cards; ORA's identity card is sui generis to the ORA tier.
- **Decision 21 (ORA voice preprocessing, DECIDED).** Identity is a new fourth ORA-side unit (A1a tesi, A1b comunicati, A1c newsletter sections, A1-identity). It does not pass through the newsletter splitter or any per-week pipeline; it is a one-off synthesis with event-triggered regeneration. The §3 authority axis label A1 (broadly: "ORA's official voice") accommodates it without amendment.
- **CLAUDE.md §5 schema.** Two adjustments confirmed:
  1. `attribution: party` is the value used for `type: identity` documents (replacing the previously-implied `<source-slug>`; the source-slug shape would have applied only to a 1-HTML-per-source identity layout, which we no longer have).
  2. New optional frontmatter field `source_documents` (a list of `{file, role, note}` items) on synthesized canonical docs. Documents which raw artifacts back the synthesis and what each contributed.

## Structural cleanup performed alongside this decision

Executed 2026-05-13:

- Created `memory/corpus/ora-party/identity/_raw/`.
- Moved into `_raw/`:
  - `drindrin-manifesto.html` (213,828 bytes)
  - `pagellapolitica-nascita.html` (493,224 bytes)
  - `wikipedia-ora.html` (157,712 bytes)
- Created `memory/corpus/ora-party/identity/identity.md` — the canonical retrievable card. Frontmatter per §5 schema with `type: identity`, `attribution: party`, `corpus_status: include`, `content_hash` populated, plus the new `source_documents` block listing the three raw artifacts and their roles.
- Cleaned up curator scratch files (`*.extracted.txt`) used during synthesis — no need to persist.
- CLAUDE.md updates:
  - `§5` corpus tree comment for `identity/` updated to reflect the new shape.
  - `§9` decisions index gains a `22` row marked `DECIDED (2026-05-13)`.
  - Open-decisions count adjusted accordingly.

## What this decision does NOT settle

- **Regeneration cadence.** When and how often is `identity.md` refreshed? Today the trigger is "re-run when the drindrin homepage changes meaningfully." There is no scheduled job. If the audit framework (decision 18 v2) eventually covers party-side cards, identity should be in scope.
- **Voice-preservation policy for synthesized cards.** This card paraphrases the drindrin homepage in places (it had to — the source is a navigation/marketing page, not a structured prose document). Verbatim quoting was applied to the three value statements and the slogan. If the eval framework (decision 12) ever reports attribution complaints on identity-type queries ("this is paraphrased, I want ORA's exact words"), the resolution is either (a) richer verbatim quoting in the card, or (b) a small `identity-quotes.md` supplemental that holds the party's exact phrasing for the most-quoted passages.
- **Press tier (AllNews) design.** This decision leaves Pagella in `_raw/` for now. When the press tier is built out (and `scrape_news.py` populates it under `ora-party/AllNews/` or a similarly-named folder per §3), the Pagella article *could* be promoted into it as a `type: press_wrapper`, byte-identical conversion. That is an option for the press-tier decision when it comes due, not a commitment here.

## Riccardo's stated rationale (verbatim)

After surfacing five options (Opt 1 / Opt 2 / Opt 3 / Opt 4, plus a do-nothing baseline) and walking through the trade-offs:

> "option 2. let's execute. be comprehensive. when you have done, the files go in raw"

Interpretation locked: the deciding constraint was getting a single, faithful, self-contained identity unit on the same footing as the leaders' `profile/00-anagrafica-e-carriera.md` (decision 19) — at the cost of accepting a small paraphrase tax on the synthesized card. The drift / paraphrase risks were judged acceptable for an A1-attributed identity unit because (a) the underlying drindrin homepage is itself a navigation/marketing page that benefits from being restructured into prose, (b) substantive value statements are quoted verbatim, (c) `source_documents` frontmatter makes provenance auditable. "Be comprehensive" was applied to the card body (founders, full timeline, governance, methodology, six priority themes, three direction pillars, current candidacies, communication channels, name etymology).

## Reference

- CLAUDE.md §3 (authority axis — A1 tier and the Wikipedia gap), §4 (sourcing — attribution discipline), §5 (frontmatter schema, `_raw/` rule), §7 (long-term ingestion rule).
- Decision 03 (corpus trust hierarchy — A1 dominance preserved).
- Decision 10 (citation — pill must read `type` to render identity correctly).
- Decision 19 (leader corpus unit — direct precedent for the curated-artifact-as-retrievable / raw-in-`_raw/` pattern).
- Decision 21 (ORA voice preprocessing — locates identity as a fourth A1-side unit alongside tesi / comunicati / newsletter sections).
