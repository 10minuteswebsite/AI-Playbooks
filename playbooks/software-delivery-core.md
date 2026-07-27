# Software Delivery Core Playbook

**Status:** Stable
**Version:** 2.1.0
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

When project adapters exist, read `AGENTS.md` or `CLAUDE.md`, then the shared workflow, `docs/PROJECT_CONTEXT.md`, `docs/CURRENT_STATE.md`, Git status, and only the recent history relevant to the next documented step. Treat the repository as operational memory; never require the previous conversation to continue.

When the user invokes the architect, detect whether the project is new, managed by AI-Playbooks, or an existing unmanaged project. Initialize a new project, continue a managed project, or ask permission before adopting an unmanaged project. Preserve existing files and behavior during adoption.

### 1. Frame

Complete the project brief and risk assessment. Identify the smallest useful outcome, exclusions, dependencies, unknowns, and working configuration to preserve.

### 2. Design proportionally

Create only the documentation justified by risk. Define domain boundaries, data ownership, contracts, security, failure behavior, observability, deployment, and rollback. Record an ADR for choices with long-lived consequences, meaningful alternatives, migration cost, security impact, or vendor lock-in.

### 3. Plan a vertical increment

Create a work item that can normally be implemented and reviewed in one day and released independently. Include acceptance criteria, verification, affected boundaries, risk, and rollback. Split work that mixes unrelated outcomes.

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

## Completion criteria

Work is complete only when the observable outcome and acceptance criteria are met, relevant checks pass, documentation matches reality, security and data boundaries remain intact, rollback is understood, and another person can reproduce the result from the repository.

Before ending a work session, update the short operational state with completed work, pending work, important files, verification, risks, blockers, and one next exact step. Do not copy conversations, large code blocks, full diffs, or facts obtainable from Git into the handoff.
