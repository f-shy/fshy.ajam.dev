# Marlin

> marlin.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/marlin/ | JSON https://fshy.ajam.dev/api/v1/entity/marlin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Marlin

- `compute/marlin` | paid-only | evidence documented | binding write-gated | category cloud VM
- needs card unknown, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.marlin.org/
- free tier: TEE and ZK coprocessors for delegating workloads to a decentralized cloud, sold to protocols that need verifiable execution; the homepage exposes no price, plan, credit or sign-up for an individual. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: no individual on-ramp exists: the homepage exposes no price, plan, credit or sign-up, and the products are TEE and ZK coprocessors sold as integration contracts to other protocols, so the gate is a business relationship rather than a person's signup. What that contract asks of a counterparty, whether a card, entity documents or an ID check, is not stated, and the proving marketplace subdomain answered 525 so no signup page could be read
- interface: unknown
- limits:
  - write-gated (binding): There is no individual on-ramp at all: the products are integration contracts for other protocols, so the first gate is a business relationship. [1]
- limits note: There is no individual on-ramp at all: the products are integration contracts for other protocols, so the first gate is a business relationship.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None reachable: a protocol integration is the only entry point.
- reliability: no reliability event recorded
- notes: The 525 is evidence about the Kalypso endpoint on 2026-10-22, not proof that the programme is withdrawn; it may be a certificate or origin fault. A retest is worth one request before any record calls it dead.
- extras:
  - facets.class: paid-cloud
- evidence:
  - [1] 2026-10-22: positioning as 'Scalable coprocessors for decentralized compute', TEE and ZK, no pricing or signup
  - [2] 2026-10-22: the proving marketplace subdomain answers HTTP 525 (TLS handshake to origin failed), so the endpoint is not serving
- sources:
  - [1] https://www.marlin.org/
  - [2] https://kalypso.marlin.org/
