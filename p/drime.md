# Drime

> drime.cloud | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drime/ | JSON https://fshy.ajam.dev/api/v1/entity/drime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Drime (Advanced / 10 TB lifetime)

- `storage/drime` | qualifies-with-caveat | evidence reported | binding write-gated | category EU collaborative cloud, lifetime one-time
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://drime.cloud/pricing
- price $3.00/TB at 6 TB subscription (EUR 15.99 = $17.96); one-time $36.00/TB lifetime at 10 TB ($359.97), which amortises to $1.50/TB/mo over 2 years and $0.50/TB/mo over 6 years | parsed USD 3/TB-mo
- free tier: Subscription: Starter 500 GB, Essentials 2 TB, Professional 3 TB, Advanced 6 TB. Lifetime via StackSocial: 2 TB $149.97, 3 TB $199.97, 10 TB $359.97. Direct partner landing shows 10 TB lifetime at $249 promo against a $360 base. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Subscription page lists 'Unlimited Bandwidth' as a feature of every paid tier. No metered-egress clause found on the pricing page. | metered: yes
- identity: email | detail: email
- interface: rest, rclone
- limits:
  - write-gated (binding): Review. Shortest track record of any vendor here. [1]
- limits note: Lifetime tiers cap members/workspaces (100 on Advanced 6 TB) but not file size
- interface detail: Native rclone Tier 1 backend (rclone/rclone backend/drime, integration_tests: Passing, data_integrity: High), plus REST API + webhooks and a documented developer portal
- tooling: rclone native, first-class; API token auth
- composes with: best-in-lane chaining among the lifetime vendors: real API, real backend, so it can sit under AList/OpenList
- reliability: Founded 2024 per third-party review. Shortest track record of any vendor here. No data-loss event yet, simply because there is not enough history. Redemption deadline: code must be redeemed within 30 days of purchase.
- notes: the same as the free tier
- extras:
  - price_verbatim: $3.00/TB at 6 TB subscription (EUR 15.99 = $17.96); one-time $36.00/TB lifetime at 10 TB ($359.97), which amortises to $1.50/TB/mo over 2 years and $0.50/TB/mo over 6 years
- evidence:
  - [2] 2026-10-21: 'Essentials ... EUR 5.50 EUR 4.40 per month, billed annually ... 2 TB of storage'; 'Advanced EUR 19.99 EUR 15.99 per month ... 6 TB'
  - [1] 2026-10-21: 'Deal Price $359.97 ... 10TB'
  - [3] 2026-10-21: 'Advanced - 10TB Lifetime ... $249 ... $360'
  - [4] 2026-10-21: backend: drime, tier: Tier 1, integration_tests: Passing
  - [5] 2026-10-21: native backend docs
- sources:
  - [1] https://www.stacksocial.com/sales/drime-secure-cloud-storage-lifetime-subscription-advanced-plan-10tb
  - [2] https://drime.cloud/pricing
  - [3] https://drime.cloud/kenmoo
  - [4] https://github.com/rclone/rclone/blob/b5a81dab/docs/data/backends/drime.yaml
  - [5] https://rclone.org/drime/
