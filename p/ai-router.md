# AI-ROUTER

> ai-router.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ai-router/ | JSON https://fshy.ajam.dev/api/v1/entity/ai-router.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI-ROUTER

- `inference/ai-router` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://ai-router.dev/pricing/
- free tier: No free allowance is stated on the pricing page read 2026-11-18: access is sold as daily, weekly and monthly USD packages, e.g. a 1-day 50U plan at $1.59/day. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: payment via Alipay, Crypto or Stripe is needed to buy a package
- interface: rest
- limits:
  - volume-quota (binding): paid packages with USD limits, e.g. $1.59/day for a 50U 1-day plan [1]
- endpoint: https://api.ai-router.dev/v1
- tooling: an OpenAI-compatible key issued by the gateway after a package is bought
- composes with: the prepaid package is the scarce link; no standing free tier is published
- reliability: packages are time-limited and expire after their stated validity (24 hours, 7 days or 30 days)
- evidence:
  - [1] 2026-11-18: access is sold as timed USD quota packages with no free tier | capture: sha256:82fdd39c79164a0a00912f198bb8f030e11c06f7c624f3d91970cb84018f31cb | quote: $1.59 USD/ day
- sources:
  - [1] https://ai-router.dev/pricing/
