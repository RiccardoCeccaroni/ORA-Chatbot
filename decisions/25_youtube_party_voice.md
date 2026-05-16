# 25 — YouTube content as A1c-equivalent party voice + A2 leader voice

**Status:** DECIDED
**Decided on:** 2026-05-15
**Decision:**

- **Two new retrievable types:**
  - `party_event_distillation` — multi-speaker ORA-channel videos (tesi presentations, working-group panels, party dialogues). Tier label: `A1c-event` — sibling-trust to `newsletter_section` (A1c). Attribution at document level: `party`.
  - `leader_event_distillation` — leader-only content (Boldrin or Forchielli monologues, plus the AF&MB dialogue split into two leader-attributed halves). Tier label: `A2-<attribution>-event` (mirrors the existing `A2-<attribution>-article` pattern for `leader_article`).

- **Member-only speaker filter (per-claim).** A claim is extracted into a card only if the speaker is an ORA member listed in `memory/Moreinfofromyt/members.yaml`. External experts speaking inside ORA-channel dialogues (Cassese, Sesta, Bizzarri, Molteni, Skeptical Health) have their claims dropped at distillation time, even when they appear in a video tagged as party content. The ORA member's claims in the same dialogue are kept. When no ORA member is identified across the entire video, the resulting card carries `corpus_status: exclude` (v1: 4 cards excluded — Skeptical Health, Bizzarri, Esteri presentation w/ Cristolo, Agricoltura w/ unknown speakers).

- **Per-claim attribution in chunk text.** Every bullet ends `*<speaker>, ~mm:ss* (estende|raffina|contraddice|nuovo|ripete T<N>)`. Speaker provenance survives chunking — when the agent uses a chunk, it cites the named speaker + the video timestamp. This means that within a `party_event_distillation` card (tier `A1c-event`, attribution `party`), the actual quoted speaker is named in the chunk text — preserving the leader-vs-party discipline even though the document-level tier is uniform. The agent's citation must name the speaker, not just "ORA".

- **Chunking unit: one chunk per `## H2` section.** Cards have up to 7 sections (`Posizioni dichiarate`, `Razionale / diagnosi`, `Misure concrete proposte`, `Affermazioni empiriche (verifica via tier-dati)`, `Confronti con altri partiti`, `Cautele / non-impegni`, `Citazioni distintive`). Empty sections (e.g., `_(nessun contenuto)_`) emit nothing. Per-bullet chunking was rejected as too granular; per-card was rejected as too coarse.

- **Empirical-claims chunks cross-check against the data tier.** The `## Affermazioni empiriche` section's chunk carries an implicit signal (the anchor name) that the agent should treat the contained numeric claims as "to be verified against `memory/corpus/data/`" per decision 17. No special metadata flag needed — the section anchor is enough for the agent prompt to route correctly.

**Rationale (settled in the prior 2026-05-15 session, captured in the handoff document):** YouTube content is ORA-published material (the official channel) and therefore party-voice — but every utterance is one human speaking, so chunk-level attribution preserves leader-vs-party discipline at the citation site. Equivalent trust to newsletter (A1c) is defensible: both are recent, both are first-person ORA voice, both are less canonical than tesi (A1a) but more so than third-party press. The reranker (`voyage-rerank-2.5` per decision 07) handles redundancy when multiple speakers say similar things across cards — no Stage-2 aggregation needed in v1.

**Source of decision:** Two prior Claude Code sessions (2026-05-15): the YouTube transcript-pull session (locked Option X + speaker filter + 7-section schema during distillation), and this session (locked folder placement + per-H2 chunking + `corpus_status: exclude` rule for 4 quality-failing cards).

---

## The question

CLAUDE.md §3 (Authority axis) is LOCKED with three tiers: A1 (party voice — tesi/comunicato/newsletter), A2 (leader voice — Boldrin/Forchielli/others), A3 (third-party press, deferred). The party's YouTube channel (`@ora.italia`) publishes a substantial body of content that is ORA's own voice but doesn't fit any existing slot: it's videos, with multiple speakers per video, including occasional external guests. Where does this go?

## Why it matters for the ORA chatbot

