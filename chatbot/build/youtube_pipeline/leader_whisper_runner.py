"""Whisper-transcribe the 6 'Presidente e Segretario' leader videos.

Reuses download_audio / compress_audio / transcribe / get_api_key / format_transcript
/ reflow_paragraph helpers from whisper_transcribe.py — does NOT modify that script.

The 6 target videos are not in all_transcripts/_manifest.tsv (that's the party
pipeline manifest). This runner reads from leader_videos.tsv instead, writes
JSONs to the shared _raw_whisper/ folder, and writes plain-text transcripts to
leader_transcripts/.

Usage:
    python leader_whisper_runner.py [--workers N]
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from openai import OpenAI

from whisper_transcribe import (
    WHISPER_DIR,
    compress_audio,
    download_audio,
    format_transcript,
    get_api_key,
    transcribe,
    WIN_FORBIDDEN,
)

HERE = Path(__file__).parent
LEADER_MANIFEST = HERE / "leader_videos.tsv"
LEADER_TRANSCRIPTS_DIR = HERE / "leader_transcripts"


def load_leader_manifest() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
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


def write_leader_transcript(vid: str, title: str, playlist: str, whisper_data: dict) -> Path:
    body = format_transcript(whisper_data.get("text", ""))
    safe = title.translate(WIN_FORBIDDEN)
    dest = LEADER_TRANSCRIPTS_DIR / f"{safe} [{vid}].txt"
    duration = whisper_data.get("duration", 0)
    dur_str = f"{int(duration // 60)}m{int(duration % 60):02d}s" if duration else "n/a"
    header = (
        f"# {title}\n\n"
        f"YouTube: https://www.youtube.com/watch?v={vid}\n"
        f"Video ID: {vid}\n"
        f"Playlist: {playlist}\n"
        f"Transcription: OpenAI Whisper-1 (language=it)\n"
        f"Duration: {dur_str}\n\n"
        f"---\n\n"
    )
    dest.write_text(header + body + "\n", encoding="utf-8")
    return dest


def process_one(vid: str, row: dict[str, str], client: OpenAI) -> tuple[str, int]:
    title = row.get("title", "?")
    playlist = row.get("playlist", "Presidente e Segretario")

    cached_json = WHISPER_DIR / f"{vid}.json"
    if cached_json.exists() and cached_json.stat().st_size > 200:
        try:
            data = json.loads(cached_json.read_text(encoding="utf-8"))
            if data.get("text"):
                write_leader_transcript(vid, title, playlist, data)
                return ("cached", len(data["text"].split()))
        except json.JSONDecodeError:
            pass

    with tempfile.TemporaryDirectory(prefix=f"whisper_leader_{vid}_") as td:
        work = Path(td)
        raw = download_audio(vid, work)
        small = compress_audio(raw, vid, work)
        data = transcribe(small, vid, client)
        write_leader_transcript(vid, title, playlist, data)
        return ("ok", len(data.get("text", "").split()))


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    workers = 1
    i = 0
    while i < len(argv):
        if argv[i] == "--workers" and i + 1 < len(argv):
            workers = max(1, int(argv[i + 1]))
            i += 2
        else:
            i += 1

    WHISPER_DIR.mkdir(exist_ok=True)
    LEADER_TRANSCRIPTS_DIR.mkdir(exist_ok=True)
    manifest = load_leader_manifest()
    client = OpenAI(api_key=get_api_key())

    results: list[tuple[str, str, str, int]] = []

    def run_one(vid: str) -> tuple[str, str, str, int]:
        row = manifest[vid]
        title = row.get("title", "?")
        print(f"[{vid}] START {title[:55]}", flush=True)
        try:
            status, words = process_one(vid, row, client)
            print(f"[{vid}] DONE  {status} ({words} words)", flush=True)
            return (vid, status, title, words)
        except Exception as e:
            print(f"[{vid}] FAIL  {e}", flush=True)
            return (vid, f"fail: {e}", title, 0)

    ids = list(manifest.keys())

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
        print(f"  [{vid}] {status}: {title[:50]} ({words} words)", flush=True)
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
