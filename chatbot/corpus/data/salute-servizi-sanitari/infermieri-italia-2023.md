---
id: infermieri-italia-2023
type: data
attribution: oecd
quality_tier: D1
title: "Infermieri praticanti per 1000 abitanti, Italia, 2023"
data_metric: "infermieri praticanti (status: P = Practising) per 1000 abitanti"
data_period: "2023; serie 2015-2023"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Nurses, dataflow DSD_HEALTH_REAC_EMP@DF_NURSE"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: fc815f587ff8ecc53f4af15558801c0c3daa7a316c87f8eb3cef7fcde4671d9f
tags: [salute-servizi-sanitari]
description: "Infermieri praticanti per 1000 abitanti in Italia: 6,86 nel 2023, in crescita lenta dal 5,49 del 2015 ma strutturalmente sotto la media OCSE (~10 per 1000)."
---

# Infermieri praticanti per 1000 abitanti, Italia, 2023

**Valore (2023):** **6,86 infermieri praticanti per 1000 abitanti**.
**Crescita 2015 → 2023:** +1,37 punti (+25%).
**Posizione internazionale:** **strutturalmente sotto la media OCSE**.

## Serie storica

| Anno | Per 1000 abitanti | YoY |
|---|---|---|
| 2015 | 5,49 | — |
| 2016 | 5,61 | +0,12 |
| 2017 | 5,85 | +0,24 |
| 2018 | 5,77 | -0,08 |
| 2019 | 6,16 | +0,39 |
| 2020 | 6,28 | +0,12 |
| 2021 | 6,80 | +0,52 ← spinta post-Covid |
| 2022 | 6,81 | +0,01 (stagnazione) |
| **2023** | **6,86** | **+0,05** |

La **crescita reale è piuttosto lenta** (~0,17 punti/anno in media). Il salto 2020 → 2021 (+0,52) riflette in parte una **revisione contabile** e in parte gli ingressi straordinari post-Covid (concorsi pubblici, assunzioni emergenza pandemia).

## Confronto internazionale — verificato OECD/EU Health Profile 2025

- **Italia 2023: 6,9 per 1000** abitanti
- **Media UE 2023: 8,4 per 1000**
- **Italia è ~20% SOTTO la media UE**

**Rapporto infermieri/medici Italia 2023: 1,3** — **uno dei più bassi dell'UE** (vs media UE attesa ~2,5-3).

## Retribuzione — il fattore politico critico

Il PDF è esplicito sul nodo retributivo:

> *"Mentre nella maggior parte dei Paesi UE gli infermieri guadagnano circa il 20% in più rispetto al salario medio nazionale, gli infermieri italiani sono retribuiti più o meno alla pari."*

→ L'Italia ha una **anomalia retributiva strutturale**: l'infermieristica italiana NON guadagna il premio salariale (+20% sopra salario medio) tipico delle controparti europee. Riflette il sistema contrattuale del comparto sanità pubblica italiano.

## Calo della pipeline formativa

- **Dal picco 2013, laureati in infermieristica italiani in calo > 3% annuo (2013-2022)**
- **Tra 2020 e 2022, numero di nuovi infermieri laureati < numero di medici laureati** (sproporzione anomala — nella maggior parte dei Paesi UE i nuovi infermieri sono multipli dei nuovi medici)
- **2023: lieve ripresa** — laureati infermieri tornano superiori ai medici. Segnale incoraggiante ma non sufficiente a chiudere il gap.
- Dal 2020 il numero annuo di laureati infermieri italiani è **sceso a meno della metà della media UE**
- Rapporto candidati/posti ai corsi di laurea **quasi 1:1** — selezione competitiva eliminata di fatto

**31 professioni sanitarie legalmente riconosciute in Italia** — frammentazione che limita l'interoperabilità e complica la pianificazione coordinata della forza lavoro.

## Rapporto medici/infermieri

In Italia 2023: **6,86 infermieri / 5,35 medici ≈ 1,28 infermieri per medico**.

Il rapporto OCSE atteso è **~2,5-3 infermieri per medico** (Norvegia 4, Germania 2,7, Francia 2,5). **L'Italia ha uno squilibrio strutturale** verso i medici. Ne risulta:

- carichi infermieristici elevati (ratio paziente/infermiere alti)
- medici impegnati in attività che altrove sono delegate al personale infermieristico (educazione paziente, somministrazioni)
- elevato burnout della categoria infermieristica

## Definizione "Practising"

Lo status **P (Practising)** rappresenta **infermieri che effettivamente esercitano** la professione clinica (anche part-time). **Esclude:**

- infermieri laureati ma non praticanti
- infermieri "professionally active" non-clinici (amministrazione, formazione, ricerca)
- studenti in formazione
- OSS (Operatori Socio-Sanitari) — categoria distinta nel CCNL italiano, non rientra qui

**Include:** infermieri ospedalieri, territoriali, RSA, ambulatoriali, di emergenza, pediatrici, ostetriche di sala (di solito), infermieri di studio MMG.

## Caveat e note di lettura

- **Forte sotto-dotazione strutturale** rispetto ai pari europei. È il principale punto di vulnerabilità del SSN italiano sui dati comparativi.
- **Maldistribuzione territoriale:** Nord 7,5-8 per 1000, Sud 5,5-6 per 1000 (ISTAT, non in questo batch).
- **Età media elevata:** la categoria infermieristica italiana ha età media ~47-48 anni (FNOPI); con curva pensionistica in arrivo, sostituzioni inadeguate.
- **Trend in lieve crescita** — non sufficiente a chiudere il gap OCSE nel medio termine. Servirebbe raddoppiare le iscrizioni alle facoltà di Scienze Infermieristiche e aumentare la retribuzione (attualmente l'Italia è tra i Paesi UE con stipendi infermieristici reali più bassi).
- **Infermieri stranieri (~5% del totale):** vedi card `personale-straniero-sanitario-italia-2024.md`.

## Sorgente raw

`_raw/salute-servizi-sanitari/DF_NURSE/OECD.ELS.HD,DSD_HEALTH_REAC_EMP@DF_NURSE,1.1+..PS+10P3HB...MINU..P..csv`
