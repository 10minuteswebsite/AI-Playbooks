# Current State

**Status:** awaiting human review
**Active backlog item:** None
**Last verified:** 2026-08-13

## Objective

Publish the installed Arquitecto Omnicanal v2 skill as the single GitHub-canonical skill shared by Codex, Claude Code, and OpenCode. This is documentation and skill packaging work only.

## Verified repository state

- Canonical repository: `10minuteswebsite/AI-Playbooks`.
- Branch `agent/canonical-omnichannel-architect-skill` starts from current `main` commit `044ea9c`.
- Agent Interoperability Standard v1 is merged in PR #14 at `044ea9c`.
- No application runtime, deployment manifest, or application dependencies are present in the repository; functional application code is out of scope.
- Existing project templates already provide `moving.md`, `HANDOFF.md`, `TODO.md`, `AGENTS.md`, `CLAUDE.md`, progressive workflow, current state, and validation.

## Completed session memory

### Completed

- Reviewed the merged Agent Interoperability Standard v1, ADR-0006, repository instructions, and durable state before editing.
- Added the complete installed Arquitecto Omnicanal v2 skill under `skills/omnichannel-agent-architect/`, including its operational references, installation guidance, and agent metadata.
- Declared that repository folder as the canonical source shared by Codex, Claude Code, and OpenCode.
- PR #11 `make OpenCode the primary architect platform` is merged into `main` (commit `83cd69c`).
- Added root-level provider-neutral project instructions and continuity memory plus `opencode.json` with the public canonical bootstrap URL.
- Replaced current user guidance and templates that required switching between platforms; preserved legacy adapters and historical ADRs.
- Added ADR-0005 defining OpenCode as the primary operating model.
- Added Agent Interoperability Standard v1, ADR-0006, reusable instructions/PR assets, and the `agent-handoff-check` workflow/script.

### Decisions

- `skills/omnichannel-agent-architect/` is the single canonical skill source; local/product-managed installations are replaceable copies.
- The skill preserves GitHub-first durable state, provider-neutral continuation, human-only merge/deploy, and existing omnichannel architecture principles.
- OpenCode is the primary operating platform per ADR-0005; Codex and Claude remain only historical compatibility artifacts.
- OpenCode loads only the short remote `ARCHITECT_BOOTSTRAP.md`; large playbooks remain lazy and repository-controlled.
- Existing agent-specific files are preserved; no provider-specific behavior is removed.
- No keys, tokens, dependencies, application code, or deployment settings are introduced.

### Verification

- Passed: installed-source byte parity, documentation validation (94 Markdown files), secret scan, project handoff/bootstrap, GitHub-first architect, finite discovery, global instruction, interoperability fixture, JSON, skill YAML, and `git diff --check`.
- The direct handoff checker correctly rejected an empty PR body; its fixture suite passed with complete evidence and expected negative cases.
- Pull Request: [#15](https://github.com/10minuteswebsite/AI-Playbooks/pull/15), draft, targeting `main`; no merge or deployment performed.

## Next exact step

Human review of PR #15 is the next step. Do not merge or deploy without explicit human approval.

## Important files

- `moving.md`, `HANDOFF.md`, `TODO.md`: universal continuation memory.
- `opencode.json`: OpenCode remote bootstrap configuration.
- `ARCHITECT_BOOTSTRAP.md`: public canonical entry point.
- `templates/project/`: files installed into managed projects.
- `scripts/`: executable validation and bootstrap behavior.
- `skills/omnichannel-agent-architect/`: canonical shared Arquitecto Omnicanal skill.
