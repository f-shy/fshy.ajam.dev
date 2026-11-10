# HostSlick

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostslick/ | JSON https://fshy.ajam.dev/api/v1/entity/hostslick.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostSlick

- `compute/hostslick` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:33.037Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/HostSlick/vps
- price parsed USD 11.26/mo
- free tier: KVM AMD Ryzen I at EUR 9.99/month (the tracker writes the euro sign; transliterated here for ASCII): 4 Ryzen cores fair-share, 2,048 MB RAM, 25 GB NVMe, 2,000 GB/month bandwidth, 1 Gbps port, 1 IPv4 + IPv6, Lelystad Netherlands. The tracker's line reads "starting at EUR 9.99 per month". The ladder above it: KVM AMD Ryzen II at EUR 14.99/month with 4 cores, 4,096 MB and 40 GB NVMe; KVM AMD Ryzen III at EUR 21.99 with 6 cores, 6,144 MB and 60 GB NVMe. The vendor's own store page for the same product confirms the shape and not the price. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month on the Ryzen I plan, stated as a plan line both by the tracker and by the vendor store page ("Bandwidth - 2TB"); the vendor runs a separate unmetered 10 Gbit and 40 Gbit dedicated line, which is a different product | metered: yes | free allowance: 2048 GB per month | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2,000 GB a month is about 66 GB a day, 6.6 percent of one day of the 1 TB daily transfer volume, and the 25 GB NVMe disk holds no working set; the 4 shared Ryzen cores are the only generous part of the plan. [1]
- limits note: 2,000 GB a month is about 66 GB a day, 6.6 percent of one day of the 1 TB daily transfer volume, and the 25 GB NVMe disk holds no working set; the 4 shared Ryzen cores are the only generous part of the plan.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, sold through a WHMCS store at hostslick.com/clients, so any client runs inside the VM and no wrapper is needed; no API was documented on either page read.
- composes with: 4 Ryzen cores and 2 GB for EUR 9.99 is the most CPU per euro among evaluated providers, which fits a short build or a compile job rather than a serving node; 2 TB a month caps it as a crawler front end and the 25 GB disk caps it as anything that holds data.
- reliability: no reliability event recorded
- notes: Price is tracker-only: the vendor's own product page for KVM AMD Ryzen I rendered its specs but no price in the HTML evaluated providers read, so the EUR 9.99 stays reported rather than documented. The search result for the same URL carried a snippet with "EUR 9.99EUR Monthly", which is a search index and not a page read, and it was not used as evidence. verification criteria: a client-side render of the store page, which needs a browser evaluated providers did not use, to lift the price to documented.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 25
  - term: monthly
  - price_on_page: EUR 9.99/mo (tracker; the vendor store page rendered no price in the read)
  - out_of_pocket_usd: 11.15
  - renewal_usd: not published: no page read prints a renewal price
  - stock: 0 Available on every Ryzen plan at the vendor store read 2026-11-07
  - cart_url: https://hostslick.com/clients/store/amd-ryzen-linux-kvm-vps-netherlands
- evidence:
  - [1] 2026-10-22: the cheapest row quoted: "HostSlick - EUR 9.99 / month" / "cpu 4 Ryzen Cores (shared)" / "ram 2,048 MB RAM" / "disk 25 GB NVMe" / "bandwidth 2,000 GB/month bandwidth" / "rj45 1 Gbps port speed" / "inet IPv4 + IPv6" / "city Lelystad Netherlands", under "starting at EUR 9.99 per month"
  - [2] 2026-10-22: the vendor's own product page confirms the shape: "KVM AMD Ryzen I - Specs" / "CPU - 4 vCore" / "RAM - 2 GB" / "Bandwidth - 2TB" / "NVME Disk Space - 25 GB" / "Port Speed - 1 Gbps" / "Location - Lelystad, Netherlands (EU)"
  - [3] 2026-10-22: 
  - [1] 2026-11-07: the tracker still lists KVM AMD Ryzen I at EUR 9.99 a month | capture: sha256:786b2d50cc63888ff9a875964f8a8f5a08be614629ea7c5a0840562eb1c285f7 | quote: These are the cheapest VPSs currently offered by HostSlick, starting at €9.99 per month:
  - [2] 2026-11-07: the vendor store page shows the Ryzen plans at 0 available | capture: sha256:2d49b2f25bb04367f4d71f13fed35d36785a716517c1ae88b95e22fe7cfc9b4c | quote: 0 Available
- sources:
  - [1] https://vpspricetracker.com/provider/HostSlick/vps
  - [2] https://hostslick.com/clients/store/amd-ryzen-linux-kvm-vps-netherlands
  - [3] https://hostslick.com/
