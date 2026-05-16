# 24 — Contact / user-routing data

**Status:** DECIDED
**Decided on:** 2026-05-15
**Decision:**
- **Storage model: hybrid.** A short retrievable identity-style card under `memory/corpus/ora-party/contacts/contacts.md` (so the agent recognises contact-routing questions and can describe the org structure in its answer) **plus** a structured JSON file at `memory/lookups/contacts.json` (single source of truth for name → role / email / social URLs). The JSON sits **outside** `memory/corpus/` and is therefore invisible to the chunker/embedder — values are retrieved via a deterministic tool, never via ANN.
- **Surface policy: public scraped data, on-demand only.** The bot returns a contact only when the user explicitly asks ("come contatto il referente Toscana?", "qual è il LinkedIn di Andrea Savi?"). It does **not** volunteer contacts; it refuses bulk requests ("dammi le email di tutti i membri"). All data is what is already publicly visible on `ora-italia.it/partito/` + `/consiglio-direttivo/` + `/assemblea-nazionale/` + `/territorio/` — no new privacy surface vs. the source page.
- **New tool — `contact_lookup`.** Extends decision 23's tool inventory from 5 to 6. Deterministic key→value lookup over the JSON (no LLM, no ANN). API sketch:
  ```
  contact_lookup(
    area: str = None,     # region slug or "americhe"/"asia"/"europa" — for territorial referenti
    role: str = None,     # role/area slug ("segretario","presidente","innovazione",...) — for national orgs
    name: str = None,     # person slug — for "who is X / how do I reach X" questions
  ) -> {
    matches: list[{
      name: str, role: str | None, org: str,        # org ∈ {segreteria-nazionale, consiglio-direttivo, assemblea-nazionale, territorio}
      email: str | None, socials: dict[str, str],   # socials keyed by platform: x | instagram | facebook | linkedin
      source_url: str, last_scraped: date,
    }],
    truncated: bool,      # true if the query would have returned more than the cap (bulk-request guard)
  }
  ```
  The tool caps results (proposed: 10) and sets `truncated=true` so the agent can refuse bulk surfacing.

**Rationale (verbatim from the 2026-05-15 session):** "Hybrid: retrievable card + JSON tool" — selected as Riccardo's choice from the three storage options. "Public scraped data only, on-demand only" — selected as the surface policy. The deeper reason (developed in-session): semantic retrieval over names + emails buys nothing — the user query is an **exact-key lookup**, not a similarity question, and embedding contact data risks the model hallucinating a plausible-looking-but-wrong email when retrieval is fuzzy. A deterministic tool is exact, auditable, and trivially refreshable; the retrievable card keeps the agent *aware* of the routing capability so it knows when to call the tool.

**Source of decision:** This session, 2026-05-15. Confirmed via `AskUserQuestion` after technical probe of the four target pages (`/partito/`, `/consiglio-direttivo/`, `/assemblea-nazionale/`, `/territorio/`) confirmed they are all static HTML — no browser automation needed.

---

## The question

The four objectives (CLAUDE.md §2) are **State / Project / Justify / Compare** — all *content* objectives, all about *positions*. A user who comes to the chatbot wanting to **contact the party** (territorial referente, segreteria member, leader on a specific topic) is asking a routing question that doesn't map to any of the four. Do we add this capability, and if so, how do we store the data?

The triggering user request:

> "i want to add some data to the corpus. specifically about the contacts in general of the party, so that when a user come to the chatbot and wants to talk to someone or with the territory of a certain area, it can find the email or the social."

## Why it matters for the ORA chatbot

- **Capability gap.** Without this data the bot must refuse a perfectly legitimate user need ("come contatto la sezione Veneto?"). For a public-facing party-website chatbot, refusing to help a citizen reach the party is a poor experience.
- **Faithfulness risk if mis-stored.** Embedding emails and social URLs as text chunks invites the most expensive failure mode: a model that returns a *plausible* email that doesn't actually work. RAG is the wrong tool for exact-key lookup.
- **Scope creep risk.** Adding "routing" as a vague 5th objective dilutes the four locked content objectives. Better to mark it as an **auxiliary capability** — adjacent to but distinct from the four — with its own decision file and a dedicated tool, kept structurally separate from the content tiers.
- **Privacy.** All the contact data is already publicly displayed on `ora-italia.it`. The bot doesn't introduce new exposure as long as it stays on-demand (no enumeration, no bulk dumps).

