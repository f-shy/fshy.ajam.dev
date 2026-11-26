# Serverdiscounter NEXT Share

> serverdiscounter.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serverdiscounter/ | JSON https://fshy.ajam.dev/api/v1/entity/serverdiscounter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Serverdiscounter NEXT Share (managed Nextcloud)

- `netdisk-pan/serverdiscounter-next-share` | qualifies | evidence documented | binding per-object-cap | category managed Nextcloud, paid only
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T14:45:36.596Z (live) | stale on 2026-12-17
- url https://serverdiscounter.com/en/nextcloud
- price EUR 2.40/TB/month including VAT at 25 TB (EUR 59.95/month), rising to EUR 4.95/TB/month at 1 TB, read 2026-10-22 | parsed USD 2.7/TB-mo
- free tier: 14 Days Free Trial All features. No credit card. No commitment. | unit: TiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: 10 GB is a decimal figure the vendor writes as 10 GB.
- retention: Minimum term one month, cancellation monthly, no setup fee, and a 30-day money-back guarantee | source: [1]
- egress: 'Traffic Flatrate' on all four tiers, stated as a line of the feature comparison rather than a footnote | metered: no | free allowance: flatrate | source: [1]
- identity: card | detail: a Serverdiscounter account and a card. The trial is advertised as needing no card; the paid order does. No identity document stated
- interface: webdav, rest, rclone
- limits:
  - per-object-cap (binding): 10 GB per file on every tier, including 25 TB [1]
- binding note: The 10 GB per-file ceiling is then the only number that shapes the plan: every object over 10 GB has to be chunked client-side, which is a property of the tooling and not of the quota.
- tooling: rclone webdav, the Nextcloud clients, and the admin panel for per-user quotas. 'Mount as network drive' is an advertised feature on every tier
- composes with: Full admin access plus per-user storage quotas means the archive can be divided into shares with separate credentials without buying more accounts
- reliability: Stuttgart, Germany, 100% renewable power, UPS and backup power stated. 30-day money-back. The per-file cap is the friction and it is uniform across tiers, so it never improves with size
- notes: The trial is 14 days and needs no card, which is the cheapest way to test a WebDAV mount before paying.
- evidence note: Prices and the per-file cap are from the vendor's own comparison table, read. `documented`, not `measured`: no order was placed, so the WebDAV endpoint and the real per-file behaviour are unexercised.
- extras:
  - access_mode: paid
  - free_tier_exists: no
  - trial: 14 days, no card, deleted unless extended
  - region: Stuttgart, Germany
  - contract: 1 month minimum, monthly cancellation, no setup fee
  - price_includes_vat: yes
  - tier_prices_eur_month_inc_vat.small_1TB: 4.95
  - tier_prices_eur_month_inc_vat.basic_5TB: 15.95
  - tier_prices_eur_month_inc_vat.grow_10TB: 29.95
  - tier_prices_eur_month_inc_vat.big_25TB: 59.95
  - per_file_cap_bytes_derived: 10000000000
- evidence:
  - [1] 2026-10-22: 'NEXT Share Small ... EUR 4,95 /M, incl. VAT ... 1 TB', 'NEXT Share Basic EUR 15,95 ... 5 TB', 'NEXT Share Grow EUR 29,95 ... 10 TB', 'NEXT Big EUR 59,95 ... 25 TB', each with 'Users: Unlimited', 'Admin Access', 'Traffic Flatrate'
  - [1] 2026-10-22: the detailed feature comparison gives 'Max. file size 10 GB 10 GB 10 GB 10 GB' against 1 TB / 5 TB / 10 TB / 25 TB, and 'Minimum term 1 Month' with 'Cancellation period Monthly'
  - [1] 2026-10-22: FAQ: 'Is cloud storage per user? No, it's a quota per contract. You can create unlimited users and distribute the storage among all users'
  - [1] 2026-11-19: the first-party comparison table still lists 1/5/10/25 TB tiers; the same read shows 10 GB max file size, Flatrate traffic and 1 Month minimum term | capture: sha256:4128b72274dce249218e836c6bb8d665e68ae42d269a719297941b099394aa23 | quote: | Cloud Storage | 1 TB | 5 TB | 10 TB | 25 TB |
  - [1] 2026-11-19: the first-party page still advertises a 14-day trial needing no credit card; the paid order still requires a card | capture: sha256:4128b72274dce249218e836c6bb8d665e68ae42d269a719297941b099394aa23 | quote: 14 Days Free Trial All features. No credit card. No commitment.
  - [2] 2026-11-25: the four tiers are still 1, 5, 10 and 25 TB | capture: sha256:91d34c81e92486e6eb73b3527c5f81a0dd1b7c731f83b5fdc8c07bb27bff57bb | quote: | Cloud Storage | 1 TB | 5 TB | 10 TB | 25 TB |
  - [2] 2026-11-25: the per-file cap is 10 GB on all four tiers | capture: sha256:91d34c81e92486e6eb73b3527c5f81a0dd1b7c731f83b5fdc8c07bb27bff57bb | quote: | Max. file size | 10 GB | 10 GB | 10 GB | 10 GB |
  - [2] 2026-11-25: traffic is flatrate on all four tiers | capture: sha256:91d34c81e92486e6eb73b3527c5f81a0dd1b7c731f83b5fdc8c07bb27bff57bb | quote: | Traffic | Flatrate | Flatrate | Flatrate | Flatrate |
  - [2] 2026-11-25: the minimum term is one month | capture: sha256:91d34c81e92486e6eb73b3527c5f81a0dd1b7c731f83b5fdc8c07bb27bff57bb | quote: | Minimum term | 1 Month | 1 Month | 1 Month | 1 Month |
  - [1] 2026-11-25: the page advertises a 14-day free trial with all features, no credit card, and no commitment | capture: sha256:4128b72274dce249218e836c6bb8d665e68ae42d269a719297941b099394aa23 | quote: 14 Days Free Trial All features. No credit card. No commitment.
  - [1] 2026-11-25: the comparison table states a 10 GB max file size on all four tiers | capture: sha256:4128b72274dce249218e836c6bb8d665e68ae42d269a719297941b099394aa23 | quote: | Max. file size | 10 GB | 10 GB | 10 GB | 10 GB |
  - [1] 2026-11-25: the comparison table states flatrate traffic on all four tiers | capture: sha256:4128b72274dce249218e836c6bb8d665e68ae42d269a719297941b099394aa23 | quote: | Traffic | Flatrate | Flatrate | Flatrate | Flatrate |
  - [1] 2026-11-25: the comparison table states a one-month minimum term on all four tiers | capture: sha256:4128b72274dce249218e836c6bb8d665e68ae42d269a719297941b099394aa23 | quote: | Minimum term | 1 Month | 1 Month | 1 Month | 1 Month |
  - [1] 2026-11-25: the first-party Nextcloud page states a 14-day free trial with all features, no credit card and no commitment | capture: sha256:b9dd2191e69b0afb2cf87e01eb361639dbd0c905b4d4e6cd7dc2a3cf9d01919e | quote: 14 Days Free Trial All features. No credit card. No commitment.
  - [1] 2026-11-25: the first-party Nextcloud page states flatrate traffic for the offer | capture: sha256:b9dd2191e69b0afb2cf87e01eb361639dbd0c905b4d4e6cd7dc2a3cf9d01919e | quote: Unlimited users, traffic flatrate and 100% renewable energy.
- sources:
  - [1] https://serverdiscounter.com/en/nextcloud
  - [2] https://web.archive.org/web/20260809095924/http://serverdiscounter.com/en/nextcloud?provider=wayback
