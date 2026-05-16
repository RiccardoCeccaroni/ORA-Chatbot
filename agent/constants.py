"""Constants for the ORA chatbot agent — models, collection names, defaults."""

# Models (decision 09 + 11.D)
# 2026-05-15 rework: agent simplified, verifier dropped, synthesizer restored
# to Opus. Sonnet kept as a constant for possible future use (e.g., if cost
# becomes critical we can flip the synthesizer back).
OPUS_MODEL = "claude-opus-4-7"        # planner + synthesizer
SONNET_MODEL = "claude-sonnet-4-6"    # unused at runtime; kept for fast-flip
HAIKU_MODEL = "claude-haiku-4-5"      # web-summarizer (verify_answer no longer called)

# Voyage models (decisions 05 + 07)
EMBEDDING_MODEL = "voyage-4-large"
RERANK_MODEL = "rerank-2.5"
VECTOR_DIM = 1024

# Qdrant (decision 06)
COLLECTION_NAME = "ora_chunks"

# Retrieval defaults (decision 07)
RETRIEVE_TOP_K_INITIAL = 50           # dense ANN candidate pool
RETRIEVE_TOP_K_FINAL = 10             # after reranking
DATA_TOP_K_FINAL = 5                  # data-lookup returns fewer; stat-cards are denser

# Memory (decision 15)
CONVERSATION_HISTORY_TURNS = 10       # sliding window
SESSION_IDLE_TIMEOUT_MIN = 30

# Verifier (decision 11.D + 23) — REMOVED 2026-05-15 in the agent rework.
# Groundedness is now solely the responsibility of the deterministic citation
# enforcement step in orchestrator.enforce_citations() + the weekly chat_log
# review mandated by decision 11.E. The model verifier (Haiku then Sonnet)
# produced too many false refusals to justify its cost+latency.
# Constant kept at 0 for legacy callers; nothing inside the orchestrator reads it.
VERIFIER_MAX_REGEN = 0

# Retrieval tier policy (Riccardo 2026-05-14):
# - other-parties is retrieved ONLY when query_type=compare AND user explicitly
#   asked for comparison with another party. Standalone "what does PD think?"
#   → off_scope_other_party_only refusal.
# - The bot is about ORA; it never goes to other-parties unprompted.
#
# Tier labels must match what chunk_corpus.py:tier_for() emits.
# Updated 2026-05-15 (decision 25): added A1c-event (party_event_distillation)
#   + A2-<leader>-event (leader_event_distillation). Backfilled previously-missing
#   labels: A1-contacts (decision 24), A1-statuto / A1-fondamenti / A1-codice-etico
#   (this session's identity-slice work), A2-<leader>-article (existing leader_article).
ORA_TIERS = [
    # A1 — party voice
    "A1a",                    # tesi
    "A1b",                    # comunicato
    "A1c",                    # newsletter_section
    "A1c-event",              # party_event_distillation (decision 25)
    "A1-identity",            # identity card
    "A1-contacts",            # contacts card (decision 24)
    "A1-statuto",             # statuto (governance bylaws)
    "A1-fondamenti",          # fondamenti (Allegato 2 — 15 policy fundamentals)
    "A1-codice-etico",        # codice etico (Allegato 3)
    # A2 — leader voice (Boldrin)
    "A2-boldrin",             # leader_topic_profile
    "A2-boldrin-article",     # leader_article (nFA 2006–2014)
    "A2-boldrin-event",       # leader_event_distillation (decision 25)
    # A2 — leader voice (Forchielli)
    "A2-forchielli",          # leader_topic_profile
    "A2-forchielli-event",    # leader_event_distillation (decision 25)
]
OTHER_PARTIES_TIER = "other-parties"
