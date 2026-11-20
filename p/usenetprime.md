# UsenetPrime

> usenetprime.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetprime/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetprime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetPrime

- `debrid/usenetprime` | paid-only | evidence documented | binding none | category Usenet provider (US/EU servers) - no free trial | tier Prime Unlimited Yearly
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://www.usenetprime.com/
- free tier: None on the page read: "Unlimited subscriptions or blocks that never expire" with "Prime Unlimited Yearly $6.25/mo, Billed $75 annually". No trial, free account or free allowance is offered. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The page renders a currency switch (USD/EUR) and a plan grid; no free path is present in the rendered content.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "5,912+ days retention" in the service feature list. | days: 5912 | source: [1]
- egress: Unlimited on subscriptions; blocks do not expire. No traffic price is published. | metered: no | free allowance: none | source: [1]
- identity: card | detail: The page says "Checkout is handled by the billing portal"; every plan is a purchase. The instrument at checkout was not read.
- interface: unknown
- limits:
  - request-rate: up to 50 connections [1]
  - retention-clamped: 5,912+ days [1]
- binding note: No byte counter on the unlimited plan; 50 connections and 5,912 days are far above what a monthly transfer of 1 TiB needs, so the price is the constraint.
- interface detail: NNTP over SSL, up to 50 connections, US and EU servers. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client
- composes with: One of several $6-ish unlimited months; it adds nothing over its competitors except a EUR display and US/EU server choice, so it is a price comparison, not a ladder step.
- reliability: No suspension or throttle report was read.
- notes: Repeatability: not applicable. Abandonment: if a trial link appears, add a tier.
- evidence note: Prices and limits are quoted from the vendor page on 2026-10-23.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no free trial
- evidence:
  - [1] 2026-10-23: "Unlimited subscriptions or blocks that never expire", "Prime Unlimited Yearly $6.25/mo Billed $75 annually", "5,912+ days retention", "Up to 50 connections", "Checkout is handled by the billing portal"
- sources:
  - [1] https://www.usenetprime.com/
