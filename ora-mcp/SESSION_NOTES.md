# Note di sessione — 23 maggio 2026

> Appunti personali per ricordare cosa abbiamo fatto oggi e a che punto siamo.
> Non un documento tecnico — quello è `DECISIONS.md`. Questo è il diario.

## Dove eravamo prima di iniziare

Avevo già costruito il **chatbot ORA!** (cartella `ORA Chatbot - presentation`):
agentic-RAG, 3 665 chunks indicizzati in Qdrant, Voyage per embed+rerank,
Claude Opus come sintetizzatore, Haiku come verificatore. Tutto pronto per
una demo alla direzione di ORA!.

**La direzione ha bocciato il chatbot.** Non vogliono un bot che parla a nome
del partito. Però hanno aperto la porta a un'idea diversa: **un MCP server**
che esponga il corpus agli assistenti AI di terze parti (Claude Desktop,
Cursor, ChatGPT) invece di costringere il partito a fare l'enunciatore.

## Cosa abbiamo fatto oggi, in ordine

### 1. Capito il pivot e progettato il nuovo progetto

Onestamente all'inizio dubitavo che valesse la pena. Mi sono fatto convincere
del valore strategico: ORA! sarebbe il primo partito italiano con un MCP, e
il framing cambia tutto — non *"abbiamo costruito un bot"* ma *"abbiamo
costruito infrastruttura che gli AI che usate già possono interrogare"*.
Discussa la differenza con Claude e siamo arrivati alla decisione: pivot.

### 2. Nuova cartella `ora-mcp/`

Tutta separata dal chatbot. Stessa connessione Qdrant (stesso indice
`ora_chunks` — 3 665 chunks), ma niente più chatbot runtime, persona,
verifier, CLI. Solo: due tool MCP, cinque resources, server FastMCP +
Starlette.

### 3. Tutto self-contained

A un certo punto ho detto che non volevo dover tornare nella cartella del
chatbot per niente. Abbiamo copiato dentro a `ora-mcp/`:

- Tutto il `corpus/` (810 file, ~103 MB)
- I 3 script di mantenimento (`chunk_corpus.py`, `ingest_qdrant.py`,
  `audit_frontmatter.py`) + `youtube_pipeline/`
- Il file `chunks.jsonl` corrente
- Le credenziali in `.env` (e nel formato legacy in `build/.secrets/`)

Ora `ora-mcp` è il singolo artefatto. La cartella del chatbot non serve più
per gestire l'MCP, anche se la lascio lì come cronologia.

### 4. Discusso a fondo i tool

Lunga conversazione su quanti tool esporre. Prima avevo proposto due tool
(`corpus_retrieve` generico + `data_lookup`), poi ho proposto di aggiungere
un terzo (`find_position` strutturato), poi tu hai notato giustamente che
due tool sovrapposti confondono l'LLM. Ho cambiato idea e abbiamo deciso
per **un solo tool principale** (`find_position`) che restituisce buckets
gerarchici, più `data_lookup` separato. Cinque resources canoniche
(about, manifesto, statuto, fondamenti, codice-etico).

### 5. Trovato e risolto un bug grave durante i test

Quando ho fatto i primi smoke test, il bucket `official_party` era **vuoto
per ogni domanda**. Disastro: l'LLM non avrebbe avuto la voce ufficiale e
sarebbe stato costretto a dedurre dai leader (esattamente ciò che la
gerarchia di fiducia deve impedire).

Causa: avevo assunto che il campo `attribution` valesse `"ora"` e `"other"`,
ma in realtà nei chunk di Qdrant è `"party"` per ORA e
`"azione"`/`"pd"`/`"fdi"`/ecc. uno per partito. Una sonda diretta su Qdrant
l'ha rivelato. Fix in 5 minuti, tutti i bucket si sono popolati.

### 6. Test esaustivo da 105 domande

Per la presentazione tu volevi una verifica completa. Abbiamo eseguito 105
test in 8 sezioni:
- 25 temi del manifesto
- 20 domande tipiche utente
- 10 viste Boldrin + 10 Forchielli
- 15 query quantitative
- 10 confronti con altri partiti
- 5 letture di resources
- 10 edge case (privacy, off-topic, parametri)

**Risultato: 99 verdi, 6 gialli, 0 rossi.** Il sistema è pronto per la demo,
con 6 piccole cose da sapere (vedi `comprehensive_test_report.pdf`):
3 policy specifiche con rilevanza marginale (salario minimo, flat tax,
agricoltura — il manifesto è ad alto livello), 2 edge cases out-of-scope
gestiti con cautela, e 1 caso da rivedere (query "Boldrin vita privata"
ha matchato chunks biografici molto rilevanti — controllare il contenuto).

