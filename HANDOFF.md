<!-- ai-playbooks-handoff:v3 -->
# AI-Playbooks project continuity

This repository is the canonical method for software and AI-agent delivery. It contains no application runtime; changes here affect playbooks, standards, templates, examples, and validation tooling.

## Current work

- Branch: `agent/canonical-omnichannel-architect-skill`.
- Objective: correct PR #15 so the installed Arquitecto Omnicanal v2 skill can become the canonical shared source for Codex, Claude Code, and OpenCode after independent approval and human merge.
- Completed: reviewed merged interoperability PR #14, added the complete installed skill, resolved the substantive review findings, and replaced the superficial regression check with a section-aware structural validator plus 10 mutation tests. Added dedicated path-filtered CI and documented the boundary between automated invariants, separate PR checks, and human review. Applicable local validations pass.
- Pull Request: [#15](https://github.com/10minuteswebsite/AI-Playbooks/pull/15), draft, targeting `main`.
- Pending: push the validator commit, wait for its remote checks, then obtain a third independent review of PR #15. TODO-006 remains active until human-approved merge; merge is outside this task and no deployment applies.

## Decisions and constraints

- GitHub is the only permanent source of truth; local checkouts are temporary agent workspaces.
- `moving.md` is the universal entry point. Context is read progressively through `HANDOFF.md`, `docs/CURRENT_STATE.md`, `TODO.md`, and only the next relevant artifacts.
- OpenCode is the primary operating platform per ADR-0005. Existing Codex and Claude files are preserved only as legacy compatibility artifacts. OpenCode receives a standard `opencode.json` remote instruction pointing to the public canonical bootstrap; no keys or secrets belong there.
- Agent Interoperability Standard v1 requires durable handoff, remote commit verification, PR evidence, explicit `BLOCKED` reporting, and human-only merge/deploy by default.
- `skills/omnichannel-agent-architect/` is the proposed canonical skill source in PR #15. It becomes canonical only after human-approved merge; local and product-managed installations are operational copies.
- This migration does not change application code, dependencies, or deployment.
- `scripts/test_omnichannel_architect_skill.py` extracts concrete Markdown/YAML sections, checks deterministic structural invariants, and rejects 10 known-invalid temporary mutations. It does not replace secret scanning, diff/dependency review, functional/deploy checks, or human judgment.

## Continuation

Read `docs/CURRENT_STATE.md`, then active item `TODO-006` in `TODO.md`. Use current Git history and PR #15 as evidence. Do not reconstruct this work from chat.

## Session close

Update the backlog and current state with real verification results, review the diff, commit, push, and open the requested pull request. End with “Ya terminé” and evidence, or ask one exact blocking question.
