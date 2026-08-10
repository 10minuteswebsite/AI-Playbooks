<!-- ai-playbooks-handoff:v3 -->
# AI-Playbooks project continuity

This repository is the canonical method for software and AI-agent delivery. It contains no application runtime; changes here affect playbooks, standards, templates, examples, and validation tooling.

## Current work

- Branch: `main` (current work happens on short-lived feature branches from `main`).
- Objective: keep the repository and generated project structure optimized for OpenCode, with model changes handled inside the same platform.
- Completed in this increment: audited current references; updated current playbooks, bootstrap, guides, templates, examples, validators, project manifest, and ADR-0005.
- Published: PR #11 merged into `main` as commit `83cd69c`; TODO-004 marked completed.

## Decisions and constraints

- GitHub is the only permanent source of truth; local checkouts are temporary agent workspaces.
- `moving.md` is the universal entry point. Context is read progressively through `HANDOFF.md`, `docs/CURRENT_STATE.md`, `TODO.md`, and only the next relevant artifacts.
- Existing Codex and Claude files are preserved only as legacy compatibility artifacts. OpenCode receives a standard `opencode.json` remote instruction pointing to the public canonical bootstrap; no keys or secrets belong there.
- This migration does not change application code, dependencies, or deployment.

## Continuation

Read `docs/CURRENT_STATE.md`, then the current `TODO.md`. The OpenCode-first increment (TODO-004) is merged in `main`; use the current diff and recent history as evidence. Do not reconstruct this work from chat.

## Session close

Update the backlog and current state with real verification results, review the diff, commit, push, and open the requested pull request without merging automatically. End with “Ya terminé” and evidence, or ask one exact blocking question.
