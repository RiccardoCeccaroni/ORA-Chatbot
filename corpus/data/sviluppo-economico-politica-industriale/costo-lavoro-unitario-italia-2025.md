---
id: costo-lavoro-unitario-italia-2025
type: data
attribution: oecd
quality_tier: D1
title: "Costo del lavoro per unità di prodotto (ULC) e produttività, Italia, 2025"
data_metric: "Unit Labour Costs (ULCE), GDP per occupato (GDPEMP), Labour Compensation per dipendente (LCEMP) — variazione % anno su anno"
data_period: "2025 Q1-Q4 (più trimestri 2022-2025 disponibili)"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Productivity and Unit Labour Costs, dataflow DSD_PDB@DF_PDB_ULC_Q + DSD_PDB@DF_PDB_ISIC4_I4"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 5fde61c7d306995d572e8a97bff6a40ef3c45809938c1b44913327257af0ceb8
tags: [sviluppo-economico-politica-industriale, lavoro-politiche-sociali]
description: "ULC Italia 2025: +3,2% YoY (Q4) — salari crescono più della produttività. Produttività per occupato 2025: -0,3% YoY. Italia perde competitività di costo strutturale."
---

# Costo del lavoro per unità di prodotto (ULC) e produttività, Italia, 2025

**Valori più recenti (2025-Q4, YoY):**

- **ULC (Unit Labour Costs, basato su occupazione) Italia: +3,17%** YoY
- **GDP per occupato (produttività): -0,33%** YoY
- **Compenso del lavoro per dipendente: ~+3% YoY** (cresce coi salari nominali)

**Significato critico:** **Costi del lavoro per unità prodotta crescono al ~3% mentre produttività CALA leggermente.** L'Italia sta **perdendo competitività di costo** rispetto ai pari UE/OCSE.

## Identità ULC = (Costo del lavoro) / (Produttività)

L'**ULC** = compenso del lavoro nominale ÷ produttività reale. Se i salari nominali crescono più della produttività, l'ULC aumenta — significa che ogni unità di output costa di più, l'economia diventa meno competitiva nei mercati internazionali.

```
ULC YoY = ΔSalari nominali − ΔProduttività
≈ +3% − (−0,3%) ≈ +3,3% (matches data)
```

## Serie storica ULC Italia (variazione YoY, %)

| Trimestre | ULC YoY |
|---|---|
| 2024-Q4 | +4,13% |
| 2025-Q1 | +3,78% |
| 2025-Q2 | +3,91% |
| 2025-Q3 | +3,11% |
| 2025-Q4 | +3,17% |

**Trend:** crescita ULC italiana ~3-4% YoY costantemente — picco 2024-Q4 (+4,1%) ora in lieve decelerazione.

## Produttività italiana (GDP per persona occupata, YoY) — il vero problema

| Trimestre | GDPEMP YoY |
|---|---|
| 2024-Q4 | **-0,65%** |
| 2025-Q1 | **-0,92%** |
| 2025-Q2 | -0,60% |
| 2025-Q3 | +0,14% |
| 2025-Q4 | -0,33% |

**Produttività italiana per occupato è NEGATIVA in 4 dei 5 trimestri analizzati.** Conferma: il PIL cresce meno dell'occupazione = ogni occupato produce meno valore aggiunto.

## Decomposizione: perché Italia perde competitività

L'ULC italiano cresce per via di tre forze sovrapposte:

1. **Salari nominali in recupero post-inflazione 2022-2023.** I rinnovi contrattuali (CCNL 2023-2024) hanno introdotto aumenti contrattuali compensativi (vedi card `indice-retribuzione-contrattuale-italia-2025.md` in lavoro).

2. **Produttività stagnante o in calo.** Manca crescita del PIL reale che compensi i salari (vedi `previsione-crescita-pil-italia-2027.md`).

3. **Composizione settoriale.** L'occupazione cresce in settori a bassa produttività (servizi alla persona, ristorazione, turismo) e cala in settori ad alta produttività (manifatturiero medio-grande).

## Confronto internazionale (orientativo)

**ULC YoY 2025-Q3 (riferimento OECD, da verificare con web search):**
- **Italia:** ~+3,1%
- **Germania:** ~+4,0% (più alto per Tarifabschluss recenti)
- **Francia:** ~+2,5%
- **Spagna:** ~+3,8%
- **USA:** ~+2,8%
- **Eurozona:** ~+3,2%

Italia è **in linea con eurozona** sull'ULC, ma il **gap di produttività è strutturalmente peggiore** — i partner UE hanno ULC simile perché entrambe le componenti (salari + produttività) crescono, mentre in Italia salari salgono e produttività cala.

## Produttività per settore (riferimento DF_PDB_ISIC4_I4, non in dettaglio qui)

Italia ha settori con dinamiche produttive molto diverse:
- **ICT e telecomunicazioni:** produttività in crescita (+1-2%/anno)
- **Manifatturiero:** moderatamente positivo
- **Costruzioni:** volatile, peggiorato post-Superbonus
- **Servizi alla persona (Q + I):** **produttività stagnante o in calo** — pesa sulla media
- **Pubblica Amministrazione (O):** misurazione complessa

## Implicazioni di policy

**ULC crescente + produttività stagnante = ricetta per perdita di competitività esterna.** Vie d'uscita (non mutuamente esclusive):

1. **Aumentare la produttività** via: investimenti in R&D, digitalizzazione, automazione, formazione, M&A che consolidano dimensioni d'impresa, riforme di concorrenza (vedi card PMR).
2. **Moderare la crescita salariale**: politicamente difficile e contrario al recupero del potere d'acquisto perso 2020-2023.
3. **Tagliare il cuneo fiscale** (vedi card `cuneo-fiscale-italia-2025.md`): riduce il costo del lavoro per le imprese senza ridurre il netto in tasca al lavoratore. **È la strada che governi italiani recenti hanno scelto.**

## Caveat e note di lettura

- **Dato quarterly con stagionalità** (anche se l'OECD pubblica serie destagionalizzate).
- **ULC basato su "employment" (ULCE)** = misura per occupato, non per ora lavorata. Versione "per hour" (ULCH) generalmente preferita ma non in questo filter.
- **Crescita YoY ≠ livello.** Un ULC che cresce 3% ogni anno significa accumulare +15% in 5 anni — degradazione composta della competitività di costo.
- **Confronto con Germania**: Italia ha ULC livello LIVELLO simile a Germania ma **produttività significativamente più bassa** = i salari italiani sono inferiori in valore assoluto ma il rapporto è peggiore.
- **Italia in eurozona**: non può compensare la perdita di competitività via svalutazione del cambio (come pre-Euro). Le opzioni sono solo le 3 sopra.
- **Dati 2025 provvisori** — revisioni trimestrali tipiche.

## Sorgente raw

`_raw/sviluppo-economico-politica-industriale/DF_PDB_ULC_Q/OECD.SDD.TPS,DSD_PDB@DF_PDB_ULC_Q,1.0+.Q........csv` (ULCE + GDPEMP + LCEMP quarterly)
`_raw/sviluppo-economico-politica-industriale/DF_PDB_ISIC4_I4/OECD.SDD.TPS,DSD_PDB@DF_PDB_ISIC4_I4,1.0+.A.GVAHRS.......csv` (produttività per settore ATECO, drill-down)
`_raw/sviluppo-economico-politica-industriale/DCCN_PRODUTTIVITA/Contributi alla crescita del valore aggiunto (IT1,98_197_DF_DCCN_PRODUTTIVITA_2,1.0).csv` (contributi capitale+lavoro alla crescita VA, ISTAT)
