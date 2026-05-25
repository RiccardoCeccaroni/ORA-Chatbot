"""Stage-1 distillation of Whisper transcripts into per-video party-voice cards.

Usage:
    python distill.py <video_id> [<video_id> ...]

For each ID:
  1. Load Whisper verbose-JSON (with segment timestamps).
  2. Load the matching tesi text (for `(estende/raffina/contraddice/nuovo)` tags).
  3. Load members.yaml (speaker filter — only ORA members' claims are extractable).
  4. Build a Sonnet-4.6 prompt with the 6-section schema.
  5. Call Anthropic API.
  6. Write the card to distillations/<safe_title> [<id>].md with full frontmatter.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml
from anthropic import Anthropic

HERE = Path(__file__).parent
PROJECT_ROOT = HERE.parent.parent  # .../ORA Chatbot - presentation/
KEY_FILE = PROJECT_ROOT / "build" / ".secrets" / "api keys.txt"
WHISPER_DIR = HERE / "_raw_whisper"
TRANSCRIPTS_DIR = HERE / "all_transcripts"
DISTILLATIONS_DIR = HERE / "distillations"
MEMBERS_FILE = HERE / "members.yaml"
MANIFEST = TRANSCRIPTS_DIR / "_manifest.tsv"
UPLOAD_DATES = HERE / "_upload_dates.tsv"
MANIFESTO_DIR = PROJECT_ROOT / "corpus" / "ora-party" / "manifesto"

MODEL = "claude-sonnet-4-6"

# Video → tesi mapping. 50 videos pre-mapped; new videos fall back to LLM
# classification via classify_tesi(). The agricoltura tesi (#01) is missing
# from the corpus per CLAUDE.md §8.3, so the Programmapres agricoltura video
# distills with no tesi reference (every claim tagged `(nuovo)`).
VIDEO_TESI: dict[str, list[int]] = {
    # === Il Programma di ORA! (16) ===
    "Mc41tvKhWQY": [7, 4],   # Esteri e Difesa
    "qDjnZfiVWC4": [5],      # Diritti Civili
    "zdLdYlZqNjI": [15],     # Pari opportunità e Inclusione
    "dMQ3_L9Vsms": [21],     # Università
    "PqmsuwPVhx8": [8],      # Giustizia
    "H5iuLjHKOoc": [],       # Agricoltura — tesi missing from corpus
    "LSIBU1Yeltw": [20],     # Unione Europea
    "1B-l8LWq1pw": [6],      # Energia, Ambiente, Sostenibilità
    "e_VFkzB9Dz8": [17],     # Spesa Pubblica
    "k4hAY723b8g": [19],     # Tassazione e Fiscalità
    "hqb5NQ7FZks": [13],     # Istruzione
    "N_jydqv8QXI": [12],     # Innovazione
    "2Lqd9B-hcl0": [18],     # Sviluppo Economico
    "oLQKVTBgnl4": [16],     # Sanità
    "2gPMBT6lIBs": [10],     # Immigrazione
    "4OxwOXjdp0E": [14],     # Lavoro e Politiche Sociali
    # === Presentazione Tesi (11 transcribed) ===
    "w9PupB72_Vg": [12],     # Innovazione e Crescita
    "qmo7GtfvKM4": [18],     # Sviluppo Economico
    "4CeywmWehiA": [7],      # Esteri e Relazioni Internazionali
    "UK48hXhFQ6c": [13],     # Istruzione
    "LgtMHPsM6Zk": [9],      # Governance, Riforme istituzionali
    "Z0g3jO-xPAs": [3],      # Cultura, Sport, Turismo
    "c3tMqjcoJvQ": [14],     # Lavoro e Politiche Sociali
    "1ewWgRefDZA": [5, 15],  # Diritti civili + Pari opportunità
    "S0w8peX4UjI": [21],     # Università e Ricerca
    "MMHssSHUlKM": [10, 2],  # Interni (immigrazione + comuni)
    "7_ZEGOGLenM": [16],     # Salute e Servizi Sanitari
    # === Giustizia playlist (unique, excl. Programmapres) ===
    "ZngxcBmM4pA": [8],      # Presentazione Tesi - Giustizia
    "jbgLTfUDIeQ": [8],      # con Sesta (external, Boldrin's claims only)
    "o0suYIitBrQ": [8],      # con Cassese (external, Boldrin's claims only)
    # === Università playlist (unique) ===
    "LysNxK2RY5U": [21],     # con Bizzarri (external; Boldrin/Forchielli claims)
    "uCOwoEwt1VY": [21, 12], # Università e impresa
    "8tb7kAaWuRA": [21],     # Pisa Coraggio dell'Ovvio
    "yU3ujuiE0tI": [21, 14], # salari, crisi universitaria
    # === Sanità playlist (unique) ===
    "2ASG8eJ6AZc": [16],
    "h08-LN50rk4": [16],
    "y3t2CJQqSAE": [16],
    "xlUaAxFGeOA": [16],     # Merigliano-Molteni (Molteni external)
    "PTjvhzcGMD0": [16],     # Skeptical Health (external)
    "zQ88HKcUoSo": [16],
    "1P-Z5kRH2Ug": [16],
    "wFpvG7vfzQg": [16],
    "nQihdcc1UnI": [16],
    "y4xPFzM25Tc": [16],
    "YeYSarq-VvA": [16],
    "eF-nN72qMgU": [16],
    "XBIrrKcBvhY": [16],
    "ItwhAbsRt-U": [16],
    "1jHMmXKc924": [16, 17], # Legge di Bilancio Sanità
    "VgYqswx9CBE": [16],
}

WIN_FORBIDDEN = str.maketrans({
    ":": "：", "<": "＜", ">": "＞", "\"": "＂",
    "/": "／", "\\": "＼", "|": "｜", "?": "？", "*": "＊",
})


def get_anthropic_key() -> str:
    text = KEY_FILE.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"sk-ant-[A-Za-z0-9_\-]+", text)
    if not m:
        raise RuntimeError("No Anthropic key found in api keys.txt")
    return m.group(0)


def load_members() -> tuple[list[str], list[str]]:
    data = yaml.safe_load(MEMBERS_FILE.read_text(encoding="utf-8"))
    members = [m["name"] for m in data.get("members", [])]
    externals = [m["name"] for m in data.get("external_guests", [])]
    return members, externals


def load_manifest() -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 3:
            out[parts[0]] = (parts[1], parts[2])
    return out


def load_upload_dates() -> dict[str, str]:
    out: dict[str, str] = {}
    if not UPLOAD_DATES.exists():
        return out
    for line in UPLOAD_DATES.read_text(encoding="utf-8").splitlines():
        parts = line.strip().split("\t")
        if len(parts) >= 2 and parts[0]:
            d = parts[1]
            if len(d) == 8 and d.isdigit():
                out[parts[0]] = f"{d[:4]}-{d[4:6]}-{d[6:]}"
            elif d and d != "NA":
                out[parts[0]] = d
    return out


def find_tesi_file(tesi_num: int) -> Path | None:
    """Find <NN>-*.md under the manifesto dir."""
    pat = f"{tesi_num:02d}-*.md"
    matches = list(MANIFESTO_DIR.glob(pat))
    return matches[0] if matches else None


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


PROMPT_TEMPLATE = """Sei un analista che estrae contenuti politici attribuibili al partito ORA da un video pubblicato sul canale YouTube ufficiale del partito.

