# ADR-0001: Shared Project Memory and Automatic Git Handoff

**Status:** Accepted
**Date:** 2026-07-27
**Decision owners:** Repository owner
**Supersedes / superseded by:** None

## Context

Codex and Claude Code need to work interchangeably without relying on conversation history or loading an entire repository into context. Existing global instructions point to AI-Playbooks but do not define project-local memory, safe adoption, or a complete Git handoff.

## Decision drivers

- one durable source of truth;
- minimal context loading;
- safe adoption of existing projects;
- non-technical invocation;
- autonomous, traceable delivery;
- explicit human control for sensitive changes.

## Considered options

### Duplicate complete instructions in AGENTS.md and CLAUDE.md

- Benefits: each agent has a standalone file.
- Costs and risks: drift, contradiction, duplicated context, and expensive maintenance.

### Short adapters with one shared workflow and two memory documents

- Benefits: consistent behavior, small context footprint, stable versus volatile information separation, and tool portability.
- Costs and risks: agents must follow references correctly; structural validation is required.

## Decision

Use short `AGENTS.md` and `CLAUDE.md` adapters that reference `docs/AI_WORKFLOW.md`. Store durable facts in `docs/PROJECT_CONTEXT.md` and operational handoff in `docs/CURRENT_STATE.md`. Require approval before adopting an existing unmanaged project and never overwrite conflicting files automatically.

Completed verified work is committed, pushed, and proposed through a pull request automatically. Normal reversible changes may merge automatically after all gates pass. Sensitive, destructive, production, security, data, payment, access, material-risk, or meaningful-cost changes require human approval before merge.

## Consequences

### Positive

- either agent can resume from repository evidence;
- conversations remain small and disposable;
- shared policy cannot silently diverge between adapters;
- Git preserves detailed history outside memory documents.

### Negative or accepted tradeoffs

- current state must be maintained accurately;
- legacy instruction conflicts require review;
- remote automation depends on GitHub authentication and repository policy.

## Validation and rollback

- Evidence: end-to-end bootstrap, adoption, conflict, handoff, and continuation tests.
- Success criteria: a second agent continues from one exact step without prior chat context.
- Review trigger: agent instruction precedence changes or repeated handoff failures.
- Rollback/replacement plan: remove the adapters and memory structure in a focused revert while preserving Git history.
