"""Whisper-transcribe a set of YouTube videos, replacing the YouTube auto-caption
versions currently in all_transcripts/.

Usage:
    python whisper_transcribe.py <video_id> [<video_id> ...]

Per video:
  1. Skip if _raw_whisper/<id>.json already exists and is well-formed (idempotent).
  2. yt-dlp -> audio stream (m4a/webm), saved to a temp dir.
  3. ffmpeg compress -> mono 16 kHz mp3 @ 24 kbps so 2h+ videos fit Whisper's 25MB cap.
  4. POST to OpenAI Whisper-1 in Italian, response_format=verbose_json.
  5. Save raw JSON to _raw_whisper/<id>.json; write cleaned text to
     all_transcripts/<safe_title> [<id>].txt (overwriting the YouTube auto-caption).
  6. Delete the compressed audio (we keep only the JSON as cold archive).

The OpenAI key is read from ../.secrets/api keys.txt — the parser looks
for an `sk-...` token that is NOT an Anthropic key (`sk-ant-...`).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from openai import OpenAI

import imageio_ffmpeg

HERE = Path(__file__).parent
PROJECT_ROOT = HERE.parent.parent  # .../ORA Chatbot - presentation/
KEY_FILE = PROJECT_ROOT / "build" / ".secrets" / "api keys.txt"
WHISPER_DIR = HERE / "_raw_whisper"
TRANSCRIPTS_DIR = HERE / "all_transcripts"
MANIFEST = TRANSCRIPTS_DIR / "_manifest.tsv"

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

WIN_FORBIDDEN = str.maketrans({
    ":": "：", "<": "＜", ">": "＞", "\"": "＂",
    "/": "／", "\\": "＼", "|": "｜", "?": "？", "*": "＊",
})


def get_api_key() -> str:
    """Find an OpenAI key in the shared secrets file (which holds multiple keys)."""
    text = KEY_FILE.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    # First pass: prefer a key on/near a line mentioning OpenAI.
    for i, line in enumerate(lines):
        if "openai" in line.lower():
            for cand in [line] + lines[i + 1 : i + 5]:
                m = re.search(r"sk-(?!ant-)[A-Za-z0-9_\-]{20,}", cand)
                if m:
                    return m.group(0)
    # Fallback: any sk- key that is not an Anthropic key.
    m = re.search(r"sk-(?!ant-)[A-Za-z0-9_\-]{20,}", text)
    if m:
        return m.group(0)
    raise RuntimeError(f"No OpenAI key found in {KEY_FILE}")


def load_manifest() -> dict[str, tuple[str, str]]:
    """Return {video_id: (title, playlists)} from the consolidated manifest."""
    out: dict[str, tuple[str, str]] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        vid, title, playlists = parts[0], parts[1], parts[2]
        out[vid] = (title, playlists)
    return out


def download_audio(vid: str, work_dir: Path) -> Path:
    """Download the smallest m4a audio-only stream available for the video."""
    out_pattern = str(work_dir / f"{vid}.%(ext)s")
    cmd = [
        "yt-dlp",
        "-f", "bestaudio[ext=m4a]/bestaudio",
        "-o", out_pattern,
        "--no-playlist",
        "--quiet", "--no-warnings",
        f"https://www.youtube.com/watch?v={vid}",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        raise RuntimeError(f"yt-dlp failed for {vid}: {res.stderr.strip() or res.stdout.strip()}")
    for cand in work_dir.iterdir():
        if cand.stem == vid and cand.suffix in (".m4a", ".webm", ".opus", ".mp3", ".mp4"):
            return cand
    raise RuntimeError(f"yt-dlp produced no audio file for {vid}")


def compress_audio(src: Path, vid: str, work_dir: Path) -> Path:
    """ffmpeg -> mono 16 kHz mp3 @ 24 kbps. ~180 KB/min, fits 2h+ in 25 MB."""
    dst = work_dir / f"{vid}.mp3"
    cmd = [
        FFMPEG, "-y", "-i", str(src),
        "-ac", "1", "-ar", "16000", "-b:a", "24k",
        "-vn",
        "-loglevel", "error",
        str(dst),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if res.returncode != 0 or not dst.exists():
        raise RuntimeError(f"ffmpeg failed for {vid}: {res.stderr.strip()}")
    return dst


def transcribe(audio: Path, vid: str, client: OpenAI) -> dict:
    """Call OpenAI Whisper. Returns the verbose_json payload as dict."""
    out = WHISPER_DIR / f"{vid}.json"
    if out.exists() and out.stat().st_size > 200:
        try:
            data = json.loads(out.read_text(encoding="utf-8"))
            if data.get("text"):
                return data
        except json.JSONDecodeError:
            pass  # re-transcribe
    with audio.open("rb") as f:
        resp = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="it",
            response_format="verbose_json",
        )
    data = resp.model_dump() if hasattr(resp, "model_dump") else dict(resp)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data


def reflow_paragraph(text: str, width: int = 90) -> str:
    words = text.split()
    lines: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for w in words:
        add = len(w) + (1 if cur else 0)
        if cur_len + add > width and cur:
            lines.append(" ".join(cur))
            cur = [w]
            cur_len = len(w)
        else:
            cur.append(w)
            cur_len += add
    if cur:
        lines.append(" ".join(cur))
    return "\n".join(lines)


def format_transcript(text: str) -> str:
    """Split into sentences, group into ~4-sentence paragraphs, reflow each."""
    text = text.strip()
    if not text:
        return ""
    # Split on sentence boundaries. Whisper puts periods/!/? followed by space.
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paragraphs: list[list[str]] = []
    cur: list[str] = []
    for s in sentences:
        cur.append(s.strip())
        if len(cur) >= 4:
            paragraphs.append(cur)
            cur = []
    if cur:
        paragraphs.append(cur)
    return "\n\n".join(reflow_paragraph(" ".join(p)) for p in paragraphs)


def write_transcript(vid: str, title: str, playlists: str, whisper_data: dict) -> Path:
    body = format_transcript(whisper_data.get("text", ""))
    safe = title.translate(WIN_FORBIDDEN)
    dest = TRANSCRIPTS_DIR / f"{safe} [{vid}].txt"
    duration = whisper_data.get("duration", 0)
    dur_str = f"{int(duration // 60)}m{int(duration % 60):02d}s" if duration else "n/a"
    header = (
        f"# {title}\n\n"
        f"YouTube: https://www.youtube.com/watch?v={vid}\n"
        f"Video ID: {vid}\n"
        f"Playlist(s): {playlists}\n"
        f"Transcription: OpenAI Whisper-1 (language=it)\n"
        f"Duration: {dur_str}\n\n"
        f"---\n\n"
    )
    dest.write_text(header + body + "\n", encoding="utf-8")
    return dest


def process_one(vid: str, manifest: dict[str, tuple[str, str]], client: OpenAI) -> tuple[str, int]:
    if vid not in manifest:
        raise RuntimeError(f"{vid} not in manifest")
    title, playlists = manifest[vid]

    # Idempotency: if JSON exists and is valid, just (re)write the txt and return.
    cached_json = WHISPER_DIR / f"{vid}.json"
    if cached_json.exists() and cached_json.stat().st_size > 200:
        try:
            data = json.loads(cached_json.read_text(encoding="utf-8"))
            if data.get("text"):
                write_transcript(vid, title, playlists, data)
                return ("cached", len(data["text"].split()))
        except json.JSONDecodeError:
            pass

    with tempfile.TemporaryDirectory(prefix=f"whisper_{vid}_") as td:
        work = Path(td)
        raw = download_audio(vid, work)
        small = compress_audio(raw, vid, work)
        data = transcribe(small, vid, client)
        write_transcript(vid, title, playlists, data)
        return ("ok", len(data.get("text", "").split()))


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python whisper_transcribe.py [--workers N] <video_id> [<video_id> ...]", file=sys.stderr)
        return 2
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    workers = 1
    ids: list[str] = []
    i = 0
    while i < len(argv):
        if argv[i] == "--workers" and i + 1 < len(argv):
            workers = max(1, int(argv[i + 1]))
            i += 2
        else:
            ids.append(argv[i])
            i += 1

    WHISPER_DIR.mkdir(exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(exist_ok=True)
    manifest = load_manifest()
    client = OpenAI(api_key=get_api_key())

    results: list[tuple[str, str, str, int]] = []  # (vid, status, title, words)

    def run_one(vid: str) -> tuple[str, str, str, int]:
        title = manifest.get(vid, ("?", ""))[0]
        print(f"[{vid}] START {title[:55]}", flush=True)
        try:
            status, words = process_one(vid, manifest, client)
            print(f"[{vid}] DONE  {status} ({words} words)", flush=True)
            return (vid, status, title, words)
        except Exception as e:
            print(f"[{vid}] FAIL  {e}", flush=True)
            return (vid, f"fail: {e}", title, 0)

    if workers == 1:
        for vid in ids:
            results.append(run_one(vid))
    else:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(run_one, vid) for vid in ids]
            for f in as_completed(futures):
                results.append(f.result())

    print("\n=== Summary ===", flush=True)
    ok = sum(1 for _, s, _, _ in results if s in ("ok", "cached"))
    print(f"Success: {ok}/{len(results)}", flush=True)
    for vid, status, title, words in results:
        if not status.startswith(("ok", "cached")):
            print(f"  FAIL [{vid}] {title}: {status}", flush=True)
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
