---
id: transizione-istruzione-lavoro-giovani-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Transizione istruzione-lavoro 18-24, Italia, 2024"
data_metric: "Distribuzione % della popolazione 18-24 per stato di istruzione (in/non in) × stato occupazionale (occupato/disoccupato/inattivo) — proxy NEET secondo definizione OECD-EAG"
data_period: "2024"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Education at a Glance, dataflow DSD_EAG_LSO_EA@DF_LSO_TRANS"
date_published: "2025"
date_scraped: "2026-05-12"
content_hash: d166d1f02076866d49a25896586b36e473d9591f0f5bdfbe5f72e3517532acce
tags: [istruzione, lavoro-politiche-sociali]
description: "Italia 2024 — su 100 giovani 18-24: 54% solo in formazione, 4% in formazione+lavoro, 23% lavoro senza formazione, 17,5% né in formazione né in lavoro (NEET-adjacent). Dati OECD Education at a Glance."
---

# Transizione istruzione → lavoro, giovani 18-24, Italia, 2024

## Headline

**Su 100 giovani italiani 18-24, nel 2024:**

- **54,2% sono in formazione e fuori dalla forza lavoro** (studenti puri).
- **4,4% sono in formazione + lavoro** (studenti che lavorano).
- **23,3% lavorano senza essere in formazione** (giovani che hanno completato e sono entrati nel mercato del lavoro).
- **17,5% non sono in formazione e non sono in lavoro** ← **proxy NEET-adjacent**.

Il **17,5% NEET-adjacent** è la cifra politicamente più sensibile di questa card.

## Distribuzione completa 18-24 — Italia 2024

| Combinazione (Istruzione × Lavoro) | Quota % | Etichetta |
|---|---|---|
| In formazione + occupato (`ED_E_O × EMP`) | **4,4%** | "Studio + lavoro" |
| In formazione + non occupato (`ED × OLF`) | **54,2%** | "Studenti a tempo pieno" |
| In formazione + in popolazione (`ED × POP`) | 59,3% | Totale "in education" |
| Non in formazione + occupato (`NED × EMP`) | **23,3%** | "Hanno completato e lavorano" |
| **Non in formazione + non occupato** (`NED × NE`) | **17,5%** | **NEET-adjacent** |

