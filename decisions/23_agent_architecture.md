# 23 — Agent architecture

**Status:** DECIDED
**Decided on:** 2026-05-14
**Decision:** **Single Anthropic-SDK-native agent organized as a structured workflow** (Anthropic's terminology: prompt chaining + routing + evaluator-optimizer). One Opus 4.7 brain making decisions across stages, five named tools, deterministic post-processing for citations, Haiku verifier loop for self-checking. No agent framework — custom Python orchestration (~300 lines).

**Amended 2026-05-15 (a) — verifier regen briefly disabled (`VERIFIER_MAX_REGEN = 0`).** Synthesizer also flipped from Opus to Sonnet for the test round (see decision 09 amendment). Rationale at the time: showcase eval (2026-05-14 runs) showed verifier-fail → regen → still-fail → refusal taking 90–115s while landing on a refusal anyway. Riccardo's call: drop the retry.

**Amended 2026-05-15 (b) — regen reverted to 1, verifier model upgraded to Sonnet 4.6.** Brief intermediate state.

**Amended 2026-05-15 (c) — agent rework. 6 stages → 4. Verifier removed. New `focus_topic` field. Opus everywhere.**

Following observed failures across (a) and (b) — Sonnet over-inclusive synthesis (nuclear question got renewables-reframing), Sonnet-on-Sonnet verifier still producing false `verifier_failed` refusals on clean answers — Riccardo decided to simplify the architecture rather than keep tuning model choices.

**The new flow:**

```
1. Plan (Opus 4.7)        — adds new field `focus_topic`: the narrow aspect the user is zooming
                             on (e.g., "nucleare nello specifico; non reinquadrare con rinnovabili").
                             Empty when the question is broad or independent.
                             The PLAN_TOOL schema also got an expanded tier_filters description
                             enumerating all 14 ORA tiers (the prior version listed only 7,
                             leaving event/article/identity-extension tiers invisible to the planner).
2. Parallel retrieve      — unchanged (corpus_retrieve + web_search + optional data_lookup).
3. Synthesize (Opus 4.7)  — receives focus_topic; when non-empty, the user template injects a
                             "Restringimento di focus" block instructing Opus to stay on the narrow
                             aspect and not reframe with the broader context.
4. Enforce citations      — unchanged deterministic regex pass. Now the SOLE groundedness layer.
                             If everything gets stripped, emit_refusal(no_corpus_position).
```

**What was removed:** the Haiku/Sonnet verifier, the regen loop, the feedback-back-to-synthesizer mechanism. `VERIFIER_MAX_REGEN` stays in `constants.py` at 0 for legacy compatibility but is unread.

**System-prompt corrections applied alongside the rework:** synthesizer inventory was off on two counts (6→9 Boldrin video monologues; 7→8 other parties). Planner schema's `tier_filters` description was missing 8 of the 14 ORA tiers (A1c-event, A1-contacts, A1-statuto, A1-fondamenti, A1-codice-etico, A2-boldrin-article, A2-boldrin-event, A2-forchielli-event). Now complete with one-line descriptions of each.

**Expected effects:** ~50-60s per query (no verifier, no regen), ~$0.22/query (Opus dominant but only one big call). Sharper narrowing on follow-up questions (the focus_topic mechanism).

**Trade-off accepted:** miscitation risk (Opus cites real chunk_id but misrepresents the chunk's content) is now caught only by deterministic citation enforcement (which catches uncited claims) + weekly chat_log review (decision 11.E). The model verifier was supposed to catch this case but its false-positive rate made it net-negative.

Riccardo's calls (2026-05-15): "Agent orchestration (Recommended)" + "Drop it (Recommended)" + "Opus everywhere (Recommended)" from the rethink Q&A, plus a separate audit-then-fix instruction to ensure the agent knows about every tier in the corpus.

**Amended 2026-05-15 (d) — no meta-commentary on leader-vs-party divergence.** The synthesizer was producing didactic asides like «aggiunge però due elementi che sono posizioni personali e non risultano nelle tesi di ORA» whenever a leader's view extended past the party's documented position. Riccardo's call: stop the meta-commentary. Attribution alone («Forchielli ha sostenuto...», «Boldrin ha scritto in un video del [...]...») already communicates that the content is the leader's voice, not the party's. Meta-commentary only when the divergence is **palese e materiale** (party explicitly says X, leader explicitly says NOT X on the same point) AND useful for the user's question. The "Never blur leader opinion with party position" rule from §4 / decision 23 still holds — clear attribution remains mandatory; what's dropped is the editorial framing on top of it. Encoded in `agent/system_prompt.py` under "Niente meta-commentario sulla divergenza".

This decision specifies the *shape* of the agent that was paradigm-locked in decision 08 (Agentic RAG with two-axis parallel retrieval).

---

## The agent flow (9 stages)

```
USER QUERY (Italian)
      │
      ▼
[1. Intent + plan]                        internal reasoning (Opus 4.7)
   The agent reflects on:
     • What is the user actually trying to know?
       — query_type ∈ {state, project, justify, compare, refusal-likely, off-scope, adversarial}
     • Is this an empirical question requiring data? (yes/no)
     • Which corpus tiers are most relevant?
       — tier_filters ⊆ {A1a, A1b, A1c, A1-identity, A2-boldrin, A2-forchielli, data, other-parties}
     • Is this adversarial? (loaded / roleplay / injection) → routes to #11 templates
     • Clear off-scope? → emit_refusal immediately, skip retrieval
      │
      ▼
[2. Corpus retrieval]                     tool: corpus_retrieve
   Dense+rerank with tier filters from Stage 1.
   Returns top-5-10 reranked chunks with metadata.
      │
      ▼
[3. Data tier lookup, IF Stage 1 marked empirical]   tool: data_lookup
   Retrieves D1-D4 stat-cards per decision 17.
   Agent then reflects: are these data methodologically sound and on-point for the query?
      │
      ▼
[4. Reflect on retrieval]                 internal reasoning (Opus 4.7)
   Agent reads the retrieved chunks/data and asks:
     • Do these chunks actually address the question?
     • Are there gaps I need to fill?
     • Does the answer require comparison material I don't have? (objective 4)
      │
      ▼
[5. Web search]                           tool: web_search
   Triggered:
     • ALWAYS in parallel with Stage 2 (per locked decision 03 two-axis design).
     • PLUS agent can invoke additional targeted web searches if Stage 4 flagged gaps.
   Web results SUMMARIZED through Haiku per #11.C (untrusted-source quarantine).
      │
      ▼
[6. Synthesize answer]                    Opus 4.7 generation
   Inputs: classified query + reranked chunks + data + summarized web + persona system prompt
   Output: Italian answer with inline [chunk_id] citation markers.
   Synthesis applies the ORA citation-precedence rule (below) and the
   "only what we're sure about" principle (below).
      │
      ▼
[7. Citation enforcement]                 deterministic regex per #11.D
   Strip claims without resolving markers.
   Track strip rate; if >X% of claims stripped, mark for regen.
      │
      ▼
[8. Combined verify]                      tool: verify_answer (Haiku 4.5)
   ONE Haiku call returning two structured scores:
     • FAITHFULNESS: each cited claim supported by its chunk? (per #11.D)
     • RELEVANCE: does the answer address the user's actual question?
   If either fails → regen once → if still fails → emit_refusal.
      │
      ▼
[9. Format pills + log + return]          deterministic
   Build citation pills from surviving markers.
   Append full log entry to Postgres per #11.E.
   Return answer + pills to UI.
```

Per query: ~3-5 LLM calls, ~$0.07-0.10, ~2-3s end-to-end at MVP volume.

---

## Tool inventory (5 tools — extended to 6 by decision 24)

Anthropic's playbook: invest in tool descriptions as much as in HCI; keep count small; clear separation between tools. Tools are documented "as if for a junior developer."

> **Forward-pointer (2026-05-15):** Decision 24 added a 6th tool — `contact_lookup` — for the new contacts/routing capability. Its spec lives in `decisions/24_contacts.md`. The five tools below are unchanged; `contact_lookup` is a deterministic key→value lookup over a JSON file (no LLM, no ANN). When implementing the agent, update this section to list six.

### `corpus_retrieve`
```
corpus_retrieve(
  query: str,                              # Italian query, optionally classifier-rewritten
  tier_filter: list[str] = None,           # subset of A1a/A1b/A1c/A1-identity/A2-boldrin/A2-forchielli/data/other-parties; null = all
  attribution_filter: list[str] = None,    # e.g. ["party"] or ["boldrin","forchielli"]
  date_range: tuple[date, date] = None,    # bounded by date_published; null = no bound
  top_k: int = 10                          # post-rerank
) -> list[Chunk]                           # each carries text, chunk_id, parent_id, tier, attribution, source_url, date_published, content_hash, extras
```
Wraps Qdrant dense ANN + voyage-rerank-2.5. Tier filters applied as Qdrant payload pre-filter before ANN.

### `data_lookup`
```
data_lookup(
  metric: str,                             # e.g. "tasso di occupazione"
  period: str = None,                      # e.g. "2024" or "Q1 2025"
  source_tier_preference: list[str] = ["D1","D2","D3"]   # per decision 17 tier rules
) -> list[StatCard]
```
Separate tool because the data tier has its own contradicting-rules per #17 (D1/D2/D3/D4). The agent calls this when Stage 1 marked the question as empirical. Returns stat-cards with `quality_tier`, `data_period`, `data_metric`, `source_doc`, methodological caveats.

### `web_search`
```
web_search(
  query: str,
  max_results: int = 5,
  domain_preference: list[str] = None      # e.g. ["istat.it","bancaditalia.it"] for empirical, or other-party domains for comparison
) -> list[WebResult]                       # each WebResult is ALREADY summarized through Haiku per #11.C
```
The summarization-through-Haiku is **inside the tool** — the agent never sees raw web HTML. Result objects carry the summarized text + source URL + fetch timestamp. Always-parallel invocation in Stage 5 plus agent-initiated additional searches.

### `verify_answer`
```
verify_answer(
  answer_text: str,                        # the synthesized Italian answer
  original_query: str,
  cited_chunks: list[Chunk]                # chunks corresponding to the markers in the answer
) -> {
  faithfulness: {pass: bool, per_claim: list[{claim, chunk_id, status: "supported"|"partial"|"not_supported", reason}]},
  relevance: {pass: bool, score: 0|0.5|1, reason: str}
}
```
Single Haiku 4.5 call producing both scores in structured output (Anthropic tool-use JSON schema). Cheaper than two separate calls. Both scores must pass; either fails → regen once → if still fails → emit_refusal.

### `emit_refusal`
```
emit_refusal(
  reason: "no_corpus_position" | "off_scope" | "roleplay" | "loaded_no_underlying_policy" | "verifier_failed" | "data_unavailable" | "comparison_other_party_unknown",
  related_topic_lens: str = None           # for off_scope redirect to a policy lens
) -> str                                   # the Italian refusal template
```
Templates per #11. Includes the default refusal phrase, off-scope redirect, roleplay chatbot-transparency phrase, hedged-inference fallback. Centralized so phrasing stays consistent and is updateable in one place.

### Intentionally NOT tools

- **Intent classification** → inline reasoning in Stage 1, no tool call (saves an LLM call + ~300ms).
- **Citation enforcement** → deterministic regex in Stage 7, no tool call.
- **Inventory awareness** → encoded in the system prompt with prompt caching.

---

## System prompt structure

The system prompt is **prompt-cached** (per decision 09's caching strategy — 90% discount on cache reads). It contains:

1. **Persona** (decision 16): third-person, encyclopedic, never first-person spokesperson; Italian language.
2. **Corpus inventory** (static description):
   > *"You have access to the following retrievable corpus through `corpus_retrieve`:
   > - 20 ORA tesi programmatiche covering [list of topics from manifesto files]
   > - 26 ORA comunicati (press releases)
   > - 34 ORA newsletter sections
   > - 1 ORA identity card
   > - 26 Boldrin topic profiles tesi-aligned + 131 historical articles 2006-2014
   > - 21 Forchielli topic profiles tesi-aligned
   > - 7 other parties' topic profiles (PD, M5S, FdI, Lega, FI, AVS, Azione, IV) across ~140 documents
   > - 133 data stat-cards across 21 topics, tiered D1-D4 (ISTAT-led)
   > Plus live web search via `web_search` for currency and gap-filling."*
3. **Citation-precedence rule (ORA-scoped, see below).**
4. **"Only what we're sure about" principle (see below).**
5. **Guardrail dispatch** (#11 templates and triggers).
6. **Tool descriptions** (one per tool, per Anthropic ACI guidance).
7. **Output format**: Italian, with inline `[chunk_id]` citation markers on every factual claim.

---

## Citation-precedence rule (ORA-scoped only)

Applies **only when speaking about ORA itself** (not when comparing with other parties, where each party's positions come from its own materials in `other-parties/<party>/profile/`).

| Situation | Behavior |
|---|---|
| Only party (A1) has a position | Cite party only |
| Only leaders (A2) have a position (gap-filling) | Cite leader, labeled as **personal view** ("posizione personale di Boldrin / Forchielli") |
| Party AND leaders both have positions AND they **agree** | Cite **both, party first**, then leader as supporting view |
| Party AND leaders both have positions AND they **contradict** | Cite **party only**; mention leader divergence **only if the user explicitly asks** |

**Why this is stricter than CLAUDE.md §4's prior version:** the older rule allowed surfacing divergence "if the divergence is publicly notable" — Riccardo removed that exception (2026-05-14). For a centrist party that must project unity to opposition-facing screenshots, only an explicit user request surfaces internal disagreement.

**For comparison questions (objective 4 — ORA vs other parties):** the rule above does not apply. Each party's positions are cited from its own corpus tier (`other-parties/<party>/profile/`), and ORA's positions are cited per the rule above.

### Strict rule on other-parties tier retrieval (Riccardo 2026-05-14)

The bot retrieves from the `other-parties` tier **only when the user explicitly requests a comparison involving ORA**. Standalone questions about another party (e.g., «cosa propone il PD sul lavoro?» without mentioning ORA) → planner classifies as `off_scope`, refusal_reason `off_scope_other_party_only`, and `emit_refusal` returns a template that offers to perform a comparison instead.

**Structural enforcement** in `agent/orchestrator.py:retrieve_parallel()`:
- For `query_type=compare` AND non-empty `comparison_parties`: tier_filter = `ORA_TIERS + ["other-parties"]`
- For everything else: tier_filter = `ORA_TIERS` only
- Planner can narrow further (intersect) but cannot smuggle `other-parties` into a non-compare query.

`ORA_TIERS` is the explicit whitelist in `agent/constants.py`: `["A1a", "A1b", "A1c", "A1-identity", "A2-boldrin", "A2-forchielli"]`.

> **Forward-pointer (2026-05-15, decision 24):** When the agent is implemented, `ORA_TIERS` must also include `"A1-contacts"` — the new contacts/routing tier introduced by decision 24. Without it the structural filter would silently block contact-routing queries from retrieving the org-structure card, even though it's tagged `attribution: party`. The chunker already emits `tier=A1-contacts` on the contact chunks.

Rationale: the bot is **of ORA**, not of other parties. Surfacing other-parties' positions unprompted would dilute the chatbot's identity and offer competitor messaging on the wrong canvas.

---

## "Only what we're sure about" principle

Locked verbatim by Riccardo (2026-05-14): *"The chatbot should say only what is sure about."*

This is a posture, not a single rule. It threads through the agent's behavior:

- **Verifier threshold (Stage 8):** any claim marked `partially_supported` gets softened to hedged language (*"la posizione potrebbe essere…"*, *"secondo le fonti disponibili…"*) or stripped. Not asserted as fact.
- **Refusal threshold:** when in doubt between answering and refusing, refuse. The bot says *"ORA non ha una posizione documentata su questo"* rather than guess.
- **Hedged-inference path (#11.B sub-branch 2):** the explicit `[inferenza]` label survives into the final answer.
- **Empirical claims:** if `data_lookup` returns no usable D1-D2-D3 stat-card AND `web_search` doesn't surface one from a trusted source (ISTAT, BdI, MEF, Eurostat, ISS, OECD), the bot says *"non dispongo di dati su questo"* — never invents a number.
- **Comparison claims:** if no documented position for the other party on the asked topic is retrievable, the bot says *"non ho una posizione documentata di [other party] su questo"* — does not infer.

Baked verbatim into the system prompt.

---

## Web-axis behavior (decision 03 reconciliation)

Per decision 03 (LOCKED): web search runs in parallel with corpus retrieval on **every** query. Cost trade-off accepted in exchange for currency + comparison engine + surfacing un-ingested ORA materials.

Per this decision 23 (2026-05-14): in **addition** to the always-parallel call, the agent can invoke **additional targeted web searches** in Stage 5 when Stage 4 reflection flagged gaps in the corpus retrieval. Example: a comparison question where corpus has ORA's position but other-party position is thin in `other-parties/<party>/profile/` — the agent does a targeted web search on that party's recent statements on the topic.

This preserves the locked #03 design ("always parallel") and adds the gap-fill capability Riccardo described.

Cost: every query incurs at least one web call ($0.005-0.01 of summarization). Adversarial agent-initiated searches add ~$0.005 each, bounded by a per-query cap (default: max 2 additional web searches).

---

## Self-check (Stage 8): combined faithfulness + relevance in one Haiku call

Decision 11.D locked the faithfulness check. This decision 23 adds **relevance** to the same Haiku call:

- **Faithfulness:** per-claim check — is each cited claim actually in its cited chunk?
- **Relevance:** answer-level check — does the answer address the actual user question?

One Haiku 4.5 call with structured output (JSON schema via tool-use). ~$0.01/query, ~500ms.

**If either fails:** regenerate once with explicit feedback ("verifier marked claim X as not_supported; the cited chunk says Y instead"). If regen also fails → `emit_refusal(verifier_failed)`.

---

## Failure mode handling

| Failure | Behavior |
|---|---|
| `web_search` times out (30s) or returns error | Continue with corpus axis only; flag in log; do NOT surface error to user |
| `corpus_retrieve` returns nothing under filtered tier | Agent loosens filter and retries once; if still empty → `emit_refusal(no_corpus_position)` |
| `data_lookup` returns nothing relevant | Agent falls to web for the metric on trusted-source domains; if web also fails → `emit_refusal(data_unavailable)` |
| `verify_answer` marks faithfulness fail on regen attempt | `emit_refusal(verifier_failed)` |
| Comparison question + other-party position unknown | `emit_refusal(comparison_other_party_unknown)` — does NOT infer the other party's view |
| Any LLM call times out (30s default) | Generic apology refusal; log for review |

---

## Cost summary (per query, MVP volume)

| Stage | Tool / call | Cost (uncached) | Cost (cached, after first call) |
|---|---|---|---|
| 1. Intent + plan | Opus 4.7, ~2K in + 300 out | $0.018 | $0.005 (system-prompt cache hits) |
| 2. Corpus retrieve | Qdrant + voyage-rerank-2.5 | ~$0.001 | same |
| 3. Data lookup (if empirical) | Qdrant filtered | ~$0 | same |
| 4. Reflect on retrieval | Opus 4.7, small | $0.005 | $0.003 |
| 5. Web search | summarization via Haiku | $0.005-0.015 | same (depends on agent-initiated searches) |
| 6. Synthesize | Opus 4.7, ~8K in + 1K out | $0.065 | $0.025 (cached) |
| 7. Citation enforcement | regex | $0 | $0 |
| 8. Verify | Haiku 4.5, ~3K in + 500 out | $0.005 | $0.005 |
| 9. Format + log | code | $0 | $0 |
| **Total** | | **~$0.10/query** | **~$0.04/query (cached)** |

Within £5 MVP cap: ~50 uncached queries OR ~125 cached queries (after the first call populates the cache).

End-to-end latency target: ~2-3s p50 (perceptible but acceptable for chatbot UX). p95 closer to 5s if regen triggers or extra web searches happen.

---

## Rationale

**Why a single agent (not multi-agent):** Anthropic's playbook says explicitly: *"only increase complexity when needed"* and *"for most apps, optimizing single LLM calls with retrieval and in-context examples is usually enough."* Our problem shape — structured pipeline with light branching — does not warrant multi-agent coordination overhead. Single-agent is also easier to evaluate (decision 12) and debug.

**Why workflow not "true agent":** Anthropic distinguishes *workflows* (predefined code paths) from *agents* (LLM dynamically directs its own process). Our flow has predictable structure with a few branch points; that's a workflow in Anthropic's vocabulary. Workflows offer *"predictability and consistency for well-defined tasks"* — exactly what we need for a faithfulness-critical political product. We can graduate to a true agent loop later if eval (decision 12 stage 2) shows multi-hop questions failing under the workflow.

**Why D1 (native SDK + custom Python):** Three reasons:
1. Our flow is structured, not open-ended — we don't need a framework's agent-loop machinery.
2. Debuggability matters more than convenience for screenshot-risk products: when something fails in production, we trace it through code we wrote, not framework internals.
3. Zero lock-in. If we graduate to a Claude Agent SDK or LangGraph pattern, the prompt-chain code translates directly because it's plain Python.

**Why these 5 tools and not more:** Per Anthropic's ACI guidance — too many tools confuse the model. Five with clear separation of concerns: retrieve (corpus), retrieve (data), retrieve (web), verify, refuse. Everything else is inline reasoning or deterministic code.

**Why combined verify (faithfulness + relevance) in one call:** Cheaper (one Haiku call instead of two) and faster (parallel computation inside one prompt). Anthropic's evaluator-optimizer pattern explicitly handles multi-criteria evaluation in a single call.

**Why "only what we're sure about" is the dominant principle:** Locked verbatim by Riccardo. For a public-facing political chatbot, the cost of an incorrect assertion (screenshot weaponizable by opposition) is higher than the cost of a refusal (user mildly frustrated). Refusal is the safer default; assertion requires confidence.

---

## Migration triggers (when to revisit)

- **Eval (decision 12 stage 1) shows multi-hop questions failing.** → Consider graduating to iterative agent loop (option A2 from discussion): after Stage 4 reflection, agent can decide "I need to retrieve again with different filters."
- **Stage 1 (intent classification) is too unreliable** as inline Opus reasoning. → Split into a dedicated Haiku classifier with stricter structured output.
- **Cost at steady-state public traffic exceeds €1k/mo.** → Switch synthesizer from Opus 4.7 to Sonnet 4.6 per decision 09 migration triggers; or split classify-vs-synthesize across Haiku and Opus.
- **Latency p95 > 5s consistently.** → Reduce regen attempts, drop combined verify to faithfulness-only, or move classification to a faster path.
- **Framework genuinely needed** (e.g., adding stateful multi-turn conversation across sessions). → Re-evaluate Claude Agent SDK or LangGraph.

---

## Open future paths intentionally deferred

- **Iterative retrieval loop (A2 from design discussion):** the agent decides post-retrieval to re-retrieve with different filters. Deferred until eval shows we need it.
- **Cross-session memory** is intentionally NOT supported per decision 15 (in-session 10-turn window only). The agent's Stage 1 receives `conversation_history` and resolves the user query against it before classifying — see decision 15 for the full integration.
- **Cross-encoder reranker swap or hybrid retrieval (deferred from decision 06/07):** would change `corpus_retrieve` internals without affecting the agent's shape.
- **Domain-specific reasoning for the data tier:** currently `data_lookup` returns stat-cards and the synthesizer reasons about them; could add a dedicated empirical-reasoner sub-prompt.

---

## Reference

- Anthropic, *Building Effective Agents* (Schluntz & Zhang, 2024) — patterns (augmented LLM, prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, true agents) and ACI principles drove this design.
- KB concept: `11_agentic_rag.md`
- KB concept: `12_agentic_patterns_architectures.md`
- Cross-references: #03 (two-axis retrieval), #07 (corpus retrieval tool internals), #08 (paradigm), #09 (generator model), #11 (guardrails + verifier + logging), #17 (data tier rules)
- CLAUDE.md §4 sourcing rules (updated 2026-05-14 to match the new citation-precedence rule, ORA-scoped)

## Amendment 2026-05-14 — General-context mode (cross-ref decision 11)

The workflow now supports a `general_context` query mode in addition to the four objectives. Triggered when the planner classifies the user query as descriptive/background (asking about a system or situation, not ORA's position).

Implementation surface:
- **Planner** — new `query_type` enum value `general_context`; planner prompt distinguishes it from `state` (the latter requires ORA to be the subject of the question).
- **Synthesizer** — receives a `mode` arg; when `general_context`, the per-call user message swaps in `MODE_INSTRUCTIONS_GENERAL_CONTEXT` which authorizes `[web:N]` and stat-card citations as primary grounding and instructs the model to append an optional «👉 Posizione di ORA» paragraph when corpus content is available.
- **Citation enforcement** — web result IDs (`web:1`, `web:2`, …) are added to the `valid_chunk_ids` set so the regex-based stripper preserves web-cited sentences.
- **Verifier** — receives the same `mode` arg; when `general_context`, uses `VERIFIER_SYSTEM_PROMPT_GENERAL_CONTEXT` which accepts web/data sources as fully legitimate grounding.

No new tools, no change to the workflow shape, no framework change. The "only what we're sure about" principle still holds — in general-context mode "what we're sure about" includes anything web search + the data tier can substantiate, not just the ORA corpus.

## Observations
*(populate during MVP demo runs — note where the workflow shape proves sufficient vs where eval flags it as insufficient)*
