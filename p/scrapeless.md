# Scrapeless Agent Browser

> scrapeless.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrapeless/ | JSON https://fshy.ajam.dev/api/v1/entity/scrapeless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scrapeless Agent Browser

- `compute/scrapeless` | paid-only | evidence documented | binding write-gated | category browser host
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:51.745Z (live) | stale on 2026-12-26
- url https://www.scrapeless.com/en/pricing
- free tier: Our service operates on a subscription basis. If your usage is below the minimum account commitment in a given month, we will not retain the remaining funds for you. If you have enabled automatic renewal, your account will be charged for the next billing cycle. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
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
  - [1] 2026-11-25: the FAQ states a subscription basis with a minimum monthly account commitment, no rollover of unused funds, and an option to pay without a monthly subscription | capture: sha256:60493a092eb35cd631dfadcb2a252663c42458054d70ce9018d1b007b2bd40f4 | quote: Our service operates on a subscription basis. If your usage is below the minimum account commitment in a given month, we will not retain the remaining funds for you. If you have enabled automatic renewal, your account will be charged for the next billing cycle. ... Yes, you can choose to pay without a monthly subscription. However, we offer lower discounts for monthly or annual subscriptions.
  - [1] 2026-11-25: the FAQ still states the subscription basis, the minimum monthly commitment, no rollover of unused funds, and the option to pay without a monthly subscription | capture: sha256:60493a092eb35cd631dfadcb2a252663c42458054d70ce9018d1b007b2bd40f4 | quote: Our service operates on a subscription basis. If your usage is below the minimum account commitment in a given month, we will not retain the remaining funds for you. If you have enabled automatic renewal, your account will be charged for the next billing cycle. ... Yes, you can choose to pay without a monthly subscription. However, we offer lower discounts for monthly or annual subscriptions.
- sources:
  - [1] https://www.scrapeless.com/en/pricing
