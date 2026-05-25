"""Minimal interactive CLI for the ORA chatbot.

Usage:
    python -m agent.cli                 # interactive REPL
    python -m agent.cli "single query"  # one-shot

The REPL maintains an in-session 10-turn sliding window per decision 15.
"Nuova conversazione" (or Ctrl-D / Ctrl-C) resets the window.
"""

from __future__ import annotations

import sys

from agent.constants import CONVERSATION_HISTORY_TURNS
from agent.orchestrator import answer_query


def _print_answer(result) -> None:
    print()
    print("=" * 72)
    print(result.answer)
    print("=" * 72)
    if result.cited_chunk_ids:
        print(f"\nCitazioni ({len(result.cited_chunk_ids)}):")
        for cid in result.cited_chunk_ids:
            print(f"  - {cid}")
    if result.web_results:
        print(f"\nFonti web ({len(result.web_results)}):")
        for r in result.web_results:
            print(f"  - {r.get('source_url')}")
    print()
    print(
        f"[stage 1 type: {result.plan.get('query_type') if result.plan else '?'}  "
        f"refusal: {result.is_refusal}  "
        f"regen: {result.regen_count}  "
        f"elapsed: {result.elapsed_seconds:.1f}s]"
    )
    print()


def run_one_shot(query: str) -> None:
    result = answer_query(query, history=[])
    _print_answer(result)


def run_repl() -> None:
    print("ORA chatbot — MVP")
    print('Comandi: "nuova conversazione" per resettare; Ctrl-C per uscire.')
    print()
    history: list[dict[str, str]] = []
    while True:
        try:
            user_input = input("Tu: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nArrivederci.")
            return
        if not user_input:
            continue
        if user_input.lower() in {"nuova conversazione", "/nuova", "/reset"}:
            history = []
            print("[conversazione resettata]\n")
            continue
        result = answer_query(user_input, history=history)
        _print_answer(result)
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": result.answer})
        # Keep window
        if len(history) > CONVERSATION_HISTORY_TURNS * 2:
            history = history[-CONVERSATION_HISTORY_TURNS * 2:]


def main() -> None:
    if len(sys.argv) > 1:
        run_one_shot(" ".join(sys.argv[1:]))
    else:
        run_repl()


if __name__ == "__main__":
    main()
