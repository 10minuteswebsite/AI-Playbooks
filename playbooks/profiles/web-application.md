# Web Application Profile

**Status:** Stable
**Version:** 1.0.0

Use with the Software Delivery Core for browser-based products and dashboards.

## Required decisions

- user journeys, supported browsers/devices, accessibility target, localization, and offline expectations;
- rendering and caching strategy;
- authentication, session, authorization, and sensitive-data behavior in the browser;
- API boundaries, state ownership, loading/empty/error states, and analytics privacy;
- performance budgets and deployment/rollback strategy.

## UI preference

For web dashboards, use [Material UI (MUI)](https://mui.com/material-ui/all-components/) by default. Prefer official MUI components for tables, forms, navigation, layouts, charts when applicable, and visual consistency. Use another library only for a clear project-specific technical advantage recorded with its tradeoffs and replacement impact.

## Minimum verification

- component and journey tests for critical flows;
- authorization tests beyond merely hiding UI elements;
- keyboard navigation, focus, labels, contrast, and responsive behavior;
- loading, empty, validation, error, retry, and expired-session states;
- performance and bundle-size checks proportional to user impact;
- end-to-end smoke test against a production-like environment.
