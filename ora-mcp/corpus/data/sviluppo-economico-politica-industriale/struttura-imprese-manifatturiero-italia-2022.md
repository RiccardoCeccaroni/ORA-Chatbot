---
id: struttura-imprese-manifatturiero-italia-2022
type: data
attribution: oecd
quality_tier: D1
title: "Struttura imprenditoriale per classe dimensionale, manifatturiero Italia, 2022"
data_metric: "numero imprese e fatturato (turnover) manifatturiero per classe dimensionale (PMI 1-249 dipendenti vs grandi imprese 250+)"
data_period: "2022 (annuale)"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Structural Business Statistics by size class (ISIC Rev. 4), dataflow DSD_SDBSBSC_ISIC4@DF_SDBS_ISIC4"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 6ecde46e801ad5e5d7dbadf2e3ba35db1961b744ae193091e3af40a23714b4e1
tags: [sviluppo-economico-politica-industriale, innovazione-crescita]
description: "Manifatturiero Italia 2022: 358.488 imprese totali, di cui 99,6% PMI (<250 dip.) e solo 0,4% grandi imprese. Le grandi però producono il 46% del fatturato. Tessuto frammentato — il 'nanismo' imprenditoriale italiano."
---

# Struttura imprenditoriale per classe dimensionale — manifatturiero Italia, 2022

**Numero imprese manifatturiere 2022:** **358.488** totali.

| Classe dimensionale | Numero | Quota | Fatturato (€ mld) | Quota fatturato |
|---|---|---|---|---|
| **PMI (1-249 dipendenti)** | **356.971** | **99,58%** | **675,5** | **53,9%** |
| **Grandi imprese (250+ dipendenti)** | **1.517** | **0,42%** | **578,3** | **46,1%** |
| **Totale** | **358.488** | **100,0%** | **1.253,8** | **100,0%** |

**Punto critico:** in Italia, **lo 0,4% delle imprese manifatturiere produce il 46% del fatturato del settore.** Le PMI (99,6%) producono il 54%.

## Cosa significa il "nanismo imprenditoriale italiano"

Italia è famosa nel dibattito europeo per la **frammentazione del suo tessuto produttivo**: imprese mediamente piccole, poche aziende grandi globalmente competitive.

### Fatturato medio per impresa (2022, manifatturiero)
- **PMI italiana media: €1,89 milioni di fatturato/anno**
- **Grande impresa italiana media: €381 milioni di fatturato/anno**
- **Rapporto Large/PMI: ~200x**

### Confronto internazionale (orientativo)

Quota di grandi imprese (250+ dipendenti) nel manifatturiero, % imprese:
- **Italia 2022:** 0,42%
- **Media UE:** ~0,8%
- **Germania:** ~1,2%
- **Francia:** ~0,7%
- **Spagna:** ~0,4% (simile all'Italia)
- **USA:** ~1,5%

**Italia ha la metà della densità di grandi imprese di Germania.** Spagna è simile (peer mediterraneo).

Quota fatturato grandi imprese sul totale (% fatturato):
- **Italia:** ~46%
- **Germania:** ~65%
- **Francia:** ~58%
- **Spagna:** ~40%

**In Germania le grandi imprese dominano molto di più (65% del fatturato vs 46% italiano)** — riflette le grandi multinazionali tedesche (Siemens, BMW, BASF, ecc.).

## Cause storiche del nanismo italiano

1. **Distretti industriali storici**: l'Italia post-bellica si è sviluppata su distretti di micro-imprese specializzate (Brianza, Marche, Toscana, Veneto). Modello "leggero" ma con poche grandi corporation.

2. **Capitalismo familiare**: il ~70% delle PMI italiane è a controllo familiare. Difficoltà di crescita per:
   - Riluttanza all'apertura del capitale a investitori esterni
   - Successione generazionale problematica
   - Tassazione successioni che disincentiva il consolidamento

3. **Mercato del capitale sotto-sviluppato**: l'Italia ha **poche IPO**, mercato venture capital piccolo, banche poco propense a finanziare crescita per equity.

4. **Soglie regolatorie**: alcune normative italiane scattano oltre 15 dipendenti (Statuto dei Lavoratori), 50 dipendenti (rappresentanza sindacale), 250 (definizione UE PMI). Effetto **"trappole dimensionali"** documentato: imprese restano sotto soglia per evitare costi regolatori.

5. **Bassa internazionalizzazione**: solo il 15-20% delle PMI italiane esporta direttamente; le grandi imprese sono internazionalizzate al 95%+. La crescita richiede internazionalizzazione che le PMI faticano a sostenere.

## Implicazioni di policy

Il nanismo italiano si manifesta in:

- **Produttività media più bassa** rispetto a Germania/USA (vedi card `pil-pro-capite-italia-2024.md`)
- **Bassi investimenti in R&S** per impresa (le micro-imprese non hanno team R&D)
- **Difficoltà di entrare in catene globali del valore** (servono dimensioni minime)
- **Sotto-investimento in digitalizzazione** (manca scala per investimenti tech)
- **Resistenza a riforme** che richiedono massa critica (es. consolidamento bancario, energia)

Proposte politiche ricorrenti su "**Made in Italy 4.0**", "**piano consolidamento PMI**", incentivi a M&A tra PMI, agevolazioni IPO. I risultati sono stati limitati negli ultimi 30 anni — il tessuto cambia lentamente.

## Caveat e note di lettura

- **Dataset limitato al MANIFATTURIERO (codice C ISIC Rev. 4).** Servizi, costruzioni, agricoltura NON inclusi. Italian "nanismo" è ancora più marcato nei servizi (commercio, ristorazione, artigianato).
- **PMI classificazione UE**: 1-249 dipendenti. Sub-categorie (micro <10, piccola 10-49, media 50-249) non disaggregate in questa view.
- **Fatturato in valuta nazionale (€ mln)** — vale a livello aggregato, non per confronti con dati a parità di potere d'acquisto.
- **2022 dato disponibile** — versioni più recenti (2023, 2024) potrebbero esistere ma non in questo export.
- **Distribuzione territoriale**: PMI italiane concentrate al Nord-Est e Centro (Veneto, Emilia, Marche, Toscana). Le grandi imprese tendono al Nord-Ovest (Lombardia, Piemonte). Sud relativamente povero di tessuto produttivo strutturato.
- **Imprese individuali (ditte individuali)** generalmente INCLUSE nel conteggio se rilevate come "enterprises" (definizione statistica OECD). Lavoratori autonomi puri (P.IVA senza dipendenti) sono inclusi parzialmente.

## Sorgente raw

`_raw/sviluppo-economico-politica-industriale/DF_SDBS_ISIC4/OECD.SDD.TPS,DSD_SDBSBSC_ISIC4@DF_SDBS_ISIC4,1.0+A..ENTR+TUTT.C._T+S1T249+S_GE250..csv`
