# 06 — Vector store

**Status:** DECIDED
**Decided on:** 2026-05-14
**Decision:** **Qdrant Cloud free tier** (managed, $0/month permanent, 0.5 vCPU / 1 GB RAM / 4 GB disk single-node cluster). Voyage integration via API (not first-party). Hybrid BM25+dense deferred — v1 uses dense + reranker only.

**Rationale (Riccardo, 2026-05-14):**

1. **Free tier covers us with massive headroom.** 3,239 vectors at voyage-4-large's 1024 dims = ~13 MB raw, ~50 MB with HNSW index + payload. We use <5% of free-tier capacity (RAM, disk, both). Room for ~100,000 chunks before we'd outgrow it; corpus grows by ~1,000 chunks/year. The free tier is "free forever" with no credit card, no time limit, no traffic caps — only inactivity suspension after 1 week of zero queries (immaterial for a public-facing bot, cron-heartbeat workaround if ever needed).

2. **Best-in-class metadata filtering** for our rich frontmatter schema. The chunks carry `tier`, `attribution`, `parent_id`, `date_published`, `quality_tier`, `tesi_alignment`, `topic_slug`, and more. Qdrant's filter primitives (nested JSON, geo, has_vector, text-match) are deeper and faster than any competitor — and unlike Pinecone, no "read-unit multiplier" cost penalty on filtered queries.

3. **Open-source escape hatch.** Qdrant is Apache-2.0 OSS. If Cloud pricing ever changes, or if party-owned infrastructure becomes a requirement, the same engine runs anywhere with no rewrite — Docker, VPS, Kubernetes, on-prem. This preserves long-term independence in a way managed-only options (Pinecone, Atlas) don't.

4. **Reversibility of embedder swap** (the eval idea from decision 05): Qdrant supports multiple collections trivially, so spinning up `gemini-embedding-001` alongside `voyage-4-large` for empirical comparison is a 10-minute job.

5. **Trade-offs accepted:**
   - **No native hybrid BM25+dense search.** Atlas and Weaviate ship this in one query; Qdrant requires sparse vectors (more engineering). Decision: skip hybrid in v1, use dense + voyage-rerank-2.5 only. If post-launch eval shows dense+rerank misses Italian-specific lexical queries (acronyms, doc refs), add sparse-vectors hybrid in v2.
   - **Voyage integration is API-call, not first-party.** Atlas has auto-embeddings since Jan 2026; on Qdrant we write ~50 lines of Python (embed → upsert). One-time cost.
   - **Single-node free tier = no HA.** A cluster outage breaks retrieval (web search still answers, per the locked agentic two-axis design — graceful degradation). Atlas M10 at $57/mo also doesn't provide HA at that tier, so paying the premium wouldn't buy HA. Real HA across vendors is ~$150-300/mo; that's a v2 conversation tied to uptime SLA requirements.
   - **0.5 vCPU could throttle at concurrent-load scale** (dozens of simultaneous queries). At expected traffic, queries are ~10 ms. Upgrade path: $30/mo Standard tier (2 vCPU, 2 GB RAM, one click in UI) if monitoring shows we're saturating.

6. **MongoDB Atlas Vector Search was the strong alternative.** First-party Voyage stack (embed + rerank + auto-embed + store all from MongoDB since the Voyage acquisition), native hybrid search, integrated reranking — the cleanest matched-pair production option. Cost ~$57/mo for M10. Rejected for v1 because: (a) Qdrant's free tier delivers the same dense-retrieval quality, (b) the only quality gap is hybrid search which is recoverable later, (c) the trade is $700/yr vs ~50 lines of glue code, (d) the open-source escape hatch preserves long-term reversibility that Atlas doesn't offer.

**Cost summary:**
- v1 operational cost for vector store: **$0/mo permanent**
- Migration trigger to $30/mo Standard tier: concurrent-query saturation (unlikely at expected traffic) OR corpus growth past ~100k chunks (unlikely on current ingestion rate)
- Migration trigger to Atlas Vector Search: post-launch eval shows native hybrid retrieval materially helps (revisitable as a v2 decision)
- Upgrade is one click; no data migration needed within Qdrant tiers

## The question

A vector store is the database that holds embeddings (decision 05) and answers nearest-neighbour queries quickly. **Which one do we use?**

Functionally they all do the same thing. The differences are: hosting model (local file / self-hosted server / managed cloud), how easy it is to add metadata filters (e.g., "only manifesto sections", "only post-2026 newsletters"), how it handles incremental updates, and cost.

## Why it matters for the ORA chatbot

- Metadata filtering matters here: decision 03 (trust hierarchy) and decision 13 (freshness) both require filtering by `attribution`, `date_published`, `type`. The store must support that cleanly.
- Corpus is small (likely <10k chunks). Performance is not a bottleneck — convenience is.
- Decision 13 (freshness) implies frequent incremental upserts (weekly newsletters). The store should make that easy.

## Options

### A — Local file-based (FAISS, Chroma in persistent mode)
- Zero infra. Vectors live on disk next to the corpus.
- Good for prototyping. Backup is "copy the file".
- Multi-user / multi-process is awkward.

### B — Chroma / Qdrant / Milvus / Weaviate, self-hosted (Docker)
- Single container, runs locally or on a small VM.
- Real metadata filtering, real upserts, real persistence.
- You manage the process.

### C — pgvector (Postgres extension)
- If you already use Postgres, you get vector search inside SQL with full transactional metadata.
- Slower than purpose-built stores at large scale, but irrelevant here.
- Good fit if you also want to store conversation logs, eval results, etc. in the same DB.

### D — Managed cloud (Pinecone, Weaviate Cloud, Qdrant Cloud)
- Zero ops. Pay-per-vector or per-pod.
- Locks you into a vendor. Sends data to a third party.

### E — Use the LLM provider's built-in retrieval (OpenAI Vector Store, Anthropic's `files` + search)
- Tightest integration with that provider's models.
- Less control over chunking, metadata, ranking.

## What we'd need to know to choose

- Do you want everything to run on your laptop / a single VM (option A/B/C), or are you OK with a managed service (option D/E)?
- Will the chatbot be served from your machine, or hosted somewhere (option 14 — interface)?
- Do you anticipate wanting to run SQL-style queries alongside vector search (e.g., "show me all newsletters from March that mention X")?

## Reference

- KB concept: `04_embeddings_and_vector_search.md`
- KB concept: `14_production_concerns.md`

## Observations
*(populate once chunk count is estimated)*
