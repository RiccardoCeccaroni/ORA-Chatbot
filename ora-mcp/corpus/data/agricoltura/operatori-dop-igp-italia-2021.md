---
id: operatori-dop-igp-italia-2021
type: data
attribution: istat
quality_tier: D1
title: "Operatori certificati DOP/IGP/STG (food), Italia, 2021"
data_metric: "Numero di operatori (produttori, trasformatori, confezionatori) certificati per la produzione di prodotti agroalimentari DOP, IGP o STG, per settore merceologico"
data_period: "2021 (singolo anno)"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Operatori DOP IGP STG, dataflow DCSP_DOPIGP_1 (101_1030)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: cf102745422e9077a8d36fd15608fe9e91070621d7f3cd6a85947fd7ccbd2c5c
tags: [agricoltura]
description: "83.471 operatori italiani certificati DOP/IGP/STG (alimentari, esclusi i vini) nel 2021, divisi tra 5 settori: formaggi (24.637), olio extravergine (24.139), ortofrutticoli e cereali (20.861), carni fresche (10.177), preparazioni di carni (3.657). Italia è il #1 in UE per numero di prodotti agroalimentari a denominazione."
---

# Operatori certificati DOP/IGP/STG (food), Italia, 2021

> **Aggiornamento al 2022:** ISTAT ha pubblicato il 5 settembre 2024 lo statistica-report relativo al 2022. Totale 2022 = 83.759 (+0,3%); 81.403 produttori puri (+0,4% sul 2021); 319 prodotti UE riconosciuti (vs 315). Per il dato aggiornato e l'analisi della redistribuzione geografica Nord→Mezzogiorno (2012-2022) vedi [[operatori-dop-igp-italia-2022]]. Questa card resta valida come riferimento di framework concettuale (definizione operatore, settori esclusi, segmento vinicolo, casi UE storici) e per la geografia regionale di base.

**Totale operatori certificati nel comparto agroalimentare italiano (esclusi vini), 2021:** **83.471 operatori**

> **Cosa significa "operatore":** un'azienda agricola, un'industria di trasformazione, un confezionatore o un grossista iscritto a un Consorzio di tutela e abilitato dall'organismo di controllo (es. CSQA, DNV, IFCQ, 3A Parco Tecnologico, ecc.) alla produzione di un alimento con marchio DOP, IGP o STG. Un singolo operatore può lavorare per più denominazioni.

## Composizione per settore merceologico (Italia, 2021)

| Settore (codice) | Operatori | Quota |
|---|---|---|
| **Formaggi** (CHEESE) | **24.637** | 29,5% |
| **Oli extravergine di oliva** (EXTRVIRGOIL) | 24.139 | 28,9% |
| **Ortofrutticoli e cereali** (FRUITVEGCERAL) | 20.861 | 25,0% |
| **Carni fresche** (MEAT) | 10.177 | 12,2% |
| **Preparazioni di carni** (MEATPRODUCTS) | 3.657 | 4,4% |

## Cosa NON include questo dataset

Il dataset ISTAT `DCSP_DOPIGP_1` copre solo **i 5 settori agroalimentari** sopra. **NON include**:

- **Vini DOC/DOCG/DOP/IGT** — registrati separatamente nel database OIV/MIPAAF, con ~280.000 operatori vitivinicoli italiani certificati (ben più del totale food sopra) → vedi [[coltivazioni-italia-2025]] per il dato di produzione
- **Spiriti e liquori** con designazione geografica (Grappa, Limoncello di Capri, ecc.) — registrati nel database UE GIView
- **Aceti, sale, miele, spezie DOP/IGP** — minori per numero di operatori
- **Pasta IGP** (es. Pasta di Gragnano IGP) e **prodotti da forno** — censiti come "FRUITVEGCERAL" in ISTAT ma con copertura parziale

## Italia nel quadro UE delle denominazioni alimentari

L'Italia è **leader UE assoluta per numero di prodotti agroalimentari registrati DOP/IGP/STG**:

| Paese | Prodotti DOP/IGP/STG registrati (food, 2024) |
|---|---|
| **Italia** | **~330** (di cui ~180 DOP food, ~140 IGP food, ~3 STG) |
| Francia | ~270 |
| Spagna | ~210 |
| Portogallo | ~190 |
| Grecia | ~115 |
| Germania | ~95 |

Per **valore economico aggregato** della filiera DOP/IGP (food + vino) l'Italia produce ~20 miliardi di euro all'anno (stima ISMEA Qualivita 2024) — il **settore agroalimentare certificato è il 21% del valore della produzione agricola italiana totale** (~94 miliardi VA agricoltura ISTAT 2024).

## Distribuzione regionale (drill-down disponibile nel raw)

Il dataset contiene anche la disaggregazione **regionale** e per **zona altimetrica** (montagna/collina/pianura), oltre alla disaggregazione per **sesso** dell'operatore (per la sotto-categoria di operatori individuali). Esempio Sardegna 2021:

