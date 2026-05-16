"""Chunk the retrievable ORA corpus into a single JSONL file.

Implements decision 04 (DECIDED 2026-05-13): structure-aware, per content type,
with stable parent_id on every chunk (so future bolt-on of D / parent expansion
is a generation-time change, not a re-chunk).

Atomic units (locked):
  - tesi:                  ## Contesto + each ### under ## Proposte
  - leader_topic_profile / party_topic_profile:
                           ## Sintesi + each ### under ## Posizioni documentate
                           + ## Evoluzione nel tempo (if present)
  - comunicato:            1 chunk per doc; paragraph-cluster split if >1200 tok
  - newsletter_section:    1 chunk per file
  - identity:              per ##
  - contact:               per ## (decision 24 — Organi nazionali / Referenti
                           territoriali / Come reperire un contatto specifico)
  - party_event_distillation / leader_event_distillation:
                           per ## (decision 25 — YouTube cards; sections include
                           Posizioni dichiarate, Razionale / diagnosi, Misure
                           concrete proposte, Affermazioni empiriche, Confronti,
                           Cautele, Citazioni distintive). Empty sections containing
                           only `_(nessun contenuto)_` are skipped.
  - data:                  per ## (Snapshot / Table / Caveats); skip ## Sorgente raw
  - leader_article:        paragraph-cluster split, soft cap ~500 tok

Chunk-level conventions (locked):
  - Contextual header prepended to each chunk's `text` field
    (parent title + heading path, e.g. "Tesi 06 — …\nSezione: Proposte > Politiche energetiche")
  - Inline per-stance citation links kept verbatim in chunk text
  - Oversized ### blocks kept whole (no hard cap; faithfulness > size uniformity)
  - No overlap between sibling chunks
  - Markdown images stripped; tables kept verbatim
  - Skip sections: ## Problemi, ## Quadri analitici, ## Concordanze e divergenze,
                   ## Riferimenti, ## Sorgente raw

Output: `build/chunks.jsonl`, one JSON object per line.
Re-run is idempotent — overwrites the file.

Usage:
    python chunk_corpus.py            # dry-run (default), prints summary
    python chunk_corpus.py --apply    # write chunks.jsonl
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Iterable


def _json_default(o: Any):
    if isinstance(o, (_dt.date, _dt.datetime)):
        return o.isoformat()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

import yaml
import tiktoken

# ---------------------------------------------------------------------------
# Constants & config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
OUT_PATH = Path(__file__).resolve().parent / "chunks.jsonl"

SOFT_CAP_TOKENS = 500     # paragraph-cluster split target
COMUNICATO_SPLIT_THRESHOLD = 1200  # paragraph-split a comunicato above this
COMUNICATO_SPLIT_TARGET = 600

# Sections that never get embedded.
SKIP_HEADINGS = {
    "Problemi",
    "Quadri analitici",
    "Concordanze e divergenze",
    "Concordanze e divergenze con l'altro leader",
    "Riferimenti",
    "Sorgente raw",
    "Sorgenti raw",
    "Tesi Programmatica",  # H4 label inside tesi
}

# H2 framing sections retained for profiles (in addition to the per-### positions).
PROFILE_FRAMING_H2 = {"Sintesi", "Evoluzione nel tempo"}

# Tier label mapping by (doc_type, attribution) hint.
def tier_for(doc_type: str, attribution: str, path: Path) -> str:
    if doc_type == "tesi":
        return "A1a"
    if doc_type == "comunicato":
        return "A1b"
    if doc_type == "newsletter_section":
        return "A1c"
    if doc_type == "identity":
        return "A1-identity"
    if doc_type == "contact":
        return "A1-contacts"
    if doc_type == "statuto":
        return "A1-statuto"
    if doc_type == "fondamenti":
        return "A1-fondamenti"
    if doc_type == "codice_etico":
        return "A1-codice-etico"
    if doc_type == "party_event_distillation":
        return "A1c-event"
    if doc_type == "leader_event_distillation":
        return f"A2-{attribution}-event"
    if doc_type == "leader_topic_profile":
        return f"A2-{attribution}"
    if doc_type == "leader_article":
        return f"A2-{attribution}-article"
    if doc_type in ("party_topic_profile", "party_programme"):
        return "other-parties"
    if doc_type == "data":
        return "data"
    return "unknown"


ENCODER = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    return len(ENCODER.encode(text))


# ---------------------------------------------------------------------------
# Frontmatter & inclusion
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")  # ![alt](url)


def under_underscore(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(part.startswith("_") for part in rel.parts[:-1])


def parse_doc(path: Path) -> tuple[dict, str] | None:
    """Return (frontmatter_dict, body_str) or None on parse failure."""
    text = path.read_text(encoding="utf-8")
    # Strip BOM if present
    if text.startswith("﻿"):
        text = text.lstrip("﻿")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    body = text[m.end():]
    return fm, body


def is_retrievable(fm: dict, path: Path, root: Path) -> bool:
    """Implements the §5 inclusion rule from CLAUDE.md."""
    status = fm.get("corpus_status")
    if status == "include":
        return True
    if status == "exclude":
        return False
    # Status absent → include iff no underscore folder in path
    return not under_underscore(path, root)


# ---------------------------------------------------------------------------
# Body parsing into a heading tree
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass
class Section:
    level: int          # 1..6
    heading: str        # text after the #s
    body_lines: list[str] = field(default_factory=list)
    children: list["Section"] = field(default_factory=list)
    parent: "Section | None" = field(default=None, repr=False)

    def body_text(self) -> str:
        return "\n".join(self.body_lines).strip()

    def heading_path(self) -> list[str]:
        path: list[str] = []
        n: Section | None = self
        while n and n.parent is not None:  # skip the root sentinel
            path.insert(0, n.heading)
            n = n.parent
        return path


def parse_into_sections(body: str) -> Section:
    """Build a hierarchical section tree. Root has level=0."""
    root = Section(level=0, heading="")
    stack: list[Section] = [root]
    for line in body.splitlines():
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip()
            sec = Section(level=level, heading=heading)
            # Pop stack to a parent with lower level
            while stack and stack[-1].level >= level:
                stack.pop()
            sec.parent = stack[-1]
            stack[-1].children.append(sec)
            stack.append(sec)
        else:
            stack[-1].body_lines.append(line)
    return root


def effective_root(root: Section) -> Section:
    """If the document is wrapped in a single H1 title (H1 with no H1 siblings,
    and all other top-level content is under it), return that H1 as the working
    root so handlers can iterate its H2 children directly. Otherwise return root
    unchanged. Handles the data/identity case where `# Title` precedes all `##`
    sections."""
    h1s = [c for c in root.children if c.level == 1]
    if len(h1s) == 1 and not any(c.level >= 2 for c in root.children):
        return h1s[0]
    return root


def find_section(root: Section, heading: str, level: int | None = None) -> Section | None:
    """First descendant matching heading (case-insensitive) and optionally level."""
    target = heading.strip().lower()
    def walk(s: Section):
        for c in s.children:
            if c.heading.strip().lower() == target and (level is None or c.level == level):
                return c
            r = walk(c)
            if r is not None:
                return r
        return None
    return walk(root)


# ---------------------------------------------------------------------------
# Text utilities
# ---------------------------------------------------------------------------

def strip_images(text: str) -> str:
    return IMAGE_RE.sub("", text)


def section_full_text(sec: Section) -> str:
    """Body of this section + all descendant sections (headings + bodies), in document order."""
    parts: list[str] = []
    if sec.body_text():
        parts.append(sec.body_text())
    for c in sec.children:
        parts.append("#" * c.level + " " + c.heading)
        sub = section_full_text(c).strip()
        if sub:
            parts.append(sub)
    return "\n\n".join(p for p in parts if p)


def paragraph_split(text: str) -> list[str]:
    """Split on blank lines; each returned item is a paragraph (possibly multi-line)."""
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def cluster_paragraphs(paragraphs: list[str], target_tokens: int = SOFT_CAP_TOKENS) -> list[str]:
    """Greedy paragraph-cluster split with a soft token cap."""
    clusters: list[str] = []
    buf: list[str] = []
    buf_tok = 0
    for p in paragraphs:
        p_tok = count_tokens(p)
        if buf and buf_tok + p_tok > target_tokens:
            clusters.append("\n\n".join(buf))
            buf, buf_tok = [], 0
        buf.append(p)
        buf_tok += p_tok
    if buf:
        clusters.append("\n\n".join(buf))
    return clusters


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower())
    s = re.sub(r"\s+", "-", s).strip("-")
    return s[:80]


# ---------------------------------------------------------------------------
# Chunk emission
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    chunk_id: str
    parent_id: str
    doc_type: str
    attribution: str
    tier: str
    anchor: str            # heading path joined with " > "
    tokens: int
    text: str              # body + prepended contextual header
    source_url: str | None
    date_published: Any
    content_hash: str | None
    extras: dict[str, Any] = field(default_factory=dict)


def emit_chunk(
    *,
    fm: dict,
    doc_type: str,
    parent_id: str,
    unit_slug: str,
    heading_path: list[str],
    body: str,
    title: str | None,
    extras: dict[str, Any] | None = None,
) -> Chunk:
    body = strip_images(body).strip()
    header_parts = []
    if title:
        header_parts.append(title.strip())
    if heading_path:
        header_parts.append("Sezione: " + " > ".join(heading_path))
    header = "\n".join(header_parts)
    full_text = (header + "\n\n" + body) if header else body
    chunk_id = f"{parent_id}::{unit_slug}" if unit_slug else parent_id
    return Chunk(
        chunk_id=chunk_id,
        parent_id=parent_id,
        doc_type=doc_type,
        attribution=str(fm.get("attribution", "")),
        tier=tier_for(doc_type, str(fm.get("attribution", "")), Path()),
        anchor=" > ".join(heading_path) if heading_path else "(root)",
        tokens=count_tokens(full_text),
        text=full_text,
        source_url=fm.get("source_url"),
        date_published=fm.get("date_published"),
        content_hash=fm.get("content_hash"),
        extras=extras or {},
    )


# ---------------------------------------------------------------------------
# Per-type handlers
# ---------------------------------------------------------------------------

TESI_SKIP_H2 = {
    "Tesi Programmatica",  # H4 label inside title H2 — but also appears as own H2
    "Problemi", "Problema",
    "Riferimenti",
    "Glossario",
    "Conclusione",
}


def _tesi_emit_section(
    fm: dict, parent_id: str, title: str,
    section: Section, heading_path: list[str], unit_slug: str,
) -> Chunk | None:
    body_text = section_full_text(section).strip()
    if not body_text:
        return None
    return emit_chunk(
        fm=fm, doc_type="tesi", parent_id=parent_id,
        unit_slug=unit_slug,
        heading_path=heading_path,
        body=body_text,
        title=title,
    )


def handle_tesi(fm: dict, body: str) -> list[Chunk]:
    """Robust to three observed tesi shapes:

    Pattern 1 (single-theme): `## Contesto`, `## Problemi`, `## Proposte` → `### N.`
    Pattern 2 (multi-theme):  `## Theme A` → `### Contesto/Proposte/Problemi`;
                              proposte children may be `### N.` body or `#### N.` children
    Pattern 3 (irregular):    `### Proposte` at H3 with sibling numbered items
    """
    chunks: list[Chunk] = []
    root = parse_into_sections(body)
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))

    # Detect file-title H2 (the heading whose text matches the file title or comes
    # before any Contesto/Proposte). Skip it as an emit target but recurse into it
    # for nested H3/H4 content if the file uses the rare H2-title-as-container pattern.
    top_h2s = [c for c in root.children if c.level == 2]
    proposte_at_h2 = any(c.heading.lower() == "proposte" for c in top_h2s)
    contesto_at_h2 = any(c.heading.lower() == "contesto" for c in top_h2s)

    # --- Top-level Contesto (Patterns 1 + parts of 2): emit if present
    ctx = find_section(root, "Contesto", level=2)
    if ctx:
        c = _tesi_emit_section(fm, parent_id, title, ctx, ["Contesto"], "contesto")
        if c: chunks.append(c)

    # --- Top-level Proposte at H2 (Pattern 1): emit each ### inside
    proposte = find_section(root, "Proposte", level=2)
    if proposte and any(child.level == 3 for child in proposte.children):
        for h3 in proposte.children:
            if h3.level != 3 or h3.heading in SKIP_HEADINGS or h3.heading in TESI_SKIP_H2:
                continue
            c = _tesi_emit_section(
                fm, parent_id, title, h3,
                ["Proposte", h3.heading],
                f"proposte/{slugify(h3.heading)}",
            )
            if c: chunks.append(c)

    # --- Pattern 2: multi-theme — each non-skip ## H2 (besides Contesto/Problemi/Proposte/title)
    # may itself contain ### Contesto/Proposte/Problemi
    for h2 in top_h2s:
        if h2.heading.lower() in {"contesto", "proposte", "problemi", "problema"}:
            continue
        if h2.heading in SKIP_HEADINGS or h2.heading in TESI_SKIP_H2:
            continue
        # Is this h2 the file-title sentinel? Heuristic: it has no Contesto/Proposte
        # descendants AND it's the only non-skip H2 → treat as title, recurse for H3s.
        # But normally for Pattern 2 themes, h2 has ### Contesto / ### Proposte.
        h2_contesto = find_section(h2, "Contesto", level=3)
        h2_proposte = find_section(h2, "Proposte", level=3)

        if h2_contesto or h2_proposte:
            # Pattern 2 theme
            if h2_contesto:
                c = _tesi_emit_section(
                    fm, parent_id, title, h2_contesto,
                    [h2.heading, "Contesto"],
                    f"{slugify(h2.heading)}/contesto",
                )
                if c: chunks.append(c)
            if h2_proposte:
                # If H3 Proposte has H4 children → emit per H4 (Pattern 2b)
                # Else emit H3 Proposte body itself (Pattern 2a)
                h4_children = [c for c in h2_proposte.children if c.level == 4 and c.heading not in SKIP_HEADINGS]
                if h4_children:
                    for h4 in h4_children:
                        c = _tesi_emit_section(
                            fm, parent_id, title, h4,
                            [h2.heading, "Proposte", h4.heading],
                            f"{slugify(h2.heading)}/proposte/{slugify(h4.heading)}",
                        )
                        if c: chunks.append(c)
                else:
                    c = _tesi_emit_section(
                        fm, parent_id, title, h2_proposte,
                        [h2.heading, "Proposte"],
                        f"{slugify(h2.heading)}/proposte",
                    )
                    if c: chunks.append(c)
        else:
            # Theme H2 with neither sub-Contesto nor sub-Proposte.
            # If this is the file-title H2 (Pattern 1 file), it should have ### Tesi Programmatica
            # and that's it — skip. Otherwise treat as a theme body chunk.
            non_skip_children = [
                ch for ch in h2.children
                if ch.heading not in SKIP_HEADINGS and ch.heading not in TESI_SKIP_H2
            ]
            if h2.body_text().strip() or non_skip_children:
                # Pattern 3 fallback or theme without sub-structure: emit each non-skip H3 if any,
                # else the whole H2 body.
                h3_children = [ch for ch in h2.children if ch.level == 3 and ch.heading not in SKIP_HEADINGS and ch.heading not in TESI_SKIP_H2]
                if h3_children and not (proposte_at_h2 and h2 is top_h2s[0]):
                    # This is likely Pattern 3 (innovazione-crescita): emit each ###
                    for h3 in h3_children:
                        c = _tesi_emit_section(
                            fm, parent_id, title, h3,
                            [h2.heading, h3.heading],
                            f"{slugify(h2.heading)}/{slugify(h3.heading)}",
                        )
                        if c: chunks.append(c)
                elif not h3_children and h2.body_text().strip():
                    c = _tesi_emit_section(
                        fm, parent_id, title, h2,
                        [h2.heading],
                        slugify(h2.heading),
                    )
                    if c: chunks.append(c)

    return chunks


def handle_profile(fm: dict, body: str, doc_type: str) -> list[Chunk]:
    """Both leader_topic_profile and party_topic_profile."""
    chunks: list[Chunk] = []
    root = effective_root(parse_into_sections(body))
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", "")) or f"{fm.get('attribution', '')} — {fm.get('topic_slug', '')}"

    # Sintesi
    sintesi = find_section(root, "Sintesi", level=2)
    if sintesi and section_full_text(sintesi).strip():
        chunks.append(emit_chunk(
            fm=fm, doc_type=doc_type, parent_id=parent_id,
            unit_slug="sintesi",
            heading_path=["Sintesi"],
            body=section_full_text(sintesi),
            title=title,
        ))

    # Posizioni documentate → each ###
    posizioni = find_section(root, "Posizioni documentate", level=2)
    if posizioni:
        for h3 in posizioni.children:
            if h3.level != 3:
                continue
            if h3.heading in SKIP_HEADINGS:
                continue
            body_text = section_full_text(h3).strip()
            if not body_text:
                continue
            chunks.append(emit_chunk(
                fm=fm, doc_type=doc_type, parent_id=parent_id,
                unit_slug=f"posizioni/{slugify(h3.heading)}",
                heading_path=["Posizioni documentate", h3.heading],
                body=body_text,
                title=title,
            ))

    # Evoluzione nel tempo
    evoluzione = find_section(root, "Evoluzione nel tempo", level=2)
    if evoluzione and section_full_text(evoluzione).strip():
        chunks.append(emit_chunk(
            fm=fm, doc_type=doc_type, parent_id=parent_id,
            unit_slug="evoluzione",
            heading_path=["Evoluzione nel tempo"],
            body=section_full_text(evoluzione),
            title=title,
        ))

    # For profiles that have neither "Posizioni documentate" nor "Sintesi"
    # (e.g. forchielli 00-anagrafica-e-carriera), fall back to emitting every H2.
    if not chunks:
        for h2 in root.children:
            if h2.level != 2:
                continue
            if h2.heading in SKIP_HEADINGS:
                continue
            body_text = section_full_text(h2).strip()
            if not body_text:
                continue
            chunks.append(emit_chunk(
                fm=fm, doc_type=doc_type, parent_id=parent_id,
                unit_slug=slugify(h2.heading),
                heading_path=[h2.heading],
                body=body_text,
                title=title,
            ))

    return chunks


def handle_comunicato(fm: dict, body: str) -> list[Chunk]:
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    text = strip_images(body).strip()
    tok = count_tokens(text)
    if tok <= COMUNICATO_SPLIT_THRESHOLD:
        return [emit_chunk(
            fm=fm, doc_type="comunicato", parent_id=parent_id,
            unit_slug="",
            heading_path=[],
            body=text,
            title=title,
        )]
    # Split into paragraph clusters at the lower target
    paras = paragraph_split(text)
    clusters = cluster_paragraphs(paras, target_tokens=COMUNICATO_SPLIT_TARGET)
    return [
        emit_chunk(
            fm=fm, doc_type="comunicato", parent_id=parent_id,
            unit_slug=f"part-{i+1:02d}",
            heading_path=[f"parte {i+1}"],
            body=c,
            title=title,
        )
        for i, c in enumerate(clusters)
    ]


def handle_newsletter_section(fm: dict, body: str) -> list[Chunk]:
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    section_title = str(fm.get("section_title", "") or "")
    text = strip_images(body).strip()
    return [emit_chunk(
        fm=fm, doc_type="newsletter_section", parent_id=parent_id,
        unit_slug="",
        heading_path=[section_title] if section_title else [],
        body=text,
        title=title,
        extras={
            "parent_newsletter": fm.get("parent_newsletter"),
            "tesi_alignment": fm.get("tesi_alignment"),
        },
    )]


def handle_identity(fm: dict, body: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    root = effective_root(parse_into_sections(body))
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    for h2 in root.children:
        if h2.level != 2:
            continue
        if h2.heading in SKIP_HEADINGS:
            continue
        body_text = section_full_text(h2).strip()
        if not body_text:
            continue
        chunks.append(emit_chunk(
            fm=fm, doc_type="identity", parent_id=parent_id,
            unit_slug=slugify(h2.heading),
            heading_path=[h2.heading],
            body=body_text,
            title=title,
        ))
    if not chunks:
        # No H2s — emit the whole body as one chunk
        chunks.append(emit_chunk(
            fm=fm, doc_type="identity", parent_id=parent_id,
            unit_slug="",
            heading_path=[],
            body=strip_images(body).strip(),
            title=title,
        ))
    return chunks


def handle_statuto(fm: dict, body: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    root = parse_into_sections(body)
    for h2 in root.children:
        if h2.level != 2:
            continue
        if not h2.heading.startswith("Articolo"):
            continue
        body_text = section_full_text(h2).strip()
        if not body_text:
            continue
        chunks.append(emit_chunk(
            fm=fm, doc_type="statuto", parent_id=parent_id,
            unit_slug=slugify(h2.heading),
            heading_path=[h2.heading],
            body=body_text,
            title=title,
        ))
    return chunks


FONDAMENTO_SPLIT_RE = re.compile(r"\n\s*\n(\d+)\s*\n\s*\n")


def handle_fondamenti(fm: dict, body: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    root = parse_into_sections(body)
    target = find_section(root, "Fondamenti", level=2)
    text = target.body_text() if target else body.strip()
    items = FONDAMENTO_SPLIT_RE.split("\n\n" + text)
    numbers = items[1::2]
    bodies = items[2::2]
    for n, b in zip(numbers, bodies):
        body_clean = b.strip()
        if not body_clean:
            continue
        chunks.append(emit_chunk(
            fm=fm, doc_type="fondamenti", parent_id=parent_id,
            unit_slug=f"fondamento-{int(n):02d}",
            heading_path=[f"Fondamento {n}"],
            body=body_clean,
            title=title,
        ))
    return chunks


def handle_contact(fm: dict, body: str) -> list[Chunk]:
    """Decision 24 retrievable card. Splits by H2 (Organi nazionali / Referenti
    territoriali / Come reperire un contatto specifico). Each H2 is self-
    contained and answers a distinct query category."""
    chunks: list[Chunk] = []
    root = effective_root(parse_into_sections(body))
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    for h2 in root.children:
        if h2.level != 2:
            continue
        if h2.heading in SKIP_HEADINGS:
            continue
        body_text = section_full_text(h2).strip()
        if not body_text:
            continue
        chunks.append(emit_chunk(
            fm=fm, doc_type="contact", parent_id=parent_id,
            unit_slug=slugify(h2.heading),
            heading_path=[h2.heading],
            body=body_text,
            title=title,
        ))
    if not chunks:
        # Card without H2s — emit whole body as one chunk.
        chunks.append(emit_chunk(
            fm=fm, doc_type="contact", parent_id=parent_id,
            unit_slug="",
            heading_path=[],
            body=strip_images(body).strip(),
            title=title,
        ))
    return chunks


def handle_codice_etico(fm: dict, body: str) -> list[Chunk]:
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    text = strip_images(body).strip()
    return [emit_chunk(
        fm=fm, doc_type="codice_etico", parent_id=parent_id,
        unit_slug="",
        heading_path=[],
        body=text,
        title=title,
    )]


EMPTY_SECTION_MARKER = "_(nessun contenuto)_"


def _handle_event_distillation(fm: dict, body: str, doc_type: str) -> list[Chunk]:
    """Per-H2 chunking for party_event_distillation / leader_event_distillation.

    Skips sections whose body contains only `_(nessun contenuto)_`.
    Carries playlist/speakers/tesi_touched/duration through to chunk extras.
    """
    chunks: list[Chunk] = []
    root = effective_root(parse_into_sections(body))
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    extras_base = {
        "playlist": fm.get("playlist"),
        "speakers": fm.get("speakers"),
        "tesi_touched": fm.get("tesi_touched"),
        "duration": fm.get("duration"),
    }
    for h2 in root.children:
        if h2.level != 2:
            continue
        if h2.heading in SKIP_HEADINGS:
            continue
        body_text = section_full_text(h2).strip()
        if not body_text:
            continue
        # Skip sections that only contain the "empty" marker
        body_no_marker = body_text.replace(EMPTY_SECTION_MARKER, "").strip()
        if not body_no_marker:
            continue
        chunks.append(emit_chunk(
            fm=fm, doc_type=doc_type, parent_id=parent_id,
            unit_slug=slugify(h2.heading),
            heading_path=[h2.heading],
            body=body_text,
            title=title,
            extras=extras_base,
        ))
    return chunks


def handle_party_event_distillation(fm: dict, body: str) -> list[Chunk]:
    return _handle_event_distillation(fm, body, "party_event_distillation")


def handle_leader_event_distillation(fm: dict, body: str) -> list[Chunk]:
    return _handle_event_distillation(fm, body, "leader_event_distillation")


def handle_data(fm: dict, body: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    root = effective_root(parse_into_sections(body))
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    for h2 in root.children:
        if h2.level != 2:
            continue
        if h2.heading in SKIP_HEADINGS:
            continue
        body_text = section_full_text(h2).strip()
        if not body_text:
            continue
        chunks.append(emit_chunk(
            fm=fm, doc_type="data", parent_id=parent_id,
            unit_slug=slugify(h2.heading),
            heading_path=[h2.heading],
            body=body_text,
            title=title,
            extras={
                "quality_tier": fm.get("quality_tier"),
                "data_metric": fm.get("data_metric"),
                "data_period": fm.get("data_period"),
                "tags": fm.get("tags"),
            },
        ))
    if not chunks:
        chunks.append(emit_chunk(
            fm=fm, doc_type="data", parent_id=parent_id,
            unit_slug="",
            heading_path=[],
            body=strip_images(body).strip(),
            title=title,
            extras={
                "quality_tier": fm.get("quality_tier"),
                "data_metric": fm.get("data_metric"),
                "data_period": fm.get("data_period"),
                "tags": fm.get("tags"),
            },
        ))
    return chunks


def handle_leader_article(fm: dict, body: str) -> list[Chunk]:
    parent_id = str(fm.get("id"))
    title = str(fm.get("title", ""))
    # Drop the leading H1 (title) if present — it's already in the prepended header
    body = re.sub(r"^\s*#\s+.*?\n", "", body, count=1)
    text = strip_images(body).strip()
    paras = paragraph_split(text)
    clusters = cluster_paragraphs(paras, target_tokens=SOFT_CAP_TOKENS)
    if len(clusters) == 1:
        return [emit_chunk(
            fm=fm, doc_type="leader_article", parent_id=parent_id,
            unit_slug="",
            heading_path=[],
            body=clusters[0],
            title=title,
            extras={
                "topics": fm.get("topics"),
                "stance_count": fm.get("stance_count"),
                "relevance": fm.get("relevance"),
            },
        )]
    return [
        emit_chunk(
            fm=fm, doc_type="leader_article", parent_id=parent_id,
            unit_slug=f"part-{i+1:02d}",
            heading_path=[f"parte {i+1}"],
            body=c,
            title=title,
            extras={
                "topics": fm.get("topics"),
                "stance_count": fm.get("stance_count"),
                "relevance": fm.get("relevance"),
            },
        )
        for i, c in enumerate(clusters)
    ]


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

HANDLERS = {
    "tesi": handle_tesi,
    "comunicato": handle_comunicato,
    "newsletter_section": handle_newsletter_section,
    "identity": handle_identity,
    "contact": handle_contact,
    "statuto": handle_statuto,
    "fondamenti": handle_fondamenti,
    "codice_etico": handle_codice_etico,
    "party_event_distillation": handle_party_event_distillation,
    "leader_event_distillation": handle_leader_event_distillation,
    "data": handle_data,
    "leader_topic_profile": lambda fm, body: handle_profile(fm, body, "leader_topic_profile"),
    "party_topic_profile": lambda fm, body: handle_profile(fm, body, "party_topic_profile"),
    "leader_article": handle_leader_article,
}


def process_file(path: Path) -> list[Chunk]:
    parsed = parse_doc(path)
    if parsed is None:
        return []
    fm, body = parsed
    if not is_retrievable(fm, path, CORPUS):
        return []
    doc_type = fm.get("type")
    handler = HANDLERS.get(doc_type)
    if handler is None:
        return []
    return handler(fm, body)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write chunks.jsonl")
    args = ap.parse_args()

    if not CORPUS.exists():
        sys.exit(f"corpus path not found: {CORPUS}")

    all_chunks: list[Chunk] = []
    skipped_no_handler: dict[str, int] = {}
    skipped_excluded = 0
    skipped_bad_frontmatter = 0
    files_processed = 0

    for path in sorted(CORPUS.rglob("*.md")):
        if under_underscore(path, CORPUS):
            continue
        parsed = parse_doc(path)
        if parsed is None:
            skipped_bad_frontmatter += 1
            continue
        fm, _body = parsed
        if not is_retrievable(fm, path, CORPUS):
            skipped_excluded += 1
            continue
        doc_type = fm.get("type")
        if doc_type not in HANDLERS:
            skipped_no_handler[str(doc_type)] = skipped_no_handler.get(str(doc_type), 0) + 1
            continue
        try:
            chunks = process_file(path)
        except Exception as e:
            print(f"ERROR processing {path}: {e}", file=sys.stderr)
            continue
        all_chunks.extend(chunks)
        files_processed += 1

    # Stats by doc_type
    by_type: dict[str, dict[str, Any]] = {}
    for c in all_chunks:
        d = by_type.setdefault(c.doc_type, {"count": 0, "tokens": 0, "min": 1e9, "max": 0})
        d["count"] += 1
        d["tokens"] += c.tokens
        d["min"] = min(d["min"], c.tokens)
        d["max"] = max(d["max"], c.tokens)

    print(f"\n{'APPLIED' if args.apply else 'DRY-RUN'} — root={CORPUS}\n")
    print(f"Files processed:        {files_processed}")
    print(f"Files excluded:         {skipped_excluded}")
    print(f"Files w/ bad fm:        {skipped_bad_frontmatter}")
    print(f"Files w/ no handler:    {sum(skipped_no_handler.values())}")
    for t, n in sorted(skipped_no_handler.items()):
        print(f"    {n:4d}  type={t}")
    print(f"\nTotal chunks emitted:   {len(all_chunks)}")
    print(f"{'doc_type':30}  {'count':>6}  {'tok/min':>8}  {'tok/avg':>8}  {'tok/max':>8}")
    for t, d in sorted(by_type.items()):
        avg = d["tokens"] // max(d["count"], 1)
        print(f"{t:30}  {d['count']:>6}  {d['min']:>8}  {avg:>8}  {d['max']:>8}")

    if args.apply:
        with OUT_PATH.open("w", encoding="utf-8", newline="\n") as f:
            for c in all_chunks:
                f.write(json.dumps(asdict(c), ensure_ascii=False, default=_json_default) + "\n")
        print(f"\nWritten: {OUT_PATH}")
    else:
        # Show a sample chunk per doc_type for inspection
        print("\n--- SAMPLE PER doc_type ---")
        seen: set[str] = set()
        for c in all_chunks:
            if c.doc_type in seen:
                continue
            seen.add(c.doc_type)
            preview = c.text[:200].replace("\n", " | ")
            print(f"\n[{c.doc_type}] {c.chunk_id}")
            print(f"  tier={c.tier}  attribution={c.attribution}  tokens={c.tokens}")
            print(f"  anchor: {c.anchor}")
            print(f"  text[:200]: {preview}")


if __name__ == "__main__":
    main()
