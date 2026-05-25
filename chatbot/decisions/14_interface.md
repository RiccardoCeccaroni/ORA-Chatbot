# 14 — Interface

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** **Chatbot embedded on the ORA party website** (`ora-italia.it`). Public-facing.
**Rationale:** This is a product for the party, not a personal tool or internal-team utility. Embedding on the official site reaches the existing audience without asking users to install anything (Telegram bot, WhatsApp, etc.). It also matches the high-trust posture of decisions 03/10/16 — users arrive having already chosen to engage with the party's site, and citations point back to documents on the same domain.
**Implications carried by this decision:**
- Rich text rendering is available — citations can be hyperlinked source pills, not plain-text `[1]` footnotes.
- Latency budget is interactive-chat (~1–3 s), not research-tool (10–30 s).
- Hosting choice and any rate-limiting/abuse-handling depend on what infrastructure the party already runs for the site (TBD when implementation starts).

**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md`.

## The question

Where do users talk to the chatbot? CLI, web app, messaging platform, embed on a partner site, voice?

This is the *outer shell*. The RAG core (decisions 04–13) is the same regardless; the interface determines who reaches it, with what UX affordances, at what cost.

## Why it matters for the ORA chatbot

- Interface choice drives citation format (decision 10 — rich HTML vs plain text vs WhatsApp 4096-char limit).
- It also drives memory choice (decision 15 — does the channel give you a session ID?).
- And cost: a public web app needs hosting, rate limiting, abuse handling; a personal CLI needs none of that.

## Options

### A — Local CLI (Python script)
- For your own use during development. Zero infra.
- Not a deliverable product.

### B — Simple web app (Streamlit, Gradio, FastAPI + React)
- A page you can share. Auth optional.
- Best balance of features (rich formatting for citations) and effort.

### C — Telegram bot
- Italian audience uses it heavily. Streaming-style UX, free hosting via webhook.
- Plain-text + light markdown. Citations need to be condensed.

### D — WhatsApp bot
- Even broader Italian audience. Heavy hosting / API setup (Meta Business).
- Strong distribution if usage is the goal.

### E — Embed on `ora-italia.it`
- Iframe / widget on the party site. Reaches the existing audience without convincing them to install anything.
- Requires coordination with whoever runs the site.

### F — Voice (phone, Alexa, Google Assistant)
- Niche; high engineering cost; very different prompt design (no citations in speech).

## What we'd need to know to choose

- Is this a personal tool, an internal-party tool, or a public-facing tool?
- If public: who's the audience — sympathizers (Telegram/web), undecided voters (party site embed), journalists (web with download/quote features)?
- Who maintains it after you ship?
- Are you OK building two interfaces (a web demo + a Telegram bot)?

## Reference

- KB concept: `15_political_chatbot_application.md`
- KB concept: `14_production_concerns.md`

## Observations
*(record your distribution plan once you talk to whoever sets party comms strategy)*
