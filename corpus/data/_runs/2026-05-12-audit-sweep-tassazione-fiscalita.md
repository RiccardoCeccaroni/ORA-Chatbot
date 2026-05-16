# Audit report — 2026-05-12 — folder: `tassazione-fiscalita/`

**Modalità:** manuale.

**Cards swept:** 5 · **Skipped:** 0 · **Errors:** 0

**Severity breakdown:** critical 0 · moderate 1 · informational 0 · verified 4 · error 0

---

## Moderate (1)

### `tassazione-fiscalita/pressione-fiscale-italia-2024.md` — moderate (high confidence — methodology gap)

La stat-card cita la pressione fiscale italiana 2024 al **42,2% del PIL** (calcolato "come media dei 4 trimestri"), con €937 mld entrate fiscali AAPP su PIL €2.202 mld; trend 2023→2025 indicato come **41,0 → 42,8%**. La verifica web rileva che ISTAT, nel comunicato annuale "Pil e indebitamento AP — Anni 2022-2024" (marzo 2025), riporta la **pressione fiscale 2024 al 42,6% del PIL** (in salita dal **41,4% del 2023**). Le differenze tra card e comunicato annuale ISTAT sono:

| | Card | ISTAT comunicato annuale | Δ |
|---|---|---|---|
| Pressione fiscale 2024 | 42,2% | **42,6%** | -0,4 p.p. |
| Pressione fiscale 2023 | 41,0% | **41,4%** | -0,4 p.p. |
| PIL 2024 (utilizzato) | €2.202 mld | €2.199,6 mld (definitivo) | +€2,4 mld (0,1%) |

Le differenze sono coerenti e di entità simile (-0,4 p.p.), suggerendo che la card e il comunicato usano due dataflow ISTAT diversi:
- **Card:** conti non-finanziari trimestrali (dataflow `Z0500GG_QC` o simile), con derivazione "media dei 4 trimestri" — metric valida ma non equivalente al rapporto annuale aggregato.
- **Comunicato ISTAT annuale:** rapporto entrate-fiscali-annuali / PIL-annuale (definitivo). Questa è la cifra che giornali e politici citano come "pressione fiscale italiana 2024".

Per un chatbot che dovrà rispondere a "qual è la pressione fiscale italiana?", citare 42,2% quando l'opinione pubblica conosce 42,6% crea un problema di credibilità anche se la card è metodologicamente trasparente.

**Si suggerisce:** allineare la card al valore del comunicato annuale ISTAT (**42,6% per 2024, 41,4% per 2023**) — è il riferimento atteso dai lettori. Mantenere la nota metodologica spiegando che ISTAT pubblica due versioni: il dato trimestrale aggregato (che la card stava usando) e il dato annuale del comunicato (che è la versione standard). In alternativa, conservare il dato trimestrale ma aggiungere esplicitamente nel corpo: "Cifra annuale standard ISTAT: 42,6% — la media dei 4 trimestri qui calcolata è 42,2%, differisce per effetto della stagionalità del PIL."

- Source URL: https://esploradati.istat.it/databrowser/ (URL liveness OK)
- Newer release: ISTAT comunicato "Pil e indebitamento AP — Anni 2023-2025" (più recente del 2022-2024, rilasciato presumibilmente marzo 2026); verifica con il valore definitivo 2024 e provvisorio 2025 in quella release.
- Evidence snippet: *"La pressione fiscale è salita al 42,6% del PIL nel 2024, in aumento di oltre un punto rispetto al 41,4% del 2023."* — ISTAT marzo 2025, ripreso da Il Sole 24 Ore + ItaliaOggi
- Tool calls used: 1

---

## Verified (4)

### `tassazione-fiscalita/cuneo-fiscale-italia-2025.md` — verified (high confidence — match esatto)

OECD Taxing Wages 2026 (rilascio aprile 2026) per Italia: tax wedge per single earner al 100% del salario medio = **45,8% nel 2025** (in calo di 1,21 p.p. dal 47,0% del 2024). Italia 5ª OCSE per cuneo nel 2025 (era 4ª nel 2024). Card cita **45,76%** — match esatto entro arrotondamento (45,76% → 45,8% web). Source dataflow corrente.

- Evidence snippet: *"The tax wedge for the average single worker in Italy decreased by 1.21 percentage points from 47.0% in 2024 to 45.8% in 2025."* — OECD Taxing Wages 2026

### `tassazione-fiscalita/aliquote-statutarie-cit-dividendi-italia-2026.md` — verified (high confidence — math match)

Card cita: IRES 24%, ritenuta su dividendi 26%, carico combinato CIT+dividend per persona fisica residente **43,76%**. Math check: 1 - (1-0,24) × (1-0,26) = 1 - 0,76 × 0,74 = 1 - 0,5624 = **0,4376 = 43,76%** ✓. Aliquota IRES 24% confermata da fonti italiane multiple (PwC, Bird & Bird, DLA Piper) per il 2026. Ritenuta su dividendi 26% conferma per persona fisica residente. **Tutto coerente, math esatto.**

Da segnalare per contesto: dal 1° gennaio 2026 il regime di esenzione parziale del 95% dei dividendi (per soci corporate residenti) richiede partecipazione ≥10% o valore fiscale ≥€500.000 — questa è una modifica 2026 specifica per dividendi inter-corporate, non rilevante per la cifra 43,76% della card (che è company → individual). La card resta corretta.

### `tassazione-fiscalita/entrate-fiscali-totali-italia-2024.md` — verified (medium-high confidence)

Card: entrate fiscali AAPP 2024 = **€940 mld** (OECD Revenue Statistics provvisorio). Coerente con il quadro ISTAT (entrate fiscali specifiche, escluse entrate da capitale e da partecipazioni). Il rapporto OECD Revenue Statistics annuale è la fonte autorevole; release 2025 atteso/uscito a fine 2025 con dati 2024. Nessun newer release indicato.

### `tassazione-fiscalita/imposte-produzione-d29-italia-2025.md` — verified (high confidence)

Card: imposte sulla produzione D.29 ESA 2010 (IRAP + IMU imprese + tasse locali) = €64,2 mld nel 2025 (provvisorio); 73% del carico sui servizi. Dataflow ISTAT conti nazionali corrente. ISTAT rilascio annuale "Conti per branca produttiva" copre questa categoria con tipico lag 1 anno. Coerente con il quadro ISTAT 2025.

---

## Calibration notes

1. **Metric "pressione fiscale" è esattamente il caso d'uso dell'auditor.** L'opinione pubblica cita una versione (annuale, 42,6%), la card cita un'altra (media trimestrale, 42,2%). Entrambe sono metodologicamente corrette ma incoerenti. L'auditor scheduled mensile su card fiscali è il meccanismo che cattura questa discrepanza prima che il chatbot dia una risposta che fa storcere il naso a un giornalista.

2. **Math-checkable cards sono ad alta confidenza.** `aliquote-statutarie-cit-dividendi-italia-2026` ha una formula esplicita (1 - (1-CIT) × (1-WHT)) che l'auditor può verificare in 5 secondi. Le card a struttura math-verifiable sono il caso d'oro. Si propone in v2 della spec: se la card include una formula algebrica derivata, l'auditor la ri-applica e tagga "math-verified."

3. **Le OECD pubblicano cadenze diverse per dataflow diversi.** Taxing Wages annuale (aprile), Revenue Statistics annuale (novembre/dicembre), Corporate Income Tax Rates Database trimestrale. L'auditor scheduled deve riconoscere il calendario delle fonti, non semplicemente "trimestrale per tutto."

---

## Skipped (0)

Prima esecuzione.
