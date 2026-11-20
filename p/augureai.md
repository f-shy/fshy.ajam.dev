# Augure

> augureai.ca | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/augureai/ | JSON https://fshy.ajam.dev/api/v1/entity/augureai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Augure

- `inference/augure` | qualifies | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://augureai.ca/pricing
- free tier: Every account starts on the Free plan with no card required; it includes Ossington 5 and Tofino 3 with a daily allowance, and developer keys have a USD 100 CAD per day hard ceiling (USD 25 CAD until the first successful payment). | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the page states the Free plan needs no card
- interface: rest
- limits:
  - volume-quota (binding): a daily allowance on the Free plan [1]
  - request-rate: developer keys are capped at USD 100 CAD per day, USD 25 CAD per day until the first successful payment [1]
- endpoint: https://api.augureai.ca/v1
- composes with: the daily allowance is the scarce link, and the USD 25 CAD ceiling binds before the USD 100 CAD one
- reliability: a daily spend ceiling on keys means a long run stops mid-flight rather than degrading
- evidence:
  - [1] 2026-11-18: accounts start on a no-card Free plan with a daily allowance, and developer keys carry a USD 100 CAD daily ceiling | capture: sha256:01294a33611fe4add94a0402b93f57384853abf6e4089dc5a7469c641d858280 | quote: Yes. Every account starts on the Free plan, with no card required. Free includes Ossington 5 and Tofino 3 with a daily allowance. Rosedale One appears in the model list but is locked until you move to a paid plan.
- sources:
  - [1] https://augureai.ca/pricing
