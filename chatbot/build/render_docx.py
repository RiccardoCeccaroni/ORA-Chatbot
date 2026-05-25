"""Render a showcase_results.jsonl into a human-readable .docx for review.

Output format (per Riccardo, 2026-05-15):
  - Each line of questions is a section. Each turn is rendered as:
      Domanda N: <question>
      <answer body — inline [chunk_id] / [web:N] markers replaced with
                     superscript footnote numbers [1], [2], ...>
      Fonti per questo turno:
        [1] <label> — <tier/attribution> — <hyperlink to source_url>
        ...
  - Citations are numbered in first-occurrence order WITHIN each turn (turns are
    independent — turn 2's [1] is not the same as turn 1's [1]).

Usage:
  python build/render_docx.py evaluation/runs/<run_dir>
  → writes <run_dir>/qa_review.docx
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.shared import Pt, RGBColor
except ImportError:
    print("ERROR: python-docx not installed. Run: pip install python-docx", file=sys.stderr)
    sys.exit(1)


# Same citation token shape the orchestrator's enforce_citations uses.
CITATION_PATTERN = re.compile(r"\[([\w][\w\-:/\.#]*)\]", re.UNICODE)


def _add_hyperlink(paragraph, url: str, text: str) -> None:
    """Append a clickable hyperlink to a docx paragraph.

    python-docx doesn't expose hyperlinks in its public API; we splice the
    OOXML directly. Standard pattern from the python-docx FAQ.
    """
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    new_run = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    r_pr.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    r_pr.append(underline)
    new_run.append(r_pr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def _replace_inline_citations(text: str, citations: dict) -> tuple[str, list[tuple[str, dict]]]:
    """Replace [chunk_id]/[web:N] markers with superscript [N] numbers.

    Returns (rewritten_text, ordered_footnotes) where ordered_footnotes is
    a list of (citation_id, citation_meta) in first-occurrence order.
    Unknown markers (e.g. [inferenza], stripped chunks) are left as-is.
    """
    order: list[str] = []
    seen: dict[str, int] = {}

    def _sub(m: re.Match) -> str:
        cid = m.group(1)
        if cid.lower() == "inferenza":
            return m.group(0)  # keep the hedge label literal
        if cid not in citations:
            return m.group(0)  # unknown marker — leave it (visible signal of a stripped/unmapped citation)
        if cid not in seen:
            order.append(cid)
            seen[cid] = len(order)
        return f"[{seen[cid]}]"

    rewritten = CITATION_PATTERN.sub(_sub, text)
    footnotes = [(cid, citations[cid]) for cid in order]
    return rewritten, footnotes


def _render_entry(doc: Document, entry: dict) -> None:
    """Render one showcase entry — either single-turn or multi-turn."""
    heading_text = f"{entry.get('id', '?')} — {entry.get('category', '')}"
    h = doc.add_heading(heading_text, level=1)

    if entry.get("error"):
        p = doc.add_paragraph()
        run = p.add_run(f"[ERRORE: {entry['error']}]")
        run.italic = True
        run.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
        return

    if entry.get("showcases"):
        p = doc.add_paragraph()
        run = p.add_run(f"Showcase: {entry['showcases']}")
        run.italic = True
        run.font.size = Pt(9)

    turns = entry.get("turns")
    if turns:
        for i, t in enumerate(turns, 1):
            _render_turn(doc, t, turn_number=i)
    else:
        # single-turn entry — synthesize a fake turn list of length 1
        single = {
            "query": entry.get("query", ""),
            "answer": entry.get("answer", ""),
            "citations": entry.get("citations", {}),
            "is_refusal": entry.get("is_refusal", False),
            "refusal_reason": entry.get("refusal_reason"),
            "elapsed_s": entry.get("elapsed_s"),
        }
        _render_turn(doc, single, turn_number=None)


def _render_turn(doc: Document, turn: dict, turn_number: int | None) -> None:
    label = f"Domanda {turn_number}" if turn_number else "Domanda"
    q_p = doc.add_paragraph()
    q_run = q_p.add_run(f"{label}: {turn.get('query', '')}")
    q_run.bold = True

    citations = turn.get("citations") or {}
    answer = turn.get("answer", "") or ""
    rewritten, footnotes = _replace_inline_citations(answer, citations)

    body = doc.add_paragraph(rewritten)
    body.paragraph_format.space_after = Pt(6)

    # Per-turn metadata line (small + grey-ish)
    meta_bits = []
    if turn.get("is_refusal"):
        rr = turn.get("refusal_reason") or ""
        meta_bits.append(f"RIFIUTO ({rr})" if rr else "RIFIUTO")
    if turn.get("elapsed_s") is not None:
        meta_bits.append(f"{turn['elapsed_s']}s")
    if meta_bits:
        m = doc.add_paragraph()
        run = m.add_run(" · ".join(meta_bits))
        run.italic = True
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)

    if footnotes:
        f_label = doc.add_paragraph()
        run = f_label.add_run("Fonti per questo turno:")
        run.bold = True
        run.font.size = Pt(9)
        for idx, (cid, meta) in enumerate(footnotes, 1):
            line = doc.add_paragraph(style="List Number" if False else None)
            line.paragraph_format.left_indent = Pt(18)
            line.paragraph_format.space_after = Pt(2)
            tier = meta.get("tier", "")
            attr = meta.get("attribution", "")
            tier_attr = " — ".join(x for x in [tier, attr] if x and x != "web")
            prefix_run = line.add_run(f"[{idx}] {cid}")
            prefix_run.font.size = Pt(9)
            if tier_attr:
                ta_run = line.add_run(f"  ({tier_attr})")
                ta_run.font.size = Pt(9)
                ta_run.italic = True
            url = meta.get("source_url") or ""
            if url:
                line.add_run("  ").font.size = Pt(9)
                _add_hyperlink(line, url, url)
    doc.add_paragraph()  # spacer


def render(run_dir: Path) -> Path:
    in_path = run_dir / "showcase_results.jsonl"
    if not in_path.exists():
        raise FileNotFoundError(f"Not found: {in_path}")
    entries: list[dict] = []
    for line in in_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        entries.append(json.loads(line))

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    title = doc.add_heading("ORA Chatbot — Revisione domande e risposte", level=0)
    sub = doc.add_paragraph()
    s_run = sub.add_run(f"Generato da {in_path.name}")
    s_run.italic = True
    s_run.font.size = Pt(9)
    doc.add_paragraph()

    for e in entries:
        _render_entry(doc, e)

    out_path = run_dir / "qa_review.docx"
    doc.save(out_path)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=str, help="Path to an evaluation/runs/<...> directory.")
    args = parser.parse_args()
    out = render(Path(args.run_dir))
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
