# Codex Migration History

This is a concise, sanitized record of durable decisions relevant to moving between Codex, Claude Code, OpenCode, and future agents. It is not a transcript.

## Recovered decisions

- GitHub is the permanent source of truth; agents manage temporary checkouts and the user should not have to clone or organize local folders.
- `moving.md` is the short universal entry point. `HANDOFF.md`, `docs/CURRENT_STATE.md`, and `TODO.md` provide progressive operational memory, with GitHub retaining detailed history.
- A project that already uses the architect continues from documented state. An unmanaged existing project is inspected first and only adopted after the user approves preserving what works.
- The architect is autonomous and protective: it continues safe work, never remains silent or idle, and ends only with a finished result and evidence or one exact human-blocking question.
- Session close requires updating the backlog and current state, verifying, and publishing normal authorized changes.
- Dashboard UI defaults to official Material UI components when applicable; another library requires a clear technical advantage and justification.

## Constraints and rejected approaches

- Do not copy full conversations, secrets, credentials, or private data into the repository.
- Do not replace existing useful agent instructions or configurations merely to switch vendors.
- Do not load every playbook at startup; use progressive disclosure to protect context and tokens.
- Do not change functional application code, dependencies, or deployment as part of this migration preparation.

## Not recoverable from repository evidence

No prior Codex session database or private conversation archive is available in this checkout. The record above contains only decisions already represented in repository history and the approved migration request.

## OpenCode migration

OpenCode is configured through `opencode.json` using its official schema and a remote `instructions` entry for the public `ARCHITECT_BOOTSTRAP.md`. This avoids duplicating large playbooks and keeps the canonical method updateable from GitHub.
