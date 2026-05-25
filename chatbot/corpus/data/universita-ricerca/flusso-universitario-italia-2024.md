---
id: flusso-universitario-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Flusso universitario italiano — immatricolati, iscritti, laureati, docenti, 2019-2024"
data_metric: "Conteggi del flusso dell'università italiana: immatricolati (entrata), laureati (uscita), iscritti (stock), docenti (input). Anni diversi per ciascun aggregato per disponibilità dati"
data_period: "Immatricolati 2024 + Laureati 2022 + Docenti di ruolo 2019 (cross-section di anni diversi)"
source_url: "https://esploradati.istat.it/databrowser/"
source_doc: "ISTAT — dataflows DCIS_IMMATRIC1 (56_857), DCIS_LAUREATI (56_190), DCIS_ISCRITTI1 (56_858), DCIS_DOCENTI1 (56_1135). Perimetro docenti: solo personale di ruolo (Ordinari + Associati + Ricercatori a tempo indeterminato)."
date_published: "2024"
date_scraped: "2026-05-13"
content_hash: d4b4b0b988a8415ba9da320d4ab3748b3774ba5645fb15caf5da74a993acfd39
tags: [universita-ricerca, istruzione]
description: "Università italiana: 350k immatricolati 2024, 366k laureati 2022, 55.426 docenti di ruolo 2019 (ISTAT) — il flusso entrata-uscita del sistema universitario. Perimetro esteso MUR/USTAT ~110k+ (include RTD, assegnisti, contrattisti) — vedi caveat."
---

# Flusso universitario italiano — immatricolati, laureati, docenti

## Headline cifre

| Metrica | Valore | Anno |
|---|---|---|
| **Immatricolati a corsi universitari** | **349.733** | 2024 |
| **Laureati totali** | **366.194** | 2022 |
| **Docenti universitari di ruolo (ISTAT DCIS_DOCENTI1)** | **55.426** | 2019 |

(Nota: i tre dati hanno **anni di riferimento diversi** per via della pubblicazione separata dei rispettivi dataflow ISTAT.)

**⚠️ Perimetro docenti.** Il dato ISTAT `DCIS_DOCENTI1` conta **solo il personale di ruolo** (Ordinari + Associati + Ricercatori a tempo indeterminato). Il perimetro esteso usato da MUR/USTAT — che include RTD-A/B, assegnisti di ricerca e docenti a contratto — è di oltre 100 mila unità per gli stessi anni. La differenza tra le due cifre è strutturale, non un errore: l'università italiana ha quasi tanti "non di ruolo" quanti "di ruolo". Quando il chatbot riporta il numero, deve qualificare il perimetro.

## Composizione laureati 2022 per tipologia di corso

| Tipologia | Laureati 2022 | Quota |
|---|---|---|
| Corsi di laurea di I livello (Triennali) | 201.104 | **54,9%** |
| Corsi di laurea magistrale di II livello (specialistiche/biennali post-triennale) | 126.598 | 34,6% |
| Corsi di laurea magistrale a ciclo unico (Medicina, Giurisprudenza, ecc.) | 38.492 | 10,5% |
| **Totale laureati** | **366.194** | 100% |

**Quasi 55% dei laureati italiani sono "Triennali"** (laurea di I livello) — la maggioranza degli usciti dal sistema universitario italiano. La quota magistrale (35%) indica che **circa 1 triennale su 1,6 prosegue per la magistrale**.

## Composizione docenti di ruolo 2019 per qualifica (ISTAT DCIS_DOCENTI1)

| Qualifica | Numero 2019 | Quota |
|---|---|---|
| Ordinari (prof. ordinari, "cattedra piena") | 13.685 | 24,7% |
| Associati (prof. associati) | 22.283 | **40,2%** |
| Ricercatori a tempo indeterminato (RTI) | 19.458 | 35,1% |
| **Totale di ruolo** | **55.426** | 100% |

**Italia 2019: 55.426 docenti di ruolo**, di cui la quota più grande sono **associati** (~40%). Il rapporto **ricercatori / ordinari ≈ 1,4** indica un'università invecchiata: la base ricercatori è inferiore al "double" classico di paesi anglosassoni dove il rapporto è ~3-4 ricercatori per ordinario.

