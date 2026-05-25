# Content refresh — energia-ambiente-sostenibilita — 2026-05-13

## Item resolved

`capacita-generazione-elettrica-italia-2024` → emessa nuova card `capacita-generazione-elettrica-italia-2025.md`. Card 2024 **conservata** come snapshot storico (non eliminata); aggiunto banner cross-link al top con motivazioni esplicite (boom idro 2024 +30%, traiettoria capacità PV 37→43,5 GW).

## Fonte

- **Comunicato stampa Terna** "Nel 2025 fabbisogno elettrico pari a 311,3 TWh": <https://www.terna.it/it/media/comunicati-stampa/dettaglio/consumi-elettrici-2025> — pubblicato gennaio 2026 (data esatta non esposta nella pagina, ma il Rapporto Mensile gennaio 2026 conferma).
- **Rapporto Mensile sul Sistema Elettrico gennaio 2026** (sezione consuntivo annuale 2025): <https://download.terna.it/terna/Rapporto_mensile_gennaio_26_8de72eb920ebc63.pdf> (3,87 MB, archiviato).
- **Cross-validation** via stampa specializzata: regionieambiente.it, industriaitaliana.it, greenreport.it, affaritaliani.it, infobuildenergia.it, solareb2b.it (tutti coerenti col comunicato Terna).

## Numeri-chiave del consuntivo 2025

| Indicatore | TO_VERIFY (atteso) | Trovato | Δ |
|---|---|---|---|
| Domanda elettrica nazionale | 311,3 TWh stabile | **311,3 TWh** (−0,3% vs 2024) | 0 |
| Quota FER su consumi | 41,1% | **41,1%** (−0,9 pt vs 42,0% del 2024) | 0 |
| Fotovoltaico var. % | +25,1% | **+25,1%** (44,3 TWh, record) | 0 |
| Nuova capacità FER | +7,2 GW | **+7.191 MW (≈7,2 GW)** | 0 |
| Impianti accumulo | 884k per 17,9 GWh | **884.404 per 17,92 GWh; 7.362 MW** | 0 |

**Nessuna discrepanza >20%** vs TO_VERIFY. Tutti i numeri target confermati esattamente.

## Numeri aggiuntivi raccolti (non in TO_VERIFY)

- Produzione nazionale netta: **268 TWh** (+2,0% vs 2024) — copre 84,9% domanda.
- Import netto estero: **47,1 TWh** (15,1% domanda), **−8,1% vs 2024**.
- Idroelettrico: **−21,2%** (ritorno alla media post-anno eccezionale 2024).
- Eolico: −3,3%; Geotermico: −0,3%; Termoelettrica fossile: +4,6% (gas compensa idro).
- Carbone: −13,5% (in dismissione).
- Capacità FER installata fine 2025: **83,5 GW** (di cui PV 43,5 GW, eolico 13,6 GW).
- Accumuli — produzione stand-alone 2025: **1,5 TWh** (era 0,14 TWh nel 2024, +1000%).
- Accumuli — utility-scale aggiunti 2025: **723 MW** (il segmento sta decollando).
- Solo solare aggiunto 2025: **+6.437 MW** (era +6.700 MW nel 2024, −5,3%).
- Solo eolico aggiunto 2025: **+608 MW** (−11,2% vs 2024).
- Produzione FER totale: **130.937 GWh ≈ 131 TWh**, −2,3% vs 2024 (il record PV non compensa il crollo idrico).

## Decisione sulla card 2024 — conservata, non superseduta

Motivazioni:
1. **Boom idroelettrico 2024 (+30%, 54,8 TWh)** è un picco climatico raro; la card 2024 documenta l'anomalia. La 2025 non ne è una sostituzione narrativa.
2. **Riferimento per la fotografia della capacità PV** a metà strada (37,1 GW fine 2024 → 43,5 GW fine 2025). Utile per leggere la traiettoria di addizioni.
3. La 2024 ha breakdown GWh per fonte più dettagliato (Terna sezione 5 in PDF); la 2025 si appoggia al comunicato stampa con totali aggregati. **Le due card sono complementari, non sovrapposte.**
4. **Banner cross-link** al top della 2024 chiarisce inequivocabilmente al lettore (e al chatbot) che la 2025 è la lettura corrente.

## Caveat documentati nella card 2025

- Quota FER in arretramento è effetto del *denominatore idro*, non inversione strutturale (la media mobile 5-anni mostra ancora crescita).
- Fossili +4,6% è compensazione climatica, non cambio di policy.
- Discrepanza "quota su consumi 41,1%" vs "quota su generazione ~49%" — Terna pubblica entrambe; PNIEC/Eurostat usano la prima.
- 884k accumuli sono in larghissima parte residenziali piccoli (5-15 kWh); i 723 MW utility-scale 2025 sono il dato strategico per il bilanciamento.
- Per allineamento UE: cross-check con Eurostat `nrg_ind_ren` (D1) raccomandato come verifica supplementare.

## Sorgente raw archivata

```
_raw/energia-ambiente-sostenibilita/TERNA_CONSUNTIVO_2025/
├── comunicato_consumi_elettrici_2025.html   (201 KB, HTTP 200, snapshot pagina ufficiale)
└── Rapporto_mensile_gennaio_2026.pdf        (3,87 MB, HTTP 200, scaricato da download.terna.it)
```

## TO_VERIFY status

Voce marcata `[x] Risolto 2026-05-13` con 1-line summary inline.

## Script eseguiti

- `python /tmp/restructure_scope_a.py` — hashato 2 card (la nuova 2025 e la 2024 aggiornata con il banner).

## Block conditions check

- Pagine Terna 403/404? **No** — HTTP 200 su entrambe le risorse archiviate.
- Numeri >20% diversi da TO_VERIFY? **No** — match esatto sui 5 valori target.
- Release Terna 2025 non pubblicata? **No** — pubblicata regolarmente a gennaio 2026 come atteso.

Nessun escalation. Item chiuso autonomamente.
