"""Constants for the ORA! MCP server — models, collection, retrieval defaults.

Lifted from the original ORA chatbot project (agent/constants.py) and pruned
to the retrieval-only subset. Synthesizer / verifier / memory constants are
not relevant to an MCP server, which only does retrieval.
"""

# Voyage models — must match the embedding model used at index time
EMBEDDING_MODEL = "voyage-4-large"
RERANK_MODEL = "rerank-2.5"
VECTOR_DIM = 1024

# Qdrant — collection name is shared with the original project's index
COLLECTION_NAME = "ora_chunks"

# Attribution values as they actually appear in the Qdrant payloads.
# Verified 2026-05-23 by scrolling the live index; see tests/probe_attribution.py.
# The original chatbot's tooling sets these on every chunk in chunk_corpus.py.
PARTY_ATTRIBUTION = "party"                       # official ORA voice (615 chunks)
LEADER_ATTRIBUTIONS = ["boldrin", "forchielli"]   # leader personal output
OTHER_PARTIES_ATTRIBUTIONS = [                    # one per comparison party
    "azione", "pd", "fdi", "iv", "fi", "avs", "lega", "m5s",
]

# Retrieval defaults (kept identical to the chatbot for behavioral parity)
RETRIEVE_TOP_K_INITIAL = 50      # dense ANN candidate pool
RETRIEVE_TOP_K_FINAL = 10        # after reranking
DATA_TOP_K_FINAL = 5             # stat-cards are denser, return fewer

# Tier labels — must match what build/chunk_corpus.py:tier_for() emits in
# the original project. Exposed in the MCP tool schemas so host AIs can
# filter retrieval by trust tier.
ORA_TIERS = [
    # A1 — party voice
    "A1a",                    # tesi (manifesto theses)
    "A1b",                    # comunicato
    "A1c",                    # newsletter_section
    "A1c-event",              # party_event_distillation
    "A1-identity",            # identity card
    "A1-contacts",            # contacts card
    "A1-statuto",             # statuto (governance bylaws)
    "A1-fondamenti",          # fondamenti (15 policy fundamentals)
    "A1-codice-etico",        # codice etico
    # A2 — leader voice (Boldrin)
    "A2-boldrin",
    "A2-boldrin-article",
    "A2-boldrin-event",
    # A2 — leader voice (Forchielli)
    "A2-forchielli",
    "A2-forchielli-event",
]
OTHER_PARTIES_TIER = "other-parties"
