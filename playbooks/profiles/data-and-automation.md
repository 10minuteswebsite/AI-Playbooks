# Data and Automation Profile

**Status:** Stable
**Version:** 1.0.0

Use with the Software Delivery Core for data pipelines, scheduled jobs, reporting, and business automation.

## Required decisions

- source ownership, schema, quality expectations, lineage, retention, and permitted use;
- scheduling, triggers, checkpoints, idempotency, late data, and replay;
- destination contracts and reconciliation;
- failure isolation, alerting, manual recovery, and backfill;
- cost, capacity, privacy, and access boundaries.

## Minimum verification

- schema, transformation, and data-quality tests;
- empty, duplicate, late, corrupt, and partial inputs;
- safe replay and idempotent output;
- reconciliation totals and traceable provenance;
- recovery from checkpoint without silent loss or duplication.
