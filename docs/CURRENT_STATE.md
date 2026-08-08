# Current State

**Status:** complete
**Active backlog item:** None
**Last verified:** 2026-08-07

## Objective

Prepare AI-Playbooks for provider-neutral continuation with OpenCode while retaining Codex and Claude compatibility. This is documentation and configuration work only.

## Verified repository state

- Canonical repository: `10minuteswebsite/AI-Playbooks`.
- Current branch: `migration/opencode_prep`.
- Recent main history includes the universal handoff, active-interaction, and TODO backlog releases through `ca459dc`.
- No application runtime, deployment manifest, or application dependencies are present in the repository; functional application code is out of scope.
- Existing project templates already provide `moving.md`, `HANDOFF.md`, `TODO.md`, `AGENTS.md`, `CLAUDE.md`, progressive workflow, current state, and validation.

## This session

### Completed

- Reviewed the canonical playbooks, templates, scripts, recent commits, and repository status.
- Confirmed OpenCode's current configuration schema and remote `instructions` support from its official documentation.
- Added root-level provider-neutral project instructions and continuity memory plus `opencode.json` with the public canonical bootstrap URL.

### Decisions

- OpenCode loads only the short remote `ARCHITECT_BOOTSTRAP.md`; large playbooks remain lazy and repository-controlled.
- Existing agent-specific files are preserved; no provider-specific behavior is removed.
- No keys, tokens, dependencies, application code, or deployment settings are introduced.

### Verification

- Completed: repository and history inspection; official OpenCode schema documentation review.
- Passed: JSON parse, documentation validation, secret scan, project handoff tests, GitHub-first architect tests, finite discovery tests, global-instruction validation, and `git diff --check`.
- Commit published: `prepare repository for OpenCode migration` (see GitHub history).
- Draft pull request: [#10](https://github.com/10minuteswebsite/AI-Playbooks/pull/10).

## Next exact step

Review and merge pull request [#10](https://github.com/10minuteswebsite/AI-Playbooks/pull/10) when repository policy permits.

## Important files

- `moving.md`, `HANDOFF.md`, `TODO.md`: universal continuation memory.
- `opencode.json`: OpenCode remote bootstrap configuration.
- `ARCHITECT_BOOTSTRAP.md`: public canonical entry point.
- `templates/project/`: files installed into managed projects.
- `scripts/`: executable validation and bootstrap behavior.
