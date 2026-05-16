# 03 — Corpus trust hierarchy

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** **Two-axis retrieval design** with explicit attribution tiers:

- **Authority axis (corpus):**
  - **A1 — ORA's official voice:** A1a Tesi programmatiche (slow, foundational) > A1b Comunicati (recent, event-specific) > A1c Newsletter (recent, digest). When a comunicato/newsletter contradicts a tesi, **prefer the more recent and flag the evolution**.
  - **A2 — Members' personal voice:** A2a Boldrin > A2b Forchielli > A2c other members. Used to fill A1 gaps. **Always cited as personal view; never blurred with party position.**
  - **A3 — Third-party press coverage** (lowest authority within corpus).
- **Live context axis (web search):** runs **in parallel on every query** for currency + other-parties comparison.
- **Synthesis rule:** *"Authority answers, context enriches."* The answer is grounded in the authority axis; web search adds currency, never replaces the authoritative voice.

**Rationale:** A single hierarchy bundled "whose voice is most trusted" with "what's most recent" — splitting them keeps both clean. Lets the bot say "Posizione fondante: X. Aggiornamento recente: Y." instead of silently picking one.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md`. See CLAUDE.md §3 (full retrieval design) and §4 (sourcing rules including divergence and gap-filling).

## The question

When two sources in the corpus disagree about ORA's position on something, which one wins?

Concrete example: the manifesto (formal programmatic document, January 2026) says one thing about immigration; a newsletter from March 2026 nuances it; Boldrin in a YouTube interview from 2024 says something stronger. What should the bot present as ORA's position?

This is **not** a question of which file to keep — it's about how the retrieval and generation layers should *weight* sources when answering.

## Why it matters for the ORA chatbot

- Without a hierarchy, the bot averages everything and produces mushy answers.
- With the wrong hierarchy, the bot misrepresents the party (e.g., quoting a leader's 2018 tweet over the 2026 manifesto as if they were equivalent).
- This is also the foundation for **attribution** in the answer text: the bot should say *who* said *what* and *when*.

## Options

### A — Strict tier ordering
A fixed hierarchy applied at retrieval ranking and/or generation prompt:
1. **Manifesto** (formal, voted, current)
2. **Newsletter / comunicati** (party-issued, dated)
3. **Identity documents** (wikipedia, founding statements)
4. **Leader content tagged as party-aligned** (e.g., "programmatic" YouTube episodes)
5. **Leader content tagged as personal opinion**
- Pros: predictable, defensible, easy to explain in citations.
- Cons: rigid; can suppress recent leader statements that *do* represent updated party thinking.

### B — Recency-weighted within attribution tier
Same tiers as A, but within each tier, newer beats older. Across tiers, manifesto still beats leader interview even if the interview is more recent — unless explicitly superseded by a newer party communication.
- Pros: handles policy evolution.
- Cons: more logic, more edge cases.

### C — Multi-source synthesis with explicit labeling
No hierarchy at retrieval. At generation, the model is instructed to surface *all* relevant sources and label them: "The 2026 manifesto says X; in a March 2026 newsletter, the party clarified Y; Boldrin in a personal interview said Z." User decides what to make of it.
- Pros: maximally honest.
- Cons: longer answers; assumes user can parse nuance; harder to handle short / mobile / voice answers.

### D — Two-pass: party-only first, then optionally augment
First retrieval only over party-attributed content. If results are weak or absent, second retrieval over leader content with explicit "this is leader-not-party" labeling.
- Pros: keeps party speech clean; gracefully degrades.
- Cons: more pipeline complexity.

## What we'd need to know to choose

- How often do you expect leader views and party positions to diverge?
- Is your priority "always give an answer if there's anything in the corpus" or "give a clean party answer or none"?
- Should the user see the timeline of position changes, or just the current position?

## Reference

- KB concept: `08_grounding_and_citation.md`
- KB concept: `07_retrieval_strategies.md` (re-ranking by metadata)
- KB concept: `15_political_chatbot_application.md`

## Observations
- The corpus already carries an `attribution` field in YAML frontmatter (e.g., `attribution: party` on manifesto/comunicati). Useful signal — preserve it.
- Newsletters have `date_published`, which enables recency weighting.
- Leader content currently lacks a "party-aligned vs personal" tag — that would need to be added if option B/D is chosen.
