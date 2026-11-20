# Cortecs

> cortecs.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cortecs/ | JSON https://fshy.ajam.dev/api/v1/entity/cortecs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cortecs

- `inference/cortecs` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://cortecs.ai/
- free tier: No free allowance is stated on the site read 2026-11-18: a flat 5% service fee is charged on top-up and token usage is billed at the upstream provider's published rates. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an account with a topped-up balance is required before key use
- interface: rest
- limits:
  - volume-quota (binding): flat 5% service fee on top-ups; token usage at upstream published rates [1]
- endpoint: https://api.cortecs.ai/v1
- tooling: an OpenAI-compatible key against the European gateway
- composes with: the 5% top-up fee plus upstream per-token billing is the scarce link; no free tier is published
- reliability: all models and features are available after top-up with no additional limits
- evidence:
  - [1] 2026-11-18: a flat 5% service fee applies on top-up | capture: sha256:b3753a3b5ecbcbb0249304130694e4b4493595246a78f6bb5c50949a480c77a6 | quote: You pay a flat 5% service fee when topping up.
- sources:
  - [1] https://cortecs.ai/
