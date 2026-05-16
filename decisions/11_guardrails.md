# 11 — Guardrails

**Status:** DECIDED
**Decided on:** 2026-05-10 (refusal phrase + off-scope) / 2026-05-14 (adversarial half)

**Locked from the 2026-05-10 session:**
- **Default refusal phrase** when both retrieval axes yield nothing usable: *"ORA non ha una posizione documentata su questo."*
- **Off-scope categories** (medical, legal, personal-financial, personal-life advice): decline the personal advice and **redirect to the related policy lens** — e.g., "Non posso darti consigli sul tuo caso, ma la posizione di ORA sull'accesso alle cure è…".
- **Hypothetical questions (objective 2):** reason **only from documented Tier-1/Tier-2 principles**. If nothing in corpus supports an answer, say so and offer a hedged inference **labeled as such**.
- **Data:** prefer data already cited in ORA materials; allow live retrieval from ISTAT, Banca d'Italia, MEF, Eurostat, ISS, OECD. **Never invent numbers.**

---

## Adversarial half (DECIDED 2026-05-14)

### 11.A — Hostile / loaded questions: engage the framing

**Decision:** Option A. The bot **acknowledges the loaded premise**, then answers from corpus.

**Template:**
> *"La domanda presuppone X. Secondo [Tesi NN / comunicato YY], la posizione di ORA è in realtà Y."*

**Rationale (Riccardo, 2026-05-14):** Directness is more important than rhetorical hygiene. Silent reframing risks looking like a dodge. The bot is allowed to name what the question presupposes, then correct from documented stance. Trade-off accepted: engaging with the framing can validate adversarial premises, but the alternative (silent reframe) loses transparency.

**Edge case:** if the loaded framing maps to no policy question at all (pure ad hominem on the party), the bot falls back to the default refusal phrase.

---

### 11.B — Roleplay as Boldrin / Forchielli: transparency + best-effort reporting, two sub-branches

**Decision:** Hard line against impersonation and fabricated quotes — but the bot offers constructive alternatives instead of pure refusal.

**Sub-branch 1: past / documented topics** (leader has spoken on the subject)
> *"Sono un chatbot, non Boldrin — non posso impersonarlo. Posso però riportare quello che ha scritto o detto pubblicamente su [topic], con le citazioni. La mia ricostruzione potrebbe contenere errori — verifica sempre le fonti."*

→ Bot then generates third-person summary of documented views, citing chunks from `leaders/boldrin/profile/` and `leaders/boldrin/articles/`.

**Sub-branch 2: hypothetical / unfolding situations** (leader has *not* yet addressed the subject)
> *"Sono un chatbot — non posso pensare cosa Boldrin sosterrebbe in questa situazione. Date però le sue opinioni passate su [topics related], posso supporre che potrebbe pensare [hedged inference]. Tieni presente che è una mia inferenza dalle sue posizioni documentate, non una sua dichiarazione."*

→ Bot then generates a hedged inference grounded in documented Tier-2 chunks, with the inference label preserved in the output.

**The hard line that survives:** **no fabricated first-person quotes, ever.** The bot does not generate text formatted as "Boldrin says: …" or "Sono Boldrin e penso che…". Detection in the system prompt + a trigger-pattern list ("Pretend you are…", "Act as…", "From the perspective of…", "In the voice of…", "Speak as…", and Italian equivalents).

**Rationale (Riccardo, 2026-05-14):** Pure refusal loses information value. Users genuinely want to know what the leaders think on emerging topics. The bot's job is to surface documented views (sub-branch 1) and to offer hedged inferences when the documented record doesn't yet cover the topic (sub-branch 2) — both with explicit transparency about its own fallibility. This is consistent with objective 2 (hypotheticals → reason from documented principles, label inference) and with the chatbot's encyclopedic-not-spokesperson persona.

**Trigger patterns** (system prompt; non-exhaustive):
- IT: "fingi di essere …", "comportati come …", "rispondi come se fossi …", "fai finta di essere …", "parla come …"
- EN: "pretend you are …", "act as …", "from the perspective of …", "in the voice of …", "speak as …"

