# Liquid Inference

> liquidinference.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/liquidinference/ | JSON https://fshy.ajam.dev/api/v1/entity/liquidinference.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Liquid Inference

- `inference/liquid` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://liquidinference.ai/pricing/
- free tier: Free plan: 50 free-model requests a day with no fee; monthly plans raise the allowance to 2,000 (Lite), 10,000 (Plus) or 100,000 (Pro) free-model requests a day. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account is required; a card is only used for a monthly plan or funding
- interface: rest
- limits:
  - request-rate (binding): 50 free-model requests per day on the Free plan [1]
- endpoint: https://router.inference.ai.exchange/v1
- composes with: the 50-per-day free-model cap binds immediately on the standing free plan
- reliability: free-model offers are buyer-paid at the exchange fee floor of at most 1 cent per million tokens, so a 'free' model is not zero cost
- notes: Free offers still carry an exchange fee; see /docs/fees.md.
- evidence:
  - [1] 2026-11-18: the Free plan allows 50 free-model requests a day at no fee | capture: sha256:fc5f9af966f8fdc932fd2ecce9cbaa03564613a3a811ee546cca7e1fd545fd4b | quote: 50 free-model requests a day. No fee.
- sources:
  - [1] https://liquidinference.ai/pricing/
