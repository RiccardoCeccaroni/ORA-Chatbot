# 09 — Generation model

**Status:** DECIDED (MVP); revisit before public launch
**Decided on:** 2026-05-14
**Decision:** **Claude Opus 4.7** (`claude-opus-4-7`) via the Anthropic API for the MVP, with a hard £5 testing-budget cap and the explicit plan to re-evaluate Opus vs Sonnet 4.6 once eval signal (decision 12) exists.

**Amended 2026-05-15 (a) — synthesizer flipped to Sonnet 4.6 for a test round.** The planner stage stays on Opus 4.7. The synthesizer became `claude-sonnet-4-6`. Riccardo's call (2026-05-15): "yes let's try sonnet for the test."

**Amended 2026-05-15 (b) — synthesizer reverted to Opus 4.7 as part of the agent rework.** The Sonnet synthesizer test produced over-inclusive answers (notable example: a follow-up question "E sul nucleare nello specifico?" got an answer that reframed with the broader rinnovabili+nucleare strategy instead of staying narrow). Riccardo's call: rebuild the agent with Opus throughout and a new `focus_topic` field from the planner that tells the synthesizer when to stay narrow. Synthesizer is `claude-opus-4-7` again; see decision 23 amendment (b) for the full rework.

**Concrete setup:**
- Model: `claude-opus-4-7` (Anthropic, $5/MTok input, $25/MTok output, $0.50/MTok cached input read, 90% discount on cache reads, 50% discount via Batch API for non-interactive runs).
- Auth: Anthropic API key (`sk-ant-api03-…`). The user's Claude Max subscription cannot power the deployed backend — it is restricted to claude.ai, Claude Desktop, and Claude Code, by Anthropic's design. The Max subscription continues to pay for itself on the *build* side (we are using it right now via Claude Code), but the chatbot itself needs an API key.
- Persona/system prompt enforces decision 16 (third-person, encyclopedic, never first-person spokesperson) and decision 10 (citation pills).
- Inputs: retrieved+reranked chunks (decision 07) + parallel web-search results (decision 03 two-axis design).
- Output: Italian, with mandatory visible citation pills.

**Rationale (Riccardo, 2026-05-14):**

1. **"Most powerful, will be shipped, professional"** is the locked product framing. Opus 4.7 is the strongest faithfulness + instruction-following model in the Anthropic line, which directly serves the two non-negotiables of this product: (a) never blur leader opinion with party position; (b) always cite. Both are *instruction-following* problems before they are *raw IQ* problems. Opus excels here.

2. **Italian fluency is strong on Opus 4.7.** Anthropic trains on substantial Italian data; output is fluent and idiomatic. No empirical advantage from switching to another vendor on Italian at this quality tier.

3. **Cost dropped substantially in 2026.** Opus 4.7 is now **$5/$25 per MTok**, not the legacy $15/$75. Only ~1.7× the cost of Sonnet 4.6, not 5×. This changes the calculus — paying for the top model is no longer a 5× tax.

4. **£5 testing budget covers a realistic MVP eval.** At a representative 8K input + 1K output per query (system prompt + persona + ~5 reranked chunks + answer):
   - Per query: 8K × $5/MTok + 1K × $25/MTok = $0.04 + $0.025 = **$0.065/query**
   - £5 ≈ $6.30 ≈ **~95 queries** of uncached eval traffic
   - With prompt caching (system prompt + persona cached): drops to ~$0.025/query → **~250 queries** within £5
   - The eval suite (decision 12, still OPEN) is unlikely to need more than 50-100 representative queries at this stage
   - Hard stop: monitor cumulative spend in the Anthropic console; if approaching £5, pause and review

5. **Stack coherence.** We are using Anthropic tools to build (Claude Code via Max subscription). Shipping on Anthropic for inference is the simplest stack — single vendor for the model-side concerns, single billing surface, consistent SDK conventions. No win from cross-vendor heterogeneity on this axis.

6. **Reversibility is cheap.** The generation model is the *most reversible* choice in the stack — swapping it is a config change, not a re-embed. If post-MVP eval shows Opus is overkill and Sonnet 4.6 matches it on our 50-query suite, the switch to Sonnet ($0.039 → $0.012 with caching) is one line of code. Conversely, if Sonnet had been the MVP choice and it failed on hard cases, we would have spent eval cycles on the wrong model.

**Alternatives considered:**

