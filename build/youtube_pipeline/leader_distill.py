"""Stage-1 distillation of Whisper transcripts into per-video LEADER-voice cards.

Sibling to distill.py — but treats output as the PERSONAL VIEW of a named leader
(Boldrin or Forchielli), strictly NOT as official ORA party position. Per
CLAUDE.md §3 (A2 tier): "Always cited as the member's personal view, never as
ORA's official position."

Usage:
    python leader_distill.py --speaker <slug> <video_id> [<video_id> ...]

where <slug> is `boldrin` or `forchielli`.

Per video:
  1. Load Whisper verbose-JSON (with segment timestamps) from _raw_whisper/.
  2. Load video metadata from leader_videos.tsv (sibling of _manifest.tsv).
  3. Build a leader-voice prompt that filters strictly to the named leader.
  4. Call Anthropic API (claude-sonnet-4-6).
  5. Write the card to leader_distillations/<safe_title> [<id>] ({slug}).md.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

from anthropic import Anthropic

HERE = Path(__file__).parent
PROJECT_ROOT = HERE.parent.parent  # .../ORA Chatbot - presentation/
KEY_FILE = PROJECT_ROOT / "build" / ".secrets" / "api keys.txt"
WHISPER_DIR = HERE / "_raw_whisper"
LEADER_TRANSCRIPTS_DIR = HERE / "leader_transcripts"
LEADER_DISTILLATIONS_DIR = HERE / "leader_distillations"
LEADER_MANIFEST = HERE / "leader_videos.tsv"

MODEL = "claude-sonnet-4-6"

WIN_FORBIDDEN = str.maketrans({
    ":": "：", "<": "＜", ">": "＞", "\"": "＂",
    "/": "／", "\\": "＼", "|": "｜", "?": "？", "*": "＊",
})

LEADER_INFO: dict[str, dict[str, str]] = {
    "boldrin":    {"full_name": "Michele Boldrin",    "role": "Segretario",  "tier": "A2a"},
    "forchielli": {"full_name": "Alberto Forchielli", "role": "Presidente",  "tier": "A2b"},
}


def get_anthropic_key() -> str:
    text = KEY_FILE.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"sk-ant-[A-Za-z0-9_\-]+", text)
    if not m:
        raise RuntimeError("No Anthropic key found in api keys.txt")
    return m.group(0)


def load_leader_manifest() -> dict[str, dict[str, str]]:
    """Returns {video_id: {title, playlist, date_published, speakers}} from leader_videos.tsv."""
    out: dict[str, dict[str, str]] = {}
    if not LEADER_MANIFEST.exists():
        raise RuntimeError(f"Missing {LEADER_MANIFEST}")
    lines = LEADER_MANIFEST.read_text(encoding="utf-8").splitlines()
    if not lines:
        return out
    header = lines[0].split("\t")
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        row = {header[i]: parts[i] if i < len(parts) else "" for i in range(len(header))}
        vid = row.get("video_id", "").strip()
        if vid:
            out[vid] = row
    return out


def format_transcript_with_timestamps(whisper_json: dict) -> str:
    """[MM:SS] timestamps on every Whisper segment."""
    segs = whisper_json.get("segments", [])
    if not segs:
        return whisper_json.get("text", "")
    lines: list[str] = []
    for s in segs:
        start = int(s.get("start", 0))
        mm, ss = divmod(start, 60)
        text = s.get("text", "").strip()
        if text:
            lines.append(f"[{mm:02d}:{ss:02d}] {text}")
    return "\n".join(lines)


PROMPT_TEMPLATE = """Sei un analista che estrae le OPINIONI PERSONALI di {LEADER_FULL_NAME} ({LEADER_ROLE} del partito ORA) da un video del canale YouTube ufficiale di ORA.

Queste sono opinioni PERSONALI di {LEADER_FULL_NAME}. NON sono posizioni ufficiali del partito ORA. Mai usare frasi come "la posizione del partito" — sempre "la posizione personale di {LEADER_FULL_NAME}". Mai dire "ORA ritiene", "il partito propone", o simili. Sempre "{LEADER_FULL_NAME} ritiene", "{LEADER_FULL_NAME} propone", "secondo {LEADER_FULL_NAME}".

ORA è un partito centrista italiano. {LEADER_FULL_NAME} è {LEADER_ROLE} del partito. Il chatbot di ORA userà il tuo output come materiale di TIER A2 (voce personale del leader), usato per riempire i vuoti del TIER A1 (voce ufficiale del partito), sempre etichettato come visione personale e mai confuso con la posizione ufficiale.

## Regole

1. **Fedeltà**: estrai SOLO ciò che è detto letteralmente. Niente inferenze, niente plausibility-fill, niente estrapolazioni.

