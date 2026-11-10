# DigiRDP

> digirdp.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/digirdp/ | JSON https://fshy.ajam.dev/api/v1/entity/digirdp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DigiRDP

- `compute/digirdp` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:32.092Z (live) | stale on 2026-12-08
- url https://digirdp.com/cloud-vps-plan/linux-vps-hosting
- free tier: Cloud VPS Host IPV6 at USD 1.00/month, with USD 5.99 shown struck through as the list price and 'Save 83%' beside it, billed USD 12.00 per year in the page's annual view: quoted as '1 c / 40 t', 1 GB RAM, 10 GB disk on RAID 50, a /64 IPv6 only, and marked 'Semi-Annual/Annual billing only'. The page marks it 'Most Popular' and 'Chosen by 62% of our customers'. The tracker instead lists USD 5.99/month for a different, larger product: 3 cores, 6 GB RAM, 500 GB HDD, 10,240 GB/month in Los Angeles. Re-read 2026-11-07: the order page still shows USD 1.00 per month against the USD 5.99 strike with Save 83 percent, billed $12.00/yr, and the plan card still lists 'Semi-Annual/Annual billing only'. The WHMCS store group page manage.digirdp.com/store/ssd-vps-hosting lists the same product as 'SSD VPS Host IPV6' starting at GBP 1.13 monthly (the store's currency selector also offers USD, INR and EUR) with 'Semi-Annual/Annual billing' in the card features and an Order Now button, so the plan is in stock. No page read prints a renewal price. The cart itself renders no price to a cookieless or direct read: the site cart page renders prices client-side, a direct cart read of manage.digirdp.com answered HTTP 403, and a cookieless read of the store resolves to the default product group. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read for the USD 1.00 plan: the card prints '1 c / 40 t' and explains neither figure, and the provider's unmetered-bandwidth claim is made about its Windows RDP accounts rather than this plan | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: no monthly byte allowance is stated for this plan on the page read; the card prints '1 c / 40 t' without explaining the '40 t', so no transfer figure is asserted here
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: order buttons on the site post to digirdp.com/cart/add with a base64-encoded reference into manage.digirdp.com, which is the management panel; no API is documented
- composes with: USD 12 a year is the cheapest price in this slice, but it buys 1 GB and 10 GB of disk with no IPv4 address, so it is a control-plane host behind a tunnel rather than anything that can serve traffic; the larger tracked 500 GB HDD plan at USD 5.99 is the one that would hold data
- reliability: no reliability event recorded
- notes: Two products share the USD 5.99 list price: the vendor's USD 1.00/month is the discounted rate on its IPv6 plan, shown struck against USD 5.99 with 'Save 83%' and billed USD 12.00/yr in the annual view, while the tracker's USD 5.99 buys a 6 GB storage VPS in Los Angeles that this page does not price. The recorded offer is the vendor's cheapest with its billing caveat quoted; the tracked row stays in evidence. The '40 t' in '1 c / 40 t' is left as written rather than interpreted. The page also says deployment is a 'choice of India or US'.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-22: plan card quoted: 'Cloud VPS Host IPV6', 'Most Popular', '$ 1 .00 / mo', 'billed $12.00/yr', '1 c / 40 t', '1Gb RAM', '10Gb Disk - Raid 50', '/64 IPV6', 'Semi-Annual/Annual billing only'
  - [1] 2026-10-22: plan table quoted: 'Cloud VPS Host Starter' at '$3.00 / mo' 'billed $36.00/yr' with '1Gb RAM', '15Gb Disk - Raid 50', '/64 IPV6 + 1 IPV4'; and the monthly-billing list at the top of the page shows the same IPv6 plan at '$5.99' with 'Save 83%'
  - [2] 2026-10-22: tracker row quoted: 'DigiRDP - $5.99 / month', '3 Intel Cores (shared)', '6,144 MB RAM', '500 GB HDD', '10,240 GB/month bandwidth', '1 Gbps port speed', 'IPv4', 'Los Angeles California U.S.A.'; info page marks it 'In stock now' and lists Windows 'Yes (unlicensed)'
  - [3] 2026-11-07: the WHMCS store group page prices the 'SSD VPS Host IPV6' card (product370, order button on the same card) starting at GBP 1.13 monthly, so the plan is in stock | capture: sha256:a95f9bdc3d10274dab5095087bea71fc3c6f64eda015540fcf97d98444856b17 | quote: <div class="price-amount word-break-all"> £1.13 GBP
  - probe:https://manage.digirdp.com/index.php?rp=/store/cloud-vps-hosting/ssd-vps-hosting 2026-11-07: a direct cart read of manage.digirdp.com answered HTTP 403, so the cart price is not readable that way | capture: sha256:eb2df3e019026db48e89765b495aa525270d804664a0fbebb605c9a361020844 | quote: "status": 403
  - [1] 2026-11-07: the order page still bills the IPv6 plan $12.00/yr beside the USD 1.00 monthly price, the USD 5.99 strike and 'Semi-Annual/Annual billing only' | capture: sha256:c0ef1108ccbe398445ad3c094f33c5612ca69062789b8112c442fe68250337e9 | quote: billed $12.00/yr
- sources:
  - [1] https://digirdp.com/cloud-vps-plan/linux-vps-hosting
  - [2] https://vpspricetracker.com/provider/DigiRDP/vps
  - [3] https://manage.digirdp.com/store/ssd-vps-hosting
