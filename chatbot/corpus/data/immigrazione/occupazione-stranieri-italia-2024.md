---
id: occupazione-stranieri-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Occupazione degli stranieri (nati all'estero) vs nativi, Italia, 2024"
data_metric: "tasso di occupazione per luogo di nascita (foreign-born vs native-born), per sesso e titolo di studio"
data_period: "2023-2024 (annuale)"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — International Migration Database, dataflows DSD_MIG@DF_MIG_EMP_EDU + DSD_MIG@DF_MIG_NUP_SEX (MEASURE=EMP_WAP, % of working-age population in same subgroup)"
date_published: "2026"
date_scraped: "2026-05-12"
content_hash: 25c7f3e7087013a44190badacd56caa99726467580497256fee09f2822df71bf
tags: [immigrazione, lavoro-politiche-sociali, pari-opportunita-inclusione]
description: "Tasso di occupazione 2024: nati all'estero 64,7% vs nativi 61,8% (FB superiore al NB). Ma con istruzione terziaria: nativi 83,6% vs nati all'estero 70,9% (sovra-qualificazione/sotto-utilizzo). Gap di genere tra stranieri molto ampio: M 79,4% vs F 51,8% (27,6 p.p.)."
---

# Occupazione degli stranieri (nati all'estero) vs nativi, Italia, 2024

## Dato aggregato 2024

| Gruppo | Tasso di occupazione |
|---|---|
| **Nati all'estero (Foreign-born, FB)** | **64,7%** |
| **Nati in Italia (Native-born, NB)** | **61,8%** |
| Gap (FB − NB) | **+2,9 p.p.** |

⚠️ **Lettura immediata: il tasso di occupazione dei nati all'estero in Italia è SUPERIORE a quello dei nati italiani.** Questo contraddice frontalmente la narrazione "gli stranieri non lavorano / vivono di sussidi". Nei dati OCSE 2024 l'opposto è vero.

## Disaggregazione per titolo di studio (ISCED 2011)

| Titolo di studio | Nati all'estero | Nati in Italia | Gap (FB − NB) |
|---|---|---|---|
| ISCED 0-2 (al massimo licenza media) | **59,3%** | 41,8% | **+17,5 p.p.** |
| ISCED 3-4 (diploma secondario superiore) | 68,2% | 67,0% | +1,2 p.p. |
| ISCED 5-8 (istruzione terziaria) | **70,9%** | **83,6%** | **−12,7 p.p.** |

### La storia in tre fasce
- **Bassa istruzione: gli stranieri lavorano molto più degli italiani.** 59,3% vs 41,8% — un divario enorme. Il mercato del lavoro italiano per i lavori low-skill è coperto da stranieri (agricoltura, ristorazione, cura, edilizia).
- **Media istruzione: praticamente identici** (68% vs 67%).
- **Alta istruzione: gli stranieri lavorano molto meno degli italiani laureati** (70,9% vs 83,6%). Questo è il **fenomeno del brain waste / sotto-utilizzo**: laureati stranieri impiegati in lavori sotto la loro qualifica, oppure con disoccupazione strutturale per non-riconoscimento titoli.

## Disaggregazione per sesso

| Gruppo | M | F | Gap di genere |
|---|---|---|---|
| Nati all'estero (FB) | **79,4%** | **51,8%** | **−27,6 p.p.** |
| Nati in Italia (NB) | 69,7% | 53,6% | −16,2 p.p. |

### Lettura
- **Uomini stranieri**: tasso di occupazione 79,4% — **superiore di ~10 p.p. agli uomini italiani** (69,7%). Concentrati in lavori manuali, edilizia, agricoltura, logistica.
- **Donne straniere**: tasso di occupazione 51,8% — **inferiore alle donne italiane** (53,6%) di 1,8 p.p. e con un **gap di genere intra-gruppo di 27,6 punti percentuali**, quasi il doppio rispetto agli italiani.

**La donna straniera in Italia è il segmento più escluso dal mercato del lavoro.** Cause documentate (OECD, Banca d'Italia):
- Cultura d'origine (ruoli familiari)
- Lingua + servizi di accompagnamento all'occupazione
- Carico di cura familiare (asili nido scarsi + sussidiarietà familiare)
- Discriminazione assunzioni

## Lettura politica

### "Gli immigrati non lavorano" — smentito dai dati
- Nati all'estero **occupazione totale 64,7% > nativi 61,8%**. ORA può usare questo numero direttamente.
- **Uomini nati all'estero 79,4%** — il sotto-gruppo più occupato in Italia, superiore a tutti gli altri.

### "Però le donne straniere..."
- Sì: **51,8% donne nate all'estero** è basso. Punto di intervento di policy: integrazione donne migranti, servizi all'infanzia, formazione professionale.
- È coerente con la posizione ORA di "centrismo economico-liberale": il mercato del lavoro lascia inutilizzato un grande capitale umano femminile (italiano + straniero).

### Brain waste — l'inefficienza più costosa
- Laureati nati all'estero **70,9% occupati**, italiani **83,6%**. Gap di 12,7 punti.
- Cause: **non-riconoscimento dei titoli esteri** (procedure CIMEA lunghe e costose), barriere all'esercizio professionale (albi), lingua tecnica.
- Costo per il sistema: laureati stranieri sotto-utilizzati, mentre l'Italia ha carenze acute in sanità, ingegneria, IT.

### Il triangolo politico
Su questa tabella si possono costruire le tre seguenti posizioni programmatiche, tutte basate sugli stessi dati:
1. **Pro-immigrazione lavorativa**: il sistema produttivo italiano si regge sui low-skill stranieri (59% occupazione FB ISCED 0-2 vs 42% NB).
2. **Riforma riconoscimento titoli**: il gap −12,7 p.p. sui laureati è un problema strutturale auto-inflitto.
3. **Politiche di genere mirate**: la donna straniera è il segmento più escluso — intervento mirato (asili, lingua, formazione) cumula i benefici di immigrazione + occupazione femminile.

## Metodologia

Fonti combinate:
- **`DSD_MIG@DF_MIG_EMP_EDU`** — Labour market outcomes of immigrants - Employment rates by educational attainment.
- **`DSD_MIG@DF_MIG_NUP_SEX`** — Labour market outcomes of immigrants - Employment, unemployment, and participation rates by sex.

Misura: **EMP_WAP — Employment rate / employment to working-age population ratio** (% del sottogruppo di età lavorativa in occupazione).
Unità: **percentage of working-age population in the same subgroup** (PT_WAP_SUB).
Definizione di "foreign-born": **persone nate all'estero** (place of birth ≠ Italia), indipendentemente dalla cittadinanza attuale (include quindi anche cittadini italiani naturalizzati nati all'estero).
Universo: **15-64 anni**.
ISCED 2011: 0-2 = al massimo secondaria inferiore; 3-4 = secondaria superiore; 5-8 = terziaria (laurea +).

## Caveat e note di lettura

- "Foreign-born" ≠ "stranieri di cittadinanza non-italiana". Include italiani naturalizzati. La differenza in Italia è significativa: dei ~6,5M nati all'estero residenti, ~1,5M ha cittadinanza italiana per acquisizione.
- **Serie corta** (2023-2024 in questo export). Per la serie pluriennale si può chiedere a OECD un re-export TIME_PERIOD esteso (~10 anni disponibili).
- I tassi di occupazione qui sono **rispetto alla popolazione del sottogruppo**, non rispetto al totale. Quindi sommano coerentemente con i tassi della Rilevazione Forze di Lavoro ISTAT.
- L'**EMP_WAP più alto degli stranieri** è in parte spiegato dalla composizione anagrafica: gli stranieri sono in media più giovani degli italiani (concentrati in fasce produttive 25-54 vs italiani con quota over-55 alta). Aggiustando per età, il gap si riduce ma non si annulla.
- Per il **tasso di disoccupazione FB vs NB** (concetto diverso da EMP_WAP) → gap residuo (re-export con MEASURE=UE_WAP_SUB).

## Sorgente raw

- `_raw/immigrazione/DF_MIG_EMP_EDU/OECD.ELS.IMD,DSD_MIG@DF_MIG_EMP_EDU,1.0+..A......csv` — disaggregazione per istruzione
- `_raw/immigrazione/DF_MIG_NUP_SEX/OECD.ELS.IMD,DSD_MIG@DF_MIG_NUP_SEX,1.0+..A.EMP_WAP.....csv` — disaggregazione per sesso
