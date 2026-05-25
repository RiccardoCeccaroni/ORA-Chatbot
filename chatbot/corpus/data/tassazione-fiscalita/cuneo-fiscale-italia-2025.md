---
id: cuneo-fiscale-italia-2025
type: data
attribution: oecd
quality_tier: D1
title: "Cuneo fiscale, Italia, 2025"
data_metric: "Average tax wedge (AV_TW) — totale imposte sul lavoro + contributi sociali come % del costo totale del lavoro, lavoratore single senza figli al 100% del salario medio"
data_period: "2025; serie 2016-2025"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Taxing Wages, dataflow DSD_TAX_WAGES_COMP@DF_TW_COMP"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 4643dd149fcc2c53f3587b41fc64b6c0de05dcafde40cb46ed400bf605bfb827
tags: [tassazione-fiscalita, lavoro-politiche-sociali]
description: "Cuneo fiscale italiano per lavoratore single al salario medio — 45,76% del costo del lavoro nel 2025, +4 punti percentuali sopra la media UE-22 OECD."
---

# Cuneo fiscale, Italia, 2025

**Valore (2025):** **45,76%** del costo totale del lavoro.
**Definizione precisa:** quota di imposte sul reddito + contributi sociali (lavoratore + datore di lavoro) sul costo totale del lavoro, calcolata per un **lavoratore single, senza figli, retribuito al 100% del salario medio italiano**.
**Variazione 2024 → 2025:** -1,20 p.p. (riduzione marcata).
**Distanza dalla media UE-22 OECD 2025:** **+4,03 p.p.** (Italia 45,76% vs EU22 41,73%).

## Serie storica — cuneo Italia vs comparatori

| Anno | Italia | EU-22 OECD | Germania | Francia | Spagna |
|---|---|---|---|---|---|
| 2016 | 47,76 | 42,40 | 49,50 | 48,02 | 39,38 |
| 2017 | 47,66 | 42,20 | 49,54 | 47,44 | 39,58 |
| 2018 | 47,73 | 41,99 | 49,47 | 47,41 | 39,68 |
| 2019 | **47,91** ← picco | 41,85 | 49,27 | 47,17 | 39,79 |
| 2020 | 46,90 | 41,54 | 48,81 | 46,48 | 39,33 |
| 2021 | 46,03 | 41,32 | 48,14 | 46,90 | 39,87 |
| 2022 | 45,62 | 41,32 | 48,29 | 47,08 | 40,05 |
| 2023 | 45,48 | 41,53 | 47,71 | 46,87 | 40,75 |
| 2024 | **46,96** | 41,64 | 47,93 | 47,12 | 41,14 |
| **2025** | **45,76** | **41,73** | **49,26** | 47,18 | 41,44 |

**Trend Italia:** dal picco del 47,91% (2019) il cuneo è sceso di ~2 punti in 6 anni. Nel 2024 risalita transitoria (46,96%), ribasso nel 2025 (45,76%).

**Posizionamento internazionale 2025:** l'Italia resta tra i paesi OCSE con cuneo più alto, ma è **sotto Germania (49,26%)** e in linea con Francia (47,18%). La distanza dalla Spagna (41,44%) è di **+4,3 p.p.**

## Come si costruisce il numero — esempio numerico

Per un lavoratore single al 100% del salario medio italiano (riferimento OECD 2025), il **costo totale del lavoro** (=100) si scompone così:

- **Take-home pay del lavoratore (~54,2%)**
- **Cuneo fiscale (45,76%):**
  - Imposta sul reddito (IRPEF) del lavoratore
  - Contributi sociali a carico del lavoratore (~9-10% lordo)
  - **Contributi sociali a carico del datore di lavoro (~30%)** — la componente più pesante in Italia

In Italia il cuneo è **strutturalmente alto sulla componente datoriale**: vedi [[entrate-fiscali-totali-italia-2024]] — il 68,7% dei contributi sociali totali italiani è versato dal datore di lavoro.

## Per chi è e per chi non è questo numero

**Questo numero descrive specificamente:**
- single
- senza figli
- al 100% del salario medio (≈ €33-35.000 lordi/anno nel 2024-25)

