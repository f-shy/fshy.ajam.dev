# Bullethost

> bullethost.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bullethost/ | JSON https://fshy.ajam.dev/api/v1/entity/bullethost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bullethost

- `compute/bullethost` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:30.074Z (live) | stale on 2026-12-08
- url https://www.bullethost.net/vps/
- free tier: Linux I at EUR 4.99/month: 2 vCores, 4 GB RAM, 50 GB SSD, 3 TB bandwidth, 1 Gbps connection, 2 Tbps DDoS protection, 1 IPv4 plus 1 IPv6, KVM, deployed in what the page's own counters call '2 EU deployment regions'. The tracker instead lists a cheaper EUR 3.00/month plan on EUR 8.99 quarterly billing with 2 GB RAM, 30 GB SSD and 1,536 GB/month in the Netherlands, which the vendor's VPS page does not show. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 3 TB of bandwidth included on Linux I at 1 Gbps, with no period printed on the card and no overage price published on the page read | metered: yes | free allowance: 3 TB on Linux I (the card prints no period) | source: [1]
- identity: email | detail: not stated
- interface: rest, s3-compatible
- limits:
  - volume-quota (binding): 3 TB of bandwidth on Linux I at 1 Gbps, with no period printed on the card and the tracker's sibling row quoted per month; the tracked EUR 3.00 plan carries a much smaller 1,536 GB/month allowance, so the cheapest row and the cheapest documented row are bound by different numbers [1]
- limits note: 3 TB of bandwidth on Linux I at 1 Gbps, with no period printed on the card and the tracker's sibling row quoted per month; the tracked EUR 3.00 plan carries a much smaller 1,536 GB/month allowance, so the cheapest row and the cheapest documented row are bound by different numbers
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: KVM with an order link into a WHMCS store at /clients/store; no API or S3 endpoint is documented on the VPS page
- composes with: 4 GB of RAM and 50 GB of SSD for EUR 4.99 with 3 TB of transfer is a workable always-on crawler or job runner in the EU; the 50 GB disk is too small to hold any part of the archive, so it chains with a storage host rather than replacing one
- reliability: no reliability event recorded
- notes: Two prices for two products. The tracker's EUR 3.00/month row is the vendor's own Minimal VPS group card, Mini I: 1 Core, 2 GB RAM, 30 GB SSD, 1.5 TB bandwidth, 1 Gbps, listed at EUR 8.99 with no billing period printed on the card and marked Out of Stock; EUR 8.99 / 3 months = EUR 2.99 per month (derived), matching the tracker's EUR 3.00 on quarterly billing. Linux I at EUR 4.99/month is out of stock at the cart and on the vendor's product page. No annual or renewal figure is printed on any page read.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 50
  - monthly_eur: 4.99
  - annual_eur: not published: the vendor's VPS page prints no annual total
  - renewal_eur: not published: no page read prints a renewal or month-13 sentence
  - in_stock: no
  - billing_term: monthly
- evidence:
  - [1] 2026-10-22: plan card quoted: 'Linux I', 'EUR4.99 /mo', 'KVM Virtualization', '2 vCores', '4 GB RAM', '50 GB SSD', '3 TB bandwidth', '1 Gbps connection', '2 Tbps DDoS protection', '1 IPv4 + 1 IPv6'
  - [1] 2026-10-22: the page's hero counters read '7' 'Live VPS plans' and '2' 'EU deployment regions', and the FAQ line 'you can start with Linux VPS from EUR 4.99 per month' matches the lowest card on the page
  - [2] 2026-10-22: tracker row quoted: 'Bullethost - EUR3.00 / month', 'quarterly Service', '1 Intel Cores (shared)', '2,048 MB RAM', '30 GB SSD', '1,536 GB/month bandwidth', '1 Gbps port speed', 'Netherlands'; intro 'starting at EUR8.99 per quarter'; info page marks it 'In stock now'
  - [1] 2026-11-07: the vendor's VPS page lists Linux I at EUR 4.99 per month | capture: sha256:c636eac0c18618bae6e29c198093f5571b21bc3b289f4fd03736d605eeef85c4 | quote: Linux I
  - [3] 2026-11-07: the vendor cart suspends orders for Linux I (pid 20) | capture: sha256:8dac4aa2e0fd05b552829907539ccde21478764e9405902e913965f764658fb0 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available.
  - [1] 2026-11-07: the vendor's VPS page still lists Linux I at EUR 4.99 per month with 2 vCores, 4 GB RAM and 50 GB SSD | capture: sha256:c636eac0c18618bae6e29c198093f5571b21bc3b289f4fd03736d605eeef85c4 | quote: Linux I
  - [1] 2026-11-07: the page prints the list price and no renewal sentence | capture: sha256:c636eac0c18618bae6e29c198093f5571b21bc3b289f4fd03736d605eeef85c4 | quote: Linux I
  - [4] 2026-11-07: the vendor's own product page for Linux I answers the WHMCS out-of-stock template | capture: sha256:963be573d4a7842ed4cd740355f8d5305553e2779753a74244b396a2ad31e637 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available. For further information, please contact us.
  - probe:https://www.bullethost.net/clients/cart.php?a%3Dadd%26pid%3D20 2026-11-07: the cart read of the Linux I order lands on the product page and carries the out-of-stock phrase with no price | capture: sha256:0ce6098a9a56d92fff5cac6973db085124723f3e302b4602354c5c7aea0ba8e9 | quote: out of stock
  - [5] 2026-11-07: the card prints no billing period | capture: sha256:1d9a57a1d9d87a9ecd48e4e6e0ad9078b07952c6ec20ec0999563dcc746f4dc2 | quote: €8.99 ### Mini I
  - [5] 2026-11-07: the 'Mini I' card is marked out of stock in the vendor's own store | capture: sha256:1d9a57a1d9d87a9ecd48e4e6e0ad9078b07952c6ec20ec0999563dcc746f4dc2 | quote: Out of Stock
  - [5] 2026-11-07: the vendor's own store group holds the plan the tracker priced at EUR 3.00/month | capture: sha256:1d9a57a1d9d87a9ecd48e4e6e0ad9078b07952c6ec20ec0999563dcc746f4dc2 | quote: €8.99 ### Mini I
  - [1] 2026-11-07: the order page prints the EUR 4.99 monthly price and no annual or renewal figure | capture: sha256:3bd153f1236c00835f67f5954d04f3bb971babb1318e1901522c3539dfe91691 | quote: You can start with Linux VPS from EUR 4.99 per month, and we also offer Windows VPS plans for projects that need RDP access, Windows applications, or Microsoft-based environments.
- sources:
  - [1] https://www.bullethost.net/vps/
  - [2] https://vpspricetracker.com/provider/Bullethost/vps
  - [3] https://www.bullethost.net/clients/cart.php?a=add&pid=20
  - [4] https://www.bullethost.net/clients/store/xeonvps/linux-i
  - [5] https://www.bullethost.net/clients/store/minimal-vps
