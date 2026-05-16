---
id: spesa-pubblica-istruzione-italia-2022
type: data
attribution: oecd
quality_tier: D1
title: "Spesa pubblica e totale per istruzione, Italia, 2022"
data_metric: "Spesa per istituzioni educative (ISCED 1-8) come % del PIL — distribuita tra fonte pubblica (S13), privata domestica (S1D_NON_EDU) e non-domestica (S2). Framework OECD-UOE"
data_period: "2022; serie 2015-2022"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Education at a Glance, dataflow DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM"
date_published: "2025"
date_scraped: "2026-05-12"
content_hash: fd4e78a65006ad5da3bdb1ff82c6e351893133598901e5a32278671eb06d627a
tags: [istruzione, spesa-pubblica]
description: "Spesa per istruzione Italia 2022: totale 3,87% PIL (-0,8 p.p. vs OCSE 4,70%), pubblica 3,33% PIL (-0,6 p.p. vs OCSE 3,96%). Italia strutturalmente sotto-investe nell'istruzione."
---

# Spesa per istruzione, Italia, 2022

## Headline

| Indicatore (2022, ISCED 1-8) | 🇮🇹 Italia (% PIL) | 🌐 OCSE (% PIL) | Gap |
|---|---|---|---|
| **Spesa totale per istruzione** | **3,87%** | **4,70%** | **−0,83 p.p.** |
| Di cui pubblica (governo) | 3,33% | 3,96% | −0,63 p.p. |
| Di cui privata domestica | 0,49% | (n/d singolarmente) | — |
| Di cui non-domestica (UE+altri) | 0,05% | (n/d singolarmente) | — |

**L'Italia spende meno della media OCSE per istruzione di circa 0,8 punti di PIL** — tradotto in euro 2022 (PIL Italia ~2.000 mld), il gap è di **~17 miliardi di euro l'anno**.

## Serie storica Italia 2015-2022 (% PIL)

| Anno | Spesa totale | Pubblica (S13) | Privata domestica | Estera (S2) |
|---|---|---|---|---|
| 2015 | 3,91 | 3,33 | 0,48 | 0,10 |
| 2016 | 3,60 | 3,11 | 0,45 | 0,04 |
| 2017 | 3,83 | 3,31 | 0,47 | 0,05 |
| 2018 | 4,08 | 3,47 | 0,57 | 0,04 |
| 2019 | 3,83 | 3,30 | 0,51 | 0,02 |
| **2020** | **4,16** | **3,62** | 0,51 | 0,03 | ← picco Covid |
| 2021 | 4,00 | 3,42 | 0,51 | 0,07 |
| **2022** | **3,87** | **3,33** | 0,49 | 0,05 |

**Pattern:** la spesa italiana è cresciuta nel 2020-2021 con il PNRR Covid (e ulteriori finanziamenti emergenziali), poi è tornata sui livelli pre-pandemia 2022. **Italia non ha avuto un'espansione strutturale della spesa per istruzione nell'ultimo decennio.**

## Spesa pubblica in valore assoluto (USD PPP costanti 2020)

| Anno | Spesa pubblica per istruzione (mln USD PPP) |
|---|---|
| 2015 | 92.600 |
| 2018 | 100.214 |
| 2020 | 95.494 |
| **2022** | **100.291** |

In termini reali la spesa pubblica italiana per istruzione è cresciuta di circa **+8% reale tra 2015 e 2022** — sotto la crescita reale del PIL nello stesso periodo, da cui il **declino della quota sul PIL**.

## Confronto con altri capitoli di spesa pubblica italiana

L'Italia 2022 ha speso:
- **3,33% PIL su istruzione** (questo dato, OECD UOE).
- ~8,85% PIL su **sanità** totale (di cui ~6,6% pubblica) — vedi [[spesa-sanitaria-pil-italia-2024]].
- ~16-17% PIL su **pensioni** (orientativo, da verificare con web search).
- ~3-4% PIL su **interessi sul debito**.

L'istruzione è **uno dei capitoli pubblici più piccoli** del bilancio italiano in % di PIL — sotto sanità, pensioni, interessi.

## Composizione fonti — Italia vs OCSE

**Italia 2022:**
- Pubblica (S13): **86%** del totale spesa istruzione (3,33 / 3,87).
- Privata domestica: **13%**.
- Non-domestica (UE, altri): **1%**.

