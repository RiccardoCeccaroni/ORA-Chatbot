---
id: durata-procedimenti-penali-italia-2017
type: data
attribution: istat
quality_tier: D1
title: "Durata dei procedimenti penali in Italia, 2014-2017 (ultimo dato ISTAT disponibile)"
data_metric: "Intervallo medio e mediano in mesi tra l'iscrizione del procedimento (notizia di reato) e la definizione del procedimento al momento della decisione del PM — autori adulti — dataflow PROCEEDCRIME_A"
data_period: "2017 (ultimo anno disponibile); serie storica 2014-2017"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z0500GIU,1.0/IT1_GIUC/IT1_GIUCD/73_440/73_440_DF_DCCV_PROCEEDCRIME_A_11"
source_doc: "ISTAT — Procedimenti e reati al momento della decisione del PM — adulti, dataflow 73_440_DF_DCCV_PROCEEDCRIME_A_11 ('Dettaglio reati, intervallo medio e mediano tra iscrizione e definizione del procedimento')"
date_published: "2019"
date_scraped: "2026-05-13"
content_hash: 1fedc6547d84e646d39f9c79d6040f9fac401634b1b7446c3e60174a869c409e
tags: [giustizia, processi-penali, durata, stale-data-disclosure]
description: "Nel 2017 (ultimo anno ISTAT disponibile) un procedimento penale italiano per adulti dura mediamente 26 mesi e mediamente 22 mesi (mediana) tra iscrizione e definizione del PM. Trend 2014→2017 in peggioramento da 22 a 26 mesi (+18%). Forte eterogeneità tra distretti (Roma 34 mesi vs Trento 12 mesi) e tipo reato (terrorismo/mafia 100+ mesi vs frode/ricettazione 1 mese). DATO DA NON USARE COME PROXY DELLA TABELLA TESI (CEPEJ-based, definizione diversa: la tesi cita 'durata processo' incl. cognizione e impugnazione, ISTAT cita solo fase pre-dibattimentale fino a decisione PM)."
---

# Durata dei procedimenti penali in Italia, 2014-2017 (ultimo dato ISTAT disponibile)

**Headline:** secondo l'ultimo rilevamento ISTAT disponibile (2017), un procedimento penale per adulti italiano dura in media **26 mesi** e mediana **22 mesi** tra iscrizione e decisione del Pubblico Ministero. Il trend 2014→2017 è in peggioramento (+18% sulla media). Forti disparità: il distretto di Roma a 34 mesi è quasi 3× più lento di Trento (12 mesi); per reati di mafia/terrorismo si arriva a 100+ mesi (~9 anni), mentre per frodi semplici 1 mese. **Il dato ISTAT misura solo la fase pre-dibattimentale, NON la durata processuale completa di cui parla la tabella della tesi.**

## Italia — serie storica 2014-2017

| Anno | Durata media (mesi) | Durata mediana (mesi) | Δ vs anno precedente (media) |
|---|---:|---:|---:|
| 2014 | 22 | 18 | baseline |
| 2015 | 25 | 22 | +14% |
| 2016 | 26 | 22 | +4% |
| **2017** | **26** | **22** | flat |

(Fonte: ISTAT `73_440_DF_DCCV_PROCEEDCRIME_A_11`, sezione "Italia/tutti i distretti/tutti i reati".)

**Letture:**
- La distanza tra media (26) e mediana (22) di 4 mesi indica una **coda destra significativa** — un piccolo numero di procedimenti molto lunghi (mafia, terrorismo, processi complessi) alza la media.
- La crescita 2014→2017 (+4 mesi sulla media, +4 sulla mediana) è preoccupante in chiave trend.
- **Nessun dato successivo al 2017 è disponibile in questo dataflow ISTAT.** Le statistiche più recenti su durata processuale sono pubblicate dal Ministero della Giustizia (Monitoraggio civile e penale, D2/D3, non in questa scheda) e dal CEPEJ a livello europeo.

## Eterogeneità per distretto giudiziario 2017 (mesi medi, tutti i reati)

| Distretto più lento | Mesi | Distretto più rapido | Mesi |
|---|---:|---|---:|
| Roma | 34 | Trento | 12 |
| Brescia | 32 | Reggio di Calabria | 17 |
| Bologna | 30 | Taranto (sez.) | 17 |
| Cagliari | 29 | Campobasso | 17 |
| Venezia | 29 | Trieste | 19 |
| Bari | 27 | | |
| Milano | 27 | | |
| Palermo | 26 | | |

