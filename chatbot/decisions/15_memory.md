# 15 — Conversation memory

**Status:** DECIDED
**Decided on:** 2026-05-14
**Decision:** **In-session memory via 10-turn sliding window; no cross-session memory; 30-minute idle timeout plus explicit "Nuova conversazione" button.** Aggregate logging is already locked in decision 11.E (Postgres, anonymous, weekly review).

The three sub-questions:

| Sub-question | Decision |
|---|---|
| In-session memory (turn N knows about turn 1?) | **B — sliding window of last 10 turns, verbatim, no summarization** |
| Cross-session memory (returning users) | **E — no, every session starts fresh** |
| Aggregate logging | locked in #11.E (Postgres, anonymous, weekly review) |
| Session boundary | 30 minutes idle OR explicit "Nuova conversazione" button OR browser session ends |

---

## How it integrates with the agent (#23)

The agent flow locked in decision 23 is **stateless per query** — each query is processed independently. In-session memory is a small additive change concentrated in Stage 1 (intent + plan):

**At session boundary (new session begins):**
- Empty `conversation_history` list
- New `session_id` (rotating anonymous hash per #11.E)

**Per turn during a session:**
1. Receive `user_query` (Italian, raw).
2. Look up `conversation_history` (list of last 10 `{role, content, chunk_ids}` entries).
3. Build agent prompt with `conversation_history` prepended to the new query.
4. **Stage 1 of the agent flow now does two things:**
   - **Resolve the query** against the history (disambiguate pronouns, "and what about X" follow-ups, "specificamente" qualifiers). Example: prior turn was *"Cosa propone ORA sull'energia?"*, current turn is *"e per il nucleare?"* → Stage 1 resolves to *"Cosa propone ORA sull'energia nucleare?"*
   - **Then classify** the resolved query as before (intent, tier filters, adversarial flags, etc.).
5. Stages 2-8 receive the **resolved query**, not the raw user input. Retrieval, synthesis, verify all use the disambiguated form.
6. **Postgres log per #11.E now stores both** `raw_user_query` AND `resolved_query` — useful for the weekly review (you see what the bot thought the user meant).
7. After answer is sent: append `{role: assistant, content: answer, chunk_ids: [...]}` to `conversation_history`. If list now exceeds 10 entries, drop the oldest.

**Session storage:** in-process per browser session (server-side session token tied to anonymous hash). Flushed to Postgres on each turn for log + recovery if the process restarts. **No Redis needed at MVP scale.**

**Session lifetime:** 30 minutes of inactivity OR explicit "Nuova conversazione" button click OR browser session ends. On expiry: `conversation_history` cleared, new `session_id` issued.

---

## Cost & latency impact

| Dimension | Without memory (decision 23 baseline) | With 10-turn memory |
|---|---|---|
| Per-query input tokens | ~10K | ~12-13K (add ~2-3K for history) |
| Per-query cost (uncached) | $0.10 | $0.11-0.12 (+$0.01-0.015) |
| Per-query cost (cached) | $0.04 | $0.045-0.05 |
| Latency | ~2-3s | ~2-3s (history doesn't add a network call) |

Within the £5 MVP cap: ~80-90 cached queries instead of ~100. Still comfortable.

---

## Privacy / GDPR notes

- **No PII storage.** Conversation history lives only in the anonymized session table — no IP, no name, no email.
- **30-minute idle expiry** ensures memory is short-lived even within a single user's interactions.
- **No cross-session** means a returning user is, from the bot's perspective, a new user every session.
- **Visible disclosure** per #11.E already covers the logging side: *"Le domande sono registrate in forma anonima per il monitoraggio della qualità."*
- **No additional consent flow needed.** Because there's no cross-session memory and no PII, the GDPR surface is limited to the logging disclosure already locked.

---

## Rationale

**In-session B (10-turn window):**
- Truly stateless (A) breaks normal chat behavior — follow-up questions fail. Bad UX for a public-facing chatbot.
- Summarization (C) is needed only when conversations exceed context budget. Opus 4.7's 200K context absorbs 10 turns trivially; summarization adds complexity for no MVP benefit.
- 10 turns is generous for a Q&A-shaped bot. Most political-information conversations are 3-5 turns. The 10-turn ceiling rarely binds in practice, but provides headroom for power-users.

**No cross-session (E):**
- Opt-in cross-session memory (D) would require: a user-profile schema, consent flow, privacy policy update, data-retention policy, user-deletion endpoint per GDPR Art. 17. Real work for marginal UX benefit on a Q&A bot where most users have a single question to ask.
- For an opposition-monitored political product, *less* persistent user data is a feature, not a bug.
- Reversible later: if eval (#12 stage 2) shows users want it, the in-session-only design extends cleanly to opt-in cross-session without rewriting the agent.

**30-min idle timeout + explicit button:**
- 30 min is the standard "abandoned conversation" threshold across most chatbots.
- Explicit button gives the user agency. Important for political topics where a user may want to start clean ("I want to ask about something completely different and don't want context bleed").
- Browser session end is the universal safety net.

**Why the resolve-then-classify pattern in Stage 1:**
- Disambiguates *before* retrieval. If we pass "e per il nucleare?" raw to corpus retrieval, dense embedding misses; if we pass the resolved "Cosa propone ORA sull'energia nucleare?", retrieval hits the right tesi.
- Keeps the rest of the agent flow (Stages 2-8) unaware of conversation history — single point of complexity, easy to reason about.
- Both raw and resolved queries logged for weekly review per #11.E — visibility into how the bot interpreted ambiguous follow-ups.

---

## Migration triggers (when to revisit)

- **Eval (#12) shows users routinely hitting the 10-turn ceiling.** → Add summarization (option C) for older turns.
- **Users explicitly request cross-session memory ("the bot doesn't remember me").** → Reopen for opt-in profile (option D), with the corresponding privacy work.
- **Multi-user / shared-device concerns** (e.g., the bot is deployed in a kiosk where multiple people use the same browser). → Tighten session timeout or require explicit "start" action per user.
- **Cost at steady-state public traffic** if the +$0.01-0.015/query history overhead becomes material. → Reduce window from 10 to 5 turns, or move history to a summarization scheme.

---

## Reference

- KB concept: `12_agentic_patterns_architectures.md` (memory modules in agentic RAG)
- KB concept: `14_production_concerns.md`
- KB concept: `15_political_chatbot_application.md`
- Cross-references: #11.E (logging design — what gets stored regardless of memory choice), #23 (agent flow — Stage 1 modified by this decision)

## Observations
*(populate during MVP demo runs — note how often follow-up questions appear, average session length, whether 10-turn window proves enough)*
