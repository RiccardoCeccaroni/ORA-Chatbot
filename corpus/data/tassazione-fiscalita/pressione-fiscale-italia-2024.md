---
id: pressione-fiscale-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Pressione fiscale della Pubblica Amministrazione, Italia, 2024"
data_metric: "pressione fiscale delle Amministrazioni Pubbliche rispetto al PIL (entrate fiscali totali AAPP / PIL ai prezzi di mercato)"
data_period: "2024 (annuale, derivato come media dei 4 trimestri); serie quarterly 2023-Q1 / 2025-Q4"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — Conti economici trimestrali delle Amministrazioni Pubbliche, dataflow DCCN_FPQ (indicatore TB_R_GDP)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 6f6a9b74cc182c8f340c36a3d11de5ef08d634989d9dd6003b9af4bfba7c2d4a
tags: [tassazione-fiscalita, spesa-pubblica]
description: "Pressione fiscale Italia 2024: circa 42,2% del PIL (media dei 4 trimestri); con €937 mld di entrate fiscali AAPP su PIL di €2.202 mld. Trend in lieve crescita 2023→2025 (41,0 → 42,8%)."
---

# Pressione fiscale della Pubblica Amministrazione, Italia, 2024

**Valore annuale 2024 (media aritmetica dei 4 trimestri):** **circa 42,2% del PIL**.
**Cross-check OECD:** gettito totale tasse 2024 (€940,4 mld incl. tasse riscosse per UE) / PIL 2024 (€2.202 mld) = **42,7%**.
**Definizione ufficiale ISTAT:** la pressione fiscale è il rapporto tra **entrate tributarie + contributi sociali effettivi** della Pubblica Amministrazione e il **PIL ai prezzi di mercato**.

## Serie storica — pressione fiscale trimestrale (TB_R_GDP)

| Trimestre | 2023 | 2024 | 2025 |
|---|---|---|---|
| Q1 | 35,6% | 36,5% | 37,3% |
| Q2 | 40,4% | 41,2% | 42,1% |
| Q3 | 39,3% | 40,3% | 40,5% |
| **Q4** | **48,7%** | **50,6%** | **51,4%** ← picco stagionale |
| **Media annua** | **~41,0%** | **~42,2%** | **~42,8%** |

⚠️ **Forte stagionalità quartertale.** Il Q4 italiano è strutturalmente alto per:
- saldo annuale IVA + acconti
- saldo IRES novembre
- conguaglio IRPEF (acconto + saldo persone fisiche)
- 13a mensilità → contributi previdenziali aggiuntivi

Il **dato annuo va calcolato come somma di entrate trimestrali / somma PIL trimestrale**, non come media aritmetica delle 4 ratios (qui usata come approssimazione).

## Composizione (2024, gettito ~€940 mld dall'OECD Revenue Stats)

| Categoria | Codice OECD | Importo 2024 | Quota del totale |
|---|---|---|---|
| **Contributi sociali** (employer + employee + autonomi) | T_2000 | €274,4 mld | **29,2%** |
| **IRPEF + addizionali** (imposta su redditi persone fisiche) | T_1110 | €258,7 mld | **27,5%** |
| **IVA** (imposta sul valore aggiunto) | T_5111 | €145,2 mld | **15,4%** |
| **Accise + altre imposte su consumi** | T_5120 | €76,0 mld | 8,1% |
| **IRES + altre imposte società** | T_1210 | €58,8 mld | 6,3% |
| **Imposte sulla proprietà** (IMU, registro, ecc.) | T_4000 | €49,5 mld | 5,3% |
| **Altre imposte** | T_6000 | €32,4 mld | 3,4% |

I **contributi sociali** (29,2%) sono la categoria più grande, **superiore all'IRPEF** (27,5%). Insieme rappresentano il **57%** del gettito complessivo.

L'**IVA è la terza voce** (15,4%), poi a distanza le accise e l'IRES. Le **imposte sulla proprietà** (5,3%) sono storicamente sotto la media UE.

## Confronto internazionale (orientativo)

- **Media UE-27 2023:** ~41,0% del PIL
- **Italia 2023:** ~41,0% — circa **in linea con la media UE**
- **Francia 2023:** ~46,0% (massimo UE)
- **Germania 2023:** ~41,5%
- **Spagna 2023:** ~38,5%
- **Irlanda 2023:** ~22,5% (minimo UE, distorto da società estere)

L'Italia è **stabilmente in linea con la media UE**, sopra Spagna/Portogallo ma sotto Francia, Belgio, Austria, Danimarca, Svezia. Il narrativo "Italia super-tassata" deve essere qualificato: a livello aggregato non è vero, ma **la pressione fiscale è distribuita in modo molto ineguale** — alta sul lavoro (cuneo fiscale, vedi card `cuneo-fiscale-italia-2025.md`), bassa su rendite e patrimonio.

## Caveat e note di lettura

- **Dato trimestrale fortemente stagionale.** Non confondere il valore Q4 (51%) con la pressione fiscale annua (~42%).
- **Definizione "AAPP"** = General Government (S13 in SEC2010), include Stato + Regioni + Comuni + enti previdenziali + altri enti pubblici. Esclude imprese pubbliche non finanziarie.
- **Pressione fiscale ≠ aliquote**. Riflette **gettito effettivo / PIL**, quindi cambia con: crescita economica, evasione, agevolazioni, indicizzazione.
- **Italia ha un'evasione fiscale stimata di ~€85-90 mld/anno** (tax gap IVA + altre imposte — fonte MEF NADEF, non in questo dataset). Se l'evasione fosse zero, la pressione fiscale teorica sarebbe ~46-47%.
- **Distribuzione iniqua del carico**: lavoratori dipendenti e pensionati pagano ~70% di IRPEF; autonomi sotto-rappresentati. Riformare questa asimmetria è uno dei temi più dibattuti.
- Il dato 2025 è **provvisorio** (Q4 e annuale soggetti a revisione fino al settembre 2026).

## Sorgente raw

`_raw/spesa-pubblica/DCCN_FPQ/Indicatori (in rapporto al PIL) (IT1,95_42_DF_DCCN_FPQ_2,1.0).csv` (pressione fiscale TB_R_GDP)
`_raw/tassazione-fiscalita/DF_REVITA/OECD.CTP.TPS,DSD_REV_OECD@DF_REVITA,2.1+..S13....A.csv` (composizione gettito)
`_raw/sviluppo-economico-politica-industriale/DCCN_PILN/Prodotto interno lordo e principali componenti (IT1,92_506_DF_DCCN_PILN_1,1.0).csv` (PIL denominatore)
