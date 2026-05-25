# ORA Chatbot

A personal project: an **Agentic-RAG chatbot** built around the published material of **ORA**, the Italian centrist party founded by Michele Boldrin and Alberto Forchielli. It answers questions about ORA's positions, leaders' views, and how ORA compares to other Italian parties — always grounded in cited sources.

*This is an independent project and is not affiliated with or endorsed by ORA.*

This repository is an end-to-end build: corpus, ingestion pipeline, retrieval index, agent runtime, and evaluation artifacts.

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

## Repository layout

```
.
├── decisions/           25 architectural decisions (the audit trail)
├── corpus/              ~592 retrievable documents across 4 trust tiers
│   ├── ora-party/         Tier A1 — official party voice
│   ├── leaders/           Tier A2 — Boldrin & Forchielli (gap-fill, always cited as personal)
│   ├── other-parties/     Tier 3 — comparison corpus (retrieved only on explicit comparisons)
│   └── data/              ISTAT stat-cards for empirical questions
├── agent/               Runtime — orchestrator, system prompt, tools, CLI
└── build/               Pipeline that turned the corpus into a searchable index
```

Evaluation sets, rubric, and run outputs are kept separately and not included in this repository.

## How to read it

1. **`decisions/`** — 25 markdown files in numbered order, one per architectural fork. The full design rationale lives here (chunking, embedding, vector store, retrieval, generation model, guardrails, evaluation, persona, etc.).
2. **`agent/`** — the runtime code. Entry point: `agent/cli.py`. Orchestration: `agent/orchestrator.py`. System prompt: `agent/system_prompt.py`.
3. **`corpus/`** — browse a few `ora-party/manifesto/*.md` files to see what the bot retrieves.

## Stack

- **Embeddings:** Voyage `voyage-4-large`
- **Vector store:** Qdrant Cloud (free tier), dense-only in v1
- **Reranker:** Voyage `voyage-rerank-2.5`
- **Generation:** Claude Opus 4.7 (synthesizer), Claude Haiku 4.5 (verifier)
- **Logging:** Postgres (Neon)
- **Orchestration:** native Anthropic SDK + custom Python (no LangChain / LlamaIndex)

## Running it locally

The repository ships **without** any API keys — they are excluded by `.gitignore`. If you want to run the bot yourself, you'll need to bring your own keys for every external service the bot talks to.

**1. Create `.env` at the repository root:**

```
ASSEMBLYAI_API_KEY=your_assemblyai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

**2. Create `build/.secrets/api keys.txt`** with the credentials the build/runtime scripts read (see `agent/secrets.py`):

```
cluster: <your Qdrant API key>
end point: <your Qdrant cluster URL>
voyage: <your Voyage AI key>
anthropic key: <your Anthropic key>
postgres: <your Postgres connection string>
openaikey: <your OpenAI key>
```

If you want the weekly-run error notifier (`build/youtube_pipeline/`), also create `build/.secrets/gmail_app_password.txt` with a Gmail app password.

**3. Install Python dependencies** (see imports in `agent/` and `build/`).

**4. Run the bot:**

```
python -m agent.cli
```

Be aware: the bot calls Anthropic (Opus + Haiku), Voyage (embeddings + reranker), Qdrant (vector store), and a live web search on every query — each turn costs real money on your accounts.

## Status

Post-MVP. RAG index live (3,665 chunks in Qdrant). All 25 architectural decisions are **DECIDED**.

## Author

Riccardo Ceccaroni — `riccardoceccaroni02@gmail.com`
