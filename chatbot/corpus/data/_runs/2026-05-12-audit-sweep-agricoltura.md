# Audit report — 2026-05-12 — folder: `agricoltura/`

**Modalità:** manuale.

**Cards swept:** 9 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 2 · informational 1 · verified 6 · error 0

---

## Moderate (2)

### `agricoltura/emissioni-gas-serra-agricoltura-italia-2023.md` — moderate (high confidence)

La stat-card riporta le emissioni GHG del settore agricoltura per il 2023: **32,3 Mt CO2eq, 8,4% delle emissioni nazionali totali**, da ISPRA rapporto 414/2025 (maggio 2025). La verifica web rileva che ISPRA ha pubblicato il National Inventory Document 2026 (aprile 2026) con la serie completa 1990-2024. Il NID 2026 conferma agricoltura all'**8% delle emissioni totali nazionali nel 2024**, su un totale di ~360 Mt → **~28,8 Mt CO2eq da agricoltura nel 2024**, in calo dai 32,3 Mt del 2023 (-3,5 Mt, ~-11%). Coerente con la riduzione complessiva nazionale -3,6% sull'anno e con la prosecuzione del declino strutturale del patrimonio bovino.

**Si suggerisce:** ri-fetchare il rapporto ISPRA agricoltura aggiornato 2024 dal sito SINA-ISPRA (la pubblicazione annuale dedicata all'agricoltura segue tipicamente di pochi mesi il NID generale) e creare la stat-card `emissioni-gas-serra-agricoltura-italia-2024.md`. La card 2023 può essere mantenuta come riferimento storico o superseduta — scelta di Riccardo.

- Source URL: https://emissioni.sina.isprambiente.it/wp-content/uploads/2025/05/Le-emissioni-di-gas-serra-in-Italia_rapp.414-2025.pdf (URL liveness OK; punta al rapporto 2025, cioè la versione precedente)
- Candidate newer release: ISPRA NID 2026 (aprile 2026); rapporto agricoltura aggiornato atteso a maggio-giugno 2026
- Evidence snippet: *"L'agricoltura contribuisce all'8% delle emissioni totali nazionali"* — ISPRA NID 2026, dati 1990-2024
- Tool calls used: 1

### `agricoltura/operatori-dop-igp-italia-2021.md` — moderate (medium confidence)

La stat-card riporta 83.471 operatori italiani certificati DOP/IGP/STG (alimentari, esclusi i vini) nel 2021, con la composizione per settore: formaggi 24.637, olio extravergine 24.139, ortofrutta e cereali 20.861, carni fresche 10.177, preparazioni di carni 3.657. La verifica web rileva che ISTAT ha pubblicato il report "Prodotti agroalimentari di qualità DOP, IGP e STG — Anno 2022" (rilasciato settembre 2024), con dati per 2022: **circa 81.400 produttori certificati (+0,4% sul 2021)** nei segmenti corrispondenti, e un quadro complessivo di 195.407 operatori nazionali (inclusi i vini) per €20,2 mld di produzione. Italia conferma il primato UE per riconoscimenti DOP/IGP/STG.

**Si suggerisce:** ri-esportare il CSV ISTAT con la vista DCSC_PRODQUALIT (o il dataflow successore) per il 2022 e generare la stat-card `operatori-dop-igp-italia-2022.md`. Considerare di estendere lo scope per includere il dato sui produttori vinicoli (segmento più ampio: ~195k operatori totali vs ~81k esclusi i vini) — utile per il chatbot in domande comparative su filiere DOP/IGP.

- Source URL: https://esploradati.istat.it/databrowser/ (URL liveness OK)
- Candidate newer release: ISTAT "Prodotti agroalimentari di qualità DOP, IGP e STG — Anno 2022" (settembre 2024)
- Evidence snippet: *"In 2022, there were approximately 81,400 certified producers in the quality agricultural sector, a slight increase compared to 2021 (+0.4%)."* — ISTAT 2022 release
- Tool calls used: 1

---

## Informational (1)

### `agricoltura/valore-aggiunto-agricoltura-italia-2024.md` — informational (medium confidence — possibile ambiguità metrica)

La stat-card riporta il valore aggiunto netto dell'agricoltura italiana 2024 come **€42,4 mld (+9,0% nominale, +3,5% volume)**, con produzione totale €74,6 mld (+2,2% nominale) e reddito agricolo +12,5%. La verifica web sul comunicato ISTAT "Andamento dell'economia agricola — Anno 2024" (rilasciato gennaio 2025, aggiornato luglio 2025) riporta cifre che presentano un'ambiguità metrica:

- **Valore aggiunto a prezzi base 2024 = €31,84 mld** (per via dei conti satellite SEC 2010, ai prezzi base)
- **Produzione totale 2024 = €74,6 mld (+2,2%)** — match con la card
- **Volume +3,5%, reddito agricolo +12,5%** — match con la card
- **Italia 1ª in UE per VA agricolo 2024 (sorpasso su Spagna €39,5 mld)** — match con la card

Le cifre di volume (+3,5%) e produzione (€74,6 mld) coincidono; ma il valore di "VA agricolo" differisce tra il €42,4 mld della card e i €31,84 mld del comunicato. Possibili spiegazioni: (a) la card cita VA a costo dei fattori (incluse imposte indirette e sussidi alla produzione), non VA a prezzi base; (b) la card include qualche aggregato adiacente (silvicoltura/pesca) che il comunicato cita separatamente; (c) versione diversa del comunicato (preliminare gennaio 2025 vs aggiornata luglio 2025).

**Si suggerisce:** ri-fetchare il PDF del comunicato ISTAT "Andamento dell'economia agricola 2024" (versione luglio 2025 aggiornata) e verificare quale metrica produce il valore €42,4 mld; aggiungere al corpo della card un'esplicita etichetta sulla metrica usata ("valore aggiunto a costo dei fattori" o equivalente), per evitare ambiguità nel chatbot. La narrazione strutturale "Italia 1ª UE per VA agricolo" è confermata e non in discussione.

- Source URL: https://www.istat.it/comunicato-stampa/landamento-delleconomia-agricola-anno-2024/ (URL liveness OK)
- Newer release: aggiornamento luglio 2025 del comunicato gennaio 2025 — minor versioning
- Evidence snippet: *"The value added at basic prices of the primary sector in Italy, including fishing and forests, was 31 billion and 841 million euros."* — ISTAT report 2024
- Tool calls used: 1

---

## Verified (6)

- **`prezzi-agricoli-italia-2025.md`** — ISTAT indice prezzi prodotti agricoli, dato dicembre 2025 (rilasciato 2026). Output index 136,2 vs Input 127,8 (base 2020=100). Dataflow corrente; rolling monthly.
- **`pac-sussidi-italia-2023-2027.md`** — periodo programmatico PAC 2023-2027 con Piano Strategico Nazionale approvato 2 dicembre 2022. Il next ciclo PAC sarà 2028-2032 (non ancora in negoziazione attiva). Dotazione €36,87 mld confermata fino al 2027.
- **`coltivazioni-italia-2025.md`** — ISTAT coltivazioni 2025 (provvisorio). Mappatura corrente: foraggere 5,3 Mha, frumento duro 1,13 Mha, olive 1,09 Mha. Pattern stabile.
- **`superficie-agricola-italia-2024.md`** — OECD TOTAGR_LAND: 12,90 Mha 2024 per l'Italia. Serie 2012-2024 con valori 12,7-13,1 Mha — stabilità decennale confermata.
- **`zootecnia-bestiame-italia-2024.md`** — ISTAT 1/12/2024 stock + 2025 macellazioni. Bovini -11% dal 2020 (5,33M nel 2024) — coerente con narrazione del declino bovino e con il calo emissioni agricole. Macellazioni 2025 disponibili attraverso 2026-02 (molto recenti).
- **`produzione-latte-formaggio-italia-2025.md`** — ISTAT 2025 latte 13,23 Mt, formaggio vaccino 1,22 Mt. Dato di consuntivo 2025 (somma 12 mesi), disponibile da inizio 2026.

---

## Calibration notes

1. **Pattern "card 2023 → ISPRA NID 2026 ha già il 2024" è ricorrente.** L'ISPRA pubblica il NID annuale ad aprile/maggio. Card ISPRA di ogni anno vecchia di 1 anno è prevedibilmente moderate al prossimo sweep. Da considerare auto-classificazione di questi casi nel manifest.

2. **ISTAT comunicati stampa con URL diretti permettono fetch reale.** A differenza dei dataflow databrowser, le card che linkano `www.istat.it/comunicato-stampa/...` possono essere verificate al livello di contenuto (parzialmente). Le card `valore-aggiunto-agricoltura-italia-2024` e `previsioni-popolazione-italia-2024-2080` ne sono esempi. Pattern da preferire.

3. **Ambiguità metriche emerge spesso in agricoltura/conti nazionali.** "Valore aggiunto" può significare 4-5 cose diverse a seconda del SEC framework (prezzi base / costo fattori / lordo / netto / con/senza imposte indirette). Le card che usano questi concetti dovrebbero sempre tag-are esplicitamente la sotto-metrica usata, idealmente come parte di `data_metric` in frontmatter. Si propone un'aggiunta alla §5 di CLAUDE.md: per type=data con metriche di contabilità nazionale, esplicitare il sub-aggregato SEC.

---

## Skipped (0)

Prima esecuzione.
