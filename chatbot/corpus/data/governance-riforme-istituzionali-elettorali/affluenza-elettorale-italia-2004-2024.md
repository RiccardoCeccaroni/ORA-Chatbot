---
id: affluenza-elettorale-italia-2004-2024
type: data
attribution: istat
quality_tier: D1
title: "Affluenza elettorale in Italia — elezioni europee e regionali, 2004-2024"
data_metric: "Percentuale di elettori aventi diritto che hanno effettivamente votato (voter turnout), per tipo di consultazione elettorale"
data_period: "2004-2024 (europee: 2004, 2009, 2014, 2019, 2024; regionali: serie annuale 2004-2024)"
source_url: "https://esploradati.istat.it/databrowser/#/it/dw/categories/IT1,Z1000POLI,1.0/IT1,DF_BES_TERRIT,1.0/IT1,DF_BES_TERRIT_6,1.0"
source_doc: "ISTAT — Benessere Equo e Sostenibile (BES) — Politica e istituzioni, edizione 2025"
date_published: "2025"
date_scraped: "2026-05-13"
content_hash: 3c30b4a44f4192dfee2fe6d4aeebd40679776fd04e0b25973e1af4a8798dd34b
tags: [governance, elezioni, affluenza, partecipazione-politica, BES, italia]
description: "Affluenza alle europee in Italia in caduta strutturale: 73,1% nel 2004 → 49,8% nel 2024 (-23 pp in 20 anni, prima volta sotto il 50%). Affluenza alle regionali altrettanto in calo: 71% (2004) → ~40-45% (2021-2023). ORA propone STV + collegi medio-piccoli motivando anche con la riduzione del 'voto sprecato' nei sistemi maggioritari; i dati BES ISTAT confermano un problema strutturale di partecipazione, ma non identificano la magnitudine del collegio come driver causale."
---

# Affluenza elettorale in Italia — elezioni europee e regionali, 2004-2024

**Headline:** l'affluenza alle elezioni europee in Italia è crollata da **73,1% nel 2004** a **49,8% nel 2024** (-23,3 punti percentuali in 20 anni, prima volta sotto il 50%). L'affluenza alle elezioni dei consigli regionali è in calo simile: dal ~71% (2004-2005) al 39,8% nelle ultime tornate (2023) — anche se la serie è più rumorosa per via dell'eterogeneità tra regioni.

## Dati Italia — affluenza elezioni europee (BES `06POL001`)

| Anno elezione | Affluenza Italia (%) | Δ vs precedente |
|---|---|---|
| 2004 | 73,1 | — |
| 2009 | 66,5 | -6,6 pp |
| 2014 | 58,7 | -7,8 pp |
| 2019 | 56,1 | -2,6 pp |
| **2024** | **49,8** | **-6,3 pp** |

**Caduta cumulata 2004 → 2024: -23,3 punti percentuali.** L'Italia ha attraversato la soglia psicologica del 50% per la prima volta nel 2024.

## Dati Italia — affluenza elezioni regionali (BES `06POL001P`)

Le elezioni regionali non sono sincronizzate fra regioni: nello stesso anno si vota in un sottoinsieme variabile. La media nazionale è quindi una media pesata fra le regioni votanti in quell'anno.

| Anno | Affluenza media (%) | Note |
|---|---|---|
| 2004 | 71,2 | concomitanza con europee |
| 2005 | 71,4 | regionali "ordinarie" |
| 2010 | 63,6 | |
| 2014 | 62,7 | |
| 2015 | 52,2 | |
| 2018 | 68,4 | regionali Lombardia + Lazio in concomitanza con politiche |
| 2020 | 58,6 | regionali post-pandemia |
| 2021 | 44,4 | |
| 2023 | **39,8** | livello più basso del decennio |

## Confronto con altri tipi di elezione (qualitativo)

I dati BES ISTAT non coprono direttamente le **elezioni politiche nazionali** (Camera e Senato) — fonte canonica per queste è il Ministero dell'Interno (D2 institutional). Solo a titolo di contesto: l'affluenza alle politiche italiane è scesa dal ~85% degli anni '70-'80 al **63,9% nel 2022**, la più bassa di sempre per elezioni politiche (Min. Interno, non in questa scheda).

## Lettura politica

La tesi [[09-governance-riforme-istituzionali-elettorali]] discute l'affluenza in due passaggi:

1. **Contesto del trade-off elettorale (§ Sistema elettorale e di voto, voce 1):** *"nei sistemi maggioritari il winner-takes-all riduce la partecipazione di chi sostiene candidati senza chance e incentiva il voto strategico. I proporzionali, invece, favoriscono più partecipazione e meno strategia."*
2. **Proposta STV (§ Sistema di voto):** uno dei benefici dichiarati è *"ridurre il fenomeno del voto sprecato"*, che teoricamente dovrebbe alzare l'affluenza.

