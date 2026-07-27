## Outcome

<!-- What does this change make possible or improve? -->

## Changes

<!-- List the focused changes. -->

## Decision and tradeoffs

<!-- Explain material choices; link an ADR when required. -->

## Verification

<!-- State the checks actually performed and their results. -->

## Risk and rollback

<!-- Note remaining risk and how to reverse the change. -->

## Checklist

- [ ] Documentation matches the intended behavior.
- [ ] Status and version labels are accurate.
- [ ] No secrets, personal data, or real customer content are included.
- [ ] Domain boundaries do not depend unnecessarily on a provider.
- [ ] Relevant links, examples, and templates were checked.
- [ ] `python3 scripts/validate_docs.py` passes.
- [ ] `python3 scripts/scan_secrets.py` passes.
- [ ] `python3 scripts/test_project_handoff.py` passes when project workflow behavior changed.
- [ ] Applicable profiles, quality gates, security checks, and human approvals were considered.
- [ ] AI evaluation and tool-permission evidence is included when AI behavior changed.
- [ ] Any material decision has an ADR or an explanation of why one is unnecessary.
