# Morph

> morphllm.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/morphllm/ | JSON https://fshy.ajam.dev/api/v1/entity/morphllm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Morph

- `inference/morph` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference endpoint, free tier plus paid credits
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://www.morphllm.com/pricing
- free tier: Free plan at USD 0 per month with 250K credits and low rate limits; separately, a free tier of 200 requests/month applies to Fast Apply, WarpGrep and Compact; credits reset monthly and do not roll over | unit: credits | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign-up at morphllm.com/sign-up; prepaid credits are required beyond the free tier; no card or phone field is stated on the pricing page
- interface: rest
- limits:
  - volume-quota (binding): 200 requests/month on the free tier for Fast Apply, WarpGrep and Compact; 250K credits on the Free plan, reset monthly and non-rolling [1]
  - request-rate: Free plan rate limits are described as Low [1]
- binding note: the 200 requests/month ceiling and 250K credits reset monthly, so the monthly counter binds first
- endpoint: https://api.morphllm.com/v1
- tooling: an OpenAI-compatible key and the Morph SDK; Fast Apply, WarpGrep and Compact products
- composes with: pairs with coding agents through the free 200 requests/month; the scarce link is that small monthly ceiling
- reliability: no reliability event recorded
- notes: the pricing page states both a 200 requests/month free tier and a Free plan with 250K credits; both are non-rolling monthly allowances.
- evidence:
  - [1] 2026-11-18: a free tier of 200 requests per month and a Free plan with 250K credits | capture: sha256:8113aeaffa468fb3fe792f53590f89ceb92b6ff5c59dd0979702f01831f83d9e | quote: Usage-based pricing. No per-seat fees. Free tier: 200 requests/month. All prices in USD per 1M tokens unless otherwise noted.
  - [1] 2026-11-18: the Free plan is USD 0 with 250K credits and low rate limits | capture: sha256:8113aeaffa468fb3fe792f53590f89ceb92b6ff5c59dd0979702f01831f83d9e | quote: | Free | $0 | 250K | Low |
- sources:
  - [1] https://www.morphllm.com/pricing
