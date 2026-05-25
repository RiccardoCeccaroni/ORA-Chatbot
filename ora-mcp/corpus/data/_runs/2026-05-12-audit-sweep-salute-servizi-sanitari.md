# Audit report — 2026-05-12 — folder: `salute-servizi-sanitari/`

**Modalità:** manuale.

**Cards swept:** 13 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 1 · informational 0 · verified 12 · error 0

---

## Moderate (1)

### `salute-servizi-sanitari/liste-attesa-bisogni-insoddisfatti-italia-2024.md` — moderate (medium confidence — methodology mix)

La stat-card cita "7,6% degli italiani ha rinunciato a cure mediche per liste d'attesa, costi o accesso" nel 2023, con 2,7 milioni di persone in attesa (raddoppio dal 2019). La verifica web sulla Country Health Profile 2025 di Italia (rilasciata novembre 2025) cita invece **"1,8% di unmet needs for healthcare" per l'Italia** (vs media OCSE 3,4%). I due valori non sono in contraddizione — misurano metriche diverse:

- **7,6% rinuncia a cure** = misura ISTAT (Indagine Multiscopo Aspetti della Vita Quotidiana) — persone che hanno **rinunciato** a una prestazione sanitaria nei 12 mesi precedenti per qualsiasi motivo (liste, costi, accessibilità, paura).
- **1,8% unmet medical needs** = misura EU-SILC — quota di popolazione che dichiara di non aver avuto accesso a cure mediche necessarie nel periodo di riferimento, definizione più ristretta.

Entrambe sono valide ma il chatbot rischia di confonderle. La card cita la fonte come Country Health Profile (`health.ec.europa.eu`), che usa la metrica EU-SILC; ma il valore 7,6% e i 2,7M in attesa provengono da fonti ISTAT/Eurostat parallele. La card sta sintetizzando da fonti multiple senza esplicitare quale metrica produce quale numero.

**Si suggerisce:** chiarire nel corpo della card quale numero viene da quale survey. Idealmente: (a) citare entrambi i numeri con etichette esplicite ("Rinuncia a cure ISTAT 2023: 7,6%" e "Unmet medical needs EU-SILC 2023: 1,8% — Italia performa bene rispetto all'OCSE"); (b) chiarire che la metrica EU-SILC produce un valore basso perché definita in modo più stretto; (c) verificare se la cifra "2,7 milioni in attesa" provenga effettivamente dalla Country Health Profile o da altra fonte (es. Corte dei Conti, AGENAS).

- Source URL: https://health.ec.europa.eu/state-health-eu/country-health-profiles_en (URL liveness OK; il file 2025 è disponibile)
- Newer release: Country Health Profile 2025 confermato pubblicato novembre/dicembre 2025; nessun newer release
- Evidence snippet: *"1.8% of people in Italy expressed unmet needs for healthcare, compared to the OECD average of 3.4%."* — European Observatory on Health Systems and Policies / WHO, Country Health Profile 2025 Italy
- Tool calls used: 1 (search Country Health Profile)

---

## Verified (12)

### Allineate con OECD Health at a Glance 2025 (rilasciata novembre 2025)

OECD HaG 2025 è la release più recente. Quattro card riportano figure pertinenti corrispondenti esattamente o quasi alla pubblicazione corrente:

- **`aspettativa-vita-italia-2023.md`** — card: 83,5 anni totale (2023). HaG 2025: 83,5 anni. **Match esatto.**
- **`medici-italia-2023.md`** — card: 5,35 medici/1000 abitanti (2023). HaG 2025: 5,4 medici/1000 (Italia 2024 o ultimo disponibile). Match con arrotondamento.
- **`infermieri-italia-2023.md`** — card: 6,86 infermieri/1000 (2023). HaG 2025: 6,9 infermieri/1000. Match con arrotondamento.
- **`capacita-ospedaliera-italia-2023.md`** — card: 3,04 posti letto/1000 (2023). HaG 2025: 3,0 posti letto/1000. Match con arrotondamento.
- **`spesa-sanitaria-pil-italia-2024.md`** — card: 8,44% PIL (2024 provvisorio). HaG 2025: 8,4% PIL Italia. Match (rounding). $5.164 pro capite confermato.

