# WebHorizon

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webhorizon/ | JSON https://fshy.ajam.dev/api/v1/entity/webhorizon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WebHorizon

- `compute/webhorizon` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/WebHorizon/vps
- free tier: Ryzen-KVM-1GB (India): 1 AMD Ryzen 7000 core, 1GB DDR5, 15GB NVMe, 1TB @ 500Mbps, IPv4 + /56 IPv6, DDoS protection not available. listed Out of stock on the vendor's order portal (read 2026-11-07), which prints no per-plan price for the India line; the line's from-price and the entry EPYC plan's price are quoted in the record's evidence rows. The vendor's virtual-servers page (read 2026-11-07) shows the entry EPYC plan in stock with Instant ETA and its larger siblings out of stock. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1TB a month on the entry plan at 500Mbps, stated by the vendor's order portal (read 2026-11-07); the tracker's earlier monthly figure agrees to rounding. No overage price is published. | metered: yes | free allowance: 1TB a month (vendor order portal, read 2026-11-07) | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1TB a month on a 500Mbps port for the entry plan, stated by the vendor's order portal; the tracker's earlier monthly figure agrees to rounding. Whether the byte allowance or the port binds first is still unverified. [1]
- limits note: 1TB a month on a 500Mbps port for the entry plan, stated by the vendor's order portal; the tracker's earlier monthly figure agrees to rounding. Whether the byte allowance or the port binds first is still unverified.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not read: the vendor site returned a script shell, so no client, panel or API could be seen
- composes with: the India location at USD 3 is the cheapest Asian presence among documented hosts; with a 1 TB allowance it is a metadata node, and the bytes stay where they were scraped
- reliability: no reliability event recorded
- notes: The vendor's marketing pages answered a JavaScript shell on the first read (2026-10-22); the order portal at clients.webhorizon.net and the /virtual-servers table are readable as of 2026-11-07: the Performance Ryzen line is priced from three dollars a month, every India Ryzen plan including the entry plan shows Out of stock with no cart price printed, and the entry EPYC plan shows Instant ETA while its larger siblings show Out of Stock. The per-plan India cart price stays unverified until a plan is orderable.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - price_on_page: From $3.00 USD/month for Performance Ryzen VPS (line from-price; the entry Ryzen-KVM-1GB (India) plan is out of stock and the cart prints no per-plan price)
  - renewal_usd: not published: no page read prints a renewal figure; the portal cart lists the entry plan out of stock and the products page prints only the line from-price
- evidence:
  - [1] 2026-10-22: 'These are the cheapest VPSs currently offered by WebHorizon, starting at $3.00 per month' and the row 'WebHorizon - $3.00 / month 1 Ryzen Cores (shared) 1,024 MB RAM 15 GB NVMe 1,024 GB/month bandwidth 0.49 Gbps port speed IPv4 + IPv6 India'
  - [1] 2026-10-22: next rows: '$4.99 / month 1 Intel Cores (shared) 2,048 MB RAM 30 GB NVMe 2,048 GB/month bandwidth 5 Gbps' in Norway, and the same at 4.99 with an Epyc core in the Netherlands
  - [2] 2026-10-22: table quoted: 'NVME-KVM-16GB | 8 AMD EPYC 7003 | 16GB DDR4 ECC | 240GB NVME RAID10 | 16TB @ 5Gbps | $40.00/mo' and the entry row 'NVME-KVM-2GB ... 30GB NVME RAID10 ... 2TB @ 5Gbps ... $4.99/mo'
  - [3] 2026-10-22: the homepage lists five products: Enterprise EPYC VPS from $4.99/mo, Performance Ryzen VPS from $3.00/mo, Virtual Dedicated Servers from $40.00/mo, Baremetal at custom pricing and Web Hosting from $2.99/mo; no storage product
  - [4] 2026-10-22: the storage path returns the site's own 404 page ('Page Not Found'), as does /vps, so no storage product exists at either name
  - [5] 2026-11-07: the order portal lists the entry plan as out of stock, with no price on the page | capture: sha256:7e2cfa270f9b58dcdf495845d98e0b6dd269ceee70b41dd4c524caa65ff11199 | quote: Out of stock Ryzen-KVM-1GB (India)
  - [6] 2026-11-07: the portal's product page prices the Performance Ryzen line from USD 3.00 | capture: sha256:85c9f2fc8c43e7bb072873a9911c644743345c3b11d38c8b10689e13555032de | quote: From $3.00 USD
  - [2] 2026-11-07: the vendor's virtual-servers table states the entry EPYC plan at $4.99/mo with Instant ETA | capture: sha256:4fa281a11d696b8a36db3fa1dbc872f3074c7f356813c7da199bd33cc69543ed | quote: NVME-KVM-2GB | 1 AMD EPYC™ 7003 | 2GB DDR4 ECC | 30GB NVME RAID10 | 2TB @ 5Gbps | $4.99/mo | Instant
  - [5] 2026-11-07: the vendor's own cart page states the transfer allowance and port for the India plans | capture: sha256:7e2cfa270f9b58dcdf495845d98e0b6dd269ceee70b41dd4c524caa65ff11199 | quote: 1TB @ 500Mbps
  - [5] 2026-11-07: the vendor's own cart page states the transfer allowance | capture: sha256:7e2cfa270f9b58dcdf495845d98e0b6dd269ceee70b41dd4c524caa65ff11199 | quote: 1TB @ 500Mbps
  - [5] 2026-11-07: the vendor's own cart page states the transfer allowance and port | capture: sha256:7e2cfa270f9b58dcdf495845d98e0b6dd269ceee70b41dd4c524caa65ff11199 | quote: 1TB @ 500Mbps
  - [5] 2026-11-07: the wall note is superseded: the order portal is readable and shows the entry plan out of stock | capture: sha256:7e2cfa270f9b58dcdf495845d98e0b6dd269ceee70b41dd4c524caa65ff11199 | quote: Out of stock Ryzen-KVM-1GB (India)
  - [5] 2026-11-07: the entry plan's order state as of 2026-11-07 | capture: sha256:7e2cfa270f9b58dcdf495845d98e0b6dd269ceee70b41dd4c524caa65ff11199 | quote: Out of stock Ryzen-KVM-1GB (India)
  - [6] 2026-11-07: the vendor's own order portal prices the Performance Ryzen line from USD 3.00 | capture: sha256:85c9f2fc8c43e7bb072873a9911c644743345c3b11d38c8b10689e13555032de | quote: From $3.00 USD
  - [6] 2026-11-07: the vendor's own products page prices the Performance Ryzen line from USD 3.00 | capture: sha256:85c9f2fc8c43e7bb072873a9911c644743345c3b11d38c8b10689e13555032de | quote: From $3.00 USD
- sources:
  - [1] https://vpspricetracker.com/provider/WebHorizon/vps
  - [2] https://webhorizon.net/virtual-servers
  - [3] https://webhorizon.net/
  - [4] https://webhorizon.net/storage-vps
  - [5] https://clients.webhorizon.net/?/cart/performance-ryzen-vps-india/
  - [6] https://clients.webhorizon.net/?/products/
