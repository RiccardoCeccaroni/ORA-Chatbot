# 05 — Embedding model

**Status:** DECIDED
**Decided on:** 2026-05-13
**Decision:** **`voyage-4-large` from Voyage AI** (API, $0.12/MTok, 200M-token free tier, 32K context window, native pairing with `voyage-rerank-2.5` queued for decision 07).

**Rationale (Riccardo, 2026-05-13):**

1. **Italian-quality not the decider.** Neither Voyage nor Google publish Italian-specific MTEB/MIRACL numbers. Both train on Italian as a tier-1 European language. The gap between voyage-4-large and gemini-embedding-001 on Italian retrieval is almost certainly within 1-2 percentage points — indistinguishable in production until ORA-corpus eval signal exists. So the Italian-language axis came out neutral and the decision fell to operational fit.

2. **Operational fit favors Voyage:**
   - **Native reranker pair** with `voyage-rerank-2.5` — matched embed+rerank consistently beats mix-and-match in production RAG. Gemini and OpenAI ship no reranker; mixing vendors at the reranker stage is doable but inelegant.
   - **32K context window** swallows every chunk we produce, including the 5 oversized tesi/comunicato chunks (max 5,306 tokens). Gemini's 2K window would force pre-splitting logic.
   - **Built for RAG** rather than general-purpose. Voyage's retrieval-specific training shows up in benchmarks.
   - **Anthropic recommends Voyage** in its own RAG documentation — coherent with the rest of the stack (decision 09 is open but Anthropic models are likely candidates).
   - **Free tier (200M tokens)** covers our entire corpus (~1.19M tokens), ongoing weekly ingestion, and millions of query embeddings — effectively free for v1 and well beyond.

3. **Gemini-embedding-001 was the strong alternative.** Tops the overall MTEB leaderboard by ~1.5 points; Google has unmatched Italian training data; vendor longevity is unambiguous. Counterarguments: 2K context limit forces engineering workaround for 5 of our chunks; no native reranker; not retrieval-specialized.

4. **Self-host (BGE-M3) was the third realistic option.** Top open-weight multilingual, no vendor dependency, but requires GPU ops (~$60-100/mo plus monitoring/restart logic). Deferred to v2 if vendor independence becomes a concern.

**Reversibility:** switching embedding models means re-embedding the whole corpus (a one-way door for an in-production vector index). At our scale this is a ~10-minute job and $0.14 — so reversibility is cheap as long as we don't lock into a vendor-specific vector store schema. Decision 06 should preserve this.

**Cost summary (May 2026 pricing):**
- One-shot corpus embed: 1.19M tokens × $0.12/MTok = **$0.14** (free tier)
- Weekly newsletter additions: <500k tokens/yr (free tier)
- Query embeddings: ~80 tok × queries → free tier for years
- Reranker query cost: ~$0.001/query (free tier covers ~200M tokens)
- **Effective monthly cost for embedding+reranking stack: $0 until ~hundreds of thousands of queries/month**

**Empirical eval queued (post-implementation):** spin up `gemini-embedding-001` alongside `voyage-4-large` for a side-by-side on 30-50 representative ORA queries (~half a day of work, ~$1 in tokens) once retrieval is wired. If Gemini turns out meaningfully better on the ORA corpus specifically, the switch is reversible.

## The question

An embedding model is the function that turns each chunk of text (and each user question) into a vector — a list of numbers — such that semantically similar text ends up at similar coordinates. Retrieval works by finding the chunk vectors closest to the question vector.

**Which embedding model do we use?**

The choice is non-trivial because:
1. The model must speak Italian well (the corpus is Italian).
2. The model's "vector size" (e.g., 768, 1536, 3072) determines the index size.
3. Cost / latency vary 100× across options.
4. Switching later means re-embedding the whole corpus — a one-way door.

## Why it matters for the ORA chatbot

- A bad embedder on Italian text retrieves wrong chunks. The downstream LLM then either guesses or refuses — both look bad.
- Closed-API embedders (OpenAI, Cohere, Voyage) require sending the corpus to a third party. The corpus is public, so this is fine for *party* content, but worth a conscious choice.
- Vector size and index pricing interact with decision 06 (vector store).

## Options

### A — OpenAI `text-embedding-3-large` (3072 dims) or `-small` (1536 dims)
- Strong multilingual, including Italian.
- API call per chunk and per query; flat per-token pricing.
- Closed; ingestion sends content to OpenAI servers.

### B — Cohere `embed-multilingual-v3.0`
- Built specifically for multilingual retrieval, including Italian.
- Optimized for retrieval (separate doc/query embeddings).
- Closed API.

### C — Voyage AI (`voyage-3` family, `voyage-multilingual-2`)
- Newer, often top of MTEB-style multilingual leaderboards.
- Closed API.

### D — Open-weight multilingual (e.g., `intfloat/multilingual-e5-large-instruct`, `BAAI/bge-m3`, `jina-embeddings-v3`)
- Free, runs locally (GPU recommended) or via a self-hosted inference server.
- Quality on Italian is competitive but not always best-in-class.
- No data leaves your machine. Reproducible.

### E — Italian-specialized
- Models fine-tuned on Italian corpora (e.g., `dbmdz/bert-base-italian-xxl-cased` + sentence-transformer fine-tune, or domain-specific Italian models).
- Best on Italian-only; weak on cross-language; smaller community.

## What we'd need to know to choose

- Are you OK sending the corpus to a third-party API, or do you want a self-hosted/local setup?
- Is there a hard cost ceiling for the project (one-shot indexing + ongoing query embedding)?
- Do you have access to a GPU (yours or rented) for option D/E?
- Will you ever want to switch generation model (decision 09) to one of the same vendor's models for stack consistency?

## Reference

- KB concept: `04_embeddings_and_vector_search.md`
- KB concept: `13_costs_latency_tradeoffs.md`

## Observations
*(populate after corpus size is measured — total tokens for one-shot embedding cost estimate)*
