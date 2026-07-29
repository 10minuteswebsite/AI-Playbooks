# Finite Project Discovery Playbook

**Status:** Stable
**Version:** 1.0.0
**Audience:** People and AI systems starting software projects

## Purpose

Turn a non-technical idea into enough verified project definition for the architect to choose the first safe, useful increment. Discovery must reduce uncertainty without making the user complete a technical questionnaire.

## Conversation contract

- First extract every reliable fact already present in the conversation, repository, connected systems, and existing documentation. Never ask the user to repeat known information.
- Ask at most one concise question per interaction. Prefer a plain-language question that resolves the most consequential unknown.
- Explain briefly that discovery is finite and stop asking as soon as the next useful increment can be framed safely.
- Ask only about business intent, user experience, policy, risk, cost, or external facts that cannot be discovered. The architect decides routine technical details.
- Offer no more than three options when examples would make a decision easier. Recommend one option when evidence supports it.
- Confirm an answer only when doing so fixes an important product rule or corrects an ambiguity. Avoid repetitive acknowledgements and long interim summaries.
- Use the user's language and produce the best current artifact in the current interaction; never promise to prepare it later.

## Adaptive question budget

These are ceilings, not targets:

- **Simple:** normally 3–6 user answers. Examples: a small internal tool, single automation, or narrow prototype.
- **Moderate:** normally 6–10 user answers. Examples: a multiuser application, database-backed dashboard, or limited external integrations.
- **Complex or high-risk:** normally 10–15 user answers. Examples: SaaS, agentic systems, payments, sensitive data, multiple roles, or several operational integrations.

Exceed the ceiling only when a material safety or business decision remains unresolved. Say why one additional answer is necessary.

## Question routing

Resolve the highest-value unknown first and skip everything already known. Common areas are:

1. desired outcome and the problem it solves;
2. primary users and whether use is personal, internal, multiuser, or commercial;
3. observable successful result and principal user journey;
4. essential scope for the first useful version and explicit exclusions;
5. autonomy level and actions that require human approval;
6. external integrations and access dependencies;
7. data read, stored, changed, retained, or deleted;
8. privacy, security, audit, recovery, regulatory, budget, or deadline constraints;
9. reports, dashboards, notifications, memory, or learning behavior when applicable.

Do not ask the user to choose a programming language, framework, database, folder structure, or test strategy unless they have a real constraint or preference. Recommend those choices from evidence and document material tradeoffs.

## Sufficiency test

Discovery is sufficient when the architect can state, without inventing facts:

- who the first user is and what problem is being solved;
- the observable outcome and first vertical increment;
- the essential in-scope and out-of-scope boundaries;
- important data, integrations, permissions, and risks;
- acceptance evidence for the first increment;
- any decision that still requires the user.

Stop the interview when this test passes. Record remaining non-blocking assumptions explicitly and validate them through small, reversible delivery.

## Proportional output

### Project brief

Use [the project brief template](../templates/project-brief.md) for simple or low-risk projects. It is enough to begin when the sufficiency test passes and no consequential architecture decision is unresolved.

### Architecture blueprint

Add [the architecture template](../templates/architecture-template.md) for moderate, complex, or higher-risk projects involving authentication, multiple roles, persistent data, AI behavior, payments, sensitive actions, dashboards, or external integrations. Complete only the sections justified by scope and risk.

Before implementation, the architect must define the relevant architecture, technology choices, data boundaries, user flows, delivery increments, risks, verification, and rollback. Require explicit user approval only for a material business choice, accepted risk, cost, production effect, sensitive access, or irreversible action. Do not impose a universal waterfall gate for routine reversible technical decisions.

## Completion

Discovery is complete when the proportional artifact reflects known facts, separates assumptions and open decisions, identifies the first useful increment and its acceptance evidence, and enables the architect to proceed without another general questionnaire.
