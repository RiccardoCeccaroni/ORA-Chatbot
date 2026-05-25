---
folder: universita-ricerca
pipeline_run_date: 2026-05-13
mode: partial-folder (1 existing card, 5 existing raws, no new downloads needed)
wishlist_voci: 7 (4 mapped to existing raws, 3 declared gaps)
shortlist_candidates: 4 (3 ISTAT + 1 OECD — all already downloaded)
downloads: 0 (raws already present from previous session 2026-05-12)
cards_written: 4 (new) + 1 (existing, flagged for revision)
voci_status:
  voce_1_iscritti_universitari: covered (new card iscritti-universitari-italia-2024)
  voce_2_laureati_per_regione: covered (new card laureati-italia-per-regione-2022)
  voce_3_docenti_di_ruolo: covered (new card docenti-universitari-di-ruolo-italia-2019; CORRECTION over existing card 102k figure)
  voce_4_campo_studio_oecd: covered (new card distribuzione-laureati-campo-studio-italia-oecd-2023)
  voce_5_gerd_per_fonte: gap (not in existing raws; deferred to next batch — OECD STI/STP MSTI)
  voce_6_mobilita_internazionale: gap (deferred — OECD/Eurostat international student mobility)
  voce_7_completion_rate: gap (deferred — OECD/Eurostat completion)
---

# Pipeline run — `universita-ricerca` — 2026-05-13

## Esito sintetico

4 stat-card nuove scritte in `memory/corpus/data/universita-ricerca/`:

1. **`iscritti-universitari-italia-2024.md`** — 1.909.503 iscritti 2023/24, 61,7% triennali; distribuzione regionale (Lombardia 17,5%, Lazio 17,4%, Mezzogiorno 29,0%); vista storica 2010 per gruppo classi di laurea.
2. **`laureati-italia-per-regione-2022.md`** — 366.194 laureati 2022, 54,9% triennali; distribuzione macroaree (Nord-ovest 28,1%, Centro 23,8%, Mezzogiorno 28,9%); analisi rapporto magistrale/triennale = 0,63.
3. **`docenti-universitari-di-ruolo-italia-2019.md`** — 55.426 docenti strutturati 2019 (Ord 24,7% / Ass 40,2% / Ric 35,1%); composizione per 14 aree scientifico-disciplinari; chiarimento metodologico ISTAT-vs-MUR (55k di ruolo vs 102k incluso precariato).
4. **`distribuzione-laureati-campo-studio-italia-oecd-2023.md`** — Italia 1,6% ICT vs OCSE 5,4% (**ultima al mondo OCSE** su 43 paesi); STEM totale 23,5% vs 24,2%; sovrappeso umanistico (Arts+Soc-Sci = 32% Italia vs 18,8% OCSE).

Card esistente:

- **`flusso-universitario-italia-2024.md`** (preesistente) — conservata ma flag 🔴 critical in TO_VERIFY: la cifra "Docenti totale 101.713 (2019)" attribuita a DCIS_DOCENTI1 è il perimetro MUR-USTAT, non ISTAT (cifra ISTAT effettiva = 55.426). Vedi sezione "Contraddizione data" sotto.

## Contraddizione data risolta inline (NON blocker)

Block condition #3 attivata e gestita inline, **non escalata**.

**Discrepancy:** la card preesistente `flusso-universitario-italia-2024.md` riporta nel headline:

> Docenti universitari (Italia, totale) = 101.713 (2019)

attribuendo a `DCIS_DOCENTI1 (56_1135)`. Il CSV ISTAT effettivo per Italia × Totale × Totale qualifica × Totale Sesso × 2019 restituisce **55.426** (13.685 Ord + 22.283 Ass + 19.458 Ric). Gap = **−45%**.

**Magnitudo:** >20% — soddisfa la soglia del block condition #3 per "contraddizione di magnitudine".

**Metodologicamente esplicabile:** SÌ.
- ISTAT `DCIS_DOCENTI1` conta **solo docenti di ruolo** (Ordinari + Associati + Ricercatori a Tempo Indeterminato/RTI). Esclude RTD-A, RTD-B (tenure track post-2010), professori a contratto, assistenti, dottorandi, assegnisti.
- MUR/USTAT pubblica come "personale docente" il totale **incluso RTD + contrattisti**, che porta a ~102k (in linea con la cifra USTAT citata nella tesi).
- Le due cifre **non sono in contraddizione**: descrivono universi diversi.

**Risoluzione applicata** (per memory `feedback_data_contradictions_handling` — "address inline"):
1. Nuova card `docenti-universitari-di-ruolo-italia-2019.md` scritta con la cifra ISTAT corretta (55.426) e spiegazione metodologica esplicita ISTAT-vs-MUR (tabella di confronto perimetri).
2. Card preesistente `flusso-universitario-italia-2024.md` **conservata** ma flaggata in `_audit/TO_VERIFY.md` come 🔴 action_critical, con proposta di revisione: sostituire 101.713 con 55.426 e linkare alla nuova card docenti (coerente con `attribution: istat` + `quality_tier: D1`).
3. Decisione finale di rimanere coerenti con `attribution: istat` (cifra 55k) lasciata a Riccardo via TO_VERIFY — non bloccante per la pipeline.

