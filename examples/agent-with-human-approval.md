# Example: Agent With Human Approval

## Outcome

An agent researches synthetic account context and drafts an update, but a person must approve before the external record changes.

## Applied guidance

- Software Delivery Core
- AI-Enabled Application and Agentic AI System profiles
- AI Agent Designer, QA, Security, and Backend roles

## Boundaries and decisions

- One read-only search tool and one reversible write tool are exposed through typed contracts.
- Search results are untrusted data and cannot redefine system instructions.
- The write tool requires organization scope, proposed change, reason, idempotency key, and approval token.
- The agent cannot create its own approval token or expand its permissions.
- Step, retry, time, token, and cost budgets stop runaway execution.

## First work item

Return a cited draft and approval request for one synthetic workflow. Exclude automatic execution, bulk changes, and sensitive data.

## Required evidence

- evaluation cases for success, insufficient evidence, refusal, prompt injection, wrong scope, stale data, and tool failure;
- contract tests proving writes fail without valid approval;
- duplicate and retry tests;
- trace review with secrets and personal data redacted;
- kill-switch, rollback, latency, and cost evidence.
