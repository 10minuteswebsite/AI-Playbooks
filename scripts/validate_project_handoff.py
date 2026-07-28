#!/usr/bin/env python3
"""Validate that a project can be handed between Codex and Claude without chat history."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    "docs/AI_WORKFLOW.md",
    "docs/PROJECT_CONTEXT.md",
    "docs/CURRENT_STATE.md",
    "docs/architecture/README.md",
    "docs/decisions/README.md",
    "docs/work-items/README.md",
)
REQUIRED_DIRECTORIES = (
    "docs/architecture",
    "docs/decisions",
    "docs/work-items",
)
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an AI-Playbooks project handoff")
    parser.add_argument("target", type=Path, help="Project directory to validate")
    return parser.parse_args()


def section_value(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$\n+(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def validate(target: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (target / relative).is_file():
            errors.append(f"missing required file: {relative}")
    for relative in REQUIRED_DIRECTORIES:
        if not (target / relative).is_dir():
            errors.append(f"missing required directory: {relative}")
    if errors:
        return errors

    agents = (target / "AGENTS.md").read_text(encoding="utf-8")
    claude = (target / "CLAUDE.md").read_text(encoding="utf-8")
    workflow = (target / "docs" / "AI_WORKFLOW.md").read_text(encoding="utf-8")
    context = (target / "docs" / "PROJECT_CONTEXT.md").read_text(encoding="utf-8")
    current = (target / "docs" / "CURRENT_STATE.md").read_text(encoding="utf-8")

    for name, adapter in (("AGENTS.md", agents), ("CLAUDE.md", claude)):
        if "ai-playbooks-adapter:v1" not in adapter:
            errors.append(f"{name} is missing the managed adapter marker")
        for required_reference in (
            "docs/AI_WORKFLOW.md",
            "docs/PROJECT_CONTEXT.md",
            "docs/CURRENT_STATE.md",
            "git status",
        ):
            if required_reference not in adapter:
                errors.append(f"{name} does not reference {required_reference}")

    if "ai-playbooks-workflow:v" not in workflow:
        errors.append("docs/AI_WORKFLOW.md is missing the shared workflow marker")
    if "single source of truth" not in workflow:
        errors.append("shared workflow does not declare a single source of truth")
    if "Conversation history is temporary context" not in workflow:
        errors.append("shared workflow still depends on conversation history")

    status_match = re.search(r"^\*\*Status:\*\*\s*(.+)$", current, re.MULTILINE)
    status = status_match.group(1).strip().lower() if status_match else ""
    next_step = section_value(current, "Next exact step")
    if status in {"active", "ready", "paused"}:
        if not next_step or next_step.lower() in {"none", "n/a", "unknown", "tbd"} or "<" in next_step:
            errors.append("CURRENT_STATE.md must define a concrete next exact step while work is active")

    for relative, text in (
        ("AGENTS.md", agents),
        ("CLAUDE.md", claude),
        ("docs/AI_WORKFLOW.md", workflow),
        ("docs/PROJECT_CONTEXT.md", context),
        ("docs/CURRENT_STATE.md", current),
    ):
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{relative} contains a possible {name}")
        for email in EMAIL.findall(text):
            if not email.lower().endswith(("@example.com", "@example.invalid")):
                errors.append(f"{relative} contains a possible personal email address")

    if "docs/AI_WORKFLOW.md" not in agents or "docs/AI_WORKFLOW.md" not in claude:
        errors.append("Codex and Claude do not share the same workflow source")
    return errors


def main() -> int:
    target = parse_args().target.expanduser().resolve()
    errors = validate(target)
    if errors:
        print("Project handoff validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Project handoff validation passed: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
