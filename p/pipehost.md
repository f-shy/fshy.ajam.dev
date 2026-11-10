# PipeHost

> pipehost.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pipehost/ | JSON https://fshy.ajam.dev/api/v1/entity/pipehost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PipeHost

- `compute/pipehost` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:58.955Z (live) | stale on 2026-11-22
- url https://pipehost.net/cloud
- price parsed USD 6.65/mo
- free tier: The vendor store's Vienna category prices the XS plan at EUR 5.90 'Starting from · Monthly': 1 core, 3 GB DDR4 RAM, 35 GB NVMe SSD, 1 IPv4 + /64 IPv6, a 10 Gbit/s port under a fair-use policy, in Vienna, with an Order Now button and no sold-out badge, while the XL and XXL plans on the same page carry Sold out badges. The store exposes no other billing term: the product URL and the cart-add URL both serve the category page, whose HTML prints only 'Monthly', so the annual price and the renewal price are not published. The tracker's cheapest row, the record's original source for the shape, is the same plan at EUR 5.90; the tracker page also lists two more EUR 5.90 rows, one with an Epyc core and more storage in Vienna and one with the same shape in Amsterdam. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the store page prints '10 Gbit/s Port (Fair Use)' with no byte allowance; the plan API's bandwidth field reads 10 with the unit unstated; no overage price is published | metered: yes | free allowance: fair use on a 10 Gbit/s port; no byte allowance published | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): the vendor publishes no byte allowance: the store page prints '10 Gbit/s Port (Fair Use)' and the plan API's bandwidth field reads 10 with the unit unstated; no overage price is published. A 10 Gbit/s port under a fair-use policy is a burst shape whatever the cap is; the cap is not published. [1]
- limits note: the vendor publishes no byte allowance: the store page prints '10 Gbit/s Port (Fair Use)' and the plan API's bandwidth field reads 10 with the unit unstated; no overage price is published. A 10 Gbit/s port under a fair-use policy is a burst shape whatever the cap is; the cap is not published.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor page states 'REST API & CLI'; panel at panel.pipehost.net; OS templates plus custom ISO; daily backups included on every plan per the page; regions selected per order with live latency measurement in the browser
- composes with: EUR 5.90 for 3 GB of RAM and 35 GB of NVMe with 2.5 TB on a 10 Gbps port in Vienna is the fastest port per euro among documented hosts, and with the REST API and CLI it is the easiest to automate of the small hosts here. The 2.5 TB cap, not the port, is what stops it being a transfer host.
- reliability: the vendor page states a 99.99 percent network SLA and daily backups on every plan; no reliability incident observed
- notes: Wall: the plan configurator is client-side and rendered as '0 plans, prices in EUR' to both the raw fetch and the text extractor, and pipehost.net/pricing returned 404, so every plan number here is the tracker's and the record is labelled reported. Currency: the pages print a euro sign and it is written EUR throughout this record because the file is ASCII-only.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 3
  - facets.shape.disk_gib: 35
  - price_on_page: EUR 5.90/month for XS in Vienna; renewal: not published
- evidence:
  - [3] 2026-10-22: cheapest row: 'EUR 5.90 / month', '1 Intel Cores (shared)', '3,072 MB RAM', '35 GB NVMe', '2,560 GB/month bandwidth', '10 Gbps port speed', 'IPv4 + IPv6', Vienna Austria; header 'starting at EUR 5.90 per month'
  - [3] 2026-10-22: largest-storage row: 'EUR 84.90 / month', '20 Epyc Cores (shared)', '61,440 MB RAM', '650 GB NVMe', '76,800 GB/month bandwidth', '10 Gbps port speed', Vienna
  - [1] 2026-10-22: page quoted: 'Every plan has dedicated vCPU cores, NVMe storage, IPv4, IPv6 and daily backups' and 'REST API & CLI', '99.99% network SLA', six European locations: Vienna, Amsterdam, Frankfurt, Eygelshoven, Maribor, Stockholm
  - [2] 2026-11-07: the store page prices the Vienna Xeon XS at EUR 5.90, monthly term, with a 10 Gbit/s fair-use port and no byte allowance, and shows no stock badge (Order Now) | capture: sha256:68cb1f8087adb713ccfc829ca7abde66bd017aab81a99ec7e41aa8d65cf3dc11 | quote: 01 / XS €5.90 Starting from · Monthly 1 Core 3GB DDR4 RAM 35GB NVME SSD 1 IPv4 + /64 IPV6 10 Gbit/s Port (Fair Use)
  - [2] 2026-11-07: the store's Vienna category prices the XS plan at 5.90 EUR on a monthly term | capture: sha256:30dc83d962910a44eaa3bb50cfcd00e73000570a457424b85d46ed8b10b7fd74 | quote: €5.90 Starting from · Monthly
  - [4] 2026-11-07: the cart-add URL serves the same category page; the XS card carries an Order Now button with no Sold out badge while the XL and XXL cards carry Sold out badges, and the page HTML prints only Monthly as a billing term | capture: sha256:875dc4a35163e24c073f7839ffa5f06c4689a86fbda0ad2152206cebb95fc0df | quote: Sold out
  - [2] 2026-11-07: the store's Vienna category prices the XS plan at 5.90 EUR on a monthly term | capture: sha256:68cb1f8087adb713ccfc829ca7abde66bd017aab81a99ec7e41aa8d65cf3dc11 | quote: 01 / XS €5.90 Starting from · Monthly 1 Core 3GB DDR4 RAM 35GB NVME SSD 1 IPv4 + /64 IPV6 10 Gbit/s Port (Fair Use)
- sources:
  - [1] https://pipehost.net/cloud
  - [2] https://panel.pipehost.net/index.php/store/vps-xeon-vienna
  - [3] https://vpspricetracker.com/provider/PipeHost/vps
  - [4] https://panel.pipehost.net/index.php?rp=/store/vps-xeon-vienna/xs
