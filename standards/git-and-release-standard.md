# Git and Release Standard

**Status:** Stable
**Version:** 1.1.0

## Objective

Make every change focused, reviewable, traceable, reversible, and reproducible.

## Change workflow

- start from the current default branch on a focused branch;
- do not mix unrelated user work;
- use small commits with intent-revealing messages;
- open a pull request describing outcome, decisions, verification, risk, and rollback;
- require passing checks and proportional human review before merge;
- do not rewrite shared history without explicit coordination.

For projects using the shared AI workflow, agents automatically commit completed verified work, push it to an authenticated GitHub remote, and open or update a pull request. They may merge automatically only when the change is normal, reversible, all checks pass, and no conflict or unresolved review remains.

Human approval is required before merging changes involving security boundaries, sensitive/personal data, payments, production infrastructure or deployment, destructive operations, meaningful cost, access expansion, acceptance of material risk, or another sensitive/irreversible effect.

## Release workflow

- use semantic versions for stable public artifacts;
- maintain a changelog with added, changed, deprecated, removed, fixed, and security sections as applicable;
- identify compatibility and migration requirements;
- tag and publish from reviewed source;
- record artifact, configuration, database, model, prompt, and dependency versions needed to reproduce behavior;
- use staged rollout and a tested rollback path for production systems.

## Emergency changes

Emergency work may shorten but must not eliminate review, verification, traceability, or post-incident follow-up. Record the exception and complete missing evidence immediately after containment.
