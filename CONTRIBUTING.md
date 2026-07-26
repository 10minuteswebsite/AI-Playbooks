# Contributing

## Change process

1. Open an issue or describe the objective and affected playbook.
2. Create a focused branch from `main`.
3. Update the playbook, related templates, and documentation together.
4. Add an ADR when the change is consequential or difficult to reverse.
5. Verify links, examples, status labels, sensitive-data safety, and consistency with repository principles.
6. Run `python3 scripts/validate_docs.py` and `python3 scripts/scan_secrets.py`.
7. Open a pull request using the repository template.
8. Merge only after review and all material questions are resolved.

## Versioning

Stable playbooks use semantic versions:

- **Patch:** clarification with no intended behavioral change.
- **Minor:** backward-compatible capability or guidance.
- **Major:** changed responsibility, workflow, safety boundary, or incompatible instruction.

Placeholder playbooks begin versioning when promoted to Draft. Record the promotion and rationale in the pull request.

## Review checklist

- The business or operational reason is clear.
- Facts, assumptions, decisions, and open questions are distinguishable.
- Vendor details remain behind domain-oriented boundaries.
- Selected profiles and their project-specific requirements remain consistent.
- Agent DNA, prompt traceability, shared memory, evaluations, tool permissions, and scope isolation remain consistent where applicable.
- No secrets, personal data, or real customer content appear in the change.
- Instructions are testable and do not claim unperformed verification.
- Status and version metadata are accurate.
