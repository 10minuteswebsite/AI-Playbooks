# AI Evaluation Standard

**Status:** Stable
**Version:** 1.0.0

## Objective

Measure whether an AI feature or agent is useful, safe, reliable, and economical before and after release.

## Evaluation contract

Define:

- user task and success/failure criteria;
- critical segments, languages, channels, and edge cases;
- deterministic baseline where possible;
- quality, safety, latency, and cost metrics;
- acceptance thresholds and who may approve exceptions;
- model, instruction, tool, retrieval, memory, and dataset versions.

## Dataset

Use representative, boundary, adversarial, refusal, escalation, and recovery cases. Prefer synthetic data; use production-derived examples only with authorization, minimization, de-identification, access controls, and retention rules. Keep test data separate from training and optimization data when unbiased measurement matters.

## Grading

Combine deterministic assertions, schema validation, domain rules, model-based graders, and calibrated human review. Validate automated graders against human judgment before relying on them for material decisions.

## Release gate

Run the full relevant suite whenever the model, instructions, tools, schemas, retrieval, memory, guardrails, or orchestration changes. Compare with the accepted baseline. Block release on critical safety failures or missed minimum thresholds unless an authorized owner records the risk and mitigation.

## Production loop

Monitor quality signals, user corrections, escalations, policy violations, latency, cost, and drift. Convert confirmed failures into versioned regression cases without storing unnecessary sensitive data.
