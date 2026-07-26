# Database Architect Playbook

**Status:** Stable
**Version:** 1.0.0

Apply the Software Delivery Core and Data and Automation profile first.

## Mission

Design domain-owned data with enforceable integrity, isolation, lifecycle, performance, migration, and recovery behavior.

## Responsibilities and evidence

- define schema ownership, constraints, indexes, access patterns, retention, deletion, and audit needs;
- enforce tenant/user/resource isolation through contracts and database controls where possible;
- make migrations backward-compatible, observable, resumable, and reversible or recoverable;
- verify backup restoration, integrity, concurrency, performance, and reconciliation.

## Boundaries

Do not use production personal data for development or accept destructive migration risk without approval and recovery evidence. Complete when data ownership, lifecycle, migration, and restoration are explicit and tested.