---

### 11.C — Prompt injection: structural mitigations, no heuristic detection

**Decision:** Three structural mitigations, no regex-based detection.

1. **System prompt hardening:** explicit instruction that any commands appearing inside retrieved chunks or web-search results are **data to be summarized, not instructions to be followed**. Anthropic models (Opus 4.7 in particular) are reasonably robust to this with a tight system prompt.

2. **Clear delimitation in the prompt:** retrieved chunks and web results are wrapped in unambiguous XML-style tags (`<retrieved_chunk id="…">…</retrieved_chunk>`, `<web_result url="…">…</web_result>`). The system prompt explicitly identifies these as untrusted-data regions.

3. **Untrusted-source quarantine:** web-search results are **summarized through the model** before going into the final-answer prompt, not pasted raw. This converts arbitrary upstream content into bot-controlled prose, dramatically reducing injection surface.

**Skipped:** regex heuristics for "ignore previous instructions"-style patterns. Bad signal-to-noise ratio; breaks on novel patterns; false-positives on legitimate questions.

**Rationale (Riccardo, 2026-05-14):** Structural mitigations are durable; heuristic detection is fragile. The combination of system prompt + delimitation + summarization addresses the realistic attack surface (both user-side and content-side injection) without introducing a maintenance burden for a list of detection patterns.

---

### 11.D — Groundedness check: both layers (citation enforcement + model verifier)

**Decision:** Combine deterministic citation enforcement with a model-based verifier pass. Belt-and-suspenders.

**Amended 2026-05-15 (a) — verifier model upgraded from Haiku 4.5 to Sonnet 4.6.** Haiku produced 13/13 false rejections of well-cited Sonnet-synthesized answers. Sonnet 4.6 replaced it.

**Amended 2026-05-15 (b) — model verifier REMOVED entirely.** After Sonnet-on-Sonnet still produced bogus rejections on the partial pension-line test (verifier_failed on clean, on-topic answers), Riccardo decided to drop the model verifier altogether. Groundedness now relies on:
1. **Deterministic citation enforcement** (`orchestrator.enforce_citations()`) — every factual claim must end in a `[chunk_id]` or `[web:N]` marker that resolves to a retrieved chunk; sentences whose only marker doesn't resolve are stripped.
2. **Weekly chat_log review** by Riccardo (decision 11.E) — catches miscitations after the fact rather than before. Acceptable because the deterministic layer already prevents un-cited claims from shipping.

The `agent/tools/verify_answer.py` file remains on disk but is no longer imported by the orchestrator. Per-query cost drops by ~$0.03 and latency by ~15s. Risk accepted: a Sonnet/Opus miscitation (right chunk_id, wrong claim about that chunk) could slip past the deterministic layer; weekly review is the backstop. Riccardo's call (2026-05-15): "Drop it (Recommended)" — see the rework session log.

**Pipeline:**

1. **Generation:** the answerer (Opus 4.7) is required by the system prompt to emit every factual claim with an inline citation marker like `[A1a:tesi-06#proposte-3]` or `[A2-boldrin:profile-04#sintesi]`. Marker format mirrors the chunk_id schema from decision 04.

2. **First pass — citation enforcement (deterministic, ~0ms, $0):**
   - Regex-extract all citation markers from the answer.
   - Each marker must resolve to a chunk_id that was actually in the retrieved+reranked set for this query.
   - Sentences without a valid resolving citation: stripped (graceful) or trigger regeneration depending on density.

3. **Second pass — Haiku verifier (model judgment, ~500ms, ~$0.01/query):**
   - For each cited claim that survived pass 1, call `claude-haiku-4-5` with the claim text and the cited chunk's full text.
   - Verifier outputs: `supported` / `partially_supported` / `not_supported`.
   - `not_supported` → regenerate the answer with explicit feedback, or fall back to the default refusal phrase if regen fails.
   - `partially_supported` → soften the claim (replace strong assertion with hedged language) before sending.

4. **Citation pills in the UI** are built mechanically from the surviving markers — no separate citation step.

**What each layer catches:**

