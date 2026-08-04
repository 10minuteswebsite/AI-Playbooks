<!-- ai-playbooks-handoff:v1 -->
# Universal Agent Handoff

This contract applies to Codex, Claude, and any other agent working in this repository.

## Source-of-truth hierarchy

1. The user's current explicit request.
2. Repository-local instructions and `docs/AI_WORKFLOW.md`.
3. `docs/PROJECT_CONTEXT.md` for durable product and technical facts.
4. `docs/CURRENT_STATE.md` for short-lived operational state.
5. Git and GitHub for detailed history, diffs, reviews, checks, and publication evidence.

Conversation history is optional context and must never be required for continuation.

## Continuity rules

- Read progressively: begin with `moving.md` and `docs/CURRENT_STATE.md`, then open only the files needed for the next exact step.
- Preserve working behavior, user changes, configuration, decisions, and scope unless the current task authorizes a change.
- Separate verified facts, assumptions, decisions, blockers, and unperformed checks.
- Do not copy conversations, full diffs, large code blocks, or Git-recoverable history into handoff documents.
- Complete and verify one focused increment at a time. Record material decisions in ADRs instead of hiding them in chat.
- Use repository-native commands and policies. Never assume a tool, model, vendor, or agent-specific feature is available.

## Mandatory session close

Before ending every substantive work session:

1. leave the repository in a stable state when possible;
2. run verification proportional to the change;
3. review the final diff and preserve unrelated work;
4. update `docs/CURRENT_STATE.md` with completed work, active work, decisions, blockers, verification results, important files, and one next exact safe step;
5. commit and publish verified work according to `docs/AI_WORKFLOW.md`, or record the exact publication blocker;
6. ensure the next agent can continue without the previous conversation.

Never mark a check as passed unless it actually ran. Never mark the session complete while `CURRENT_STATE.md` is stale.
