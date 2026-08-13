<!-- ai-playbooks-todo:v1 -->
# Project Plan and Backlog: AI-Playbooks

## Product objective

Provide reusable, provider-neutral, documentation-first operating rules and templates that let people and AI agents deliver software and agent systems safely and continue from GitHub without conversation history.

## Initial development plan

- Phase 0 — Verify the canonical workflow, project memory, migration requirements, and validation evidence.
- Phase 1 — Operate OpenCode as the primary platform with model changes inside the same project.
- Phase 2 — Preserve only useful legacy compatibility files and keep the repository memory protocol platform-independent.

## Now

- [ ] **TODO-006 — Publish the canonical Arquitecto Omnicanal skill**
  - Priority: High
  - Outcome: PR #15 is independently approved and human-merged, making the candidate shared skill source canonical.
  - Dependency: Independent rereview of the requested corrections and human merge authorization.
  - Current evidence: structural validator, 10 mutation tests, dedicated CI workflow, documentation suite, secret scan, handoff checks, and syntax validation pass locally; remote CI pending the next pushed commit.

## Next

- None recorded.

## Later

- [ ] **TODO-002 — Add broader automated coverage for future agent adapters**
  - Priority: Low
  - Outcome: A vendor-neutral adapter fixture can be validated without duplicating provider-specific rules.
  - Dependency: A concrete additional adapter requirement.

## Blocked

- None recorded.

## Recently completed

- Added the universal moving/handoff protocol and repository backlog in prior releases.
- **TODO-001 — Complete provider-neutral OpenCode migration preparation** — OpenCode configuration, root continuity memory, template support, ADR, and validators completed; all checks passed.
- **TODO-003 — Adopt OpenCode-first operating guidance** — Current documentation and templates no longer require switching between platforms; legacy files remain preserved for compatibility.
- **TODO-004 — Publish OpenCode-first operating guidance** — Published and merged into `main` as PR #11 (commit `83cd69c`); OpenCode is the primary platform per ADR-0005 and Codex/Claude remain historical compatibility only. All checks passed.
- **TODO-005 — Publish Agent Interoperability Standard v1** — Merged into `main` as PR #14 (commit `044ea9c`); the canonical standard and reusable enforcement assets are published.

## Maintenance rules

- Use stable `TODO-NNN` IDs and observable outcomes.
- Record discovered work in `Next` or `Later` without silently expanding the active item.
- Keep current state short and update it before every substantive session ends.
