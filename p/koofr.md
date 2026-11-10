# Koofr

> koofr.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/koofr/ | JSON https://fshy.ajam.dev/api/v1/entity/koofr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Koofr (Suitcase XL+ 500 GB / 5 TB 5XXL)

- `storage/koofr` | fails-quota | evidence reported | binding none | category Slovenian cloud drive, subscription + StackSocial lifetime
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://koofr.eu/pricing/
- price $7.86/TB at 5 TB (EUR 35 = $39.32); $7.86/TB at 2.5 TB; $11.23/TB at 1 TB. Lifetime 1 TB $159.99 = $159.99/TB one-time, or $2.67/TB/mo over 5 years. | parsed USD 7.86/TB-mo
- free tier: Briefcase 10/25/100 GB at EUR 0.5/1/2 per mo; Suitcase 250 GB EUR 4, 500 GB EUR 7, 1 TB EUR 10; Crate 2.5 TB EUR 20, 5 TB EUR 35; 10 TB+ on request | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered by tier on PUBLIC transfers only, daily: '200 GB daily public transfer limit' (Briefcase), '1 TB daily public transfer limit' (Suitcase XL/XL+/XXL), '4 TB daily public transfer limit' (Crate). At the 5 TB tier that is ~30 TB/mo. Private/rclone traffic is not stated as capped. | metered: yes | free allowance: 30 TB per month
- identity: email | detail: email
- interface: webdav, rclone
- limits note: Constraint type: per-ip-shaping on public links, daily granularity
- interface detail: rclone native `koofr` backend (Tier 2, added v1.47), WebDAV, app passwords
- tooling: rclone native; WebDAV endpoint at app.koofr.net (probed: /api/v2.1/user returns 401 = live, auth required)
- composes with: rclone -> anywhere; also aggregates 30 external cloud connections on the top tier
- reliability: Operated since 2012, Slovenian/EU. No data-loss event documented. Lifetime deal is sold through StackSocial ($159.99 with code KOOFR, 10k+ sold), not by Koofr directly, so entitlement rests on a third-party marketplace SKU.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Briefcase 10/25/100 GB at EUR 0.5/1/2 per mo; Suitcase 250 GB EUR 4, 500 GB EUR 7, 1 TB EUR 10; Crate 2.5 TB EUR 20, 5 TB EUR 35; 10 TB+ on request
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $7.86/TB at 5 TB (EUR 35 = $39.32); $7.86/TB at 2.5 TB; $11.23/TB at 1 TB. Lifetime 1 TB $159.99 = $159.99/TB one-time, or $2.67/TB/mo over 5 years.
- evidence:
  - [1] 2026-10-21: 'Suitcase ... 500 GB XL+ 7 EUR /mo ... 1 TB XXL 10 EUR /mo'; 'Crate 2.5 TB XXXL 20 EUR /mo 5 TB 5XXL 35 EUR /mo 10 TB and up'
  - [1] 2026-10-21: '1 TB daily public transfer limit' on Suitcase tiers; '4 TB daily public transfer limit' on Crate
  - [2] 2026-10-21: native backend, Tier 2, requires an app password
  - [3] 2026-10-21: 'Coupon Price $159.99 with code KOOFR ... Deal Price $199.99 ... 10k+ Sold'
- sources:
  - [1] https://koofr.eu/pricing/
  - [2] https://rclone.org/koofr/
  - [3] https://www.stacksocial.com/sales/koofr-cloud-storage-plans-lifetime-subscription-1tb
