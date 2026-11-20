# Tiger Cloud

> tigerdata.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tigerdata/ | JSON https://fshy.ajam.dev/api/v1/entity/tigerdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tiger Cloud

- `compute/tiger-cloud` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:58.529Z (live) | stale on 2026-12-05
- url https://www.tigerdata.com/pricing
- free tier: No free plan. Performance plan, quoted: 'Starting at $30/month'. The FAQ states the only free route: 'Yes! We offer new users a free, 30-day trial period (no credit card required) of our Performance plan.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: the 30-day clock ends it, and the trial is on a plan whose paid floor is USD 30 a month, so there is no downgrade path to zero at day 31. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card for the trial: the FAQ states 'We offer new users a free, 30-day trial period (no credit card required) of our Performance plan', so no hold exists on that route. The evidence does not say which identifier the account is created with, so whether an email alone suffices is not stated. A card becomes necessary at day 31, because the trial runs on a plan whose paid floor is USD 30 a month and there is no free lane to fall back to
- interface: unknown
- limits:
  - retention-clamped (binding): the 30-day clock ends it, and the trial is on a plan whose paid floor is USD 30 a month, so there is no downgrade path to zero at day 31. [1]
- limits note: the 30-day clock ends it, and the trial is on a plan whose paid floor is USD 30 a month, so there is no downgrade path to zero at day 31.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a 30-day Tiger trial is a genuine time-series Postgres with compression, useful for one benchmarking run; after it the free time-series lane in documented records is InfluxDB Cloud Serverless at 17 kb/s, not Tiger.
- reliability: no reliability event recorded
- notes: Timescale free tier, which older notes record, is not on the page read on 2026-10-22. The product is now called Tiger Cloud and the vendor domain is tigerdata.com. The verdict is trial-only rather than paid-only because a clocked free lane exists; the USD 30 a month paid floor is in the offer field, and there is no perpetual free lane.
- extras:
  - facets.class: paid-only
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
- evidence:
  - [1] 2026-10-22: Performance plan 'Starting at $30/month' with 4 database services, up to 8 CPU and 32 GB memory per service, point-in-time recovery to 3 days
  - [1] 2026-10-22: FAQ: 'We offer new users a free, 30-day trial period (no credit card required) of our Performance plan.', quoted
  - [2] 2026-10-22: the timescale.com pricing URL now redirects to tigerdata.com/pricing, so the vendor renamed the product
  - [1] 2026-11-03: the pricing page lists compute and storage billing and no egress allowance or price | capture: sha256:9d21af3f9fa8e8dc8f6b0b2d096abed91789fda01d62317a22c803c375637cb2 | quote: Hourly billing for your configured compute and actual storage used, no hidden fees. Cancel anytime.
- sources:
  - [1] https://www.tigerdata.com/pricing
  - [2] https://www.timescale.com/pricing
