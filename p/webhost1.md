# WebHOST1

> webhost1.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webhost1/ | JSON https://fshy.ajam.dev/api/v1/entity/webhost1.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WebHOST1

- `compute/webhost1` | trial-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://webhost1.ru/vps-vds/test
- free tier: Two free routes rather than a free tier. The first is a 30-day money-back trial: an individual registers, fills the profile, pays for the chosen tariff, and may claim a full refund inside 30 days, once per account, on any tariff except the promo ones; from the second month the refund covers only the unspent remainder. The second is 60 days free, described as two months at no charge, when moving from another hosting company. Legal entities instead send a taxpayer-number scan and a letter on company letterhead to obtain a 30-day test. The cheapest paid shape is the USA or Netherlands SSD 20 plan at RUB 336 a month list, RUB 285.60 a month on the annual term (RUB 4,032 list for 12 months, RUB 3,427.20 discounted), for one core at 2.8 GHz, 2 GB RAM, 20 GB disk and a 100 Mbit/s port. Foreign bank cards are accepted through the Robokassa gateway with a minimum payment of RUB 1,000, and the provider names the countries whose cards it will not take. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: money-back-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a paid order up front and a card to make it, because the trial is a refund rather than a free period: 'individuals pay for the service and get a 100 percent refund within 30 days once per account'. Payment runs through Robokassa, which takes foreign bank cards with a minimum of RUB 1,000, and the vendor lists the countries whose cards it refuses, including Azerbaijan, the United States, Ukraine, Turkey and Venezuela. No hold amount is stated, and whether a debit or prepaid card is accepted is not stated. A legal entity instead sends a taxpayer-number scan and a company letter for a 30-day test.
- interface: unknown
- limits:
  - per-ip-shaping (binding): The 100 Mbit/s port is the ceiling on every tariff up to the top of the range, so a 24/7 transfer job tops out at about 1.08 TB a day before anything else binds; the free part is a refund window rather than capacity, and it is once per account. [1]
- limits note: The 100 Mbit/s port is the ceiling on every tariff up to the top of the range, so a 24/7 transfer job tops out at about 1.08 TB a day before anything else binds; the free part is a refund window rather than capacity, and it is once per account.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A foreign-card payment path plus a refund window is the useful composition: RUB 1,000 is the minimum top-up and covers 3.5 months of the cheapest plan, so a 30-day paid month that is then refunded costs a card authorisation and nothing else, and the migration route adds a second free 60 days if there is an older invoice to show.
- reliability: no reliability event recorded
- notes: The 'free VPS on 60 days' banner is a migration offer, not a tier: it needs an existing service elsewhere, which is a real constraint rather than a detail. Arithmetic: 336 x 12 = 4,032; 285.60 x 12 = 3,427.20; 1,000 / 285.60 = 3.5 months. Not established: whether the refund is paid back to a foreign card or only to the internal balance, and whether the migration offer requires proof of the previous invoice.
- extras:
  - facets.class: regional-low-floor
  - facets.free_tier_kind: money-back-trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 20
  - facets.shape.port_mbit: 100
- evidence:
  - [1] 2026-10-22: individuals pay for the service and get a 100 percent refund within 30 days once per account, legal entities send a taxpayer-number scan and a company letter for a 30-day test, and migration from another host gives two months free, quoted and translated
  - [2] 2026-10-22: RU SSD 20 at RUB 285.60 a month for 1 core at 2.8 GHz, 2 GB RAM, 20 GB disk and a 100 Mbit/s port, listed at RUB 4,032 for 12 months before a 15 percent discount to RUB 3,427.20; extra IP RUB 157.50 a month, +1 GB RAM RUB 300 a month, +1 core RUB 300 a month, quoted
  - [3] 2026-10-22: payment through Robokassa includes foreign bank cards with a minimum of RUB 1,000, the commission was removed, and the article lists the countries whose cards are refused, including Azerbaijan, the United States, Ukraine, Turkey and Venezuela, quoted and translated
- sources:
  - [1] https://webhost1.ru/vps-vds/test
  - [2] https://webhost1.ru/vds/ssd/vps-vds-ru
  - [3] https://webhost1.ru/help/articles/general-information/webhost1-oplata-serverov-cherez-robokassa-teper-bez-komissii.html