(Le righe dell'OECD sommano a 100% per costruzione, con qualche sovrapposizione nelle categorie aggregate.)

## Insight chiave

- **L'Italia ha una bassa quota "studio + lavoro"** (4,4%) rispetto a paesi nordici (15-25%) e UK/US. Il modello italiano è di **completamento formativo a tempo pieno**, poi entrata nel mercato del lavoro — non transizione graduale.
- **17,5% NEET-adjacent è altissimo per standard OCSE** (media OCSE 18-24 ~10-12%). Questo è coerente con il dato ISTAT NEET 15-29 (~16%, orientativo, da verificare) e ESL 13,1% (vedi [[abbandono-scolastico-precoce-italia-2020]]).
- **Solo 23,3% lavora e non studia** — significa che su tutti i 18-24enni italiani, **solo poco meno di 1 su 4 è in piena transizione "lavorativa adulta"**. Gli altri 3 su 4 sono o ancora in formazione (59%), o senza né formazione né lavoro (17,5%).

## NEET-adjacent ≠ NEET ISTAT/Eurostat ufficiale

⚠️ **Attenzione metodologica.** Il 17,5% qui calcolato dalla card OECD-EAG `NED × NE` è una **proxy del tasso NEET**, ma:

- Il **NEET ufficiale Eurostat** si misura su **15-29 anni** (più ampio del 18-24 qui). NEET Italia 2023 ufficiale ≈ 16% (15-29).
- Il **NEET include anche disoccupati ATTIVI** (in cerca di lavoro), non solo inattivi. Qui `NED × NE` racchiude entrambi (`NE = Not in Employment`, comprende disoccupati + outside labor force).

Quindi il 17,5% OECD-EAG 18-24 e il ~16% Eurostat 15-29 sono **valori coerenti ma misurati su universi diversi**.

Per il NEET ufficiale ISTAT/Eurostat servirebbe un dataflow specifico (`DCCV_NEET_FORZLV` o `DF_NEET`), non incluso in questo batch — listato nei gap nel manifest.

## Confronto col sistema dei pari

Su scala 18-24, paesi OECD con un robusto sistema di **apprendistato duale** (Germania, Svizzera, Austria, Danimarca) mostrano:
- Quote "studio + lavoro" del 15-25% (vs 4,4% italiano).
- NEET-adjacent intorno al 5-8% (vs 17,5% italiano).

L'Italia è invece nel **gruppo dei paesi sud-europei** (Spagna, Grecia, Portogallo) con sistemi a separazione netta studio→lavoro e alta quota NEET-adjacent. Lo Stato spagnolo ad esempio ha NEET 18-24 ~14-16% nel 2024.

## Metodologia

Framework: **OECD Education at a Glance — Labour-market Status by educational attainment (LSO)**. Dataflow `DSD_EAG_LSO_EA@DF_LSO_TRANS`, sub-modulo "Transition between education and work".

- **Popolazione di riferimento:** giovani 18-24 anni (`AGE = Y18T24`).
- **EDU_STATUS (codici principali):**
  - `ED` = In education (in formazione)
  - `ED_E_O` = In education AND employment OR outside labour force (in formazione, parallelo lavoro o inattivo)
  - `NED` = Not in education (fuori dalla formazione)
- **LABOUR_FORCE_STATUS (codici principali):**
  - `EMP` = Employment (occupato)
  - `OLF` = Outside the labour force (inattivo)
  - `NE` = Not in employment (non occupato = disoccupato + inattivo)
  - `POP` = Population (totale popolazione, riga di controllo)
- **MEASURE:** POP. **UNIT_MEASURE:** PT_POP_SUB = % di popolazione nella stessa sub-categoria.
- **Fonte raw per Italia:** RFL ISTAT armonizzata EU-LFS.

## Caveat e note di lettura

- **17,5% è un valore "OECD-derived" sul 18-24, non il NEET ufficiale 15-29.** Sembrano simili ma misurano due cose diverse — sempre indicare quale.
- **Single-year (2024) snapshot.** Il dataflow contiene 2022-2024 ma 12 righe Italia totali → poche per trend longitudinali.
- **Ridurre il NEET-adjacent richiede politiche su DUE livelli:** scuola (anti-abbandono, ESL) e mercato del lavoro (apprendistato, garanzia giovani). I paesi che riescono di solito operano su entrambi i fronti.
- **L'effetto demografia:** la popolazione 18-24 italiana è ~3,5 mln nel 2024. Il 17,5% NEET-adjacent = ~610 mila giovani.

## ORA — perché la cifra è politicamente rilevante

Il NEET è il **principale indicatore del fallimento della transizione scuola-lavoro in Italia**:
- Ogni partito politico ha posizioni sul NEET. ORA, in una posizione centrista pro-merito, è probabilmente per ridurre il NEET tramite (a) riforme dell'istruzione secondaria (anti-abbandono, IeFP), (b) apprendistato di terzo livello, (c) sostegno alla domanda di lavoro qualificato dal lato datoriale.
- Il 17,5% (OECD 18-24) e il 16% (ISTAT 15-29) sono entrambi nel range "sopra OCSE ma sotto Grecia/Spagna" — l'Italia è male ma non la peggiore. Cita correttamente: il dato Eurostat 15-29 è quello che le forze politiche italiane usano nei dibattiti.

## Sorgente raw

`_raw/istruzione/DF_LSO_TRANS/OECD.EDU.IMEP,DSD_EAG_LSO_EA@DF_LSO_TRANS,1.0+AUS+AUT+BEL+CAN+CHL+COL+CRI+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+OECD+ARG+BRA+BGR.csv`

Dataflow OECD `DSD_EAG_LSO_EA@DF_LSO_TRANS(1.0)` — 528 righe (44 paesi × ~12 combinazioni × 1 anno), 12 righe Italia (2024).
