# Phase Router

> phase.xyz | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/phase/ | JSON https://fshy.ajam.dev/api/v1/entity/phase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Phase Router

- `inference/phase` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://router.phase.xyz/
- free tier: No free inference allowance is published: a prepaid API key or a per-request USDT wallet pays for each call, with a signed receipt, and there is no subscription. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a prepaid API key or a USDT x402 wallet funds requests; no free route is stated
- interface: rest
- limits:
  - volume-quota (binding): prepaid API key or per-request USDT wallet; no free tier [1]
- endpoint: https://router.phase.xyz/v1
- composes with: the prepaid balance or wallet is the scarce link
- reliability: no standing free tier is published
- evidence:
  - [1] 2026-11-18: requests are paid through a prepaid key or a per-request wallet with no free tier | capture: sha256:cf56592c9ca3f151b2d2ee16135e4de55fdfdad7d843cd23c114ac939670e884 | quote: A prepaid API key, or a wallet that pays per request (x402). No subscription.
- sources:
  - [1] https://router.phase.xyz/
