# Audit report — 2026-05-12 — folder: `lavoro-politiche-sociali/`

**Modalità:** manuale.

**Cards swept:** 8 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 0 · informational 2 · verified 6 · error 0

**Caveat di metodologia:** le 8 card di questo folder hanno description in frontmatter che descrive la struttura dei dati senza citare valori numerici specifici. La verifica programmatica è quindi limitata al pattern "il dataflow ISTAT è ancora attivo e il periodo citato è il più recente disponibile" — i valori puntuali nel corpo delle card potrebbero divergere ma non sono visibili in questo sweep manuale senza ulteriore inspection.

---

## Informational (2)

### `lavoro-politiche-sociali/retribuzione-mediana-oraria-privati-italia-2023.md` — informational (low-medium confidence)

La stat-card cita la mediana della retribuzione lorda oraria dei dipendenti del settore privato in Italia per il **2023**. La verifica web rileva che il comunicato stampa ISTAT più recente sulla "Struttura delle retribuzioni in Italia" copre l'**Anno 2022** (rilasciato gennaio 2025), con €11,75/ora mediana, €11,25 donne, €14,89 laureati, ecc. La card potrebbe aver attinto a un dataflow ISTAT distinto (`DCSC_RACLI` — Retribuzioni orarie dei dipendenti del settore privato), che è aggiornato annualmente e potrebbe avere il 2023, mentre il comunicato stampa biennale "Struttura delle retribuzioni" resta al 2022.

**Si suggerisce:** verificare il corpo della card per identificare la fonte specifica (`DCSC_RACLI` vs comunicato stampa "Struttura retribuzioni"); se la card cita il dato 2023 da `DCSC_RACLI`, mantenere ma esplicitare che il comunicato "Struttura retribuzioni" (la fonte più narrativa) è ancora fermo al 2022. Se invece la card ha etichettato erroneamente come "2023" dati che provengono dal report 2022, correggere il riferimento.

- Source URL: https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0 (URL liveness OK)
- Newer release: ISTAT comunicato "Struttura delle retribuzioni 2022" (gennaio 2025) — più recente comunicato disponibile; dataflow `DCSC_RACLI` aggiornato annualmente

### `lavoro-politiche-sociali/indici-grandi-imprese-retribuzione-costo-lavoro-italia-2026.md` — informational (medium confidence)

La stat-card riporta gli indici mensili (base 2021=100) delle retribuzioni e del costo del lavoro per le grandi imprese (≥500 dipendenti), serie mensile fino a **2026-02**. La verifica web non ha trovato un valore corrispondente esplicito, ma il pattern di rilascio ISTAT per gli "Indici delle grandi imprese" è mensile con lag di ~2 mesi: il dato 2026-03 dovrebbe essere disponibile dalla fine di maggio 2026, il dato 2026-04 da fine giugno. La card è quindi correntemente al penultimo punto della serie attesa al momento dello scrape (12 maggio 2026).

**Si suggerisce:** ri-fetchare il dataflow dopo il 25 maggio 2026 per aggiungere il punto 2026-03 alla card. Non urgente — la serie è auto-rinfrescante mensilmente; in produzione l'auditor scheduled mensile coprirà automaticamente questi casi.

- Source URL: https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0 (URL liveness OK)
- Newer release: 2026-03 prevista intorno al 25 maggio 2026
- Tool calls used: 0

---

## Verified (6)

### Allineate con ISTAT "Occupati e disoccupati — Anno 2025 provvisorio"

ISTAT ha rilasciato il dato annuale provvisorio 2025 (dato dicembre 2025 + ricalcolo annuo) a inizio 2026: tasso di occupazione 62,5%, tasso di disoccupazione 6,1%, tasso inattività 33,3% (15-64). Tutte le 4 card sotto sono allineate con questa release:

- **`forze-lavoro-italia-2025.md`** — forze di lavoro totali 15+, 2025 annuale provvisorio. Dataflow ISTAT corrente.
- **`disoccupati-italia-2025.md`** — disoccupati 15+, 2025 annuale provvisorio. Allineata con dato 6,1% disoccupazione.
- **`occupati-totali-italia-2025.md`** — occupati 15+, 2025 annuale provvisorio. Allineata con dato 62,5% occupazione.
- **`tasso-occupazione-italia-15-64-2025.md`** — 62,5% per il 2025 annuale (web conferma esattamente).
- **`tasso-disoccupazione-italia-2025.md`** — 6,1% per il 2025 annuale (web conferma). Tasso giovanile dicembre 2025 = 20,5%.

### Altre card ISTAT con dati 2025 correnti

- **`indice-retribuzione-contrattuale-italia-2025.md`** — indice retribuzione contrattuale oraria base dicembre 2021=100, dato annuo 2025. Dataflow corrente ISTAT.

---

## Calibration notes

1. **Le card che descrivono solo la struttura del metric (senza citare valori numerici nella description di frontmatter) sono parzialmente verificabili da un audit veloce.** L'auditor deve aprire il corpo della card per leggere i numeri specifici prima di poter cercare discrepanze. Per uno sweep ad alto throughput, questo aumenta i tool calls per card. Si propone in v2 della spec di richiedere che la description di frontmatter contenga sempre **i valori numerici principali** della card (almeno headline + 1-2 confronti), in modo che un auditor non debba aprire il corpo per ogni card. CLAUDE.md §5 attualmente non lo richiede esplicitamente.

2. **Le card a serie temporale mensile/trimestrale aggiornano frequentemente.** Card 6 (`indici-grandi-imprese`) e l'inflazione (in `sviluppo-economico`) sono casi di alta-frequenza. L'auditor scheduled dovrebbe trattarle in modo differente dalle card "annuali stabili" — controllo settimanale o mensile è sensato per le high-frequency, trimestrale o semestrale per le stable. Si propone una sub-classificazione nel manifest: `series_frequency: monthly | quarterly | annual | structural`.

3. **L'ISTAT pubblica simultaneamente nuovi dati su molti dataflow correlati.** L'auditor ha visto durante lo sweep di immigrazione e di lavoro che ISTAT rilascia in blocco (es. statistiche provvisorie 2025 a marzo 2026 hanno toccato sia migration che labour). Il manifest dell'auditor potrebbe sfruttare questa correlazione: una volta confermato che il rilascio di blocco è uscito, marcare tutte le card del blocco come "newer-release-possibly-available" senza dover fare una search per ognuna.

---

## Skipped (0)

Prima esecuzione.
