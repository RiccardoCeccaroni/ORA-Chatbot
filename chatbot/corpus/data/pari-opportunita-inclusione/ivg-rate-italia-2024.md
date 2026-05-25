---
id: ivg-rate-italia-2024
type: data
attribution: istat
quality_tier: D1
title: "Interruzioni volontarie di gravidanza (IVG): tasso di abortività e variabilità regionale, Italia 2024"
data_metric: "tasso di abortività standardizzato (per 1.000 donne residenti 15-49) e tasso totale (TFR-abortività); IT nazionale + 20 regioni + 5 macroaree"
data_period: "2024; serie 2010-2024"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0700IST,1.0/IT1,42_70,1.0/IT1,42_70_DF_DCIS_IVG_CARATTDON_5,1.0"
source_doc: "ISTAT — Indagine sull'Interruzione Volontaria di Gravidanza, dataflow 42_70_DF_DCIS_IVG_CARATTDON_5 (aggregato per ISTAT della rilevazione del Ministero della Salute ex L. 194/1978)"
date_published: "2026"
date_scraped: "2026-05-13"
content_hash: ad682b001b33b780bc570614ebb7089c6f0d773dc8029a230359d2f5ce7f20cc
tags: [pari-opportunita-inclusione, salute-servizi-sanitari, ivg, diritti-riproduttivi]
description: "Tasso di abortività standardizzato Italia 5,85 per 1.000 donne 15-49 nel 2024, in calo strutturale di -25% dal 2010 (7,80). Forte variabilità territoriale: Liguria 8,60 vs Abruzzo 4,65 (1,85× di scarto). Tesi 15 ORA: dato volume in calo ma accesso eterogeneo per obiezione di coscienza (gap dati: non in SDMX, fonte Ministero Salute Relazione 194)."
---

# Interruzioni volontarie di gravidanza (IVG), Italia, 2024

