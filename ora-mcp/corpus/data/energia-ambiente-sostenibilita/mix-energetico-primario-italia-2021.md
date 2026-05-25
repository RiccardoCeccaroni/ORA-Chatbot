---
id: mix-energetico-primario-italia-2021
type: data
attribution: iea
quality_tier: D1
title: "Mix energetico primario (TES) per fonte, Italia, 2021"
data_metric: "Quote percentuali delle fonti energetiche nella Total Energy Supply (TES); dipendenza da import; intensità energetica TES/PIL"
data_period: "2021; serie 2005-2021"
source_url: "https://www.iea.org/reports/italy-2023"
source_doc: "IEA — Italy 2023 Energy Policy Review (in-depth peer review, 2023)"
date_published: "2023"
date_scraped: "2026-05-12"
content_hash: 56def06cf57317ebfc6315949670bcb8bff2953a63d6f76ea6ad13f30f41f38a
tags: [energia-ambiente-sostenibilita, sviluppo-economico-politica-industriale, esteri-relazioni-internazionali]
description: "Composizione della Total Energy Supply italiana 2021: gas 42%, petrolio 33%, rinnovabili 19%, carbone 3,7%. Italia importa l'80% della propria energia primaria."
---

# Mix energetico primario (TES) per fonte, Italia, 2021

**Quote delle fonti nella Total Energy Supply (TES), 2021:**

| Fonte | Quota TES 2021 |
|---|---|
| Gas naturale | **42%** |
| Petrolio | **33%** |
| Rinnovabili (idro + solare + eolico + bioenergia + geotermico) | **19%** |
| Carbone | **3,7%** |
| Importazioni nette di elettricità | residuo (~2-3%) |

**Quota fossile totale:** 78% (gas + petrolio + carbone), in calo dal **90% del 2005**.

**Bioenergia e rifiuti** sono la principale fonte rinnovabile: 38% della produzione domestica e **10% della TES nel 2020**.

## Dipendenza dall'import

L'Italia è un **importatore netto di energia primaria**. Tra il 2016 e il 2021 ha importato in media **l'80% della propria TES**, prevalentemente petrolio e gas. La produzione domestica è composta principalmente da fonti rinnovabili (idro, solare, eolico, bioenergia), che rappresentano il **74% della produzione interna 2021**. La produzione di petrolio e gas naturale è limitata.

## Intensità energetica dell'economia

**Variazione TES 2005-2021:** −20% complessivo. Gran parte del calo avviene tra 2005 e 2014 per la contrazione prolungata del PIL e lo spostamento verso settori meno energivori. La TES si stabilizza dopo il 2014, scende del 7,7% nel 2020 (Covid) e rimbalza del +8,7% nel 2021.

**Intensità energetica (TES/PIL):**
- Italia: **−17% tra 2005 e 2021**
- Media paesi IEA: −23% nello stesso periodo

L'intensità energetica italiana è **relativamente bassa** rispetto a molti paesi IEA in livello, ma il **ritmo di miglioramento è più lento della media IEA**.

## Consumo finale (TFC) per settore, 2021

- **Edifici:** ~40% TFC (settore più energivoro dal 2008; gas naturale copre >50% degli usi negli edifici)
- **Trasporti:** ~30% TFC (petrolio copre l'89% degli usi nel trasporto)
- **Industria:** ~30% TFC (elettricità, petrolio e gas in quote simili)
- **Elettricità su TFC:** ~21,5% (sotto la media IEA del 23%) → margine ampio per l'elettrificazione degli usi finali

## Caveat e note di lettura

- I dati IEA 2021 sono i più recenti coerenti tra TES e TFC nel report; per il TFC alcune voci si riferiscono al 2020 (annotato esplicitamente da IEA nella Fig. 2.1).
- TES = Total Energy Supply (energia primaria interna lorda); TFC = Total Final Consumption (consumo finale).
- La quota fossile italiana del 78% è in linea con la media IEA. Il primato di criticità non è il livello fossile in sé, ma la **composizione**: forte dipendenza dal gas naturale (vedi card `dipendenza-energetica-russia-italia-2021`).
- Dato fermo al 2021: il post-2022 (shock prezzi, taglio import russi, boom solare 2023-24) NON è coperto. Per dati più recenti consultare la pagina IEA Country Profile (`iea.org/countries/italy`) o aggiornamenti Eurostat/Terna.
- IEA è D1 per autorevolezza ma usa definizioni proprie diverse da Eurostat: per la quota rinnovabili nei consumi finali (target UE) usare la definizione Eurostat (vedi card `quota-rinnovabili-italia-2021`).

## Sorgente raw

`_raw/energia-ambiente-sostenibilita/IEA_2023_REVIEW/Italy_2023_Energy_Policy_Review.pdf` — capitolo 2 "General energy policy", sezione "Energy supply and demand", Figure 2.1 e 2.2.
