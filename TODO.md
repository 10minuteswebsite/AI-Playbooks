<!-- ai-playbooks-todo:v1 -->
# Project Plan and Backlog: AI-Playbooks

## Product objective

Provide reusable, provider-neutral, documentation-first operating rules and templates that let people and AI agents deliver software and agent systems safely and continue from GitHub without conversation history.

## Initial development plan

- Phase 0 — Verify the canonical workflow, project memory, migration requirements, and validation evidence.
- Phase 1 — Operate OpenCode as the primary platform with model changes inside the same project.
- Phase 2 — Preserve only useful legacy compatibility files and keep the repository memory protocol platform-independent.

## Now

- [ ] **TODO-004 — Publish OpenCode-first operating guidance**
  - Priority: Highest
  - Outcome: Current instructions no longer require switching platforms; OpenCode and model continuity are explicit.
  - Verification: documentation, secret, handoff, JSON, and regression checks.

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
- **TODO-004 — Publish OpenCode-first operating guidance** — Documentation and validation updates completed; publication pending.

## Maintenance rules

- Use stable `TODO-NNN` IDs and observable outcomes.
- Record discovered work in `Next` or `Later` without silently expanding the active item.
- Keep current state short and update it before every substantive session ends.
