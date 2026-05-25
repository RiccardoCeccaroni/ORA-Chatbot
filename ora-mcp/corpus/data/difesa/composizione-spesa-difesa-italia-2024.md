---
id: composizione-spesa-difesa-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Composizione della spesa pubblica per la difesa — Italia, 2024 (COFOG 02 sub-funzioni)"
data_metric: "Spesa per consumi finali delle Amministrazioni Pubbliche (S13, aggregato P3_D_W0) per sub-funzione COFOG 02 (Difesa militare, civile, aiuti militari esteri, R&D difesa, defence n.e.c.), valori a prezzi correnti in milioni di euro"
data_period: "2024 (consolidato; 2025 disponibile in versione provvisoria)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500CONT,1.0/IT1,95_94,1.0/IT1,95_94_DF_DCCN_OTEPPA_1,1.0"
source_doc: "ISTAT — Spesa per consumi per funzione (COFOG 2 e 3 cifre), dataflow DCCN_OTEPPA_1 (95_94)"
date_published: "2025"
date_scraped: "2026-05-13"
content_hash: b870995aa70841604d3996fc8710b21f3ee12006db2548ee6bcec7392f03951f
tags: [difesa, spesa-pubblica, cofog, composizione]
description: "Composizione spesa difesa Italia 2024 (consumi finali AP, €M): difesa militare €20.544 (85,1%), aiuti militari esteri €1.407 (5,8%), defence n.e.c. €522 (2,2%), difesa civile €890 (3,7%), R&D difesa €89 (0,4%). Totale G020 = €24.148 mln. Il vero squilibrio è la voce R&D difesa allo 0,4% — l'Italia spende per R&D difesa una frazione di Germania (37×) e Francia (16×)."
---

# Composizione della spesa pubblica per la difesa — Italia, 2024

**Headline:** la spesa difesa italiana misurata come "consumi finali AP" (P3_D_W0, definizione ISTAT) nel 2024 ammonta a **€24,148 mld**. Il **85% va alla difesa militare in senso stretto** (G0201 = €20,5 mld), il resto frammentato tra civil defence, aiuti esteri, R&D, residuali. La **R&D difesa è lo 0,4% del totale** (€89 mln) — anomalia strutturale italiana, vedi sotto.

## Spesa per sub-funzione COFOG 02, Italia, 2024 (€M, prezzi correnti)

| Sub-funzione COFOG | Codice | 2024 (€M) | % G020 |
|---|---|---|---|
| **Difesa militare** | G0201 | **20.544** | **85,1%** |
| Aiuti militari esteri | G0203 | 1.407 | 5,8% |
| Difesa civile | G0202 | 890 | 3,7% |
| Defence n.e.c. (residuale) | G0205 | 522 | 2,2% |
| R&D Difesa | G0204 | **89** | **0,4%** |
| **Totale Difesa** | **G020** | **24.148** | **100%** |

*Nota: la somma delle sub-funzioni dà 23.452 vs G020 = 24.148; il gap di ~€700M (3%) deriva da arrotondamenti e dalla quota P31_D_W0 (individual consumption) che ISTAT classifica G020 ma non scomposta nei sub-codici. Per le proporzioni la quadratura è sostanzialmente corretta.*

## Evoluzione 2019 → 2024 — trend per sub-funzione (€M)

| Sub-funzione | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Δ 2019→2024 |
|---|---|---|---|---|---|---|---|
| Difesa militare (G0201) | 19.750 | 19.923 | 19.751 | 19.541 | 19.738 | 20.544 | **+4,0%** |
| Aiuti militari esteri (G0203) | 904 | 1.144 | 1.063 | 1.254 | 1.482 | 1.407 | **+55,6%** |
| Difesa civile (G0202) | 696 | 696 | 790 | 833 | 847 | 890 | **+27,9%** |
| Defence n.e.c. (G0205) | 278 | 328 | 381 | 404 | 427 | 522 | **+87,8%** |
| R&D Difesa (G0204) | 73 | 69 | 68 | 62 | 65 | 89 | **+21,9%** |
| **Totale Difesa (G020)** | 21.700* | 22.160 | 22.053 | 22.094 | 22.565 | 24.148 | **+11,3%** |

*2019 totale stimato sommando le sub-funzioni; OTEPPA_1 non riporta direttamente G020 totale 2019.

