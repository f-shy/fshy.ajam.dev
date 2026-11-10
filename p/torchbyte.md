# Torchbyte

> torchbyte.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/torchbyte/ | JSON https://fshy.ajam.dev/api/v1/entity/torchbyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Torchbyte

- `compute/torchbyte` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://torchbyte.com/vps
- free tier: Game VPS Start at EUR 4.65/month: 1 vCPU (AMD Ryzen 9), 2 GB DDR4, 30 GB NVMe, 10 Gbit/s unmetered, Bucharest Romania. The next plan is EUR 9.50/month with 2 vCPU, 4 GB and 80 GB, and the Enterprise line starts at EUR 9.60 with 2 vCPU (Xeon Gold), 4 GB and 60 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unmetered: 'no traffic caps and no bandwidth billing' on a 10 Gbit/s port; no price per TB exists because no allowance is sold | metered: no | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits note: the vendor states no byte allowance: 'Every node uplinks at 10 Gbit/s with no traffic caps and no bandwidth billing', so the first limit is the disk and not the network. The tracker lists 50,000 GB a month, which the vendor page contradicts
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the page names a VPS control panel and a billing portal at billing.torchbyte.com, with root access over SSH or RDP; no API is documented on the page read
- composes with: unmetered 10 Gbit/s with 2 GB and a Ryzen 9 core for EUR 4.65 makes this one of two hosts among documented hosts whose network is not a byte meter (Ultahost is the other) and the only one of the two on a 10 Gbit/s port, so it fits a fan-out crawler or a mirror whose cost is bytes rather than CPU
- reliability: no reliability event recorded
- notes: The tracker's 50,000 GB a month is not on the vendor page, which states the opposite; the record takes the vendor. A second unresolved internal disagreement is recorded rather than smoothed: the pricing page says prices include 21 percent VAT while the /vps structured data marks the same EUR 4.65 with valueAddedTaxIncluded false. Unverified: whether 'unmetered' survives a sustained multi-terabyte month, which only an order would show. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
- evidence:
  - [2] 2026-10-22: cheapest row: 'Torchbyte - EUR 4.65 / month', '1 Ryzen Cores (shared)', '2,048 MB RAM', '30 GB NVMe', '50,000 GB/month bandwidth', '10 Gbps port speed', 'Bucharest Romania'
  - [1] 2026-10-22: structured product data for the entry VPS, quoted: 'Game VPS Start', 'price EUR 4.65', 'description: 1 vCPU (AMD Ryzen 9), 2 GB DDR4 RAM, 30 GB NVMe, 10 Gbit/s unmetered, DDoS protection included', 'availability: InStock'
  - [1] 2026-10-22: structured product data for the rest of the ladder, quoted: 'Game VPS Basic' at 'price 9.50' with '2 vCPU (AMD Ryzen 9), 4 GB DDR4 RAM, 80 GB NVMe', and the Enterprise line's entry plan at 'price 9.60' with '2 vCPU (Intel Xeon Gold), 4 GB DDR4 RAM, 60 GB NVMe'
  - [1] 2026-10-22: 'Every node uplinks at 10 Gbit/s with no traffic caps and no bandwidth billing', and the page badge reads '10 Gbit/s unmetered'
  - [3] 2026-10-22: 'Billed monthly, EUR incl. 21% VAT', 'No setup fees', '48h money-back guarantee'; the VPS line is listed 'from EUR 4.65/mo' and the game-server line 'from EUR 4.74/mo'
- sources:
  - [1] https://torchbyte.com/vps
  - [2] https://vpspricetracker.com/provider/Torchbyte/vps
  - [3] https://torchbyte.com/pricing
