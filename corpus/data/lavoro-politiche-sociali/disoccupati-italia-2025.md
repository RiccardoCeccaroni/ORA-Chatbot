---
id: disoccupati-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Persone in cerca di occupazione, Italia, 2025"
data_metric: "disoccupati 15+ anni (numero in migliaia)"
data_period: "2025 (annuale, provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Rilevazione sulle Forze di Lavoro (RFL), dataflow DCCV_DISOCCUPT1 (151_929)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: a1f0ee08f19ba0da5116aad353611312ef340f6c9dac83827bf5aaec791e21ee
tags: [lavoro-politiche-sociali]
description: "Numero di persone in cerca di occupazione 15+ in Italia (in migliaia), dato annuo 2025 (provvisorio), con serie trimestrale e ripartizione per classe di età."
---

# Persone in cerca di occupazione, Italia, 2025

**Valore (2025, annuale provvisorio):** **1,58 milioni** (1.576 mila persone in cerca di occupazione 15-74).
**Variazione su 2024 (1,66 mln):** **−88 mila (−5,3%)**
**Ultimo dato trimestrale (2025-Q4):** 1,40 mln (15-74)

## Serie trimestrale recente (15-74, dati destagionalizzati)

| Trimestre | Disoccupati (mila) |
|---|---|
| 2023-Q4 | 1.938 |
| 2024-Q1 | 1.974 |
| 2024-Q2 | 1.710 |
| 2024-Q3 | 1.428 |
| 2024-Q4 | 1.541 |
| 2025-Q1 | 1.758 |
| 2025-Q2 | 1.701 |
| 2025-Q3 | 1.440 |
| 2025-Q4 | 1.403 |

## Ripartizione per classe di età (2025 annuale)

| Fascia | Disoccupati (mila) |
|---|---|
| 15-24 anni | 272 |
| 15-29 anni | 491 |
| 25-34 anni | 418 |
| 35-44 anni | 331 |
| 45-54 anni | 333 |
| 55-64 anni | 206 |
| **15-64 anni** | **1.561** |
| 65-74 anni | 15 |
| **15-74 anni (headline)** | **1.576** |

## Metodologia

Fonte: **Rilevazione sulle Forze di Lavoro (RFL)** — ISTAT.
Definizione armonizzata Eurostat/ILO: persona in cerca di occupazione = 15+ non occupata che (a) ha cercato lavoro attivamente nelle ultime 4 settimane e (b) è disponibile a lavorare entro 2 settimane. ISTAT misura fino ai 74 anni (oltre, i numeri sono insignificanti).
Dataflow: `DCCV_DISOCCUPT1` (ID 151_929).

**Dati 2025 provvisori**, soggetti a revisione.

## Caveat e note di lettura

- Il **calo del numero di disoccupati (-88 mila YoY) è coerente con il calo del tasso** (vedere `tasso-disoccupazione-italia-2025.md`).
- Una parte del calo va però letta alla luce di una **possibile uscita dalle forze di lavoro** (scoraggiamento, pensionamento anticipato, etc.), non solo di nuovi ingressi nell'occupazione. Per separare i due effetti serve incrociare con la popolazione per condizione (`DCCV_POPCOND1`, non ancora in card dedicata).
- **L'oscillazione trimestrale è marcata**: i disoccupati si concentrano in T1 (gennaio-marzo, dopo il periodo natalizio) e calano in T3 (estate). Il dato annuale livella questa stagionalità.
- I **disoccupati di lunga durata** (in cerca da >12 mesi) — circa il 50% del totale in Italia — non sono isolati in questa view; serve un dataflow specifico.
- **Differenza vs definizione amministrativa:** ISTAT (LFS) ≠ disoccupati amministrativi (iscritti CPI / percettori NASPI). I numeri possono divergere di 1-2 milioni.

## Indicatori complementari

- Tasso di disoccupazione 15-64 (2025): 6,3% → `tasso-disoccupazione-italia-2025.md`
- Forze di lavoro 15+ (2025): 25,69 milioni → `forze-lavoro-italia-2025.md`
- Occupati 15+ (2025): 24,12 milioni → `occupati-totali-italia-2025.md`

## Sorgente raw

`_raw/istat/DCCV_DISOCCUPT1/Classe di età (IT1,151_929_DF_DCCV_DISOCCUPT1_1,1.0).csv`
