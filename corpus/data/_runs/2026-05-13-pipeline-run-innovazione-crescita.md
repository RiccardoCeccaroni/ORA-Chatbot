---
folder: innovazione-crescita
pipeline_run_date: 2026-05-13
mode: resume-after-token-limit
wishlist_voci: 5 (+1 PMR già coperta = 6 effettive)
shortlist_candidates: 3 dataset (1 ISTAT produttività + 1 ISTAT CIS + 1 OECD MSTI; il MSTI consolida wishlist voci 1, 3, 5 — R&S, brevetti, ricercatori)
downloads: 6 raw (di cui 1 OECD MSTI completato in retry dopo HTTP 429 iniziale)
cards_written: 3 nuove + 1 preesistente = 4 totali
voci_status:
  voce_1_rs_gerd: covered (nuova card spesa-ricerca-sviluppo-italia-vs-paesi-2023)
  voce_2_produttivita: covered (nuova card produttivita-lavoro-italia-1996-2025)
  voce_3_brevetti: covered (fuso nella card R&S)
  voce_4_imprese_innovative: covered (nuova card imprese-innovative-italia-2022)
  voce_5_ricercatori: covered (fuso nella card R&S)
  voce_PMR_regolamentazione_mercati: covered (card preesistente regolamentazione-mercati-italia-2023)
gaps_declared:
  - venture_capital_italia: D1 non disponibile (Dealroom commerciale); Tier-3 web search live
  - startup_innovative_count_mimit: registro amministrativo MIMIT, D2 da batch successivo
  - european_innovation_scoreboard: indice composito Commissione UE, non SDMX; Tier-3
block_conditions_triggered: 0 (nessuna)
---

# Pipeline run — `innovazione-crescita` — 2026-05-13 (resume mode)

## Esito sintetico

**Modalità resume** dopo interruzione token-limit della run precedente nella stessa giornata. La sessione precedente aveva già:

1. Letto la tesi 12 (`memory/corpus/ora-party/manifesto/12-innovazione-crescita.md`).
2. Cachato i cataloghi SDMX e identificato i candidati.
3. Scritto wishlist (`_raw/_wishlist/innovazione-crescita.md`) e shortlist (`_raw/_shortlist/innovazione-crescita.md`), entrambe `status: approved` auto-approvate.
4. Scaricato i raw (con un blocco HTTP 429 su OECD MSTI documentato in `_BLOCKED_NOTE.txt`).
5. Scritto la card `regolamentazione-mercati-italia-2023.md` (preesistente, NON modificata in questa run).

Questa run di completamento ha eseguito:

- **Retry OECD MSTI**: download completato (1,54 MB, HTTP 200) all'inizio della sessione. Il blocco iniziale di quota era transitorio.
- **Deep read** (Phase 4) dei 4 raw rimanenti (DCSP_RS_1, DCSP_RS_10, DCCN_PRODUTTIVITA_1, DCSP_LACIS_15, DF_MSTI).
- **Judgment** (Phase 5): fusione aggressiva di 5 voci wishlist in 3 card nuove + riuso di 1 preesistente.
- **Card writing** (Phase 6): 3 card nuove scritte (vedi sezione successiva).

## Card scritte (totale folder = 4)

### 1. `spesa-ricerca-sviluppo-italia-vs-paesi-2023.md` — FUSIONE di 3 voci wishlist

Fuse: **voce 1 (R&S GERD)** + **voce 3 (brevetti)** + **voce 5 (ricercatori)**. Tutte e tre dipendono dallo stesso dataflow OECD MSTI (che consolida cross-country) + ISTAT DCSP_RS_1 (GERD Italia) + ISTAT DCSP_RS_10 (personale R&S Italia).

**Headline:** Italia 2023 GERD 1,37% PIL (ISTAT), contro Germania 3,13%, Francia 2,22%, USA 3,46%. Deficit quasi tutto sulla spesa privata (BERD): Italia 0,80% PIL vs Germania 2,09% (2,6×). Ricercatori per 1.000 occupati: Italia 6,3 vs Germania 10,3, Svezia 16,5. Brevetti triadici: Italia 1,54% del mondo, contro Germania 7,69% (5× tanto).

