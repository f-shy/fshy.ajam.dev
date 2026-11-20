# Host-C

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/host-c/ | JSON https://fshy.ajam.dev/api/v1/entity/host-c.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Host-C

- `compute/host-c` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:07.272Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Host_C/vps
- price parsed USD 6.99/mo
- free tier: Event Horizon NX 01 Storage 1 TB G2 at USD 6.99/month: 1 Intel core shared, 2,048 MB RAM, 1,000 GB HDD, 3,000 GB/month bandwidth, 1 Gbps port, IPv4 + IPv6, Oradea Romania. The tracker's line reads "starting at $6.99 per month". The sibling rows move the traffic and not the disk: USD 7.99 buys the same 1 TB disk and 2 GB with 4,000 GB/month, and USD 8.00 buys a 60 GB NVMe White Neptune plan with 2,048 GB/month. | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 3 TB a month on the cheapest plan, 4 TB on the USD 7.99 sibling, stated as a plan line; no overage rate and no post-quota policy published on the page read | metered: yes | free allowance: 3000 GB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 3,000 GB a month against a 1,000 GB disk is 3 writes of the disk per month, so the plan can be filled but not served; 3,000 GB is 100 GB a day, 10 percent of the 1 TB daily transfer ceiling. [1]
- limits note: 3,000 GB a month against a 1,000 GB disk is 3 writes of the disk per month, so the plan can be filled but not served; 3,000 GB is 100 GB a day, 10 percent of the 1 TB daily transfer ceiling.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root and an own AS211462 network, sold through a live client catalog the vendor does not render into the page HTML, so the price and the order path both sit behind a client area; no API documented on the page read.
- composes with: 1 TB of HDD for USD 6.99 a month is the most disk per dollar among evaluated providers, and it is the only plan here with a disk large enough to matter for the 20 TB dataset; the 3 TB a month is what makes it an ingest target rather than a serving host, and the single shared core is enough to run a transfer agent and nothing else.
- reliability: no reliability event recorded
- notes: Price is tracker-only. The vendor homepage says in terms that its prices are loaded from the live client catalog, which is the reason this record is reported rather than documented. verification criteria: a render of host-c.com with JavaScript, or the user-area catalog, to read the same row from the vendor.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 1000
  - price_on_page: USD 6.99/month for Event Horizon NX 01 Storage 1 TB G2
  - renewal_note: not published; the tracker's rows print monthly prices only
- evidence:
  - [1] 2026-10-22: the cheapest row quoted: "Host-C - $6.99 / month" / "cpu 1 Intel Cores (shared)" / "ram 2,048 MB RAM" / "disk 1,000 GB HDD" / "bandwidth 3,000 GB/month bandwidth" / "rj45 1 Gbps port speed" / "inet IPv4 + IPv6" / "city Oradea Romania", product slug Event_Horizon_NX_01_Storage_1_TB_G2_1_I185, under "starting at $6.99 per month"
  - [2] 2026-10-22: the vendor page states where its prices live: "## Our Server Plans" followed by "Prices and checkout links are loaded from the live client catalog.", and the network line "NVMe VPS ... Own network AS211462 ... Oradea, RO" (separators elided)
  - [2] 2026-10-22: "Activation in ~45 seconds", "IPv4 + IPv6 included", "RAID 10 / RAID 60", and "Dell server platforms using Intel Xeon Scalable Generation 2 Processors"
  - [1] 2026-11-07: the tracker's cheapest Host-C row is USD 6.99 a month | capture: sha256:a1d5cbaa44aed214cfbebb31fde76f6870aae03b0af3abb22dd2706408956ca2 | quote: starting at $6.99 per month
  - [1] 2026-11-07: the tracker's rows print monthly prices only, no renewal price | capture: sha256:a1d5cbaa44aed214cfbebb31fde76f6870aae03b0af3abb22dd2706408956ca2 | quote: starting at $6.99 per month
  - [1] 2026-11-07: the tracker's cheapest row is as the record states | capture: sha256:a1d5cbaa44aed214cfbebb31fde76f6870aae03b0af3abb22dd2706408956ca2 | quote: starting at $6.99 per month
- sources:
  - [1] https://vpspricetracker.com/provider/Host_C/vps
  - [2] https://host-c.com/
