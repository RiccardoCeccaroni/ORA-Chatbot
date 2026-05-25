---
id: trasferimenti-residenza-interni-italia-2025
type: data
attribution: istat
quality_tier: D1
title: "Trasferimenti di residenza interni all'Italia, 2025 (dato provvisorio)"
data_metric: "trasferimenti di residenza tra comuni italiani (mobilità interna)"
data_period: "2025 (annuale, dato provvisorio)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,POP,1.0/IT1.POP_MIGR/IT1_28_185"
source_doc: "ISTAT — Movimento migratorio della popolazione residente, dataflow DCIS_MIGRAZIONI (28_185), view _1"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 5ecb8b42ebb39d852f0159f7fd5e1ae20d4701b5df071cb345cfc8c6f6ab53c5
tags: [immigrazione, comuni-province-regioni]
description: "Trasferimenti di residenza tra comuni italiani nel 2025 (dato provvisorio): 1.455.406 totali. Il 57,7% ha come destinazione il Nord, il 24,4% il Mezzogiorno, il 17,8% il Centro."
---

# Trasferimenti di residenza interni all'Italia, 2025 (dato provvisorio)

**Totale trasferimenti tra comuni italiani 2025:** **1.455.406**

## Ripartizione per macro-area di destinazione

| Area di destinazione | Trasferimenti | Quota |
|---|---|---|
| **Nord (ITCD)** | **840.428** | **57,7%** |
| — Nord-ovest (ITC) | 508.887 | 35,0% |
| — Nord-est (ITD) | 331.541 | 22,8% |
| **Centro (ITE)** | **259.154** | **17,8%** |
| **Mezzogiorno (ITFG)** | **355.824** | **24,4%** |
| — Sud (ITF) | 240.152 | 16,5% |
| — Isole (ITG) | 115.672 | 7,9% |

## Top regioni destinazione (trasferimenti in ingresso)

| Regione | Trasferimenti in ingresso |
|---|---|
| Lombardia (ITC4) | 330.568 |
| Emilia-Romagna (ITD5) | 130.331 |
| Veneto (ITD3) | 139.033 |
| Campania (ITF3) | 109.655 |
| Lazio (ITE4) | 108.751 |
| Toscana (ITE1) | 96.492 |
| Sicilia (ITG1) | 84.264 |
| Puglia (ITF4) | 55.986 |
| Piemonte (ITC1) | 136.122 |
| Liguria (ITC3) | 37.585 |
| Marche (ITE3) | 36.342 |
| Calabria (ITF6) | 30.948 |
| Friuli VG (ITD4) | 33.087 |
| Sardegna (ITG2) | 31.408 |
| Abruzzo (ITF1) | 30.628 |
| Trento+Bolzano (ITDA) | 29.090 |

## Lettura politica

### "Dove vanno gli italiani che si trasferiscono?"
**Il Nord attrae 1 trasferimento su 2** (57,7% delle iscrizioni interne, contro il 46% della popolazione residente nel Nord). Il Nord-ovest da solo (Piemonte, Lombardia, Liguria, Valle d'Aosta) capta il 35,0% dei flussi.

Il **Mezzogiorno** (Sud + Isole) riceve il 24,4% — ma una quota considerevole sono **rientri** (ad es. pensionati, ritorni post-istruzione), non attrazione strutturale.

### Il punto politico: mobilità interna come specchio dei divari
- **Polo attrattore Lombardia:** 330k trasferimenti in ingresso (22,7% del totale nazionale). La Lombardia da sola attrae più trasferimenti di tutto il Mezzogiorno (Sud + Isole = 355k).
- **Emilia-Romagna + Veneto + Lazio:** altri tre poli con ~110-140k trasferimenti in ingresso ciascuno.
- **Regioni del Sud non sono in calo assoluto** (la Campania resta una delle prime 5 destinazioni con 109k), ma il **bilancio netto** (in – out) non è qui calcolato — vedi gap residuo per saldo migratorio interno regionale.

### Confronto con la migrazione internazionale
- Trasferimenti **dentro l'Italia 2025**: ~1.46M
- Iscrizioni **dall'estero 2025**: ~440k
- Cancellazioni **per l'estero 2025**: ~144k

La mobilità interna è **3,3 volte più grande** dei flussi internazionali in entrata. Il dibattito politico tende a focalizzarsi sulla seconda, ma la prima ha effetti demografici e fiscali altrettanto significativi.

## Metodologia

Fonte: **Movimento migratorio della popolazione residente**, ISTAT — dataflow `DCIS_MIGRAZIONI` (28_185), vista _1 ("Migrazioni interne — Italiani e stranieri").
Definizione: trasferimenti di residenza tra comuni italiani, indipendentemente dalla cittadinanza (`DATA_TYPE = CORE`, "Trasferimenti di residenza", `CITIZENSHIP = TOTAL`).
Universo: tutti i residenti italiani che cambiano comune di residenza (sia italiani che stranieri).
Codici NUTS-1 ISTAT: ITC = Nord-ovest, ITD = Nord-est, ITCD = Nord, ITE = Centro, ITF = Sud, ITG = Isole, ITFG = Mezzogiorno.

**Dati 2025 provvisori** (variabile `OBS_STATUS = p`).

## Caveat e note di lettura

- Il dato è **lordo** (un trasferimento). Non è il **saldo migratorio netto** (in – out) per regione, che richiede l'origine oltre alla destinazione. Per il saldo interno per regione → re-export con dimensione origine×destinazione (matrice OD).
- Le **statistiche aggregate per macro-area possono mascherare flussi infraregionali** (es. dentro la Lombardia: spopolamento aree interne vs concentrazione Milano).
- "Trasferimento di residenza" è un atto amministrativo che **sottostima la mobilità reale**: lavoratori che si spostano senza cambiare residenza (es. fuori-sede, pendolari di lungo raggio) non appaiono qui.
- I dati includono anche **stranieri residenti** che si trasferiscono da un comune italiano all'altro — non solo italiani.

## Sorgente raw

- `_raw/immigrazione/DCIS_MIGRAZIONI/Migrazioni interne  - Italiani e stranieri (IT1,28_185_DF_DCIS_MIGRAZIONI_1,1.0).csv`
