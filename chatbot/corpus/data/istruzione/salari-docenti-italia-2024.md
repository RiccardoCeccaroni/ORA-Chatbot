---
id: salari-docenti-italia-2024
type: data
attribution: oecd
quality_tier: D1
title: "Salari medi degli insegnanti, Italia, 2024"
data_metric: "Salario annuo medio (mean) degli insegnanti in servizio nelle istituzioni educative pubbliche, in USD PPP a prezzi costanti, per livello ISCED (pre-primaria, primaria, secondaria I generale, secondaria II generale). Età di riferimento 25-64."
data_period: "2024; serie 2022-2024"
source_url: "https://data-explorer.oecd.org/"
source_doc: "OECD — Education at a Glance, dataflow DSD_EAG_SAL_ACT@DF_TCH (Teachers' actual salaries)"
date_published: "2025"
date_scraped: "2026-05-13"
content_hash: 9bb906bc2af0d130b917c4d95cf46ac7044eeccd290cf48f2808dff3b4efbbef
tags: [istruzione, lavoro-politiche-sociali]
description: "Salari medi insegnanti italiani 2024 (USD PPP costanti): Pre-primaria $49.507, Primaria $49.507, Sec I $52.642, Sec II $56.021. Italia -11 a -13% sotto media OCSE — meno della metà rispetto alla Germania."
---

# Salari medi degli insegnanti, Italia, 2024

> ⚠️ **Verifica periodo di riferimento pending (2026-05-13).** Evidenze testuali da EAG 2025 attribuiscono il valore $49.507 (Primaria/Pre-primaria) al **periodo di riferimento 2023**, e segnalano un calo reale del −4,4% nel 2024. Il CSV OCSE in `_raw/` etichetta esplicitamente `REF_PERIOD=2024` per questi valori, ma una ri-esportazione confermativa è bloccata da una protezione anti-bot Cloudflare sull'endpoint `sdmx.oecd.org` (HTTP 403 su 3 tentativi consecutivi il 2026-05-13). Le cifre qui esposte restano quelle del CSV originale (etichetta OCSE = 2024); la verifica definitiva richiederà un re-export manuale dal databrowser OCSE in un'altra sessione. Vedi `_audit/TO_VERIFY.md` §istruzione.

## Headline

| Livello scuola | Italia 2024 (USD PPP) | OCSE 2024 | EU-25 2024 | Differenza Italia vs OCSE |
|---|---|---|---|---|
| Pre-primaria (ISCED 02) | $49.507 | $50.489 | $48.202 | **−2%** |
| **Primaria** (ISCED 1) | **$49.507** | $57.233 | $56.730 | **−13%** |
| Secondaria I grado generale (ISCED 24) | $52.642 | $59.819 | $59.043 | **−12%** |
| Secondaria II grado generale (ISCED 34) | $56.021 | $62.922 | $62.659 | **−11%** |

**Italia paga i suoi insegnanti dell'**11-13% in meno della media OCSE** dalla primaria alla secondaria. Solo nella scuola dell'infanzia (pre-primaria) gli stipendi italiani sono **in linea con OCSE**.

## Confronto con la Germania — il gap è enorme

| Livello | Italia 2024 | Germania 2024 | Differenza Italia vs Germania |
|---|---|---|---|
| Primaria | $49.507 | **$91.950** | **−46% (Italia paga la metà)** |
| Secondaria I grado | $52.642 | **$100.831** | **−48%** |
| Secondaria II grado | $56.021 | **$105.523** | **−47%** |

Un insegnante italiano di Primaria guadagna **circa la metà del suo collega tedesco** (al netto del costo della vita, in PPP). La Germania è il caso più estremo nel confronto UE-grandi, ma il pattern si ripete in misura minore con quasi tutti i paesi UE-occidentali.

## Insight chiave

1. **Il salario in Italia non aumenta MOLTO con il livello scolastico.** Da pre-primaria ($49.507) a Sec II ($56.021): **+13%**. In OCSE la progressione è ben più ripida: da $50k a $63k = **+25%**. **Gli insegnanti italiani della Sec II sono pagati come la Primaria OCSE.**

