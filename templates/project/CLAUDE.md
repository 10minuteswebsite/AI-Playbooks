<!-- ai-playbooks-adapter:v1 -->
# Claude Code Project Instructions

`docs/AI_WORKFLOW.md` is the shared source of truth for how Claude and Codex work in this project. Follow it before doing substantive work.

At the start of every task:

1. Read `docs/AI_WORKFLOW.md`.
2. Read `docs/PROJECT_CONTEXT.md`.
3. Read `docs/CURRENT_STATE.md`.
4. Inspect `git status` and relevant recent commits.
5. Continue from the documented next exact step when it matches the user's request.

Load only the files needed for the current task. Do not depend on conversation history for project state and do not duplicate the shared workflow in this file.
