<!-- ai-playbooks-handoff:v3 -->
# AI-Playbooks project continuity

This repository is the canonical method for software and AI-agent delivery. It contains no application runtime; changes here affect playbooks, standards, templates, examples, and validation tooling.

## Current work

- Branch: `standard/agent-interoperability-v1`.
- Objective: publish Agent Interoperability Standard v1 and reusable handoff enforcement assets for the canonical repository and Enrutador pilot.
- Completed: canonical standard, ADR-0006, PR template, reusable adapters, and handoff-check workflow prepared.
- Commit pushed: `1d1ca54` (`add agent interoperability standard v1`).
- Pull Request: [#14](https://github.com/10minuteswebsite/AI-Playbooks/pull/14), draft and open.
- Pending: human review of the canonical PR; the Enrutador pilot PR is also open.

## Decisions and constraints

- GitHub is the only permanent source of truth; local checkouts are temporary agent workspaces.
- `moving.md` is the universal entry point. Context is read progressively through `HANDOFF.md`, `docs/CURRENT_STATE.md`, `TODO.md`, and only the next relevant artifacts.
- OpenCode is the primary operating platform per ADR-0005. Existing Codex and Claude files are preserved only as legacy compatibility artifacts. OpenCode receives a standard `opencode.json` remote instruction pointing to the public canonical bootstrap; no keys or secrets belong there.
- Agent Interoperability Standard v1 requires durable handoff, remote commit verification, PR evidence, explicit `BLOCKED` reporting, and human-only merge/deploy by default.
- This migration does not change application code, dependencies, or deployment.

## Continuation

Read `docs/CURRENT_STATE.md`, then `TODO.md` item `TODO-005`. Use current Git history as evidence. Do not reconstruct this work from chat.

## Session close

Update the backlog and current state with real verification results, review the diff, commit, push, and open the requested pull request. End with “Ya terminé” and evidence, or ask one exact blocking question.
