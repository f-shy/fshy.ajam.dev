# SmokyHosts

> smokyhosts.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/smokyhosts/ | JSON https://fshy.ajam.dev/api/v1/entity/smokyhosts.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SmokyHosts

- `compute/smokyhosts` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://smokyhosts.com/vps/
- free tier: Mini VPS at USD 2.95/month: 1 vCPU, 1 GB RAM, 10 GB SSD, 100 GB bandwidth, 1 Gbps port, 1 IPv4, IPv6 only on request, Buffalo USA. Size S is USD 4.95 with 2 GB RAM, 20 GB SSD and 400 GB bandwidth. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 100 GB per month on the entry plan; overage is not priced on the page read | metered: yes | free allowance: 100 GB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 100 GB a month on the entry plan is the smallest allowance among documented hosts [1]
- limits note: 100 GB a month on the entry plan is the smallest allowance among documented hosts
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM; the site lists Classic, Premium NVMe, 10Gbps, Storage, IPv6-only and IPv6-only storage ranges, no API mentioned
- composes with: 100 GB a month rules it out as a scraper front end; it fits a DNS, monitor or bastion box where the traffic is small and the port is never the point
- reliability: no reliability event recorded
- notes: The tracker says 500 GB and Kansas for the USD 2.95 row; the vendor page read says 100 GB and Buffalo. The vendor page is the record, and the fivefold gap in the bandwidth figure is exactly the kind of error the tracker's per-provider pages carry, so re-read before quoting either. Unverified: whether IPv6 really is issued only on request, which the card states twice.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-22: 'Mini VPS, Buffalo, USA, 1vCPU, 1GB RAM, 1 IPv4 Address, No IPv6 address on request, 10GB SSD storage, 100GB Bandwidth, 1Gbps, $2.95 /month, Order Now', quoted from the plan card
  - [1] 2026-10-22: 'Size S VPS, Buffalo, USA, 1vCPU, 2GB RAM, 20GB SSD storage, 400GB Bandwidth, $4.95 /month'; a Kansas City Size S is also listed at the same USD 4.95 with 400 GB
  - [2] 2026-10-22: tracker row 'USD 2.95 / month, 1 Intel Cores (shared), 1,024 MB RAM, 10 GB SSD, 500 GB/month bandwidth, 1 Gbps port speed, IPv6, Kansas U.S.A.'
- sources:
  - [1] https://smokyhosts.com/vps/
  - [2] https://vpspricetracker.com/provider/SmokyHosts/vps
