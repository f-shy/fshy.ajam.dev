# ExtraVM

> extravm.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/extravm/ | JSON https://fshy.ajam.dev/api/v1/entity/extravm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ExtraVM

- `compute/extravm` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:06.322Z (live) | stale on 2026-12-08
- url https://extravm.com/vps
- price parsed USD 8/mo
- free tier: The 1 GB plan at USD 4.50 per month (1 core, 15 GB NVMe, 3 TB at 1 Gbps) is marked 'Sold Out' on the vendor's own plan table, so the cheapest plan the same table lets you order is the 2 GB tier: 1 core, 2 GB RAM, 30 GB NVMe, 5 TB a month at 1 Gbps, USD 8.00 per month. The table heading states 'This is the monthly traffic allocation and network port speed. We only limit outbound port speed, inbound is 10Gbps.' Locations offered: Dallas TX, Los Angeles CA, Miami FL, Secaucus NJ, Amsterdam NL, Singapore, Tokyo JP, Sydney AU. The tracker lists the 1 GB plan at USD 4.50 in Dallas, Miami and Los Angeles with no stock flag. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: monthly traffic allocation with only the outbound port speed limited; inbound is stated as 10 Gbps. No overage rate is published | metered: yes | free allowance: 5 TB a month on the 2 GB tier; 3 TB a month on the sold-out 1 GB tier | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): 5 TB a month on the cheapest orderable tier, outbound only, with inbound stated as unmetered at 10 Gbps; 30 GB of NVMe is the second wall and the 1 GB tier that would have carried 3 TB is sold out [1]
- limits note: 5 TB a month on the cheapest orderable tier, outbound only, with inbound stated as unmetered at 10 Gbps; 30 GB of NVMe is the second wall and the 1 GB tier that would have carried 3 TB is sold out
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with full kernel access, ISO install, Linux/Windows/BSD; SSH and a client dashboard, no public API documented on the page read
- composes with: at USD 8.00 the 2 GB tier is the cheapest way to get 5 TB a month out of a US host among evaluated providers; it suits a crawler that needs to send bulk bytes from a US address.
- reliability: no reliability event recorded
- notes: The tracker reports the 1 GB plan as currently offered and the vendor marks it sold out on the day of reading, so this record prices the 2 GB tier instead and keeps the USD 4.50 row in evidence. That is a stock disagreement, not a withdrawal, so the verdict is not dead. Only the 2 GB, 3 GB, 4 GB, 5 GB and 6 GB rows carry an order button; every tier from 8 GB up is sold out. verification criteria: the overage charge and whether the 3 TB and 5 TB figures are outbound only in practice.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - price_on_page: USD 8.00/month: the 2 GB tier, the cheapest the plan table lets you order (the 1 GB tier at USD 4.50 is marked Sold Out)
  - renewal_note: not published: the vendor's own VPS page read on 2026-11-07 prints a monthly price per tier and no renewal price
- evidence:
  - [1] 2026-10-22: plan table rows quoted: '1 GB RAM / 1 Core / 15 GB NVMe / 3 TB - 1Gbps / $4.50 /mo / Sold Out' and '2 GB RAM / 1 Core / 30 GB NVMe / 5 TB - 1Gbps / $8.00 /mo / Order'
  - [1] 2026-10-22: column note quoted: 'This is the monthly traffic allocation and network port speed. We only limit outbound port speed, inbound is 10Gbps.'
  - [2] 2026-10-22: row quoted from the Cheapest VPSs table: 'USD 4.50 / month', '1 Ryzen Cores (shared)', '1,024 MB RAM', '15 GB NVMe', '3,072 GB/month bandwidth', '1 Gbps port speed', 'Dallas Texas U.S.A.'
  - [1] 2026-11-07: the plan table prices the 1 GB tier at $4.50 a month marked Sold Out and the 2 GB tier at $8.00 a month with an Order button | capture: sha256:5b663ff1f8b86917b5855cb548715d2b3aac3de3a003d3f2427b379879af4a0d | quote: | 1 GB RAM | 1 Core | 15 GB NVMe | 3 TB - 1Gbps | | $4.50 /mo | Sold Out | | 2 GB RAM | 1 Core | 30 GB NVMe | 5 TB - 1Gbps | | $8.00 /mo | [Order](https://extravm.com/billing/store/kvm-nvme-vps-dallas-tx/2gb-ram-dallas) |
- sources:
  - [1] https://extravm.com/vps
  - [2] https://vpspricetracker.com/provider/ExtraVM/vps
