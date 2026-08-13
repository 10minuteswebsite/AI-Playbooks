# Project Context: AI-Playbooks

## Purpose

This public repository is a reusable operating system for creating and maintaining software and AI-agent projects with people and AI. It is documentation and tooling, not a deployable application.

## Main areas

- `playbooks/`: delivery core, architect, discovery, profiles, and roles.
- `skills/omnichannel-agent-architect/`: candidate shared skill source proposed by PR #15 for Codex, Claude Code, and OpenCode; it becomes canonical after a human-approved merge.
- `standards/`: documentation, testing, security, AI evaluation, observability, supply chain, and release guidance.
- `templates/`: project memory, handoff, agent adapters, planning, architecture, risk, operations, and release artifacts.
- `scripts/`: documentation, secret, global-instruction, bootstrap, and handoff validation.
- `examples/`: worked reference flows.

## Collaboration constraints

GitHub is the durable source of truth. OpenCode is the primary platform and supports changing models without changing project continuity. Preserve existing behavior and configuration, avoid secrets and private conversation content, and make small verifiable changes. Legacy Codex/Claude files may remain but must not be required. OpenCode enters through `moving.md` and reads progressively.

PR #15 proposes that the three supported agent clients share `skills/omnichannel-agent-architect/` as their single source. Until human-approved merge, it is a candidate canonical source. Local or product-managed skill directories are replaceable operational copies and must not diverge into provider-specific Architect skills.
