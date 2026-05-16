# 02 — Language(s)

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** **Italian** for product (chatbot UI, corpus, user-facing answers). **English** for working conversations with Riccardo and for decision files / specs.
**Rationale:** Audience is Italian voters; corpus is Italian; the bot is embedded on `ora-italia.it`. There is no English-speaking constituency that justifies maintaining a second answer-language quality bar. Conversation-language English keeps Claude's instruction-following stronger and matches Riccardo's preference.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md` and `user_working_style.md`. See CLAUDE.md §4 (Persona) and §7 (Working language).

## The question

What languages does the chatbot accept as input and produce as output?

The corpus is **overwhelmingly Italian**. The decision is about:
1. Italian only?
2. Italian + English (e.g., for journalists, expat Italians, international observers)?
3. Italian-input/Italian-output but accept English questions and translate internally?

## Why it matters for the ORA chatbot

- **Embedding model choice depends on this** (decision 05). An English-only embedding model would lose information; a multilingual one is a different short-list (e5-multilingual, Cohere multilingual, OpenAI `text-embedding-3-*` which is multilingual, …).
- **Generation model choice depends on this** (decision 09). Most frontier LLMs handle Italian well, but quality varies. Open-weight options are weaker.
- **Citation faithfulness gets harder cross-language.** If the bot answers in English citing an Italian source, the user sees a paraphrase, not a quote — harder to verify.
- **The party operates in Italian.** An English answer might paraphrase party positions in ways that lose nuance ("liberale" ≠ "liberal").

## Options

### A — Italian-only
- Simplest. Faithful to corpus language. Cheapest embedding/generation.
- Excludes English-speaking users.

### B — Italian-first, accept English input → answer in Italian
- Broader reach, single answer-language to maintain.
- Users get answers in a language they may not read.

### C — Italian-first, answer in the language of the question
- Best UX, hardest to keep faithful. English answers must quote Italian sources verbatim alongside translations.
- Roughly 2× the eval effort (need a quality bar in each language).

### D — Multilingual from the start (IT, EN, plus minority languages spoken in Italy)
- Maximum reach. Disproportionate cost.
- Probably overkill unless there's a specific reason.

## What we'd need to know to choose

- Who do you imagine asking it questions?
- Is there an English-speaking constituency (foreign press, EU policy observers) that matters?
- Are you willing to maintain answer quality in more than one language?

## Reference

- KB concept: `04_embeddings_and_vector_search.md` (multilingual embeddings)
- KB concept: `15_political_chatbot_application.md`

## Observations
- Corpus content: manifesto, comunicati, newsletter — all Italian.
- Identity HTML pages: mixed (wikipedia entries exist in EN and IT).
- Leader content: Boldrin/Forchielli speak primarily Italian on YouTube; some written work in English.