ORA è un partito centrista italiano, fondato e guidato da Michele Boldrin (Segretario) e Alberto Forchielli (Presidente). Il chatbot di ORA userà il tuo output per **dichiarare**, **proiettare**, **giustificare** e **confrontare** le posizioni del partito.

## Regole

1. **Fedeltà**: estrai SOLO ciò che è detto letteralmente. Niente inferenze, niente plausibility-fill, niente estrapolazioni.
2. **Filtro speaker — STRETTO**: estrai solo affermazioni fatte da un membro ORA della lista qui sotto. Scarta le affermazioni di ospiti esterni (Cassese, Sesta, Bizzarri, Molteni, Skeptical Health, ecc.) o di chiunque NON sia nella lista. Le *risposte* di un membro ORA a una domanda di un ospite esterno SONO estraibili.
3. **Uno speaker per bullet**: ogni bullet ha ESATTAMENTE uno speaker. Se un pensiero è co-formulato da due membri, dividi in due bullet separati o attribuisci al membro che lo ha formulato in modo più chiaro. Mai `*Nome1 / Nome2, ~mm:ss*`.
4. **Niente meta-commenti**: estrai solo claim effettivamente espressi nella trascrizione. NIENTE note su cosa manca, NIENTE rinvii a documenti esterni (es. "*non citato verbalmente*", "*riferimento nella tesi*"). Se una sezione non ha contenuto, scrivi `_(nessun contenuto)_` e basta.
5. **Inferenza dello speaker**: la trascrizione non ha etichette di speaker. Inferisci dai marcatori conversazionali: chiamate per nome ("Allora Stefano, raccontami..."), turni domanda-risposta (l'host fa domande, l'ospite risponde), e dal formato del video (sotto trovi gli speaker probabili).
6. **Scarta**: saluti, chiacchiere su meteo/viaggi, format-meta ("oggi parliamo di..."), battute interne, aneddoti biografici che NON ancorano un punto di policy, reazioni del pubblico, false partenze a metà frase.
7. **Tieni**: posizioni dichiarate, catene di ragionamento, diagnosi della situazione corrente, misure concrete proposte, affermazioni empiriche (numeri, tassi, date) con le cifre esatte dello speaker, confronti con altri partiti, cautele e incertezze esplicite.
8. **Aneddoti personali**: tienili SOLO quando ancorano un punto di policy (es. un medico cita pazienti visti per giustificare una proposta sui tempi di attesa). Scarta narrazione pura.

