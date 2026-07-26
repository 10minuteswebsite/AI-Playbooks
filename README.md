# AI Playbooks

Reusable, versioned operating instructions for designing and delivering software and AI systems with people and AI working together.

## Purpose

This repository is the source of truth for delivery workflow, project profiles, engineering roles, architectural decisions, standards, and templates. It favors plain language, explicit tradeoffs, small verifiable increments, secure data handling, replaceable integrations, and human control over material risk.

## Repository map

```text
GETTING_STARTED.md            Guided workflow for non-programmers
REFERENCES.md                 Standards and research baselines
playbooks/
  software-delivery-core.md   Universal delivery workflow
  software-architect.md       Architecture role
  profiles/                   Project-type guidance
  roles/                      Responsibility-specific guidance
templates/
  ...                         Planning, architecture, risk, AI, release, and operations
standards/
  ...                         Documentation, testing, security, AI, operations, and release
examples/                     Worked delivery examples
```

## How to use

1. Start with [Getting Started](GETTING_STARTED.md).
2. Apply the [Software Delivery Core](playbooks/software-delivery-core.md).
3. Select one or more [project profiles](playbooks/profiles/).
4. Complete the project brief and risk assessment before implementation.
5. Deliver and verify one small vertical increment at a time.
6. Use role playbooks when a responsibility needs deeper guidance.
7. Commit documentation, decisions, implementation, tests, and evidence together.

Example invocation:

> Apply `playbooks/software-delivery-core.md`, select the relevant profiles, and guide me in plain language. Work in one small vertical increment, distinguish facts from assumptions, run the required checks, and stop for material risk or irreversible actions.

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
- Never commit secrets, real personal data, or sensitive customer content.

## Current release

- Software Delivery Core and Software Architect: **Stable**
- Project profiles and role playbooks: **Stable**
- Standards and templates: **Stable**
- Worked examples: **Reference**

## Verification

Run:

```sh
python3 scripts/validate_docs.py
python3 scripts/scan_secrets.py
```

`templates/github-actions/documentation-quality.yml` is ready to copy into `.github/workflows/` to run both checks automatically after the publishing account is authorized with GitHub's `workflow` scope.
