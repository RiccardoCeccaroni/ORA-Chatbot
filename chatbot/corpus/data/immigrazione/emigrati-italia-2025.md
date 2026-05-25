---
id: emigrati-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Emigrati dall'Italia, 2025 (dato provvisorio)"
data_metric: "cancellazioni anagrafiche per l'estero (emigrazioni)"
data_period: "2025 (annuale, dato provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,POP,1.0/IT1.POP_MIGR/IT1_28_185"
source_doc: "ISTAT — Movimento migratorio della popolazione residente, dataflow DCIS_MIGRAZIONI (28_185)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 52dfbe20d74d68a0712b9cbe7747202551c033b06910d87a3dc255434853b604
tags: [immigrazione, lavoro-politiche-sociali]
description: "Cancellazioni anagrafiche per l'estero nel 2025 (dato provvisorio): 144.157 totali, di cui 109.004 cittadini italiani (76%). Destinazione UE 52% degli italiani; principali: Spagna, Germania, Svizzera, UK, Francia."
---

# Emigrati dall'Italia, 2025 (dato provvisorio)

**Cancellazioni anagrafiche per l'estero, totale 2025:** **144.157**
- di cui **cittadini italiani**: **109.004** (~76%)
- di cui **stranieri**: **35.153** (~24%)

**Saldo migratorio con l'estero 2025 (provv.):** ≈ **+295.759** (440k iscritti – 144k cancellati)

## Top 10 cittadinanze degli emigrati (2025)

| Cittadinanza | Cancellati |
|---|---|
| Italia | 109.004 |
| Romania | 9.346 |
| Ucraina | 3.981 |
| Albania | 1.434 |
| Cina | 1.192 |
| India | 1.141 |
| Marocco | 1.026 |
| Polonia | 906 |
| Germania | 896 |
| Moldova | 888 |

## Top 10 paesi di destinazione (totale, 2025)

| Destinazione | Emigrati |
|---|---|
| Germania | 14.583 |
| Spagna | 14.357 |
| Svizzera | 12.736 |
| Regno Unito | 12.077 |
| Francia | 10.632 |
| Romania | 8.385 |
| (aggregati: UE-27 totale = 72.751; Extra-UE = 35.197) | |

## Top destinazioni dei soli cittadini italiani (2025)

| Destinazione | Italiani |
|---|---|
| Spagna | 13.270 |
| Germania | 12.501 |
| Svizzera | 12.001 |
| Regno Unito | 11.184 |
| Francia | 9.354 |
| Stati Uniti d'America | 6.280 |
| (aggregati: UE-27 = 56.572; Extra-UE = 25.729; America = 16.170) | |

## Lettura politica

### "Fuga di cervelli" — il numero che pesa
**109.004 cittadini italiani hanno cancellato la residenza in Italia nel 2025.** Il 76% degli emigrati totali sono italiani — non stranieri che tornano nel paese d'origine.

Quota italiani che vanno **in altri paesi UE: 52%** (56.572 / 109.004). Il "fuga in UE" è il fenomeno dominante: lavoratori e studenti che si stabiliscono in Spagna, Germania, Svizzera, UK, Francia.

### Confronto con immigrazione
- Iscritti dall'estero 2025: **439.916**
- Cancellati per l'estero 2025: **144.157**
- **Saldo netto migratorio: +295.759**

L'Italia è ancora un paese a saldo migratorio positivo significativo — l'immigrazione compensa più che ampiamente l'emigrazione.

### Ma il bilancio "qualitativo" è asimmetrico
Gli emigrati sono **italiani al 76%** (spesso giovani laureati che lasciano per opportunità all'estero) — gli iscritti sono **stranieri all'87%** (per ricongiungimento familiare, lavoro, ecc., vedi card `inflows-permanenti-categoria-italia-2024.md`).

**Il saldo numerico nasconde uno scambio strutturale:**
- escono italiani 25-44 anni con istruzione terziaria (proxy: brain drain)
- entrano stranieri di diverse provenienze e profili educativi

Questa asimmetria è il cuore del dibattito sulla **competitività del mercato del lavoro italiano** e sulla **demografia** (vedi card OECD su inflows + occupazione stranieri).

## Metodologia

Fonte: **Movimento migratorio della popolazione residente**, ISTAT — dataflow `DCIS_MIGRAZIONI` (28_185).
Definizione: cancellazioni di residenza per l'estero registrate nelle anagrafi comunali (variabile `CHANGE_OF_RESIDENCE = FREIGN` per "Cancellazioni per l'estero", `DATA_TYPE = TDEREG`).
Universo: tutte le persone (indipendentemente da cittadinanza, sesso, età).

**Dati 2025 provvisori** (variabile `OBS_STATUS = p`).

## Caveat e note di lettura

- Il dato **sottostima l'emigrazione reale italiana** in modo noto:
  - Molti italiani all'estero **non si cancellano dall'anagrafe** (per mantenere SSN, servizi, residenza familiare). L'AIRE (Anagrafe Italiani Residenti all'Estero) cattura solo una parte.
  - Le stime dei consolati/AIRE indicano numeri reali sostanzialmente più alti (~150-180k italiani che lasciano l'Italia ogni anno).
- **Definizione di "emigrato"** = chi si cancella in anagrafe, non chi vive di fatto all'estero.
- Il **bilancio numerico positivo** (+295k) NON significa che l'Italia "guadagna" demograficamente: dipende dalla composizione (età, istruzione, durata della permanenza degli immigrati).
- Per la **serie storica** dell'emigrazione italiana questa view è solo 2025 — re-export con TIME_PERIOD esteso richiesto per analisi di trend.

## Sorgente raw

- `_raw/immigrazione/DCIS_MIGRAZIONI/Emigrati - cittadinanza (IT1,28_185_DF_DCIS_MIGRAZIONI_5,1.0).csv` — breakdown per cittadinanza
- `_raw/immigrazione/DCIS_MIGRAZIONI/Emigrati - paesi di destinazione (IT1,28_185_DF_DCIS_MIGRAZIONI_6,1.0).csv` — breakdown per paese di destinazione
