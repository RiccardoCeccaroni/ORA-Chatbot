---
id: retribuzione-mediana-oraria-privati-italia-2023
type: data
attribution: istat
quality_tier: D1
title: "Retribuzione lorda oraria mediana, dipendenti del settore privato, Italia, 2023"
data_metric: "retribuzione lorda oraria mediana"
data_period: "2023 (annuale)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500LAB,1.0"
source_doc: "ISTAT — Retribuzioni annuali complessive dei lavoratori dipendenti (dataflow DCSC_RACLI, 533_957)"
date_published: "2025"
date_scraped: "2026-05-11"
content_hash: db584bf9b1aa8cb3111a824a16350056fc818bce48a5a144a16c2b6789d4aabb
tags: [lavoro-politiche-sociali, pari-opportunita-inclusione]
description: "Mediana della retribuzione lorda oraria delle posizioni lavorative dipendenti del settore privato in Italia, 2023, con ripartizione per sesso, età e qualifica contrattuale."
---

# Retribuzione lorda oraria mediana, dipendenti privati, Italia, 2023

**Valore (totale, 2023):** **€11,98 / ora**
**Per sesso:** Maschi **€12,42** / Femmine **€11,42** → **gap di genere ~ €1,00 / ora (-8,1% per le donne sulla mediana)**

## Ripartizione per sesso e qualifica contrattuale (2023, totale fasce d'età)

| Qualifica | Maschi (€/ora) | Femmine (€/ora) | Totale (€/ora) | Gap M-F (€) |
|---|---|---|---|---|
| Dirigente; impiegato | 18,06 | 13,34 | **14,95** | 4,72 |
| Operaio | 11,76 | 10,50 | **11,27** | 1,26 |
| Apprendista | 9,49 | 9,23 | **9,39** | 0,26 |
| **Totale qualifiche** | **12,42** | **11,42** | **11,98** | **1,00** |

## Ripartizione per età (2023, totale qualifiche e sessi)

| Fascia d'età | Mediana €/ora |
|---|---|
| 15-29 anni | 10,70 |
| 30-49 anni | 12,24 |
| 50 anni e più | 13,08 |
| **Totale** | **11,98** |

## Metodologia

Fonte: **ISTAT — Retribuzione annuale complessiva dei lavoratori dipendenti** (dataflow `DCSC_RACLI`, 533_957).

Definizione: *"Valore mediano della distribuzione della retribuzione oraria della singola posizione lavorativa dipendente delle imprese, ottenuto come rapporto fra la retribuzione lorda imponibile a fini contributivi a carico del datore di lavoro e le ore retribuite stimate sempre a carico del datore di lavoro."*

- **Misura:** mediana (50° percentile), NON media. La mediana è meno sensibile agli outlier salariali alti (es. dirigenti con compensi elevati).
- **Universo:** posizioni lavorative dipendenti del **settore privato**. Esclude lavoratori autonomi, collaboratori, e dipendenti pubblici.
- **Unità di misura:** euro lordi per ora retribuita (imponibile contributivo).

## Caveat e note di lettura

- Il dato è di **2 anni fa** (riferimento 2023, ultima annualità disponibile nel dataflow al momento del prelievo). Le retribuzioni nominali italiane sono cresciute fra 2023 e 2025 — vedere gli indici contrattuali (`DCSC_RETRCONTR1C`) per il trend di breve termine.
- La categoria "**Dirigente; impiegato**" è aggregata in un'unica voce nel codelist ISTAT: la grossa differenza fra dirigenti (retribuzioni alte) e impiegati (retribuzioni medie) **non è isolata** in questa view. Il valore mediano combinato (€14,95) approssima più l'impiegato medio che il dirigente, dato che gli impiegati sono molti più numerosi.
- Il **gap di genere mediano** (~8% sulla retribuzione oraria) è **sostanzialmente minore** del gap di reddito complessivo (~20-25%, fonte Eurostat per il "gender overall earnings gap"). Le differenze sono spiegate da: meno ore lavorate dalle donne, minore partecipazione, segregazione settoriale, minore presenza in ruoli dirigenziali — fattori che pesano sul reddito annuo ma NON sulla retribuzione oraria comparabile a parità di qualifica.
- Gli **apprendisti** mostrano retribuzioni più basse (€9,39/ora mediana) coerentemente con la natura formativa del contratto e l'età più giovane dei lavoratori.
- **Non disponibile in questa view:** disaggregazione per ATECO (settore economico), classe dimensionale d'impresa, ripartizione territoriale Nord/Centro/Sud. Sono presenti in altri view dello stesso dataflow (cittadinanza, titolo di studio — non utilizzati per questo card).

## Sorgente raw

`_raw/istat/DCSC_RACLI/Classe di età (IT1,533_957_DF_DCSC_RACLI_1,1.0).csv`
