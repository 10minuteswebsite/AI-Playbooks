#!/usr/bin/env python3
"""Validate that a project can be handed between Codex and Claude without chat history."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    ".ai-playbooks.json",
    "moving.md",
    "HANDOFF.md",
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
    moving = (target / "moving.md").read_text(encoding="utf-8")
    handoff = (target / "HANDOFF.md").read_text(encoding="utf-8")
    workflow = (target / "docs" / "AI_WORKFLOW.md").read_text(encoding="utf-8")
    context = (target / "docs" / "PROJECT_CONTEXT.md").read_text(encoding="utf-8")
    current = (target / "docs" / "CURRENT_STATE.md").read_text(encoding="utf-8")
    try:
        manifest = json.loads((target / ".ai-playbooks.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        manifest = {}
        errors.append(".ai-playbooks.json is not valid JSON")

    expected_manifest = {
        "entrypoint": "moving.md",
        "handoff": "HANDOFF.md",
        "current_state": "docs/CURRENT_STATE.md",
        "compatible_agents": "any",
    }
    for key, expected in expected_manifest.items():
        if manifest.get(key) != expected:
            errors.append(f".ai-playbooks.json must define {key} as {expected}")

    for name, adapter in (("AGENTS.md", agents), ("CLAUDE.md", claude)):
        if "ai-playbooks-adapter:v" not in adapter:
            errors.append(f"{name} is missing the managed adapter marker")
        for required_reference in (
            "moving.md",
            "HANDOFF.md",
            "docs/CURRENT_STATE.md",
        ):
            if required_reference not in adapter:
                errors.append(f"{name} does not reference {required_reference}")

    if "ai-playbooks-workflow:v" not in workflow:
        errors.append("docs/AI_WORKFLOW.md is missing the shared workflow marker")
    if "detailed operational policy shared by all agents" not in workflow:
        errors.append("shared workflow is not declared agent-neutral")
    if "Conversation history is temporary context" not in workflow:
        errors.append("shared workflow still depends on conversation history")

    if "ai-playbooks-moving:v2" not in moving:
        errors.append("moving.md is missing the universal entry marker")
    for required_reference in ("HANDOFF.md", "docs/CURRENT_STATE.md", "git status"):
        if required_reference not in moving:
            errors.append(f"moving.md does not reference {required_reference}")
    if len(moving) > 2500:
        errors.append("moving.md is too long for a minimal progressive entry point")
    if "AGENTS.md" in moving or "CLAUDE.md" in moving:
        errors.append("moving.md depends on an agent-specific adapter")

    if "ai-playbooks-handoff:v2" not in handoff:
        errors.append("HANDOFF.md is missing the universal handoff marker")
    for required_rule in (
        "Codex, Claude, and any other agent",
        "Conversation history is optional context",
        "Read progressively",
        "Mandatory session close",
        "Active interaction contract",
        "exactly two valid terminal states",
        "Waiting is valid only after asking that blocking question",
        "docs/CURRENT_STATE.md",
    ):
        if required_rule not in handoff:
            errors.append(f"HANDOFF.md is missing required continuity rule: {required_rule}")

    status_match = re.search(r"^\*\*Status:\*\*\s*(.+)$", current, re.MULTILINE)
    status = status_match.group(1).strip().lower() if status_match else ""
    next_step = section_value(current, "Next exact step")
    decisions = section_value(current, "Decisions this session")
    if status in {"active", "ready", "paused"}:
        if not next_step or next_step.lower() in {"none", "n/a", "unknown", "tbd"} or "<" in next_step:
            errors.append("CURRENT_STATE.md must define a concrete next exact step while work is active")
    if not decisions:
        errors.append("CURRENT_STATE.md must record session decisions or explicitly state that none were made")

    for relative, text in (
        ("moving.md", moving),
        ("HANDOFF.md", handoff),
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

    if "moving.md" not in agents or "moving.md" not in claude:
        errors.append("Codex and Claude do not share the universal entry point")
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