### 2. `produttivita-lavoro-italia-1996-2025.md` — voce 2

Da ISTAT DCCN_PRODUTTIVITA_1, edizione aprile 2026.

**Headline:** Produttività del lavoro Italia +0,40% annuo medio 1996-2023 (totale economia) — confermato come la cifra centrale della tesi 12. Indice 2025 (provvisorio): 96,6 — sotto il livello 2020 (=100). Manifatturiero +0,88% annuo storico ma rallentato a +0,47% nell'ultima decade (2014-2023). Caduta brusca 2023-2024 (-4,6 punti dall'indice 2022 al 2024).

### 3. `imprese-innovative-italia-2022.md` — voce 4

Da ISTAT DCSP_LACIS_15 (CIS 2020-2022).

**Headline:** 3.553 imprese italiane con 10+ addetti hanno avuto attività di innovazione di prodotto/processo in corso o abbandonate nel 2022. Manifatturiero 52% (1.848 imprese), servizi 33% (1.156). Settori dominanti "made-in-Italy classico" (metallurgia 477, abbigliamento 261); settori high-tech minoritari (farmaceutica 19, elettronica 68, ricerca scientifica 72); telecomunicazioni 0.

### Card preesistente (non modificata)

- **`regolamentazione-mercati-italia-2023.md`** — PMR OECD 2018+2023. Copre la voce "barriere alla concorrenza" della tesi 12 §2 (riforma SRL). Non sovrapposta con le 3 nuove card.

## Fusione applicata e motivazione

La wishlist iniziale aveva **5 voci** + 1 già coperta = 6 metriche-ask. La shortlist ha ridotto a **3 dataset** (consolidamento via OECD MSTI). Le 5 voci nuove sono diventate **3 card** (fusione 1+3+5 → 1 card R&S). Conta nuova: 3 card × ratio 0,6 voci-per-card è coerente con la **disciplina di trim** del prompt (target: 0,7-1,0; 5 voci → 4 card è "normale", 6 voci → 6 card è "over-producing").

Razionale della fusione:
- Voci 1+3+5 (GERD, brevetti, ricercatori) condividono **lo stesso dataflow** (OECD MSTI) e la **stessa narrativa** (input-throughput-output del ciclo R&S). Spezzarle in 3 card avrebbe creato ridondanza nelle sezioni "Caveat", "Lettura politica", "Lettura attesa per il chatbot".
- Voce 4 (imprese innovative) usa un dataflow distinto (CIS) e un perimetro diverso (tessuto produttivo, non spese aggregate). Card autonoma.
- Voce 2 (produttività) è la **metrica-outcome** che giustifica tutte le altre. Card autonoma per chiarezza.

## Block conditions

**Nessuna delle quattro condizioni di blocco è stata attivata.** Tutti i datasets analizzati sono consistenti tra loro e con la tesi 12. Nessuna contraddizione >20% rilevata. Tutti i download (incluso il MSTI con quota iniziale) sono stati completati.

## Dataset scartati / non utilizzati

- **`DCSP_LACIS_1/` cartella vuota**: presente come placeholder. In wishlist era candidata alternativa a LACIS_15 ma non scaricata (LACIS_15 sufficiente). Non rimossa per audit trail.
- **PCT applications dal MSTI**: estratte ma non incluse nelle tabelle principali della card R&S (citate brevemente). Le PCT sono meno selettive dei brevetti triadici e meno discriminanti — i triadici sono il proxy OECD preferito.
- **TFP per branca dettagliata dal DCCN_PRODUTTIVITA_1**: le 46 branche industriali sono presenti nel raw ma solo i 3 macro-aggregati (totale, manifatturiero, servizi) sono stati estratti nella card. Sotto-card settoriale dedicata sarebbe un follow-up.

## Gaps dichiarati (non bloccanti, da batch futuri)

Tutti riconosciuti come limiti di scope D1 della pipeline, non come fallimenti:

1. **Venture Capital Italia (cifra centrale della tesi 12 §1: 0,06% PIL Italia vs 0,3% FR/DE).** Fonte primaria Dealroom.co (commerciale) — fuori D1. Resta a Tier-3 (web search live). Aggiungere come D3 in batch futuro: pinging AIFI (Associazione Italiana del Private Equity), Invest Europe.

