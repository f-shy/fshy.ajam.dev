# superbot

> superbot.gg | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/superbot/ | JSON https://fshy.ajam.dev/api/v1/entity/superbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## superbot

- `inference/superbot-gg` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway (BYOK plus house models)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://superbot.gg/api
- free tier: Superbot Free carries 10,000 beta credits a month, refilled on the 1st. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a free account is required; calls use a scoped caller key and your own subscriptions can be connected
- interface: rest
- limits:
  - volume-quota (binding): 10,000 beta credits a month (USD 10 at 1 credit = USD 0.001), refilled on the 1st; 1,200 requests a minute per key [1]
- endpoint: https://api.superbot.gg/v1
- composes with: The monthly credit is a beta allowance, not a standing promise; the house models also carry a per-minute key limit.
- reliability: 402 budget spent; 429 over the per-key bucket; a wake fee applies to idle models on other plans
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Superbot Free grants 10,000 beta credits a month, refilled on the 1st | capture: sha256:3a2cbbdbf2c59df40a07af8be0547482f847838cb4b0b4ca6c43c8d0d02e305b | quote: Superbot Free carries 10,000 beta credits a month, refilled on the 1st.
- sources:
  - [1] https://superbot.gg/api