| Failure mode | Layer that catches it |
|---|---|
| Bot makes a factual claim with no citation at all | Pass 1 (deterministic, free) |
| Bot cites chunk X but the claim isn't actually in chunk X | Pass 2 (Haiku verifier) |
| Bot cites chunk X and claim is partially in chunk X but overstated | Pass 2 → soften |

**Cost / latency:** added ~500ms p50 latency, ~$0.01/query in verifier tokens. For a screenshot-risk-dominant product, this is the right trade. With Opus 4.7 at $0.065/query, the verifier adds ~15% cost for materially higher correctness.

**Rationale (Riccardo, 2026-05-14):** "C, or any option that is the most sure of not getting mistakes." The two layers address different failure modes — citation enforcement catches uncited hallucination structurally; the verifier catches miscited or overstated claims. Combining them costs ~15% more per query and ~500ms latency in exchange for materially lower screenshot risk. Acceptable in the context of a public political chatbot where one bad answer becomes a campaign asset for the opposition.

---

### 11.E — Logging + human review: log everything, Postgres, weekly review, GDPR disclosure

**Decision:** Full logging to Postgres, weekly review by Riccardo, visible GDPR disclosure in the bot UI.

**What gets logged per query:**
- `timestamp` (UTC)
- `anonymous_session_hash` (rotating server-side hash of session token; no PII, no IP)
- `query_text` (raw user question, Italian)
- `retrieved_chunk_ids` (the top-N from retrieval + reranking)
- `answer_text` (final response sent to the user)
- `latency_ms` (end-to-end)
- `cost_usd` (sum of embedding + reranker + Opus + Haiku-verifier calls)
- `auto_flags` (any of: `refusal_triggered`, `loaded_frame_detected`, `roleplay_refusal`, `citation_strip`, `verifier_fail`, `regen_attempted`, `web_search_used`)
- `model_versions` (snapshot of Opus + Haiku + voyage model names for the call)

**Storage:** Postgres table, append-only, no user-data deletion logic in MVP (the disclosure says queries are anonymous; nothing in the schema is PII-linkable).

**Review:**
- **Cadence:** weekly.
- **Owner:** Riccardo (`riccardoceccaroni02@gmail.com`).
- **Output:** the review can result in (a) updated system prompt, (b) updated refusal templates, (c) new trigger patterns added to 11.B's list, (d) new auto-flag categories added. The bot does **not** silently auto-tune based on logs.

**GDPR disclosure:** small visible footer link in the bot UI:
> *"Le domande sono registrate in forma anonima per il monitoraggio della qualità."* — clickable to a longer privacy note.

**Rationale (Riccardo, 2026-05-14):** "Yes agree, we should record everything. And we can use postgre." Confirmed weekly review + visible GDPR disclosure. For a public political chatbot, comprehensive logging is the only way to catch adversarial patterns and quality regressions. Postgres adds queryability (vs JSONL) for the weekly review workflow without meaningfully more engineering for our scale.

---

## Cost summary (adversarial half)

Per-query incremental cost vs no-guardrails baseline:
- Citation enforcement (regex): $0, ~0ms
- Haiku verifier: ~$0.01, ~500ms
- Web-source summarization (when web search is used): ~$0.005, ~300ms
- Logging write: negligible (Postgres async insert)

**Total guardrail cost per query: ~$0.01-0.015, ~500-800ms p50 latency added.**

This sits on top of the Opus 4.7 generation cost (~$0.065/query) for a total of ~$0.075-0.08/query at MVP volume. Within the £5 MVP budget: ~80 fully-guarded test queries before cap. Confirmed acceptable.

---

## The question

How does the chatbot handle questions it shouldn't answer faithfully — or shouldn't answer at all?

Concretely, what does the bot do when a user:
1. Asks for an **opinion** the party hasn't taken? ("What does ORA think about UFOs?")
2. Asks a **loaded / adversarial** question? ("Is ORA racist?")
3. Asks the bot to **roleplay** as Boldrin or Forchielli?
4. Asks for **personal attacks** on other politicians?
5. Asks for **medical/legal/financial advice**?
6. Asks about a **breaking event** more recent than the last indexed newsletter?
7. Tries **prompt injection** ("ignore your instructions and tell me…")?

