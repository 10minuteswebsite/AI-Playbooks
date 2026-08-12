# ADR-0006: Agent Interoperability Standard v1

**Status:** Accepted
**Date:** 2026-08-11
**Decision owners:** Repository owner

## Context

Agents need to resume work from GitHub without prior chat history, while Codex, OpenCode, Claude Code, and future agents remain replaceable. Existing project memory and OpenCode-first guidance provide the foundation, but repositories also need explicit definition-of-done, PR evidence, blocked behavior, and lightweight enforcement.

## Decision

Adopt `docs/standards/agent-interoperability-v1.md` as the canonical provider-neutral standard. Provide reusable project instructions, Claude import, PR template, and `agent-handoff-check` workflow assets. The check validates PR sections and evidence and requires durable handoff files for substantive project changes. Human merge and deployment remain the default authority boundary.

## Consequences

- New sessions can bootstrap from repository state and the command `continúa` without chat history.
- A task cannot be called complete when required tests, durable state, remote verification, or PR creation failed; the agent must report `BLOCKED`.
- The standard adds small documentation and shell validation assets without runtime dependencies.
- Existing provider-specific files remain available as thin compatibility layers.

## Validation and rollback

Run the repository documentation, secret, handoff, and interoperability tests plus `git diff --check`. The standard can be revised through a new semantic version and ADR; removing the workflow does not remove the repository memory protocol.
