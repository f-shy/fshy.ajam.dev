# Scrapeless Agent Browser

> scrapeless.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrapeless/ | JSON https://fshy.ajam.dev/api/v1/entity/scrapeless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scrapeless Agent Browser

- `compute/scrapeless` | paid-only | evidence documented | binding write-gated | category browser host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:56.072Z (live) | stale on 2026-11-22
- url https://www.scrapeless.com/en/pricing
- free tier: no free tier: the product is a subscription with a minimum monthly account commitment, and unused funds do not roll over | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: a minimum monthly account commitment; usage below it is not refunded or rolled over [1]
  - write-gated (binding): a monthly subscription is the model, though payment can be made without a card via Stripe alternatives or cryptocurrency [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and its FAQ states the subscription basis and that unused funds are not retained. The record's monthly credit figure is not on the extracted page, so the verdict moves to paid-only on the commitment model
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the unit is a request against a monthly commitment; there is no session
  - free_tier_kind: none
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Our service operates on a subscription basis. If your usage is below the minimum account commitment in a given month, we will not retain the remaining funds for you.' and 'Yes, you can choose to pay without a monthly subscription', quoted
- sources:
  - [1] https://www.scrapeless.com/en/pricing
