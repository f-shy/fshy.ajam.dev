# GraphN

> graphn.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/graphn/ | JSON https://fshy.ajam.dev/api/v1/entity/graphn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GraphN

- `inference/graphn` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://graphn.ai/pricing
- free tier: USD 1 in free credits against a per-token catalogue, with DeepSeek V4.1 Flash at USD 0.30 per 1M input tokens on the same page. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup is required and the page states no other gate
- interface: rest
- limits:
  - volume-quota (binding): USD 1 of free credits [1]
- endpoint: https://model.graphn.ai/v1
- composes with: USD 1 is the whole allowance, so it buys evaluation rather than a workload
- reliability: a starter credit this small is exhausted by a few long completions
- evidence:
  - [1] 2026-11-18: the account starts with USD 1 in free credits and models are billed per token | capture: sha256:273e0966e70787845ad478ccadb78c528f03c838f5cfe35b2ad3e59083b0b318 | quote: $1 in free credits
- sources:
  - [1] https://graphn.ai/pricing
