# Repository creation

## Before creating

1. Search for existing exact name.
2. Search semantic variants.
3. Avoid duplicates.

## Minimum facts

Need:
- owner
- repository name
- visibility
- one-line purpose

Never guess visibility.

## Create

If GitHub tools support repository creation:
- create
- verify existence
- use main/default branch policy
- no secrets
- no deployment

If unavailable:
- report BLOCKED
- give exact minimum human action

## Bootstrap

New 10minuteswebsite project should start with:
- README.md
- AGENTS.md
- moving.md
- TODO.md
- HANDOFF.md
- docs/PROJECT_CONTEXT.md
- docs/CURRENT_STATE.md
- .github/pull_request_template.md
- CLAUDE.md when applicable
- opencode.json when applicable
- agent-handoff-check when the canonical standard requires it

Read current AI-Playbooks standard before generating these.

## Initial commit

Empty repo may need a bootstrap commit before normal PR flow.
After that, normal flow is mandatory:
branch -> test -> handoff -> commit -> push -> verify -> PR -> human merge.

## Complete only when

- repo actually exists
- remote identity known
- durable bootstrap exists
- remote commit exists
- next step documented
- no secrets
- no unauthorized deploy