**Personale non di ruolo (non incluso in DCIS_DOCENTI1).** Per gli stessi anni, MUR/USTAT pubblica un perimetro più ampio che aggiunge: Ricercatori a tempo determinato di tipo A/B (RTD), titolari di assegni di ricerca, docenti a contratto. Il dato combinato (perimetro USTAT) per il sistema universitario italiano nel 2019 ammonta a circa 100-110 mila unità — quasi raddoppia la base. La quota di **personale precario sulla forza docente complessiva** è il dato strutturale più rilevante per il dibattito sul reclutamento universitario.

## Implicazioni della cross-section temporale

- **350k immatricolati 2024 vs 366k laureati 2022** → in equilibrio, il sistema è stazionario in dimensione. La leggera prevalenza dei laureati 2022 sugli immatricolati 2024 riflette: (a) gli effetti del Covid (lieve aumento iscrizioni 2020-2021), (b) il fatto che i laureati 2022 erano matricola ~2017-2019, anni di iscrizioni leggermente più alte. Il sistema universitario italiano è **complessivamente STABILE in dimensione** dal 2015 in poi (non in espansione).
- **Rapporto studenti / docenti.** Su ~1,8 mln di iscritti totali, il rapporto cambia drasticamente a seconda del perimetro docenti scelto:
  - **Perimetro ISTAT (di ruolo)**: 1,8M / 55,4k = **~32 studenti/docente di ruolo**.
  - **Perimetro USTAT (incluso RTD + assegnisti + contrattisti, ~100-110k)**: 1,8M / ~105k = **~17 studenti/docente**.
  Il rapporto "comparable OCSE" (~14-15) usa un perimetro che include il personale non di ruolo, quindi la cifra di confronto è il 17. **Per dire che l'università italiana è sotto-staffata vs OCSE** la base del confronto è il perimetro esteso, non quello di ruolo.
- **Tasso di laurea sui matricolati**: con ~350k immatricolati per anno e ~330k laureati di I+II livello per anno (escludendo magistrale), tasso completamento ~80% se misurato come "uscite/entrate stazionarie". MA il tasso di completamento universitario italiano per coorte (laureati / immatricolati 6-8 anni prima) è ~60-65% — sotto OCSE ~70-75%.

## Cosa NON è in questa card

