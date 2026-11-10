# Serverdiscounter NEXT Share

> serverdiscounter.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serverdiscounter/ | JSON https://fshy.ajam.dev/api/v1/entity/serverdiscounter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Serverdiscounter NEXT Share (managed Nextcloud)

- `netdisk-pan/serverdiscounter-next-share` | qualifies | evidence documented | binding per-object-cap | category managed Nextcloud, paid only
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T04:06:37.166Z (live) | stale on 2026-11-13
- url https://serverdiscounter.com/en/nextcloud
- price EUR 2.40/TB/month including VAT at 25 TB (EUR 59.95/month), rising to EUR 4.95/TB/month at 1 TB, read 2026-10-22 | parsed USD 2.7/TB-mo
- free tier: No free tier. A 14-day free trial with no credit card and 'no commitment', which is deleted at the end unless extended. Plans: Small 1 TB at EUR 4.95/month including VAT, Basic 5 TB at EUR 15.95, Grow 10 TB at EUR 29.95, Big 25 TB at EUR 59.95 | unit: TiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
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
- sources:
  - [1] https://serverdiscounter.com/en/nextcloud
