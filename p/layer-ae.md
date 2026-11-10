# Layer.ae

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/layer-ae/ | JSON https://fshy.ajam.dev/api/v1/entity/layer-ae.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Layer.ae

- `compute/layer-ae` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:35.518Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Layer_ae/vps
- free tier: USD 24.99/month (L8G): 2 Ryzen cores (shared), 8 GB DDR5 RAM, 200 GB NVMe, 12,000 GB/month bandwidth, 10 Gbps port, IPv4 and IPv6, Spokane Washington USA. The vendor cart at my.layer.ae prices L8G at USD 24.99 on a monthly term only, the billing-cycle selector offering no other term, with USD 0.00 setup and USD 24.99 total due today; the store listing shows stock of 1 Available for L8G and 0 Available for every other plan in the group, the cheap annual L512M plan included. The cart read (2026-11-07) resolved the L8G add (final URL cart.php?a=confproduct&i=0) and priced it $24.99 with no stock warning. The store's $20.00-a-year L512M stays at 0 Available; its monthly equivalent is USD 20.00 / 12 = USD 1.67, which matches the tracker's $1.67 card. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 12,000 GB a month included per the vendor cart description (free_allowance is in GB a month); overage price and throttling policy are not stated on the pages read | metered: yes | free allowance: 12000 | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 12,000 GB a month, which is the wall rather than the 10 Gbps port; the per-TB overage price is not stated on the pages read, and the 200 GB NVMe is the disk limit [1]
- limits note: 12,000 GB a month, which is the wall rather than the 10 Gbps port; the per-TB overage price is not stated on the pages read, and the 200 GB NVMe is the disk limit
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: client area and server status at my.layer.ae; the storefront is a JavaScript application whose plan table did not render to automated retrieval, so no vendor price was read; a 10 Gbps port on the orderable plan.
- composes with: USD 24.99 is an entry price rather than a cheap tier: Luxvps sells 4 GB for EUR 4.50 and Layer7 sells 6 GB for EUR 4.90, so the reason to pick this host is the 200 GB disk and the 12 TB allowance, not the compute; the USD 1.67 annual plan that makes the provider interesting is not orderable from the page, so the cheap end needs the client area
- reliability: no reliability event recorded
- notes: Layer.ae provides VPS hosting in the United Arab Emirates.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 8
  - facets.shape.disk_gib: 200