**Cosa dicono i dati rispetto a questa giustificazione:**
- L'**affluenza italiana è in caduta strutturale**, indipendentemente dal sistema elettorale: il calo del 2004→2024 alle europee (-23 pp) avviene a sistema elettorale invariato (proporzionale puro). Quindi il driver dominante della crescita dell'astensione **non è il sistema elettorale** ma fattori più ampi (disaffezione, perdita di senso di efficacia — vedi [[fiducia-istituzioni-italia-vs-paesi-2023]]).
- Questo non smentisce la proposta di STV — STV può comunque migliorare *altri* aspetti (proporzionalità, accountability, voto sincero). Ma significa che **l'argomentazione "STV → più affluenza" non ha supporto empirico evidente** nei dati italiani, perché le europee italiane sono già a sistema proporzionale e l'affluenza cala lo stesso.
- Il dato regionale (39,8% nel 2023) è il segnale empirico più forte: una crisi di legittimazione del sistema sub-nazionale che colpisce le elezioni più vicine al cittadino. Un sistema elettorale che ricostruisca il *link* elettore-rappresentante (come argomenta la tesi sui collegi medio-piccoli) potrebbe avere senso *strumentale* — ma il test del 5 di affluenza non è probante in un senso o nell'altro.

## Caveat e note di lettura

- **Definizione operativa:** la metrica BES `06POL001` è "percentage of eligible voter who cast a ballot in the last election for the european parliament (**excluding voting abroad**)". L'esclusione del voto AIRE (Italiani all'estero) riduce di ~1 punto il dato pubblicato rispetto al dato Min. Interno. Quando si confronta con valori cross-country va verificato il trattamento del voto estero.
- **Periodicità election-cycle.** Per ciascun anno non elettorale, la riga BES replica l'ultimo valore disponibile (es. le righe 2005-2008 ripetono il 73,1 del 2004). Solo i valori in anno-elezione sono nuovi.
- **Elezioni regionali — granularità spuria.** Il valore 2023 (39,8%) si riferisce alle regionali Lombardia + Lazio votate nel 2023. Confronti anno-su-anno della media regionale sono di limitata informatività.
- **Le elezioni politiche nazionali non sono in BES.** Per la serie storica completa Camera/Senato serve dataset Min. Interno (D2, da ingerire separatamente).
- **Confronto cross-country non in questa scheda.** L'affluenza cross-country per le europee è raccolta da Eurostat / Parlamento europeo (D1 institutional, non in questa pipeline). Italia 2024 (49,8%) si posiziona poco sopra la media UE-27 alle europee 2024 (~51%).

## Lettura attesa per il chatbot ORA

- **State**: in Italia l'affluenza alle europee è scesa al 49,8% nel 2024 (era 73,1% nel 2004); alle regionali si attesta sul ~40-45% nelle tornate più recenti.
- **Project (cosa farebbe ORA)**: la riforma elettorale ORA (proporzionale con collegi 4-6 seggi + STV) ambisce a "ridurre il voto sprecato" come parte della giustificazione, ma il sistema attuale per europee è già proporzionale puro — la proposta agisce sulle politiche.
- **Justify**: il calo dell'affluenza è strutturale e cross-elezioni; non è isolabile come "effetto del sistema elettorale" perché il sistema europee è invariato e cala lo stesso. La giustificazione empirica della riforma è quindi più nei dati di **fiducia/efficacia politica** (scheda [[fiducia-istituzioni-italia-vs-paesi-2023]]) che nei dati di affluenza.
- **Compare**: Italia 49,8% (europee 2024) è sotto a Belgio (89,8% — voto obbligatorio), Germania (64,8%), Spagna (49,2% simile), e sopra a UK pre-Brexit (35,6% nel 2014); media UE-27 2024 ~51%. **Confronto cross-country non incluso in questa scheda — serve fetch separato Parlamento europeo D1.**

## Sorgente raw

- File: `_raw/governance-riforme-istituzionali-elettorali/DF_BES_TERRIT_6/data.csv` (6,1 MB)
- Dataset: ISTAT `DF_BES_TERRIT_6` v1.0 — "BES — Politica e istituzioni"
- Filtri applicati al fetch: `startPeriod=2000`, nessun altro filtro (l'intero dataset è ~6 MB, gestibile).
- Indicatori estratti per questa scheda: `06POL001` (voter turnout EP), `06POL001P` (voter turnout regional councils). Dimensioni rilevanti: REF_AREA (per Italia = `IT`), DATA_TYPE (indicatore), SEX=T (totale), TIME_PERIOD.
- Edition: 2025. Cadenza di aggiornamento upstream: annuale (gennaio-marzo per riprendere l'anno elettorale precedente).
