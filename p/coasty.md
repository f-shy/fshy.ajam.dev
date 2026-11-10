# Coasty

> coasty.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coasty/ | JSON https://fshy.ajam.dev/api/v1/entity/coasty.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coasty

- `compute/coasty` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:05.602Z (live) | stale on 2026-12-05
- url https://coasty.ai/pricing
- free tier: $5 of credit at signup on a $0.05-a-managed-step meter, with no monthly minimum and no card | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://coasty.ai/pricing meters $0.05 per managed step and states no egress allowance or overage price | metered: no | source: [1]
- identity: email | detail: 'No credit card, no subscription', quoted from coasty.ai/pricing read 2026-10-22
- interface: rest, ssh
- limits:
  - request-rate (binding): $0.05 a managed step; the first $5 is free, which is 100 steps [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: REST API with an OpenAPI schema, an MCP server (npx @coasty/mcp) and managed SSH and VNC credentials for machines; no CLI is documented
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The free grant is one-time and metering is per step.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the meter is per managed step, not per second, so an idle session costs nothing
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'First $5 on us' and '$0.05 per managed step' and 'No monthly minimum' and '$25 of API credit every month' on the paid tier, quoted
  - [1] 2026-11-03: pricing is per managed step; no egress allowance or overage price is published | capture: sha256:50ff4f16b1018336474117cb51e66b8bacb34d0087e37f0b351b5c78b8421353 | quote: Usage-based pricing for the computer-use API.
  - [2] 2026-11-03: the REST API returns managed SSH credentials | capture: sha256:087cbd8a2f699ca04d6f014f03555eea997c048262ce31ed6fd6c34a5156475d | quote: | `GET /v1/machines/{id}/connection` | `connection:read` | Managed SSH/VNC credentials; external returns `409 INVALID_STATE`. |
- sources:
  - [1] https://coasty.ai/pricing
  - [2] https://coasty.ai/docs/llms.txt
