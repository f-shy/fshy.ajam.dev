# Qoddi

> qoddi.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qoddi/ | JSON https://fshy.ajam.dev/api/v1/entity/qoddi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qoddi

- `compute/qoddi` | paid-only | evidence documented | binding none | category platform host
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://qoddi.com/pricing/
- free tier: The free tier covers static sites only: 'Static sites - Free - Your first 3 static sites - Git deployments - Unlimited bandwidth'. Application hosting starts at 'USD 6/ month, from - 1 GB RAM / 1 vCPU on XS'. Hourly rates cap at a monthly maximum: XS 'USD 0.008' an hour and 'USD 6' a month, S 2 GB USD 18, M 4 GB USD 36, L 8 GB USD 69, XL 16 GB USD 120. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Static sites - Free - Your first 3 static sites - Git deployments - Unlimited bandwidth - Unlimited team members', quoted | metered: no | source: [1]
- identity: card | detail: a card is required even for the free tier: the pricing page states "Account verification requires a credit or debit card, including for free sites. Prepaid cards are not accepted.", so a debit card is accepted and a prepaid card is rejected. The record does not state whether the card is charged or authorised for any amount at verification, whether a hold is placed, or whether an email address is also required
- interface: git
- limits note: nothing binds above the scale at the paid floor; the free tier carries no compute, so the first wall is the USD 6 monthly minimum.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the per-second rate capped at a monthly maximum makes this a burst host: an hour of the 8 vCPU / 8 GB L box costs USD 0.092 and a full month costs USD 69, so an afternoon job is billed in cents.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'Free tier for static assets, staging, and developer apps'. The app-hosting half is gone from the pricing page, which now prices App hosting from USD 6 a month; only static sites remain free. The aggregator omits the card requirement, which applies even to the free static tier and rejects prepaid cards.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
- evidence:
  - [1] 2026-10-22: 'Static sites - Free - Your first 3 static sites - Git deployments - Unlimited bandwidth - Unlimited team members', quoted
  - [1] 2026-10-22: 'App hosting - USD 6/ month, from - 1 GB RAM / 1 vCPU on XS - Git or Docker deployments', quoted
  - [1] 2026-10-22: 'Account verification requires a credit or debit card, including for free sites. Prepaid cards are not accepted.', quoted
  - [1] 2026-10-22: rate table: 'XS | 1 GB | 1 vCPU | USD 0.008 | USD 6' through 'XL | 16 GB | 8 vCPUs | Billed per second | USD 120', quoted
- sources:
  - [1] https://qoddi.com/pricing/
