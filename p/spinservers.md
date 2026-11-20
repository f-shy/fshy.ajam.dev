# SpinServers

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spinservers/ | JSON https://fshy.ajam.dev/api/v1/entity/spinservers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SpinServers

- `compute/spinservers` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.serverhunter.com/offer/spinservers-dual-xeon-e5-2670-32gb-ram-1tb-hdd/
- free tier: USD 79.00/month for a dual-socket machine in Carrollton, Texas: 2x Intel Xeon E5-2670 at 2.6 GHz, 32 GB DDR3, 1 TB HDD, 1,000 Mbit uplink, 20 TB traffic, no setup fee, listed in stock. The row's product type is 'Hybrid' with virtualization 'None'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 20 TB a month per the tracker row, on a 1,000 Mbit uplink. No overage price is stated | metered: yes | free allowance: 20 TB per month | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 20 TB a month is the allowance on the row. At the stated 1,000 Mbit port that is about 44 hours of line-rate traffic if the 20 TB is decimal, so the month's counter is reachable and is the wall a crawler meets; no overage price is stated. [1]
- limits note: 20 TB a month is the allowance on the row. At the stated 1,000 Mbit port that is about 44 hours of line-rate traffic if the 20 TB is decimal, so the month's counter is reachable and is the wall a crawler meets; no overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the pages read
- composes with: Kimsufi at USD 19.90 with 32 GB and a 300 Mbps port is still the cheaper machine, and SpinServers' edge is the 20 TB and the 1 Gbit port, not the price
- reliability: no reliability event recorded
- notes: Found via serverhunter. The core count on the row reads '4 cores' for '2x Intel Xeon E5-2670', which is one core per socket on a dual-socket server part; that is treated as an aggregator artifact and the thread count is unverified, so shape.vcpu carries the row's number rather than a corrected one. Unverified: the vendor's order page for the same configuration, which would also give the disk count and the RAID level.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 32
  - facets.shape.disk_gib: 1024
- evidence:
  - [1] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Monthly price USD 79.00, 'Product type Hybrid', 'Virtualization type None', 'Stock In stock', 'Processor cores 4 cores', 'Processor speed 2.6 GHz', 'Processor 2x Intel Xeon E5-2670', 'Memory amount 32 GB', 'Memory type DDR3', 'Total HDD Capacity 1 TB', 'Uplink 1,000 Mbit', 'Traffic 20 TB', 'Location Carrollton, Texas, United States of America'
  - [2] 2026-10-22: the vendor homepage returns 200 and describes 'Spin Servers is a wholesale provider of instant and dedicated servers in the USA' with no plan table in the extract; https://www.spinservers.com/pricing/ returned a 404 body
  - [3] 2026-10-22: the provider page lists twelve dedicated and hybrid configurations from Dual Intel Xeon E5-2670 32GB RAM 1TB HDD to Dual Intel Xeon E5-2696 v3 512GB DDR4 Pre-order
- sources:
  - [1] https://www.serverhunter.com/offer/spinservers-dual-xeon-e5-2670-32gb-ram-1tb-hdd/
  - [2] https://www.spinservers.com/
  - [3] https://www.serverhunter.com/company/spinservers/
