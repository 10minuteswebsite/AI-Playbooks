# ADR-0005: OpenCode-First Operating Model

**Status:** Accepted
**Date:** 2026-08-08
**Decision owners:** Repository owner
**Supersedes:** The current-workflow portions of [ADR-0001](0001-cross-agent-project-memory.md) and [ADR-0002](0002-universal-moving-handoff.md)

## Context

The repository was originally written around switching between Codex and Claude Code. The project is now moving to OpenCode, where multiple models can be selected inside one platform. Requiring a platform handoff adds unnecessary instructions, duplicates context, and makes the primary workflow appear more complex than it is.

## Decision

OpenCode is the primary operating platform. Project instructions use `opencode.json` to load the canonical bootstrap, and `moving.md`, `HANDOFF.md`, `TODO.md`, and `docs/CURRENT_STATE.md` remain the repository memory for new sessions. Changing models inside OpenCode does not require a handoff, a new adapter, or repeated project explanation.

Existing `AGENTS.md`, `CLAUDE.md`, global profile files, and historical cross-agent examples are preserved only when useful for compatibility or historical traceability. They must not be required by current startup instructions, tests, or user guidance.

## Consequences

- The user has one simple workflow: open the OpenCode project, choose a model, and say “Usa el arquitecto” or continue from `moving.md`.
- The repository remains the durable source of truth and supports a new OpenCode session without conversation history.
- Legacy files can be removed later through a separate cleanup decision once compatibility needs are known.
- Documentation and validation now describe OpenCode first; historical ADRs retain the reason the earlier design existed.

## Verification and rollback

Verify the OpenCode configuration, bootstrap, handoff, documentation, and secret checks. If OpenCode is replaced later, add a new platform decision and retain the repository memory protocol; do not restore platform-switching as a requirement unless evidence requires it.
