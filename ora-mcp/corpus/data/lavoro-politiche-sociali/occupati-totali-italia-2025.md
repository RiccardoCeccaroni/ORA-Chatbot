---
id: occupati-totali-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Numero di occupati totali, Italia, 15 anni e oltre, 2025"
data_metric: "occupati 15+ anni (numero in migliaia)"
data_period: "2025 (annuale, provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Rilevazione sulle Forze di Lavoro (RFL), dataflow DCCV_OCCUPATIT1 (150_938)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: c6b142fca1a5da3788bd2df85cb509ba39c27ab52966299539c1947e45471f53
tags: [lavoro-politiche-sociali]
description: "Numero di occupati 15+ in Italia (in migliaia), dato annuo 2025 (provvisorio), con serie trimestrale e ripartizione per classe di età."
---

# Numero di occupati totali, Italia, 15 anni e oltre, 2025

**Valore (2025, annuale provvisorio):** **24,12 milioni** di occupati (24.117 mila).
**Variazione su 2024 (23,93 mln):** **+185 mila (+0,8%)**
**Ultimo dato trimestrale (2025-Q4):** 24,07 mln

## Serie trimestrale recente (15+, dati destagionalizzati)

| Trimestre | Occupati (mln) |
|---|---|
| 2023-Q4 | 23,81 |
| 2024-Q1 | 23,64 |
| 2024-Q2 | 23,98 |
| 2024-Q3 | 24,13 |
| 2024-Q4 | 23,98 |
| 2025-Q1 | 24,08 |
| 2025-Q2 | 24,20 |
| 2025-Q3 | 24,12 |
| 2025-Q4 | 24,07 |

## Ripartizione per classe di età (2025 annuale)

| Fascia | Occupati (mila) |
|---|---|
| 15-24 anni | 1.049 |
| 15-29 anni | 2.924 |
| 25-34 anni | 4.232 |
| 35-44 anni | 5.352 |
| 45-54 anni | 7.010 |
| 55-64 anni | 5.607 |
| **15-64 anni** | **23.251** |
| 65 anni e più (Y65-89) | 866 |
| **15 anni e più (Y15-89, headline)** | **24.117** |

## Metodologia

Fonte: **Rilevazione sulle Forze di Lavoro (RFL)** — ISTAT.
Definizione armonizzata Eurostat/ILO: occupato = persona 15+ che ha lavorato almeno un'ora retribuita nella settimana di riferimento (o assente per ferie/malattia/maternità).
Dataflow: `DCCV_OCCUPATIT1` (ID 150_938).

**Dati 2025 provvisori**, soggetti a revisione nel prossimo Rapporto Annuale ISTAT.

## Caveat e note di lettura

- Il numero in valore assoluto va sempre letto **insieme alla popolazione di riferimento**: i 24,12 mln di occupati sono su una popolazione 15+ di circa 50,7 mln (tasso di occupazione 15+ ≈ 47,6%). La cifra del tasso (vedere card relativa) è quella usata nei confronti internazionali.
- **Il numero di occupati continua a crescere nonostante il calo demografico** — fenomeno trainato dalla fascia 55-64 (+280 mila su 2024) e dagli over-65 ancora attivi (+84 mila). Le fasce sotto i 55 anni mostrano variazioni negative o stabili in valore assoluto.
- La **crescita 2024→2025 di +185 mila** va vista nel contesto di un'inflazione bassa, una forza lavoro in lieve aumento e un tasso di disoccupazione in calo: il mercato del lavoro italiano è in fase di assorbimento.
- **Non incluso in questa view:** occupati per settore (industria/servizi/agricoltura), tipologia contrattuale (tempo indeterminato/determinato), part-time/full-time, dipendenti/autonomi. Sono accessibili in altri dataflow ISTAT non in questo batch.

## Indicatori complementari

- Tasso di occupazione 15-64 (2025): 62,5% → `tasso-occupazione-italia-15-64-2025.md`
- Forze di lavoro 15+ (2025): 25,69 milioni → `forze-lavoro-italia-2025.md`
- Disoccupati totali (2025): 1,58 milioni → `disoccupati-italia-2025.md`

## Sorgente raw

`_raw/istat/DCCV_OCCUPATIT1/Occupati  (migliaia) - Classe di età (IT1,150_938_DF_DCCV_OCCUPATIT1_1,1.0).csv`
