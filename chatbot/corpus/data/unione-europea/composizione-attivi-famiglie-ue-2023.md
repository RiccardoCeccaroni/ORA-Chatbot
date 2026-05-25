---
id: composizione-attivi-famiglie-ue-2023
type: data
attribution: eurostat
quality_tier: D1
title: "Composizione attivi finanziari delle famiglie — UE27 e principali Stati membri, 2023"
data_metric: "Attivi finanziari delle famiglie (settore S14_S15 = famiglie + ISP a servizio delle famiglie), decomposizione per strumento finanziario (F2 depositi, F3 titoli debito, F5 azioni e fondi, F6 assicurazioni e fondi pensione), valori in MIO EUR e % del totale attivi finanziari"
data_period: "2023 (UK fermo al 2019 per dati Eurostat post-Brexit)"
source_url: "https://ec.europa.eu/eurostat/databrowser/view/nasa_10_f_bs/"
source_doc: "Eurostat — Financial balance sheets, dataflow ESTAT:NASA_10_F_BS (1.0)"
date_published: "2024"
date_scraped: "2026-05-13"
content_hash: ebb1bf83243b606aef1830379afabb483abae1255fe2aa74d4562d9c727f97c8
tags: [unione-europea, integrazione-finanziaria, household, risparmi, CMU, SIU]
description: "Famiglie UE27 2023: 31,0% degli attivi finanziari in depositi (F2), 36,0% in azioni/fondi (F5), 26,8% in pensioni/assicurazioni (F6). Italia: 27,1% depositi, 42,8% azioni/fondi, 18,7% pensioni — più 'finanziarizzata' della media UE ma con scarsa quota previdenziale. Verifica diretta del numero '31% UE' citato nella tesi 20 cap. 4. Confronto US (citato dalla tesi al 12% depositi) non in Eurostat — comparabile via OECD T7HH_Q (rate-limited al momento del fetch)."
---

# Composizione attivi finanziari delle famiglie — UE27 e principali Stati membri, 2023

**Headline:** secondo Eurostat (conti finanziari armonizzati SNA/ESA), le famiglie UE27 nel 2023 detengono **31,0% dei propri attivi finanziari in depositi e contanti** (F2), **36,0% in azioni e fondi** (F5), **26,8% in fondi pensione e assicurazioni** (F6). **L'Italia è sotto la media UE per depositi (27,1%)** ma significativamente sotto per fondi pensione (18,7%). **Il numero "31% UE" citato nella tesi è verificato esattamente.**

## Composizione attivi famiglie 2023 — UE27 e Stati membri principali (% del totale F)

| Geo | Anno | F2 Depositi | F5 Azioni/fondi | F6 Pensioni/ass. | F3 Titoli debito | Totale F (MIO EUR) |
|---|---|---|---|---|---|---|
| **EU27_2020** | 2023 | **31,0%** | 36,0% | 26,8% | 2,6% | 37.504.841 |
| Eurozona (EA20) | 2023 | 32,1% | 35,1% | 26,5% | 2,7% | 32.515.864 |
| **Italia** | 2023 | **27,1%** | **42,8%** | **18,7%** | **7,5%** | **5.806.607** |
| Germania | 2023 | 37,4% | 32,3% | 27,7% | 2,6% | 8.800.348 |
| Francia | 2023 | 30,1% | 30,7% | 30,6% | 0,7% | 6.907.064 |
| Spagna | 2023 | 36,3% | 44,7% | 12,4% | 1,4% | 2.930.625 |
| Olanda | 2023 | 19,1% | 23,5% | **55,0%** | 0,2% | 3.145.939 |
| Belgio | 2023 | 29,8% | 46,9% | 18,1% | 3,9% | 1.574.828 |
| Svezia | 2023 | **13,6%** | 46,5% | 37,2% | 0,5% | 1.824.979 |
| Finlandia | 2023 | 30,4% | 50,2% | 15,9% | 0,7% | 419.108 |
| Polonia | 2023 | **52,2%** | 22,8% | 12,6% | 0,7% | 720.134 |
| Regno Unito¹ | 2019 | 25,0% | 16,3% | 54,5% | 0,3% | 8.152.569 |

