# Webtropia Storage Server RYZ5-20

> webtropia.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webtropia/ | JSON https://fshy.ajam.dev/api/v1/entity/webtropia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webtropia Storage Server RYZ5-20 (4× 22 TB)

- `storage/webtropia-storage-server-ryz5-20` | qualifies-with-caveat | evidence reported | binding none | category dedicated storage server
- needs card no, phone no, ID no, institution no | verified 2026-11-25T13:25:54.293Z (live) | stale on 2026-12-10
- url https://www.webtropia.com/en/amd-storage-server.html
- price EUR 1.37 per TB per month (EUR 120.99 per month for 88 TB raw on the RYZ5-20) | parsed USD 1.54/TB-mo
- free tier: 4× 22 TB = 88 TB raw (RYZ5-12: 4× 14 TB = 56 TB, €79.99) | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: No per-object cap is stated on the product page; the offer is raw dedicated disks (2 x 240 GB SSD or 4 x 22 TB).
- retention: source: [1] | note: No retention term is stated on the product page; the disks are dedicated, and full root access allows the renter to manage files.
- egress: Dedicated servers include unlimited traffic on a 1,000 Mbit connection with a guaranteed 300 Mbit. | metered: no | price per TB: unverified: no per-TB traffic charge is listed for dedicated servers
- identity: email | detail: email
- interface: ssh
- limits note: Guaranteed bandwidth is only 300 Mbit (peak 1 Gbit). At 300 Mbit sustained the theoretical monthly ceiling is ~97 TB, so even 'unlimited' would be shaped well below Hetzner's 1 Gbit. Setup €0.00. Windows +€31/mo, CloudLinux +€12/mo.
- interface detail: full root
- tooling: unrestricted
- composes with: as any dedicated server
- reliability: Cheapest raw €/TB found in Europe, but the traffic term is unverified. Do not commit without a ticket. German provider (webtropia.com / Host Europe group lineage).
- notes: the same as the free tier
- evidence note: the monthly price is quoted from the first-party product section; the traffic term is not stated there, which holds the rung at reported
- extras:
  - price_verbatim: RYZ5-20 €109.99 ÷ 88 TB = €1.25/TB/mo raw ≈$1.45 — the lowest €/TB of the storage providers compared. RYZ5-12 €79.99 ÷ 56 TB = €1.43/TB. RYZ7-20 €119.99 ÷ 88 = €1.36/TB. Caveat: egress term unpublished; treat as unverified until confirmed in writing.
- evidence:
  - [1] 2026-10-21: RYZ5-12 €79.99, RYZ7-12 €89.99, RYZ5-20 €109.99, RYZ7-20 €119.99 per month; '2 x 240 GB SSD or 4 x 14 TB' / '4 x 22 TB'; setup €0.00
  - withheld 2026-10-21: same page — 'Peak Bandwidth 1.000 MBit', 'Guaranteed bandwidth 300 MBit', no traffic volume row anywhere in the table
  - [2] 2026-10-21: 'from 87.99 €', 'up to 4x 22 TB Enterprise HDDs', branded WD/Seagate drives
  - [1] 2026-11-10: the product section lists the RYZ5-20 with 4 x 22 TB and EUR 120.99 per month | capture: sha256:74c8288c1a52c06fbd3e4665a9ea445caca4c743a1324e4b2fe8b45c6848e50a | quote: ## Storage Server RYZ5-20 AMD RYZEN 5 3600 - 4 x 3,6 GHz 32 GB DDR4 RAM 2 x 240 GB SSD or 4 x 22 TB Linux or Windows Server 120,99 € per month
  - [1] 2026-11-10: the page states the monthly price the basis names | capture: sha256:74c8288c1a52c06fbd3e4665a9ea445caca4c743a1324e4b2fe8b45c6848e50a | quote: Storage Server RYZ5-20 120,99 €
  - [1] 2026-11-25: the product page offers full root access | capture: sha256:74c8288c1a52c06fbd3e4665a9ea445caca4c743a1324e4b2fe8b45c6848e50a | quote: With root access, adjustments can be made that would not be possible with shared hardware
  - [1] 2026-11-25: the product is raw dedicated disks | capture: sha256:74c8288c1a52c06fbd3e4665a9ea445caca4c743a1324e4b2fe8b45c6848e50a | quote: 2 x 240 GB SSD or 4 x 22 TB
  - [3] 2026-11-25: dedicated-server traffic is unlimited, with a 300 Mbit guarantee and no overage column | capture: sha256:a5b7bf116d45a58c704ac420d5d1f9f1c8aa3bf970f3f3cbfcfd5918ce789735 | quote: | DEDICATED SERVER | 1,000 Mbit | 300 Mbit | Unlimited | - |
- sources:
  - [1] https://www.webtropia.com/en/amd-storage-server.html
  - [2] https://www.webtropia.com/en/dedicated-storage-server.html
  - [3] https://www.webtropia.com/en/technology/connection.html
