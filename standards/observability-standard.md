# Observability and Operations Standard

**Status:** Stable
**Version:** 1.0.0

## Objective

Make user impact, system behavior, failures, and recovery understandable without exposing sensitive data.

## Required signals

- user outcome and business metric;
- availability, latency, traffic, errors, and resource saturation where applicable;
- structured logs with correlation and scope identifiers;
- traces across important boundaries;
- deployment/version markers;
- AI quality, escalation, tool use, cost, and safety signals for AI systems.

## Rules

- define service objectives and alerts around user impact, not only infrastructure;
- redact secrets and minimize personal data at collection time;
- set access, retention, and deletion policy for telemetry;
- make failures actionable with owner, severity, context, and runbook link;
- test dashboards, alerts, rollback, backup restoration, and incident communication before relying on them.

## Release evidence

Every production release identifies the version, owner, expected signals, observation window, rollback trigger, and rollback procedure.
