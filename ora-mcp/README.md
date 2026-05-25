# ORA! — MCP server

Espone il corpus curato del partito **ORA!** agli assistenti AI che parlano il
protocollo MCP (Model Context Protocol). Server pubblico, accessibile da
Claude Desktop, Cursor, ChatGPT con MCP, e altri client conformi.

---

## Per la direzione di ORA! — perché esiste

L'idea iniziale era un chatbot autonomo sul sito ora-italia.it. La direzione
ha preferito un'alternativa: invece di un bot che parla a nome del partito,
**rendere disponibili le posizioni di ORA! agli assistenti AI** che il
pubblico già usa quotidianamente.

### Cosa cambia rispetto al chatbot

| Chatbot                                | MCP server                              |
|----------------------------------------|-----------------------------------------|
| Parla a nome del partito (rischio).    | Il partito **non parla**. Restituisce documenti, l'AI dell'utente li cita. |
| Il partito deve ospitarlo sul sito.    | Si attiva in Claude Desktop / Cursor / ChatGPT — zero modifiche al sito. |
| Il partito si assume la responsabilità delle risposte. | Il partito è la **fonte**, non l'enunciatore. |
| Audience limitata ai visitatori del sito. | Audience: chiunque usi un'AI moderna e voglia approfondire ORA!. |

### Cosa offre, in pratica

Quando un giornalista, ricercatore, o elettore chiede a Claude *«qual è la
posizione di ORA! sulla riforma fiscale?»*, Claude può chiamare in tempo
reale questo server, recuperare i passaggi rilevanti del manifesto, e
**citarli verbatim** con riferimento al documento sorgente.

### Cosa contiene il corpus

- Manifesto completo (21 tesi programmatiche)
- Comunicati ufficiali e newsletter
- Documenti di identità, statuto, fondamenti, codice etico
- Profili tematici di Boldrin e Forchielli (citati sempre come vista personale)
- Schede statistiche curate da ISTAT, Eurostat, OECD, Banca d'Italia
- Profili comparativi degli altri principali partiti italiani (per confronto)

In totale: **3.665 documenti indicizzati**, aggiornabili quando il
partito lo decide.

### Cosa NON fa

- Non parla a nome del partito (non genera risposte; restituisce fonti).
- Non scrive sui social, non risponde alle email, non gestisce contatti.
- Non sostituisce il sito ora-italia.it; lo affianca.

### Come si demo

1. Apri Claude Desktop.
2. Incolla la configurazione fornita in `demo/claude_desktop_config.json`.
3. Riavvia.
4. Fai una delle domande in `demo/demo_questions.md`.

---

## Per gli sviluppatori — come si usa

### Endpoint

- **MCP (streamable HTTP):** `<host>/mcp`
- **Landing page (HTML):** `<host>/`
- **Health check:** `<host>/health`

### Tools esposti

- `find_position(topic, top_k_per_bucket=5, include_comparison=False, include_leaders=True, date_from?, date_to?)` — **tool principale**. Restituisce la posizione di ORA! su un tema, organizzata in bucket per affidabilità: `official_party`, `leader_views` (Boldrin / Forchielli), `supporting_data` (stat-cards), `comparison` (altri partiti, opzionale).
- `data_lookup(metric, period?, quality_tier_floor="D3", top_k=5)` — schede statistiche, ordinate per qualità della fonte.

### Resources esposte

- `ora://about` — chi è ORA!, gli obiettivi, la gerarchia di affidabilità.
- `ora://manifesto` — manifesto completo (21 tesi, ~575 KB).
- `ora://statuto` — statuto del partito (~57 KB).
- `ora://fondamenti` — 15 fondamenti programmatici, Allegato 2 (~10 KB).
- `ora://codice-etico` — codice etico, Allegato 3 (~4 KB).

### Esecuzione locale

```bash
# 1. Installa
pip install -e .

# 2. Configura le credenziali
cp .env.example .env
# Modifica .env: QDRANT_URL, QDRANT_API_KEY, VOYAGE_API_KEY

# 3. Avvia
python -m ora_mcp.server
# → http://localhost:8000/mcp
```

### Deploy su Fly.io

```bash
fly launch --no-deploy --copy-config --name ora-mcp
fly secrets set QDRANT_URL=... QDRANT_API_KEY=... VOYAGE_API_KEY=...
fly deploy
```

L'endpoint pubblico risultante è `https://ora-mcp.fly.dev/mcp`.

### Test rapido

```bash
# Health check
curl https://ora-mcp.fly.dev/health

# Ispettore MCP (interattivo)
npx @modelcontextprotocol/inspector
# poi punta a https://ora-mcp.fly.dev/mcp
```

### Manutenzione del corpus

Il corpus e la pipeline di costruzione vivono **dentro questo progetto**
(`corpus/` e `build/`). Per aggiornare:

```bash
# Aggiungi/modifica file in corpus/, poi:
pip install ".[build]"                       # se non già fatto
python build/chunk_corpus.py --apply         # corpus → chunks.jsonl
python build/ingest_qdrant.py --apply        # chunks.jsonl → Qdrant
```

L'MCP server vede le modifiche automaticamente (legge dallo stesso indice
Qdrant `ora_chunks`). Nessun redeploy necessario per aggiornamenti del
corpus.

Il sotto-progetto `build/youtube_pipeline/` (estensione opzionale per
trascrivere e distillare video YouTube dei leader nel corpus) richiede
`pip install ".[youtube]"` e una chiave OpenAI in
`build/.secrets/api keys.txt`.

### Stack

- **MCP SDK:** `mcp` (FastMCP, streamable HTTP transport)
- **Vector store:** Qdrant Cloud (read-only)
- **Embeddings:** Voyage `voyage-4-large` + `rerank-2.5`
- **Server framework:** Starlette + Uvicorn
- **Rate limit:** in-memory sliding window (30 req/min/IP)

### Documentazione tecnica

Decisioni architetturali e razionali in [`DECISIONS.md`](DECISIONS.md).

---

## Autore

Riccardo Ceccaroni — `riccardoceccaroni02@gmail.com`
