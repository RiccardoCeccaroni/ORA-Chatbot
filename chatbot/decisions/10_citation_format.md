# 10 — Citation format

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** **Visible source pills on every answer**, attribution mandatory. Each pill must identify the **tier + specific document** (e.g., "Tesi 06 — Energia", "Comunicato — Ponte di Messina, 2026-02-14", "Newsletter 2026-03-15", "Boldrin — personal view"). Web sources show the URL. The exact rendering (chip, footnote-style, hyperlink shape) depends on the chatbot interface's UI affordances but must remain visible — not hidden behind a "show sources" toggle by default.
**Rationale:** This is a high-trust product. Users must be able to verify every claim by clicking through. Visible pills also enforce internal discipline: if every claim must point to a source, hallucinations become visible. The tier label additionally surfaces the *attribution* distinction (party vs leader-personal) that decision 03 mandates.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md`. See CLAUDE.md §4 (Sourcing & persona rules).

## The question

When the chatbot makes a claim about ORA, **how does it show the user where that claim came from?**

This is the user-facing half of grounding. Internal grounding (decision 03 — trust hierarchy) handles which sources the bot trusts; citation format handles what the user *sees* afterward.

## Why it matters for the ORA chatbot

- In a political-information bot, citations are the single biggest trust signal. A user who can click through to the manifesto trusts the answer; a user staring at confident-sounding paragraphs without sources doesn't.
- Verifiability also disciplines the bot: if every claim must point to a source, hallucinated claims become visible.
- Different citation styles affect length and readability of answers — important for chat UX (mobile, voice).

## Options

### A — Inline numeric footnotes (`[1]`, `[2]`) with a sources list at the bottom
- Classic, compact, readable.
- User can scan the answer and check sources at the end.

### B — Inline links: each claim is a hyperlink to the source URL
- More immediate; clicking is one step instead of two.
- Visually noisy if there are many claims per sentence.

### C — Quoted snippets inline
- The bot quotes the original Italian sentence verbatim and then paraphrases / explains.
- Maximum faithfulness; longer answers; some users dislike walls of quotes.

### D — Sidebar / collapsible sources panel
- Answer text stays clean. A "sources" panel below or beside shows the retrieved chunks.
- Requires a richer UI than plain chat (depends on decision 14 — interface).

### E — Two-tier: short answer + "vedi fonti" expand
- One concise paragraph with no inline marks, plus a button to show the cited chunks.
- Mobile-friendly. Hides sources unless asked — a trade-off against trust.

## Sub-decisions baked in

- **Source identifier granularity:** cite the *document* ("Manifesto, sezione Immigrazione, 2026-01-09"), the *chunk* ("paragraph 3 of newsletter 2026-03-15"), or include a *verbatim quote*?
- **Linking:** if the source has a `source_url` (the corpus YAML frontmatter does), should the citation be clickable?
- **Date stamp:** always show the date of the cited source, so users can judge currency?
- **Attribution stamp:** always show whether it's party / leader-party-aligned / leader-personal (per decision 03)?

## What we'd need to know to choose

- Where will the bot be used (decision 14)? Plain-text channels (WhatsApp, Telegram) limit formatting; web UI can do rich.
- Is the audience expected to verify, or to read at face value?
- How long should a typical answer be — one paragraph or a structured several-paragraph response?

## Reference

- KB concept: `08_grounding_and_citation.md`
- KB concept: `15_political_chatbot_application.md`

## Observations
- Every markdown file in `memory/corpus/ora-party/` already has `source_url`, `date_published`, `title`, `id` in YAML frontmatter — citations can be auto-built from these fields.
- HTML files in `identity/` and `leaders/` may or may not have similar metadata — to be checked.
