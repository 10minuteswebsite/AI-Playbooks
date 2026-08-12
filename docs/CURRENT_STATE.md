# Current State

**Status:** active
**Active backlog item:** TODO-005
**Last verified:** 2026-08-11

## Objective

Maintain AI-Playbooks as an OpenCode-first methodology. Model changes happen inside OpenCode; Codex/Claude handoff is historical compatibility only. This is documentation and configuration work only.

## Verified repository state

- Canonical repository: `10minuteswebsite/AI-Playbooks`.
- Branch `standard/agent-interoperability-v1` starts from current `main` commit `499ad6a`.
- Recent main history includes the universal handoff, active-interaction, and TODO backlog releases through `83cd69c`.
- No application runtime, deployment manifest, or application dependencies are present in the repository; functional application code is out of scope.
- Existing project templates already provide `moving.md`, `HANDOFF.md`, `TODO.md`, `AGENTS.md`, `CLAUDE.md`, progressive workflow, current state, and validation.

## Completed session memory

### Completed

- PR #11 `make OpenCode the primary architect platform` is merged into `main` (commit `83cd69c`).
- Added root-level provider-neutral project instructions and continuity memory plus `opencode.json` with the public canonical bootstrap URL.
- Replaced current user guidance and templates that required switching between platforms; preserved legacy adapters and historical ADRs.
- Added ADR-0005 defining OpenCode as the primary operating model.
- Added Agent Interoperability Standard v1, ADR-0006, reusable instructions/PR assets, and the `agent-handoff-check` workflow/script.

### Decisions

- OpenCode is the primary operating platform per ADR-0005; Codex and Claude remain only historical compatibility artifacts.
- OpenCode loads only the short remote `ARCHITECT_BOOTSTRAP.md`; large playbooks remain lazy and repository-controlled.
- Existing agent-specific files are preserved; no provider-specific behavior is removed.
- No keys, tokens, dependencies, application code, or deployment settings are introduced.

### Verification

- Passed: existing JSON/documentation/secret/handoff/architect/discovery checks; interoperability fixture and final diff checks remain pending.

## Next exact step

Complete validation for TODO-005, then publish the canonical branch and PR without merging or deploying.

## Important files

- `moving.md`, `HANDOFF.md`, `TODO.md`: universal continuation memory.
- `opencode.json`: OpenCode remote bootstrap configuration.
- `ARCHITECT_BOOTSTRAP.md`: public canonical entry point.
- `templates/project/`: files installed into managed projects.
- `scripts/`: executable validation and bootstrap behavior.
