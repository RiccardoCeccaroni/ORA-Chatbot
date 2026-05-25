---
id: popolazione-titolo-studio-25-64-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Popolazione italiana 25-64 anni per titolo di studio, 2024"
data_metric: "Quota % della popolazione 25-64 con almeno il diploma di scuola secondaria superiore (ISCED 3+); quota % della popolazione 25-39 con istruzione terziaria (ISCED 5-8). Framework EU LFS post-2020 (Regolamento UE 2019/1700)"
data_period: "2024"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500BES,1.0/BES_TERR/IST/DCSC_BES_TERRIT/IT1,DF_BES_TERRIT_2,1.0"
source_doc: "ISTAT — BES (Benessere Equo e Sostenibile) at local level, dataflow DF_BES_TERRIT_2 (Education and training), indicatori 02IST002-N22 (25-64) e 02IST003P-N22 (25-39)"
date_published: "2025"
date_scraped: "2026-05-13"
content_hash: 4423f73ce372500ed6612404a7f333a118ee4bac828035f444a477910b399ff6
tags: [istruzione, lavoro-politiche-sociali]
description: "Italia 2024 — 66,7% della popolazione 25-64 ha almeno il diploma (ISTAT BES). Il 30,9% dei 25-39enni ha completato l'istruzione terziaria. Nord 71% diploma+ vs Sud 60%. Per la stessa metrica in framework OCSE vedi card OECD parallela."
---

# Popolazione italiana 25-64 per titolo di studio, 2024

> ℹ️ **Cambio di framework metodologico.** Dal 2021 la rilevazione ISTAT ha adottato il Regolamento UE 2019/1700 sulle Forze di Lavoro. La metodologia post-2020 si concentra sul perimetro 25-64 (allineato a OCSE e Eurostat) e non più sull'aggregato demografico 15+ utilizzato dal vecchio dataflow `DCCV_POPTIT1_UNT2020`. Questa card sostituisce la precedente `popolazione-titolo-studio-italia-2020.md` (perimetro 15+), rimossa nel refresh content del 2026-05-13.
>
> Per la stessa metrica letta col framework OCSE Education at a Glance (criteri ISCED leggermente diversi) vedi [[titolo-studio-adulti-25-64-italia-2024]].

## Headline 2024

| Indicatore | Italia 2024 |
|---|---|
| **Popolazione 25-64 con ALMENO il diploma** (ISCED ≥ 3) | **66,7%** |
| **Popolazione 25-39 con istruzione terziaria** (ISCED 5-8) | **30,9%** |
| Popolazione 25-64 con istruzione terziaria (cfr. card OECD EAG) | **22,3%** (fonte OCSE) |
| Quota NEET 15-29 anni | 15,2% |

**Per il primo anno dopo la pandemia, due terzi della popolazione adulta italiana ha almeno il diploma.** Il 66,7% del 2024 rappresenta un balzo significativo dal 62,6% del 2020 (+4,1 p.p. in 4 anni), riflesso del ricambio generazionale.

## Trend 2020-2024 (Italia, sex=Totale)

| Anno | ≥ Diploma (25-64) | Tertiary 25-39 | NEET 15-29 |
|---|---|---|---|
| 2020 | 62,6% | 28,2% | 23,3% |
| 2021 | 62,7% | 28,1% | 23,1% |
| 2022 | 63,0% | 28,6% | 19,0% |
| 2023 | 65,5% | 30,0% | 16,1% |
| **2024** | **66,7%** | **30,9%** | **15,2%** |

**Triplo movimento favorevole:** la quota diplomati cresce, la quota laureati tra i giovani cresce, la quota NEET cala. Il 2022-2024 mostra il primo miglioramento strutturale post-pandemia.

## Distribuzione territoriale 2024 (NUTS-1, ISTAT BES)

| Area | ≥ Diploma (25-64) | Tertiary 25-39 |
|---|---|---|
| Nord-est | **71,3%** ← più alto | **34,7%** ← più alto |
| Nord-ovest | 69,1% | 33,0% |
| Italia | 66,7% | 30,9% |
| Sud | **60,2%** ← più basso | **26,1%** ← più basso |

**Divario Nord-Sud strutturale:** ~11 punti percentuali di gap su entrambi gli indicatori. Centro e Isole non sono disponibili nel cut BES territoriale.

## Definizione precisa degli indicatori

**02IST002-N22 — Persone con almeno il diploma di scuola secondaria superiore, 25-64.**
- Numeratore: 25-64enni con livello di istruzione ISCED ≥ 3.
- Denominatore: tutti i 25-64enni.
- Allineato all'indicatore Eurostat `tps00065`.

**02IST003P-N22 — Persone con istruzione terziaria, 25-39.**
- Numeratore: 25-39enni con ISCED 5-8 (terziaria breve + triennale + magistrale + dottorato).
- Denominatore: tutti i 25-39enni.
- **NOTA: perimetro 25-39 (non 25-64).** ISTAT BES traccia il tasso di laurea nella fascia 25-39 per cogliere la cohort più recente. Per il dato 25-64 (allineato OCSE) vedi [[titolo-studio-adulti-25-64-italia-2024]] (22,3% nel 2024).