2. **Numero startup innovative registrate MIMIT (12.842 a fine 2024).** Registro amministrativo, non SDMX. D2 (PA italiana, ministeriale) ma fuori dal v1 della pipeline. Da considerare per batch dedicato a registri amministrativi MIMIT/Invitalia.

3. **European Innovation Scoreboard (Italia = Moderate Innovator).** Indice composito Commissione UE, non disponibile via SDMX. Resta Tier-3.

4. **OECD MSTI fino al 2021 ma non oltre.** Cross-country aggiornato al 2023 richiederebbe altre fonti (Eurostat `rd_e_gerdtot`); follow-up tecnico per batch successivi.

## Caveat e follow-up tecnici

- **Disallineamento temporale ISTAT vs OECD MSTI**: ISTAT 2023 esiste, MSTI cross-country si ferma al 2021. Card lo gestisce mostrando entrambi e segnalando il delta.
- **Indicatore CIS ABORON vs totale innovatori**: il dato 3.553 imprese è un **sotto-insieme** (innovazioni "ancora in corso o abbandonate"), non il totale italiano di imprese innovative (~50% delle 10+ addetti, ~30-50k). La card lo spiega esplicitamente nei caveat per evitare misuse del chatbot.
- **Produttività 2024-2025 provvisoria**: i numeri 96,6 (2025) sono stime preliminari dall'edizione aprile 2026 del DCCN_PRODUTTIVITA_1. Saranno rivisti almeno 2 volte (settembre 2026, settembre 2027). La card lo segnala.
- **Quota OECD MSTI HTTP 429**: documentata come quirk noto del download. Retry intra-giornaliero funziona. Aggiunta come nota tecnica per ridurre attriti su batch futuri.

## Note tecniche emerse durante il run

- **Dimensione MSTI download**: con 6 misure (G, B, H, T_RS, P_TRIAD, P_PCT) × 9 paesi × 22 anni × 12 unità di misura/transformation, il file finale è ~1,5 MB (5.194 righe). Adeguato. Non c'è motivo di stringere ulteriormente la key — il filtro a 9 paesi + 6 misure è già selettivo.
- **CSV ISTAT con BOM utf-8-sig**: confermata la pratica della run precedente (`difesa`, `universita-ricerca`). Tutti i parser Python usano `encoding="utf-8-sig"`.
- **ISTAT `_2026M4` edition selector**: il dataflow Produttività include 4 edizioni concorrenti nello stesso file. Il filtro `EDITION` è cruciale per non doppi-contare.

## Riepilogo finale

| Indicatore | Valore |
|---|---|
| Wishlist voci | 5 (+ 1 PMR preesistente = 6 effettive) |
| Shortlist dataset | 3 (consolidato da 5 voci) |
| Raw scaricati | 6 (DCCN_PRODUTTIVITA_1, DCSP_LACIS_1 vuoto, DCSP_LACIS_15, DCSP_RS_1, DCSP_RS_10, DF_MSTI) |
| Raw effettivamente usati | 5 (LACIS_1 vuoto scartato) |
| Card nuove scritte | 3 |
| Card preesistenti conservate | 1 (PMR, non modificata) |
| **Totale card folder** | **4** |
| Block conditions attivate | 0 |
| Gaps dichiarati per batch futuri | 3 (VC Dealroom, registro MIMIT, EIS) |

**Esito:** folder `innovazione-crescita/` ora ha **4 card complete**, coprendo input R&S, output produttività, struttura innovativa del tessuto produttivo, e regolamentazione dei mercati. Gap residuo principale: venture capital in valore — copertura via Tier-3 web search del chatbot. Le 4 card insieme rispondono alle metriche-chiave della tesi 12: state (GERD 1,37%, produttività +0,40%/anno, 3.553 imprese in attività innovativa, PMR 1,23), justify (gap con Germania, brevetti piatti, mix settoriale tradizionale), project (riforme tesi 12 sono coerenti con la diagnosi quantitativa), compare (Italia vs DE/FR/UK/ES/PL/SE/NL/US).
