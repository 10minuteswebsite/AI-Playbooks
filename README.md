# AI Playbooks

Reusable, versioned operating instructions for designing and delivering software and AI systems.

## Purpose

This repository is the source of truth for engineering roles, architectural decisions, and documentation templates. It favors documentation-first delivery, explicit tradeoffs, small verifiable increments, secure data handling, and replaceable integrations.

## Repository map

```text
playbooks/
  software-architect.md       Production-ready primary playbook
  roles/                      Draft role playbooks for future expansion
templates/
  architecture-template.md   Solution design
  api-template.md            API or event contract
  decision-record-template.md
  module-template.md          Module-level documentation
standards/
  documentation-standard.md
```

## How to use

1. Link or copy the relevant playbook into the AI tool or project instructions.
2. Provide the business objective, users, constraints, existing system, and desired outcome.
3. Ask the assistant to complete the relevant template before implementation.
4. Review material assumptions and decisions.
5. Implement and verify one small vertical increment at a time.
6. Commit documentation, decisions, code, and verification evidence together.

Example invocation:

> Use `playbooks/software-architect.md`. Design this project documentation-first, record material decisions, and do not implement until the architecture and acceptance criteria are clear.

## Status labels

- **Stable**: approved for regular use.
- **Draft**: usable for evaluation but incomplete.
- **Placeholder**: scope only; expand before operational use.
- **Deprecated**: retained for history and must not be used for new work.

## Maintenance

- Make focused changes with a clear reason.
- Record consequential choices with an Architecture Decision Record (ADR).
- Preserve working behavior unless evidence justifies a change.
- Review stable playbooks after major incidents, platform changes, or at least every six months.
- Never commit secrets, real personal data, or customer conversation content.

## Current release

- `software-architect.md`: **Stable**
- Foundational templates and documentation standard: **Stable**
- Additional role playbooks: **Placeholder**
