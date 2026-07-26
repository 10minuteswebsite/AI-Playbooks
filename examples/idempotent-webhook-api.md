# Example: Idempotent Webhook API Increment

## Outcome

A synthetic payment-provider event creates one domain record even when the provider retries the same event.

## Applied guidance

- Software Delivery Core
- API Service profile
- Backend, Database, QA, Security, and DevOps roles

## Boundaries and decisions

- A provider adapter verifies authenticity and converts the payload into a domain command.
- A unique provider event ID is stored with the domain effect in one transaction.
- Duplicate delivery returns the documented successful outcome without repeating the effect.
- Provider fields and errors remain outside the domain contract.

## First work item

Handle one event type with verified signature, schema validation, idempotent persistence, structured audit metadata, and safe retry behavior. Exclude refunds and outbound notifications.

## Required evidence

- valid, invalid-signature, malformed, duplicate, concurrent duplicate, and database-failure tests;
- contract compatibility and tenant-scope tests;
- redacted logs correlated by event ID;
- replay demonstration and rollback/recovery procedure.
