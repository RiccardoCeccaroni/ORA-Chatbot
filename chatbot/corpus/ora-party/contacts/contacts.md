---
id: ora-contacts
type: contact
attribution: party
title: "ORA! — Organi e referenti del partito"
source_url: "https://ora-italia.it/partito/"
date_compiled: 2026-05-15
date_scraped: 2026-05-15
description: "Carta della struttura di contatto del partito ORA: segretario, presidente, segreteria nazionale, consiglio direttivo, assemblea nazionale, referenti territoriali. I valori puntuali (nomi, email, social) sono esposti dallo strumento contact_lookup; questa carta descrive solo la struttura. Decisione 24."
content_hash: f291457ce6a8b70ae941e2a1b141e755ef74fb5e7b633f3183f504f24958b91d
corpus_status: include
---

# ORA! — Organi e referenti del partito

Il partito ORA si articola su due assi di contatto:

- **Organi nazionali** — la struttura politico-organizzativa del partito.
- **Referenti territoriali** — una rete di referenti regionali ed esteri che cura la presenza del partito sul territorio.

## Organi nazionali

### Vertice del partito
- **Segretario** — Michele Boldrin. È il Segretario di ORA, eletto al congresso fondativo di Abano Terme (2025).
- **Presidente** — Alberto Forchielli. È il Presidente di ORA e cofondatore del partito insieme a Boldrin.

### Segreteria Nazionale
Organo collegiale che opera sotto la responsabilità del Segretario. Copre aree funzionali distinte (es. Innovazione, Comunicazione, Istruzione, Organizzazione e Territori, Programma & Lab). I membri attualmente censiti sono **12**. Pagina ufficiale: <https://ora-italia.it/partito/>.

### Consiglio Direttivo
Organo intermedio fra Segreteria Nazionale e Assemblea Nazionale. Membri censiti: **10**. Pagina ufficiale: <https://ora-italia.it/consiglio-direttivo/>.

### Assemblea Nazionale
Organo di rappresentanza più ampio del partito. Membri censiti: **85**. Pagina ufficiale: <https://ora-italia.it/assemblea-nazionale/>.

## Referenti territoriali

ORA è presente sull'intero territorio italiano tramite referenti regionali e in tre sezioni estere.

### Regioni d'Italia (20)
Abruzzo, Basilicata, Calabria, Campania, Emilia-Romagna, Friuli-Venezia Giulia, Lazio, Liguria, Lombardia, Marche, Molise, Piemonte, Puglia, Sardegna, Sicilia, Toscana, Trentino-Alto Adige, Umbria, Val d'Aosta, Veneto.

### Sezioni estere (3)
Americhe, Asia, Africa e Oceania, Europa.

Pagina ufficiale: <https://ora-italia.it/territorio/>.

## Come reperire un contatto specifico

Per ottenere il **nome**, l'**email** o i **profili social** di una persona o di un referente territoriale, l'agente deve chiamare lo strumento `contact_lookup` (decisione 24). Lo strumento accetta:

- `area` — slug regionale (`abruzzo`, `lombardia`, …) o estero (`americhe`, `asia`, `europa`) per i referenti territoriali;
- `role` — slug del ruolo nella segreteria (`innovazione`, `comunicazione`, `programma`, `tesoriere`, …);
- `name` — slug della persona (`michele-boldrin`, `andrea-savi`, …).

Lo strumento restituisce **solo i dati pertinenti alla richiesta** e impone un limite massimo di risultati. Per disegno (decisione 24, politica di superficie) le **richieste in blocco** — ad esempio "elenca tutti i membri con le loro email" — vengono **rifiutate**: il chatbot risponde solo a domande di contatto puntuali e su richiesta esplicita dell'utente.
