# Subconscious

> subconscious.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/subconscious/ | JSON https://fshy.ajam.dev/api/v1/entity/subconscious.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Subconscious

- `inference/subconscious` | paid-only | evidence documented | binding volume-quota | category inference endpoint, pay-as-you-go and team plan
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://www.subconscious.dev/
- free tier: no free tier stated: the apex describes pay as you go per token or a Team Token Plan with a fixed monthly price and 5x usage; no free-token allowance is published | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is required; signup fields not stated on the apex page
- interface: rest
- limits:
  - volume-quota (binding): pay per token or fixed monthly Team Token Plan; no free allowance [1]
- binding note: no free tokens stated, so payment binds first
- endpoint: https://api.subconscious.dev/v1
- tooling: an Anthropic-compatible key (the SDK is @ai-sdk/anthropic) against api.subconscious.dev/v1
- composes with: pairs with an Anthropic-compatible agent on a paid per-token or team-plan basis
- reliability: no reliability event recorded
- notes: long-running agent inference sold per token or via a monthly plan; no free offer found.
- evidence:
  - [1] 2026-11-18: two paid ways to use the service, no free tier | capture: sha256:c4822dc3ff3e2fd8cb69cdbf70a1874dbc9f68a600c1afc78cba304b81eb1c9a | quote: - Two ways to pay. Pay as you go per token, or pick a Team Token Plan with a fixed monthly price and 5x the usage. Current rates are on the [pricing page](https://www.subconscious.dev/pricing).
- sources:
  - [1] https://www.subconscious.dev/
