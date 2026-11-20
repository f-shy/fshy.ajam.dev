# Ambient

> ambient.xyz | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ambient/ | JSON https://fshy.ajam.dev/api/v1/entity/ambient.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ambient

- `inference/ambient` | paid-only | evidence documented | binding volume-quota | category inference endpoint, paid subscription and pay-per-token
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://ambient.xyz
- free tier: no free tier: pay per token with plans from USD 1 per month; no free allowance is published | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is obtained from app.ambient.xyz; no card or phone field is stated on the pages read
- interface: rest
- limits:
  - volume-quota (binding): a monthly compute allowance is granted by the subscription and resets at the start of each billing period [2]
- binding note: no free allowance exists, so a paid subscription binds first
- endpoint: https://api.ambient.xyz/v1
- tooling: OpenAI- or Anthropic-compatible SDK pointed at Ambient, plus a browser and desktop app
- composes with: pairs with an OpenAI-compatible agent, but a paid plan or per-token balance is required
- reliability: no reliability event recorded
- notes: the apex states pay per token and plans from USD 1 per month; the pricing page describes only paid subscriptions.
- evidence:
  - [1] 2026-11-18: pay per token, plans from USD 1 per month | capture: sha256:ecb1d28617886d7ed7a560e2a403290dd41b629b77766dc64807f2e10b1c465a | quote: Pay per token · Plans from $1/mo
- sources:
  - [1] https://ambient.xyz
  - [2] https://ambient.xyz/pricing/
