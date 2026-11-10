# RakSmart

> raksmart.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/raksmart/ | JSON https://fshy.ajam.dev/api/v1/entity/raksmart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RakSmart

- `compute/raksmart` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.raksmart.com/
- free tier: USD 2.99 per month list, USD 1.99 during the flash weeks of 11-17 and 25-30 November 2026, for a Silicon Valley VPS with 2 GB RAM, 2 cores, 50 GB HDD, 10 TB a month and a 5 Gbps international BGP port. The mainland-optimised variant of the same shape carries 3 TB a month at the same price; the premium CN2 variant carries 1 TB a month at USD 4.99 list and USD 3.99 flash. Hong Kong is a 1 GB / 1 core / 50 GB / 3 TB row at USD 2.99 list and USD 1.99 flash. Annual rows start at USD 49.90 for 4 GB, 2 cores, 50 GB NVMe and 10 TB. The promotion runs 15 October to 30 November and returns to list price on 1 December. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 TB a month on international BGP, 3 TB on mainland-optimised, 1 TB on CN2, all on ports up to 5 Gbps; no overage price stated | metered: yes | free allowance: 10 TB per month on the international BGP row | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 10 TB a month on the international BGP row, 3 TB on the mainland-optimised row and 1 TB on the CN2 row at the same or a higher price, so the network choice is what sets the allowance; the 5 Gbps port is not reachable within 10 TB a month. [1]
- limits note: 10 TB a month on the international BGP row, 3 TB on the mainland-optimised row and 1 TB on the CN2 row at the same or a higher price, so the network choice is what sets the allowance; the 5 Gbps port is not reachable within 10 TB a month.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: crypto payment accepted per the vendor homepage; no API documented on the page read
- composes with: 10 TB a month, 2 cores and a 5 Gbps port at USD 1.99 for a fortnightly window is the cheapest transfer shape in the Chinese lane, and the flash window is the only time that price exists
- reliability: no reliability event recorded
- notes: RAKsmart offers VPS hosting with promotional pricing from USD 1.99 to USD 5.00 monthly, with payment options including cryptocurrency, credit cards, and PayPal.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 50
- evidence:
  - [2] 2026-10-23: plan table quoted: '硅谷 | 2G | 2核 | 50G HDD | 10T/月 | 5G国际BGP | $2.99/月 | $1.99/月'; '硅谷 | 2G | 2核 | 50G HDD | 3T/月 | 5G大陆优化 | $2.99/月 | $1.99/月'; '香港 | 1G | 1核 | 50G HDD | 3T/月 | 1G国际BGP | $2.99/月 | $1.99/月'; 'VPS促销时间：10月15日-11月30日'
  - [1] 2026-10-23: vendor homepage read renders no VPS price table: it carries 'Multi-IP clusters from $80/mo', '100+ Cryptos supported', '1-Click App deployment' and no plan row
- sources:
  - [1] https://www.raksmart.com/
  - [2] https://www.zhujiceping.com/100898.html
