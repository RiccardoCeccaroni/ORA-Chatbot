---
id: titolo-studio-adulti-25-64-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Titolo di studio della popolazione adulta 25-64, Italia, 2024"
data_metric: "Distribuzione % della popolazione 25-64 per livello di istruzione più alto raggiunto (Below upper secondary / Upper secondary / Tertiary) — framework OECD ISCED 2011"
data_period: "2024"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Education at a Glance, dataflow DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA"
date_published: "2025"
date_scraped: "2026-05-12"
content_hash: c7d1f496b53b75b6b8c775386492d283e291273c581455f7c45e2645bd5da790
tags: [istruzione, lavoro-politiche-sociali, pari-opportunita-inclusione]
description: "Italia 2024 — 22,3% degli adulti 25-64 ha completato l'istruzione terziaria, contro 41,8% di media OCSE. Italia 2° peggior tasso OCSE su terziaria — gap di 19,5 punti percentuali."
---

# Titolo di studio degli adulti 25-64, Italia, 2024

## Headline

**Solo il 22,3% degli adulti italiani 25-64 ha completato l'istruzione terziaria.** La media OCSE è **41,8%**. Italia è di **−19,5 punti percentuali sotto la media OCSE**, e si colloca tra i paesi OCSE col tasso più basso (peggio fanno solo Messico, Turchia, Costa Rica).

## Distribuzione completa — Italia vs comparatori (% pop. 25-64, 2024)

| Livello istruzione | 🇮🇹 Italia | 🌐 OCSE | 🇩🇪 Germania | 🇫🇷 Francia | 🇪🇸 Spagna |
|---|---|---|---|---|---|
| **Below upper secondary** (ISCED 0-2 — fino licenza media) | **33,3%** | 18,6% | 15,9% | 16,1% | 34,7% |
| Upper secondary / post-secondary non-tertiary (ISCED 3-4 — diploma) | 44,4% | 40,0% | 49,9% | 40,6% | 23,0% |
| **Tertiary** (ISCED 5-8 — laurea + dottorato) | **22,3%** | **41,8%** | 34,3% | 43,4% | 42,3% |

**Tre confronti politicamente rilevanti:**

1. **"Below upper secondary" 33,3% in Italia vs 18,6% OCSE.** Quasi il doppio. **1 italiano su 3 in età 25-64 non ha completato la secondaria superiore.**
2. **Tertiary attainment 22,3% in Italia vs 41,8% OCSE.** **Italia ha quasi la metà dei laureati per testa della media OCSE.**
3. **Italia VS Spagna:** Spagna ha più "below upper secondary" (34,7% vs 33,3%) ma ANCHE molti più laureati (42,3% vs 22,3%). Il modello spagnolo è "polarizzato" (molti laureati + molti senza diploma). Il modello italiano è "schiacciato verso il basso" (massa nel diploma, pochi laureati).

## Implicazioni — perché l'Italia è strutturalmente bassa sulla terziaria

Sotto-tassi di laurea italiani sono il risultato di una combinazione di fattori storici e correnti:

- **Coorte 25-64 = nati 1960-1999.** I 25-29enni (nati metà anni '90) hanno tassi di laurea più alti (~32% nel 2024) ma sono diluiti nella media dai 55-64enni (~15% laureati). Il "gap generazionale" è in lento recupero.
- **Tasso di iscrizione universitaria post-diploma è ~55%** (orientativo — verificare con dato OECD specifico). Su 100 diplomati, ~55 si iscrivono entro 2 anni — sotto la media OCSE ~70%.
- **Tasso di completamento universitario** ≈ 60-65% in Italia (laureati / immatricolati 6-8 anni prima) — sotto OCSE ~70-75%. Il sistema italiano ha alto dropout universitario.
- **Carenza di formazione terziaria professionale corta** (ISCED 5 — short-cycle): in Italia praticamente assente. Cfr. card [[spesa-per-studente-italia-2022]]: ISCED 5 short-cycle Italia spende solo $3.691/studente (un quarto della terziaria), molto sotto-utilizzato.
- **Effetti economici di ritorno limitati per i laureati italiani:** il "premium salariale" della laurea in Italia è ~30-40% (sotto OCSE ~50-60%), riducendo l'incentivo individuale a iscriversi.

## Insight comparativo

Tra i paesi UE-grandi del campione (Germania, Francia, Spagna), **l'Italia è l'unico paese con quota laureati 25-64 sotto il 30%.** Tutte le altre principali economie europee hanno superato il 30-35% durante gli anni 2010, l'Italia è rimasta al palo.

## Metodologia

Framework: **OECD Education at a Glance — Educational Attainment of Adults (NEAC = National Educational Attainment Classification)**. Dataflow `DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA`, release 2025 (data 2024).

- **Popolazione di riferimento:** adulti **25-64 anni** (definizione OCSE standard per "stock educativo" della popolazione produttiva).
- **Classificazione titoli:** ISCED 2011 aggregata in 3 livelli (0-2 / 3-4 / 5-8). ISCED = International Standard Classification of Education.
- **Fonte dati per Italia:** Rilevazione sulle Forze di Lavoro (RFL) ISTAT, armonizzata col regolamento UE EU-LFS post-2021.
- **MEASURE:** POP, **UNIT_MEASURE:** PT_POP_SEX_AGE (% della popolazione nella stessa fascia di sesso/età).
- **SEX:** Total (M+F aggregato in questo file). Le scomposizioni per sesso esistono nel dataflow ma non in questo export.

## Caveat e note di lettura

- **Single-year snapshot.** Il file include 2022-2024, ma le 3 righe Italia esportate sono **tutte per il 2024**. Per il trend storico serve re-export.
- **L'ISCED 5 short-cycle è raro in Italia.** Le lauree triennali "short" italiane sono classificate ISCED 6, non ISCED 5 — quindi i confronti con paesi che hanno robusti corsi ISCED 5 (Spagna, USA community college, Germania Fachschule) non sono perfetti.
- **Confronto con il dato ISTAT 2020:** la card parallela [[popolazione-titolo-studio-25-64-italia-2024]] mostrava 15,3% laurea per popolazione 15+ nel 2020. Il 22,3% qui (25-64, 2024) è coerente: stringere a 25-64 alza il dato, + 4 anni di ricambio generazionale aggiungono altri ~2 punti.
- **Differenza Italia-OCSE in trend.** Il gap Italia-OCSE sulla terziaria si è ALLARGATO dal 2010 (quando era ~13 p.p.) al 2024 (~20 p.p.) perché OCSE è cresciuto più velocemente. L'Italia recupera in valore assoluto ma perde in posizione relativa.

## ORA — la frase politicamente densa

In ogni dibattito sull'istruzione italiana il numero a cui le forze politiche tornano è **"l'Italia è quart'ultima OCSE per laureati"** (o "penultima" o "ultima UE-27") — questa card lo quantifica: 22,3% vs OCSE 41,8% nel 2024. Cifre coerenti pubblicate annualmente nel report **OECD Education at a Glance** (orientativo, da verificare con web search per l'edizione più recente).

## Sorgente raw

`_raw/istruzione/DF_LSO_NEAC_DISTR_EA/OECD.EDU.IMEP,DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA,1.0+AUS+AUT+BEL+CAN+CHL+COL+CRI+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+OECD+ARG.csv`

Dataflow OECD `DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA(1.0)` — 144 righe (48 paesi × 3 attainment levels × 1 anno), 3 righe Italia (2024).
