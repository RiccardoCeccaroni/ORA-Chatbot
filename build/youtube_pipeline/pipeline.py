"""End-to-end pipeline: YouTube input → audio → Whisper → Stage-1 distillation.

Usage:
    python pipeline.py <input> [<input> ...]

Input forms:
  - YouTube video URL:    https://www.youtube.com/watch?v=...
  - YouTube playlist URL: https://www.youtube.com/playlist?list=...
  - Raw 11-char video ID
  - --batch all           process every video already in the manifest
  - --workers N           parallel Whisper workers (default 4)

For each resolved video ID:
  1. Fetch yt-dlp metadata if not in manifest (title, upload date, playlist).
  2. Whisper-transcribe if _raw_whisper/<id>.json missing.
  3. Distill if distillations/<title>[<id>].md missing.

Idempotent and safe to re-run. Inputs already on disk are skipped.
"""

from __future__ import annotations

import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from anthropic import Anthropic
from openai import OpenAI

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# Re-use the proven primitives from the existing scripts.
from whisper_transcribe import (  # noqa: E402
    process_one as whisper_one,
    get_api_key as get_openai_key,
)
from distill import (  # noqa: E402
    distill_one,
    load_members,
    load_manifest,
    load_upload_dates,
    get_anthropic_key,
    WHISPER_DIR,
    DISTILLATIONS_DIR,
    MANIFEST,
    UPLOAD_DATES,
    WIN_FORBIDDEN,
)


def resolve_inputs(inputs: list[str]) -> list[str]:
    """Expand mixed inputs (URLs / playlists / IDs / 'all') to a list of video IDs."""
    ids: list[str] = []
    seen: set[str] = set()

    def add(vid: str) -> None:
        if vid and vid not in seen:
            seen.add(vid)
            ids.append(vid)

    for inp in inputs:
        if inp == "all":
            for k in load_manifest().keys():
                add(k)
            continue
        # Playlist URL
        m = re.search(r"[?&]list=([\w\-]+)", inp)
        if m and "playlist" in inp:
            res = subprocess.run(
                ["yt-dlp", "--flat-playlist", "--print", "%(id)s", inp],
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            for line in (res.stdout or "").splitlines():
                v = line.strip()
                if len(v) == 11:
                    add(v)
            continue
        # Video URL with v=
        m = re.search(r"[?&]v=([\w\-]{11})", inp)
        if m:
            add(m.group(1))
            continue
        # Bare 11-char ID
        if re.fullmatch(r"[\w\-]{11}", inp):
            add(inp)
            continue
        print(f"  ignored (not a URL/ID): {inp}", file=sys.stderr)
    return ids


def ensure_metadata(
    vid: str,
    manifest: dict[str, tuple[str, str]],
    upload_dates: dict[str, str],
) -> tuple[str, str, str]:
    """Return (title, playlist, date_pub). Fetch via yt-dlp + append to TSVs if new."""
    if vid in manifest and vid in upload_dates:
        title, playlists = manifest[vid]
        return title, playlists, upload_dates[vid]

    res = subprocess.run(
        ["yt-dlp", "--skip-download", "--extractor-args", "youtube:lang=it", "--print",
         "%(title)s\t%(upload_date)s\t%(playlist_title)s",
         f"https://www.youtube.com/watch?v={vid}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    line = (res.stdout or "").strip().splitlines()[0] if res.stdout else ""
    parts = line.split("\t")
    title = parts[0] if parts and parts[0] else vid
    upload_raw = parts[1] if len(parts) > 1 else ""
    playlist = parts[2] if len(parts) > 2 and parts[2] not in ("NA", "") else ""

    upload_iso = (
        f"{upload_raw[:4]}-{upload_raw[4:6]}-{upload_raw[6:]}"
        if len(upload_raw) == 8 and upload_raw.isdigit()
        else upload_raw
    )

    if vid not in manifest:
        with MANIFEST.open("a", encoding="utf-8") as f:
            safe = title.translate(WIN_FORBIDDEN)
            f.write(f"{vid}\t{title}\t{playlist}\t{safe} [{vid}].txt\t0\n")
        manifest[vid] = (title, playlist)

    if vid not in upload_dates:
        with UPLOAD_DATES.open("a", encoding="utf-8") as f:
            f.write(f"{vid}\t{upload_raw}\n")
        upload_dates[vid] = upload_iso

    return title, playlist, upload_iso


def needs_distill(title: str, vid: str) -> bool:
    safe = title.translate(WIN_FORBIDDEN)
    return not (DISTILLATIONS_DIR / f"{safe} [{vid}].md").exists()


def needs_whisper(vid: str) -> bool:
    p = WHISPER_DIR / f"{vid}.json"
    return not (p.exists() and p.stat().st_size > 200)


def process_one(
    vid: str,
    manifest: dict[str, tuple[str, str]],
    upload_dates: dict[str, str],
    members: list[str],
    externals: list[str],
    openai_client: OpenAI,
    anthropic_client: Anthropic,
) -> tuple[str, str]:
    title, playlists, _ = ensure_metadata(vid, manifest, upload_dates)
    print(f"[{vid}] {title[:60]}", flush=True)

    if needs_whisper(vid):
        print(f"  whisper...", flush=True)
        whisper_one(vid, manifest, openai_client)
    else:
        print(f"  whisper: cached", flush=True)

    if needs_distill(title, vid):
        print(f"  distill...", flush=True)
        distill_one(vid, manifest, upload_dates, members, externals, anthropic_client)
    else:
        print(f"  distill: cached", flush=True)

    print(f"[{vid}] DONE", flush=True)
    return (vid, "ok")


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    workers = 4
    inputs: list[str] = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--workers" and i + 1 < len(argv):
            workers = max(1, int(argv[i + 1]))
            i += 2
        elif a == "--batch" and i + 1 < len(argv):
            inputs.append(argv[i + 1])
            i += 2
        else:
            inputs.append(a)
            i += 1

    if not inputs:
        print("Usage: python pipeline.py <url|id|all> [--workers N]", file=sys.stderr)
        return 2

    ids = resolve_inputs(inputs)
    print(f"Resolved {len(ids)} video IDs to process (workers={workers})\n", flush=True)
    if not ids:
        return 0

    manifest = load_manifest()
    upload_dates = load_upload_dates()
    members, externals = load_members()
    openai_client = OpenAI(api_key=get_openai_key())
    anthropic_client = Anthropic(api_key=get_anthropic_key())

    results: list[tuple[str, str]] = []
    if workers == 1:
        for vid in ids:
            try:
                results.append(process_one(vid, manifest, upload_dates, members, externals, openai_client, anthropic_client))
            except Exception as e:
                print(f"[{vid}] FAIL: {e}", flush=True)
                results.append((vid, f"fail: {e}"))
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(process_one, v, manifest, upload_dates, members, externals, openai_client, anthropic_client): v for v in ids}
            for fut in as_completed(futures):
                v = futures[fut]
                try:
                    results.append(fut.result())
                except Exception as e:
                    print(f"[{v}] FAIL: {e}", flush=True)
                    results.append((v, f"fail: {e}"))

    print("\n=== Summary ===", flush=True)
    ok = sum(1 for _, s in results if s == "ok")
    print(f"Success: {ok}/{len(results)}", flush=True)
    for vid, status in results:
        if status != "ok":
            print(f"  FAIL [{vid}]: {status}", flush=True)
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
