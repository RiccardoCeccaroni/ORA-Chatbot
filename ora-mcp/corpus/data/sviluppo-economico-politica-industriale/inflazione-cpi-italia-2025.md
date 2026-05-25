---
id: inflazione-cpi-italia-2025
type: data
attribution: oecd
quality_tier: D1
title: "Tasso di inflazione (CPI), Italia, 2025-2026"
data_metric: "indice dei prezzi al consumo — tasso di crescita anno su anno (year-over-year growth rate, %) — totale (_T) COICOP 2018"
data_period: "Aprile 2025 — Marzo 2026 (mensile); serie più ampia disponibile"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Consumer price indices (CPIs, HICPs), COICOP 2018, dataflow DSD_PRICES_COICOP2018@DF_PRICES_C2018_ALL"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 398f07bc312fab4195aa24e6241146abb1c49fe9f78b746cc6165c7ea598d797
tags: [sviluppo-economico-politica-industriale, lavoro-politiche-sociali]
description: "Inflazione Italia: 1,68% a marzo 2026 (CPI YoY), in calo dal picco 12% del 2022. Periodo di disinflazione ai limiti del target BCE 2%."
---

# Tasso di inflazione (CPI), Italia, 2025-2026

**Valore più recente (marzo 2026):** **+1,68% YoY** (variazione anno su anno dell'indice CPI totale).
**Dato gennaio 2026:** +0,98% — **sotto il target BCE 2%** per la prima volta da mesi.
**Picco storico recente:** **+12% nel ottobre 2022** — Italia tra i Paesi UE più colpiti dallo shock energetico.

## Serie storica recente (CPI totale Italia, YoY %)

| Mese | YoY | Note |
|---|---|---|
| Apr 2025 | 1,91% | |
| Mag 2025 | 1,58% | |
| Giu 2025 | 1,66% | |
| Lug 2025 | 1,65% | |
| Ago 2025 | 1,57% | |
| Set 2025 | 1,57% | |
| Ott 2025 | 1,24% | discesa |
| Nov 2025 | 1,07% | |
| Dic 2025 | 1,16% | |
| **Gen 2026** | **0,98%** | sotto 2% BCE |
| Feb 2026 | 1,51% | rimbalzo |
| **Mar 2026** | **1,68%** | stabilizzazione |

**Trend 2024-2026:** disinflazione marcata, da ~6% (gennaio 2024) verso il target BCE 2% raggiunto nel 2026.

## Sequenza storica più ampia (riferimento, non in CSV)

Inflazione media annua Italia (riferimento ISTAT):
- 2020: -0,1% (Covid, prezzi compressi)
- 2021: +1,9% (rimbalzo)
- **2022: +8,1%** (shock energetico Ucraina)
- **2023: +5,7%** (ancora elevata)
- 2024: +1,0% (disinflazione rapida)
- 2025: ~+1,5% (stabilizzazione vicino target)

L'**inflazione cumulativa 2020-2025 = ~18%** — un aumento del livello generale dei prezzi che ha eroso significativamente il potere d'acquisto reale, soprattutto per i salari (che hanno recuperato solo ~10% cumulativo nello stesso periodo).

## Cosa misura il CPI

L'**indice dei prezzi al consumo (CPI)** misura la variazione media nel tempo dei prezzi di un paniere di beni e servizi acquistati dalle famiglie. La classificazione **COICOP 2018** raggruppa i consumi in 12 capitoli:

1. Alimentari e bevande analcoliche
2. Bevande alcoliche e tabacco
3. Vestiario e calzature
4. Abitazione, acqua, energia (es. bollette)
5. Mobili, articoli per la casa
6. Servizi sanitari (out-of-pocket)
7. Trasporti (auto + carburanti)
8. Comunicazioni
9. Ricreazione e cultura
10. Istruzione
11. Ristoranti e alberghi
12. Beni e servizi vari

Il valore "_T" (Totale) è il CPI complessivo. Per analisi di contributo per categoria → vedere dataset DF_PRICES_C2018_CONTRIB.

## Confronto internazionale (orientativo)

**Inflazione media UE 2025 (HICP):** ~2,0%
- **Italia 2025: ~1,5%** — sotto media UE
- Germania: ~2,1%
- Francia: ~1,8%
- Spagna: ~2,4%
- Eurozona target BCE: 2%

L'Italia è **leggermente sotto il target BCE** nei mesi recenti, dopo essere stata sopra nel 2022-2023.

## Caveat e note di lettura

- **CPI ≠ HICP.** ISTAT pubblica due indici: NIC (Nazionale Italiano), IPCA (HICP armonizzato UE). Il dato OECD usa HICP per confronti UE.
- **Indice "headline" vs "core":** il dato qui riportato è il **totale** (incluso energia + alimentari volatili). Il **core inflation** (esclude energia + alimentari freschi) è più stabile, di solito 1-2 punti diverso dal totale durante shock energetici.
- **Inflazione media ≠ inflazione percepita.** Il CPI è un paniere medio; chi spende più su voci con inflazione superiore alla media (es. famiglie a basso reddito su alimentari + bollette) percepisce un'inflazione effettiva diversa. ISTAT pubblica anche un "CPI per famiglia tipo".
- **Effetto base:** valori bassi 2024-2026 sono confrontati con valori già alti del 2022-2023 — l'inflazione "tornata bassa" non significa "prezzi tornati indietro". L'**inflazione cumulativa 2020-2025 è ~18%** — questo livello permane.
- **Adeguamenti automatici:** salari pubblici, pensioni, assegni sociali sono indicizzati al CPI con ritardo (~1 anno). Periodi di alta inflazione comportano perdita temporanea di potere d'acquisto reale per chi è indicizzato.

## Sorgente raw

`_raw/sviluppo-economico-politica-industriale/DF_PRICES_C2018_ALL/OECD.SDD.TPS,DSD_PRICES_COICOP2018@DF_PRICES_C2018_ALL,1.0+.M.N.CPI.PA._T.N.GY.csv`
