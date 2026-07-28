#!/usr/bin/env python3
"""Install the AI-Playbooks project memory and cross-agent handoff structure."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates" / "project"
MANIFEST = ".ai-playbooks.json"
MUTABLE_PATHS = {
    "docs/PROJECT_CONTEXT.md",
    "docs/CURRENT_STATE.md",
}


@dataclass
class Result:
    created: list[str]
    preserved: list[str]
    proposals: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install shared Codex/Claude project instructions without overwriting existing files."
    )
    parser.add_argument("target", type=Path, help="Project directory to initialize or adopt")
    parser.add_argument(
        "--adopt",
        action="store_true",
        help="Confirm adoption when the target already contains a project",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report planned actions without writing files",
    )
    return parser.parse_args()


def project_entries(target: Path) -> list[Path]:
    if not target.exists():
        return []
    return [entry for entry in target.iterdir() if entry.name not in {".git", ".DS_Store"}]


def is_managed(target: Path) -> bool:
    workflow = target / "docs" / "AI_WORKFLOW.md"
    agents = target / "AGENTS.md"
    claude = target / "CLAUDE.md"
    return (
        (target / MANIFEST).is_file()
        and workflow.is_file()
        and agents.is_file()
        and claude.is_file()
        and "ai-playbooks-workflow:v" in workflow.read_text(encoding="utf-8")
        and "ai-playbooks-adapter:v1" in agents.read_text(encoding="utf-8")
        and "ai-playbooks-adapter:v1" in claude.read_text(encoding="utf-8")
    )


def git_value(target: Path, args: list[str], fallback: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=target,
        capture_output=True,
        text=True,
        check=False,
    )
    value = result.stdout.strip()
    return value if result.returncode == 0 and value else fallback


def render(source: Path, project_name: str, target: Path) -> str:
    text = source.read_text(encoding="utf-8")
    replacements = {
        "{{PROJECT_NAME}}": project_name,
        "{{DATE}}": date.today().isoformat(),
        "<detect from Git>": git_value(target, ["branch", "--show-current"], "not yet created"),
        "<detect from Git or state none>": git_value(target, ["log", "-1", "--format=%h %s"], "none"),
    }
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    return text


def install(target: Path, dry_run: bool) -> Result:
    target.mkdir(parents=True, exist_ok=True)
    project_name = target.resolve().name
    result = Result(created=[], preserved=[], proposals=[])
    proposal_root = target / ".ai-playbooks-proposals"

    for source in sorted(path for path in TEMPLATE_ROOT.rglob("*") if path.is_file()):
        relative = source.relative_to(TEMPLATE_ROOT)
        relative_text = relative.as_posix()
        destination = target / relative
        expected = render(source, project_name, target)

        if not destination.exists():
            result.created.append(relative_text)
            if not dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(expected, encoding="utf-8")
            continue

        existing = destination.read_text(encoding="utf-8")
        if relative_text in MUTABLE_PATHS or existing == expected:
            result.preserved.append(relative_text)
            continue

        proposal = proposal_root / relative
        result.proposals.append(proposal.relative_to(target).as_posix())
        if not dry_run:
            proposal.parent.mkdir(parents=True, exist_ok=True)
            proposal.write_text(expected, encoding="utf-8")

    return result


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    existing_project = bool(project_entries(target))
    managed = is_managed(target)

    if existing_project and not managed and not args.adopt:
        print("Existing project detected; no files were changed.")
        print("Ask the user whether to adopt the architect structure while preserving current behavior.")
        print(f"After approval run: python3 {Path(__file__).resolve()} \"{target}\" --adopt")
        return 2

    result = install(target, args.dry_run)
    mode = "managed" if managed else "adopted" if existing_project else "new"
    print(json.dumps({"mode": mode, **result.__dict__, "dry_run": args.dry_run}, indent=2))

    if result.proposals:
        print("Existing instruction files were preserved. Review and merge the generated proposals before validation.")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
