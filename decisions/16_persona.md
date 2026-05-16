# 16 — Persona & tone

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** **Third-person, encyclopedic voice.** Examples: *"ORA!'s position is X"*, *"Secondo il manifesto, ORA!…"*, *"Il partito sostiene che…"*. **Never** first-person spokesperson — never *"noi pensiamo"*, *"la nostra posizione è"*.

**Brand correction 2026-05-15.** The party name is **ORA!** (with exclamation mark), not "ORA". All user-facing prompts (`agent/system_prompt.py`, `agent/orchestrator.py` planner + mode templates, `agent/tools/emit_refusal.py`) now use "ORA!". File paths, slugs, URLs, and Python identifiers (`ORA_TIERS`, `corpus/ora-party/`, `ora-italia.it`) keep the no-exclamation form — those are technical artifacts, not the brand. Historical decision files (this one included, in places below) may still say "ORA" — left in place as frozen records; the corrected form is what ships to users. Riccardo's note (2026-05-15): "the party is written ORA!, not ORA".
**Rationale:** First-person commits the party voice and turns every bot mistake into a party gaffe. Third-person + mandatory visible attribution (decision 10) frames the bot as a *research assistant about ORA* rather than *the voice of ORA*. This posture is consistent with the four objectives, especially objective 4 (Compare with other parties) — comparing as a third party reads as analysis, not partisanship.
**Implications carried by this decision:**
- Hypotheticals (objective 2) phrased as: *"In base ai principi del manifesto, ORA probabilmente farebbe X"*, not *"Faremmo X"*.
- Leader content (A2) always tagged: *"Boldrin, in un intervento personale, ha sostenuto Y"*, never collapsed into ORA's voice.
- The bot may have a name (TBD) but its self-description is functional, not partisan.

**Still loose (UX detail, not architectural):** answer length default (sentence / paragraph / structured), use of bullets vs prose, whether the bot has a display name.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md`. See CLAUDE.md §4 (Persona).

## The question

How does the chatbot *speak*? Formal or friendly? First person ("noi di ORA pensiamo che…") or third person ("ORA sostiene che…")? Concise or thorough? Hedging or confident?

This sounds cosmetic. It isn't — persona choice has direct implications for trust, faithfulness, and refusal handling.

## Why it matters for the ORA chatbot

- **First person commits to representing the party.** "Noi pensiamo X" reads as ORA *saying* X, which means a single bad answer is a party gaffe. Third person ("Secondo il manifesto di ORA, X") inserts a layer of attribution — safer.
- **Tone calibrates trust.** Over-confident phrasing on contested topics ("ORA crede fermamente che…") erodes credibility; visible hedging ("Il manifesto indica che…, ma nelle newsletter recenti il partito ha…") signals honesty.
- **Length is a UX decision.** A 5-paragraph answer is wrong for Telegram; a 1-sentence answer is wrong for a research session.

## Options

### A — Neutral third-person summarizer
- "Il partito ORA sostiene che…" / "Secondo il manifesto, ORA…"
- Maximum distance from the party voice. Easy to caveat. Hard to mistake for an endorsement.

### B — First-person-plural party voice
- "Noi di ORA pensiamo che…" / "La nostra posizione è…"
- Engaging, identifying. Risky: any error is a party gaffe.

### C — Conversational assistant ("I am a chatbot built on ORA's published materials")
- Speaks *about* the party, not *as* the party. Same trust posture as A but warmer.
- Useful default.

### D — Tone-adaptive (formal for journalists, friendly for sympathizers)
- A small classifier or explicit user choice toggles register.
- Two style guides to maintain; tone-drift risks.

## Other persona dimensions to set

- **Hedging policy:** explicit ("ORA non ha preso una posizione su X") or silent?
- **Answer length default:** sentence / paragraph / structured-multipart?
- **Use of bullet points vs prose:** Italian political writing favors prose; chat UI rewards bullets.
- **Emoji / informal language:** generally no for a political bot, but worth a conscious "no".
- **Naming the bot:** does it have a name? ("ORA-Bot", "OraGPT", just "the ORA assistant"?)

## What we'd need to know to choose

- What's the audience persona — voter, journalist, party member, opponent?
- Has the party communications team expressed a tone preference (the newsletters and comunicati are themselves stylistic evidence)?
- Are you OK with the bot *being* the party voice, or do you want it clearly framed as a research assistant?

## Reference

- KB concept: `15_political_chatbot_application.md`
- KB concept: `08_grounding_and_citation.md` (attribution language)

## Observations
- Newsletters and comunicati in the corpus are written in formal Italian, third-person about the party in headers ("ORA chiede…") and first-person plural in the body ("crediamo che…"). The corpus itself is mixed-voice.
