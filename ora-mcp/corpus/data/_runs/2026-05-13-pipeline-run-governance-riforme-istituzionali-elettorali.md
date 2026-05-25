---
folder: governance-riforme-istituzionali-elettorali
pipeline_run_date: 2026-05-13
mode: autonomous (per autonomous_data_pipeline_prompt.md v1)
wishlist_voci: 5
shortlist_candidates: 5 (1 ISTAT + 2 OECD dataflow; alcune voci condividono dataflow)
downloads: 3 (all HTTP 200)
cards_written: 4
voci_status:
  voce_1_affluenza_elettorale: covered (Italia EP + regionali 2004-2024; cross-country gap)
  voce_2_rappresentanza_genere: covered (Italia + 10 paesi 2002-2025 parlamento e cabinet)
  voce_3_eta_rappresentanti: covered (Italia 2004-2024; no cross-country D1 disponibile)
  voce_4_fiducia_istituzioni: covered (Italia + 10 paesi 2023; serie storica corta — solo 1 punto Italia)
  voce_5_efficacia_politica: covered (combinata con voce 4 nella stessa card)
---

# Pipeline run — `governance-riforme-istituzionali-elettorali` — 2026-05-13

## Esito sintetico

4 stat-card scritte in `memory/corpus/data/governance-riforme-istituzionali-elettorali/`:

1. **`affluenza-elettorale-italia-2004-2024.md`** — Europee Italia: 73,1% (2004) → 49,8% (2024), -23 pp; regionali in caduta simile.
2. **`donne-parlamento-italia-vs-paesi-2002-2025.md`** — Camera Italia: 9,8% (2002) → 32,8% (2025); cabinet 25% (2025). Italia sotto mediana G7 europeo per entrambi.
3. **`eta-rappresentanti-comunali-italia-2004-2024.md`** — Consiglieri comunali under 40: 32,1% (2004) → 25,5% (2024); calo in larga parte demograficamente spiegato.
4. **`fiducia-istituzioni-italia-vs-paesi-2023.md`** — Italia 2023: 30,9% fiducia parlamento, 35,9% governo, 22,3% efficacia politica esterna (penultima fra 10 paesi). Tutti sotto media OECD.

5 voci → 4 card (collasso 4+5 in una single card "fiducia + efficacia politica" essendo della stessa survey Trustlab 2023). **Rapporto coerente con la trim policy.**

## Decisione di collasso voci → card

- Voci 4 (fiducia istituzioni) + 5 (efficacia politica) sono dallo stesso dataflow OECD TDG_2025 e si leggono insieme — un'unica card più coerente di due card frammentate. **Card 4 di output, una.**
- Voce 2 (rappresentanza genere) ha doppio dataflow (OECD per parlamento+cabinet, ISTAT BES per consiglieri comunali). Decisione: card dedicata al livello nazionale/cross-country (OECD), il dato BES locale `06POL002P` (donne consiglieri comunali) **NON è stato pubblicato come card separata** — è citabile dalla card 2 come complemento. Il raw BES è comunque in `_raw/`.

## Dataset scartati / collassati (with reasons)

- **ISTAT `06POL002P` (donne consiglieri comunali)** — scaricato (è nello stesso CSV BES TERRIT_6), ma **collassato come nota** nella card 2 piuttosto che produrre una card dedicata. Motivo: granularità municipale ≠ il piano di lettura di tesi 09 (riforma Camera/Senato); più adatto eventualmente a una card del folder `comuni-province-regioni`.
- **ISTAT `06POL007P`, `06POL009P` (collection capacity prov/comuni)** — fuori scope (capacità di riscossione locale è materia tassazione/governance locale, non riforme istituzionali nazionali).
- **ISTAT `06POL012P` (prison density)** — fuori scope (giustizia/penitenziario, non riforme istituzionali nazionali).

Nessun dataset rigettato per problemi tecnici. **Tutti i 3 download HTTP 200, formato CSV (con Accept header). Nessun fallback XML necessario in questo run.**

## Voci NON coperte (fuori D1 — backlog D2/D3)

Sezione critica per questo folder. La tesi 09 ha **molti punti empirici espliciti** che semplicemente non sono in D1 SDMX. Tutti elencati nella wishlist come "voci scartate consapevolmente". Per cronaca:

