---
id: superficie-agricola-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Superficie agricola totale, Italia, 2024"
data_metric: "Total agricultural land area (TOTAGR_LAND) — superficie complessiva utilizzata per attività agricole (seminativi + colture permanenti + prati e pascoli permanenti), migliaia di ettari"
data_period: "2024; serie annuale 2012-2024"
source_url: "https://data-explorer.oecd.org/?topic=Agriculture"
source_doc: "OECD — Agricultural land area, dataflow DSD_AGRI_ENV@DF_AGLAND"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 2c13eb40a129935fd3d32ec51139122db3bec7c940b2a346de85683dc2fdd847
tags: [agricoltura, energia-ambiente-sostenibilita]
description: "Superficie agricola italiana 12,90 milioni di ettari (2024), sostanzialmente stabile attorno a 12,7-13,1 Mha negli ultimi 13 anni. Italia tra i grandi paesi UE per estensione agricola assoluta (4° dopo Francia, Spagna, Germania)."
---

# Superficie agricola totale, Italia, 2024

**Valore (2024):** **12.901,34 migliaia di ettari** = **~12,90 milioni di ha** (= 12,9 Mha).
**Variazione su 2023 (13.078,5 Mha):** **−177 mila ha** (−1,4%).
**Variazione su 2012 (12.548,1 kha):** **+353 mila ha** (+2,8% in 13 anni).

## Serie storica — l'agricoltura italiana mantiene la sua estensione

| Anno | Superficie agricola totale (kha) |
|---|---|
| 2012 | 12.548,1 |
| 2013 | 12.426,0 ← minimo serie |
| 2014 | 12.720,2 |
| 2015 | 12.660,9 |
| 2016 | 12.843,3 |
| 2017 | 13.005,8 |
| 2018 | 12.908,8 |
| 2019 | 13.150,2 |
| 2020 | 13.122,1 |
| 2021 | 12.987,4 |
| 2022 | 12.950,4 |
| 2023 | **13.078,5** ← massimo serie |
| **2024** | **12.901,3** |

**Pattern strutturale:** oscillazione attorno alla media di **~12,9 Mha**, senza trend di lungo periodo significativo. La narrazione comune della "scomparsa dell'agricoltura italiana" non è confermata dal dato di superficie totale OECD (che include sia SAU coltivata sia pascoli e prati permanenti).

## Composizione e contesto

I 12,9 milioni di ettari rappresentano **circa il 43% del territorio italiano** (Italia ha ~30,1 milioni di ha totali). Da cross-referenza con ISTAT [[coltivazioni-italia-2025]]:

- **Foraggere permanenti — prati e pascoli:** ~3,5 Mha (la voce singola più estesa)
- **Pascoli poveri:** ~1,8 Mha
- **Frumento duro:** ~1,13 Mha
- **Olive da olio:** ~1,09 Mha
- **Uva da vino:** ~0,69 Mha

(I 12,9 Mha OECD includono il riposo, le foraggere, i pascoli marginali. La SAU "lavorata" — la "Superficie Agricola Utilizzata" del Censimento ISTAT, è una nozione un po' diversa, normalmente ~12,5 Mha al Censimento agricoltura 2020.)

## Posizionamento internazionale (OECD AGLAND 2023, kha)

| Paese | Superficie agricola |
|---|---|
| Francia | 28.700 |
| Spagna | 23.700 |
| Germania | 16.600 |
| **Italia** | **13.079** |
| Polonia | 14.800 |
| Romania | 13.700 |
| Regno Unito | 17.500 |

Italia **4ª-5ª UE per estensione agricola assoluta**, ma con il 3° rapporto SAU/territorio dell'UE-5 (Italia ~43%, Spagna ~47%, Francia ~52%, Germania ~47%, Polonia ~47%). Cifra: l'Italia è territorialmente densa di agricoltura.

## Caveat e note di lettura

- **OECD vs ISTAT vs Eurostat: definizioni leggermente diverse.** Il dato OECD 12,9 Mha è "Total agricultural land area" e include prati permanenti, pascoli e terreno a riposo. La SAU ISTAT del Censimento Agricoltura 2020 era 12,53 Mha, perché esclude la SAT (superficie agricola totale = SAU + altre superfici agricole, come fabbricati rurali e boschi aziendali). Eurostat usa SAU armonizzata.
- **Variazioni annuali piccole, errore di misura ampio.** Le variazioni anno-su-anno di ±1-2% rientrano nell'errore di stima OECD (rifusione dati nazionali ISTAT/Eurostat). La curva piatta è significativa, **le micro-fluttuazioni no**.
- **La narrazione "consumo di suolo" non si misura qui.** L'ISPRA stima il consumo di suolo netto italiano in ~2.000 ha/anno (2010-2023, soprattutto in pianura padana e periurbano), che a livello aggregato è ~0,015% della superficie agricola. Il vero impatto del consumo di suolo è **qualitativo** (suoli più fertili convertiti in urbano) e **regionale**, non visibile sull'aggregato nazionale.
- **Trend strutturale: stabilità, non crescita.** Il "picco" 2023 a 13,08 Mha non è espansione agricola ma probabile riconciliazione metodologica con i dati del Censimento 2020. La realtà è una **superficie quasi-stabile** attorno a 12,9 Mha.

## Lettura politica

**Stato di fatto:** l'agricoltura italiana, misurata per estensione di terreno, è sostanzialmente stabile da 13 anni. Non si sta espandendo (no nuove terre coltivate) né scomparendo (no abbandono massiccio).

**Cosa si trasforma invece:**
- la **composizione** (più foraggere, meno cereali in certi ambiti)
- la **dimensione media aziendale** (concentrazione: meno aziende, ma più grandi, da 11 ha medi nel 2010 a ~14 ha al Censimento 2020)
- il **valore aggiunto** generato a parità di superficie (più intensività in alcuni distretti)

**Dibattito tipico:**
- "Stiamo perdendo terra agricola" → falso a livello aggregato, vero a livello regionale (pianura padana)
- "Serve ampliare le superfici biologiche" → vedi gaps_in_agricoltura_residual nel manifest (dato SINAB non ancora ingerito)
- "Difendiamo la sovranità alimentare" → vedi [[coltivazioni-italia-2025]] per la mappatura colture
- "Animal welfare vs estensione zootecnica" → vedi [[zootecnia-bestiame-italia-2024]]

## Metodologia

Framework OECD: armonizzazione FAO/Eurostat. Definizione di "agricultural land" segue **FAO**: arable land + permanent crops + permanent meadows and pastures. Esclude boschi, acque interne, terreno improduttivo. Aggiornamento annuale a fine anno + 1.

## Sorgente raw

`_raw/agricoltura/DF_AGLAND/OECD.TAD.ARP,DSD_AGRI_ENV@DF_AGLAND,1.2+.A.TOTAGR_LAND.....csv`

Dataset: OECD `DSD_AGRI_ENV@DF_AGLAND(1.2)` — Agricultural land area. 728 righe totali, **13 righe Italia** (annuali 2012-2024). MEASURE TOTAGR_LAND, UNIT_MEASURE HA (Hectares × Thousands).
