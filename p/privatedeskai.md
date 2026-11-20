# SAGG

> privatedeskai.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privatedeskai/ | JSON https://fshy.ajam.dev/api/v1/entity/privatedeskai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SAGG

- `inference/sagg` | paid-only | evidence documented | binding volume-quota | category inference gateway (failover)
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://api.privatedeskai.com/pricing
- free tier: Create an account with your e-mail (free). A key is issued after your first top-up: from $10 to $500, paid via Stripe. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: email account is free but the key needs a first paid top-up of USD 10 or more
- interface: rest
- limits:
  - volume-quota (binding): first top-up from USD 10 to USD 500 [1]
- endpoint: https://api.privatedeskai.com/v1
- composes with: No free inference tier; the word free applies only to account creation.
- reliability: 17 to 23 percent of short answers on the Gonka path ended with repeated text before an October 2026 cut-off fix; measured 2026-10-27
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: SAGG requires a USD 10 to 500 Stripe top-up before a key is issued, with no free inference allowance | capture: sha256:c5dd9f902493e593d881a30eb2dedaae6ae6f43e44e4208eb7ea2e43f40ecc48 | quote: Create an account with your e-mail (free). A key is issued after your first top-up: from $10 to $500, paid via Stripe.
- sources:
  - [1] https://api.privatedeskai.com/pricing
