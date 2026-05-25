---
id: spesa-per-studente-italia-2022
type: data
attribution: oecd
quality_tier: D1
title: "Spesa per studente per livello di istruzione, Italia, 2022"
data_metric: "Spesa annua totale per studente full-time-equivalent in USD PPP per livello ISCED, e come % del PIL pro capite. Framework OECD Education at a Glance (UOE)"
data_period: "2022"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Education at a Glance, dataflow DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD"
date_published: "2025"
date_scraped: "2026-05-12"
content_hash: a4fb5149b0efd2b183a29112ae5bb746d70fc0a6c5cb34027183d9b72d416112
tags: [istruzione, universita-ricerca, spesa-pubblica]
description: "Spesa per studente in Italia 2022 per livello ISCED: $14.959 primaria (+18% vs OCSE), $14.713 terziaria (-30% vs OCSE). Italia spende più della media nei livelli bassi, meno nei livelli alti."
---

# Spesa per studente per livello di istruzione, Italia, 2022

## Headline

L'Italia spende **MENO della media OCSE per la terziaria (-30%)** e **PIÙ della media OCSE per la primaria (+18%)**. Il pattern italiano è: spesa relativamente generosa nei livelli bassi, ma sotto-investimento progressivo man mano che si sale verso l'università.

## Spesa per studente 2022 — Italia vs OCSE (USD PPP per FTE)

| Livello ISCED | 🇮🇹 Italia (USD PPP) | 🌐 OCSE (USD PPP) | Differenza Italia |
|---|---|---|---|
| ISCED 1 — Primaria | **$14.959** | $12.655 | **+18%** ← Italia sopra OCSE |
| ISCED 2 — Sec inferiore | $11.897 | $14.265 | −17% |
| ISCED 3 — Sec superiore | $13.045 | $14.501 | −10% |
| **ISCED 5-8 — Terziaria** | **$14.713** | **$21.021** | **−30%** ← Italia molto sotto OCSE |
| ISCED 5 — Terziaria short-cycle | $3.691 | (nd diretto) | drammaticamente bassa |
| **ISCED 1-8 — Tutti i livelli** | $13.750 | $14.865 | −8% |

**Tre conclusioni politicamente dense:**

1. **L'Italia ha una distribuzione DECRESCENTE della spesa per studente** dall'infanzia all'università (al netto degli short-cycle): il sistema italiano spende relativamente bene nei primi anni e progressivamente meno mano a mano che si sale di livello.
2. **Il gap col mondo OCSE è SOPRATTUTTO sulla terziaria.** -30% sulla terziaria = -$6.300 per studente universitario italiano vs un suo coetaneo medio OCSE.
3. **L'ISCED 5 short-cycle italiano è quasi inesistente.** Solo $3.691/studente — un quarto della terziaria standard. In paesi con sistemi short-cycle robusti (USA community college, Spagna ciclos formativos, Germania Fachschule) l'investimento è simile alla terziaria lunga.

## Come % del PIL pro capite — Italia 2022

| Livello ISCED | Italia % PIL pc |
|---|---|
| ISCED 1 — Primaria | 26,6% |
| ISCED 2 — Sec inf | 21,2% |
| ISCED 3 — Sec sup | 23,2% |
| ISCED 5-8 — Terziaria | 26,2% |
| ISCED 1-8 — Tutti i livelli | **24,4%** |

L'Italia spende circa **un quarto del PIL pro capite per ciascun studente** — coerente con la media OCSE ~25-30%. La metrica "% PIL pc" normalizza per il livello di ricchezza del paese, rendendo confronti internazionali più puliti.

## Cosa è incluso

L'indicatore **FIN_PERSTUD** comprende **tutta la spesa per istituzioni educative**:
- **Spesa pubblica** (statale + regioni + EE.LL. + UE)
- **Spesa privata diretta dei nuclei familiari** (tasse universitarie, rette scuole paritarie, materiale didattico)
- **Spesa di imprese e altri privati** in formazione formale.

Filtro su `EXP_SOURCE = _T (Total)` + `EXP_DESTINATION = INST_EDU (All educational institutions)` + `EXPENDITURE_TYPE = DIR_EXP (Direct expenditure)`.

