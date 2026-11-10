# TierNet

> tier.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tier/ | JSON https://fshy.ajam.dev/api/v1/entity/tier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TierNet

- `compute/tiernet` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:42.898Z (live) | stale on 2026-12-08
- url https://www.tier.net/vps
- price parsed USD 8.99/mo
- free tier: VPS Bronze at USD 8.99/month: 1 core, 4 GB RAM, 30 GB SSD RAID 10, 2 TB at 1 Gbps, 1 IPv4 plus a /64 IPv6, sold in three US regions that the tracker names as Dallas Texas, Bend Oregon and Charlotte North Carolina. At the same USD 8.99 the Powerhouse Mini gives 1 core, 4 GB, 50 GB SSD RAID 10 and 1 TB. The billing store's current plan group lists the Bronze at 'From $8.99/mo'. No annual price and no renewal price are printed on the pages read. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month at 1 Gbps on the Bronze, 1 TB on the Powerhouse Mini; the page states no overage price and no throttle | metered: yes | free allowance: 2 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month at 1 Gbps is stated on the Bronze card; 1 TB on the Powerhouse Mini at the same price. No overage rate is published on the page read [1]
- limits note: 2 TB a month at 1 Gbps is stated on the Bronze card; 1 TB on the Powerhouse Mini at the same price. No overage rate is published on the page read
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: the plan table names a 'Simple Management' and an 'Ultimate Management' add-on at USD 15 a month and a cPanel add-on at USD 21, but no API, and the panel product is not named
- composes with: 4 GB for USD 8.99 with a stated 2 TB allowance at a named 1 Gbps port, in three US regions the tracker lists, suits a US-region crawl worker or a build node that has to know its port speed before it orders
- reliability: no reliability event recorded
- notes: Two pricing inconsistencies on the vendor page, recorded rather than resolved: the hero says USD 7.49 while the cheapest card is USD 8.99, and the promo block still advertises a code that expired on 31 May 2025, which is evidence the page carries stale campaign text. The 7-day money-back guarantee is stated on every card. Unverified: whether USD 7.49 is the annual-term rate that the page's billing-cycle tabs hide from a text read. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 30
  - price_on_page: USD 8.99/month for VPS Bronze
- evidence:
  - [2] 2026-10-22: cheapest row repeated for three locations: 'TierNet - USD 8.99 / month', '1 Intel Cores (shared)', '4,096 MB RAM', '30 GB SSD', '2,048 GB/month bandwidth', '1 Gbps port speed', 'Dallas Texas', 'Bend Oregon', 'Charlotte North Carolina'
  - [1] 2026-10-22: Premium table 'VPS Bronze' card, quoted: 'USD 8.99 /per month', 'Cores: 1', '4GB', '30GB SSD RAID 10', '2TB @ 1Gbps', '1x IPv4, /64 IPv6'; the table is headed 'ALL PRICES ARE IN USD'
  - [1] 2026-10-22: Powerhouse 'Mini' card at 'USD 8.99 /month' with 'Cores: 1', '4GB', '50GB SSD RAID 10', '1TB @ 1Gbps'; the next Premium card is USD 12.99 with 2 cores, 6 GB, 50 GB, 4 TB
  - [1] 2026-10-22: the page header says 'Starting from USD 7.49 /mo' and 'VPS Hosting - From USD 7.49/mo', which no plan card on the page repeats; the page also carries the promo text 'TIER-VPS10 ... Valid till May 31, 2025'
  - [1] 2026-11-07: the Bronze card still prices USD 8.99 per month with the same shape, and the capture holds no 7.49 header line | capture: sha256:1a79fcc6758a899a0b0c24efab2f1cac03e78a35943bc8e179178ad8f34b3bc9 | quote: ## VPS Bronze #### $8.99/per month
  - [1] 2026-11-07: the Bronze card is unchanged at USD 8.99 per month | capture: sha256:1a79fcc6758a899a0b0c24efab2f1cac03e78a35943bc8e179178ad8f34b3bc9 | quote: ## VPS Bronze #### $8.99/per month
- sources:
  - [1] https://www.tier.net/vps
  - [2] https://vpspricetracker.com/provider/TierNet/vps
