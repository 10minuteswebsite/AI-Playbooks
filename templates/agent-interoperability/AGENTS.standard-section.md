## Automatic session bootstrap

At the beginning of every new agent session in this repository, before substantive work:

1. Treat GitHub and the current repository state as the durable source of truth.
2. Read `moving.md`, `TODO.md`, and `docs/CURRENT_STATE.md`.
3. Read only relevant contracts, tests, architecture notes, and project documentation.
4. Inspect the current branch and relevant recent commits.
5. Reconstruct state from the repository; never depend on previous chat history.
6. If the human says `continue` or `continúa`, determine the next unblocked step and continue.
7. If the human specifies a new task, use durable project state before implementing.

## Durable handoff and definition of done

GitHub is the only durable source of truth. Before claiming a substantive task complete, run applicable checks, update durable state, commit, push, verify the remote commit, and open a Pull Request. The PR must record changes, tests/results, risks, remaining work, next step, and deployment status. Human approval is required for merge and deployment. If any required step fails, report `BLOCKED` with the exact failure, completed work, remaining work, and minimum human action.
