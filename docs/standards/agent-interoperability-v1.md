# Agent Interoperability Standard v1

**Status:** Stable
**Version:** 1.0.0
**Scope:** Codex, OpenCode, Claude Code, and future repository-capable agents
**Source of truth:** GitHub repository state

## Purpose

This standard makes agent work resumable without chat history. GitHub stores the durable project state; a chat session is temporary execution context. Agents are replaceable, and model changes inside the same platform do not change the project state.

## Session bootstrap

Before substantive work, an agent must:

1. Treat GitHub and the current repository as the durable source of truth.
2. Read `moving.md`, `TODO.md`, and `docs/CURRENT_STATE.md`.
3. Read the relevant contracts, tests, architecture notes, and project documentation only for the requested task.
4. Inspect the current branch and relevant recent commits.
5. Reconstruct state from the repository, never from previous chat history.
6. If the user says `continúa` or `continue`, select the next unblocked step documented in the repository and proceed.
7. If the user gives a new task, use durable state as context before editing.

`moving.md` is the shortest entry point. `HANDOFF.md` defines collaboration and session close. `TODO.md` holds the complete plan and backlog. `docs/CURRENT_STATE.md` records the active increment, decisions, verification, risks, blockers, and exact next step.

## Durable handoff and definition of done

A substantive task is complete only when applicable items are complete:

1. Required tests and validations ran, with actual results recorded.
2. `moving.md` reflects the current state and exact next logical step when the project protocol requires it.
3. `TODO.md` records status changes and newly discovered work without silently expanding scope.
4. `docs/CURRENT_STATE.md` reflects architecture, integrations, runtime/deployment state, decisions, risks, and verification when they changed.
5. Relevant code, tests, configuration, and documentation are committed.
6. The task branch is pushed to `origin`.
7. The final commit is verified on the remote branch.
8. A Pull Request targets the intended base branch.

The PR must state what changed, tests and results, risks or limitations, remaining work, the recommended next step, and deployment status. If any required step fails, do not claim completion: report `BLOCKED`, the exact failed step and error, what completed, what remains, and the minimum human action required.

## GitHub and human authority

Use a dedicated branch and focused commits. Push only verified work. Agents may prepare branches and Pull Requests. Human approval is required for merge and deployment by default, as well as production access, destructive actions, secrets, privilege expansion, spending, or material risk acceptance.

## Compatibility

- **Codex:** reads `AGENTS.md`.
- **OpenCode:** reads local `AGENTS.md` and the existing `opencode.json` canonical bootstrap without changing model/provider selection or permission safeguards.
- **Claude Code:** reads `CLAUDE.md`, which should import `AGENTS.md` rather than duplicate it.
- **Future agents:** follow `moving.md` and the repository-native memory hierarchy; no provider-specific behavior is required.

## Validation and versioning

Repositories should provide a lightweight `agent-handoff-check` workflow that validates required PR evidence and, for substantive project changes, confirms durable handoff files are included. Documentation-only changes may omit `moving.md` when durable project state is not changed. Increment the standard's semantic version when its requirements change and record consequential changes in an ADR or changelog.
