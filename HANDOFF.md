<!-- ai-playbooks-handoff:v3 -->
# AI-Playbooks handoff

This repository is the canonical method for software and AI-agent delivery. It contains no application runtime; changes here affect playbooks, standards, templates, examples, and validation tooling.

## Current work

- Branch: `migration/opencode_prep`.
- Objective: prepare the repository and generated project structure for provider-neutral continuation with OpenCode while preserving Codex and Claude compatibility.
- Completed in this increment: repository review, migration design, OpenCode configuration, project-level continuity files, template support, ADR, and validation updates.
- Commit created: `prepare repository for OpenCode migration` (see GitHub history).
- Pull request: [#10](https://github.com/10minuteswebsite/AI-Playbooks/pull/10), draft.
- Pending: review and merge according to repository policy.

## Decisions and constraints

- GitHub is the only permanent source of truth; local checkouts are temporary agent workspaces.
- `moving.md` is the universal entry point. Context is read progressively through `HANDOFF.md`, `docs/CURRENT_STATE.md`, `TODO.md`, and only the next relevant artifacts.
- Existing Codex and Claude files must be preserved. OpenCode receives a standard `opencode.json` remote instruction pointing to the public canonical bootstrap; no keys or secrets belong there.
- This migration does not change application code, dependencies, or deployment.

## Continuation

Read `docs/CURRENT_STATE.md`, then `TODO.md` item `TODO-001`. Use the current diff and recent history as evidence. Do not reconstruct this work from chat.

## Session close

Update the backlog and current state with real verification results, review the diff, commit, push, and open the requested pull request. End with “Ya terminé” and evidence, or ask one exact blocking question.
