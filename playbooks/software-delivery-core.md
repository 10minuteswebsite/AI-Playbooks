# Software Delivery Core Playbook

**Status:** Stable
**Version:** 2.6.0
**Audience:** People and AI systems delivering software

## Mission

Turn a validated user or business need into secure, maintainable software through small, reversible, independently verifiable changes. This core applies to every project. Select one or more profiles for project-specific guidance.

## Non-negotiable principles

1. Define the user, problem, outcome, constraints, risks, and acceptance criteria before implementation.
2. Separate verified facts, assumptions, decisions, and open questions. Never invent missing project facts.
3. Prefer the simplest reversible design that meets current evidence. Avoid speculative scale and abstraction.
4. Organize by domain and responsibility. Keep provider-specific details behind explicit contracts and adapters.
5. Keep modules, files, and functions cohesive. Split responsibilities that cannot be explained, reviewed, and tested independently.
6. Deliver one small vertical increment at a time, from user input to an observable result.
7. Treat generated code as untrusted until it has been reviewed and verified.
8. Protect secrets and personal data; use least privilege and synthetic test data.
9. Preserve working behavior unless a documented reason and regression evidence justify a change.
10. Keep the repository as the source of truth for scope, decisions, implementation, tests, releases, and operations.

## Select a profile

Choose profiles by product shape and risk, not by preferred vendor:

- [Web application](profiles/web-application.md)
- [API service](profiles/api-service.md)
- [Mobile application](profiles/mobile-application.md)
- [Data and automation](profiles/data-and-automation.md)
- [AI-enabled application](profiles/ai-enabled-application.md)
- [Agentic AI system](profiles/agentic-ai-system.md)
- [Omnichannel agent](profiles/omnichannel-agent.md)

Use multiple profiles when boundaries overlap. Record why each profile applies in the project brief.

## Delivery loop

### 0. Recover project state

When a managed project exists, begin with `moving.md`, then read `HANDOFF.md`, `docs/CURRENT_STATE.md`, the active and blocked portions of `TODO.md`, Git status, and only the recent history relevant to the next documented step. Load durable context, work items, architecture, decisions, code, and tests progressively as the step requires. Treat the repository as operational memory; never require the previous conversation to continue.

When project files are not present, identify the GitHub repository from available context and verify access through a connector/API or Git. Ask only for the repository link or authorization when necessary. Use a temporary checkout managed by the AI and keep GitHub as the durable source of truth; do not require the user to manage a local workspace.

When the user invokes the architect, detect whether the project is new, managed by AI-Playbooks, or an existing unmanaged project. Initialize a new project, continue a managed project, or ask permission before adopting an unmanaged project. Preserve existing files and behavior during adoption.

### 1. Frame

For a new or undefined project, use the [Finite Project Discovery Playbook](finite-project-discovery.md). Complete the project brief and risk assessment. Identify the smallest useful outcome, exclusions, dependencies, unknowns, and working configuration to preserve. Ask only one user question per interaction and end discovery when the sufficiency test passes.

### 2. Design proportionally

Create only the documentation justified by risk. Define domain boundaries, data ownership, contracts, security, failure behavior, observability, deployment, and rollback. Record an ADR for choices with long-lived consequences, meaningful alternatives, migration cost, security impact, or vendor lock-in.

### 3. Plan a vertical increment

Maintain the initial development plan and known backlog in `TODO.md`. Give actionable items stable `TODO-NNN` identifiers and observable outcomes. Record newly discovered work without silently expanding the active scope. Select one `Now` item, then create a work item that can normally be implemented and reviewed in one day and released independently. Include acceptance criteria, verification, affected boundaries, risk, and rollback. Split work that mixes unrelated outcomes.

### 4. Implement safely

Inspect before editing. Change only the approved scope. Maintain compatibility unless the work item explicitly authorizes a breaking change. Add or update documentation and tests in the same change.

### 5. Verify by risk

Run the applicable quality gates from the testing and secure-development standards. Review the final diff. Report commands or checks actually run, their results, and any residual risk. Never claim a check that was not executed.

### 6. Review and publish

Use a focused branch and pull request. Require human approval before production deployment, external communication, spending, deletion, access expansion, or another sensitive or irreversible action unless a documented policy explicitly delegates it.

### 7. Operate and learn

Observe user outcomes, reliability, security, cost, and regressions. Record incidents and feedback. Convert failures into tests, guardrails, documentation, or design improvements.

## Autonomy boundaries for AI

AI may research, draft, implement, test, explain, and propose within the approved scope. AI must stop for a missing business decision, unavailable credential, acceptance of material risk, use of real sensitive data, production release, or sensitive/irreversible external action unless the project policy explicitly authorizes it.

Do not stop at a plan, status update, partial result, or routine technical question while safe in-scope work remains. Continue autonomously until the outcome is complete or one exact human decision blocks progress. Do not offload ordinary technical tasks to the user.

## Completion criteria

Work is complete only when the observable outcome and acceptance criteria are met, relevant checks pass, documentation matches reality, security and data boundaries remain intact, rollback is understood, and another person can reproduce the result from the repository.

Before ending every substantive work session, update `TODO.md` with discovered, reprioritized, blocked, or recently completed work and update the short operational state with the active backlog item, completed work, pending work, decisions, important files, verification, risks, blockers, and one next exact step. Do not copy conversations, large code blocks, full diffs, or facts obtainable from Git into the handoff. Never leave the backlog or state stale after a later material change.
