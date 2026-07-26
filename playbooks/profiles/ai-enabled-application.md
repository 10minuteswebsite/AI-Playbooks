# AI-Enabled Application Profile

**Status:** Stable
**Version:** 1.0.0

Use when AI generates, classifies, extracts, recommends, searches, or summarizes but does not autonomously control a multi-step workflow. Add the Agentic AI profile if models select tools or actions.

## Required decisions

- why AI is appropriate and what deterministic baseline exists;
- model/provider boundary and replacement path;
- input/output schemas, uncertainty handling, citations, and fallback behavior;
- permitted data, retention, residency, and model-training policies;
- quality, safety, latency, and cost targets;
- versioning and rollback for model, instructions, datasets, and retrieval configuration.

## Minimum verification

- versioned evaluation dataset with representative and adversarial cases;
- deterministic validation around model input and output;
- comparison with a baseline and explicit acceptance thresholds;
- regression evaluation for every model, prompt, tool, or retrieval change;
- monitoring for quality, safety, latency, cost, and drift.
