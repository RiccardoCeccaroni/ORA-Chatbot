# ORA Chatbot

A personal project: an **Agentic-RAG chatbot** built around the published material of **ORA!**, the Italian centrist party founded by Michele Boldrin and Alberto Forchielli. It answers questions about ORA's positions, leaders' views, and how ORA compares to other Italian parties — always grounded in cited sources.

*This is an independent project and is not affiliated with or endorsed by ORA.*

This subdir holds the chatbot's design and runtime code. The shared corpus and ingestion pipeline live in the sibling [`../ora-mcp/`](../ora-mcp/) project.

---

## What the bot does

The bot answers questions about ORA in Italian. On every query, two retrieval axes run in parallel:

- **Authority axis** — a curated corpus tiered by trust: party voice first (manifesto / comunicati / newsletter), leader views as gap-fill (always cited as personal), other Italian parties only when the user explicitly asks for a comparison.
- **Live web search** — for current events, recent statements, and external coverage.

A synthesizer (Claude Opus 4.7) composes an answer with every claim cited to a specific corpus document or web result. A deterministic post-processing step then strips any sentence that isn't backed by a citation, so unsupported claims never reach the user. If nothing is found, the bot says so explicitly rather than inventing a position.

**Persona:** third-person, encyclopedic — *"ORA's position is…"*. Never first-person spokesperson.

## The four objectives

1. **State** — express ORA's positions on Italian policy matters.
2. **Project** — answer hypotheticals ("what would ORA do if X?") with action + underlying stance.
3. **Justify** — always motivate the position; cite data on empirical questions.
4. **Compare** — on request, contrast ORA with PD, M5S, FdI, Lega, FI, AVS, Azione, IV.

## Layout

```
.
├── decisions/           25 architectural decisions (the audit trail)
├── agent/               Runtime — orchestrator, system prompt, tools, CLI
└── build/               Chatbot-specific build artifacts
    ├── postgres_schema.sql   Schema for the conversation-logging Postgres table
    ├── render_docx.py        Renders eval-set outputs to Word documents
    └── run_eval.py           Eval harness driving the agent against a fixed question set
```

The **shared corpus** (party material, leader profiles, comparison parties, statistical cards) and the **shared ingestion pipeline** (chunking, embedding, Qdrant ingest, YouTube transcription) live in [`../ora-mcp/corpus/`](../ora-mcp/corpus/) and [`../ora-mcp/build/`](../ora-mcp/build/). Both projects read from the same Qdrant Cloud index (`ora_chunks`).

## How to read it

1. **`decisions/`** — 25 markdown files in numbered order, one per architectural fork. The full design rationale lives here (chunking, embedding, vector store, retrieval, generation model, guardrails, evaluation, persona, etc.).
2. **`agent/`** — the runtime code. Entry point: `agent/cli.py`. Orchestration: `agent/orchestrator.py`. System prompt: `agent/system_prompt.py`.
3. **`../ora-mcp/corpus/`** — browse a few `ora-party/manifesto/*.md` files to see what the bot retrieves.

## Stack

- **Embeddings:** Voyage `voyage-4-large`
- **Vector store:** Qdrant Cloud (free tier), dense-only in v1
- **Reranker:** Voyage `voyage-rerank-2.5`
- **Generation:** Claude Opus 4.7 (synthesizer), Claude Haiku 4.5 (verifier)
- **Logging:** Postgres (Neon) — schema in `build/postgres_schema.sql`
- **Orchestration:** native Anthropic SDK + custom Python (no LangChain / LlamaIndex)

## Running it locally

The repository ships **without** any API keys — they are excluded by `.gitignore`. To run the bot yourself you'll need to bring your own keys for every external service the bot talks to, plus a populated Qdrant index.

**1. Create `.env`** at the monorepo root:

```
ASSEMBLYAI_API_KEY=your_assemblyai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

**2. Create `build/.secrets/api keys.txt`** with the credentials the runtime reads (see `agent/secrets.py`):

```
cluster: <your Qdrant API key>
end point: <your Qdrant cluster URL>
voyage: <your Voyage AI key>
anthropic key: <your Anthropic key>
postgres: <your Postgres connection string>
openaikey: <your OpenAI key>
```

**3. Populate the Qdrant index.** The chatbot reads from the same `ora_chunks` collection that the MCP uses. Either ingest the corpus yourself via the sibling pipeline:

```
cd ../ora-mcp
pip install ".[build]"
python build/chunk_corpus.py --apply
python build/ingest_qdrant.py --apply
```

…or point your Qdrant credentials at an existing populated index.

**4. Install Python dependencies** (see imports in `agent/` and `build/`).

**5. Run the bot:**

```
python -m agent.cli
```

Be aware: the bot calls Anthropic (Opus + Haiku), Voyage (embeddings + reranker), Qdrant (vector store), and a live web search on every query — each turn costs real money on your accounts.

## Status

Post-MVP. All 25 architectural decisions are **DECIDED**.

## Author

Riccardo Ceccaroni — `riccardoceccaroni02@gmail.com`
