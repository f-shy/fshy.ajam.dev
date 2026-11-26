# TrustedRouter

> trustedrouter.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trustedrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/trustedrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TrustedRouter

- `inference/trustedrouter` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://trustedrouter.com/pricing
- free tier: Prepaid credits at provider cost plus a 5.5% markup with a USD 0.01 per million token floor; migration credits are available to teams already spending over USD 100 per month by approval, and there is no standing free tier. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: card, ACH bank, PayPal and stablecoin checkout for prepaid credits
- interface: rest
- limits:
  - volume-quota (binding): provider cost plus 5.5% with a USD 0.01/Mtok floor; migration credits by approval [1]
- endpoint: https://api.trustedrouter.com/v1
- composes with: the prepaid balance is the scarce link
- reliability: a one-microdollar minimum per billed request applies to small calls
- evidence:
  - [1] 2026-11-18: migration credits are approval-gated and there is no standing free tier | capture: sha256:8394d0e1bbf722410a6fad949b830a5f8081358a6a1ba6169cb6d79454f8beb5 | quote: Teams already spending more than $100/month on LLMs can request migration credits by approval.
- sources:
  - [1] https://trustedrouter.com/pricing
