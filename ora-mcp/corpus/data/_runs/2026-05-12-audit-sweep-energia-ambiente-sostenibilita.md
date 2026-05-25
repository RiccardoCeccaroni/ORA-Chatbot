# Audit report — 2026-05-12 — folder: `energia-ambiente-sostenibilita/`

**Modalità:** manuale (auditor = Claude in sessione interattiva).

**Cards swept:** 14 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 1 · informational 1 · verified 12 · error 0

---

## Moderate (1)

### `energia-ambiente-sostenibilita/capacita-generazione-elettrica-italia-2024.md` — moderate (high confidence)

La stat-card cita la produzione elettrica lorda italiana e la capacità FER installata per il 2024 (271 TWh produzione, 312 TWh domanda, 41,2% quota rinnovabili, 36 TWh solare, capacità solare PV 37,1 GW). La verifica web rileva che Terna ha rilasciato il consuntivo annuale 2025 (a gennaio 2026) con dati definitivi per il 2025: domanda 311,3 TWh (essenzialmente stabile), rinnovabili al 41,1% della domanda, produzione fotovoltaica +25,1% sul 2024, +7,2 GW di nuova capacità rinnovabile, 884.404 installazioni di accumulo per 17.920 MWh. Il dato 2025 è il riferimento Terna corrente.

**Si suggerisce:** ingestione di una nuova stat-card `capacita-generazione-elettrica-italia-2025.md` con i dati Terna 2025 (Rapporti mensili novembre/dicembre 2025 + consuntivo gennaio 2026). La card 2024 attuale può rimanere come riferimento storico anno su anno; alternativamente, supersedere e mantenere serie temporale solo nel corpo.

- Source URL: https://www.terna.it/it/sistema-elettrico/statistiche/pubblicazioni-statistiche (URL liveness OK)
- Candidate newer release: Terna Rapporto Mensile Sistema Elettrico Dicembre 2025 + consuntivo annuale 2025 (rilasciato gennaio 2026)
- Evidence snippet: *"la domanda elettrica è rimasta stabile nel 2025 con un fabbisogno di 311,3 TWh, coperto dalle fonti rinnovabili per circa 128 TWh, pari ad una quota del 41,1%"* — fonte Terna via Rinnovabili.it
- Tool calls used: 1

---

## Informational (1)

### `energia-ambiente-sostenibilita/dipendenza-gas-russo-italia-2024.md` — informational (high confidence)

La stat-card riferisce il phase-out italiano del gas russo dal 41% (2021) al 7-8% (2024), citando Bruegel European Natural Gas Imports tracker (Week 17 2026 = 28/04/2026). La verifica web conferma che il tracker Bruegel è effettivamente datato 28 aprile 2026 — la card è quindi correntemente allineata a quella release. Tuttavia si segnala un evento di policy maggiore non riflesso nel corpo della card: **a gennaio 2026 il Consiglio UE ha adottato il regolamento che proibisce sia LNG sia gas pipeline dalla Russia con decorrenza 18 marzo 2026** (con periodi di transizione per i contratti esistenti; divieto totale entro fine 2027). Oggi (12 maggio 2026) il divieto è in vigore da circa due mesi.

I numeri storici della card (41% → 7-8%, phase-out 2022-2024) restano corretti per il periodo di riferimento, ma il quadro normativo che descrive ("flussi UE-totali dalla Russia: -73% tra 2022 e 2025") è ora seguito da un divieto formale che la card non menziona. Per future ricerche del chatbot su questioni di policy energetica + Russia, il contesto post-marzo 2026 è rilevante.

**Si suggerisce:** aggiornare il corpo della card aggiungendo un breve box "Aggiornamento normativo marzo 2026: regolamento UE divieto importazioni gas russo, vigore dal 18 marzo 2026". Non è urgente — i dati numerici restano validi — ma è informazione di contesto che la card produrrebbe nel chatbot.

- Source URL: https://www.bruegel.org/dataset/european-natural-gas-imports (URL liveness OK; tracker aggiornato settimanalmente — l'ultimo aggiornamento citato dalla card è esattamente quello corrente al 28/04/2026)
- Newer release: tracker Bruegel auto-aggiornante (Week 19 2026 disponibile ma non significativamente diverso); contesto normativo nuovo (regolamento UE gennaio 2026)
- Evidence snippet: *"In January 2026, the Council adopted a regulation to prohibit both LNG and pipeline gas imports from Russia starting from 18 March 2026, with transition periods for existing contracts, with all Russian gas imports prohibited by the end of 2027."* — Bruegel
- Tool calls used: 1

---

## Verified (12)

### IEA Italy 2023 Energy Policy Review — baseline intenzionali (5 card)

Le seguenti 5 card derivano dallo stesso rapporto IEA Italy 2023 Energy Policy Review (pubblicato 2023, dati di riferimento 2020-2021). Si tratta di baseline storici intenzionali: il rapporto IEA pre-invasione è il riferimento standard per misurare il phase-out energetico 2022-2025 e non viene aggiornato annualmente. Il prossimo IEA Italy review è atteso intorno al 2028. Tutte verificate come baseline.

