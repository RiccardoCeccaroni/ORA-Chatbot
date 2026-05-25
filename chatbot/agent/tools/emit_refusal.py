"""emit_refusal — return the right Italian refusal template per reason code.

Templates per decision 11. Centralized so phrasing stays consistent and is
updatable in one place.
"""

from __future__ import annotations

REFUSAL_REASONS = {
    "no_corpus_position",
    "off_scope",
    "off_scope_other_party_only",
    "roleplay",
    "loaded_no_underlying_policy",
    "verifier_failed",
    "data_unavailable",
    "comparison_other_party_unknown",
    "timeout",
}


def emit_refusal(reason: str, *, related_topic_lens: str | None = None, topic: str | None = None) -> str:
    """Returns the Italian refusal phrase for the given reason code.

    `related_topic_lens` is used for off-scope redirect.
    `topic` is interpolated into a few templates that name what we don't have.
    """
    if reason == "no_corpus_position":
        if topic:
            return f"ORA! non ha una posizione documentata su {topic}."
        return "ORA! non ha una posizione documentata su questo."

    if reason == "off_scope":
        if related_topic_lens:
            return (
                f"Non posso darti consigli sul tuo caso specifico, ma la posizione di ORA! "
                f"su {related_topic_lens} è documentata — vuoi che te la riporti?"
            )
        return (
            "Sono un chatbot dedicato alle posizioni politiche di ORA! — non posso darti "
            "consigli su questioni mediche, legali o personali. Posso però illustrarti "
            "la posizione del partito su temi correlati, se ti interessa."
        )

    if reason == "off_scope_other_party_only":
        other = topic or "quel partito"
        return (
            f"Sono un chatbot dedicato a ORA! — non rispondo a domande dirette su {other} "
            "o altri partiti per conto loro. Posso però **confrontare** la posizione di "
            "ORA! con quella di un altro partito su un tema specifico, se lo desideri "
            f"(per esempio: «Qual è la differenza tra ORA! e {other} su [tema]?»)."
        )

    if reason == "roleplay":
        # See decision 11.B — chatbot transparency, no impersonation
        return (
            "Sono un chatbot, non Boldrin né Forchielli — non posso impersonare nessuno né "
            "generare loro virgolettati che non esistano. Posso però riportare quello che "
            "hanno scritto o detto pubblicamente sul tema, con le citazioni. La mia "
            "ricostruzione potrebbe contenere errori — verifica sempre le fonti."
        )

    if reason == "loaded_no_underlying_policy":
        return (
            "La domanda non si traduce in una questione di policy concreta su cui ORA! "
            "abbia una posizione documentata. Se vuoi, riformulala in termini di "
            "obiettivi o misure specifiche e cercherò la posizione del partito."
        )

    if reason == "verifier_failed":
        return (
            "Non sono riuscito a produrre una risposta che fosse pienamente sostenuta "
            "dalle fonti disponibili. Per evitare errori, preferisco non rispondere su "
            "questo punto specifico. Puoi riformulare la domanda o chiedere su un tema correlato."
        )

    if reason == "data_unavailable":
        if topic:
            return f"Non dispongo di dati affidabili su {topic} dalle fonti che consulto (ISTAT, Banca d'Italia, MEF, Eurostat, ISS, OECD)."
        return "Non dispongo di dati affidabili su questo dalle fonti che consulto."

    if reason == "comparison_other_party_unknown":
        party = topic or "quel partito"
        return f"Non ho una posizione documentata di {party} su questo tema, quindi non posso fare un confronto affidabile."

    if reason == "timeout":
        return (
            "Si è verificato un problema tecnico durante l'elaborazione della tua domanda. "
            "Riprova tra un momento."
        )

    # Default fallback
    return "Non sono in grado di rispondere a questa domanda in modo affidabile."
