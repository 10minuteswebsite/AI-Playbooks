# ADR-0003: Repository-Native Project Plan and Backlog

**Status:** Accepted
**Date:** 2026-08-05
**Decision owners:** Repository owner
**Supersedes / superseded by:** Extends [ADR-0002](0002-universal-moving-handoff.md)

## Context

The universal handoff records the active objective and next exact step, but software development continually reveals additional work. Without a shared backlog, those tasks remain trapped in conversations, are forgotten, or are implemented immediately and silently expand the current scope. `CURRENT_STATE.md` cannot hold the full plan without becoming large and stale.

## Decision drivers

- preserve the initial development plan and discovered work;
- keep current state short;
- prevent silent scope expansion;
- provide any agent with the same priorities and blockers;
- retain detailed execution history in GitHub rather than duplicating it;
- remain simple enough for a non-programmer to review.

## Considered options

### Put every pending task in `CURRENT_STATE.md`

- Benefits: one fewer file.
- Costs and risks: operational state becomes a large backlog, obscures the next step, and increases context consumption.

### Use only GitHub Issues

- Benefits: strong assignment, labels, and discussion features.
- Costs and risks: depends on connector access, is less portable to offline or temporary agents, and creates a second access barrier during startup.

### Keep a concise repository-native `TODO.md`

- Benefits: universally readable, versioned with the project, available to every agent, and easy for a non-programmer to inspect.
- Costs and risks: requires maintenance discipline and can duplicate GitHub if completed history is allowed to accumulate.

## Decision

Add root `TODO.md` as the source of truth for the initial development plan and complete known backlog. Use stable `TODO-NNN` identifiers and the sections `Now`, `Next`, `Later`, `Blocked`, and `Recently completed`.

Keep `docs/CURRENT_STATE.md` focused on the active backlog item, session evidence, and next exact step. Use `docs/work-items/` for detailed specifications of selected complex tasks. Store full completion history in Git and GitHub, retaining only recent completions in `TODO.md`.

When work is discovered during implementation, record it in `Next` or `Later` without changing the active scope. Reprioritization that changes product outcomes follows the normal human decision boundary.

## Consequences

### Positive

- discovered work is not lost between agents or conversations;
- the active increment remains focused;
- the initial plan and future priorities are visible in one place;
- current-state context remains small;
- task history stays independently verifiable in GitHub.

### Negative or accepted tradeoffs

- agents must keep backlog and current state consistent;
- duplicate or vague tasks can accumulate without validation;
- projects using older templates require a controlled update to receive `TODO.md`.

## Validation and rollback

- Evidence or experiment: bootstrap tests create, update, and validate a backlog while cross-agent continuation recovers the active task identifier.
- Success criteria: every managed project has a valid `TODO.md`, active state points to a backlog item, and discovered work can be recorded without changing current scope.
- Review date or trigger: recurring duplicate tasks, stale backlog incidents, or a decision to use GitHub Issues as the canonical planner.
- Rollback/replacement plan: remove `TODO.md` from the manifest and routing while migrating unresolved items to the chosen replacement without deleting Git history.