**Esclude:** spesa per istruzione informale, spesa per ricerca pura di base, sussidi che non transitano per le istituzioni (es. buoni studenti dati direttamente alle famiglie). Per la spesa pubblica isolata vedi [[spesa-pubblica-istruzione-italia-2023]] (DF_UOE_FIN_SOURCE).

## Confronto con altri indicatori

- **% PIL spesa pubblica istruzione Italia ~4%** vs OCSE ~4,9% (orientativo, da verificare). L'Italia spende meno in % di PIL — ma la spesa per studente che vediamo qui è normalizzata per studente, non per cittadino.
- **Salari docenti italiani sotto OCSE.** Una parte importante del gap di spesa per studente è dovuta a salari docenti italiani strutturalmente bassi rispetto all'OCSE. (Dataflow OECD `DSD_EAG_SAL_ACT` da scaricare con REF_AREA=ITA — non incluso in questo batch).
- **Composizione spesa terziaria:** Italia investe relativamente poco in **R&D universitaria** (~0,3% PIL vs OCSE ~0,5%), che fa parte della spesa terziaria. Il gap di -30% è in parte ricerca, in parte didattica.

## Metodologia

Framework: **OECD Education at a Glance — UOE (UNESCO/OECD/Eurostat) Joint Questionnaire**. Dataflow `DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD`, release 2025 (data 2022).

- **Unit:** USD PPP per studente FTE (full-time equivalent) per anno scolastico.
- **PPP base:** GDP PPP — converte la spesa nazionale al potere d'acquisto OCSE comparabile.
- **Anno scolastico:** 2021/22.
- **Studente FTE:** ponderato per la frazione del programma. Un part-time conta meno di 1 studente intero.
- **ISCED 11 levels:** 0 (early childhood) / 1 (primary) / 2 (lower sec) / 3 (upper sec) / 4 (post-secondary non-tertiary) / 5 (short-cycle tertiary) / 6 (bachelor) / 7 (master) / 8 (doctoral). 5T8 = aggregato terziaria. 6T8 = solo università long-cycle.

## Caveat e note di lettura

- **Snapshot 2022 single-year.** Il dataflow ha le serie storiche ma il file include solo 2022. Per il trend 2015-2022 serve re-export.
- **Alcuni sub-livelli ISCED 11 per Italia hanno valori vuoti** (ISCED 11_34 / 11_35 / 4 sono missing). L'Italia non riporta o non ha la distinzione tra sec sup generale (ISCED 34) e vocazionale (ISCED 35) come l'OECD richiede — quindi solo l'aggregato ISCED 3 è disponibile.
- **PPP volatili.** Il dato in USD PPP è sensibile a oscillazioni del tasso di cambio PPP. La metrica % PIL pc è più stabile.
- **OECD = media aritmetica dei paesi membri**, non aggregato ponderato. Paesi piccoli pesano come paesi grandi → la media OCSE è alzata da Stati Uniti, Lussemburgo, Norvegia, Svizzera (paesi con spesa molto alta).

## ORA — perché la cifra è politicamente rilevante

Il sotto-investimento italiano sulla terziaria (-30% vs OCSE) è uno degli argomenti chiave nel dibattito su:
- **Diritto allo studio universitario** — borse di studio, alloggi, riduzione tasse universitarie.
- **Brain drain dei laureati italiani** — Italia investe meno, paga peggio, espelle talenti.
- **Salari ricercatori e docenti universitari** — Italia paga ~30-40% sotto omologhi OCSE.
- **Riforma università** — il sotto-investimento storico è il principale vincolo a riforme strutturali (assenza fondi per espandere posti, borse, infrastrutture).

## Sorgente raw

`_raw/istruzione/DF_UOE_INDIC_FIN_PERSTUD/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD,3.1+..ISCED11_1+ISCED11_2+ISCED11_3+ISCED11_34+ISCED11_35+ISCED11_4+ISCED11_5+ISCED11_5T8+ISCED11_6T8+ISCED11_1T8._T.INST_EDU.DIR_EXP.V+_Z.USD_PPP_ST+PT_B1GQ_P.csv`

Dataflow OECD `DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD(3.1)` — 920 righe (46 paesi × ~10 ISCED levels × 2 unità), 20 righe Italia (2022).
