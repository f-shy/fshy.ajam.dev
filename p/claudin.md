# Claudinio

> claudin.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/claudin/ | JSON https://fshy.ajam.dev/api/v1/entity/claudin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Claudinio

- `inference/claudinio` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://claudin.io
- free tier: No free tier is stated. Flat-rate coding subscriptions from USD 19 a month with an hourly anti-runaway ceiling of USD 2 to USD 10 depending on the plan. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a subscription account paid by card, PIX, Apple Pay, Google Pay or Amazon Pay; sign in with GitHub
- interface: rest
- limits:
  - volume-quota (binding): flat-rate USD 19 to USD 99 a month with an hourly anti-runaway ceiling of USD 2 to USD 10 [1]
- endpoint: https://api.claudin.io/v1
- tooling: Claude Code, Cursor and Cline connect through OpenAI- and Anthropic-compatible endpoints
- composes with: the paid subscription and the hourly anti-runaway ceiling are the scarce links; no free allowance is published
- reliability: the hourly anti-runaway ceiling resets automatically and only acts on extreme spikes; no daily caps, weekly quotas or session limits
- notes: no free tier is published; a flat-rate subscription is required
- evidence:
  - [1] 2026-11-18: plans are flat-rate subscriptions from USD 19 a month with an hourly anti-runaway ceiling; no free tier is stated | capture: sha256:885cc9c14dcbb8c532aab955315d30b8abed3a78f637472483b90ef772e70805 | quote: You pay once (from $19/mo), plug the key into your editor, and just code.
- sources:
  - [1] https://claudin.io