- **Claude Sonnet 4.6** ($3/$15, ~$0.039/query): the strongest cost/quality compromise. Defensible default for a v1 ship. Rejected for MVP because the user explicitly chose "most powerful" within the £5 cap, and Opus 4.7's £5-budget headroom is comfortable (~95+ queries). Will be re-evaluated against Opus in eval (decision 12).
- **Claude Haiku 4.5** ($1/$5, ~$0.013/query): cheapest in the Anthropic line. Likely measurably weaker on persona discipline and on subtle political nuance. Possible router-stage role in a future Mixed setup (option E above) but not the answerer.
- **GPT-4o / GPT-4.1** (OpenAI): comparable quality. Loses stack coherence with the Anthropic-tooled build side. No standalone reason to switch.
- **Gemini 2.x Pro** (Google): comparable quality, strong Italian. Loses stack coherence. Long context window is irrelevant given our reranked top-5/10 design (decision 07).
- **Open-weight (Llama 3, Mistral Large 2, Qwen 2.5)**: cheaper at scale but require inference infra and underperform on careful citation/instruction-following at our quality bar. Vendor-independence axis (cf. embedder #05 rationale 4) deferred to v2 if it becomes a constraint.
- **Mixed router/answerer** (option E): defer to v2. v1 keeps a single model for simplicity; agentic patterns (decision 08) call Opus 4.7 throughout, paid for by the £5 cap during MVP and metered after.

**Cost summary (MVP + projected):**

| Phase | Queries | Cost (Opus 4.7, uncached) | Cost (Opus 4.7, cached) |
|---|---|---|---|
| **MVP eval** (£5 cap) | ~95 | $6.30 | ~$2.40 |
| **Private beta** (50 users × 10 q/mo) | 500 | $33/mo | $13/mo |
| **Soft launch** | 5,000/mo | $325/mo | $125/mo |
| **Steady public** | 25,000/mo | $1,625/mo | $625/mo |

The "Steady public" line is where the Opus-vs-Sonnet conversation reopens. Sonnet would be ~5× cheaper at that volume (~$125/mo cached). Whether that 5× saving is worth the quality delta is an eval question (decision 12), not an a-priori one.

**Migration triggers (when to revisit):**
- Post-MVP eval (decision 12) shows Sonnet 4.6 ≈ Opus 4.7 on the ORA-corpus suite → switch to Sonnet for production.
- Public-traffic monthly bill exceeds €1,000/mo and party budget cares → switch to Sonnet or to Mixed router/answerer.
- Anthropic releases a successor model (Opus 4.8, Claude 5) with materially better Italian or faithfulness → re-test.
- Latency requirements tighten (e.g., <2s p95 end-to-end) and Opus is the bottleneck → switch to Sonnet (faster) or Haiku.

## The question

Once relevant chunks have been retrieved, the chatbot calls an LLM to read the chunks and produce the answer. **Which LLM?**

This is separable from the embedding model (decision 05) — you can mix vendors. But many people pick the same vendor for both to simplify billing and infra.

## Why it matters for the ORA chatbot

- Italian fluency varies across models. Frontier models (Claude, GPT-4-class, Gemini) are all good; cheaper / open models drop off.
- Faithfulness — staying grounded in retrieved chunks instead of hallucinating — varies more across models than raw fluency. Claude and GPT-4 class models tend to be more controllable here than smaller models.
- Cost-per-answer varies ~100× across the spectrum. A bot designed for thousands of users has very different economics than a personal-research bot.
- The agent paradigm (decision 08) interacts: agentic RAG calls the LLM many times per question, so model price matters more there.

## Options

### A — Anthropic Claude (Opus 4.x / Sonnet 4.x / Haiku 4.x)
- Strong on faithfulness and instruction-following. Multilingual (incl. Italian) is solid.
- Best when you have a structured prompt with citations and want the model to respect it.
- Closed API.

### B — OpenAI GPT (`gpt-4o`, `gpt-4-turbo`, `gpt-4.1`)
- Strong all-rounder. Tooling and ecosystem most mature.
- Closed API.

### C — Google Gemini (1.5/2.x Pro/Flash)
- Long context window can swallow many chunks. Multilingual is fine.
- Closed API.

### D — Open-weight (Llama 3.x, Mistral, Qwen 2.5, DeepSeek)
- Run locally (need GPU) or via inference providers (Together, Fireworks, Groq).
- Italian quality varies; the best 70B+ models are competitive on basic tasks but not on subtle political nuance.
- No data leaves your machine if self-hosted.

### E — Mixed (small/fast for routing, big/precise for final answer)
- A "router" model (cheap, Haiku-class) decides next steps; a "answerer" model (Opus-class) writes the final response.
- Cost-optimal for agentic setups (decision 08 option D/E).

## What we'd need to know to choose

- Are you OK with closed APIs sending the (public) user question to a third party?
- What's the expected volume? Personal use (10s of queries/day) vs. demo (100s) vs. public (1000s+)?
- Is there a stylistic preference — Claude's careful hedging, GPT's confident concision, Gemini's verbose — that fits the party's tone (decision 16)?
- If you also use Anthropic for prompts elsewhere, stack consistency may be a tiebreaker.

## Reference

- KB concept: `01_llms_and_their_limits.md`
- KB concept: `13_costs_latency_tradeoffs.md`
- KB concept: `14_production_concerns.md`

## Observations
*(record sample-answer comparisons here once you do A/B tests in decision 12 eval)*
