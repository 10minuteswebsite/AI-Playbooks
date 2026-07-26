# API Service Profile

**Status:** Stable
**Version:** 1.0.0

Use with the Software Delivery Core for HTTP APIs, webhooks, events, and internal service contracts.

## Required decisions

- consumers, ownership, authentication, authorization, tenancy, and data classification;
- schema and semantic versioning, compatibility, deprecation, pagination, and rate limits;
- idempotency, retries, timeouts, ordering, concurrency, and partial failures;
- error taxonomy, observability, service objectives, and recovery;
- provider adapter and replacement boundaries.

## Minimum verification

- schema and contract tests;
- authorization and scope-isolation tests;
- duplicate, retry, timeout, malformed input, and concurrency tests;
- compatibility checks for existing consumers;
- load and failure tests when capacity or availability is material.