**Riccardo NON è bloccato** perché:
- la nuova card riporta la cifra coerente con la fonte;
- la cifra MUR ~102k resta accessibile e correttamente perimetrata via spiegazione;
- la card preesistente ha già una caveat sulla data antica del 2019.

## Voci scartate (gap dichiarati, da batch futuro)

- **Voce 5 (GERD per fonte di finanziamento):** richiede OECD MSTI (Main Science and Technology Indicators), dataflow `OECD.STI.STP:DSD_STI@DF_MSTI_PUB`. Non incluso nei raw esistenti. **Deferred to next batch.**
- **Voce 6 (Mobilità internazionale studenti universitari):** richiede OECD `DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_MOBILE_STUDENTS` o Eurostat `educ_uoe_mobs02`. **Deferred to next batch.**
- **Voce 7 (Tasso di completamento studi):** richiede OECD `DSD_EAG_COMPLETION`. **Deferred to next batch.**

Le tre voci coprono punti centrali della tesi 21 (brain drain Tier-4, attrattività studenti Tier-8, fuori-corso Tier-2) e meritano un batch dedicato. Suggerito da combinare con un re-fetch di DCIS_DOCENTI1 al 2022-2023 quando disponibile (vedi TO_VERIFY).

## Dataset scartati

Nessuno. Tutti e 5 i raw scaricati sono stati processati. Il file `DCIS_ISCRITTI1_2` (vista 2010 frozen per gruppo classi di laurea) è incluso nella card iscritti come breakdown disciplinare storica.

## Caveat e follow-up

- **Vista 2010 non aggiornata:** DCIS_ISCRITTI1 vista `_2` mantiene il 2008-2010 frozen (per la disaggregazione "Gruppo di classi di laurea"). Il MUR/USTAT pubblica annualmente la composizione disciplinare in formato non-SDMX; l'edizione 2023/24 sarebbe più informativa ma fuori dal perimetro SDMX-pipeline.
- **Anno 2019 per docenti:** è vecchio. Il PNRR Missione 4 (2022-2026) ha finanziato un'espansione del corpo accademico via 5.500 RTD-B. La composizione attuale è probabilmente sotto-stimata dal dato 2019.
- **Possibile artefatto ICT 1,6%:** in Italia molte lauree in Informatica sono classificate come L-31 / LM-18 (Informatica) — codifica ISCED-F può finire in F06 (ICT) o F05 (Natural Sciences/Math), seconda della mappatura MUR → OECD. La cifra 1,6% va doppio-checkata con vista alternativa (es. lauree Italia per classe di laurea 2023/24 da USTAT). Flag in TO_VERIFY come 🟡 moderate.

## Note tecniche emerse durante il run

Nessuna emergenza tecnica nuova oltre a quelle già documentate nel pilot `difesa`:

1. **Path lunghi Windows** sui file OECD CSV: il nome canonico OECD `DF_UOE_NF_DIST_FIELD/OECD.EDU.IMEP,DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_DIST_FIELD,1.0+....csv` (191 char) genera FileNotFoundError in `os.listdir()` quando Python tenta di leggere col path relativo. **Soluzione:** copiare il file in `/tmp/sdmx_pilot/` con nome breve prima di processare. Non richiede di rinominare il raw originale.
2. **Encoding utf-8-sig** indispensabile per le CSV ISTAT (BOM all'inizio). I file OECD usano utf-8 puro.
3. **Confidence ricodifica ISCED-F:** la mappatura del MUR delle lauree italiane a ISCED-F (livello broad) merita un controllo separato. Possibile sotto-rappresentazione ICT per misclassificazione.

## Riepilogo finale

| Indicatore | Valore |
|---|---|
| Wishlist voci (nuove) | 7 |
| Shortlist candidates (nuovi, con priorità trim) | 4 (3 ISTAT + 1 OECD) |
| Raw scaricati nuovi | 0 (riuso dei 5 raws preesistenti) |
| Card scritte nuove | 4 |
| Card preesistenti inspectate | 1 (`flusso-universitario-italia-2024`) |
| Dataset scartati | 0 |
| Block condition attivate | 1 (contraddizione data, gestita inline) |

**Esito:** folder `universita-ricerca/` ora ha **5 card totali** (1 preesistente + 4 nuove), coprendo stock iscritti, laureati per regione, docenti di ruolo per area+qualifica, e composizione disciplinare cross-country. Gap residuo principale: GERD financing breakdown + mobilità internazionale + completion rate — candidate per batch successivo.