- **Studenti universitari iscritti totale** (stock 2024) — disponibile in `DCIS_ISCRITTI1_1`. Non sintetizzato qui per brevità ma esiste nel raw.
- **Distribuzione laureati per disciplina/gruppo di classi di laurea** — disponibile nel raw `DCIS_LAUREATI`, e parallelamente in OECD `DF_UOE_NF_DIST_FIELD` (in `_raw/universita-ricerca/`).
- **Tasso di iscrizione universitaria post-diploma** (% diplomati che si iscrivono all'università entro 2 anni) — non in questi dataflow.
- **Italia VS OCSE su entry rate / completamento** — necessario OECD `DF_EAG_ENRL_RATE_AGE` (non scaricato in questo batch).
- **Brain drain laureati** (% laureati che emigrano dopo la laurea) — non c'è dataflow OECD/ISTAT diretto su questo; di solito da fonti accademiche o report Banca d'Italia.

## Metodologia

**Fonte:** Indagini annuali ISTAT su università e istruzione superiore, condotte in collaborazione col Ministero dell'Università e della Ricerca (MUR).

- **DCIS_IMMATRIC1 (56_857):** matricole iscritte al I anno di un corso di laurea triennale, magistrale o magistrale a ciclo unico in qualunque ateneo italiano. Anno di riferimento 2024 = anno accademico 2023/24.
- **DCIS_LAUREATI (56_190):** laureati conseguiti nell'anno solare. 2022 nel file scaricato = solo anno 2022.
- **DCIS_ISCRITTI1 (56_858):** iscritti totali al sistema universitario italiano. Vista `_1` = 2024 (snapshot). Vista `_2` = 2010 (frozen — archiviata ma non in card).
- **DCIS_DOCENTI1 (56_1135):** docenti in servizio nell'anno solare. 2019 nel file scaricato. Sezione: per area scientifico-disciplinare × qualifica (Ordinario / Associato / Ricercatore) × ateneo.

## Caveat e note di lettura

- **Anni diversi.** Cross-section di 2019 (docenti) / 2022 (laureati) / 2024 (immatricolati) — coerenza temporale limitata. Le tre serie hanno tempistiche di pubblicazione ISTAT separate.
- **"Italia totale"** include atenei statali + non statali pubblici + paritari + telematici. La quota telematici è salita dal ~2% (2010) al ~10-12% (2024) — alimentata da Università telematiche come Pegaso, Unicusano, Mercatorum.
- **Definizione "Laurea":** include tutti i titoli di livello terziario lungo (Triennali + Magistrali + Ciclo Unico). Esclude Master, Dottorati, Specializzazioni post-laurea.
- **Docenti 2019** è un dato relativamente vecchio. La popolazione docente è invecchiata di ~5 anni dal 2019 — il rapporto ordinari/ricercatori sarebbe ora ancora più sbilanciato. Per il dato 2023-2024 serve un re-export.
- **Iscritti totale stock** (in `DCIS_ISCRITTI1_1`) è stato lasciato in raw per evitare di sovraccaricare questa card. ~1,8 mln iscritti complessivi è il riferimento orientativo per il 2024 (da verificare nel file).

## Confronto con cifre internazionali

- **350k immatricolati / anno** in Italia rappresentano circa il **47-50% di una coorte di 19-20enni** (coorte ~700-720k nati 2003-2004). Il tasso di iscrizione universitaria italiano è circa il 50% di una coorte — vicino alla media UE (~55%) ma sotto i top performer (Polonia, Spagna, Francia: ~65-70%).
- **Docenti universitari in confronto cross-country.** Per un confronto apples-to-apples con Germania (~410k 2020) e Francia (~300k 2020), il perimetro corretto è quello USTAT esteso (~100-110k per l'Italia, **non** i 55,4k di ruolo ISTAT). Anche col perimetro esteso, l'Italia ha **meno docenti universitari per abitante** delle principali economie europee. Per misure normalizzate (per abitante o per studente) la posizione italiana resta nella metà inferiore dell'OCSE indipendentemente dal perimetro scelto.

## ORA — perché le cifre sono politicamente rilevanti

L'università italiana è centrale in vari dibattiti:
- **Numero chiuso** in Medicina, Architettura, Veterinaria — la pressione su tipologie di laurea "Ciclo unico" (38k laureati/anno) è strutturale.
- **Salari docenti / dottorato** — il numero ridotto di docenti di ruolo (55k ISTAT) e la struttura invecchiata (associati > ricercatori) è il sintomo del sotto-investimento decennale. La fascia precaria (~50k di personale non di ruolo) accentua la diagnosi.
- **Brain drain laureati italiani** — l'Italia laurea ~330k/anno (I+II livello) ma circa 30-40k laureati emigrano all'estero per lavoro entro 5 anni (orientativo, da verificare con web search OCPI / Banca d'Italia).
- **PNRR Missione 4** — espansione borse di studio, alloggi universitari, riforma dottorati. Politicamente molto carico negli ultimi 2 anni.

## Sorgente raw

`_raw/universita-ricerca/DCIS_IMMATRIC1/` — dataflow ISTAT 56_857 (immatricolati 2024).
`_raw/universita-ricerca/DCIS_LAUREATI/` — dataflow ISTAT 56_190 (laureati 2022).
`_raw/universita-ricerca/DCIS_ISCRITTI1/` — dataflow ISTAT 56_858 (iscritti 2024 + 2010).
`_raw/universita-ricerca/DCIS_DOCENTI1/` — dataflow ISTAT 56_1135 (docenti 2019).

Tutti i file sono filtrati a `Regione della sede didattica = Italia` (aggregato nazionale) per le cifre headline; le breakdown per ateneo / regione / disciplina sono nei raw e non sintetizzate qui.

Cross-card: vedi [[titolo-studio-adulti-25-64-italia-2024]] (OECD attainment 25-64) e [[spesa-per-studente-italia-2022]] (spesa per studente terziaria).