## Output

Produci SOLO il corpo della scheda (le 7 sezioni `##` qui sotto). Niente frontmatter, niente preambolo, niente commenti fuori dalle sezioni. Sezioni vuote ricevono `_(nessun contenuto)_`.

Ogni bullet termina con la provenienza: `*{nome speaker}, ~{mm:ss}*`. Usa i timestamp dai marcatori `[MM:SS]` della trascrizione. Se lo speaker non è chiaro: `*?, ~mm:ss*`.

{TESI_TAG_INSTRUCTIONS}

## Sezioni

## Posizioni dichiarate
Posizioni esplicite dichiarate da membri ORA.

## Razionale / diagnosi
Ragionamenti, affermazioni causali, diagnosi della situazione corrente.

## Misure concrete proposte
Azioni/misure/programmi specifici (con condizioni, ambito, tempistica se menzionati).

## Affermazioni empiriche (verifica via tier-dati)
Affermazioni quantitative o fattuali — preserva le cifre esatte e le citazioni di fonte se presenti.

## Confronti con altri partiti
Affermazioni su posizioni di altri partiti o critiche.

## Cautele / non-impegni
Cautele, cose esplicitamente NON impegnate, condizioni, incertezze.

## Citazioni distintive
Citazioni verbatim (≤30 parole ciascuna) che catturano il framing distintivo dello speaker.

---

## Input

### Membri ORA (solo le loro affermazioni sono estraibili)
{MEMBER_LIST}

### Ospiti esterni (scarta le loro affermazioni)
{EXTERNAL_GUESTS}

{TESI_BLOCK}

### Metadata video
- Titolo: {VIDEO_TITLE}
- Speaker probabili (formato Il Programma di ORA! = Boldrin + un working-group lead): {LIKELY_SPEAKERS}
- Data: {DATE}
- Playlist: {PLAYLIST}