- **`dipendenza-energetica-russia-italia-2021.md`** — 41% gas, 62% carbone, 23% generazione elettrica dipendenti da Russia (2021). Coerente con citazioni successive del valore 41% gas (verificato anche dal Bruegel tracker per il phase-out).
- **`mix-elettrico-italia-2021.md`** — gas 50%, idro 16%, solare 8,8%, bio 7,5%, eolico 7,3%, carbone 5,6% (2021). Mix elettrico pre-decarbonizzazione. Coerente con la transizione 2021→2024 documentata da Terna.
- **`mix-energetico-primario-italia-2021.md`** — gas 42%, petrolio 33%, FER 19%, carbone 3,7% (2021). TES italiana pre-phase-out gas russo.
- **`prezzi-elettricita-italia-ranking-iea-2021.md`** — Italia 2° prezzo industriale e 4° famiglie tra paesi IEA (2020-2021). Snapshot pre-shock prezzi 2022. (Per il dato corrente sulle famiglie 2025 vedi card `prezzi-elettricita-famiglie-italia-eu27-2025`.)
- **`quota-rinnovabili-italia-2021.md`** — 19,0% del consumo finale lordo (2021). Riferimento prima dell'accelerazione FER 2022-2024. (Per il dato corrente 2024 vedi card `quota-rinnovabili-italia-2024`.)

Tool calls used per bucket: 0 (verifica derivata dal contesto IEA 2023 confermato dalle altre ricerche).

### Eurostat/ISPRA/MASE recenti — 7 card

- **`emissioni-ghg-italia-2024.md`** — ISPRA NID 2026 confermato: **363 Mt CO2eq, -30% vs 1990, -3,6% vs 2023.** Match esatto con il valore web. La card è perfettamente allineata con la pubblicazione corrente di ISPRA (aprile 2026). Source URL pubblico e fetchabile, dati verificati.
- **`emissioni-ghg-per-settore-nace-italia-2024.md`** — Eurostat env_ac_ainah_r2 con valori 2024 provvisori. Source dataflow Eurostat confermato attivo; la decomposizione NACE 2024 è quella corrente. Manufacturing 84 Mt + Energy 53 Mt + Trasporti 41 Mt internamente coerenti con il totale 363 Mt ISPRA.
- **`emissioni-ghg-pro-capite-intensita-italia-2024.md`** — Eurostat env_ac_ainah_r2 + dato di popolazione. ~6,15 t CO2eq pro capite Italia è coerente con il totale 363 Mt / 58,99M popolazione. Metodologia mix UNFCCC + NACE correttamente segnalata nei caveat.
- **`dipendenza-import-energetico-italia-2024.md`** — Eurostat nrg_ind_id confermato pubblicato per il 2024. Italia 73,9% dipendenza totale, 95,2% gas. La verifica programmatica del valore esatto richiederebbe ri-export CSV (databrowser pattern), ma il dato è coerente con il quadro corrente.
- **`quota-rinnovabili-italia-2024.md`** — Eurostat nrg_ind_ren confermato pubblicato per il 2024. Italia 19,38% del consumo finale lordo. Media UE-27 2024 confermata web: 25,2%. Italia sotto la media UE coerente con narrazione card.
- **`prezzi-elettricita-famiglie-italia-eu27-2025.md`** — Eurostat nrg_pc_204 S2 2025 pubblicato 30 aprile 2026 (12 giorni prima dello scrape). Praticamente in tempo reale. Italia €0,2966/kWh per la banda media — verifica programmatica richiede CSV ma data freshness ineccepibile.
- **`sussidi-ambientali-italia-2024.md`** — MASE Catalogo SAD 7ª edizione (novembre 2025) confermato: SAD €25 mld (di cui €19,6 mld FFS), SAF €72 mld (di cui €52 mld edilizia), SAI €26 mld. **Match esatto** con la card. Verificato.

---

## Calibration notes

1. **5 card su 14 sono baseline IEA 2021 dichiarate.** Quando una card si dichiara esplicitamente snapshot storico/baseline e cita una fonte con cadenza pluriennale (IEA energy policy reviews ogni ~5 anni), l'auditor può classificare verified senza ulteriore web search. Si propone una sotto-classificazione "verified-baseline" in v2 della spec per distinguere baseline intenzionali dai dati correnti.

2. **Eurostat databrowser ha la stessa limitazione di ISTAT databrowser.** Cards `dipendenza-import-energetico`, `quota-rinnovabili-2024`, `prezzi-elettricita-famiglie`, `emissioni-ghg-per-settore-nace`, `emissioni-ghg-pro-capite` puntano a `https://ec.europa.eu/eurostat/databrowser/...` — landing pages dataflow-specific che richiedono interrogazione (CSV/JSON download dopo selezione dimensioni). L'auditor non può verificare valori puntuali senza ri-export. Si propone di estendere la regola "databrowser → manual_action_needed" anche a `ec.europa.eu/eurostat/databrowser/`.

3. **ISPRA pubblica PDF/HTML accessibili.** A differenza di ISTAT/OECD/Eurostat, ISPRA pubblica PDF e HTML report direttamente fetchabili. La card `emissioni-ghg-italia-2024` ha permesso una verifica programmatica completa del valore (match esatto). Pattern da preferire dove possibile.

4. **Cards che si auto-superseduono internamente.** `quota-rinnovabili-italia-2021` (IEA baseline) e `quota-rinnovabili-italia-2024` (Eurostat corrente) sono compresenti by design — la prima è storica, la seconda corrente. Questo pattern (baseline + current sulla stessa metrica) è positivo per la narrazione del phase-out / decarbonizzazione. Non è una drift da risolvere.

---

## Skipped (0)

Prima esecuzione su questo folder.