**02IST006-N22 — Quota NEET 15-29 anni.**
- Numeratore: 15-29enni non occupati e non in istruzione/formazione.
- Denominatore: tutti i 15-29enni.

Fonte ISTAT: **Rilevazione sulle Forze di Lavoro (RFL)** post-2020 (Regolamento UE 2019/1700).

## Confronto framework ISTAT BES vs OCSE Education at a Glance

| Indicatore | ISTAT BES 2024 | OCSE EAG 2024 | Δ |
|---|---|---|---|
| Almeno diploma 25-64 | 66,7% | 66,7% (100% − 33,3% below upper sec) | 0 |
| Terziaria 25-64 | (non pubblicato direttamente) | 22,3% | — |
| Terziaria 25-39 (giovani) | 30,9% | ~32% | ~1 p.p. |

I due framework concordano sulla quota "almeno diploma" 25-64 (66,7% in entrambi) ma divergono leggermente sulla terziaria 25-39 — l'OCSE include alcune qualifiche ITS/specializzazioni post-diploma con codifiche ISCED 5 che ISTAT BES tratta come post-diploma non terziario. La differenza è ~1 punto percentuale, trascurabile per la maggior parte degli usi.

## Caveat e note di lettura

- **Perimetro 25-64 vs 25-39.** Il framework BES separa intenzionalmente i due perimetri. 25-64 cattura lo stock cumulato della popolazione adulta (informativo su capitale umano corrente); 25-39 cattura la cohort recente (informativo sulla pipeline di nuovi laureati). I due numeri non vanno confrontati direttamente — il 30,9% (25-39) non è "la quota di laureati 25-64".
- **No M/F breakdown nel cut BES territoriale.** ISTAT pubblica i breakdown di genere a livello Italia ma non a livello macroarea nel dataflow DF_BES_TERRIT_2. Per genere x territorio serve un'estrazione dalla RFL diretta.
- **Centro e Isole assenti nel cut BES territoriale 2024 (NUTS-1).** Solo Nord-ovest, Nord-est, Sud sono pubblicati per indicatori dell'istruzione nella view territoriale BES. Per i dati di Lazio + Toscana + Marche + Umbria + Sicilia + Sardegna serve `DF_BES_TERRIT_2` con query a livello NUTS-2 regionale (disponibile).
- **Confronto col 2020 (legacy framework).** Il valore 2020 ISTAT BES (62,6% diploma+) NON è direttamente comparabile col valore 2020 della precedente card storica `popolazione-titolo-studio-italia-2020.md` (riferita al perimetro 15+ × cittadinanza, in cui ~35% della popolazione 15+ aveva almeno il diploma e ~15% la laurea). I due framework usano denominatori diversi (15+ vs 25-64) e ISCED-mapping diversi.
- **Convergenza generazionale lenta.** Sebbene i 25-39enni abbiano un tasso di laurea del 30,9% nel 2024 (in crescita), per portare l'aggregato 25-64 al livello OCSE serviranno 15-20 anni di ricambio generazionale.

## ORA — perché la cifra è politicamente rilevante

Lo stock educativo della popolazione adulta italiana è uno dei principali colli di bottiglia strutturali italiani:

- **L'Italia resta in fondo alle classifiche OCSE** per quota laureati 25-64 (22,3%, **penultima posizione OCSE**) — il 30,9% dei 25-39 mostra che la cohort giovane è in recupero, ma la massa 25-64 cambia lentamente.
- Il **divario territoriale** Nord (71%) vs Sud (60%) sul diploma è uno dei principali drivers del gap di produttività e occupazione regionale.
- Il **NEET 15-29 (15,2%) in calo dal 23,3% del 2020** è un successo significativo del PNRR Garanzia Giovani e dell'espansione delle politiche di formazione professionale.
- Il numero ridotto di laureati 25-64 incide su produttività, salari, capacità di innovazione, **brain drain** (emigrazione di laureati italiani all'estero — vedi card relative).

## Sorgente raw

`_raw/istruzione/DF_BES_TERRIT_2/data.csv` — 6.677 righe, BES Education and Training framework, 9 indicatori × 117 territori × serie 2020-2024 × edition 2025.

Indicatori utilizzati:
- `02IST002-N22` — At least upper secondary (25-64)
- `02IST003P-N22` — Tertiary (25-39)
- `02IST006-N22` — NEET (15-29)

Dataflow ISTAT `IT1:DF_BES_TERRIT_2(1.0)`, edizione 2025. Estratto via SDMX API con `Accept: application/vnd.sdmx.data+csv;version=1.0.0;labels=both`.

**Card storica:** `popolazione-titolo-studio-italia-2020.md` (legacy 15+ × cittadinanza, regolamento pre-2020) — **rimossa nel refresh content 2026-05-13** per evitare duplicazione metodologica con questa card; consultare lo storico via git history se serve il dato 15+.
**Card complementare OCSE:** [[titolo-studio-adulti-25-64-italia-2024]] (perimetro 25-64 con framework EAG, mostra Italia 22,3% terziaria — penultima OCSE).
