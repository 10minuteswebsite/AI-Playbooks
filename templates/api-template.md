# Contract: <API or Event Name>

**Status:** Draft | Active | Deprecated
**Owner:** <domain/team>
**Version:** <semantic or schema version>
**Type:** HTTP API | Webhook | Event | Internal port

## Purpose and boundary

State the business capability exposed, caller/producer, consumer, and what is explicitly excluded.

## Security and scope

- Authentication:
- Authorization:
- Organization/tenant scope:
- User/resource/purpose scope:
- Sensitive fields and redaction:

## Request or event envelope

```json
{
  "id": "<unique-id>",
  "type": "<domain.action>",
  "version": "1",
  "occurred_at": "<RFC-3339 timestamp>",
  "organization_id": "<scope>",
  "correlation_id": "<trace>",
  "idempotency_key": "<stable-key>",
  "data": {}
}
```

Replace this example with the actual schema. Do not use real personal data.

## Fields

| Field | Type | Required | Validation | Description |
|---|---|---|---|---|
| | | | | |

## Success response or consumer outcome

Define status, schema, persisted/emitted effects, and observable result.

## Errors

| Code/type | Meaning | Retryable | Caller action |
|---|---|---|---|
| | | | |

## Delivery semantics

- Idempotency behavior and retention window:
- Duplicate handling:
- Ordering assumptions:
- Timeout and retry policy:
- Partial-failure behavior:
- Concurrency rules:

## Compatibility

Document additive-change rules, breaking-change process, deprecation period, and migration path.

## Examples and tests

Provide synthetic examples plus contract, isolation, duplicate, and failure tests.