- **Capability gap.** 56 videos × ~30 min average = ~28 hours of ORA-channel content. Excluding it leaves the bot blind to the most discursive, current, and concretely-reasoned material ORA produces. Tesi are slow-moving; newsletters are short; comunicati are event-spot. The videos are where the party actually argues its case.
- **Authority correctness.** Embedding video transcripts as party voice creates a faithfulness risk: a guest expert speaks at length in a party-channel dialogue, but their claims are not ORA's positions. Without a speaker filter, the bot would cite an external expert's opinion as if it were the party's. The filter solves this structurally at distillation, not at retrieval.
- **Voice attribution.** CLAUDE.md §4 mandates that leader views never blur into party positions. YouTube blurs this because a working-group lead presenting a tesi is, in one breath, both a party representative (this is the party's official video) and a private individual (their phrasing is their own). Chunk-level speaker attribution lets the agent cite the human while the document-level tier signals party authority.

## Options considered

### (a) Treat the whole channel as A2 (leader voice across the board)
Every speaker is a private individual; tier as leader.
- **Pro:** Trivially correct on the "who is talking" question. No new tier.
- **Con:** Misses that the channel is the party's official outlet, that videos are produced for the party's communication, and that working-group leads are speaking *as* party representatives, not as private citizens.

### (b) Treat the whole channel as A1c (party voice, newsletter-tier) *(chosen)*
Tier as party content with chunk-level speaker provenance. Member-only speaker filter at distillation.
- **Pro:** Matches what the channel actually is — the party's published voice. Speaker provenance survives at chunk level, so leader-vs-party distinction is preserved at citation. Reranker handles redundancy across speakers.
- **Con:** Document-level tier is uniform even though some claims come from less authoritative speakers within the party (working-group members vs Boldrin). Mitigated by per-claim attribution.

### (c) Introduce a new tier A1d below A1c
Explicit "party-attributed spoken material, distilled" tier ranked below newsletter.
- **Pro:** Most honest about provenance. Cleanest separation.
- **Con:** Requires amending decision 03 (the trust hierarchy). Adds complexity. The reranker already does what an explicit tier would do — surface the most relevant chunk regardless of tier.

## Pipeline

```
memory/Moreinfofromyt/                         ← scaffolding (excluded by `_`-prefix rule N/A;
                                                  retained outside corpus/ on purpose — generation
                                                  + regeneration sources, never indexed)
├── members.yaml                               ← 130 ORA members; filter ground truth
├── all_transcripts/                           ← 50 party Whisper transcripts
├── leader_transcripts/                        ← 6 leader Whisper transcripts
├── _raw_whisper/                              ← 56 verbose-JSON Whisper outputs (cold archive)
├── distillations/                             ← 50 party cards (source of truth)
├── leader_distillations/                      ← 7 leader cards (source of truth)
├── whisper_transcribe.py                      ← yt-dlp → ffmpeg → Whisper API
├── distill.py                                 ← party-voice distiller
├── leader_distill.py                          ← leader-voice distiller
└── pipeline.py                                ← end-to-end orchestrator (idempotent)

memory/corpus/                                 ← retrievable artifacts
├── ora-party/
│   └── youtube/                               ← NEW: 50 party cards
│       └── (4 cards carry corpus_status: exclude — see QA notes)
└── leaders/
    ├── boldrin/
    │   └── youtube/                           ← NEW: 6 cards
    └── forchielli/
        └── youtube/                           ← NEW: 1 card (the AF&MB dialogue's Forchielli half)
```

## Frontmatter schema additions

```yaml
type: party_event_distillation                  # NEW — to §5 vocab
attribution: party
title: "<youtube video title>"
source_url: "https://www.youtube.com/watch?v=<id>"
date_published: "<youtube upload date, YYYY-MM-DD>"
date_compiled: "<distillation date, YYYY-MM-DD>"
playlist: "<one or more playlist names, comma-separated>"
speakers: [<list of member slugs>]              # NEW field — slugs match members.yaml
tesi_touched: [<list of tesi numbers>]          # NEW field — for retrieval signal + agent routing
duration: "<mm:ss or HH:MM:SS>"                 # NEW field — provenance
content_hash: "<sha256 of body, bare hex>"
distillation_model: "claude-sonnet-4-6"         # NEW field — provenance
transcription: "whisper-1"                      # NEW field — provenance
corpus_status: include | exclude                # explicit on every YouTube card
```

`leader_event_distillation` differs only in: `type:` value, `attribution: boldrin|forchielli`, optional `tier: A2a|A2b` field, no `tesi_touched`, body framed with a leading "*Voce personale di <leader>...*" disclaimer.

## QA exclusions for v1 (4 of 50 party cards)

| Card | Reason |
|---|---|
| `Come sarà la Sanità del Futuro? con Skeptical Health [PTjvhzcGMD0]` | External-guest dialogue, no ORA member identified — 0 bullets in body |
| `Come sta l'università italiana? - con Ranieri Bizzarri [LysNxK2RY5U]` | External-guest dialogue, no ORA member identified — 0 bullets in body |
| `Tesi Programmatiche di ORA!: Agricoltura, Foreste e Sviluppo Rurale [H5iuLjHKOoc]` | 44 bullets but every speaker tag is literally `(?)` — distiller couldn't identify any speaker. Violates the citation discipline. Loss: this was the only ORA-voice source for agriculture (tesi #01 missing per §8.3) |
| `Presentazione Tesi - Esteri e Relazioni Internazionali [4CeywmWehiA]` | 69 bullets — Maro (member) + Cristolo (not member). Filter leak. Cleanly recoverable by dropping Cristolo's bullets + backfilling Maro; deferred to v1.1 |

Source files remain in `memory/Moreinfofromyt/distillations/` for future regeneration. The excluded copies in `memory/corpus/ora-party/youtube/` carry `corpus_status: exclude` so the chunker skips them.

## Chunker contract

- `handle_party_event_distillation(fm, body)` — splits on `## H2`; emits one chunk per non-empty section; skips sections containing only `_(nessun contenuto)_`. Each chunk's `anchor` is the section heading. Each chunk's `extras` carries `playlist`, `speakers`, `tesi_touched`, `duration`.
- `handle_leader_event_distillation(fm, body)` — same per-`## H2` pattern; chunk attribution from frontmatter (`boldrin`/`forchielli`); tier `A2-<attribution>-event`.

## Agent contract (decision 23 amendment)

- `ORA_TIERS` whitelist (in `agent/orchestrator.py:retrieve_parallel()`) gains `party_event_distillation` and `leader_event_distillation`.
- `agent/system_prompt.py` gets a paragraph: party-event content is A1c-equivalent; citations must name the speaker + the YouTube timestamp + the video URL.
- For the `Affermazioni empiriche` section anchor, the agent should treat the contained figures as candidates for cross-check against the data tier per decision 17.

### Leader-as-proxy-for-party framing (Riccardo, 2026-05-15)

Reinforcement of the existing CLAUDE.md §4 gap-filling rule + decision 23 citation-precedence rule, made explicit for the abundant Boldrin leader content (6 of 7 leader cards) and for general-stance questions:

When the user asks "qual è la posizione di ORA su X?" and the corpus has **no A1 (party) answer** but does have an A2 (leader) answer — including a `leader_event_distillation` card — the bot may use the leader content as a fallback, but the **framing must make the source explicit**, not paraphrase the leader as if the party had said it. Example phrasing the system prompt should encourage:

> "Sulla posizione ufficiale di ORA su X non risulta una tesi né un comunicato. Il leader del partito, Michele Boldrin, ha però affermato in un video del [data] che [...]. Si tratta di una posizione personale del segretario, che può anticipare ma non sostituisce una presa di posizione ufficiale del partito."

This is an *agent-prompt* concern, not a structural one. The §4 gap-filling rule already authorizes the citation; this reinforces the *phrasing discipline* so the user is never misled into thinking they got a party position when they got a leader's personal view.

## Freshness

`pipeline.py all` is idempotent — re-running with a new video URL fetches metadata, downloads audio (yt-dlp), transcribes (Whisper), distills (Sonnet 4.6), and emits a new `.md` card. Future weekly cadence (per decision 13) adds `pipeline.py <new-url>` to `run_weekly.bat` whenever the channel posts.

## Pending sub-decisions (not blocking v1)

1. **Esteri card re-distillation.** Decide whether to re-run with a fixed Cristolo entry in `members.yaml` (i.e., is Cristolo actually an ORA member?) or to manually strip his bullets.
2. **Agricoltura recovery.** Re-run the distiller on `H5iuLjHKOoc` to identify the speaker; if Boldrin or a specific WG lead is identifiable, this card becomes the only A1c-tier Agricoltura source.
3. **Stage-2 aggregation.** Skipped for v1 per Riccardo's call. Revisit if retrieval-quality eval (decision 12) shows redundancy noise across the ~46 cards.
4. **Speaker enrichment.** Several non-empty cards have `speakers: []` despite valid inline attribution — would be nice to backfill these automatically from body bullets.

## Reference

- CLAUDE.md §1 (Riccardo decides architecture)
- CLAUDE.md §3 (Authority axis — locked, not amended; new types fit into existing tiers via labeling)
- CLAUDE.md §4 (Sourcing rules — speaker attribution discipline preserved)
- CLAUDE.md §5 (Frontmatter schema, indexer rule, `_raw/` mandate)
- Decision 03 (Corpus trust hierarchy)
- Decision 04 (Chunking — this is a per-type sub-decision within #04's structure-aware framework)
- Decision 13 (Freshness pipeline — `pipeline.py` joins `run_weekly.bat` cadence)
- Decision 17 (Data tier — `Affermazioni empiriche` section feeds into the contradicting-data rule)
- Decision 23 (Agent architecture — tier whitelist extension, citation discipline)
