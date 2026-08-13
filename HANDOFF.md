<!-- ai-playbooks-handoff:v3 -->
# AI-Playbooks project continuity

This repository is the canonical method for software and AI-agent delivery. It contains no application runtime; changes here affect playbooks, standards, templates, examples, and validation tooling.

## Current work

- Branch: `agent/canonical-omnichannel-architect-skill`.
- Objective: publish the installed Arquitecto Omnicanal v2 skill as the canonical shared source for Codex, Claude Code, and OpenCode.
- Completed: reviewed merged interoperability PR #14 and added the complete installed skill plus the minimal canonical-source documentation.
- Pending: validations, commit, push, remote SHA verification, Pull Request, and human review.

## Decisions and constraints

- GitHub is the only permanent source of truth; local checkouts are temporary agent workspaces.
- `moving.md` is the universal entry point. Context is read progressively through `HANDOFF.md`, `docs/CURRENT_STATE.md`, `TODO.md`, and only the next relevant artifacts.
- OpenCode is the primary operating platform per ADR-0005. Existing Codex and Claude files are preserved only as legacy compatibility artifacts. OpenCode receives a standard `opencode.json` remote instruction pointing to the public canonical bootstrap; no keys or secrets belong there.
- Agent Interoperability Standard v1 requires durable handoff, remote commit verification, PR evidence, explicit `BLOCKED` reporting, and human-only merge/deploy by default.
- `skills/omnichannel-agent-architect/` is the canonical shared skill; local and product-managed installations are operational copies.
- This migration does not change application code, dependencies, or deployment.

## Continuation

Read `docs/CURRENT_STATE.md`, then `TODO.md` item `TODO-006`. Use current Git history as evidence. Do not reconstruct this work from chat.

## Session close

Update the backlog and current state with real verification results, review the diff, commit, push, and open the requested pull request. End with “Ya terminé” and evidence, or ask one exact blocking question.