- Carni fresche: ~150 operatori
- Preparazioni di carni: ~30 operatori
- Formaggi: 10.333 operatori (Sardegna #1 in Italia per formaggi DOP/IGP grazie al Pecorino Romano DOP, Pecorino Sardo DOP, Fiore Sardo DOP)
- Ortofrutticoli e cereali: 31 operatori
- Olio extravergine: 89 operatori

La distribuzione regionale rispecchia la geografia delle denominazioni:
- **Nord (Emilia-Romagna, Lombardia, Veneto, Friuli-VG)** — concentra Parmigiano Reggiano, Grana Padano, Prosciutto di Parma e San Daniele, Aceto Balsamico di Modena
- **Centro (Toscana, Lazio, Marche, Abruzzo)** — Pecorino Toscano e Romano, Olio Toscano IGP, salumi DOP/IGP
- **Sud + Isole** — Mozzarella di Bufala Campana, Pecorino Sardo, Olio Sicilia, Bergamotto di Reggio Calabria, agrumi IGP

## Trend dell'operatorialità DOP/IGP (riferimenti esterni)

Il dataset disponibile copre solo il 2021. Riferimenti ISMEA Qualivita per il trend:

- **2014 → 2021:** crescita degli operatori certificati da ~78.000 a ~83.500 (+7% in 7 anni)
- **2021 → 2023 (stima):** stabilità o lieve crescita, in particolare nei settori formaggio e olio
- **Lato fatturato:** crescita più rapida del numero di operatori (in particolare nell'export — ~10 miliardi di euro export agroalimentare DOP/IGP nel 2024 secondo ISMEA)

## Caveat e note di lettura

- **2021 è un dato vecchio di 4-5 anni.** ISTAT non aggiorna sistematicamente questo dataflow ogni anno. Per le statistiche più aggiornate (e copertura completa inclusi vini, spiriti, ecc.) la fonte autoritativa è il **rapporto annuale ISMEA-Qualivita** (PDF, settembre/ottobre di ogni anno).
- **Doppi conteggi inter-settoriali.** Un operatore che produce sia carne che formaggio è contato in entrambi i settori. Il totale 83.471 è **somma settoriale**, non numero di aziende distinte.
- **Confronto con il fatturato non possibile da questo dataset.** Per il valore generato dalle denominazioni serve incrociare con il database ISMEA-Qualivita (PDF, da ingerire come D2).
- **"Operatore" è una nozione legale**, non economica: un operatore certificato può essere un piccolo agriturismo che vende 100 bottiglie di olio EVO IGP all'anno o un'industria che ne vende milioni. La distribuzione del numero di operatori **non riflette la concentrazione produttiva** (che è più alta).

## Lettura politica

**Significato politico del numero 83.471 (+ ~280k vini):**

1. **Italia è il "Paese delle eccellenze certificate".** Il sistema DOP/IGP è un'**asset strategico** del Made in Italy alimentare. Il governo italiano (di qualunque colore) lo difende sistematicamente nei negoziati UE.

2. **Difesa attiva nei fori internazionali.** Casi noti recenti:
   - **2024 — Feta vs Danimarca**: vittoria della Grecia (sostenuta dall'Italia) sulla esclusività della denominazione.
   - **2023 — Prosek/Prosecco**: vittoria italiana contro la Croazia.
   - **2022 — TTIP/CETA**: clausole specifiche sulle DOP/IGP italiane.
   - **In corso — Nutri-Score**: l'Italia si oppone al sistema francese di etichettatura nutrizionale a colori perché penalizza Parmigiano, prosciutto, olio (bollino rosso), nonostante siano alimenti tradizionali.
   - **2023-25 — Italian sounding USA**: la lotta contro "Parmesan", "Romano", "Asiago" prodotti negli Stati Uniti continua negli accordi bilaterali UE-USA.

3. **Stretto legame con la zootecnia (vedi [[zootecnia-bestiame-italia-2024]] e [[produzione-latte-formaggio-italia-2025]]).** Senza patrimonio bovino italiano, senza suini pesanti italiani, senza ovini sardi → il sistema DOP perde la materia prima. **La contrazione del patrimonio bovino italiano del -11% in 4 anni è un rischio strategico per il sistema DOP**.

4. **Asset di marketing all'export.** Le 330+ designazioni alimentari italiane sono il principale **veicolo di branding** dell'agroalimentare italiano all'estero (~50 mld € export agroalimentare 2024, di cui ~10 mld DOP/IGP).

5. **Tema sensibile per ORA**: bilanciare tra:
   - **Protezione storica delle DOP/IGP** (politica strutturale italiana, da preservare)
   - **Apertura a innovazione di prodotto** (es. alimenti senza glutine, alimenti funzionali, prodotti certificati biologici-vegani che non hanno DOP equivalente)
   - **Sostenibilità del modello** (le DOP richiedono filiere lunghe, allevamenti locali, vincoli stretti — sono compatibili con la transizione ecologica? Le emissioni di un kg di Parmigiano sono ~10 kg CO2eq, quelle di un kg di pasta sono ~1 kg CO2eq)

## Sorgente raw

`_raw/agricoltura/DCSP_DOPIGP_1/Operatori per settore (IT1,101_1030_DF_DCSP_DOPIGP_1,1.0).csv`

Dataset: ISTAT `DCSP_DOPIGP_1` (101_1030) — Operatori nel comparto dei prodotti DOP/IGP/STG. 119 righe, Italia + regioni + zona altimetrica × sesso, anno 2021. Indicatore OPERATORS_PDOPGITSG "Operatori nel comparto dei prodotti Dop Igp Stg", 5 settori (CHEESE, EXTRVIRGOIL, FRUITVEGCERAL, MEAT, MEATPRODUCTS).
