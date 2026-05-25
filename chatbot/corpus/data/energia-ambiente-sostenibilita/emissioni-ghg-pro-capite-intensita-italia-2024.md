---
id: emissioni-ghg-pro-capite-intensita-italia-2024
type: data
attribution: eurostat
quality_tier: D1
title: "Emissioni di gas serra pro capite e per unità di PIL, Italia, 2024"
data_metric: "GHG totali pro capite (t CO2eq/abitante) + intensità GHG di GDP (g CO2eq/€); decomposizione metodologica UNFCCC vs Eurostat NACE"
data_period: "2024 (con metodologie miste — vedi caveat); serie storica disponibile"
source_url: "https://ec.europa.eu/eurostat/databrowser/view/env_ac_ainah_r2"
source_doc: "Eurostat — env_ac_ainah_r2 (Air emissions accounts by NACE Rev. 2, yearly) + tps00001 (Population 1 Jan) + ISPRA NID 2026 (per dato territoriale UNFCCC)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 8e201ca9fe787eada5b880fc7b06c9205145a7dd677bce49a42f9dd808f73dca
tags: [energia-ambiente-sostenibilita, sviluppo-economico-politica-industriale, unione-europea]
description: "Italia 2024: emissioni GHG ~6,15 t CO2eq pro capite (UNFCCC, popolazione 58,99M); intensità GHG/PIL ~165,6 g/€. Italia sotto la media UE-27 (~7,0 t pro capite)."
---

# Emissioni di gas serra pro capite e per unità di PIL, Italia, 2024

## Valori chiave 2024

| Metrica | Valore Italia 2024 | Note |
|---|---|---|
| **GHG totali (UNFCCC, escl. LULUCF)** | **363 Mt CO2eq** | da ISPRA NID 2026 (vedi card `emissioni-ghg-italia-2024`) |
| **Popolazione (1 gennaio)** | **58,99 milioni** | Eurostat tps00001 |
| **PIL nominale 2024** | **€2.192 mld** | ISTAT, comunicato "GDP and general government net borrowing 2022-2024" (marzo 2025); cresciuto +2,9% sul 2023 |
| **GHG pro capite** | **6,15 t CO2eq/abitante** | = 363 Mt / 58,99 M |
| **Intensità GHG di PIL** | **165,6 g CO2eq / €** | = 363 Mt / €2.192 mld |

## Confronto UE-27 (anno 2022, per disponibilità Eurostat)

| Paese / Aggregato | GHG pro capite 2022 (t CO2eq) | Intensità GHG/GDP 2022 (g/€) |
|---|---|---|
| **UE-27** | ~7,0 | ~210 |
| **Italia** | ~6,5 | ~240 (resident principle Eurostat) |
| Germania | ~8,7 | ~205 |
| Francia | ~5,3 | ~145 |
| Spagna | ~6,1 | ~210 |
| Polonia | ~9,9 | ~580 |
| Svezia | ~3,7 | ~80 |

**Lettura politica per Italia 2024:**
- **Pro capite:** Italia è **sotto la media UE-27** (6,15 vs ~7,0 t). Ragioni: alto contributo nucleare a livello UE non disponibile in Italia, ma economia italiana relativamente meno intensiva (servizi, turismo) rispetto a Germania.
- **Intensità GHG/PIL:** Italia è **leggermente sopra la media UE** (~167 g/€ UNFCCC vs ~210 g/€ Eurostat resident — vedi caveat metodologico). La Francia con il nucleare batte tutti su questa metrica.

## Decomposizione metodologica UNFCCC vs Eurostat — IMPORTANTE

Le due autorità pubblicano **due numeri diversi** per le emissioni GHG italiane:

| Fonte | Italia 2024 GHG (Mt CO2eq) | Definizione |
|---|---|---|
| **ISPRA / UNFCCC** | **363** (escl. LULUCF) | **Principio territoriale**: emissioni che avvengono fisicamente sul territorio italiano, da chiunque siano effettuate (residenti + non residenti). Esclude bunker marittimi/aviazione internazionale. |
| **Eurostat env_ac_ainah_r2** | **283** (NACE industries TOTAL) + **~80** (TOTAL_HH_FD households) ≈ 363 | **Principio di residenza**: emissioni di residenti italiani ovunque operino (incluse navi battenti bandiera italiana in acque internazionali, voli aerei italiani fuori territorio). |

**La differenza non è una contraddizione** ma **due ottiche diverse**:
- UNFCCC = "cosa emette il suolo italiano" → usato per i target di Paris Agreement e UE Effort Sharing Regulation.
- Eurostat NACE = "cosa emettono le imprese italiane (+ famiglie)" → usato per analisi macroeconomica + bilanciato col PIL Eurostat.

