---
id: immigrati-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Immigrati in Italia, 2025 (dato provvisorio)"
data_metric: "iscrizioni anagrafiche dall'estero (immigrazioni)"
data_period: "2025 (annuale, dato provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,POP,1.0/IT1.POP_MIGR/IT1_28_185"
source_doc: "ISTAT — Movimento migratorio della popolazione residente, dataflow DCIS_MIGRAZIONI (28_185)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: de3bd477c29f6d2a5f1dca4a9092f7c0d0606a570bd138a8ecde3f6ef778c59c
tags: [immigrazione]
description: "Iscritti in anagrafe dall'estero in Italia nel 2025 (dato provvisorio): 439.916 totali, di cui ~56.000 italiani di ritorno e ~384.000 stranieri. Origini principali: Bangladesh, Marocco, Albania, Pakistan, Egitto."
---

# Immigrati in Italia, 2025 (dato provvisorio)

**Iscritti in anagrafe dall'estero, totale 2025:** **439.916**
- di cui **italiani di ritorno** (cittadinanza IT): **56.451** (~13%)
- di cui **stranieri** (tutte le cittadinanze non-IT): **~383.465** (~87%)

## Ripartizione per continente di cittadinanza (2025)

| Continente | Iscritti | Quota |
|---|---|---|
| Europa (incl. UE e non-UE) | 153.863 | 35,0% |
| Asia | 116.180 | 26,4% |
| Africa | 110.110 | 25,0% |
| America | 59.143 | 13,4% |
| Oceania + apolidi | residuale | <1% |

## Top 10 cittadinanze degli iscritti dall'estero (2025)

| Cittadinanza | Iscritti |
|---|---|
| Italia (italiani di ritorno) | 56.451 |
| Bangladesh | 37.454 |
| Marocco | 36.192 |
| Albania | 26.832 |
| Pakistan | 25.613 |
| Egitto | 22.610 |
| Romania | 18.810 |
| Perù | 18.650 |
| Tunisia | 17.068 |
| India | 16.899 |

## Top 10 paesi di provenienza (geografia di partenza, indipendente dalla cittadinanza, 2025)

| Paese | Iscritti |
|---|---|
| Bangladesh | 37.494 |
| Marocco | 36.425 |
| Albania | 26.958 |
| Pakistan | 25.600 |
| Egitto | 22.857 |
| Romania (e altri UE) | aggregato in continente |
| Perù | ~18.000 |
| Tunisia | ~17.000 |
| India | ~17.000 |
| Cina | ~14.000 |

## Lettura politica

### "Quanti immigrati arrivano in Italia ogni anno?"
**~440.000 iscrizioni dall'estero nel 2025**, di cui:
- **87%** sono stranieri (~383k)
- **13%** sono italiani di ritorno (56k)

Il dato di flusso non è lo stock dei residenti stranieri (~5,3 milioni, ~9% della popolazione — non in questo card, vedi gap residuo).

### Composizione delle origini
- **Asia + Africa = 51%** dei flussi (Bangladesh, Marocco, Pakistan, Egitto, India, Tunisia, Cina sono nella top 10)
- **Europa = 35%** (UE + extra-UE: Albania, Romania, Ucraina)
- **America = 13%** (Perù, Brasile, Venezuela, Ecuador prevalentemente)

### Cosa NON è in questi numeri
- ⚠️ **Non sono "sbarchi"**. I dati ISTAT registrano chi si iscrive in anagrafe — quindi gente che ha un permesso di soggiorno o cittadinanza UE. Gli sbarchi (Cruscotto statistico Ministero dell'Interno) sono un fenomeno separato, ~67.000 nel 2024 (gap residuo, non in questo card).
- ⚠️ **Non è lo stock di stranieri**. Sono iscrizioni nuove dell'anno. Per "quanti stranieri vivono in Italia" → gap residuo (DCIS_POPSTRRES).
- ⚠️ **Sottostima dell'irregolare**. Chi non si iscrive in anagrafe non appare nei flussi ufficiali.

## Metodologia

Fonte: **Movimento migratorio della popolazione residente**, ISTAT — dataflow `DCIS_MIGRAZIONI` (28_185).
Definizione: trasferimenti di residenza dall'estero registrati nelle anagrafi comunali (variabile `CHANGE_OF_RESIDENCE = FREIGN` per "Iscrizioni dall'estero").
Universo: tutte le persone (indipendentemente da cittadinanza, sesso, età).

**Dati 2025 provvisori**, soggetti a revisione (variabile `OBS_STATUS = p`).

## Caveat e note di lettura

- Il **dato 2025 è provvisorio**. La versione definitiva tipicamente arriva con il Rapporto Annuale ISTAT dell'anno successivo.
- I numeri sono **flussi anagrafici**, non flussi reali totali di immigrazione. Sotto-stimano: irregolari, residenti non iscritti, lavoratori stagionali sotto soglia di iscrizione.
- **"Italiani di ritorno" (56k)** include nuovi cittadini italiani (per acquisizione cittadinanza) che si registrano dall'estero — non solo italiani nati IT che ritornano.
- Per la **serie storica** (trend pluriennale), questa view è solo 2025 — vedi card complementare `inflows-foreign-population-italia-2012-2023.md` (OECD, serie 2012-2023, definizione armonizzata).

## Sorgente raw

- `_raw/immigrazione/DCIS_MIGRAZIONI/Immigrati - cittadinanza (IT1,28_185_DF_DCIS_MIGRAZIONI_2,1.0).csv` — breakdown per cittadinanza
- `_raw/immigrazione/DCIS_MIGRAZIONI/Immigrati - paesi di provenienza (IT1,28_185_DF_DCIS_MIGRAZIONI_3,1.0).csv` — breakdown per paese di precedente residenza