**NON descrive:**
- famiglie con figli (cuneo inferiore — Italia ha sostegni famiglia tramite Assegno Unico)
- lavoratori a basso reddito (AW67 — 67% del salario medio) — cuneo inferiore grazie al taglio cuneo 2024-25
- lavoratori ad alto reddito (AW167 — 167% del salario medio) — cuneo superiore
- coniugi a singola entrata

Per la versione disaggregata per tipo di famiglia e fascia di reddito serve il dataset OECD parallelo `DSD_TAX_WAGES_COU@DF_TW_COU` (non incluso in questo batch — la versione scaricata aveva 0 righe italiane per filtro errato, da riscaricare).

## Riforme italiane recenti riflesse nei numeri

- **2020-2022:** taglio progressivo del cuneo per i redditi medio-bassi (esonero contributivo 0,8% → 2% → 3%).
- **2023:** estensione al 7% per redditi sotto €25.000 e 6% sotto €35.000.
- **2024:** Legge di Bilancio 2024 — taglio strutturale del cuneo per €15-20 mld, ma il dato AW100 single non vede il taglio (mirato sotto AW100).
- **2025:** ulteriori interventi di "decontribuzione" e revisione IRPEF. Il dato 45,76% riflette parzialmente questi interventi.

## Metodologia

Framework: **OECD Taxing Wages** — definizione armonizzata e calcolata centralmente da OECD, **non auto-dichiarata dai paesi**, per garantire confronto cross-country. Pubblicazione annuale ad aprile.

- **Numeratore:** imposta sul reddito + SSC lavoratore + SSC datore di lavoro − benefit familiari rilevanti.
- **Denominatore:** costo totale del lavoro per il datore di lavoro = salario lordo + SSC datore di lavoro.
- **Salario medio (AW = Average Wage):** definito da OECD come media dei salari lordi degli adulti, full-time, settore privato non agricolo. Per l'Italia 2024 ≈ €35.000 lordi.

## Caveat e note di lettura

- **Cifra "single AW100" ≠ cuneo medio italiano.** Il "cuneo medio" tout court è una media ponderata su tutti i lavoratori e tutte le composizioni familiari. Il 45,76% è il punto specifico single-AW100 — il più citato perché standard cross-country, ma non rappresentativo della media nazionale.
- **Confronto con cifre MEF/Bankitalia.** Il Documento di Economia e Finanza e la Banca d'Italia citano spesso un cuneo italiano "medio" del 45-46% con metodologia leggermente diversa. Le due metodologie convergono sul livello (~46%) ma possono differire di 1-2 punti.
- **Il taglio cuneo 2024-25 è prevalentemente sul lato lavoratore e mirato sotto AW100** — l'effetto sul dato AW100 single è limitato. Per vedere l'impatto del taglio sui bassi redditi serve il dato AW67.
- **Tendenza al ribasso strutturale 2019-2025.** Il calo di 2 punti dal picco 2019 non è dovuto solo alle riforme: l'inflazione 2022-2024 ha eroso parte del cuneo via mancata indicizzazione degli scaglioni IRPEF (drag fiscale effettivo).

## Confronto con altri indicatori

- **Cuneo a famiglie con 2 figli al 100% AW**: riferimento Italia ~35-38% (stima orientativa OECD 2024, da verificare con DF_TW_COU riscaricato). Italia ha un cuneo **considerevolmente più basso per le famiglie** rispetto al cuneo single grazie all'Assegno Unico.
- **Net personal average tax rate (NPATR)** — variante che esclude SSC datoriali: Italia ~30-32% (da verificare).

## Sorgente raw

`_raw/tassazione-fiscalita/DF_TW_COMP/OECD.CTP.TPS,DSD_TAX_WAGES_COMP@DF_TW_COMP,2.1+.AV_TW..S_C0.AW100._Z.A.csv`

Dataset: OECD `DSD_TAX_WAGES_COMP@DF_TW_COMP(2.1)` — Labour taxation, cross-country comparative table. 400 righe (40 paesi × 10 anni), 10 righe Italia.