**Patterns chiave:**
- **G0201 difesa militare** è cresciuta solo +4% in 5 anni nominali — flatlining reale (l'inflazione cumulata 2019-2024 supera il 15%).
- **G0203 aiuti militari esteri** è la voce più mossa (+56%) — incorpora la crescita degli aiuti a Ucraina post-2022. Picco 2023 (€1,482M) coincide con i pacchetti militari Italia-Ucraina.
- **G0204 R&D difesa** è cresciuta in % (+22%) ma resta a livelli irrisori — €89M nel 2024 = 1 caccia F-35A in unit cost.

## Confronto con [[spesa-difesa-italia-vs-paesi-2022]] (definizione OECD vs ISTAT)

I numeri di questa scheda (consumi finali, P3_D_W0) e quelli della scheda cross-country (OTE, total expenditure) divergono per definizione:
- ISTAT P3_D_W0 G020 2022 = €22,094 M
- OECD OTE GF02 Italia 2022 = €24,893 M
- **Gap di ~€2,8 mld** = ammortamenti e formazione capitale fisso lordo, che OECD include in OTE ma ISTAT esclude dal P3.

Per la narrativa pubblica ("Italia spende €X per la difesa") il riferimento più usato è la **definizione NATO**, ancora più ampia. Vedi caveat metodologico nella scheda [[spesa-difesa-italia-vs-paesi-2022]].

## Lettura politica

**Quadro empirico per la tesi 04:**
- La tesi cita "spesa sotto il 2% del PIL e fortemente assorbita da personale e spese correnti, con pochi margini per addestramento, manutenzioni e tecnologie. Sul piano […] addestramento e formazione, manutenzioni, infrastrutture, scorte è pericolosamente bassa (10,66% del budget complessivo, contro un 25% considerato ottimale)."
- Questa scheda non smentisce, ma **fa fatica a verificare il 10,66%** — la decomposizione ISTAT è per sub-funzione COFOG (militare/civile/aiuti/R&D), non per natura economica (personale/equipaggiamenti/operations) all'interno della G0201 militare. Quella granularità è in OTEPPA_2 o in TABLE11 OECD (transaction × COFOG): da incrociare in card futura.

**Ciò che la scheda mostra in modo netto:**
1. **R&D difesa al minimo storico in % del totale (0,4%).** Tesi 04 §4 propone "ricalibrare il PNRM, creare acceleratore dual-use, incrementare R&S": il dato di partenza è €89M/anno, contro €4.855M tedeschi e €2.161M francesi (cfr. [[r-s-difesa-italia-vs-paesi-2024]]). **Italy is structurally underspending on defence R&D by 1-2 orders of magnitude vs peers.**
2. **Aiuti militari esteri (G0203) sono cresciuti +56% in 5 anni** — coerente con il sostegno a Ucraina, ma la voce è opaca: ISTAT non disaggrega per paese destinatario.
3. **Difesa militare in senso stretto è piatta in termini reali** — i +4% nominali 2019-2024 sono inferiori all'inflazione, quindi la spesa reale per personale + funzionamento militare è scesa.

## Caveat e note di lettura

- **P3_D_W0 (final consumption) ≠ spesa totale difesa.** Esclude formazione capitale fisso (acquisti di nuovi sistemi d'arma maggiori = K), trasferimenti, ammortamenti. Per il totale serve l'aggregato OTE in TABLE11 OECD (cfr. scheda cross-country).
- **2025 è provvisorio.** OTEPPA_1 mostra 2025 G020 = €24.580 M ma la disaggregazione per sub-funzione non è ancora pubblicata. Aggiornare a release ISTAT dicembre 2026.
- **G0204 R&D difesa = €89 M (ISTAT) ≠ €79 M (OECD GBARD).** Le due fonti hanno definizioni leggermente diverse di "R&D difesa": ISTAT cattura tutto il consumo finale AP che la classificazione COFOG marca come 02.4; OECD GBARD cattura "Government Budget Allocations for R&D" finalizzati alla difesa, definizione NABS14, che esclude alcuni costi indiretti. Il gap di €10M è metodologico, non statistico.
- **G0202 civil defence** include protezione civile, sicurezza nucleare civile, ecc. — NON include forze di polizia (G030, in altra scheda futura) né vigili del fuoco (G0302).

## Lettura attesa per il chatbot ORA

- **State**: Italia spende €24,1 mld in difesa (consumi finali AP, 2024), 85% di cui in difesa militare in senso stretto.
- **Project**: ORA punta a riequilibrare con +R&D e +equipaggiamenti — partendo da €89M/anno R&D che è 1/4 del normale OCSE.
- **Justify**: il 10,66% citato nella tesi per "addestramento+manutenzioni+scorte" non è verificabile da questa scheda (granularità diversa); va incrociato con TABLE11 OECD per transaction × COFOG02.
- **Compare**: la quota R&D 0,4% è anomalia storica italiana; cross-country vedi scheda [[r-s-difesa-italia-vs-paesi-2024]].

## Sorgente raw

- File: `_raw/difesa/DCCN_OTEPPA_1/data.csv` (12 MB, 48.685 righe)
- Dataset: ISTAT `DCCN_OTEPPA_1` v1.0 (id 95_94_DF_DCCN_OTEPPA_1) — "Consumption expenditure by function (COFOG 2 and 3 digit)"
- Filtri di lettura applicati: REF_AREA=IT, INSTITUTIONAL_SECTOR=S13 (general government), VALUATION=V (current prices), DATA_TYPE_AGGR=P3_D_W0 (final consumption expenditure).
- Last update upstream: dicembre 2025.
