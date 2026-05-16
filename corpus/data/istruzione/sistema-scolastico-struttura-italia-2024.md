---
id: sistema-scolastico-struttura-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Sistema scolastico italiano — struttura e dimensioni, 2024"
data_metric: "Conteggi strutturali del sistema scolastico K-12 italiano: scuole, classi, iscritti, ripetenti, per livello (Infanzia / Primaria / Secondaria I / Secondaria II) e gestione (Pubblica / Privata)"
data_period: "2024 (anno scolastico 2023/24)"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — dataflow DCIS_SCUOLE (52_1044) — Indagine annuale sulle scuole, classi, alunni, personale docente"
date_published: "2025"
date_scraped: "2026-05-12"
content_hash: 387bdea108bc9a32a39e09ea102e51c7edcf94894910289fbed7d9e93553b7b2
tags: [istruzione]
description: "Sistema scolastico italiano 2024: 53.352 scuole, 8 milioni di studenti, 4 livelli (Infanzia, Primaria, Secondaria I, Secondaria II) — struttura, gestione pubblica/privata, ripetenze."
---

# Sistema scolastico italiano — struttura e dimensioni, 2024

## Headline

**53.352 scuole. 8.035.009 studenti. 184.965 ripetenti (di cui 154.529 nella sola Secondaria II — il 5,7% degli iscritti).**

Il sistema scolastico italiano dalla scuola dell'infanzia alla secondaria di II grado, anno scolastico 2023/24.

## Struttura per livello — Italia 2024

| Livello | Scuole | Classi | Iscritti | Ripetenti | Tasso ripetenza |
|---|---|---|---|---|---|
| Infanzia | 21.928 | 63.925 | 1.249.628 | — | — |
| Primaria | 16.485 | 135.928 | 2.433.462 | 5.696 | 0,2% |
| Secondaria I grado | 8.045 | 82.428 | 1.642.229 | 24.884 | 1,5% |
| **Secondaria II grado** | 6.894 | 137.486 | 2.709.690 | **154.529** | **5,7%** |
| **TOTALE** | **53.352** | **419.767** | **8.035.009** | **185.109** | — |

**Insight chiave:** la ripetenza è quasi assente fino alla scuola media (0,2-1,5%) e **esplode al 5,7% nella Secondaria II grado**. Il sistema italiano espelle/rallenta gli studenti soprattutto nelle superiori.

## Gestione pubblica vs privata — Italia 2024

| Livello | Scuole pubbliche | Scuole private | Quota privata (scuole) | Iscritti pubblica | Iscritti privata | Quota privata (iscritti) |
|---|---|---|---|---|---|---|
| Infanzia | 15.001 | 6.927 | **31,6%** | 913.148 | 336.480 | **26,9%** |
| Primaria | 15.122 | 1.363 | 8,3% | 2.276.292 | 157.170 | 6,5% |
| Secondaria I | 7.395 | 650 | 8,1% | 1.572.032 | 70.197 | 4,3% |
| Secondaria II | 5.253 | 1.641 | **23,8%** | 2.579.049 | 130.641 | 4,8% |

**Due bolle private:** la scuola dell'infanzia (1/3 delle scuole private, 27% degli iscritti — Italia ha una forte tradizione di scuole paritarie cattoliche) e la Secondaria II (24% delle scuole private ma solo 5% degli iscritti — molte scuole di nicchia, piccole). Primaria e Sec I sono quasi interamente pubbliche.

## Iscritti per classe (class size) — Italia 2024

| Livello | Media iscritti per classe |
|---|---|
| Infanzia | 19,5 |
| Primaria | 17,9 |
| Secondaria II (totale) | 20,1 |
| Secondaria II (pubblica) | 19,7 |
| Secondaria II (privata) | 14,5 |

⚠️ Le viste "indicatori scolastici" del DCIS_SCUOLE (`_4`, `_7`, `_13`) contengono **SOLO** l'indicatore "Iscritti per classe". Non sono disponibili in questo dataset altri indicatori scolastici come tasso di regolarità, dispersione per regione, abbandono interno — sono in altri dataflow ISTAT (vedi gap nel manifest).

