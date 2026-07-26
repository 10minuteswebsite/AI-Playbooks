# Dependency and Supply Chain Standard

**Status:** Stable
**Version:** 1.0.0

## Objective

Know what a release contains, reduce dependency risk, and preserve confidence that reviewed source produced the distributed artifact.

## Dependency policy

- prefer maintained, well-scoped dependencies with compatible licenses and clear ownership;
- use lockfiles and reproducible installation;
- minimize direct and transitive dependency surface;
- review new dependencies for necessity, security, maintenance, license, size, and exit path;
- automate update proposals and vulnerability monitoring;
- remove unused dependencies.

## Build and release

- build in a controlled, repeatable environment;
- restrict workflow permissions and pin sensitive third-party automation appropriately;
- generate an SBOM for distributed or medium/high-risk products;
- retain artifact checksums and provenance proportional to risk;
- verify that the deployed artifact corresponds to the reviewed source;
- document emergency patching, dependency compromise, and credential rotation procedures.

## AI-specific supply chain

Inventory models, datasets, prompts, tools, connectors, MCP servers, plugins, and retrieved sources that can influence behavior. Validate publisher, permissions, update policy, data handling, and revocation path before enabling an external component.