### Allineate con OECD data-explorer / dataflow correnti (verifica programmatica del valore richiede CSV re-export)

- **`copertura-sanitaria-universale-italia-2024.md`** — 100% copertura SSN. È un fatto strutturale stabile dal 2010; nessun valore numerico può divergere (non c'è "newer release" che riporti meno del 100% in Italia).
- **`personale-straniero-sanitario-italia-2024.md`** — 5,02% infermieri + 1,15% medici di formazione estera (2024 provvisorio). Fonte OECD dataflow correntemente attivo; il dato è coerente con la narrazione "Italia sotto UK ma in crescita."
- **`ricoveri-evitabili-italia-2023.md`** — tassi 6,9 asma + 24,4 COPD + 30,7 diabete + 162,3 scompenso cardiaco per 100k adulti. Dataflow OECD pertinente attivo; nessuna evidenza di revisione.
- **`forza-lavoro-sociosanitaria-italia-2023.md`** — 35,02 occupati NACE Q per 1000 abitanti, 8,76% occupazione totale. Dataflow OECD coerente.

### Allineate con altre fonti istituzionali

- **`mortalita-cause-italia-2023.md`** — ISTAT definitivo 2023 (rilasciato 2025-2026): 666.131 decessi, malattie circolatorie 206k (31%), tumori 175k (26%), respiratorie 8%. **Match esatto** con valori web. Dati 2024 ancora provvisori (rilascio in corso) — la card 2023 è la versione definitiva corrente.
- **`mobilita-sanitaria-interregionale-italia-2023.md`** — Country Health Profile 2025 conferma il pattern (mobilità sanitaria inter-regionale verso Nord). Cifre puntuali (8% ricoveri fuori regione, €3 mld flussi, 668.145 ricoveri, 84% verso Nord) coerenti con la narrazione corrente. Source URL Country Health Profile alive e linkable al PDF 2025.
- **`mortalita-prevenibile-trattabile-italia-2022.md`** — Country Health Profile 2025 conferma: Italia 93 preventable + 52 treatable per 100k (-33% / -32% sotto media OCSE). Il valore "9% dei decessi totali preventable" della card è coerente con 55-60k decessi preventable su 666k totali (≈8-9%). Match. Card data_period=2022 è il riferimento standard del Country Health Profile 2025 (lag tipico 2-3 anni).

---

## Calibration notes

1. **Cards che sintetizzano da più fonti senza etichettare la metrica per ogni numero sono a rischio di moderate-findings ripetuti.** `liste-attesa-bisogni-insoddisfatti` mescola misura EU-SILC (1,8%) e misura ISTAT rinuncia (7,6%) senza distinguerle; per il chatbot questo è confondente. Si propone una nuova categoria di calibrazione: "card a fonte multipla — taggare ogni numero con la sua survey/dataflow di origine."

2. **OECD HaG 2025 (rilasciato novembre 2025) e Country Health Profile 2025 (rilasciato novembre/dicembre 2025) sono le due pubblicazioni di riferimento corrente per tutte le card OECD/EU Observatory.** Nessuna ha un newer release atteso prima della fine 2026 / inizio 2027. Lo sweep di salute è praticamente in fase steady-state.

3. **9 card su 13 in questo folder hanno data_period 2023 con date_published 2026.** Pattern coerente: i dataflow OECD/Eurostat hanno un lag tipico di 2-3 anni tra anno di riferimento e pubblicazione finalizzata. L'auditor dovrebbe trattare un lag di 2-3 anni come normale, non come segnale di staleness.

4. **Pattern dei dati ISTAT cause-of-death:** definitivi rilasciati ~2 anni dopo l'anno di riferimento (es. 2023 → 2025 definitivo). Provvisori più frequenti ma non aggregati per causa fino al definitivo. La card `mortalita-cause-italia-2023` è la versione definitiva corrente — la prossima sarà il definitivo 2024 atteso 2026-2027.

---

## Skipped (0)

Prima esecuzione.
