# Current State

**Status:** active
**Active backlog item:** TODO-004
**Last verified:** 2026-08-08

## Objective

Maintain AI-Playbooks as an OpenCode-first methodology. Model changes happen inside OpenCode; Codex/Claude handoff is historical compatibility only. This is documentation and configuration work only.

## Verified repository state

- Canonical repository: `10minuteswebsite/AI-Playbooks`.
- Current branch: `agent/opencode-first-method`.
- Recent main history includes the universal handoff, active-interaction, and TODO backlog releases through `ca459dc`.
- No application runtime, deployment manifest, or application dependencies are present in the repository; functional application code is out of scope.
- Existing project templates already provide `moving.md`, `HANDOFF.md`, `TODO.md`, `AGENTS.md`, `CLAUDE.md`, progressive workflow, current state, and validation.

## This session

### Completed

- Reviewed the canonical playbooks, templates, scripts, recent commits, and repository status.
- Confirmed OpenCode's current configuration schema and remote `instructions` support from its official documentation.
- Added root-level provider-neutral project instructions and continuity memory plus `opencode.json` with the public canonical bootstrap URL.
- Replaced current user guidance and templates that required switching between platforms; preserved legacy adapters and historical ADRs.
- Added ADR-0005 defining OpenCode as the primary operating model.

### Decisions

- OpenCode loads only the short remote `ARCHITECT_BOOTSTRAP.md`; large playbooks remain lazy and repository-controlled.
- Existing agent-specific files are preserved; no provider-specific behavior is removed.
- No keys, tokens, dependencies, application code, or deployment settings are introduced.

### Verification

- Completed: repository and history inspection; official OpenCode schema documentation review.
- Passed: JSON parse, documentation validation, secret scan, project handoff tests, GitHub-first architect tests, finite discovery tests, legacy compatibility validation, and `git diff --check`.
- Commit created: `make OpenCode the primary architect platform` (see GitHub history).
- Pending: push and pull request.

## Next exact step

Push the OpenCode-first TODO-004 commit and open its pull request, then record the resulting URL and verification evidence here.

## Important files

- `moving.md`, `HANDOFF.md`, `TODO.md`: universal continuation memory.
- `opencode.json`: OpenCode remote bootstrap configuration.
- `ARCHITECT_BOOTSTRAP.md`: public canonical entry point.
- `templates/project/`: files installed into managed projects.
- `scripts/`: executable validation and bootstrap behavior.
