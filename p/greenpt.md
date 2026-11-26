# GreenPT

> greenpt.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/greenpt/ | JSON https://fshy.ajam.dev/api/v1/entity/greenpt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GreenPT

- `inference/greenpt` | trial-only | evidence documented | binding volume-quota | category inference subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://greenpt.ai/pricing
- free tier: Starter, Pro and Teams each include a 14-day free trial, with Starter at EUR 4.50 a month and Pro at EUR 17.50 a month; the top tier has no trial and is paid from the first day. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: signup is required and a payment method is added at the start of the trial: "You add a payment method when you start, and your paid plan starts after the trial unless you cancel."
- interface: rest
- limits:
  - volume-quota (binding): a 14-day trial on the Starter, Pro and Teams tiers [1]
- endpoint: https://api.greenpt.ai/v1
- tooling: an OpenAI-compatible base URL and the vendor console
- composes with: fourteen days is the scarce link, and the top tier has no trial at all
- reliability: a trial that ends by calendar rather than by usage, so the cap arrives whether or not the allowance was used
- evidence:
  - [1] 2026-11-18: Starter, Pro and Teams include a 14-day free trial at EUR 4.50 and EUR 17.50 a month, and the top tier has none | capture: sha256:36fa179bd8db591d67f5d531d2417cecf5ce5379f26da6be2d4f95a215da92b0 | quote: Simple, transparent pricing with no surprises. Every plan runs on 100% renewable energy, hosted in the EU. Starter, Pro and Teams include a 14-day free trial.
- sources:
  - [1] https://greenpt.ai/pricing