## Options considered

### (a) RAG-only — markdown files under `memory/corpus/ora-party/contacts/` with `type: contact`
Goes through the normal chunk → embed → Qdrant pipeline.
- **Pro:** Uniform with the rest of the corpus. No new tool to wire.
- **Con:** Highest hallucination risk on the most-checkable kind of fact (an email, a URL). Semantic similarity provides no benefit for exact-key lookup.

### (b) Tool-only — JSON at `memory/lookups/contacts.json` + `contact_lookup` tool, no corpus card
Skips RAG entirely.
- **Pro:** Cleanest separation. Zero hallucination on the values.
- **Con:** The agent only knows contacts exist via the system prompt + tool description. If those don't mention contacts vividly enough, the agent may never call the tool when it should.

### (c) Hybrid — short retrievable card + JSON tool *(chosen)*
The card gives the agent *awareness* via retrieval (it surfaces on queries about "referenti", "contatti", "organi", "segreteria", "territorio"); the tool gives *values* via deterministic lookup.
- **Pro:** Best of both — retrieval helps recognize the question, tool guarantees correctness.
- **Con:** Two places to keep in sync. Mitigated by having the scraper produce both from a single parse.

### (d) Defer — open decision file, scrape later
- **Pro:** Avoids premature commitment.
- **Con:** No new information would emerge from waiting; the trade-offs are already clear.

## Surface policy

Chosen: **on-demand only, no bulk.**

- The bot answers specific contact questions: *"qual è il referente Lombardia?"*, *"come contatto Andrea Savi?"*, *"chi è il segretario di ORA?"*.
- The bot **refuses** enumeration: *"dammi tutte le email"*, *"lista di tutti i membri con i loro social"*. New `emit_refusal` reason needed: `contact_bulk_request` (or reuse `off_scope` with a related-topic redirect). To be wired into decision 23's `emit_refusal` template list when the agent is built.
- The bot does not **volunteer** a contact unsolicited: if a user asks about ORA's energy policy, the bot answers the policy question and does *not* append "and you can email energia@ora-italia.it…".
- Structural enforcement: the `contact_lookup` tool returns at most N results (proposed N=10) and sets `truncated=true`. If the planner classifies the query as `query_type=contact_bulk`, the agent skips the tool and emits a refusal.

## Data sources

All public, all currently static HTML — verified 2026-05-15:

| URL | Yields |
|---|---|
| `https://ora-italia.it/partito/` | Boldrin (Segretario), Forchielli (Presidente), 6 Segreteria Nazionale members. Each with role + 1–4 social URLs. |
| `https://ora-italia.it/consiglio-direttivo/` | Consiglio Direttivo members + socials. |
| `https://ora-italia.it/assemblea-nazionale/` | Assemblea Nazionale members + socials. |
| `https://ora-italia.it/territorio/` | 20 regional referenti + 3 overseas referenti (Americhe, Asia/Africa/Oceania, Europa). Each with name + `regione@ora-italia.it` `mailto:` link. |

Same Elementor `card_persona` block pattern repeats across the three leadership pages. No JavaScript interaction required — all data is in raw HTML. No new scraping dependency: `requests` + `beautifulsoup4` (already used by the legacy scrapers in `memory/scripts/_bin/`).

## Folder layout introduced

```
memory/
├── corpus/ora-party/contacts/
│   ├── contacts.md            # retrievable card (type: contact, corpus_status: include)
│   └── _raw/                  # cold archive (per §5 _raw/ mandate)
│       ├── partito.html
│       ├── consiglio-direttivo.html
│       ├── assemblea-nazionale.html
│       └── territorio.html
├── lookups/                   # NEW — non-corpus structured data behind deterministic tools
│   └── contacts.json
└── scripts/
    └── scrape_contacts.py     # NEW — weekly scraper + dual emitter
```

