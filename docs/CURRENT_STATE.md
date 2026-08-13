# Current State

**Status:** validator strengthened; awaiting remote CI and third independent review
**Active backlog item:** TODO-006
**Last verified:** 2026-08-13

## Objective

Correct PR #15 so the proposed Arquitecto Omnicanal v2 skill can become the single GitHub-canonical skill shared by Codex, Claude Code, and OpenCode after independent approval and human merge. This is documentation and skill packaging work only.

## Verified repository state

- Canonical repository: `10minuteswebsite/AI-Playbooks`.
- Branch `agent/canonical-omnichannel-architect-skill` starts from current `main` commit `044ea9c`.
- Agent Interoperability Standard v1 is merged in PR #14 at `044ea9c`.
- No application runtime, deployment manifest, or application dependencies are present in the repository; functional application code is out of scope.
- Existing project templates provide `moving.md`, `HANDOFF.md`, `TODO.md`, `docs/PROJECT_CONTEXT.md`, `docs/CURRENT_STATE.md`, `AGENTS.md`, `CLAUDE.md`, progressive workflow, current state, and validation. The skill documents the complete current bootstrap set, including README, PR template, optional adapters, and agent-handoff-check when applicable.

## Completed session memory

### Completed

- Reviewed the merged Agent Interoperability Standard v1, ADR-0006, repository instructions, and durable state before editing.
- Added the complete installed Arquitecto Omnicanal v2 skill under `skills/omnichannel-agent-architect/`, including its operational references, installation guidance, and agent metadata.
- Proposed that repository folder as the candidate canonical source shared by Codex, Claude Code, and OpenCode after human-approved merge.
- PR #11 `make OpenCode the primary architect platform` is merged into `main` (commit `83cd69c`).
- Added root-level provider-neutral project instructions and continuity memory plus `opencode.json` with the public canonical bootstrap URL.
- Replaced current user guidance and templates that required switching between platforms; preserved legacy adapters and historical ADRs.
- Added ADR-0005 defining OpenCode as the primary operating model.
- Added Agent Interoperability Standard v1, ADR-0006, reusable instructions/PR assets, and the `agent-handoff-check` workflow/script.
- Corrected PR #15 routing precedence, new-repository bootstrap requirements, `moving.md` semantics, pre-merge canonicality language, OpenAI agent behavior, and cross-document consistency after independent review returned `CHANGES REQUIRED`.
- Replaced the original string-search regression check with a dependency-free structural validator that extracts concrete Markdown sections and the OpenAI YAML prompt before checking localized invariants.
- Added 10 mutation tests using only the Python standard library and temporary copies; each required invalid variant is rejected.
- Added `.github/workflows/omnichannel-architect-validation.yml` so skill/validator changes run as a dedicated remote check.
- Clarified that structural validation does not replace secret scanning, diff/dependency review, functional testing, deployment review, or human review.
- Corrected a contradiction exposed by remote CI: `agent-handoff-check` now requires `HANDOFF.md`, `TODO.md`, and `docs/CURRENT_STATE.md` for substantive changes instead of requiring a mutable update to stable, navigational `moving.md`.

### Decisions

- `skills/omnichannel-agent-architect/` is the candidate canonical skill source in PR #15; it becomes canonical only after human-approved merge. Local/product-managed installations remain replaceable copies.
- The skill preserves GitHub-first durable state, provider-neutral continuation, human-only merge/deploy, and existing omnichannel architecture principles.
- OpenCode is the primary operating platform per ADR-0005; Codex and Claude remain only historical compatibility artifacts.
- OpenCode loads only the short remote `ARCHITECT_BOOTSTRAP.md`; large playbooks remain lazy and repository-controlled.
- Existing agent-specific files are preserved; no provider-specific behavior is removed.
- No keys, tokens, dependencies, application code, or deployment settings are introduced.

### Verification

- Passed after the validator changes: documentation validation (94 Markdown files), secret scan, project handoff/bootstrap, GitHub-first architect, finite discovery, global instruction consistency, structural validation of real content, all 10 mutation tests, agent-handoff-check fixtures, JSON syntax, skill/agent/workflow YAML syntax, and `git diff --check`.
- The agent-handoff-check fixture suite passed its positive case and correctly rejected its expected negative case missing `## Durable handoff`.
- Pull Request: [#15](https://github.com/10minuteswebsite/AI-Playbooks/pull/15), draft, targeting `main`; no merge or deployment performed.

## Next exact step

Commit and push the strengthened validator to the existing Draft PR #15, wait for remote CI, then obtain a third independent review. TODO-006 remains active until human-approved merge; do not merge or deploy without explicit human approval.

## Important files

- `moving.md`, `HANDOFF.md`, `TODO.md`: universal continuation memory.
- `opencode.json`: OpenCode remote bootstrap configuration.
- `ARCHITECT_BOOTSTRAP.md`: public canonical entry point.
- `templates/project/`: files installed into managed projects.
- `scripts/`: executable validation and bootstrap behavior.
- `skills/omnichannel-agent-architect/`: proposed canonical Arquitecto Omnicanal skill source in PR #15.
