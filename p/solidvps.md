# SolidVPS

> solidvps.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/solidvps/ | JSON https://fshy.ajam.dev/api/v1/entity/solidvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SolidVPS

- `compute/solidvps` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:41.346Z (live) | stale on 2026-12-08
- url https://solidvps.com/starter-kvm-cloud-vps.php
- price parsed USD 5.95/mo
- free tier: LNX-CS-2GB at USD 5.95/month: 1 vCore, 2 GB RAM, 20 GB NVMe RAID 10, 1 TB at 10 Gbps, Tampa Florida. LNX-CS-4GB is USD 9.95 with 2 vCores, 4 GB and 40 GB; the storage range starts at USD 6.95 and the budget range at USD 40/year. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB per month on the entry plan; overage is not priced on the page read | metered: yes | free allowance: 1 TB per month | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 1 TB a month on a 10 Gbps port, so the port can empty the allowance in under a day [1]
- limits note: 1 TB a month on a 10 Gbps port, so the port can empty the allowance in under a day
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: Virtualizor panel with VNC console, custom ISO, rDNS control and daily backups; cPanel or DirectAdmin offered as the panel choice
- composes with: 20 GB of NVMe at USD 5.95 in Tampa is a small service host; the storage range at USD 6.95 with up to 2 TB is the row to use when the job is retention
- reliability: no reliability event recorded
- notes: The plan table prices LNX-CS-2GB at USD 5.95 a month, but the cart read 2026-11-07 marks it sold out with orders suspended, so the entry row cannot be ordered today. The page's own prose says 'Scale from $2.95/month' with no plan at that price in the table.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
  - monthly_usd: 5.95
  - annual_usd: not published: the page prints monthly prices only
  - renewal_usd: not published: no page names a renewal rate
  - stock: sold out: the store page suspends orders for the entry plan until more stock is available
  - term: monthly
- evidence:
  - [1] 2026-10-22: plan table row 'LNX-CS-2GB, 2GB, 1 vCore, 20GB NVMe RAID 10, 1TB @10Gbps, $5.95 /mo, Order', quoted
  - [1] 2026-10-22: 'Available in Tampa-FL only Starting from $5.95/m' in the page header, while the same page's FAQ says 'Scale from $2.95/month' with no plan at that price in the table
  - [2] 2026-10-22: tracker row 'USD 6.95 / month, 2 Intel Cores (shared), 2,048 MB RAM, 250 GB HDD, 2,000 GB/month bandwidth, 10 Gbps port speed, Tampa Florida'
  - [1] 2026-11-07: the plan table prices LNX-CS-2GB at USD 5.95 a month on 2026-11-07 | capture: sha256:7b89e3ea2cf9af5bd1c474bb917422113ef662659f927f6a36ac68e13cf0b387 | quote: <td data-label="Price"><span class="">$5.95</span>/mo</td>
  - [3] 2026-11-07: the store page marks the entry plan sold out and suspends orders for it on 2026-11-07 | capture: sha256:199cd08a3f1518833234f1c1f629b94906da013bf1f42708688875ed79728a20 | quote: SOLDOUT - Out of Stock
- sources:
  - [1] https://solidvps.com/starter-kvm-cloud-vps.php
  - [2] https://vpspricetracker.com/provider/SolidVPS/vps
  - [3] https://my.solidvps.com/store/solid-cloud-budget/linux-cloud-vshared-2gb-1