`memory/lookups/` is **outside** `memory/corpus/` and is therefore invisible to the chunker/indexer by construction (no `_` prefix needed). Future deterministic-tool data lives here.

## Frontmatter schema addition

Add to CLAUDE.md §5 type vocabulary: `contact`.

```yaml
---
id: ora-contacts
type: contact
attribution: party
title: "ORA! — Organi e referenti del partito"
source_url: "https://ora-italia.it/partito/"
date_compiled: 2026-05-15
date_scraped: 2026-05-15
description: "Carta della struttura di contatto del partito ORA: segretario, presidente, segreteria nazionale, consiglio direttivo, assemblea nazionale, referenti territoriali."
content_hash: <sha256 of body, bare hex>
corpus_status: include
---
```

The card itself is short (~1 page of markdown): describes the org structure, names the segretario/presidente/segreteria roles, lists the 23 territorial scopes (20 regioni + 3 estero), and tells the agent: "for actual names, emails, and social URLs, call `contact_lookup`."

## Freshness

Same weekly cadence as the rest of the corpus (decision 13). `scrape_contacts.py` will be added to `run_weekly.bat` whenever that's reactivated. Change detection via `content_hash` on the markdown card; the JSON is overwritten each run (small, structured, easy to diff).

## Pending sub-decisions (not blocking)

1. **`emit_refusal` reason for bulk requests.** Add `contact_bulk_request` to decision 23's enum, or reuse `off_scope`? Lean toward a dedicated reason for clean telemetry.
2. **Result cap N.** Currently proposed 10. Revisit after first real user logs.
3. **Tone in the answer.** A contact reply is necessarily second-person-actionable ("Puoi contattare X a Y"), which sits slightly outside the third-person-encyclopedic persona (CLAUDE.md §4, decision 16). Treat as an allowed exception: providing a contact **is** the answer.
4. **Future: contact-search by topic.** "Chi posso contattare per parlare di energia?" → currently answered via `role` slug ("Innovazione" / "Programma") in the Segreteria. Eventually may want a topic → person mapping; defer.
5. **`ORA_TIERS` extension.** The agent's structural-whitelist (decision 23, `agent/constants.py:ORA_TIERS`) must include `"A1-contacts"` so contact-routing queries reach the card. Forward-pointer added in decision 23. Not blocking now (agent not implemented); blocks the day the agent code is written.

## Chunking & ingestion status (2026-05-15)

- **Chunker:** `handle_contact` handler added to `memory/scripts/chunk_corpus.py`. Strategy: split by H2 → 3 chunks ("Organi nazionali" 301 tok, "Referenti territoriali" 176 tok, "Come reperire un contatto specifico" 294 tok). Tier label: `A1-contacts`. Total corpus chunks: 3279 across 536 retrievable docs.
- **Embedding + Qdrant upsert:** not yet run for the new chunks. Same model + collection (voyage-4-large, `ora_chunks`, decisions 05/06). Idempotent upsert by chunk_id UUID5 — re-running `ingest_qdrant.py --apply` will only add the 3 new points (existing chunks unchanged).

## Reference

- CLAUDE.md §1 (Riccardo decides architecture)
- CLAUDE.md §2 (four objectives — this is auxiliary to them)
- CLAUDE.md §5 (frontmatter schema, `_raw/` mandate, indexer inclusion rule)
- Decision 13 (freshness pipeline)
- Decision 23 (agent architecture, tool inventory — this adds tool #6)

## Observations

- The decision to surface a brief retrievable card *plus* a deterministic tool mirrors the data-tier pattern (decision 17): data has stat-cards in the corpus and a `data_lookup` tool. Contacts now follow the same shape.
- Decision 23's tool count line ("Tool inventory (5 tools)") will need to read 6 once `contact_lookup` is implemented. Forward-pointer added there.