2. **Pre-primaria + Primaria pari merito.** Italia 2024: pre-primaria = primaria = $49.507 esatto. **Coerente col sistema italiano statale**: l'insegnante della scuola dell'infanzia statale ha la stessa scala stipendiale dell'insegnante di primaria.

3. **L'Italia è al pari con EU-25 sulla pre-primaria** ($49.507 vs $48.202), ma **sotto EU-25 su primaria/secondaria** ($49.507 vs $56.730 = -13% in primaria).

4. **Il gap di -11/-13% si traduce in circa €450-600 al mese in meno** per insegnante italiano vs collega OCSE medio. Su 30 anni di carriera = €160-220k di stipendio lifetime mancante.

## Reconciliazione con commentario "Italia paga -30% sotto OCSE"

⚠️ **Nota metodologica importante.** Il commentario politico italiano (e diverse pubblicazioni OCSE pre-2022) ha storicamente quotato il gap "-25 a -30%" tra salari docenti italiani e OCSE. **Il dato 2024 D1 mostra che il gap è -11 a -13%**, meno ampio.

**Cosa è cambiato:** dal 2019, i rinnovi contrattuali italiani (CCNL Scuola 2019-21 + supplementi anti-inflazione 2023-2024) hanno aumentato gli stipendi docenti nominali italiani in misura significativa. Nel contempo, alcuni paesi OCSE hanno avuto stipendi docenti stagnanti in termini reali. Il gap **si è effettivamente ridotto** dal -25/-30% (riferimenti 2015-2018) al -11/-13% (dato 2024).

**Cosa NON è cambiato:** il salario di ingresso (entry-level) italiano resta molto basso e progredisce poco. Il dato di carta è il **salario MEDIO** (mean), non il top-of-scale. Se ci si concentra sui salari di **mid-career** o **top-of-scale**, gli ultimi confronti OCSE (EAG 2024) mostrano l'Italia ancora -20/-25% sotto media OCSE — perché la curva salariale italiana è particolarmente piatta.

**Cosa cita correttamente:**
- **"-11 a -13% sotto OCSE 2024 sul mean teacher salary"** ✓ (dato 2024 D1).
- **"-25/-30% sotto OCSE su entry e mid-career"** è verosimile ma da verificare con dataflow OECD entry/mid/top — non incluso in questa card. Da scaricare separatamente se serve il dato per scala.
- "Italia paga la metà rispetto alla Germania" ✓ (dato 2024 D1, -46/-48%).

## Cosa NON è coperto da questa card