Per **target politici 2030** (Fit for 55, ESR Italia −43,7% vs 2005): **usare UNFCCC** (ISPRA NID).
Per **intensità GHG sul PIL** in contesto comparativo UE: **Eurostat env_ac** è la convenzione di solito utilizzata da Eurostat (es. la cifra Eurostat 240 g CO2eq/€ per Italia 2022 è in questa metrica resident).

## Decomposizione settoriale Italia 2024 (Eurostat env_ac_ainah_r2, principio residente)

| Settore NACE | GHG Italia 2024 (Mt CO2eq) | % del totale industries |
|---|---|---|
| **C — Manifatturiero** | **84,2** | 30% |
| **D — Energia (elettricità + gas + vapore)** | **53,2** | 19% |
| **H — Trasporto e magazzinaggio** | **41,0** | 15% |
| **A — Agricoltura, silvicoltura, pesca** | ~25-30 | ~10% |
| **F — Costruzioni** | ~5-7 | ~2% |
| **G+I+J+K+L+M+N — Servizi** | ~25-30 | ~10% |
| Altri settori | ~10-15 | ~5% |
| **TOTAL industries (NACE A-U)** | **282,7** | 100% |

**Aggiuntivamente famiglie (TOTAL_HH_FD):** ~80 Mt — comprende riscaldamento residenziale e trasporto privato (auto). Totale economy = ~363 Mt (UNFCCC-equivalent).

## Traiettoria storica Italia (Eurostat env_ac_ainah_r2, NACE TOTAL industries, kt CO2eq)

| Anno | kt CO2eq (industries) | Variazione vs 2008 |
|---|---|---|
| 2008 | 461.043 | baseline |
| 2010 | 411.608 | −11% |
| 2015 | 338.745 | −27% |
| 2019 | 321.598 | −30% |
| 2020 | 293.063 | −36% (Covid shock) |
| 2021 | 312.435 | −32% (rimbalzo post-Covid) |
| 2022 | 314.570 | −32% |
| 2023 | 295.943 | −36% |
| **2024** | **282.688 (e)** | **−39%** |

**Industries-only ha visto un calo strutturale del −39% dal 2008.** Ricomprendendo i settori finali (households) il calo totale è in linea con le serie ISPRA UNFCCC (−30% dal 1990, baseline diverso).

## Caveat e note di lettura

- **PIL 2024 italiano €2.192 mld** (ISTAT, marzo 2025, definitivo nominale). +2,9% rispetto al 2023. Eventuali revisioni successive ISTAT da monitorare.
- **L'intensità g CO2eq/€** è sensibile al **tipo di PIL usato**: nominale 2024 vs PIL a prezzi costanti vs PIL PPS (potere d'acquisto). Eurostat e OECD usano convenzioni diverse — verificare sempre la base.
- **Eurostat env_ac_aigg_q quarterly** è il vero indicatore "fresco": già 2025-Q3 disponibile. Per dato annuale consolidato attendere env_ac_ainah_r2 (cycle annuale, con 1 anno di ritardo + revisioni).
- **Confronto UE-27 esige la stessa metrica**: per "pro capite UNFCCC" cross-paese, usare EEA Total GHG dataset (Inventory). Per "pro capite Eurostat residente" usare env_ac_ainah_r2 + tps00001 sample-wise.
- **Confronto Eurostat resident 240 g/€ (2022) vs UNFCCC 167 g/€ (2024)**: non è uno spostamento temporale; è una **differenza metodologica + denominatore PIL**. Per uso politico, **dichiarare sempre la metrica**.

## Sorgente raw

- Emissioni industries Italia 2024: `_raw/energia-ambiente-sostenibilita/EUROSTAT_GHG_INTENSITY/env_ac_ainah_r2_raw.tsv.gz` (riga `A,GHG,TOTAL,THS_T,IT`)
- Quarterly GHG: `_raw/energia-ambiente-sostenibilita/EUROSTAT_GHG_INTENSITY/env_ac_aigg_q_raw.tsv.gz`
- Popolazione: `_raw/energia-ambiente-sostenibilita/EUROSTAT_POPULATION/tps00001_raw.tsv.gz` (riga `A,JAN,IT`)
- Territoriale UNFCCC: `_raw/energia-ambiente-sostenibilita/ISPRA_GHG_INVENTORY/ISPRA_NID_2026_Italy_GHG_1990-2024.pdf`
- EU Climate Action Italy factsheet: `_raw/energia-ambiente-sostenibilita/EU_CLIMATE_ITALY_FACTSHEET/EC_Climate_Italy_factsheet_2023.pdf` (factsheet UE-coordinato)
- Companion: `_raw/energia-ambiente-sostenibilita/OECD_GREEN_GROWTH/DF_GREEN_GROWTH_Italy.csv` (Italian Green Growth Indicators OECD, da filtrare per MEASURE = CO2 intensity, energy productivity, etc.)