## Insegnanti delle scuole statali 2015-2024

Serie temporale disponibile per gli insegnanti **delle sole scuole statali** (DCIS_SCUOLE views `_3`, `_9`, `_12`) per Infanzia, Sec I e Sec II. Dato di stock disponibile dal 2015 al 2024 per ciascun livello.

## Metodologia

Framework: **ISTAT — Indagine annuale sulle scuole (modello SCU)**, condotta in collaborazione con il Ministero dell'Istruzione e del Merito (MIM). Universo: tutte le scuole italiane attive (pubbliche statali + pubbliche non statali + paritarie + private non paritarie).

- **Anno scolastico di riferimento:** 2023/24 (etichettato 2024 nei dati).
- **"Scuole" = sede scolastica autonoma** (codice meccanografico). Una scuola può avere più plessi (succursali) che non sono conteggiati separatamente come scuole.
- **"Iscritti"** = numero di alunni iscritti all'inizio dell'anno scolastico. Non coincide con frequentanti effettivi alla fine dell'anno.
- **"Ripetenti"** = studenti iscritti nell'anno X che ripetono lo stesso anno di corso dell'anno precedente.
- **Edizione corrente** dei dati 2024 (release ISTAT 2025).

## Cosa NON è coperto da questi file

I dati ISTAT in `_raw/istruzione/DCIS_SCUOLE/` permettono di rispondere a "quante scuole, classi, studenti, insegnanti" per livello, ma **NON forniscono**:

- **Tasso di abbandono / dispersione scolastica** → vedi card [[abbandono-scolastico-precoce-italia-2020]] (basato su DCCV_ESL_UNT2020, metodologia pre-2020 — da aggiornare).
- **Regolarità del percorso scolastico** (% studenti in pari con l'età).
- **PISA / OCSE-PISA test punteggi 15-anni** — dataflow OECD separato, non ancora in corpus.
- **Spesa per studente** → vedi card [[spesa-per-studente-italia-2022]].
- **Composizione per cittadinanza degli studenti** (% studenti stranieri per livello).
- **Differenze territoriali per provincia/regione** (esistono nei file _2, _5, _8, _11 ma non sintetizzate in questa card che è national-level).

## Caveat e note di lettura

- **Anno scolastico ≠ anno solare.** L'etichetta "2024" si riferisce all'anno scolastico 2023/24 (settembre 2023 – giugno 2024).
- **Scuole serali e per adulti** sono comprese nella Sec II grado quando offrono corsi diurni equivalenti.
- **CFP / Istruzione e Formazione Professionale (IeFP)** sono parzialmente nei dati ISTAT (quando convenzionati col MIM) ma non sempre — il dato Sec II può essere sotto-stimato vs i dati MIM "Anagrafe Studenti".
- **Ripetenze Sec II 5,7% = ~155k studenti/anno** è una cifra molto alta nel confronto europeo. È il principale meccanismo italiano di "filtraggio" del flusso Sec II → Università.
- **Iscritti totali 8 milioni** è coerente con la coorte demografica italiana (circa 14 anni per coorte × 590k nati medi 2008-2020 ≈ 8,3 mln in età 3-19).

## Sorgente raw

`_raw/istruzione/DCIS_SCUOLE/` — 12 file CSV, viste `_1` (totale Italia) attraverso `_14` (diplomati per provincia). Dataflow ISTAT 52_1044.

Viste principali per ricostruzione cifre:
- `_1` Scuole - Principali dati (Italia × 4 livelli × Pubblica/Privata)
- `_2` Infanzia - scuole, classi, bambini
- `_5` Primaria - scuole, classi e alunni (incluso ripetenti)
- `_8` Secondaria I grado - scuole, classi e alunni (incluso ripetenti)
- `_11` Secondaria II grado - scuole, classi e studenti (incluso ripetenti)
- `_3`, `_9`, `_12` Insegnanti scuole statali per livello (serie 2015-2024)
- `_4`, `_7`, `_13` Indicatori scolastici (solo iscritti per classe)
- `_14` Diplomati Sec II per provincia
