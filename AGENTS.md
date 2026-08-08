# AI-Playbooks project instructions

AI-Playbooks is a versioned, documentation-first methodology for delivering software and AI-agent systems. Its main assets are the playbooks, standards, templates, examples, and small validation scripts listed in `README.md`.

GitHub (`10minuteswebsite/AI-Playbooks`) is the permanent source of truth. Start every session by reading `moving.md`, then load `HANDOFF.md`, `docs/CURRENT_STATE.md`, and only the relevant `TODO.md` sections and files needed for the next step. Do not read the whole repository or rely on conversation history.

For substantial work, follow the canonical rules in `ARCHITECT_BOOTSTRAP.md` and the referenced playbooks in this repository. Preserve existing Codex, Claude, and other agent adapters. Do not change application code or dependencies unless the request explicitly expands scope.

Useful checks:

- `python3 scripts/validate_docs.py`
- `python3 scripts/scan_secrets.py`
- `python3 scripts/test_project_handoff.py`
- `python3 scripts/test_github_first_architect.py`
- `python3 scripts/test_finite_project_discovery.py`
- `python3 scripts/validate_global_instructions.py`

Before ending substantive work, update `TODO.md` and `docs/CURRENT_STATE.md`, run relevant checks, and publish the verified change according to `docs/AI_WORKFLOW.md`.