L'Italia ha un sistema di istruzione **prevalentemente finanziato dallo Stato** (~86% pubblico). La quota privata domestica (rette + materiale + scuole paritarie) è ~13%, leggermente sopra la media OCSE.

## Metodologia

Framework: **OECD-UOE (UNESCO/OECD/Eurostat) Joint Questionnaire** — Distribution of expenditure on educational institutions by source. Dataflow `DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM`, release 2025 (data 2015-2022).

- **Cosa è incluso:** spesa per istituzioni educative formali ISCED 1-8 (primaria → dottorato). Esclude early childhood (ISCED 0) in questa vista filtrata su ISCED 1-8.
- **EXP_SOURCE codes:**
  - `S13` = General Government (stato, regioni, EE.LL.).
  - `S1D_NON_EDU` = Private domestic non-education (famiglie + imprese italiane, esclude transfer governativi).
  - `S2` = Rest of the world (finanziamenti esteri, UE compresa).
  - `_T` = Total (somma dei tre).
- **EXPENDITURE_TYPE:** DIR_EXP (direct expenditure) — pagamenti diretti, esclude trasferimenti a istituzioni che poi pagano studenti.
- **UNIT_MEASURE:**
  - `PT_B1GQ` = % del PIL (più stabile per confronti internazionali).
  - `USD_PPP` = milioni USD PPP costanti base 2020 (per livello assoluto).
- **PRICE_BASE:** costant prices 2020 base (corretto per inflazione).

## Caveat e note di lettura

- **Confronto col dato MEF italiano.** Il MEF (DEF, Bilancio dello Stato) pubblica spesa pubblica per istruzione con perimetro leggermente diverso (include anche istruzione informale, fondi a famiglie, alcuni capitoli MIM-non-formazione). Il dato OECD è ~3,3% PIL; il dato MEF "spesa pubblica per istruzione" è solitamente ~4,0-4,2% PIL — la differenza include trasferimenti diretti alle famiglie e attività non-istituzionali.
- **Il dato 2022 può essere rivisto.** Pubblicazioni OECD successive (EAG 2026) potrebbero aggiornare la cifra. Confermare con web search per la release più recente.
- **PT_B1GQ può oscillare per effetto denominatore.** Se il PIL nominale cresce molto velocemente (come in 2021-2022 con inflazione 8%), la quota dell'istruzione SCENDE meccanicamente anche a spesa nominale invariata. L'effetto è visibile 2021→2022 (-0,13 p.p.) ma in parte è inflazione, non taglio reale.
- **Sotto-utilizzo PNRR Missione 4.** Il PNRR italiano ha allocato **30 mld in 6 anni per istruzione + ricerca**, ma l'esecuzione effettiva 2021-2024 è stata sotto le attese. La quota istruzione % PIL del 2022 (3,87% totale) non riflette ancora il pieno effetto PNRR (in corso).

## ORA — perché la cifra è politicamente rilevante

Il **gap di ~17 mld** Italia vs OCSE nella spesa istruzione è cifra centrale nel dibattito su:
- **Aumento salari docenti** — Italia paga **-11/-13% sotto media OCSE 2024** sul salario medio degli insegnanti K-12 (vedi [[salari-docenti-italia-2024]]). Il gap si è ridotto dal -25/-30% di metà 2010s dopo CCNL 2019-21 + supplementi 2023-24, ma resta significativo, soprattutto su entry-level e top-of-scale dove l'Italia è ancora -20/-25% sotto OCSE.
- **Edilizia scolastica** (~30 mld di fabbisogno stimato, mai pienamente finanziato).
- **Sotto-investimento terziaria** — coerente con [[spesa-per-studente-italia-2022]] che mostra spesa per studente -30% sotto OCSE in terziaria.
- **PNRR Missione 4** — la grande scommessa decennale per chiudere parzialmente il gap.

## Sorgente raw

`_raw/istruzione/DF_UOE_FIN_SOURCE_GV_PR_NDOM/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM,3.1+..ISCED11_1T8._T+S13+S1D_NON_EDU+S2.INST_EDU..Q+_Z.USD_PPP+PT_EXP+PT_B1GQ..csv`

Dataflow OECD `DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM(3.1)` — 4279 righe, 88 righe Italia (8 anni × 4 fonti × 2-3 unità di misura). Serie 2015-2022.
