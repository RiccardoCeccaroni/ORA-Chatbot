"""Audit frontmatter across the corpus.

Read-only. Reports the current state of every .md file's YAML frontmatter
against the target schema documented in CLAUDE.md section 5, so we can see
exactly what (if anything) the one-shot migration needs to do.

Usage:
    python audit_frontmatter.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)


CORPUS_ROOT = Path(__file__).resolve().parent.parent / "corpus"


# Expected (type, attribution_default_or_rule) per folder pattern.
# attribution_rule is a callable taking the relative path parts and
# returning the expected attribution; None means "use whatever is in
# the file".
FOLDER_RULES: list[tuple[str, str, Any]] = [
    ("ora-party/manifesto", "tesi", "party"),
    ("ora-party/comunicati", "comunicato", "party"),
    ("ora-party/newsletter/sections", "newsletter_section", "party"),
    ("ora-party/newsletter", "newsletter", "party"),  # top-level newsletter sources
    ("ora-party/identity", "<identity-slice>", "party"),
    ("ora-party/contacts", "contact", "party"),  # decision 24
    ("ora-party/youtube", "party_event_distillation", "party"),  # decision 25
    ("leaders/boldrin/profile", "leader_topic_profile", "boldrin"),
    ("leaders/boldrin/articles", "leader_article", "boldrin"),
    ("leaders/boldrin/dialogues", "leader_transcript", "boldrin"),
    ("leaders/boldrin/youtube", "leader_event_distillation", "boldrin"),  # decision 25
    ("leaders/forchielli/profile", "leader_topic_profile", "forchielli"),
    ("leaders/forchielli/dialogues", "leader_transcript", "forchielli"),
    ("leaders/forchielli/youtube", "leader_event_distillation", "forchielli"),  # decision 25
    ("other-parties/coalitions", "party_programme", "coalition"),
    # Per-party folders: profile/ subfolder is topic profiles; top-level files
    # are raw party programmes / wikipedia (latter uses type=identity).
    ("other-parties", "<per-party>", None),
    ("data", "data", None),  # attribution from file (istat, eurostat, etc.)
]

# Files placed in a member-party folder but attributed to a coalition.
# (Convenience storage — the bot retrieves them via the member-party tier.)
COALITION_FILES_IN_MEMBER_FOLDERS = {
    "other-parties/azione/azione-2022-programma.md",  # Terzo Polo joint
    "other-parties/iv/iv-2022-programma.md",          # Terzo Polo joint
    "other-parties/iv/iv-2024-europee.md",            # Stati Uniti d'Europa joint
}

# Required fields per type. Synthesized types (leader_topic_profile,
# party_topic_profile) use date_compiled instead of date_published / date_scraped.
REQUIRED_FIELDS_BY_TYPE: dict[str, set[str]] = {
    "tesi": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "comunicato": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "newsletter": {"id", "type", "attribution", "title", "date_published", "date_scraped", "content_hash"},
    "newsletter_section": {"id", "type", "attribution", "title", "date_published", "date_scraped", "content_hash"},
    "identity": {"id", "type", "attribution", "title", "source_url", "date_scraped", "content_hash"},
    "leader_article": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "leader_transcript": {"id", "type", "attribution", "title", "content_hash"},
    "leader_topic_profile": {"id", "type", "attribution", "content_hash"},  # date_compiled checked separately
    "party_topic_profile": {"id", "type", "attribution", "content_hash"},   # date_compiled checked separately
    "party_programme": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "statuto": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "fondamenti": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "codice_etico": {"id", "type", "attribution", "title", "source_url", "date_published", "date_scraped", "content_hash"},
    "data": {"id", "type", "attribution", "title", "data_metric", "data_period", "quality_tier", "source_url", "content_hash"},
    "contact": {"id", "type", "attribution", "title", "source_url", "date_scraped", "date_compiled", "content_hash"},
    "party_event_distillation": {"id", "type", "attribution", "title", "source_url", "date_compiled", "content_hash", "speakers", "tesi_touched"},
    "leader_event_distillation": {"id", "type", "attribution", "title", "source_url", "date_compiled", "content_hash"},
}

# Types accepted at ora-party/identity/ (curated card + foundational slice).
IDENTITY_SLICE_TYPES = {"identity", "statuto", "fondamenti", "codice_etico"}

# Synthesized types must have date_compiled (not date_published / date_scraped).
# YouTube distillations also use date_compiled (when the distiller ran) but optionally
# carry date_published (the video upload date) as well.
SYNTHESIZED_TYPES = {"leader_topic_profile", "party_topic_profile", "party_event_distillation", "leader_event_distillation"}


def find_folder_rule(rel_path: Path, actual_type: str | None) -> tuple[str, str] | None:
    """Return (expected_type, expected_attribution) for the file path,
    or None if not in a known folder.

    For per-party folders (other-parties/<party>/...), the expected type
    depends on subfolder:
      - other-parties/<party>/profile/*.md → party_topic_profile
      - other-parties/<party>/*.md (top-level) → party_programme OR identity
        (the file itself declares which; both are valid)
    """
    posix = rel_path.as_posix()
    for folder_prefix, expected_type, attribution_rule in FOLDER_RULES:
        if posix.startswith(folder_prefix + "/"):
            # Identity-slice: accept curated identity card + foundational docs
            # (statuto, fondamenti, codice_etico). Attribution must be "party".
            if expected_type == "<identity-slice>":
                if actual_type in IDENTITY_SLICE_TYPES:
                    return (actual_type, "party")
                return ("identity", "party")  # fall back, will raise type_mismatch

            # Per-party special case: dispatch by subfolder + accept either
            # party_programme or identity at the top level.
            if expected_type == "<per-party>":
                parts = rel_path.parts  # ("other-parties", "<party>", ...)
                if len(parts) < 3:
                    return None
                party = parts[1]
                if parts[2] == "profile":
                    return ("party_topic_profile", party)
                # Top-level: programme or wikipedia/identity
                # Accept either; pick whichever matches actual type for attribution check.
                if actual_type in ("party_programme", "identity"):
                    expected_attr = (
                        "coalition" if posix in COALITION_FILES_IN_MEMBER_FOLDERS
                        else party
                    )
                    return (actual_type, expected_attr)
                # Unknown top-level type — fall through to programme as default
                return ("party_programme", party)

            if attribution_rule is None:
                return (expected_type, "<from-file>")
            return (expected_type, attribution_rule)
    return None


def parse_frontmatter(content: str) -> tuple[dict[str, Any] | None, str]:
    """Extract YAML frontmatter from a markdown file. Returns (frontmatter_dict, body).
    If no frontmatter present, returns (None, content)."""
    if not content.startswith("---"):
        return None, content
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", content, re.DOTALL)
    if not m:
        return None, content
    fm_text, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict):
            return None, content
        return fm, body
    except yaml.YAMLError:
        return None, content


def is_under_excluded_folder(rel_path: Path) -> bool:
    """True if any folder in the path begins with '_'."""
    return any(part.startswith("_") for part in rel_path.parts)


def main() -> None:
    if not CORPUS_ROOT.is_dir():
        print(f"ERROR: corpus root not found at {CORPUS_ROOT}", file=sys.stderr)
        sys.exit(1)

    findings: dict[str, list[dict[str, Any]]] = defaultdict(list)
    type_counter: Counter[str] = Counter()
    retrievability_counter: Counter[str] = Counter()

    total_files = 0
    for md_path in sorted(CORPUS_ROOT.rglob("*.md")):
        rel = md_path.relative_to(CORPUS_ROOT)
        total_files += 1

        # Skip scaffolding folders
        if is_under_excluded_folder(rel):
            retrievability_counter["under-underscore-folder (skipped)"] += 1
            continue

        content = md_path.read_text(encoding="utf-8", errors="replace")
        fm, _body = parse_frontmatter(content)

        # No frontmatter at all
        if fm is None:
            findings["no_frontmatter"].append({"path": str(rel)})
            retrievability_counter["NO frontmatter"] += 1
            continue

        # Determine retrievability
        cs = fm.get("corpus_status")
        if cs == "exclude":
            retrievability_counter["explicit corpus_status=exclude"] += 1
        elif cs == "include":
            retrievability_counter["explicit corpus_status=include"] += 1
        else:
            retrievability_counter["implicit (no corpus_status, not under _)"] += 1

        fm_type = fm.get("type")
        type_counter[fm_type or "<missing>"] += 1

        # Compare folder rule vs frontmatter
        rule = find_folder_rule(rel, fm_type)
        if rule is not None:
            expected_type, expected_attr = rule
            if fm_type != expected_type:
                findings["type_mismatch"].append({
                    "path": str(rel),
                    "expected_type": expected_type,
                    "actual_type": fm_type,
                })
            if expected_attr != "<from-file>":
                actual_attr = fm.get("attribution")
                if actual_attr != expected_attr:
                    findings["attribution_mismatch"].append({
                        "path": str(rel),
                        "expected_attribution": expected_attr,
                        "actual_attribution": actual_attr,
                    })

        # Check required fields
        if fm_type in REQUIRED_FIELDS_BY_TYPE:
            required = REQUIRED_FIELDS_BY_TYPE[fm_type]
            missing = required - set(fm.keys())
            if missing:
                findings["missing_fields"].append({
                    "path": str(rel),
                    "type": fm_type,
                    "missing": sorted(missing),
                })

        # Synthesized types need date_compiled
        if fm_type in SYNTHESIZED_TYPES:
            if "date_compiled" not in fm:
                findings["synthesized_missing_date_compiled"].append({
                    "path": str(rel),
                    "type": fm_type,
                })

        # content_hash format check (CLAUDE.md drift #5 standard: bare hex)
        ch = fm.get("content_hash")
        if ch is not None:
            if isinstance(ch, str):
                if ch.startswith("sha256:"):
                    findings["content_hash_prefixed"].append({
                        "path": str(rel),
                        "current": ch[:30] + "...",
                    })
                elif not re.fullmatch(r"[0-9a-f]{64}", ch):
                    findings["content_hash_malformed"].append({
                        "path": str(rel),
                        "current": str(ch)[:30] + "...",
                    })

        # Legacy field-name issues
        if fm_type == "comunicato" and "category" in fm and "tags" not in fm:
            findings["comunicato_uses_category_not_tags"].append({
                "path": str(rel),
                "category": fm["category"],
            })

        # (legacy "date_compiled vs date_published" check removed —
        # date_compiled is the correct field for synthesized types per schema)

    # ---------- Report ----------
    print("=" * 72)
    print(f"FRONTMATTER AUDIT — {total_files} markdown files total")
    print("=" * 72)

    print("\nRetrievability breakdown:")
    for k, v in retrievability_counter.most_common():
        print(f"  {v:5d}  {k}")

    print("\nType breakdown (for files with frontmatter, not under _ folders):")
    for k, v in type_counter.most_common():
        print(f"  {v:5d}  {k}")

    print("\n" + "=" * 72)
    print("FINDINGS (sorted by category)")
    print("=" * 72)

    if not findings:
        print("\n[Empty — corpus is fully aligned with target schema.]")
        return

    for category in [
        "no_frontmatter",
        "type_mismatch",
        "attribution_mismatch",
        "missing_fields",
        "synthesized_missing_date_compiled",
        "content_hash_prefixed",
        "content_hash_malformed",
        "comunicato_uses_category_not_tags",
    ]:
        items = findings.get(category, [])
        if not items:
            continue
        print(f"\n[{category}] — {len(items)} file(s)")
        for item in items[:20]:
            print(f"  {item}")
        if len(items) > 20:
            print(f"  ...and {len(items) - 20} more")


if __name__ == "__main__":
    main()
