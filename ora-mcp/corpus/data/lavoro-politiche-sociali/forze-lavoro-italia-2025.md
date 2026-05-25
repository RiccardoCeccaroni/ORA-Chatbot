---
id: forze-lavoro-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Forze di lavoro totali, Italia, 15 anni e oltre, 2025"
data_metric: "forze di lavoro 15+ (numero in migliaia)"
data_period: "2025 (annuale, provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Rilevazione sulle Forze di Lavoro (RFL), dataflow DCCV_FORZLV1 (150_908)"
date_published: "2026"
date_scraped: "2026-05-11"
content_hash: 35aa1d1673f0fc4e8d11fddaf355b7fbce2cc9532d14f88fa5fa67eb15ed58c3
tags: [lavoro-politiche-sociali]
description: "Forze di lavoro totali 15+ in Italia (in migliaia), dato annuo 2025 (provvisorio), con serie trimestrale e ripartizione per classe di età."
---

# Forze di lavoro totali, Italia, 15 anni e oltre, 2025

**Valore (2025, annuale provvisorio):** **25,69 milioni** (25.693 mila forze di lavoro 15+).
**Variazione su 2024 (25,60 mln):** **+97 mila (+0,4%)**
**Ultimo dato trimestrale (2025-Q4):** 25,47 mln

Forze di lavoro = occupati + disoccupati. Per il 2025: **24.117 + 1.576 = 25.693 mila** ✓.

## Serie trimestrale recente (15+, dati destagionalizzati)

| Trimestre | Forze di lavoro (mln) |
|---|---|
| 2023-Q4 | 25,75 |
| 2024-Q1 | 25,62 |
| 2024-Q2 | 25,69 |
| 2024-Q3 | 25,56 |
| 2024-Q4 | 25,52 |
| 2025-Q1 | 25,83 |
| 2025-Q2 | 25,90 |
| 2025-Q3 | 25,56 |
| 2025-Q4 | 25,47 |

## Ripartizione per classe di età (2025 annuale)

| Fascia | Forze di lavoro (mila) |
|---|---|
| 15-24 anni | 1.321 |
| 15-29 anni | 3.415 |
| 25-34 anni | 4.650 |
| 35-44 anni | 5.684 |
| 45-54 anni | 7.343 |
| 55-64 anni | 5.814 |
| **15-64 anni** | **24.812** |
| 65 anni e più (Y65-89) | 881 |
| **15+ (Y15-89, headline)** | **25.693** |

## Metodologia

Fonte: **Rilevazione sulle Forze di Lavoro (RFL)** — ISTAT.
Definizione armonizzata Eurostat/ILO: forze di lavoro = occupati + persone in cerca di occupazione (NON include inattivi e studenti che non cercano lavoro).
Dataflow: `DCCV_FORZLV1` (ID 150_908).

**Dati 2025 provvisori**, soggetti a revisione.

## Caveat e note di lettura

- Le forze di lavoro in Italia restano **basse rispetto al potenziale demografico**: ~25,7 mln su una popolazione 15+ di ~50,7 mln, ossia un **tasso di attività ~50,6%**. La gran parte della distanza vs gli altri paesi UE-27 si gioca qui (Italia ha ~13 pp di tasso di attività femminile in meno della media UE-27 + alta presenza di NEET).
- La **crescita 2024→2025 è modesta (+97 mila, +0,4%)**, e composta interamente dalla fascia 55+ (+380 mila) che compensa il calo strutturale delle fasce più giovani per via della demografia (-282 mila in 15-54).
- **Inattivi non inclusi**: studenti che non lavorano, casalinghe, scoraggiati, pensionati non attivi. Il tasso di inattività 15-64 in Italia (~33-34%) è tra i più alti d'Europa.
- Per la **composizione delle forze di lavoro per condizione lavorativa europea** (occupato / disoccupato / inattivo / studente attivo), vedere il dataflow `DCCV_POPCOND1` (in batch, non ancora in card dedicata).

## Indicatori complementari

- Occupati 15+ (2025): 24,12 milioni → `occupati-totali-italia-2025.md`
- Disoccupati 15-74 (2025): 1,58 milioni → `disoccupati-italia-2025.md`
- Tasso di occupazione 15-64 (2025): 62,5% → `tasso-occupazione-italia-15-64-2025.md`
- Tasso di disoccupazione 15-64 (2025): 6,3% → `tasso-disoccupazione-italia-2025.md`

## Sorgente raw

`_raw/istat/DCCV_FORZLV1/Classe di età (IT1,150_908_DF_DCCV_FORZLV1_1,1.0).csv`
