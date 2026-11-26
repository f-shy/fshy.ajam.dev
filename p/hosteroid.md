# Hosteroid

> hosteroid.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hosteroid/ | JSON https://fshy.ajam.dev/api/v1/entity/hosteroid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hosteroid

- `compute/hosteroid` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:33.037Z (live) | stale on 2026-12-08
- url https://www.hosteroid.uk/
- free tier: Archive-500GB at EUR 14.14/year VAT included, yearly prepaid only (the vendor states "Only EUR 1.18/mo when paid annually"): 1 vCPU, 2 GB DDR4 ECC RAM, 30 GB NVMe RAID10 boot plus 500 GB HDD RAID60 cached, 3 TB at 10 Gbps then 100 Mbps, 1 IPv4 and /64 IPv6, Bucharest Romania, stock stated as "Limited stock: 15 units". The monthly table starts higher: VM01 at EUR 3.00/month with 1 core, 512 MB, 10 GB SSD and 324 GB. The tracker's own floor is a Comet plan at EUR 1.50/month billed yearly (EUR 18.00/year) with 2 cores, 4,096 MB, 50 GB NVMe and 3,500 GB in Bucharest, which is dearer per year than the vendor's Archive plan. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 3 TB a month on the Archive plan, then shaped to 100 Mbps; the monthly ladder scales the allowance with the plan from 324 GB to 4,860 GB and states no overage price | metered: yes | free allowance: 3072 GB per month on Archive-500GB | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 3 TB a month at 10 Gbps then shaped to 100 Mbps after the allowance, so the first wall is bytes and the second is a tenth of the port; 3 TB is about 100 GB a day, a tenth of the 1 TB daily transfer volume, against 500 GB of local disk. [1]
- limits note: 3 TB a month at 10 Gbps then shaped to 100 Mbps after the allowance, so the first wall is bytes and the second is a tenth of the port; 3 TB is about 100 GB a day, a tenth of the 1 TB daily transfer volume, against 500 GB of local disk.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root and NVMe RAID10 boot, sold through a WHMCS storefront; no API documented on the page read.
- composes with: EUR 14.14 a year for 500 GB of cached HDD plus 3 TB a month is the cheapest cold tier among evaluated providers, and the 2 GB of RAM is enough to run a transfer agent in front of it; it is an archive edge, not a working set, and the 15-unit stock means it is not a plan to build a pipeline on.
- reliability: unverified, passed on: compute/fossvps records a LowEndSpirit post, "important-buc1-hosteroid-server-termination", quoting "node buc1 will terminate on 17th of April 2026 ... all data WILL BE DESTROYED"; that node was a donated FOSSVPS node in the same Bucharest datacentre as the cheapest plan read here, and the paid plan was not itself observed to be affected.
- notes: The vendor's own page is cheaper than the tracker's floor, which is the reverse of the usual direction: EUR 14.14 a year for 500 GB of disk against the tracker's EUR 18.00 a year for 50 GB, so the record leads with the vendor. Two tiers that are not free: VAT is included in the quoted figure, and the plan is annual prepay only, so a failed renewal loses the year. json as the sponsor of a donated free node, which is a different product). verification criteria: whether the 15-unit stock is per datacentre and what happens to the data at the end of the annual term.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 500
  - term: yearly prepaid only
  - price_on_page: EUR 14.14/yr VAT included
  - out_of_pocket_usd: 15.79
  - price_arithmetic: EUR 14.14 a year x 1.1165 USD/EUR (ECB reference via frankfurter.app, 2026-11-06) = USD 15.79 a year
  - renewal_usd: not published: the page prints no renewal price; the plan is yearly prepaid only and its order path is a Notify Me ticket
  - stock: limited stock: 15 units
  - cart_url: https://www.hosteroid.uk/submitticket.php?step=2&deptid=1&subject=Interest%20in%20Archive-500%20Storage%20VPS
- evidence:
  - [1] 2026-10-22: the Archive plan quoted from the storage section: "Archive-500GB" / "YEARLY PREPAID ONLY" / "EUR 14.14/yr VAT included" / "Annual billing required" / "Only EUR 1.18/mo when paid annually" / "1 vCPU" / "2 GB DDR4 ECC RAM" / "30 GB NVMe RAID10 Boot" / "500 GB HDD RAID60 (cached)" / "3 TB @ 10 Gbps -> 100 Mbps" (the page uses a right arrow, transliterated here) / "Bucharest, Romania" / "Limited stock: 15 units"
  - [1] 2026-10-22: the monthly ladder as a table: "VM01 | 1 CPU Cores | 512 MB RAM | 10 GB SSD | 324 GB Bandwidth | EUR 3.00", "VM02 | 1 | 1 GB | 20 GB | 810 GB | EUR 5.00", "VM03 | 2 | 2 GB | 30 GB | 1620 GB | EUR 8.00", "VM04 | 2 | 4 GB | 50 GB | 3240 GB | EUR 16.00", "VM05 | 4 | 8 GB | 85 GB | 4860 GB | EUR 29.00", each marked "monthly"
  - [2] 2026-10-22: the tracker's floor quoted: "Hosteroid - EUR 1.50 / month" / "yearly Service" / "cpu 2 Intel Cores (shared)" / "ram 4,096 MB RAM" / "disk 50 GB NVMe" / "bandwidth 3,500 GB/month bandwidth" / "rj45 10 Gbps port speed" / "city Bucharest Romania", under "starting at EUR 18.00 per year"
  - [1] 2026-11-07: the Archive-500GB plan is priced EUR 14.14 a year VAT included, yearly prepaid only, and its order path is a Notify Me ticket rather than a cart | capture: sha256:e47256e107970f4d5c92428881c5c556a5c8e24794e5562c305d2a4dddd14975 | quote: YEARLY PREPAID ONLY €14.14/yr VAT included
  - [1] 2026-11-07: the Archive-500GB plan is priced EUR 14.14 a year VAT included, yearly prepaid only | capture: sha256:e47256e107970f4d5c92428881c5c556a5c8e24794e5562c305d2a4dddd14975 | quote: YEARLY PREPAID ONLY €14.14/yr VAT included
- sources:
  - [1] https://www.hosteroid.uk/
  - [2] https://vpspricetracker.com/provider/Hosteroid/vps
