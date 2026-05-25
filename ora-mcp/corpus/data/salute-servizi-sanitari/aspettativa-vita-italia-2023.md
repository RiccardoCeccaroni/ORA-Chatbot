---
id: aspettativa-vita-italia-2023
type: data
attribution: oecd
quality_tier: D1
title: "Aspettativa di vita alla nascita, Italia, 2023"
data_metric: "aspettativa di vita alla nascita (totale, maschi, femmine) in anni"
data_period: "2023; serie 2015-2023"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Life expectancy, dataflow DSD_HEALTH_STAT@DF_LE"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: b4e8cf0e32078846ff13aec477e23da0d3b839ceede4d3bd1b3f27bd838e3ebe
tags: [salute-servizi-sanitari]
description: "Aspettativa di vita alla nascita in Italia (2023): 83,5 anni totale, 85,4 femmine, 81,4 maschi — tra le più alte al mondo."
---

# Aspettativa di vita alla nascita, Italia, 2023

**Valore (2023):**
- **Totale: 83,5 anni**
- **Femmine: 85,4 anni**
- **Maschi: 81,4 anni**

Il **gap di genere è di 4,0 anni** a favore delle donne — coerente con il pattern osservato in tutti i Paesi OCSE ad alto reddito.

## Serie storica

| Anno | Totale | Maschi | Femmine | Note |
|---|---|---|---|---|
| 2015 | 82,7 | 80,3 | 84,9 | |
| 2016 | 83,4 | 81,0 | 85,6 | |
| 2017 | 83,1 | 80,8 | 85,2 | |
| 2018 | 83,4 | 81,2 | 85,6 | |
| **2019** | **83,6** | 81,4 | 85,7 | picco pre-Covid |
| **2020** | **82,3** | 80,0 | 84,5 | **dip Covid: -1,3 anni** |
| 2021 | 82,7 | 80,5 | 84,9 | recupero parziale |
| 2022 | 82,8 | 80,7 | 84,8 | |
| **2023** | **83,5** | 81,4 | 85,4 | recupero quasi completo del picco 2019 |

Il **dip Covid-19 (2020)** ha azzerato circa **10 anni di guadagni** nell'aspettativa di vita italiana. Il recupero post-pandemico è stato più lento per la fascia maschile.

## Aggiornamento 2024 — verificato OECD/EU Health Profile 2025

**Aspettativa di vita Italia 2024: 84,1 anni** (totale) — **nuovo record storico**, +0,6 anni vs 2023, **+6 mesi sopra il livello pre-pandemia 2019**. Italia è **il Paese con l'aspettativa di vita più alta dell'Unione Europea, alla pari con la Svezia**, **+2,5 anni sopra la media UE**.

**Confronto verificato 2024 (PDF Eurostat demo_mlexpec):**
- **Uomini italiani:** quasi **+3 anni** di vita attesa rispetto agli uomini UE medi
- **Donne italiane:** **+1,6 anni** rispetto alle donne UE medie
- **Gender gap Italia 2024: 4,0 anni** — **significativamente inferiore alla media UE di 5,2 anni** (Italia ha un divario uomo/donna più contenuto)

**Crescita di lungo periodo (2004-2024):**
- Italia: **+3,2 anni** in 20 anni
- UE: poco più di +3,2 anni (Italia in linea con UE nonostante partisse da un livello già elevato)

Il vantaggio italiano è in parte attribuito alla **dieta mediterranea**, all'**accesso universale al SSN** (vedi card `copertura-sanitaria-universale-italia-2024.md`), e a fattori genetico-comportamentali.

⚠️ **Nota:** il valore 84,1 (2024) viene dal report OECD/EU Profile 2025 (basato su Eurostat). Il nostro raw CSV DF_LE arriva fino al 2023 (83,5 totale); il valore 2024 è citato dal PDF e non è ancora nel nostro raw OECD. Il bot dovrebbe usare 84,1 per il 2024 e segnalare la fonte (Profilo della sanità 2025).

## Cosa misura (definizione)

L'aspettativa di vita alla nascita è il **numero medio di anni che vivrebbe una persona nata oggi** se fosse soggetta per tutta la vita ai tassi di mortalità per età osservati nell'anno di riferimento. Non è una previsione individuale: è una **misura sintetica della mortalità** all'anno X.

Le tavole di mortalità OCSE sono armonizzate; per l'Italia derivano da ISTAT (registrazioni dei decessi per anno × età × sesso) e sono di **alta qualità statistica**.

## Caveat e note di lettura

- L'aspettativa di vita misura **quantità**, non qualità. **Healthy life expectancy** (anni vissuti in buona salute) è significativamente più bassa: per l'Italia ~67 anni totali (riferimento OCSE/EU, da verificare con web search), con un gap di ~16 anni tra vita totale e vita "in salute".
- **Disparità territoriali interne all'Italia:** Nord-Sud gap di ~2 anni (Trentino-Alto Adige ~84, Campania ~81,5 — riferimento ISTAT, non in questo batch).
- L'aumento è **rallentato dal 2015**: la curva si appiattisce, segno che i guadagni "facili" (mortalità infantile, malattie cardiovascolari acute) sono già stati realizzati. I prossimi guadagni richiederanno interventi su cronicità e demenze.
- Da ricordare politicamente: alta aspettativa di vita = **pressione strutturale sui sistemi pensionistico e sanitario**. Le riforme della spesa pubblica devono partire da questo dato.

## Sorgente raw

`_raw/salute-servizi-sanitari/DF_LE/OECD.ELS.HD,DSD_HEALTH_STAT@DF_LE,1.1+.A.LFEXP..Y0.........csv`