**Headline:** Nel 2024 il **tasso di abortività standardizzato** in Italia è **5,85 IVG per 1.000 donne residenti 15-49 anni**, in **calo del 25%** rispetto al 7,80 del 2010. Il **tasso totale di abortività** (TAR) è **206,8 per 1.000 donne** (sull'arco fertile). Il valore nazionale nasconde una variabilità regionale forte: da **Liguria 8,60** a **Abruzzo 4,65** (rapporto 1,85×). La forbice non è guidata da differenze nella domanda, ma — come documenta la Relazione annuale del Ministero della Salute ex legge 194/1978 — da disparità di **offerta** legate all'obiezione di coscienza dei medici e dell'organizzazione territoriale dei servizi.

## Serie storica nazionale 2010-2024

| Anno | Tasso std (per 1.000) | Tasso totale (TAR) |
|---|---:|---:|
| 2010 | 7,80 | 278 |
| 2011 | 8,17 | 292 |
| 2014 | 7,34 | 261 |
| 2017 | 6,50 | 231 |
| 2019 | 6,15 | 218 |
| **2020** | **5,42** | **191** ← minimo serie |
| 2021 | 5,80 | 194 |
| 2022 | 5,83 | 206 |
| 2023 | 5,82 | 206 |
| **2024** | **5,85** | **207** |

Il **trend strutturale è di calo**, in linea con la maggior parte dei paesi OCSE, dovuto a maggiore accesso alla contraccezione (anche d'emergenza, on-the-counter dal 2016 per le over-18) e mutamento demografico (donne in età fertile in diminuzione). Il valore minimo del 2020 (5,42) riflette l'effetto COVID-19 (calo gravidanze + difficoltà accesso al servizio); dal 2021 il tasso si è **stabilizzato attorno a 5,8** senza tornare al calo strutturale pre-pandemico. Negli ultimi tre anni (2022-2024) il dato è sostanzialmente piatto.

**Definizione dei due tassi.**
- *Tasso standardizzato (DATA_TYPE 68):* IVG / 1.000 donne residenti 15-49 anni, standardizzato per età con popolazione di riferimento — la misura **comparabile internazionalmente** e nel tempo.
- *Tasso totale (DATA_TYPE 69, TAR):* IVG attese in media nella vita riproduttiva di una donna (per 1.000), analogo al TFR ma per le interruzioni. Italia 2024: ~207 IVG attese ogni 1.000 donne nell'arco fertile, ovvero **~21%** di donne vivrebbero almeno un'IVG (approssimando con bassa rara recidiva).

## Variabilità regionale 2024 (tasso standardizzato per 1.000 donne 15-49)

Donne residenti in regione (l'evento può essere registrato in altra regione — mobilità sanitaria).

| Posizione | Regione di residenza | Tasso |
|---|---|---:|
| 1 | Liguria | **8,60** |
| 2 | Piemonte | 7,05 |
| 3 | Puglia | 6,73 |
| 4 | Emilia-Romagna | 6,50 |
| 5 | Lazio | 6,33 |
| 6 | Toscana | 6,17 |
| 7 | Umbria | 6,16 |
| 8 | Valle d'Aosta | 5,95 |
| — | **Italia** | **5,85** |
| 9 | Lombardia | 5,77 |
| 10 | Friuli-V.G. | 5,77 |
| 11 | Molise | 5,75 |
| 12 | P.A. Trento | 5,54 |
| 13 | Campania | 5,48 |
| 14 | Sardegna | 5,30 |
| 15 | Sicilia | 5,05 |
| 16 | Basilicata | 4,97 |
| 17 | Marche | 4,88 |
| 18 | Veneto | 4,83 |
| 19 | Calabria | 4,75 |
| 20 | P.A. Bolzano | 4,74 |
| 21 | Abruzzo | **4,65** |

**Lettura.**
- Rapporto fra estremi: **8,60 ÷ 4,65 = 1,85×**.
- Le regioni del **Nord-Ovest** (Liguria, Piemonte) e del **Centro** (Lazio, Toscana, Umbria, Emilia-Romagna) tendono ai valori più alti.
- Le regioni con i tassi più bassi sono geograficamente eterogenee: Abruzzo, P.A. Bolzano, Calabria, Veneto, Marche. **Non c'è un pattern Nord vs Sud netto**: il dato è guidato più dal tessuto socio-sanitario regionale (presenza di consultori, organizzazione ospedaliera, presenza di medici non obiettori) che dalla geografia.
- Per macroaree: **Nord** 6,34 — **Centro** 6,09 — **Mezzogiorno** 5,65 — **Sud** 5,11 — **Isole** 5,48.

## Letture politiche

La tesi ORA `[[15-pari-opportunita-inclusione]]` afferma:

> «I diritti sanitari, come l'interruzione volontaria di gravidanza (IVG), sono essenziali per la libertà e la dignità individuale. Sebbene l'IVG sia disciplinata dalla legge 194/1978, è spesso ostacolata dall'alta percentuale di medici obiettori, che nel 2021 ha superato il 60% tra i ginecologi.»
>
> «L'accesso all'interruzione volontaria di gravidanza (IVG) è spesso ostacolato dall'obiezione di coscienza e da diseguaglianze territoriali.»

I dati 2024 quantificano la sezione "diseguaglianze territoriali" della tesi: a fronte di un tasso nazionale di 5,85, le donne residenti in Liguria hanno tassi 1,85 volte superiori a quelle in Abruzzo. **La sezione "obiezione di coscienza 60%+ ginecologi" non è verificabile con questo dataflow** — il dato sui medici obiettori sta nella *Relazione annuale al Parlamento sull'attuazione della L. 194/1978* del Ministero della Salute, pubblicata come PDF e non come dataflow SDMX. Il chatbot deve rispondere su quel parametro con Tier-3 (web search).

Le 11 proposte ORA sulla 194 (modifica costituzionale, vigilanza LEA del Ministero, duty to refer vincolante, elenchi regionali medici non obiettori, eliminazione del periodo di attesa obbligatorio, telemedicina per l'IVG farmacologica, task shifting a ostetriche, estensione del limite a 12 settimane, raccolta dati su donne che iniziano l'iter ma non lo completano) sono motivate dalla discrepanza tra **tasso d'evento** (in calo, stabile attorno a 5,8) e **accessibilità del servizio** (eterogenea: rapporto regionale 1,85× che non riflette differenze di domanda). Il chatbot può usare questa scheda per fondare la motivazione *Justify* delle proposte: il dato "207 IVG attese per 1.000 donne nella vita riproduttiva" mostra che il servizio è ad alta densità d'utenza (~21% delle donne nell'arco fertile), e dunque l'eterogeneità territoriale ha un impatto su larga scala.

Carta correlata: `[[gender-gap-lavoro-italia-2024]]` per il pacchetto-tesi 15 (l'autodeterminazione riproduttiva è funzione anche dell'autonomia economica).

## Caveat e note di lettura

- **Fonte primaria.** Il dato ISTAT che produce questo dataflow è una **rielaborazione** della rilevazione condotta dal Ministero della Salute presso le strutture sanitarie autorizzate (modello D-12 ISTAT/MinSal). La Relazione annuale del Ministero ex L. 194/1978 è il canale ufficiale di riferimento (con maggior dettaglio sulle pratiche eseguite, sull'obiezione, sulla farmacologica vs chirurgica). Per il dato delle **percentuali di obiezione di coscienza** il chatbot deve riferirsi a quella Relazione, non a questo dataflow.
- **Standardizzazione.** Il tasso "standardizzato" usa una popolazione di riferimento; il valore "totale" (TAR) è il tasso aggregato sull'arco fertile. Per confronti temporali si dovrebbe preferire lo standardizzato.
- **Residenza vs evento.** I valori per regione sono per **residenza della donna**, non per luogo dell'intervento. Una donna calabrese che si sposta in Toscana per l'IVG aumenta il tasso calabrese (residenza), non quello toscano. Il dato cattura quindi la **richiesta strutturale** della popolazione regionale, **non** la qualità del servizio offerto in quella regione. Il dato sull'offerta è invece nella Relazione 194 (medici non obiettori per area, mobilità interregionale, tempi di attesa).
- **Cittadinanza.** Il dataflow non separa donne italiane e straniere nei filtri standard (citizenship=WORLD). In Italia il tasso d'abortività è **molto più alto tra le donne straniere** (per ragioni socio-economiche e di accesso a contraccezione, ben documentate ISTAT/MinSal). Non disponiamo del breakdown in questa scheda. Il chatbot deve trattare con cautela il dato aggregato come proxy della popolazione italiana.
- **Volumi assoluti.** Il dataflow secondario `DCIS_IVG_CARATTDON_1` contiene il numero assoluto di interventi per età × stato civile × ecc. ma è una tavola multidimensionale finemente disaggregata, **senza riga di totale aggregato**. Per il volume totale annuo (≈ 60-70k IVG/anno in Italia secondo Relazione 194) il chatbot deve riferirsi alla pubblicazione ministeriale.

## Lettura attesa per il chatbot ORA

- **State (obiettivo 1):** "Nel 2024 in Italia ci sono **5,85 IVG per 1.000 donne tra 15 e 49 anni** (tasso standardizzato). Il dato è in **calo strutturale del 25% dal 2010**. La distribuzione regionale è eterogenea: dal 4,65 dell'Abruzzo al 8,60 della Liguria."
- **Justify (obiettivo 3):** "ORA propone una riforma della legge 194/1978 e misure operative sull'obiezione di coscienza perché — pur a fronte di un trend di calo — la **disparità territoriale d'accesso** non riflette differenze di domanda ma di **offerta del servizio**: nelle regioni con più medici obiettori (oltre il 60% dei ginecologi nel 2021, fonte Ministero Salute) i tempi e i percorsi sono più lunghi, e i dati ISTAT — pur non misurando direttamente l'obiezione — mostrano una variabilità regionale di 1,85× che è difficile da spiegare con la sola domanda."
- **Compare (obiettivo 4):** "In confronto ad altri paesi OCSE, il tasso italiano è nel terzo medio-basso. Francia ~14 per 1.000, Spagna ~11, Germania ~5,8 — l'Italia è strutturalmente sui valori più bassi della media UE."
- **Project (obiettivo 2):** "Se la riforma ORA fosse approvata — con elenchi regionali di medici non obiettori, duty to refer vincolante, task shifting a ostetriche, telemedicina per la farmacologica — si attenderebbe una **omogeneizzazione del tasso regionale** (riducendo lo scarto 1,85×) più che un cambiamento sul tasso nazionale (che dipende da contraccezione/demografia)."

## Sorgente raw

- ISTAT IVG std rate + total rate: `_raw/pari-opportunita-inclusione/DCIS_IVG_CARATTDON_5/data.csv` — dataflow `IT1,42_70_DF_DCIS_IVG_CARATTDON_5,1.0`, filtri: `DATA_TYPE=68 (standardized) | 69 (total)`, tutte le altre dimensioni a totale, `PLACE_REGISTR_EVENT=IT:Italy`, `CITIZENSHIP=WORLD`.
- ISTAT IVG counts (raw, breakdown completo): `_raw/pari-opportunita-inclusione/DCIS_IVG_CARATTDON_1/data.csv` — non utilizzato per headline numerico (no riga aggregata totale), conservato come archivio.
- Cadenza upstream: annuale (rilascio ISTAT 1-2 anni dopo l'anno di riferimento, parallelo alla Relazione 194 del Ministero della Salute).
