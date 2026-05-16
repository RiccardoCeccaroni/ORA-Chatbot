# 01 — Scope & out-of-scope policy

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** Scope is **ORA party + leaders (cited as personal view) + other parties via live web for comparison**. Personal-life advice (medical, legal, financial, personal) is **out of scope** and gets redirected to the related policy lens.
**Rationale:** Required by the four objectives (State / Project / Justify / Compare). Objective 4 explicitly demands other-parties comparison. Objective 2 (hypotheticals) and gap-filling demand leader voice. Personal-life advice was carved out because it falls outside what a political-party bot should commit to.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md`. See also CLAUDE.md §2 (four objectives) and §4 (sourcing rules).

## The question

What does this chatbot answer questions *about*, and what does it refuse to answer?

Specifically:
1. Does it speak only for **the ORA party**, or also for **the personal views of its leaders** (Boldrin, Forchielli)?
2. Does it answer questions about **other parties** (PD, M5S, Lega, FdI, …) for comparison? If yes, where does the information come from?
3. Does it answer **general political-science questions** ("what is the difference between a constitutional and a parliamentary monarchy?") or only ORA-specific ones?

## Why it matters for the ORA chatbot

- Scope determines what corpus you ingest. Including leader interviews triples the corpus size; including other parties multiplies the maintenance cost.
- Misattribution is the chief failure mode. If the bot says "ORA thinks X" but X was actually Boldrin's personal opinion on his YouTube channel ten years ago, trust collapses.
- The `other-parties/` folder is empty today. If "compare ORA to PD on labor" is in scope, that folder needs to be populated — which means another scraping pipeline.
- Out-of-scope questions need a graceful refusal. ChatGPT-style hedging would erode credibility; a clean "this bot only covers ORA's published positions" is more honest.

## Options

### A — ORA party only (manifesto, comunicati, newsletter, identity)
- Tightest scope. Easiest to keep faithful. Leader content excluded.
- Risk: users asking "what does Boldrin think about X" get refused even when there's a clear answer in his content.

### B — ORA party + leader views, clearly labeled
- Ingest everything, but tag each chunk with `attribution: party | boldrin | forchielli`. The answer text always says "ORA's official position is…" vs "Boldrin has said…".
- Heavier guardrail logic but richer answers.

### C — ORA + leaders + light comparison with other parties
- Adds a minimal corpus of other-party positions (e.g., from `pagellapolitica.it` or each party's official program) to answer "how does ORA differ from M5S on Y".
- Largest scope. Highest maintenance. Highest risk of becoming a generic political bot.

### D — ORA + leaders + Italian political-science explainers
- Adds a "civics" layer (constitutional structure, EU mechanisms, etc.) for context, but never speaks for other parties.
- Useful if target users include young/uninformed voters.

## What we'd need to know to choose

- Who is the target user? Party sympathizers, undecided voters, journalists, internal-party staff?
- What's the worst question to get wrong — "what does ORA think about X" or "how does ORA compare to Y"?
- Is there appetite (time, scraping work) to maintain other-party corpora?

## Reference

- KB concept: `15_political_chatbot_application.md`
- KB concept: `08_grounding_and_citation.md` (faithfulness & attribution)

## Observations
*(populated as exploration produces evidence)*
