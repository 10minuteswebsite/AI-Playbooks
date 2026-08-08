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
    "opencode.json",
    "TODO.md",
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
    todo = (target / "TODO.md").read_text(encoding="utf-8")
    opencode = (target / "opencode.json").read_text(encoding="utf-8")
    try:
        manifest = json.loads((target / ".ai-playbooks.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        manifest = {}
        errors.append(".ai-playbooks.json is not valid JSON")
    try:
        opencode_config = json.loads(opencode)
    except json.JSONDecodeError:
        opencode_config = {}
        errors.append("opencode.json is not valid JSON")

    if opencode_config.get("$schema") != "https://opencode.ai/config.json":
        errors.append("opencode.json must use the official OpenCode schema")
    instructions = opencode_config.get("instructions")
    bootstrap_url = "https://raw.githubusercontent.com/10minuteswebsite/AI-Playbooks/main/ARCHITECT_BOOTSTRAP.md"
    if not isinstance(instructions, list) or bootstrap_url not in instructions:
        errors.append("opencode.json must load the canonical remote ARCHITECT_BOOTSTRAP.md")

    expected_manifest = {
        "entrypoint": "moving.md",
        "handoff": "HANDOFF.md",
        "backlog": "TODO.md",
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

    if "ai-playbooks-moving:v3" not in moving:
        errors.append("moving.md is missing the universal entry marker")
    for required_reference in ("HANDOFF.md", "docs/CURRENT_STATE.md", "TODO.md", "git status"):
        if required_reference not in moving:
            errors.append(f"moving.md does not reference {required_reference}")
    if len(moving) > 2500:
        errors.append("moving.md is too long for a minimal progressive entry point")
    if "AGENTS.md" in moving or "CLAUDE.md" in moving:
        errors.append("moving.md depends on an agent-specific adapter")

    if "ai-playbooks-handoff:v3" not in handoff:
        errors.append("HANDOFF.md is missing the universal handoff marker")
    for required_rule in (
        "Codex, Claude, and any other agent",
        "Conversation history is optional context",
        "Read progressively",
        "Mandatory session close",
        "Active interaction contract",
        "exactly two valid terminal states",
        "Waiting is valid only after asking that blocking question",
        "TODO.md",
        "docs/CURRENT_STATE.md",
    ):
        if required_rule not in handoff:
            errors.append(f"HANDOFF.md is missing required continuity rule: {required_rule}")

    if "ai-playbooks-todo:v1" not in todo:
        errors.append("TODO.md is missing the managed backlog marker")
    for heading in (
        "Product objective",
        "Initial development plan",
        "Now",
        "Next",
        "Later",
        "Blocked",
        "Recently completed",
        "Maintenance rules",
    ):
        if not section_value(todo, heading):
            errors.append(f"TODO.md is missing or has an empty section: {heading}")
    definitions = re.findall(r"\*\*(TODO-\d{3,})\s+—", todo)
    if not definitions:
        errors.append("TODO.md must define at least one actionable TODO-NNN item")
    if len(definitions) != len(set(definitions)):
        errors.append("TODO.md contains duplicate task definitions")

    status_match = re.search(r"^\*\*Status:\*\*\s*(.+)$", current, re.MULTILINE)
    status = status_match.group(1).strip().lower() if status_match else ""
    next_step = section_value(current, "Next exact step")
    decisions = section_value(current, "Decisions this session")
    active_match = re.search(r"^\*\*Active backlog item:\*\*\s*(.+)$", current, re.MULTILINE)
    active_item = active_match.group(1).strip() if active_match else ""
    if status in {"active", "ready", "paused"}:
        if not next_step or next_step.lower() in {"none", "n/a", "unknown", "tbd"} or "<" in next_step:
            errors.append("CURRENT_STATE.md must define a concrete next exact step while work is active")
        if not re.fullmatch(r"TODO-\d{3,}", active_item):
            errors.append("CURRENT_STATE.md must identify one active TODO-NNN item while work is active")
        elif active_item not in definitions:
            errors.append("CURRENT_STATE.md references an active backlog item not defined in TODO.md")
        if active_item and active_item not in next_step:
            errors.append("CURRENT_STATE.md next exact step must reference the active backlog item")
    if not decisions:
        errors.append("CURRENT_STATE.md must record session decisions or explicitly state that none were made")

    for relative, text in (
        ("moving.md", moving),
        ("HANDOFF.md", handoff),
        ("TODO.md", todo),
        ("AGENTS.md", agents),
        ("CLAUDE.md", claude),
        ("docs/AI_WORKFLOW.md", workflow),
        ("docs/PROJECT_CONTEXT.md", context),
        ("docs/CURRENT_STATE.md", current),
        ("opencode.json", opencode),
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
