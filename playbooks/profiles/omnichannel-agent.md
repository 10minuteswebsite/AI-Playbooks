# Omnichannel Agent Profile

**Status:** Stable
**Version:** 1.0.0

Apply after the AI-Enabled Application and Agentic AI System profiles for assistants spanning voice, messaging, web chat, or future channels.

## Canonical behavior

- Treat Agent DNA as the source of truth for identity, policies, knowledge boundaries, tools, and escalation.
- Treat prompts as derived, versioned artifacts traceable to an Agent DNA version.
- Model channels as interfaces to one intelligence with shared, explicitly scoped memory, not separate agents with diverging truth.

## Boundaries

- Isolate information by organization, user/lead, conversation, purpose, and authorization scope.
- Put channel, telephony, messaging, scheduling, CRM, and storage providers behind contracts and adapters.
- Normalize channel events before they reach domain logic; keep provider errors and identifiers at integration boundaries.
- Define identity resolution and consent before linking activity across channels.

## Reliability and verification

- make inbound events, messages, bookings, transfers, and retries idempotent;
- test duplicates, out-of-order events, delayed delivery, interruptions, handoffs, and provider failure;
- evaluate consistent policy and memory behavior across every supported channel;
- preserve channel-specific accessibility, latency, consent, and escalation requirements.
