# Secure Development Standard

**Status:** Stable
**Version:** 1.0.0

## Objective

Integrate risk-based security throughout planning, development, delivery, operation, and vulnerability response. Apply the outcomes of NIST SSDF and tailor implementation to context.

## Prepare

- assign owners for code, data, services, security decisions, and incident response;
- classify data and system risk before implementation;
- separate development, test, and production environments;
- use managed identity, least privilege, short-lived credentials, and approved secret storage;
- define security requirements and threat-model medium/high-risk changes.

## Protect

- require version control, focused review, and protected publication paths;
- prevent secrets and real personal data from entering source, prompts, fixtures, logs, or generated artifacts;
- restrict AI tools to approved repositories, paths, commands, data, and external actions;
- protect build configuration and release artifacts from unauthorized modification;
- preserve provenance for released artifacts proportional to risk.

## Produce

- validate at every trust boundary and use safe defaults;
- authenticate identity and authorize each action server-side;
- isolate tenant/user data in storage, retrieval, caches, logs, and AI memory;
- use established cryptography and secure libraries rather than custom security mechanisms;
- scan code, dependencies, containers, infrastructure, and secrets as applicable;
- verify failure behavior does not expose sensitive data or bypass controls.

## Respond

- provide a private vulnerability-reporting path;
- triage by exploitability, exposure, and user impact;
- contain, remediate, verify, communicate, and document material vulnerabilities;
- rotate exposed credentials and identify affected artifacts and data;
- add regression tests and update the threat model after an incident.

## Human control

Require explicit approval for production access, privilege expansion, sensitive data use, disabling controls, destructive migrations, security exceptions, and acceptance of material residual risk.
