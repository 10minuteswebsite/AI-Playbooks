#!/usr/bin/env python3
"""Test GitHub-first architect activation and access diagnostics."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "check_github_access.py"
SPEC = importlib.util.spec_from_file_location("check_github_access", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> int:
    assert MODULE.repository_slug("https://github.com/10minuteswebsite/AI-Playbooks") == "10minuteswebsite/AI-Playbooks"
    assert MODULE.repository_slug("git@github.com:10minuteswebsite/AI-Playbooks.git") == "10minuteswebsite/AI-Playbooks"

    with patch.object(MODULE, "command_succeeds", side_effect=[False, False]):
        accessible, message = MODULE.verify("10minuteswebsite/AI-Playbooks")
    assert not accessible
    assert "does not prove the repository is private" in message
    assert "Do not paste credentials" in message

    bootstrap = (ROOT / "ARCHITECT_BOOTSTRAP.md").read_text(encoding="utf-8")
    profile = (ROOT / "templates" / "global" / "claude-profile-instructions.md").read_text(encoding="utf-8")
    workflow = (ROOT / "templates" / "project" / "docs" / "AI_WORKFLOW.md").read_text(encoding="utf-8")
    for text in (bootstrap, profile, workflow):
        assert "GitHub" in text
        assert "temporary" in text
    assert "login page is not evidence" in bootstrap
    assert "ai-playbooks-workflow:v4" in workflow

    print("GitHub-first architect tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