- evidence:
  - [1] 2026-10-22: card quoted: '$24.99 / month', '2 Ryzen Cores (shared)', '8,192 MB RAM', '200 GB NVMe', '12,000 GB/month bandwidth', '10 Gbps port speed', 'Spokane Washington U.S.A.'; it is the only offer with a live order link: three of the 12 cards carry one and all three are this same plan. The page's lead line reads 'These are the cheapest VPSs currently offered by Layer.ae, starting at $20.00 per year'
  - [1] 2026-10-22: the three cheapest cards quoted as '$1.67 / month', 'yearly Service', '1 Ryzen Cores (shared)', '512 MB RAM', '10 GB NVMe', '500 GB/month bandwidth', '10 Gbps port speed', in Spokane, Coventry and Eygelshoven; each renders its Go control as a span with class 'button_disabled' and carries no order link
  - [2] 2026-10-22: the marketing site is a JavaScript single-page application (asset bundle /assets/index-BkzgDGeX.css, no price text in the served HTML); the client area is at my.layer.ae and layer.ae/pricing returns a 404 page reading 'Oops! Page not found'
  - [3] 2026-11-07: the store listing prices L8G from USD 24.99 monthly with 1 Available, L512M from USD 20.00 annually, and L1G, L2G, L4G and L6G from USD 7.49, 9.99, 14.99 and 19.99 monthly, all with 0 Available | capture: sha256:381adabc479303f9913fa2126228f5f899e6a2d809ba7af328c04c26427e0ea6 | quote: $24.99 USD ... Monthly ... 1 Available ... $20.00 USD ... Annually ... $7.49 USD ... $9.99 USD ... $14.99 USD ... $19.99 USD
  - [1] 2026-11-07: the tracker still shows the USD 1.67-a-month annual L512M cards, which the record described as without an order link | capture: sha256:1a81572597965156989b1ae8ce4290f14406f0b66c01fa963d366963410ef143 | quote: $1.67 / month ... yearly Service ... 512 MB RAM ... 10 GB NVMe
  - [3] 2026-11-07: the store listing shows stock 1 Available for L8G, the only plan with a non-zero count; L512M, L1G, L2G, L4G and L6G show 0 Available | capture: sha256:381adabc479303f9913fa2126228f5f899e6a2d809ba7af328c04c26427e0ea6 | quote: 1 Available
  - [3] 2026-11-07: the L512M plan is priced from USD 20.00 on an annual term in the vendor store, so the cheap annual plan is orderable there but shows 0 Available | capture: sha256:381adabc479303f9913fa2126228f5f899e6a2d809ba7af328c04c26427e0ea6 | quote: $20.00 USD ... Annually
  - [4] 2026-11-07: the L8G cart description states 12000 GB of bandwidth | capture: sha256:2be7c64b503160acb9e757a15941fa443b59dba096c35f34638b7ff1b8b9a545 | quote: 12000GB Bandwidth
  - [4] 2026-11-07: the L8G cart description confirms the 200 GB NVMe disk and the 12,000 GB monthly bandwidth | capture: sha256:2be7c64b503160acb9e757a15941fa443b59dba096c35f34638b7ff1b8b9a545 | quote: 200GB <strong>NVMe</strong> (PCIe 4.0) ... 12000GB Bandwidth
  - probe:https://my.layer.ae/store/amd-ryzen-10gbit-nvme/8gb 2026-11-07: the cart resolved the L8G add (final URL cart.php?a=confproduct&i=0) and its price list carries $24.99 with no stock warning | capture: sha256:15a520276655acaab41ed432cdba8f2ddb4b536a50634a9f48bc7991f20cca6d | quote: "prices": [ "$24.99", "$2.00" ]
  - [4] 2026-11-07: the cart page's $2.00 price is the second-IPv4 config option (IPv4: 1 selected, 2 for +$2.00) | capture: sha256:2be7c64b503160acb9e757a15941fa443b59dba096c35f34638b7ff1b8b9a545 | quote: IPv4 ... <option value="2"> 2 $2.00 USD
  - [3] 2026-11-07: the store lists L8G at 1 Available, 'Starting from $24.99 USD Monthly' | capture: sha256:d64562a6d177ff6b2d58ccdcf6b7efbe051084237343c16b881105ffe628e5b0 | quote: L8G ... 1 Available ... Starting from ... $24.99 USD ... Monthly
  - [3] 2026-11-07: the store lists L512M at 0 Available, $20.00 USD Annually | capture: sha256:d64562a6d177ff6b2d58ccdcf6b7efbe051084237343c16b881105ffe628e5b0 | quote: L512M ... 0 Available ... $20.00 USD ... Annually
  - [1] 2026-11-07: the tracker's $1.67/month annual L512M card is still listed | capture: sha256:1a81572597965156989b1ae8ce4290f14406f0b66c01fa963d366963410ef143 | quote: $1.67 / month
  - probe:https://my.layer.ae/store/amd-ryzen-10gbit-nvme/8gb 2026-11-07: the cart still prices L8G $24.99 monthly, unchanged | capture: sha256:15a520276655acaab41ed432cdba8f2ddb4b536a50634a9f48bc7991f20cca6d | quote: "prices": [ "$24.99", "$2.00" ]
- sources:
  - [1] https://vpspricetracker.com/provider/Layer_ae/vps
  - [2] https://layer.ae/
  - [3] https://my.layer.ae/store/amd-ryzen-10gbit-nvme
  - [4] https://my.layer.ae/store/amd-ryzen-10gbit-nvme/8gb
