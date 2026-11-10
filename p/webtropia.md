# Webtropia Storage Server RYZ5-20

> webtropia.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webtropia/ | JSON https://fshy.ajam.dev/api/v1/entity/webtropia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webtropia Storage Server RYZ5-20 (4× 22 TB)

- `storage/webtropia-storage-server-ryz5-20` | qualifies-with-caveat | evidence reported | binding none | category dedicated storage server
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.webtropia.com/en/amd-storage-server.html
- price RYZ5-20 €109.99 ÷ 88 TB = €1.25/TB/mo raw ≈$1.45 — the lowest €/TB of the storage providers compared. RYZ5-12 €79.99 ÷ 56 TB = €1.43/TB. RYZ7-20 €119.99 ÷ 88 = €1.36/TB. Caveat: egress term unpublished; treat as unverified until confirmed in writing. | parsed USD 1.41/TB-mo
- free tier: 4× 22 TB = 88 TB raw (RYZ5-12: 4× 14 TB = 56 TB, €79.99) | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: NOT STATED on the product page. What is published is bandwidth shape only: 'Peak Bandwidth 1.000 MBit / Guaranteed bandwidth 300 MBit'. No traffic volume, no unlimited claim, no overage rate. This is the one number that decides whether the €1.25/TB headline is real. | metered: yes | price per TB: €1.25/TB
- identity: email | detail: email
- interface: unknown
- limits note: Guaranteed bandwidth is only 300 Mbit (peak 1 Gbit). At 300 Mbit sustained the theoretical monthly ceiling is ~97 TB, so even 'unlimited' would be shaped well below Hetzner's 1 Gbit. Setup €0.00. Windows +€31/mo, CloudLinux +€12/mo.
- interface detail: full root
- tooling: unrestricted
- composes with: as any dedicated server
- reliability: Cheapest raw €/TB found in Europe, but the traffic term is unverified. Do not commit without a ticket. German provider (webtropia.com / Host Europe group lineage).
- notes: the same as the free tier
- extras:
  - price_verbatim: RYZ5-20 €109.99 ÷ 88 TB = €1.25/TB/mo raw ≈$1.45 — the lowest €/TB of the storage providers compared. RYZ5-12 €79.99 ÷ 56 TB = €1.43/TB. RYZ7-20 €119.99 ÷ 88 = €1.36/TB. Caveat: egress term unpublished; treat as unverified until confirmed in writing.
- evidence:
  - [1] 2026-10-21: RYZ5-12 €79.99, RYZ7-12 €89.99, RYZ5-20 €109.99, RYZ7-20 €119.99 per month; '2 x 240 GB SSD or 4 x 14 TB' / '4 x 22 TB'; setup €0.00
  - withheld 2026-10-21: same page — 'Peak Bandwidth 1.000 MBit', 'Guaranteed bandwidth 300 MBit', no traffic volume row anywhere in the table
  - [2] 2026-10-21: 'from 87.99 €', 'up to 4x 22 TB Enterprise HDDs', branded WD/Seagate drives
- sources:
  - [1] https://www.webtropia.com/en/amd-storage-server.html
  - [2] https://www.webtropia.com/en/dedicated-storage-server.html
