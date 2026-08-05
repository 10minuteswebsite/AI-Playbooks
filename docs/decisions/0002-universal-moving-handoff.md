# ADR-0002: Universal Progressive Agent Handoff

**Status:** Accepted
**Date:** 2026-08-04
**Decision owners:** Repository owner
**Supersedes / superseded by:** Extends [ADR-0001](0001-cross-agent-project-memory.md); extended by [ADR-0003](0003-project-plan-and-backlog.md)

## Context

Project memory already separates durable context from current operational state, but entry still depends on Codex- and Claude-specific adapters. A person moving between agents needs one short, memorable command and must not copy conversations, repeat project facts, or load the entire repository into an agent's context window.

## Decision drivers

- tool- and vendor-neutral continuation;
- minimal initial context;
- repository and GitHub as verifiable memory;
- no duplicated history or instructions;
- a mandatory, reproducible session close;
- compatibility with existing agent adapters.

## Considered options

### Expand every agent-specific instruction file

- Benefits: each supported tool receives direct instructions.
- Costs and risks: duplication, drift, tool lock-in, growing context, and continuous maintenance for new agents.

### Put all project knowledge in one large handoff file

- Benefits: one document appears self-contained.
- Costs and risks: stale duplicated facts, large context consumption, merge conflicts, and weak separation between durable and volatile information.

### Universal entry plus progressive repository memory

- Benefits: short invocation, agent neutrality, small initial context, existing documents remain authoritative, and Git retains detailed evidence.
- Costs and risks: agents must follow links progressively and every substantive session must maintain current state accurately.

## Decision

Add `moving.md` as the minimal universal entry and `HANDOFF.md` as the stable collaboration contract. Keep durable facts in `docs/PROJECT_CONTEXT.md`, volatile state in `docs/CURRENT_STATE.md`, detailed operating policy in `docs/AI_WORKFLOW.md`, and historical evidence in GitHub.

Require all substantive sessions to update current state with completed and pending work, session decisions, blockers, verification, important files, and one next exact safe step. Agents load the entry and current state first, then only the artifacts required by that step.

Retain `AGENTS.md` and `CLAUDE.md` as optional compatibility adapters that point to the universal entry. Do not make the protocol dependent on either tool.

## Consequences

### Positive

- the same user instruction works with Codex, Claude, and future agents;
- handoff no longer requires conversation history;
- initial context stays small;
- detailed progress remains verifiable in GitHub;
- adapters can be added or removed without changing project memory.

### Negative or accepted tradeoffs

- stale `CURRENT_STATE.md` can mislead the next agent, so validation and mandatory session close are required;
- older managed projects need a controlled template upgrade to receive the two new files;
- an agent that ignores repository instructions can still fail to follow the protocol.

## Validation and rollback

- Evidence or experiment: bootstrap and validator tests simulate Claude, Codex, and a vendor-neutral third agent continuing without chat history.
- Success criteria: the third agent recovers the exact next step from `moving.md`, `HANDOFF.md`, current state, and Git evidence while loading no unrelated project documentation.
- Review date or trigger: repeated stale-state incidents, material agent instruction changes, or a need to support a non-Git source of truth.
- Rollback/replacement plan: revert the entry and handoff templates while preserving `PROJECT_CONTEXT`, `CURRENT_STATE`, and Git history.
