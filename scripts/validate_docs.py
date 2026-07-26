#!/usr/bin/env python3
"""Validate local Markdown links and basic repository documentation hygiene."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
STABLE_DOC = re.compile(r"\*\*Status:\*\* Stable")
VERSION = re.compile(r"\*\*Version:\*\* \d+\.\d+\.\d+")


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    path_text = unquote(target.split("#", 1)[0])
    if not path_text:
        return None
    return (source.parent / path_text).resolve()


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line != line.rstrip():
            errors.append(f"{relative}:{line_number}: trailing whitespace")

    if STABLE_DOC.search(text) and not VERSION.search(text):
        errors.append(f"{relative}: stable document is missing a semantic version")

    for match in MARKDOWN_LINK.finditer(text):
        target = local_target(path, match.group(1))
        if target is not None and not target.exists():
            errors.append(f"{relative}: broken local link: {match.group(1)}")

    return errors


def main() -> int:
    files = markdown_files()
    errors = [error for path in files for error in validate(path)]
    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Documentation validation passed for {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
