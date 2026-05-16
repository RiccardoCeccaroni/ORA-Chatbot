# 08 — RAG paradigm (naive / advanced / modular / agentic)

**Status:** DECIDED
**Decided on:** 2026-05-10
**Decision:** **Agentic RAG with two-axis parallel retrieval** (corpus authority axis + live web context axis), synthesized under the rule *"Authority answers, context enriches"*. The agent's job: route to the right axis-mix, flag evolution when corpus and web disagree by date, decide when to refuse ("ORA non ha una posizione documentata su questo"). See decision 03 for the full axis design.
**Rationale:** Required by the four objectives:
- Objective 2 (Project — hypotheticals) needs reasoning over Tier-1/Tier-2 principles, not single-shot retrieval.
- Objective 3 (Justify) needs synthesis across multiple cited sources, often with data.
- Objective 4 (Compare) needs live web for other-parties' positions (corpus doesn't have them yet).
- Evolution flagging (newer comunicato superseding older tesi) needs an agent that compares dates and reasons, not a stateless retriever.
- Cost trade-off is explicitly accepted: web search on every query is more expensive but buys currency.

Naive / advanced / modular RAG can't deliver these in one pass.
**Source of decision:** Prior Claude Code session (sessionId `b5c21d07-7069-...`), captured in auto-memory `project_chatbot_objectives.md`. See CLAUDE.md §3 for the full retrieval design.

## The question

At the highest level, RAG systems come in four flavors of increasing sophistication. **Which flavor is right for this chatbot?**

1. **Naive RAG** — single retrieval, single generation, no feedback.
2. **Advanced RAG** — pre-retrieval enhancements (query rewriting, expansion) and post-retrieval enhancements (reranking, compression), but still single-pass.
3. **Modular RAG** — explicit modules you can swap (retriever, reranker, generator, router, memory). Single-pass but configurable.
4. **Agentic RAG** — the LLM acts as an agent that can iteratively decide *whether* to retrieve, *what* to retrieve, *whether the answer is good enough*, and *when to stop*. Multi-step, planning-capable.

## Why it matters for the ORA chatbot

- This is the highest-leverage decision in the whole project. Agentic adds significant cost and latency; pick it only if simpler approaches can't handle the workload.
- For most questions on this corpus ("what does ORA think about X"), one well-targeted retrieval + one generation is enough. Agentic shines on multi-hop questions ("how has ORA's position on Y changed between the manifesto and recent newsletters").
- Faithfulness: agentic adds a self-check step (does my answer actually appear in the retrieved chunks?), which is valuable for political content where misattribution is costly.
- Cost: every agentic step is an LLM call. A self-critique loop can 3–5× your per-query bill.

## Options

### A — Naive RAG
- One retrieval, one generation. Done.
- Good fit if user questions are mostly simple and the corpus has clean, direct answers.

### B — Advanced RAG (query rewrite + rerank + generate)
- Reliable mid-tier. Better recall on vague questions; better precision via rerank.
- The default for many production setups today.

### C — Modular RAG with a deliberate router
- A small router LLM decides per question: which sub-corpus to search (manifesto vs newsletter vs leader content), whether to compare multiple sources, whether to refuse.
- Maps cleanly onto decisions 01 (scope) and 03 (trust hierarchy).

### D — Full Agentic RAG (planning, multi-step retrieval, self-critique)
- The agent can: rephrase, retrieve, evaluate retrieved evidence, re-retrieve, draft, self-critique, refine.
- Best on hard / multi-hop / contested questions ("compare ORA's positions on labor in the manifesto vs in Boldrin's interviews from 2024–2025").
- Most expensive, most latent, hardest to evaluate.

### E — Hybrid: agentic for hard questions, naive/advanced for easy ones
- A classifier (rule or small LLM) routes simple questions to a cheap path, complex ones to the full agentic path.
- Cost-optimal in production. More moving parts.

## What we'd need to know to choose

- What's the typical question complexity? Single-fact lookup vs. multi-source comparison vs. evolution-over-time?
- What's the latency budget? An interactive chat tolerates ~2s; a "research assistant" can take 20s.
- Are you optimizing for "good enough cheap" or "best possible regardless"?
- Will you have a way to evaluate (decision 12) whether the extra agentic complexity actually improves answers, or will it just feel sophisticated?

## Reference

- KB concept: `10_rag_paradigms.md`
- KB concept: `11_agentic_rag.md`
- KB concept: `12_agentic_patterns_architectures.md`
- KB concept: `13_costs_latency_tradeoffs.md`

## Observations
*(populate as you map representative user questions to the complexity they require)*