**Letture:**
- Il distretto **Roma è il più lento d'Italia** (34 mesi = 2,8 anni solo per arrivare alla decisione del PM).
- Trento è quasi 3× più rapido (12 mesi).
- I distretti del Sud (Reggio Calabria, Campobasso) non sono uniformemente i più lenti — il "Sud lento, Nord veloce" non si conferma su questa metrica.

## Eterogeneità per tipologia di reato 2017 (Italia, mesi medi)

| Tipologia | Mesi medi |
|---|---:|
| Associazioni terroristiche internazionali | **132** (~11 anni) |
| Associazione finalizzata al traffico stupefacenti | 118 (~10 anni) |
| Associazione di stampo mafioso | 107 (~9 anni) |
| Rapina | 107 |
| Falsificazione marchi pubblici | 102 |
| Omicidio volontario | 102 |
| Rapina tentata | 102 |
| Associazione a delinquere | 101 |
| ... | ... |
| Frodi | 1 |
| Ricettazione | 1 |
| Strage | 1 |
| Omicidio volontario completato | 1 |

**Lettura:**
- I procedimenti per mafia e terrorismo sono **chiaramente fuori scala** — ma sono casi rari e tipicamente l'iscrizione precede di molti anni la decisione del PM per investigazioni complesse.
- I reati comuni (frodi, ricettazione) si chiudono in 1 mese — coerente con archiviazione veloce per autore ignoto.
- **L'eterogeneità è di 3 ordini di grandezza** (1 → 132 mesi). La media e la mediana sono indicatori poveri per descrivere un sistema così disomogeneo.

## Confronto con la tabella della tesi — **carve-out empirico critico**

La tesi 08 (sezione Contesto) presenta questa tabella:

| | Prima Istanza (durata media) | Seconda Istanza (durata media) |
|---|---|---|
| **Penale Italia** | 355 giorni | 200 giorni |
| **Penale Europa** | 133 giorni | 110 giorni |

**Questo dato è derivato dal CEPEJ Evaluation Report 2024.** I dati ISTAT di questa scheda **NON sono direttamente confrontabili** con i 355 giorni della tesi, per due ragioni metodologiche:

1. **Fase processuale diversa.** La metrica CEPEJ "disposition time of pending cases" misura il tempo per definire un procedimento in primo grado (dall'iscrizione alla sentenza di primo grado). Il dato ISTAT `PROCEEDCRIME_A` misura solo dall'iscrizione alla **decisione del PM** (archiviazione o richiesta rinvio a giudizio). Sono fasi processuali differenti: il dato ISTAT è una sotto-fase di quello CEPEJ.
2. **Universe diverso.** CEPEJ include le sentenze di primo grado completate nell'anno; ISTAT include i procedimenti chiusi dal PM (anche quelli archiviati senza giudizio). L'universo ISTAT è più ampio (più archiviazioni rapide → durata media più breve nominalmente, ma include tutti i casi indipendentemente dall'esito).

**Conseguenza per il chatbot:** quando un utente cita i 355 giorni della tesi, il chatbot deve:
- Identificare la fonte (CEPEJ 2024, D2 non in corpus v1).
- **Non spacciare** il dato ISTAT 26 mesi (788 giorni) come "smentita" del dato tesi: misurano cose diverse.
- Aggiungere il contesto ISTAT 2017 come dato complementare: anche solo la fase istruttoria PM dura ~2 anni in media, prima della prima sentenza.

## Lettura politica

**Riferimento alla [[08-giustizia]]:**

La tesi 08 propone, sul penale:

> "Semplificare e velocizzare il processo penale, per garantire una risposta giuridica più rapida: valorizzare il ruolo dell'udienza preliminare, che può essere utile per selezionare i casi meritevoli di procedere, alleggerendo così il carico dei tribunali."

E sulla durata generale (tabella):

> "Penale Italia: 355 giorni vs 133 giorni Europa (1° istanza), 200 vs 110 (appello)."

I dati ISTAT 2017 di questa scheda **rafforzano la diagnosi** della tesi sulla lentezza, ma con caveat:
- 26 mesi medi *solo* per la fase pre-dibattimentale = un ordine di grandezza in linea con la lentezza denunciata.
- Trend in peggioramento 2014→2017 (+18%): la tesi del 2025 cita un dato CEPEJ più recente probabilmente peggiore di quanto qui mostrato.
- La proposta di "valorizzare l'udienza preliminare" come filtro per ridurre carico è quantitativamente plausibile: con il 60-70% delle iscrizioni che terminano in archiviazione (dato ISTAT generale), una migliore selezione anticipata potrebbe ridurre la durata media.

**Vacuum empirico per dato più recente:** la tesi cita il 2024 (CEPEJ); ISTAT ferma il proprio dato di durata al 2017. Per un giudizio aggiornato il chatbot dovrebbe attingere a:
- Min. Giustizia "Monitoraggio civile e penale" (citato in tesi tra i riferimenti — D2/D3).
- CEPEJ Evaluation Report 2024 (D2, non in v1).

## Caveat e note di lettura

- **STALENESS — VERY IMPORTANT.** L'ultimo anno disponibile in questo dataflow ISTAT è il 2017. Una serie di 8 anni di silenzio statistico significa che il dato qui contenuto è strumento di lettura *strutturale* (sistemi lenti, eterogenei), non *congiunturale* (situazione 2024). Il chatbot deve esplicitamente disclaimare questa staleness.
- **Metrica non equivalente al CEPEJ.** Vedi sezione "Confronto con la tabella della tesi". È un errore frequente — il chatbot deve evitarlo.
- **Solo procedimenti per adulti.** Il dataflow gemello `PROCEEDCRIME_M` per minori esiste ma non è incluso in questa scheda (volume basso, profilo diverso).
- **Districts vs courts.** "Distretto" qui si riferisce al Distretto di Corte d'Appello (es. "13: Roma" = Distretto di Corte d'Appello di Roma, che comprende tribunali della regione Lazio). Non è il singolo tribunale.
- **Coda destra:** la differenza media-mediana di 4 mesi indica una distribuzione asimmetrica. Per analisi rigorose servirebbe accedere ai percentili (P75, P90), che ISTAT non pubblica in questo dataflow.
- **Reasons for outlier offence types:** i 132 mesi del terrorismo non significano "11 anni dall'iscrizione alla decisione PM" in senso letterale, ma è il tempo che intercorre tra l'iscrizione iniziale e la decisione PM finale — talvolta queste indagini durano per anni con scoperte successive che riaprono il fascicolo.

## Lettura attesa per il chatbot ORA

- **State:** la durata media dei procedimenti penali italiani fino alla decisione del PM era 26 mesi nel 2017. Trend in peggioramento. Dato non aggiornato dopo il 2017 in ISTAT D1.
- **Project (cosa farebbe ORA):** la tesi 08 propone valorizzazione udienza preliminare + semplificazione processo. I dati ISTAT confermano l'ordine di grandezza del problema ma non permettono di valutare ex-ante l'efficacia delle proposte.
- **Justify:** la lentezza è documentata, anche se la cifra precisa della tesi (355gg) viene da CEPEJ e non da ISTAT.
- **Compare:** **non disponibile in ISTAT.** La tesi cita Europa a 133 giorni (CEPEJ). Per usare quel dato il chatbot deve attingere a Tier-3 (web search CEPEJ) o segnalare il vuoto della D1.

## Sorgente raw

- File: `_raw/giustizia/PROCEEDCRIME_A_11/data.csv` (193 MB — il file più grande del corpus difesa+giustizia, perché contiene la cross-tab `reato × distretto × anno × mean/median`).
- Dataset: ISTAT `73_440_DF_DCCV_PROCEEDCRIME_A_11` v1.0 — "Procedimenti, dettaglio reati, intervallo medio e mediano tra iscrizione e definizione del procedimento"
- Filtri applicati al fetch: startPeriod=2014, no filtri dimensionali (download integrale, ~472.000 righe).
- Misure utilizzate: `PROCEEDM` (mean time in months), `PROCEEDMED` (median time in months).
- Dimensioni: 442 tipologie di reato, distretti di Corte d'Appello, anno 2014-2017.
- Last update upstream: rilascio 2019 sui dati 2017. **Serie interrotta** — non si trovano edizioni successive nel catalogo SDMX ISTAT.
- **Raccomandazione tecnica:** per ingestione futura più snella, valutare di scaricare solo lo slice all-Italy + all-districts (~10 KB invece di 193 MB) usando un key filter SDMX specifico.