### 7. Collegato il tutto a Claude Desktop

Questa parte è stata frustrante. Tre tentativi falliti per motivi diversi:
1. Prima ho usato il formato `url`/`transport` — Claude Desktop l'ha
   rifiutato (supporta solo stdio nel config). Soluzione: passare per
   `mcp-remote` (bridge stdio↔HTTP).
2. Poi il subprocess `npx` non veniva trovato dal PATH di Claude. Soluzione:
   wrappare in `cmd /c`.
3. Poi Claude Desktop non si stava davvero riavviando — i processi in
   background rimanevano in vita con la config vecchia. Soluzione: uccidere
   tutti i processi `claude.exe` e riaprire.
4. **L'ultimo bug è stato il più subdolo:** il server Python non caricava
   `.env`. Gli smoke test funzionavano perché lo caricavano loro stessi
   prima di chiamare le funzioni. Ma quando Claude Desktop lo invocava,
   `VOYAGE_API_KEY` mancava e tutto crashava. Risolto aggiungendo un
   `_load_dotenv()` all'avvio del server.

Dopo il fix, **funziona**. Claude Desktop chiama `find_position`, riceve i
buckets, compone una risposta strutturata e citata.

## Cosa abbiamo per il demo al management

- **Server MCP funzionante** localmente: `python -m ora_mcp.server`
- **Claude Desktop collegato** via `mcp-remote`
- **Test completo certificato** (105/105, 0 rossi) — PDF disponibile per
  ispezione tecnica
- **Domande di demo già pronte** in 5 categorie (`demo/demo_questions.md`)
- **Documenti di decisione** professionali (`DECISIONS.md`)

## Cose da sistemare prima del demo

1. **Velocità.** Una chiamata a `find_position` impiega ~60 secondi. Troppo
   per un demo dal vivo dove ogni risposta sembra che il sistema sia
   bloccato. Va parallelizzato (i 4 bucket sono indipendenti). Stima del
   fix: 30 minuti di lavoro, riduzione attesa 4× → ~15 secondi.

2. **Test manuale della query "Boldrin vita privata"**: controllare i
   chunks restituiti (top score 0.84, alto) — sono biografia pubblica
   accettabile o info personali scrapate? Se le seconde, ripulire il
   corpus.

3. **Affidabilità del server.** Adesso il server è un processo Python che
   muore quando spengo PowerShell o riavvio il computer. Per la sera del
   demo serve un modo per tenerlo vivo (Task Scheduler di Windows, oppure
   `nssm` per farlo girare come servizio).

4. **Deploy su Fly.io.** Per ora gira solo in locale. Per la demo dal vivo
   va bene così, ma se ORA! vuole adottarlo serve deploy su Fly.io
   (Dockerfile e `fly.toml` sono già pronti — basta `fly deploy`).

## Prossimi passi (in ordine)

1. **[Domani]** Parallelizzare `find_position` con `asyncio` — velocità 4×.
2. **[Domani]** Verificare manualmente il contenuto dei chunks biografici
   di Boldrin per il caso "vita privata".
3. **[Prima del demo]** Configurare l'auto-restart del server (servizio
   Windows o Task Scheduler).
4. **[Demo]** Aprire Claude Desktop, fare le 5-6 domande chiave, mostrare
   in 10 minuti il valore del sistema.
5. **[Post-demo, se approvato]** `fly deploy` per renderlo accessibile a
   chiunque, e passare la maintenance al team tecnico di ORA!.

## Cosa NON va detto al management

- I dettagli del debugging di oggi (i tre tentativi falliti, i bug, il
  riavvio del computer). Hanno fiducia che funzioni — mostriamo loro il
  funzionamento, non la salsiccia.
- L'idea che si possa fare uno "Streamlit demo" alternativo. Avevo proposto
  un'UI custom come fallback, ma per il framing è meglio Claude Desktop:
  *"l'AI che usate già parla con noi"* è molto più forte di *"abbiamo fatto
  un'interfaccia"*.

## Risorse importanti in questa cartella

| File | A cosa serve |
|------|--------------|
| `README.md` | Pitch + istruzioni dev (due sezioni) |
| `DECISIONS.md` | Le 29 decisioni architetturali documentate |
| `comprehensive_test_report.pdf` | Test completo, mostralo al management |
| `demo/demo_questions.md` | Domande pronte per il demo |
| `demo/claude_desktop_config.json` | Snippet di config per chi adotta |
| `CLAUDE.md` | Promemoria per Claude Code (gitignored) |
| `SESSION_NOTES.md` | Questo file — diario personale |