| Punto tesi | Metrica | Fonte attesa | Tier |
|---|---|---|---|
| "eccessivo ricorso alla decretazione d'urgenza" | n. decreti-legge per legislatura, % della legislazione | Camera dei Deputati, Osservatorio Fonti, ISLE | D2 institutional |
| "questioni di fiducia, maxiemendamenti" | n. questioni di fiducia, n. maxiemendamenti | Camera dei Deputati | D2 institutional |
| "indice di Gallagher da 3,9 a 7" | indice Gallagher di disproporzionalità | Michael Gallagher (TCD) database | D3 academic |
| "numero effettivo di partiti da 4,33 a 3,81" | Laakso-Taagepera index | accademico | D3 academic |
| "Spagna (7,6), Regno Unito (12,2)" | Gallagher cross-country | TCD database | D3 academic |
| Durata media governi | Italia vs UE | ParlGov database | D3 academic |
| Affluenza politiche nazionali Camera/Senato | serie storica | Ministero dell'Interno | D2 institutional |
| Affluenza europee cross-country | EP-elections.eu | Parlamento europeo | D1 institutional (non-SDMX) |
| Referendum costituzionali e di legge ordinaria | n. consultazioni, affluenza, esiti | Min. Interno, Corte Cost. | D2 institutional |

**Stima carico ingestion D2 per la tesi 09:** alta. Il folder governance è strutturalmente sotto-coperto da D1 SDMX. Un futuro batch D2 per questa tesi richiederà una pipeline a sé (scraper Camera dei Deputati + parser PDF Min. Interno + ingestione database accademici).

## Caveat e follow-up

- **Card 4 (fiducia istituzioni) ha solo 1 punto Italia (2023).** OECD Trustlab è biennale e l'Italia ha partecipato solo nella wave 2023 (rilascio 2025). La wave 2025 (rilascio atteso 2027) raddoppierà i dati italiani disponibili.
- **Card 1 (affluenza)** menziona valori cross-country qualitativi (Italia 49,8% vs UE-27 ~51% nelle europee 2024) ma **non li ha in scheda strutturata** — il dato cross-country viene dal Parlamento europeo, non da OECD/ISTAT SDMX. Da fetchare separatamente in batch futura.
- **Card 2 (donne parlamento)** non include il Senato — la metrica EMPW_PARL OECD è camera bassa o monocamerale. Per l'Italia bicamerale serve aggiungere il dato Senato (33,2% 2025, fonte camera.it/senato.it).
- **Card 3 (under 40 consiglieri)** è Italia-only. Confronto cross-country non disponibile in D1 SDMX.
- **Voce gap "responsiveness governativa quantitativa"** — l'efficacia politica esterna (TRUST_PE_EXT) è un proxy della responsiveness ma è auto-percepito. Per misure objective di responsiveness (es. quanto le policy approvate corrispondono alle preferenze mediane dell'elettorato) servono Manifesto Project / ParlGov / Comparative Manifestos Database (D3).

## Note tecniche emerse durante il run

Niente di nuovo emerso rispetto al run difesa. Conferme operative:

1. **ISTAT Accept header funziona** anche per BES TERRIT_6 (6 MB CSV restituito direttamente, no fallback XML necessario).
2. **OECD TDG_2025 ritorna ~360 KB senza key filter** — pesa poco, non serve filtrare. Edizione 2025 ha 938 osservazioni totali, raggiungibili in 1 download.
3. **OECD GOV_YU senza filtro per MEASURE è esiguo per le sole metriche EMPW (35 KB)** — fetch mirato funziona meglio del fetch globale.
4. **OECD `OECD_REP`** è il code per "OECD average country" (media non ponderata, non OECD totale). Era una sorpresa che le medie OECD/EU27 non siano calcolate nel raw per questo dataflow (presenti come righe REF_AREA in TDG).
5. **Importante per le card futuribili:** OECD TDG ha una dimensione `SCALE` (HMH, L, NEU, DK, CON, LIK, UNL) che cambia significato per misura. Per misure di fiducia istituzioni la metrica visibile è SCALE=HMH; per efficacia politica è SCALE=CON; per "responsiveness" (TRUST_POL) è SCALE=LIK. Va sempre verificato per misura prima dell'estrazione.

## Headline numbers per card

| Card | Metrica chiave | Italia | Benchmark | Anno |
|---|---|---|---|---|
| Affluenza | Europee | **49,8%** | 73,1% nel 2004 | 2024 |
| Donne in parlamento | Camera | **32,8%** | Spagna 44,3% / SWE 45% | 2025 |
| Donne cabinet | Ministri | **25,0%** | OECD pari mediana ~46% | 2025 |
| Under 40 consiglieri | % under 40 | **25,5%** | 32,1% nel 2004 | 2024 |
| Fiducia parlamento | TRUST_LE HMH | **30,9%** | OECD avg 36,5% | 2023 |
| Fiducia governo nazionale | TRUST_NG HMH | **35,9%** | OECD avg 39,3% | 2023 |
| Efficacia politica esterna | TRUST_PE_EXT CON | **22,3%** | OECD avg 29,8% | 2023 |
