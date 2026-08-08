# ADR-0004: Provider-Neutral OpenCode Loading

**Status:** Accepted
**Date:** 2026-08-07
**Decision owners:** Repository owner
**Extends:** [ADR-0002](0002-universal-moving-handoff.md) and [ADR-0003](0003-project-plan-and-backlog.md)

## Context

Projects need to move from Codex and Claude Code to OpenCode without copying conversations or duplicating the canonical playbooks. OpenCode's current configuration supports the official `https://opencode.ai/config.json` schema and remote URLs in its `instructions` array.

## Decision

Add `opencode.json` to the project template and to this repository. It loads only the public `ARCHITECT_BOOTSTRAP.md` URL. The bootstrap routes the agent into repository memory and tells it to load larger playbooks progressively when the task requires them. Existing `AGENTS.md`, `CLAUDE.md`, and other useful configuration remain intact.

## Consequences

- OpenCode can start from the same vendor-neutral method as other agents.
- Large playbooks are not duplicated in each project or loaded into every context window.
- The remote bootstrap must remain publicly available; a repository-local `AGENTS.md` and `moving.md` remain the durable fallback.
- The configuration contains no credentials or provider keys.

## Verification and rollback

Validate JSON, check the official schema URL and canonical bootstrap URL, run project handoff and documentation checks, and review the secret scan. Removing `opencode.json` and reverting this ADR restores the prior adapter set without affecting application code.
