# Infersia

> infersia.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infersia/ | JSON https://fshy.ajam.dev/api/v1/entity/infersia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Infersia

- `inference/infersia` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://infersia.com/pricing
- free tier: Rate-limited access to models with a published free tier, with per-token prices published beside it and no credit amount stated. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup is required and the page states no other gate
- interface: rest
- limits:
  - request-rate (binding): unpublished rate limit on the free tier [1]
- endpoint: https://api.infersia.com/v1
- composes with: the rate limit is the scarce link, and the page does not publish it
- reliability: the free tier is described but its rate is not published, so the constraint is inferred from the qualification
- evidence:
  - [1] 2026-11-18: the platform offers rate-limited access on a published free tier while the paid catalogue is priced per token | capture: sha256:2b48728dcac1a13e6a5719eb98f185675144c101d175db01e454d8b8ee9c9632 | quote: Rate-limited access to models with a published free tier. Enough to evaluate the platform properly, and it costs us cents to run.
- sources:
  - [1] https://infersia.com/pricing