### Trascrizione (timestamp `[MM:SS]`)
{TRANSCRIPT}
"""


def build_prompt(
    vid: str,
    title: str,
    playlist: str,
    date_pub: str,
    transcript: str,
    members: list[str],
    externals: list[str],
    tesi_blocks: list[tuple[int, str]],
) -> str:
    member_lines = ", ".join(members)
    external_lines = ", ".join(externals)

    if tesi_blocks:
        nums = [str(n) for n, _ in tesi_blocks]
        tag_instr = (
            f"Per le affermazioni che toccano le tesi T{'/T'.join(nums)}, aggiungi un tag finale al bullet:\n"
            f"  - `(estende T<N>)` — elabora un punto della tesi\n"
            f"  - `(raffina T<N>)` — chiarisce/raffina la posizione\n"
            f"  - `(contraddice T<N>)` — sembra diverso dalla tesi\n"
            f"  - `(nuovo)` — affronta qualcosa NON presente nella tesi\n"
            f"  - `(ripete T<N>)` — ribadisce la posizione della tesi"
        )
        tesi_text_block = "\n\n".join(
            f"### Tesi {n}\n{txt}" for n, txt in tesi_blocks
        )
    else:
        tag_instr = "Per ogni affermazione, aggiungi il tag `(nuovo)` (non c'è una tesi di riferimento per questo video)."
        tesi_text_block = "### Tesi\n_(nessuna tesi di riferimento per questo video — il tema non è ancora coperto dalle tesi programmatiche)_"

    likely = "Michele Boldrin (host) + il responsabile del gruppo di lavoro su questo tema (l'ospite, da identificare dalla trascrizione)"

    out = PROMPT_TEMPLATE
    for placeholder, value in {
        "{TESI_TAG_INSTRUCTIONS}": tag_instr,
        "{MEMBER_LIST}": member_lines,
        "{EXTERNAL_GUESTS}": external_lines,
        "{TESI_BLOCK}": tesi_text_block,
        "{VIDEO_TITLE}": title,
        "{LIKELY_SPEAKERS}": likely,
        "{DATE}": date_pub or "(sconosciuta)",
        "{PLAYLIST}": playlist,
        "{TRANSCRIPT}": transcript,
    }.items():
        out = out.replace(placeholder, value)
    return out


def distill_one(
    vid: str,
    manifest: dict[str, tuple[str, str]],
    upload_dates: dict[str, str],
    members: list[str],
    externals: list[str],
    client: Anthropic,
) -> Path:
    if vid not in manifest:
        raise RuntimeError(f"{vid} not in manifest")
    title, playlists = manifest[vid]
    date_pub = upload_dates.get(vid, "")

    whisper_path = WHISPER_DIR / f"{vid}.json"
    if not whisper_path.exists():
        raise RuntimeError(f"No Whisper JSON for {vid}")
    whisper = json.loads(whisper_path.read_text(encoding="utf-8"))
    transcript = format_transcript_with_timestamps(whisper)

    tesi_nums = VIDEO_TESI.get(vid)
    if tesi_nums is None:
        # Unmapped video — try LLM classification against the 21 tesi titles.
        tesi_nums = classify_tesi(title, client)
    tesi_blocks: list[tuple[int, str]] = []
    for n in tesi_nums:
        p = find_tesi_file(n)
        if p:
            tesi_blocks.append((n, p.read_text(encoding="utf-8")))

    prompt = build_prompt(vid, title, playlists, date_pub, transcript, members, externals, tesi_blocks)

    resp = client.messages.create(
        model=MODEL,
        max_tokens=6000,
        messages=[{"role": "user", "content": prompt}],
    )
    body = resp.content[0].text.strip()

    # Parse unique speakers from provenance tags
    speakers = extract_speakers(body, members)
    speakers_slugs = [name_to_slug(s, members) for s in speakers]

    DISTILLATIONS_DIR.mkdir(exist_ok=True)
    safe = title.translate(WIN_FORBIDDEN)
    dest = DISTILLATIONS_DIR / f"{safe} [{vid}].md"

    h = hashlib.sha256(body.encode("utf-8")).hexdigest()
    duration_sec = whisper.get("duration", 0)
    duration_str = f"{int(duration_sec // 60)}m{int(duration_sec % 60):02d}s" if duration_sec else "n/a"

    speakers_yaml = "[" + ", ".join(speakers_slugs) + "]"
    frontmatter_lines = [
        "---",
        f"id: youtube-{vid}",
        "type: party_event_distillation",
        "attribution: party",
        f'title: "{title}"',
        f'source_url: "https://www.youtube.com/watch?v={vid}"',
        f'date_published: "{date_pub}"',
        f'date_compiled: "{date.today().isoformat()}"',
        f'playlist: "{playlists}"',
        f"speakers: {speakers_yaml}",
        f"tesi_touched: [{', '.join(str(n) for n in tesi_nums)}]",
        f"duration: {duration_str}",
        f"content_hash: {h}",
        f"distillation_model: {MODEL}",
        f"transcription: whisper-1",
        "---",
        "",
        f"# {title}",
        "",
        body,
        "",
    ]
    dest.write_text("\n".join(frontmatter_lines), encoding="utf-8")
    return dest


def extract_speakers(body: str, members: list[str]) -> list[str]:
    """Return unique ORA-member speaker names found in `*Name, ~mm:ss*` tags."""
    pattern = re.compile(r"\*([^,*]+?),\s*~\d{1,2}:\d{2}\*")
    found: set[str] = set()
    members_lower = {m.lower(): m for m in members}
    for m in pattern.finditer(body):
        name = m.group(1).strip()
        if not name or name == "?":
            continue
        # Defensive: handle `Name1 / Name2` even though prompt forbids it.
        for part in re.split(r"\s*/\s*", name):
            key = part.strip().lower()
            if key in members_lower:
                found.add(members_lower[key])
    return sorted(found)


def name_to_slug(name: str, members: list[str]) -> str:
    """Convert a member name to its slug using members.yaml. Best-effort fallback."""
    data = yaml.safe_load(MEMBERS_FILE.read_text(encoding="utf-8"))
    for m in data.get("members", []):
        if m["name"] == name:
            return m["slug"]
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def classify_tesi(title: str, client: Anthropic) -> list[int]:
    """LLM classification of an unmapped video title → tesi numbers."""
    tesi_index = sorted(MANIFESTO_DIR.glob("*.md"))
    tesi_list = "\n".join(f"- T{int(t.stem[:2])}: {t.stem[3:].replace('-', ' ')}" for t in tesi_index)
    msg = (
        f"Dato il titolo di un video YouTube del partito ORA, identifica quale "
        f"delle tesi programmatiche il video probabilmente affronta. Rispondi con "
        f"i numeri delle tesi separati da virgola (es. '16' o '7, 4'), oppure 'none' "
        f"se nessuna tesi è chiaramente attinente.\n\n"
        f"Tesi disponibili:\n{tesi_list}\n\n"
        f"Titolo: {title}\n\n"
        f"Numeri delle tesi (solo numeri):"
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=50,
        messages=[{"role": "user", "content": msg}],
    )
    text = resp.content[0].text.strip().lower()
    if "none" in text or "nessuna" in text:
        return []
    nums: list[int] = []
    for m in re.finditer(r"\b(\d{1,2})\b", text):
        n = int(m.group(1))
        if 1 <= n <= 21 and n not in nums:
            nums.append(n)
    return nums


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python distill.py <video_id> [<video_id> ...]", file=sys.stderr)
        return 2
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    manifest = load_manifest()
    upload_dates = load_upload_dates()
    members, externals = load_members()
    client = Anthropic(api_key=get_anthropic_key())

    for vid in argv:
        title = manifest.get(vid, ("?", ""))[0]
        print(f"[{vid}] {title[:60]}", flush=True)
        try:
            dest = distill_one(vid, manifest, upload_dates, members, externals, client)
            print(f"  -> {dest.name}", flush=True)
        except Exception as e:
            print(f"  FAIL: {e}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