2. **Filtro speaker — STRETTISSIMO**: estrai SOLO le affermazioni fatte da {LEADER_FULL_NAME}. Scarta TUTTE le affermazioni di chiunque altro — inclusi altri membri di ORA, ospiti esterni, intervistatori, e qualsiasi altro speaker. Questo è il punto cruciale: anche se un altro membro di ORA dice qualcosa di rilevante, NON estrarlo. Solo {LEADER_FULL_NAME}.

3. **Uno speaker per bullet**: ogni bullet termina con `*{LEADER_FULL_NAME}, ~{{mm:ss}}*`. Niente altri speaker, niente attribuzioni miste, niente `*?, ~mm:ss*`.

4. **Niente meta-commenti**: estrai solo claim effettivamente espressi nella trascrizione. NIENTE note su cosa manca, NIENTE rinvii a documenti esterni (es. "*non citato verbalmente*", "*riferimento nella tesi*"). Se una sezione non ha contenuto, scrivi `_(nessun contenuto)_` e basta.

5. **Inferenza dello speaker**: la trascrizione non ha etichette di speaker. Inferisci dai marcatori conversazionali: chiamate per nome, turni domanda-risposta, e dai metadati del video qui sotto. {SPEAKER_HINT}

6. **Scarta**: saluti, chiacchiere su meteo/viaggi, format-meta ("oggi parliamo di..."), battute interne, aneddoti biografici che NON ancorano un punto di policy o di visione personale, reazioni del pubblico, false partenze a metà frase.

7. **Tieni**: opinioni personali dichiarate, catene di ragionamento, diagnosi della situazione corrente, misure concrete proposte da {LEADER_FULL_NAME}, affermazioni empiriche (numeri, tassi, date) con le cifre esatte dello speaker, confronti con altri partiti o critiche, cautele e incertezze esplicite, citazioni distintive.

