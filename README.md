# ORA Chatbot — monorepo

Two related projects, both grounded in the published material of **ORA!**, the Italian centrist party founded by Michele Boldrin and Alberto Forchielli:

| Subdir | What it is | Status |
|---|---|---|
| [`chatbot/`](./chatbot/) | The original **Agentic-RAG chatbot** designed to be embedded on the party's website. Synthesizes answers, cites sources, contrasts ORA with other Italian parties. | Historical — proposal rejected by ORA! management on 2026-05-16. Kept as the design audit trail. |
| [`ora-mcp/`](./ora-mcp/) | A public **MCP server** that exposes the same corpus to any AI assistant speaking the Model Context Protocol (Claude Desktop, Cursor, ChatGPT, claude.ai web). | Live, deployed on Fly.io at `https://ora-mcp-claudeai.fly.dev`. Sanctioned pivot suggested by ORA! management. |

## Why both live here

The chatbot project produced the corpus curation, trust hierarchy, retrieval pipeline, and 25 architectural decision docs (`chatbot/decisions/`). The MCP server reuses ~60–70% of that work — same corpus, same Qdrant index, same retrieval logic — but exposes it as a tool surface to third-party AI clients instead of generating answers itself.

The two subdirs are independent at the file level. They share the same Qdrant Cloud collection (`ora_chunks`) and the same external services (Voyage AI). Either project can re-ingest the index; the other sees the change automatically.

## Where to start reading

- **About the design rationale** → [`chatbot/decisions/`](./chatbot/decisions/) — 25 numbered architectural decisions (chunking, embedding, vector store, retrieval, generation model, guardrails, persona).
- **About the live MCP product** → [`ora-mcp/DECISIONS.md`](./ora-mcp/DECISIONS.md) and [`ora-mcp/README.md`](./ora-mcp/README.md).
- **For the audience of the MCP** → [`ora-mcp/demo/README.md`](./ora-mcp/demo/README.md) — the kit sent to ORA! management.

## Layout

```
.
├── chatbot/        Original Agentic-RAG chatbot (archived proposal)
│   ├── agent/        Runtime — orchestrator, system prompt, tools, CLI
│   ├── build/        Corpus → Qdrant ingestion pipeline
│   ├── corpus/       Source documents across 4 trust tiers
│   ├── decisions/    25 architectural decisions
│   └── memory/       Project memory used during build
└── ora-mcp/        Live MCP server (the shipped product)
    ├── ora_mcp/      Server code — FastMCP + OAuth + retrieval
    ├── corpus/       810 source markdown files
    ├── build/        Maintenance pipeline + YouTube ingest
    ├── tests/        Smoke + 105-test acceptance suites
    ├── demo/         Kit sent to ORA! management
    ├── Dockerfile    python:3.12-slim runtime
    └── fly.toml      Fly.io deploy config (Frankfurt)
```

## Author

Riccardo Ceccaroni — `riccardoceccaroni02@gmail.com`
