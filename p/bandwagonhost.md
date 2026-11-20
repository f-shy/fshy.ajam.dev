# BandwagonHost

> bandwagonhost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bandwagonhost/ | JSON https://fshy.ajam.dev/api/v1/entity/bandwagonhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BandwagonHost

- `compute/bandwagonhost` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://bandwagonhost.com/
- free tier: The host most often named in Chinese-language forums, quoted from its own front page: 20G KVM VPS with 20 GB RAID-10 SSD, 1 GiB RAM, 2 vCPU and 1 TB a month on a 1 Gbps port at USD 49.99 a year; 40G KVM at 2 GiB and 2 TB for USD 52.99 per half-year; 80G at 4 GiB and 3 TB for USD 19.99 a month; and a 320G shape at 16 GiB, 6 vCPU and 5 TB for USD 79.99 a month. Every plan allows datacenter migration, snapshots, rDNS and API access from its own KiwiVM panel. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Not established on 2026-10-22. The provider is US-registered and sells in USD, and the front page states no verification requirement.
- interface: rest
- limits:
  - volume-quota (binding): One terabyte a month is the term that binds, and the plan is annual, so an overrun is corrected only at renewal. The plan is unmanaged: the vendor states self-managed KVM, so a broken image is the buyer's problem and there is no managed support tier at this price. [1]
- limits note: One terabyte a month is the term that binds, and the plan is annual, so an overrun is corrected only at renewal. The plan is unmanaged: the vendor states self-managed KVM, so a broken image is the buyer's problem and there is no managed support tier at this price.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The datacenter-migration feature is worth more than the price: a box that can be moved between locations without reinstalling is the cheapest way to test which region a workload actually needs.
- reliability: no reliability event recorded
- notes: USD 49.99 a year is not the floor (DediOne at USD 3.99 a month and Tencent at CNY 99 a year are both cheaper), so this is recorded as the reference mid-price annual host with a migration feature, not as a bargain. The CN2 GIA plans that Chinese buyers actually pay for are on a separate store and were not read.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: front page lists 20G KVM VPS with 20 GB SSD, 1024 MB RAM, 2x CPU, 1 TB/mo, 1 Gbps at $49.99/year, quoted
  - [1] 2026-10-22: the 320G shape is 320 GB SSD, 16 GB RAM, 6x CPU, 5 TB/mo at $79.99/month, quoted
  - [1] 2026-10-22: the page states the service is self-managed KVM on KiwiVM with snapshots, datacenter migration, rDNS and API
- sources:
  - [1] https://bandwagonhost.com/
