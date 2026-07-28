# Getting Started Without a Programming Background

This guide helps a non-programmer direct AI to build software without surrendering control of the outcome, risk, or release.

## The working agreement

AI can do much of the technical work, but generated code is a proposal until verified. You remain responsible for the desired outcome, accepted risk, sensitive data, spending, publication, and irreversible actions.

## The only invocation to remember

Tell Codex or Claude:

> Usa el arquitecto.

If this is a new chat tool or account that has never received the architect instructions, say once:

> Lee y sigue https://raw.githubusercontent.com/10minuteswebsite/AI-Playbooks/main/ARCHITECT_BOOTSTRAP.md. Usa el arquitecto.

You can also copy `templates/global/claude-profile-instructions.md` into Claude's profile instructions so the short phrase works in future chats.

The architect inspects the project automatically:

- a new project receives the shared operating structure;
- an already managed project continues from its documented next step;
- an existing unmanaged project is not changed until the architect asks whether to adopt the structure and receives approval.

You do not need to tell either agent to inspect Git, read memory files, preserve existing configuration, or prepare the next handoff.

You also do not need to work locally. The architect should identify or ask for the GitHub repository, request connection access if needed, and manage its own temporary working copy.

## Before the first line of code

1. The architect installs or verifies the shared project structure.
2. It establishes stable project context in plain language.
3. It classifies risk and selects applicable profiles.
4. For medium- or high-risk work, it prepares the architecture and threat model for review.
5. It proposes the smallest end-to-end result a user can observe.

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