8. **Aneddoti personali**: tienili SOLO quando ancorano un punto di policy o di visione (es. cita un'esperienza per giustificare una proposta). Scarta narrazione pura.

## Output

Produci SOLO il corpo della scheda (le 7 sezioni `##` qui sotto). Niente frontmatter, niente preambolo, niente commenti fuori dalle sezioni. Sezioni vuote ricevono `_(nessun contenuto)_`.

Ogni bullet termina con la provenienza: `*{LEADER_FULL_NAME}, ~{{mm:ss}}*`. Usa i timestamp dai marcatori `[MM:SS]` della trascrizione.

## Sezioni

## Posizioni personali
Opinioni personali esplicite di {LEADER_FULL_NAME} (su politica, policy, partito, attualità).

## Razionale / diagnosi
Ragionamenti, affermazioni causali, diagnosi della situazione corrente fatti da {LEADER_FULL_NAME}.

## Misure proposte
Azioni/misure/programmi specifici proposti da {LEADER_FULL_NAME} (con condizioni, ambito, tempistica se menzionati).

## Affermazioni empiriche (verifica via tier-dati)
Affermazioni quantitative o fattuali di {LEADER_FULL_NAME} — preserva le cifre esatte e le citazioni di fonte se presenti.

## Confronti politici / critiche
Affermazioni di {LEADER_FULL_NAME} su posizioni di altri partiti, critiche, contrasti.

## Cautele / non-impegni
Cautele, cose esplicitamente NON impegnate da {LEADER_FULL_NAME}, condizioni, incertezze.

## Citazioni distintive
Citazioni verbatim di {LEADER_FULL_NAME} (≤30 parole ciascuna) che catturano il suo framing distintivo.

---

## Input

### Metadata video
- Titolo: {VIDEO_TITLE}
- Speaker target (estraibile): {LEADER_FULL_NAME} ({LEADER_ROLE})
- Altri speaker presenti (DA SCARTARE): {OTHER_SPEAKERS}
- Data: {DATE}
- Playlist: {PLAYLIST}

### Trascrizione (timestamp `[MM:SS]`)
{TRANSCRIPT}
"""


def build_prompt(
    speaker_slug: str,
    title: str,
    playlist: str,
    date_pub: str,
    transcript: str,
    all_speakers_in_video: list[str],
) -> str:
    info = LEADER_INFO[speaker_slug]
    leader_full = info["full_name"]
    leader_role = info["role"]

    others = [s for s in all_speakers_in_video if s != leader_full]
    if others:
        other_speakers_str = ", ".join(others)
        speaker_hint = (
            f"Questo video ha più di uno speaker. Oltre a {leader_full}, parla anche: "
            f"{other_speakers_str}. Estrai SOLO le frasi di {leader_full}. Scarta tutto il resto."
        )
    else:
        other_speakers_str = "(nessuno — video solista)"
        speaker_hint = (
            f"Questo video è un monologo di {leader_full}. Tutti i contenuti sostantivi sono suoi."
        )

    out = PROMPT_TEMPLATE
    for placeholder, value in {
        "{LEADER_FULL_NAME}": leader_full,
        "{LEADER_ROLE}": leader_role,
        "{SPEAKER_HINT}": speaker_hint,
        "{VIDEO_TITLE}": title,
        "{OTHER_SPEAKERS}": other_speakers_str,
        "{DATE}": date_pub or "(sconosciuta)",
        "{PLAYLIST}": playlist,
        "{TRANSCRIPT}": transcript,
    }.items():
        out = out.replace(placeholder, value)
    return out


def distill_one(
    vid: str,
    speaker_slug: str,
    manifest: dict[str, dict[str, str]],
    client: Anthropic,
) -> Path:
    if speaker_slug not in LEADER_INFO:
        raise RuntimeError(f"Unknown speaker slug: {speaker_slug}")
    if vid not in manifest:
        raise RuntimeError(f"{vid} not in leader manifest")

    row = manifest[vid]
    title = row.get("title", "")
    playlist = row.get("playlist", "Presidente e Segretario")
    date_pub = row.get("date_published", "")
    speakers_field = row.get("speakers", "").strip()
    all_speakers = [s.strip() for s in speakers_field.split(",") if s.strip()] if speakers_field else []

    info = LEADER_INFO[speaker_slug]
    if info["full_name"] not in all_speakers:
        raise RuntimeError(
            f"{vid}: {info['full_name']} not listed in speakers field ({speakers_field!r}) — refusing to distill."
        )

    whisper_path = WHISPER_DIR / f"{vid}.json"
    if not whisper_path.exists():
        raise RuntimeError(f"No Whisper JSON for {vid}")
    whisper = json.loads(whisper_path.read_text(encoding="utf-8"))
    transcript = format_transcript_with_timestamps(whisper)

    prompt = build_prompt(speaker_slug, title, playlist, date_pub, transcript, all_speakers)

    resp = client.messages.create(
        model=MODEL,
        max_tokens=6000,
        messages=[{"role": "user", "content": prompt}],
    )
    body = resp.content[0].text.strip()

    LEADER_DISTILLATIONS_DIR.mkdir(exist_ok=True)
    safe = title.translate(WIN_FORBIDDEN)
    dest = LEADER_DISTILLATIONS_DIR / f"{safe} [{vid}] ({speaker_slug}).md"

    h = hashlib.sha256(body.encode("utf-8")).hexdigest()
    duration_sec = whisper.get("duration", 0)
    duration_str = (
        f"{int(duration_sec // 60)}m{int(duration_sec % 60):02d}s" if duration_sec else "n/a"
    )

    frontmatter_lines = [
        "---",
        f"id: youtube-{vid}-{speaker_slug}",
        "type: leader_event_distillation",
        f"attribution: {speaker_slug}",
        f"tier: {info['tier']}",
        f"speaker: {info['full_name']}",
        f'title: "{title}"',
        f'source_url: "https://www.youtube.com/watch?v={vid}"',
        f'date_published: "{date_pub}"',
        f'date_compiled: "{date.today().isoformat()}"',
        f'playlist: "{playlist}"',
        f"duration: {duration_str}",
        f"content_hash: {h}",
        f"distillation_model: {MODEL}",
        f"transcription: whisper-1",
        "---",
        "",
        f"# {title}",
        "",
        f"_Voce personale di {info['full_name']} ({info['role']} di ORA). Non costituisce posizione ufficiale del partito._",
        "",
        body,
        "",
    ]
    dest.write_text("\n".join(frontmatter_lines), encoding="utf-8")
    return dest


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    speaker_slug = None
    ids: list[str] = []
    i = 0
    while i < len(argv):
        if argv[i] == "--speaker" and i + 1 < len(argv):
            speaker_slug = argv[i + 1]
            i += 2
        else:
            ids.append(argv[i])
            i += 1

    if not speaker_slug or not ids:
        print(
            "Usage: python leader_distill.py --speaker <boldrin|forchielli> <video_id> [<video_id> ...]",
            file=sys.stderr,
        )
        return 2

    manifest = load_leader_manifest()
    client = Anthropic(api_key=get_anthropic_key())

    for vid in ids:
        title = manifest.get(vid, {}).get("title", "?")
        print(f"[{vid}] ({speaker_slug}) {title[:55]}", flush=True)
        try:
            dest = distill_one(vid, speaker_slug, manifest, client)
            print(f"  -> {dest.name}", flush=True)
        except Exception as e:
            print(f"  FAIL: {e}", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
