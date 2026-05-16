---
id: prezzi-agricoli-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Prezzi agricoli — output venduti e input acquistati, Italia, 2025"
data_metric: "Indici dei prezzi alla produzione (prodotti venduti dagli agricoltori) e dei prezzi dei mezzi di produzione (prodotti acquistati dagli agricoltori), base 2020=100, mensile"
data_period: "2025-12 (ultimo dato provvisorio); serie mensile 2020-01 / 2025-12"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Indici dei prezzi agricoli, dataflow DCSP_PREZZIAGR_10 (prodotti venduti) e DCSP_PREZZIAGR_9 (prodotti acquistati)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 7a6ce9585b24bab222a395b9c8f2b57179e5f32727160da75482c97100aaed37
tags: [agricoltura]
description: "Indice prezzi prodotti venduti dagli agricoltori 136,2 (Dic 2025, 2020=100) vs indice prezzi prodotti acquistati 127,8 — output +36,2%/input +27,8% nel periodo 2020-2025; ribaltato il cost-price squeeze del 2022."
---

# Prezzi agricoli — output venduti vs input acquistati, Italia, 2025

**Valore (Dic 2025, base 2020=100):**
- **Indice prezzi prodotti venduti dagli agricoltori (TOTAGRICOUT):** **136,2** (provvisorio)
- **Indice prezzi prodotti acquistati dagli agricoltori (INPUTAL):** **127,8** (provvisorio)
- **Terms of trade agricoltura (output/input):** **1,066** (i prezzi di vendita superano i costi di input del ~6,6% rispetto al baseline 2020)

**Variazione cumulata 2020 → Dic 2025:**
- Output: **+36,2%**
- Input: **+27,8%**

## Serie storica — l'intera traiettoria 2020-2025

Punti chiave dell'indice generale:

| Periodo | Output (TOTAGRICOUT) | Input (INPUTAL) | Δ output−input |
|---|---|---|---|
| 2020 media | 100,0 | 100,0 | 0 |
| 2021-12 | 118,7 | 116,0 | +2,7 |
| **2022-10 (picco input)** | 133,6 | **144,8** | **−11,2** ← cost-price squeeze |
| 2022-12 | 134,5 | 143,4 | −8,9 |
| 2023-12 | 136,5 | 128,4 | +8,1 |
| **2024-11 (picco output)** | **143,6** | 126,3 | +17,3 |
| 2025-06 | 141,5 | 126,4 | +15,1 |
| **2025-12** | **136,2** | **127,8** | **+8,4** |

## Le due fasi politicamente cruciali

**Fase 1 — Cost-price squeeze (2022):** durante la crisi energetica i prezzi dei mezzi di produzione (fertilizzanti, mangimi, gasolio agricolo, sementi) sono saliti più rapidamente dei prezzi di vendita. A Ott 2022 l'indice input ha toccato 144,8 (+44,8% vs 2020) mentre l'output era a 133,6: una perdita di margine reale per gli agricoltori, alla base delle proteste UE 2024.

**Fase 2 — Recupero (2023-2025):** la disinflazione energetica ha riportato l'indice input vicino a 126-128 (stabile da inizio 2024), mentre l'output è restato sopra 135. **Il differenziale si è invertito: oggi gli agricoltori vendono a prezzi che superano del +8,4% (sopra 2020) il costo dei propri input.**

## Composizione dell'indice prodotti venduti (TOTAGRICOUT)

L'indice generale aggrega 9 grandi categorie merceologiche. Drill-down disponibili nel raw:

- **CEREA** — Cereali (frumento, mais, riso, orzo)
- **PIANIND** — Piante industriali (girasole, soia, barbabietola)
- **ORTAGI** — Ortaggi
- **FRUTTA** — Frutta
- **VINO** — Vino
- **OLIO** — Olio
- Allevamenti — bovini, suini, ovini, pollame
- **LATTE** — Latte e prodotti lattiero-caseari
- **UOVA** — Uova

## Composizione dell'indice prodotti acquistati (INPUTAL)

L'indice generale include sia i **consumi intermedi** (sementi, fertilizzanti, mangimi, energia, servizi) sia gli **investimenti** (macchinari, costruzioni rurali). Drill-down nel raw:

- **GOODSSERV** — Beni e servizi per consumi intermedi
- **ENRJLUBR** — Energia e lubrificanti (la voce più volatile 2022-2023)
- **FERTNUTR** — Concimi e ammendanti
- **PHYTHEA** — Fitosanitari e prodotti veterinari
- **FEEDST** — Mangimi (la voce maggiore per peso, ~30% del paniere)
- **INVEST** — Investimenti (macchinari, fabbricati)

## Caveat e note di lettura

- **Indici nominali, non reali.** L'indice non è deflazionato per inflazione generale (CPI). Per ricavare la dinamica reale dei prezzi agricoli rispetto al resto dell'economia, va confrontato con [[inflazione-cpi-italia-2025]] (CPI generale Italia Dic 2025 ≈ +18% cumulato vs 2020). **In termini reali, l'output agricolo è cresciuto di ~+15% e l'input di ~+8% sopra l'inflazione generale.**
- **Provvisorio per gli ultimi mesi.** Le ultime 2-3 osservazioni (Ott/Nov/Dic 2025) sono marcate `p` (provvisorio) e possono essere riviste.
- **Indice non equivale a reddito.** Il margine reale dell'agricoltore dipende anche da produzione fisica (rese, eventi meteo), sussidi (CAP), e mix produttivo. La carta misura solo i prezzi unitari medi.
- **L'indice generale nasconde forti differenze settoriali.** Esempio: nel 2023-24 il vino ha visto cali di prezzo (sovrabbondanza), mentre il latte ha guadagnato. Il drill-down per categoria è disponibile nel raw.

## Lettura politica

Il numero che alimenta il dibattito sui sussidi e sulle proteste degli agricoltori è il **gap input-output del 2022 (−11 p.p.)**, non quello attuale (+8 p.p. a favore dell'output). Il messaggio politico-economico aggiornato:

- la stretta sui margini è esistita realmente tra metà 2021 e metà 2023
- dalla seconda metà del 2023 il differenziale si è normalizzato
- le proteste UE 2024 hanno coinciso con la fase di **ricomposizione** del margine, non con il suo deterioramento

Componenti che restano strutturalmente sopra 2020:
- **Mangimi (FEEDST):** ~+25-30% (passaggio strutturale, non riassorbito)
- **Fertilizzanti (FERTNUTR):** alta volatilità, attualmente ~+30%
- **Energia agricola (ENRJLUBR):** picco a +60-80% nel 2022, oggi ~+15-20%

## Sorgente raw

Output venduti: `_raw/agricoltura/DCSP_PREZZIAGR_10/Indice dei prezzi alla produzione dei prodotti venduti dagli agricoltori, mensile (base 2020) (IT1,101_12_DF_DCSP_PREZZIAGR_10,1.0).csv`

Input acquistati: `_raw/agricoltura/DCSP_PREZZIAGR_9/Indice dei prezzi dei prodotti acquistati dagli agricoltori, mensile (base 2020) (IT1,101_12_DF_DCSP_PREZZIAGR_9,1.0).csv`

Dataset: ISTAT `DCSP_PREZZIAGR_10` (1.585 righe, prodotti venduti, base 2020=100) + ISTAT `DCSP_PREZZIAGR_9` (2.377 righe, prodotti acquistati, base 2020=100). Mensile, Italia, 2020-01 / 2025-12.