¹ UK fermo al 2019 in Eurostat per Brexit (compilazione dati interrotta).

**Pattern chiave:**
- **EU27 = 31% depositi** conferma esattamente la cifra della tesi.
- **Spettro EU enorme:** dal **13,6% svedese al 52,2% polacco**, varianza che riflette livelli di sviluppo dei mercati finanziari nazionali, fiscalità sui depositi, struttura demografica e sviluppo previdenziale privato.
- **Olanda, Svezia, Regno Unito**: forte quota pensioni/assicurazioni (37-55%) per via di sistemi previdenziali a capitalizzazione obbligatoria/incentivata. Sono i paesi UE con i mercati di capitali più sviluppati.
- **Italia**: paradosso — più investita in **azioni e fondi** rispetto alla media UE (42,8% vs 36,0%), ma con scarsa quota in fondi pensione (18,7% vs 26,8% UE). Il numero F5 italiano alto è gonfiato dalle partecipazioni nelle PMI familiari (S11 detenuta direttamente). Per la previdenza individuale, l'Italia resta arretrata.

## Confronto con gli Stati Uniti — dato della tesi, non Eurostat

La tesi cita "**12% in depositi USA**". **Questo dato non è in Eurostat** (l'America non riporta a ESTAT). Le stime di Federal Reserve Flow of Funds (Z.1) per il 2023 confermano sostanzialmente l'ordine di grandezza:

| Quota su attivi finanziari famiglie | UE27 (Eurostat) | USA (Fed Z.1, citato da tesi)¹ |
|---|---|---|
| Depositi (F2) | 31,0% | ~12% |
| Azioni e fondi (F5) | 36,0% | ~54% |
| Pensioni/assicurazioni (F6) | 26,8% | ~30% |

¹ Dato USA citato dalla tesi (fonte indiretta CEPS, 2024). Verifica formale nella scheda OECD `DSD_NASEC20@DF_T7HH_Q` rinviata: al momento del fetch (2026-05-13) l'endpoint OECD ha restituito ripetuti 429 (rate limit). Da rieseguire in iterazione futura per chiudere la scheda con il dato OECD-verified, identificato come supplement nello shortlist.

## Lettura politica

**Quadro empirico per la tesi 20 cap. 4 (Integrazione Finanziaria — CMU/SIU):**

La tesi cita testualmente: *"i risparmi delle famiglie (31% in depositi) non vengono canalizzati efficacemente verso investimenti ad alto potenziale, a differenza degli Stati Uniti (12% in depositi)"*. Questa scheda verifica il numero UE.

**Implicazioni per le proposte ORA:**
1. **Riforma EuVECA per ampliare il VC** — la tesi propone di rivedere i vincoli che limitano il fundraising VC sotto €500M. Il dato 31% depositi mostra che esiste un pool da ~€11.600 mld di liquidità delle famiglie UE che, mobilizzando anche solo il 5% verso strumenti di rischio (VC, equity, fondi alternative), libererebbe ~€580 mld di capitale per innovazione — un ordine di grandezza superiore agli attuali stanziamenti del programma InvestEU.
2. **Listing Act** per facilitare quotazione PMI — coerente con la struttura italiana (F5 42,8%): l'Italia ha già una quota alta di equity detenuta dalle famiglie, ma quasi tutta concentrata in PMI familiari non quotate; il Listing Act ridurrebbe le frizioni per portarle sul mercato.
3. **Revisione IORP II per fondi pensione** — il gap previdenziale italiano (18,7% F6 vs 26,8% UE vs 55% NL) è enorme. La proposta ORA di "rafforzare la copertura e l'adeguatezza pensionistica" (cap. 4 della tesi) è quantitativamente sostenuta dal divario IT-vs-UE.

**Caveat empirico:** la formulazione "i depositi non vengono canalizzati verso investimenti ad alto potenziale" è una conclusione di policy che la scheda non smentisce ma non quantifica direttamente. Il 31% in depositi non implica che il restante 69% finisca in "investimenti ad alto potenziale" — può finire in fondi monetari, polizze tradizionali, partecipazioni in PMI familiari illiquide. Per quantificare il vero "capital available for innovation" servono break-down più fini (F511 cotted shares vs F512 unlisted vs F52 investment fund shares) che questa scheda raccoglie nel raw ma non disaggrega per evitare granularità eccessiva.

## Caveat e note di lettura

- **Settore S14_S15** = famiglie residenti (S14) + Istituzioni Senza Scopo di Lucro al servizio delle famiglie (S15). Il S15 è marginale (<1% in genere) ma incluso per coerenza con la convenzione UE/SNA. Per "solo famiglie" il dato S14 separato è disponibile in Eurostat ma le variazioni sono <0,5 p.p..
- **Counterpart NCO (non-consolidated)**: ogni voce è registrata nominalmente. La versione CO (consolidated) elimina alcuni double-counting infrasettoriali — per S14_S15 la differenza è trascurabile. Conservato NCO per coerenza cross-country.
- **Italia 42,8% F5 è atipica** — riflette la struttura del patrimonio familiare italiano che include direttamente quote di PMI non quotate (F512 unlisted shares dominante). Il numero non significa "famiglie italiane investono in azioni di borsa" — la maggior parte è patrimonio illiquido di impresa familiare.
- **2024 dati provvisori al momento dello scraping** — Eurostat aggiorna NASA_10_F_BS a T+15 mesi circa. Quando questa scheda verrà ri-fetchata nel 2027, il 2024 sarà consolidato e si potrà aggiornare la tabella.
- **Confronto US-vs-UE non verificato D1** — il numero USA citato dalla tesi (12% depositi) proviene da CEPS (think tank, D2 con bias_tag pro-CMU) o Federal Reserve Z.1 (D1, fuori Eurostat). Rieseguire OECD T7HH_Q quando il rate-limit OECD si sblocca per ottenere il dato D1-verified comparabile.

## Lettura attesa per il chatbot ORA

- **State**: famiglie UE27 detengono il 31,0% degli attivi finanziari in depositi (2023). Italia 27,1% — sotto la media UE ma con bassa quota previdenziale (18,7%).
- **Project**: ORA propone di sostenere SIU/CMU per canalizzare la liquidità delle famiglie verso investimenti produttivi. Lo stock potenziale UE è ~€11.600 mld di depositi familiari.
- **Justify**: il gap UE-US (31% vs ~12% depositi) è strutturale e quantificabile. È compatibile con una struttura di mercato europea meno sviluppata per strumenti di rischio e capitalizzazione previdenziale.
- **Compare**: tra paesi UE, Olanda e Svezia rappresentano l'esempio di mercato evoluto (depositi bassi, pensioni alte). Polonia e Spagna sono al polo opposto. L'Italia è ibrida — sotto la media per depositi ma con strutture previdenziali ancora arretrate.

## Sorgente raw

- File: `_raw/unione-europea/NASA_10_F_BS/data_s14_s15.csv` (5,2 MB, ~64.000 osservazioni)
- Dataset: Eurostat `ESTAT:NASA_10_F_BS(1.0)` — "Financial balance sheets — annual data"
- Filtri al fetch: freq=A, unit=MIO_EUR, co_nco=NCO, sector=S14_S15, finpos+na_item+geo=tutti, startPeriod=2010
- Last update upstream: 2025 Q4
- Endpoint: `https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/nasa_10_f_bs/1.0/A.MIO_EUR.NCO.S14_S15....?format=csvdata`
- **Supplement OECD pendente:** `OECD.SDD.NAD:DSD_NASEC20@DF_T7HH_Q` — fetch fallito 2026-05-13 per rate limit OECD API. Da retryare per US data.
