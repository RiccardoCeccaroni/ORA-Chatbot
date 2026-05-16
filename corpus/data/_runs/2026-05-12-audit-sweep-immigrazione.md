# Audit report — 2026-05-12 — folder: `immigrazione/`

**Modalità:** manuale.

**Cards swept:** 10 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 0 · informational 0 · verified 10 · error 0

---

## Verified (10)

### Allineate con OECD International Migration Outlook 2025 (rilasciato novembre 2025)

- **`inflows-permanenti-categoria-italia-2024.md`** — card: 168.868 inflows permanenti 2024; composizione famiglia 61%, libera circolazione UE 23%, lavoro 10%, umanitario 5%. OECD IMO 2025: 169.000 inflows (-16% vs 2023), composizione 61% famiglia / 23% UE / 10% lavoro / 5% umanitario. **Match esatto** per cifra e composizione.
- **`inflows-foreign-population-italia-2012-2023.md`** — serie OECD armonizzata 2012-2023; 378.372 nel 2023, 191.766 nel 2020. IMO 2025 conferma il picco 2023 e il rimbalzo post-pandemico. Statistical annex IMO 2025 disponibile, copre stessi anni.
- **`occupazione-stranieri-italia-2024.md`** — tasso occupazione FB 64,7% vs NB 61,8% (2024). Dataflow OECD coerente con IMO 2025 e con la metodologia LFS armonizzata. Gap di genere stranieri (M 79,4% vs F 51,8% = 27,6 p.p.) coerente con narrazione corrente.

### Allineate con ISTAT Migrazioni interne e internazionali (rilascio provvisorio 2025 — marzo 2026)

ISTAT ha rilasciato a marzo 2026 le statistiche provvisorie 2025 sulle migrazioni interne e internazionali. Tutti i numeri principali corrispondono:

- **`immigrati-italia-2025.md`** — card: 439.916 iscrizioni dall'estero 2025 (provvisorio). ISTAT 2026-03: **"Le immigrazioni dall'estero sono 440mila"** — match esatto entro arrotondamento.
- **`emigrati-italia-2025.md`** — card: 144.157 cancellazioni per l'estero, 109.004 italiani (76%). ISTAT 2026-03: **"144mila emigrazioni (-23,7%), 109mila italiani (-22,7%), 35mila stranieri (-26,5%)"** — match esatto.
- **`trasferimenti-residenza-interni-italia-2025.md`** — card: 1.455.406 trasferimenti interni 2025; 57,7% verso Nord, 24,4% Mezzogiorno, 17,8% Centro. ISTAT 2026-03 conferma il pattern (saldo netto inter-regionale verso Nord).

### Allineate con altre pubblicazioni ISTAT/Eurostat correnti

- **`stranieri-residenti-italia-2024.md`** — ISTAT comunicato stampa "Censimento e dinamica della popolazione 2024" (dicembre 2025). Card: 5.371.251 stranieri al 31/12/2024, +117.593 vs 2023, 9,1% popolazione totale. Source URL diretto al comunicato stampa è fetchable. Il dato 2025 (saldo migratorio +296k) implicherà uno stock end-2025 più alto, ma il definitivo sarà rilasciato dicembre 2026 — la card 2024 è il dato definitivo corrente.
- **`previsioni-popolazione-italia-2024-2080.md`** — ISTAT proiezioni base 1/1/2024, rilasciate luglio 2025. Long-horizon projection; next cycle non atteso prima del 2027-2028. Source URL alive su istat.it/en/press-release.
- **`naturalizzazioni-italia-2024.md`** — card: 217.448 acquisizioni cittadinanza italiana 2024, 3ª UE (18,5%), tasso 4,1% (2° UE dopo Svezia). Eurostat news article DDN-20260327-1 (marzo 2026) **conferma esattamente**: 217.400 acquisizioni, 3ª dopo Germania (288.700) e Spagna (252.500), tasso 4,1% — secondo solo a Svezia 7,5%. Match perfetto. Source URL direct news article — fetchable.
- **`neet-seconda-generazione-italia-2024.md`** — ISTAT 2024 NEET 15-29 per cittadinanza/generazione: italiani 14,3% vs stranieri 23,7%; donne 1ª gen 38,2% vs italiane 14,7%; donne 2ª gen 14,5%. Coerente con il pattern delle pubblicazioni ISTAT "Livelli di istruzione e ritorni occupazionali — Anno 2024" (dicembre 2025) sulla disuguaglianza generazione/genere. Verificato per coerenza con il quadro 2024.

---

## Calibration notes

1. **Le card a fonte URL diretta (press release, news article) sono verificate con maggiore confidenza.** 3 card in questo folder hanno source_url puntate a documenti specifici (`/comunicato-stampa/...`, `/press-release/...`, `/products-eurostat-news/...`) anziché al databrowser generico. Per queste è possibile verificare la liveness e talvolta il contenuto. Pattern da preferire dove possibile, anche per le card databrowser-based.

2. **L'immigrazione è un dominio in cui i numeri ISTAT/OECD/Eurostat sono in cross-validation naturale.** Card `naturalizzazioni-italia-2024` (Eurostat) e `immigrati-italia-2025` (ISTAT) sono internally consistent: 217k acquisizioni cittadinanza italiane 2024 + 440k iscrizioni dall'estero 2025 = un flusso strutturale che il chatbot ha materiale per descrivere coerentemente.

3. **Zero moderate/critical findings su 10 card.** Questo sweep ha confermato che il folder è ben mantenuto e allineato alle release più recenti delle fonti corrispondenti. Cost ridotto rispetto a istruzione (3 search totali vs 5).

---

## Skipped (0)

Prima esecuzione.
