# ORA! — MCP server

A public MCP (Model Context Protocol) server that exposes a curated corpus of material from **ORA!**, an Italian centrist party, to AI assistants — Claude Desktop, Cursor, ChatGPT with MCP, claude.ai web custom connectors, and any other MCP-conformant client.

---

## What it does

When a user asks their AI assistant *"what's ORA!'s position on tax reform?"*, the assistant can call this server, retrieve the relevant passages from the manifesto and other party material, and **quote them verbatim** with a citation back to the source document. The server itself doesn't generate answers — it returns structured retrieval results that the user's AI composes into a response.

Two retrieval surfaces are exposed:

- **`find_position(topic, …)`** — the primary tool. Returns the corpus split into trust-hierarchy buckets: `official_party` (party voice), `leader_views` (Boldrin / Forchielli, always flagged as personal), `supporting_data` (statistical cards), and optionally `comparison` (other Italian parties).
- **`data_lookup(metric, …)`** — empirical stat-card retrieval, filtered by source quality tier.

Plus five static resources for ground-truth quoting: `ora://about`, `ora://manifesto`, `ora://statuto`, `ora://fondamenti`, `ora://codice-etico`.

## What the corpus contains

- The full manifesto (21 thesis files)
- Official party communications and newsletters
- Identity documents, bylaws, policy fundamentals, code of ethics
- Thematic profiles of Boldrin and Forchielli (always tagged as personal viewpoint)
- Statistical cards curated from ISTAT, Eurostat, OECD, Banca d'Italia
- Comparative profiles of other major Italian parties (for explicit comparison queries)

Roughly **3,665 indexed chunks** across all sources.

## How to try it

1. Open Claude Desktop (or another MCP-conformant client).
2. Paste the configuration from [`demo/claude_desktop_config.json`](./demo/claude_desktop_config.json).
3. Restart.
4. Ask one of the questions in [`demo/demo_questions.md`](./demo/demo_questions.md).

claude.ai web also works via the custom connector flow under `/customize/connectors`.

---

## For developers

### Endpoints

- **MCP (streamable HTTP):** `<host>/mcp`
- **Landing page (HTML):** `<host>/`
- **Health check:** `<host>/health`

The live deploy is at `https://ora-mcp-claudeai.fly.dev`.

### Tools

- `find_position(topic, top_k_per_bucket=5, include_comparison=False, include_leaders=True, date_from?, date_to?)` — primary tool. Returns ORA!'s position on a topic, organized into trust-hierarchy buckets: `official_party`, `leader_views` (Boldrin / Forchielli), `supporting_data` (stat-cards), `comparison` (other parties, optional).
- `data_lookup(metric, period?, quality_tier_floor="D3", top_k=5)` — statistical cards, ordered by source quality.

### Resources

- `ora://about` — who ORA! is, the objectives, the trust hierarchy.
- `ora://manifesto` — the full manifesto (21 theses, ~575 KB).
- `ora://statuto` — party bylaws (~57 KB).
- `ora://fondamenti` — 15 policy fundamentals, Annex 2 (~10 KB).
- `ora://codice-etico` — code of ethics, Annex 3 (~4 KB).

### Running locally

```bash
# 1. Install
pip install -e .

# 2. Configure credentials
cp .env.example .env
# Edit .env: QDRANT_URL, QDRANT_API_KEY, VOYAGE_API_KEY

# 3. Start
python -m ora_mcp.server
# → http://localhost:8000/mcp
```

### Deploying to Fly.io

```bash
fly launch --no-deploy --copy-config --name ora-mcp
fly secrets set QDRANT_URL=... QDRANT_API_KEY=... VOYAGE_API_KEY=...
fly deploy
```

The resulting public endpoint follows the pattern `https://<app-name>.fly.dev/mcp`.

### Quick test

```bash
# Health check
curl https://ora-mcp-claudeai.fly.dev/health

# MCP Inspector (interactive)
npx @modelcontextprotocol/inspector
# then point it at https://ora-mcp-claudeai.fly.dev/mcp
```

### Corpus maintenance

The corpus and its build pipeline live **inside this project** (`corpus/` and `build/`). To update, run from the `ora-mcp/` directory:

```bash
cd ora-mcp                                   # if you're at the monorepo root
# Add or modify files under corpus/, then:
pip install ".[build]"                       # if not done already
python build/chunk_corpus.py --apply         # corpus → chunks.jsonl
python build/ingest_qdrant.py --apply        # chunks.jsonl → Qdrant
```

The MCP server picks up changes automatically (it reads from the same Qdrant collection `ora_chunks`). No redeploy needed for corpus updates.

The `build/youtube_pipeline/` sub-project (optional extension that transcribes and distills YouTube videos from the leaders into corpus material) requires `pip install ".[youtube]"` and an OpenAI API key in `build/.secrets/api keys.txt`.

### Stack

- **MCP SDK:** `mcp` (FastMCP, streamable HTTP transport)
- **Vector store:** Qdrant Cloud (read-only)
- **Embeddings:** Voyage `voyage-4-large` + `rerank-2.5`
- **Server framework:** Starlette + Uvicorn
- **Auth:** OAuth 2.1 permissive provider (for claude.ai web connector compatibility)
- **Rate limit:** in-memory sliding window (30 req/min/IP)

### Technical documentation

Architectural decisions and rationale in [`DECISIONS.md`](./DECISIONS.md). Lessons learned during development in [`LEARNINGS.md`](./LEARNINGS.md).

---

## Author

Riccardo Ceccaroni — `riccardoceccaroni02@gmail.com`
