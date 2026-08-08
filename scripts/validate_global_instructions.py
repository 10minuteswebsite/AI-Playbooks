#!/usr/bin/env python3
"""Legacy check for optional Codex and Claude compatibility instructions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


MARKER = "<!-- ai-playbooks-global-bootstrap:v1 -->"
REQUIRED = (
    "playbooks/software-delivery-core.md",
    "playbooks/software-architect.md",
    "docs/AI_WORKFLOW.md",
    "docs/PROJECT_CONTEXT.md",
    "docs/CURRENT_STATE.md",
    "Usa el arquitecto",
    "ARCHITECT_BOOTSTRAP.md",
    "enlace de GitHub",
    "nunca solicites contraseñas, tokens ni secretos",
    "copia temporal",
    "no lo migres antes de recibir aprobación",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate legacy Codex/Claude bootstrap consistency")
    parser.add_argument("--codex", type=Path, default=Path.home() / ".codex" / "AGENTS.md")
    parser.add_argument("--claude", type=Path, default=Path.home() / ".claude" / "CLAUDE.md")
    return parser.parse_args()


def shared_block(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []
    if not path.is_file():
        return "", [f"missing global instruction file: {path}"]
    text = path.read_text(encoding="utf-8")
    if MARKER not in text:
        return "", [f"missing global bootstrap marker: {path}"]
    block = text.split(MARKER, 1)[1].strip()
    for required in REQUIRED:
        if required not in block:
            errors.append(f"{path} is missing required bootstrap instruction: {required}")
    return block, errors


def main() -> int:
    args = parse_args()
    codex, errors = shared_block(args.codex.expanduser())
    claude, claude_errors = shared_block(args.claude.expanduser())
    errors.extend(claude_errors)
    if codex and claude and codex != claude:
        errors.append("Codex and Claude global AI-Playbooks bootstrap blocks contradict or have drifted")
    if errors:
        print("Global instruction validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Legacy Codex/Claude instructions share the same AI-Playbooks bootstrap.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
