# Getting Started Without a Programming Background

This guide helps a non-programmer direct AI to build software without surrendering control of the outcome, risk, or release.

## The working agreement

AI can do much of the technical work, but generated code is a proposal until verified. You remain responsible for the desired outcome, accepted risk, sensitive data, spending, publication, and irreversible actions.

## Before the first line of code

1. Copy `templates/project-brief.md` into your project and complete it in plain language.
2. Copy `templates/risk-assessment.md` and classify the project.
3. Ask AI to identify the applicable profiles in `playbooks/software-delivery-core.md` and explain the choice.
4. For medium- or high-risk work, complete the architecture and threat-model templates.
5. Ask AI to propose the smallest end-to-end result a user can observe.

Do not begin implementation while the user, expected result, important exclusions, or acceptance criteria remain unclear.

## The repeatable delivery loop

For every increment:

1. Create one work item from `templates/work-item.md`.
2. Ask AI to inspect the existing project and explain the proposed change in plain language.
3. Approve only the files, systems, data, and external actions in scope.
4. Let AI implement and run the relevant checks.
5. Review the evidence: changed files, tests run, visible result, remaining risk, and rollback.
6. Use a pull request so the change can be reviewed before merging.
7. Deploy gradually, observe the result, and reverse it if acceptance criteria fail.

## Questions to ask AI every time

- What user outcome does this change produce?
- What assumptions are you making?
- Which files, data, permissions, and services will change?
- What could fail or expose data?
- How will you prove it works?
- What did you actually test?
- How can I undo it?
- What remains uncertain?

## Evidence that a task is finished

Accept a task only when AI provides:

- a concise outcome statement;
- the final changed-file list and diff summary;
- passing automated checks appropriate to the risk;
- a demonstration or reproducible verification path;
- confirmation that no secrets or real personal data were added;
- residual risks and unperformed checks;
- a rollback or recovery path.

## Stop and obtain expert review when

- the system handles health, finance, legal decisions, children, biometric data, payments, or safety-critical operations;
- data isolation, authorization, encryption, deletion, compliance, or production recovery is unclear;
- AI requests broad credentials or disables a safety control;
- a migration can lose or corrupt data;
- a release cannot be reversed;
- tests fail or the evidence does not match the claim.

## Learning path

Learn in this order while building small projects:

1. outcomes, scope, and acceptance criteria;
2. files, modules, and data flow;
3. version control and reading diffs;
4. automated tests and failure messages;
5. APIs, databases, authentication, and authorization;
6. deployment, logs, monitoring, and rollback;
7. threat modeling, dependencies, and incident response;
8. AI evaluations, tool permissions, guardrails, and human approval.

The goal is not to memorize syntax. It is to make good decisions, decompose work, inspect evidence, and recover safely.
