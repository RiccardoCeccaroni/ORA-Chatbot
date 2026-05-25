# 07 — Retrieval strategy

**Status:** DECIDED
**Decided on:** 2026-05-14
**Decision:** **Dense retrieval over Qdrant + cross-encoder reranking with `voyage-rerank-2.5`** (option A + reranker). Sparse / BM25 hybrid deferred to v2.

**Concrete pipeline:**
1. User query → `voyage-4-large` embedding (1024-d)
2. Top-50 candidates from Qdrant dense ANN search, with metadata pre-filters when the agent layer asserts them (e.g., `attribution=party` for a "what does ORA say" query, or `tier ∈ {A1a, A1b}` to scope to official voice)
3. Top-50 reranked by `voyage-rerank-2.5`, keep top-5 to top-10
4. Reranked chunks fed to the generation model (decision 09) along with parallel web-search results per the locked two-axis design
5. Citation pills built from chunk metadata (`anchor`, `parent_id`, `source_url`, `tier`)

**Rationale (Riccardo, 2026-05-14):**

1. **Reranker is the bigger quality lever.** Cross-encoder reranking on top of dense retrieval consistently delivers more retrieval quality per dollar than adding BM25 sparse vectors. `voyage-rerank-2.5` is matched to `voyage-4-large` (same vendor, same training distribution) — this matched-pair argument has run through decisions 05 and 06 and applies here too.

2. **Hybrid BM25+dense was the alternative, deferred.** Italian acronyms (PD, M5S, FdI, PNIEC, AGCOM), specific doc references ("tesi 06"), Italian named entities — lexical retrieval helps these. But the deferral aligns with decision 06 (we chose Qdrant free tier knowing native hybrid isn't first-class; sparse-vectors implementation is engineering-heavier). If post-launch eval shows dense+rerank misses Italian-specific lexical queries, sparse vectors get added in v2.

3. **Cost is negligible at our scale.** Reranking ~50 chunks × ~400 tokens = 20K input tokens per query × $0.05/MTok = **$0.001 per query**. Plus 200M-token free tier on the Voyage account covers years of normal traffic before any spend. Latency cost is ~200-500 ms per query.

4. **Metadata pre-filtering via the agent layer.** Qdrant's filtering depth (rationale for #06) is exercised here. The agent can pre-narrow candidate pool by `tier`, `attribution`, `date_published`, `tesi_alignment`, etc. before dense ANN runs — saving reranker compute and improving precision for category-specific queries.

5. **Multi-query / query rewriting (option E) explicitly NOT in v1.** Adds an LLM call before retrieval, doubles latency, doubles cost. Worth revisiting if eval shows ambiguous-query failures are common. Default in v1: agent layer composes the corpus query directly from the user's question.

**Cost summary at our scale:**
- Per-query reranker cost: ~$0.001 (free tier covers ~200M tokens)
- Per-query query-embedding cost: ~$0 (free tier)
- Effective retrieval-side cost for v1: $0 until ~hundreds of thousands of queries/month
- Latency budget: ~10ms dense retrieval + ~200-500ms rerank = sub-second total before generation

## The question

Once chunks are embedded and indexed (decisions 04–06), how does the system *find* the right chunks for a given user question?

Three main families:
1. **Dense retrieval** — embed the question, find nearest-neighbour chunk vectors.
2. **Sparse / lexical retrieval** — keyword matching (BM25, TF-IDF). Different strengths than dense.
3. **Hybrid** — run both, combine the results.

Plus an optional second stage:
- **Re-ranking** — take the top ~20 from initial retrieval, rescore them with a more expensive model that looks at the question and the candidate chunk together.

## Why it matters for the ORA chatbot

- Political content has lots of proper nouns ("Salvini", "Schillaci", "AGCOM", "PNRR") and specific bill numbers — exactly where lexical retrieval shines and dense retrieval can blur.
- Italian morphology (verb conjugations, articles, prepositions) can hurt dense embeddings more than English. Hybrid + reranking often wins for non-English corpora.
- Re-ranking adds latency and cost per query. The trade-off is real.

## Options

### A — Dense only
- Cleanest baseline. Question vector → top-k chunk vectors. Done.
- Fast, cheap. Misses exact-match queries (a name, a law name).

### B — Hybrid (dense + BM25, score fusion)
- Both retrievers run; results are merged (e.g., Reciprocal Rank Fusion).
- More robust to proper-noun queries. Modest extra complexity.

### C — Hybrid + cross-encoder reranker
- Hybrid retrieval surfaces ~30 candidates; a cross-encoder model (e.g., Cohere Rerank, BGE-reranker, Voyage rerank-2) reorders them by deep relevance.
- Highest quality. ~200–500ms extra per query. Modest extra cost.

### D — Dense + metadata pre-filter, then small-k retrieval
- Use metadata to narrow the search first ("question mentions immigration → search only chunks tagged `topic: immigrazione`"). Then dense retrieval over the filtered set.
- Requires good metadata (topic tagging step at ingestion). Cuts cost.

### E — Multi-query / query rewriting + dense
- Have an LLM rewrite the user's question into 2–4 variant queries; retrieve for each; merge results.
- Helps with vague or short queries. Adds an LLM call before retrieval.

## What we'd need to know to choose

- What's the typical user question — short keyword-like ("immigrazione?") or full natural-language ("cosa pensa ORA dell'accoglienza dei migranti via mare")?
- Are you willing to add a rerank step (extra latency / cost) for higher quality?
- Decisions 04 (chunking) and 03 (trust hierarchy) feed in here — metadata filters depend on what fields exist on each chunk.

## Reference

- KB concept: `07_retrieval_strategies.md`
- KB concept: `05_the_rag_pipeline.md`

## Observations
*(populate once a small set of representative questions has been collected)*
