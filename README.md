# AI Playbooks

Reusable, versioned operating instructions for designing and delivering software and AI systems with people and AI working together.

## Purpose

This repository is the source of truth for delivery workflow, project profiles, engineering roles, architectural decisions, standards, and templates. It favors plain language, explicit tradeoffs, small verifiable increments, secure data handling, replaceable integrations, and human control over material risk.

## Repository map

```text
GETTING_STARTED.md            Guided workflow for non-programmers
REFERENCES.md                 Standards and research baselines
playbooks/
  software-delivery-core.md   Universal delivery workflow
  software-architect.md       Architecture role
  finite-project-discovery.md Finite, adaptive new-project interview
  profiles/                   Project-type guidance
  roles/                      Responsibility-specific guidance
skills/
  omnichannel-agent-architect/ Candidate shared Architect skill (PR #15)
templates/
  ...                         Planning, architecture, risk, AI, release, and operations
  project/                    OpenCode project structure and compatibility files
  global/                     Copyable account-wide AI instructions
standards/
  ...                         Documentation, testing, security, AI, operations, and release
examples/                     Worked delivery examples
```

## How to use

For normal use in OpenCode, tell the architect: **“Usa el arquitecto.”** The architect detects whether the project is new, already managed, or requires approved adoption. Select or change models inside OpenCode as needed; do not restart the methodology or copy context between platforms.

If the AI does not already know the architect, give it the public bootstrap once:

> Lee y sigue https://raw.githubusercontent.com/10minuteswebsite/AI-Playbooks/main/ARCHITECT_BOOTSTRAP.md. Usa el arquitecto.

The architect works GitHub-first. It identifies or requests the repository, verifies access, asks for GitHub authorization when necessary, and manages any temporary checkout itself. The user does not need to clone repositories or organize local project folders.

The [Agent Interoperability Standard v1](docs/standards/agent-interoperability-v1.md) defines durable session bootstrap, handoff, commit/push/PR evidence, `BLOCKED` behavior, and human-only merge/deploy boundaries for Codex, OpenCode, Claude Code, and future agents.

PR #15 proposes [`skills/omnichannel-agent-architect/`](skills/omnichannel-agent-architect/) as the single shared Arquitecto Omnicanal skill source. It becomes canonical only after a human-approved merge. Codex, Claude Code, and OpenCode installations will then use that same version; product-local copies remain operational installations, not independent sources of truth.

Every newly bootstrapped project includes a compact OpenCode entry point. When starting a new OpenCode session, say:

> Entra al repositorio [REPOSITORIO], lee moving.md y sigue las instrucciones.

`moving.md` routes OpenCode to the stable `HANDOFF.md` contract, short `docs/CURRENT_STATE.md`, and repository-native `TODO.md`. `TODO.md` holds the initial plan and complete known backlog; current state identifies only the active item and next exact step. OpenCode then reads only the work item, decisions, architecture, code, and tests required for that step; GitHub retains the detailed, verifiable history.

The reusable installer is:

```sh
python3 scripts/bootstrap_project.py "/path/to/project"
```

For an existing unmanaged project, the first run makes no changes and requests approval. After approval, the agent runs it with `--adopt`. Existing files are preserved and conflicts are written as reviewable proposals.

Then the architect:

1. Applies the [Software Delivery Core](playbooks/software-delivery-core.md).
2. Uses [Finite Project Discovery](playbooks/finite-project-discovery.md) when a new idea needs definition.
3. Selects the relevant [project profiles](playbooks/profiles/).
4. Reads stable context and current operational state.
5. Delivers and verifies one small vertical increment at a time.
6. Updates the repository state so a later OpenCode session or model can continue without chat history.

Example invocation:

> Usa el arquitecto.

## Status labels

- **Stable**: approved for regular use.
- **Draft**: usable for evaluation but incomplete.
- **Placeholder**: scope only; expand before operational use.
- **Deprecated**: retained for history and must not be used for new work.

## Maintenance

- Make focused changes with a clear reason.
- Record consequential choices with an Architecture Decision Record (ADR).
- Preserve working behavior unless evidence justifies a change.
- Review stable playbooks after major incidents, platform changes, or at least every six months.
- Never commit secrets, real personal data, or sensitive customer content.

## Current release

- Software Delivery Core and Software Architect: **Stable**
- Project profiles and role playbooks: **Stable**
- Standards and templates: **Stable**
- Worked examples: **Reference**

## Verification

Run:

```sh
python3 scripts/validate_docs.py
python3 scripts/scan_secrets.py
python3 scripts/test_project_handoff.py
python3 scripts/test_github_first_architect.py
python3 scripts/test_finite_project_discovery.py
python3 scripts/test_omnichannel_architect_skill.py
python3 scripts/validate_global_instructions.py
```

The global-instruction check is local-only because CI does not have access to a user's home-directory configuration.

`templates/github-actions/documentation-quality.yml` is ready to copy into `.github/workflows/` to run both checks automatically after the publishing account is authorized with GitHub's `workflow` scope.
