# Ideogram

> ideogram.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ideogram/ | JSON https://fshy.ajam.dev/api/v1/entity/ideogram.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ideogram

- `compute/ideogram` | paid-only | evidence inferred | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:28.101Z (live) | stale on 2026-12-26
- url https://ideogram.ai/pricing/
- free tier: The published plans begin at Plus: '$15 per month, $180 billed annually', '2,400 priority credits/mo.'; Pro is '$60' per month with '7,500 priority credits/mo.'; Team is '$30' 'per user per month' with '3,600 priority credits/user/mo.'; pay as you go is '1¢ per credit'. 'Unlimited slow credits' is listed only under Pro. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none-published
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account, with no card or hold stated: the published plans are all paid and no free row appears. If any free allowance remains, a Korean-language report dated 2026-10-18 claims free accounts get 30 credits a week signing in with Google, Apple or Microsoft and that email signups are excluded, reported and not confirmed. So whether an email-only account reaches any free capacity is unknown, and which identifier the paid signup requires is not stated
- interface: unknown
- limits:
  - volume-quota (binding): the free lane is not on the price list: the cheapest published entry is USD 15 a month, so a person with an email address and no card has nothing to generate with, and the only reports of a remaining free allowance are 10 to 30 credits a week, which is a handful of images. [1]
- limits note: the free lane is not on the price list: the cheapest published entry is USD 15 a month, so a person with an email address and no card has nothing to generate with, and the only reports of a remaining free allowance are 10 to 30 credits a week, which is a handful of images.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nothing to chain at the free tier. The paid entry is USD 15 for 2,400 credits, which at one credit an image is a cheap image lane, but it is a subscription rather than a credit grant.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The inference is that the free lane closed, because the vendor's price list no longer carries a free row and because a September 2026 capture recorded the allowance as de-published while an October 2026 third-party report claims a 30-credit weekly allowance for social logins only. Not done.
- extras:
  - facets.class: paid-only
  - facets.free_tier_kind: none-published
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the plan list begins at 'Plus ... $15 per month, $180 billed annually ... 2,400 priority credits/mo.' and no free plan appears in the page text, quoted
  - [1] 2026-10-22: 'Unlimited slow credits' is listed only under the Pro plan at '$60 per month', quoted
  - [2] 2026-10-22: a capture dated 2026-09-21 records the free row as 'Free | Free | - | Hard stop' and notes 'Ideogram de-published the free weekly allowance', reported
  - [3] 2026-10-22: 'the free plan will now be limited to 10 credits per week, which will be renewed every Friday at midnight UTC', reported for changes effective January 2025
  - [4] 2026-10-22: a Korean-language report dated 2026-10-18 claims free accounts get 30 credits a week when signing in with Google, Apple or Microsoft, and that email signups are excluded, reported and not confirmed
  - [1] 2026-11-25: the Plus plan is published at $15 per month, $180 billed annually, with 2,400 priority credits per month | capture: sha256:230fbf5ac4748b0e5242067bc737c1288ab8ac0d25ec8cee9794f7f68e31ab73 | quote: $15 $15 per month, $180 billed annually 2,400 priority credits/mo.
  - [1] 2026-11-25: the Pro plan is published at $60 per month with 7,500 priority credits per month | capture: sha256:230fbf5ac4748b0e5242067bc737c1288ab8ac0d25ec8cee9794f7f68e31ab73 | quote: $60 $42 $42 per month, $504 billed annually 7,500 priority credits/mo.
  - [1] 2026-11-25: the Team plan is published at $30 per user per month with 3,600 priority credits per user per month | capture: sha256:230fbf5ac4748b0e5242067bc737c1288ab8ac0d25ec8cee9794f7f68e31ab73 | quote: $30 $20 $20 per user per month, $240 per user billed annually 3,600 priority credits/user/mo.
  - [1] 2026-11-25: pay-as-you-go credits are priced at one cent per credit | capture: sha256:230fbf5ac4748b0e5242067bc737c1288ab8ac0d25ec8cee9794f7f68e31ab73 | quote: 1¢ per credit Credits on demand
  - [1] 2026-11-25: the unlimited slow-credits line is a Pro feature | capture: sha256:230fbf5ac4748b0e5242067bc737c1288ab8ac0d25ec8cee9794f7f68e31ab73 | quote: - Unlimited slow credits
- sources:
  - [1] https://ideogram.ai/pricing/
  - [2] https://www.strategyoffinance.com/benchmarks/ai-credit-index/reviewed/ideogram/
  - [3] https://craftium.ai/ideogram-change-plans/
  - [4] https://mendoi-apps.com/ko/articles/ideogram-free-30-weekly-google-login-email-excluded-new-2400-credits/
