#!/usr/bin/env python3
"""Exercise OpenCode project bootstrap, adoption, handoff, and continuation behavior."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ROOT / "scripts" / "bootstrap_project.py"
VALIDATE = ROOT / "scripts" / "validate_project_handoff.py"


def run(*args: str, expected: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != expected:
        raise AssertionError(
            f"Expected exit {expected}, got {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}"
        )
    return result


def replace_state(project: Path, *, agent: str, status: str, objective: str, next_step: str) -> None:
    state = project / "docs" / "CURRENT_STATE.md"
    state.write_text(
        "\n".join(
            (
                "# Current State",
                "",
                f"**Status:** {status}",
                f"**Current objective:** {objective}",
                f"**Active backlog item:** {'TODO-001' if status.lower() in {'active', 'ready', 'paused'} else 'None'}",
                "**Active branch:** main",
                "**Last relevant commit:** none",
                "**Last updated:** 2026-01-01",
                f"**Updated by:** {agent}",
                "",
                "## Completed",
                "",
                "- Bootstrap and context review.",
                "",
                "## In progress",
                "",
                f"- {objective}",
                "",
                "## Pending",
                "",
                "- Acceptance verification.",
                "",
                "## Decisions this session",
                "",
                "- Continue through the repository handoff; no product decision was made.",
                "",
                "## Important files",
                "",
                "- `docs/PROJECT_CONTEXT.md`",
                "",
                "## Verification performed",
                "",
                "- Handoff validation passed.",
                "",
                "## Known errors",
                "",
                "- None known.",
                "",
                "## Risks or blockers",
                "",
                "- None.",
                "",
                "## Next exact step",
                "",
                f"TODO-001 — {next_step}" if status.lower() in {"active", "ready", "paused"} else next_step,
                "",
            )
        ),
        encoding="utf-8",
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="ai-playbooks-handoff-") as temporary:
        root = Path(temporary)

        new_project = root / "new-project"
        run(sys.executable, str(BOOTSTRAP), str(new_project))
        run(sys.executable, str(VALIDATE), str(new_project))
        moving = (new_project / "moving.md").read_text(encoding="utf-8")
        handoff = (new_project / "HANDOFF.md").read_text(encoding="utf-8")
        todo_path = new_project / "TODO.md"
        todo = todo_path.read_text(encoding="utf-8")
        if "shortest safe entry point for OpenCode" not in moving or "OpenCode and its selected models" not in handoff:
            raise AssertionError("OpenCode handoff instructions were not installed")
        if "AGENTS.md" in moving or "CLAUDE.md" in moving:
            raise AssertionError("Universal entry depends on a vendor-specific adapter")
        if "TODO-001" not in todo or "Initial development plan" not in todo:
            raise AssertionError("Project plan and backlog were not installed")

        replace_state(
            new_project,
            agent="OpenCode",
            status="Active",
            objective="Implement a synthetic health endpoint.",
            next_step="OpenCode: implement the endpoint described in docs/work-items/health-endpoint.md.",
        )
        work_item = new_project / "docs" / "work-items" / "health-endpoint.md"
        work_item.write_text("# Health endpoint\n\nReturn an observable synthetic status response.\n", encoding="utf-8")
        run(sys.executable, str(VALIDATE), str(new_project))

        # A vendor-neutral third agent can resume using only the universal entry,
        # current state, and repository evidence—without conversation history.
        recovered_state = (new_project / "docs" / "CURRENT_STATE.md").read_text(encoding="utf-8")
        if "implement the endpoint" not in recovered_state or "ai-playbooks-moving:v3" not in moving:
            raise AssertionError("A generic agent could not recover the documented next step")
        for liveness_rule in (
            "exactly two valid terminal states",
            "Ya terminé",
            "one concise question",
            "Never wait silently",
        ):
            if liveness_rule not in handoff:
                raise AssertionError(f"Universal handoff is missing active-interaction rule: {liveness_rule}")

        todo_path.write_text(
            todo.replace(
                "## Later\n\n- None recorded.",
                "## Later\n\n- [ ] **TODO-002 — Add a synthetic readiness endpoint**\n"
                "  - Priority: Later\n"
                "  - Outcome: A separately verifiable readiness signal.\n"
                "  - Dependencies: TODO-001 completion.\n"
                "  - Work item: Not selected.",
            ),
            encoding="utf-8",
        )
        run(sys.executable, str(VALIDATE), str(new_project))

        replace_state(
            new_project,
            agent="OpenCode",
            status="Complete",
            objective="Implement a synthetic health endpoint.",
            next_step="No active work. Select the next approved work item.",
        )
        run(sys.executable, str(VALIDATE), str(new_project))

        legacy = root / "legacy-project"
        legacy.mkdir()
        (legacy / "README.md").write_text("# Existing project\n", encoding="utf-8")
        run(sys.executable, str(BOOTSTRAP), str(legacy), expected=2)
        if sorted(path.name for path in legacy.iterdir()) != ["README.md"]:
            raise AssertionError("Legacy project changed before adoption approval")
        run(sys.executable, str(BOOTSTRAP), str(legacy), "--adopt")
        run(sys.executable, str(VALIDATE), str(legacy))
        if (legacy / "README.md").read_text(encoding="utf-8") != "# Existing project\n":
            raise AssertionError("Legacy content was overwritten during adoption")

        conflict = root / "conflict-project"
        conflict.mkdir()
        original = "# Existing agent rules\n"
        (conflict / "AGENTS.md").write_text(original, encoding="utf-8")
        run(sys.executable, str(BOOTSTRAP), str(conflict), "--adopt", expected=3)
        if (conflict / "AGENTS.md").read_text(encoding="utf-8") != original:
            raise AssertionError("Existing AGENTS.md was overwritten")
        if not (conflict / ".ai-playbooks-proposals" / "AGENTS.md").is_file():
            raise AssertionError("A merge proposal was not created for conflicting instructions")
        run(sys.executable, str(BOOTSTRAP), str(conflict), expected=2)

    print("End-to-end OpenCode project bootstrap and continuation tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
