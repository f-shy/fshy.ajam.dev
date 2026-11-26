# Qovery

> qovery.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qovery/ | JSON https://fshy.ajam.dev/api/v1/entity/qovery.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qovery

- `compute/qovery` | paid-only | evidence documented | binding none | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:45.876Z (live) | stale on 2026-12-26
- url https://www.qovery.com/pricing
- free tier: Free: $0, 3 users plus unlimited AI agents, 1 cluster of your own, 1,000 deployment minutes a month, no credit card. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card for the trial: the pricing page states 'Starter USD 299 per month billed yearly with a 14-day free trial, no credit card required'. No hold exists on the trial because no payment method is taken. The signup fields are not quoted, so the email requirement is inferred rather than read; a card enters only when Starter is bought, and debit and prepaid acceptance are not stated.
- interface: unknown
- limits note: there is no allowance to bind: the platform floor is USD 299 a month and the instances are billed by the cloud account it manages.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none for a zero-budget start: 14 days of a control plane over a cloud account that must already exist.
- reliability: no reliability event recorded
- notes: Qovery cloud deployment platform starts at USD 299 monthly with a 14-day trial period. Cloud infrastructure costs bill directly to the user's cloud provider account.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: Starter USD 299 per month billed yearly with a 14-day free trial, no credit card required; 1 managed cluster on your own cloud; 3,000 minutes of deployment per month, quoted
  - [1] 2026-10-22: Growth USD 899 per month with 2 managed clusters; the page describes the product as running in the customer's cloud account, quoted
  - [1] 2026-11-25: the pricing page states a permanent Free plan at $0 with 3 users, unlimited AI agents, one own cluster, 1,000 deployment minutes and no credit card | capture: sha256:e4a158f5e840effc09322cb9087fb635cd296ff28f0ab1ab83da88d51b1236de | quote: Free: $0, 3 users plus unlimited AI agents, 1 cluster of your own, 1,000 deployment minutes a month, no credit card.
  - [1] 2026-11-25: the pricing page still states the Free $0 plan and its limits | capture: sha256:e4a158f5e840effc09322cb9087fb635cd296ff28f0ab1ab83da88d51b1236de | quote: Free: $0, 3 users plus unlimited AI agents, 1 cluster of your own, 1,000 deployment minutes a month, no credit card.
- sources:
  - [1] https://www.qovery.com/pricing