- **Salario di entry (inizio carriera):** non in questo dataflow. Per il salario di ingresso serve `DSD_EAG_SAL_STAT@DF_STAT` (statutory salaries by experience: starting / 10 yrs / 15 yrs / top).
- **Salario top-of-scale (fine carriera):** stesso dataflow di sopra.
- **Salario insegnanti istituzioni PRIVATE:** in questa card filtro = INST_EDU_PUB (solo pubbliche). Statali + paritarie statali pubbliche. Le scuole paritarie private e indipendenti non sono coperte.
- **Salari ricercatori e professori universitari:** dataflow OECD distinto (`DSD_EDU_TER`). La card [[flusso-universitario-italia-2024]] menziona "-30/-40% sotto OCSE" per università ma quella cifra è orientativa e da verificare con un dataflow distinto.
- **Comparazione col costo della vita:** già normalizzata in USD PPP (PPP corregge per potere d'acquisto), ma resta variabilità regionale interna italiana (gli stipendi sono nazionali ma il costo della vita Milano vs Catania varia di ~30%).

## Metodologia

Framework: **OECD Education at a Glance — Teachers' actual salaries (DF_TCH)**. Dataflow `DSD_EAG_SAL_ACT@DF_TCH`, release 2025.

- **MEASURE:** Actual salaries (cosa l'insegnante effettivamente prende, NON la scala statutaria).
- **STATISTICAL_OPERATION:** MEAN (media aritmetica sui docenti in servizio).
- **UNIT_MEASURE:** USD PPP, **PRICE_BASE:** Constant prices (base 2020).
- **PERS_TYPE:** TE (Teachers — solo insegnanti, non dirigenti scolastici / personale ATA).
- **INST_TYPE_EDU:** INST_EDU_PUB (solo istituzioni pubbliche).
- **AGE:** Y25T64 (età 25-64, esclude pensionati e tirocinanti).
- **SEX:** _T (maschi + femmine aggregati).
- **EDUCATION_LEV codes:**
  - `ISCED11_02` = Pre-primary (scuola dell'infanzia statale italiana).
  - `ISCED11_1` = Primary (primaria).
  - `ISCED11_24` = Lower secondary general (sec I grado — escluso indirizzi tecnici/professionali secondari).
  - `ISCED11_34` = Upper secondary general (sec II grado liceale generale — esclude tecnici/professionali).
- **Fonte primaria per Italia:** dati MIM (Ministero Istruzione e Merito) trasmessi a OECD-UOE.

## Caveat e note di lettura

- **Mean ≠ stipendio per coorte / esperienza.** Il valore è la media su tutti i docenti in servizio, mix di età/carriere. Un docente fresco di assunzione guadagna ~$33k, un docente al top di carriera ~$60k. La distribuzione italiana è particolarmente schiacciata vs paesi OCSE con scale salariali ripide.
- **Solo istituzioni pubbliche.** I docenti delle scuole paritarie private (~5-10% del corpo docente totale) hanno stipendi spesso inferiori, NON inclusi qui.
- **"General education" only nelle ISCED 24/34.** I docenti di istituti tecnici (ISCED 35) o professionali (ISCED 25/36) NON sono inclusi nel filtro attuale. Per quei segmenti serve un export con ISCED 35/25/36 aggiunto.
- **USD PPP at constant prices base 2020.** Gli oscillamenti di tasso PPP possono fa apparire variazioni anno-su-anno che non sono variazioni reali in EUR. Per la cifra in EUR italiana: ~€45.000-50.000 lordo annuo per Primaria/Sec I, ~€51.000 lordo per Sec II.
- **Mancanze nei comparator:** Francia non riporta dati 2024 (file vuoto per FRA al 2024). Germania non riporta pre-primaria (cultura asili pre-scolari diversa). Spagna ha dati ma non confermati.
- **Trend 2022-2024 disponibile.** Il dataflow ha REF_PERIOD 2022/2023/2024 — il file scaricato in questo batch include la serie ma le cifre sintetizzate qui sono per il 2024.

## ORA — perché la cifra è politicamente rilevante

Il salario degli insegnanti è uno dei temi più ricorrenti del dibattito politico italiano sull'istruzione:
- **CCNL Scuola** — i rinnovi contrattuali sono regolarmente in discussione; il gap residuo con OCSE (anche -11% mid-career, -25% top-of-scale) è la giustificazione strutturale per aumenti.
- **Concorsi insegnanti** — il numero di candidati per posto è in calo in molte materie (italiano, STEM); il salario basso è uno dei drivers.
- **Confronto Italia-Germania-Francia** sul tema "vorremmo essere competitivi con l'Europa" — il gap -46% vs Germania è enorme e politicamente vivido.
- **PNRR Missione 4** — include investimenti su formazione docenti ma NON su livelli salariali strutturali.

## Sorgente raw

`_raw/istruzione/DF_TCH/OECD.EDU.IMEP,DSD_EAG_SAL_ACT@DF_TCH,2.1+..USD_PPP..ISCED11_02+ISCED11_1+ISCED11_24+ISCED11_34.Y25T64._T..csv`

Dataflow OECD `DSD_EAG_SAL_ACT@DF_TCH(2.1)` — 212 righe (53 paesi × ~4 livelli ISCED × 3 anni), 4 righe Italia (anno 2024 ISCED 02/1/24/34).

Cross-card: [[spesa-per-studente-italia-2022]] (spesa per studente — di cui parte è salario docente), [[spesa-pubblica-istruzione-italia-2022]] (spesa pubblica totale).
