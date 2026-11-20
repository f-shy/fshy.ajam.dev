# Synthetic

> synthetic.new | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/synthetic/ | JSON https://fshy.ajam.dev/api/v1/entity/synthetic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Synthetic

- `inference/synthetic` | paid-only | evidence documented | binding volume-quota | category inference subscription, weekly regenerating credits
- needs card unknown, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://synthetic.new/pricing
- free tier: no free tier on the pricing page: one subscription for every model, with a weekly credit quota that regenerates 2% every 202 minutes and takes one week to fully regenerate; no card or free-quota terms are stated on the pages read | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a subscription and API key are required; signup fields and card requirements are not stated on the pricing pages read
- interface: rest
- limits:
  - volume-quota (binding): weekly credit quota regenerating 2% every 202 minutes; no five-hour or monthly limits [2]
- binding note: the weekly regenerating credit quota is the only stated ceiling and binds first
- endpoint: https://api.synthetic.new/openai/v1
- tooling: an OpenAI-compatible key at api.synthetic.new/v1 with syn: model aliases
- composes with: pairs with a coding agent through a subscription; infinite mode runs background agents without counting against the rate limit but is for subscribers
- reliability: no reliability event recorded
- notes: the pricing and rate-limits pages describe a paid subscription only; no free allowance is published.
- evidence:
  - [1] 2026-11-18: credits regenerate over the week under a subscription | capture: sha256:dfdfffc6e91b0643aae63eee65cd227712e190baeb96e478edc19e213a63bc1e | quote: One subscription for every model. Credits regenerate over the week and apply at discounted model rates.
  - [2] 2026-11-18: weekly credit limit regenerates incrementally over a week | capture: sha256:342a6dbd15fb02682138f1f17206c26963014d1a25849c5623342697634ace92 | quote: Synthetic plans have a weekly credit limit that regenerates over time. Some models consume more of your credits than others, and larger plans have higher limits.
- sources:
  - [1] https://synthetic.new/pricing
  - [2] https://synthetic.new/rate-limits