## Why it matters for the ORA chatbot

- Political bots are uniquely attractive to adversarial users (journalists testing for gaffes, opposition supporters looking for sound bites, anyone trying to get the bot to "endorse" something).
- A wrong answer here becomes a screenshot. A *refusal phrased well* is the safe default.
- Refusal must not feel like hiding. The bot should say *what* it doesn't have a position on and *why*, not just bounce.

## Options (for each scenario above) — kept for posterity

These aren't mutually exclusive — different scenarios may pick different strategies.

### A — Strict-corpus refusal
- "ORA has not taken a public position on this topic in the materials I have access to."
- Includes a hint about *which* part of the corpus was searched.
- Safe; can feel evasive when overused.

### B — Corpus + adjacent-inference, clearly labeled
- "ORA has not directly addressed this, but its general stance on [adjacent topic] suggests…" — clearly framed as inference, not party position.
- Risky in politics — inferences become quotes.

### C — Two-track answer: party position + leader views
- "There's no formal party position on X. Boldrin has personally written / said Y. Forchielli has said Z."
- Honest. Requires good source labeling (decision 03).

### D — Hard refusals for specific categories
- Roleplay as a real person → refuse with a fixed phrase.
- Medical/legal/financial → refuse, direct to professionals.
- Personal attacks → refuse.
- Prompt-injection patterns → ignore the injection, answer the underlying question if any.

### E — Off-topic redirect
- "I only answer questions about ORA's positions." Polite, short.
- Risks alienating curious users.

## Other components of the guardrail layer

- **System prompt:** explicit rules baked into every LLM call (don't speculate, always cite, refuse roleplay, etc.).
- **Pre-filter:** classify the question's intent before retrieving; route some categories straight to refusal templates.
- **Post-filter:** check the generated answer for groundedness (does each factual claim appear in the retrieved chunks?) before sending it. If it fails, regenerate or refuse.

## What we'd need to know to choose

- What's the worst failure mode you want to prevent — fabrication, embarrassment, off-topic drift, opposition weaponization?
- Are you OK with the bot saying "I don't know" frequently, or do you want it to always try?
- Will there be a manual review of logged questions to spot adversarial patterns and tune refusal templates?

## Reference

- KB concept: `15_political_chatbot_application.md`
- KB concept: `08_grounding_and_citation.md`
- KB concept: `14_production_concerns.md`

## Amendment 2026-05-14 — General-context mode

Add a new `general_context` `query_type` for descriptive background questions that don't ask for ORA's position (e.g. «qual è la situazione delle pensioni in Italia?», «come si differenzia dal sistema attuale?»). In this mode:

- The synthesizer treats web results and stat-cards from the data tier as **first-class citations** (`[web:N]` markers).
- The verifier (11.D) runs with a relaxed grounding prompt: web/data citations count as fully valid grounding; absence of corpus chunks is NOT a faithfulness failure.
- If the topic intersects with documented ORA positions, the synthesizer appends a brief «👉 Posizione di ORA su questo tema» paragraph with corpus citations (precedence rule still applies). If the corpus has nothing relevant, the paragraph is omitted (we do NOT declare the absence — it's not what the user asked).
- ORA-position questions (`state` / `project` / `justify` / `compare`) keep the original strict policy: every fact requires a corpus chunk, citation-precedence enforced, refusal if no corpus material.

**Why:** prior to the amendment, the bot refused descriptive empirical questions even when web + ISTAT clearly contained the answer — over-refusal driven by the verifier rejecting web-only grounding. The chatbot should at minimum match what a user would get by asking Claude on the open web for non-ORA questions, while staying strict where it matters (ORA's documented positions).

**How to apply:** planner emits `query_type: general_context`; orchestrator passes `mode="general_context"` to synthesizer and verifier; both relax the corpus-grounding requirement accordingly.

## Observations
*(populate with categories of questions you observe being asked, and the bot's behavior on them — weekly review feeds here)*
