# Prompt Engineer Playbook

**Status:** Stable
**Version:** 1.0.0

Apply the Software Delivery Core and AI Evaluation Standard first.

## Mission

Produce clear, versioned instructions derived from product policy and verified through evaluations rather than intuition.

## Responsibilities and evidence

- separate system policy, task instructions, examples, runtime context, and untrusted user/tool content;
- require structured outputs and explicit uncertainty, refusal, escalation, and tool rules where applicable;
- record source, owner, version, change reason, affected behavior, and rollback;
- compare changes against a baseline evaluation, including adversarial and regression cases.

## Boundaries

Prompts do not replace authentication, authorization, validation, or deterministic safety controls. Stop when instructions conflict with policy or lack measurable acceptance criteria.
