<!-- ai-playbooks-handoff:v3 -->
# AI-Playbooks project continuity

This repository is the canonical method for software and AI-agent delivery. It contains no application runtime; changes here affect playbooks, standards, templates, examples, and validation tooling.

## Current work

- Branch: `main`.
- Objective: keep the repository and generated project structure optimized for OpenCode, with model changes handled inside the same platform.
- Completed: PR #11 `make OpenCode the primary architect platform` is merged into `main` (commit `83cd69c`).
- Pending: none for this increment.

## Decisions and constraints

- GitHub is the only permanent source of truth; local checkouts are temporary agent workspaces.
- `moving.md` is the universal entry point. Context is read progressively through `HANDOFF.md`, `docs/CURRENT_STATE.md`, `TODO.md`, and only the next relevant artifacts.
- OpenCode is the primary operating platform per ADR-0005. Existing Codex and Claude files are preserved only as legacy compatibility artifacts. OpenCode receives a standard `opencode.json` remote instruction pointing to the public canonical bootstrap; no keys or secrets belong there.
- This migration does not change application code, dependencies, or deployment.

## Continuation

Read `docs/CURRENT_STATE.md`, then the active sections of `TODO.md`. Use current Git history as evidence. Do not reconstruct this work from chat.

## Session close

Update the backlog and current state with real verification results, review the diff, commit, push, and open the requested pull request. End with “Ya terminé” and evidence, or ask one exact blocking question.
