# SpeedyPage

> speedypage.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/speedypage/ | JSON https://fshy.ajam.dev/api/v1/entity/speedypage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SpeedyPage

- `compute/speedypage` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:42.897Z (live) | stale on 2026-12-08
- url https://speedypage.com/vps
- price parsed USD 4.68/mo
- free tier: AMD Ryzen VPS at GBP 3.50/month: 1 Ryzen core (AMD Ryzen 7900 / 9700X, up to 5.4 GHz), 1 GB DDR5, 15 GB NVMe, 2 TB bandwidth on a 10 Gbps port, London UK. The same card shows the annual term at GBP 38.50/year and the parallel USD display at 4.29/month. The next plan is GBP 4.99/month with 1 core, 2 GB, 30 GB NVMe and 5 TB. No renewal price is printed on the pages read. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month is included on this plan; no overage price and no post-allowance throttle are stated on the page read | metered: yes | free allowance: 2 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month on a 10 Gbps port is the first wall on this plan; the page states no overage rate and no throttle behaviour after the allowance, so what happens at 2 TB is unverified [1]
- limits note: 2 TB a month on a 10 Gbps port is the first wall on this plan; the page states no overage rate and no throttle behaviour after the allowance, so what happens at 2 TB is unverified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: the plan page documents no API, no control panel and no image list, so root access and a Linux template are unverified
- composes with: GBP 3.50 for 1 GB of RAM and 2 TB of transfer on a 10 Gbps port in London is a cheap always-on front end for a crawler, a scheduler or a webhook receiver, with the bulk bytes pushed to an unmetered host
- reliability: no reliability event recorded
- notes: The tracker row and the vendor card agree on price, shape, bandwidth, port speed and location, so no figure in this record rests on the tracker alone. The quoting currency is the pound sterling; the page prints a USD figure beside it and no conversion was done here. The tracker also lists the same GBP 3.50 in Singapore with 1,024 GB of bandwidth rather than 2,048, so the allowance varies by location and the London figure is the one recorded. Unverified: whether the 2 TB is a hard suspend or a throttle, and whether 3.50 is an introductory rate that renews higher, which the card does not say. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - price_on_page: GBP 3.50/month for UK-KVM-1G
- evidence:
  - [2] 2026-10-22: cheapest row: 'SpeedyPage - GBP 3.50 / month', '1 Ryzen Cores (shared)', '1,024 MB RAM', '15 GB NVMe', '2,048 GB/month bandwidth', '10 Gbps port speed', 'London United Kingdom'. The page states 'These are the cheapest VPSs currently offered by SpeedyPage, starting at GBP 3.50 per month'.
  - [1] 2026-10-22: plan card, quoted: 'GBP 3.50 /mo', 'GBP 38.50 /yr', '1 Core', '1 GB DDR5 Memory', '15 GB NVMe Storage', '2 TB Bandwidth @ 10 Gbps', CPU 'AMD Ryzen 7900 / 9700X', 'Up to 5.4 GHz'; the location is chosen in a selector above the cards and was set to 'London, UK'
  - [1] 2026-10-22: the next card is 'GBP 4.99 /mo' with '2 GB' and '30 GB NVMe', and the USD display on the cheapest card reads '4.29 /mo' beside the GBP figure
  - [3] 2026-10-22: home page: the Virtual Servers block reads 'STARTING AT GBP 6.99/mo', struck through, then 'GBP 3.50 /mo', matching the plan card
  - [1] 2026-11-07: the vps page product schema still states the GBP low price 3.50 beside priceCurrency GBP on 2026-11-07 | capture: sha256:6e4471decb1e5d3cbb7d8f5396cffcc1397ee46851d25876945e74d1a6db86aa | quote: "lowPrice": "3.50",
  - [4] 2026-11-07: the cheapest plan's cart prices are unchanged | capture: sha256:995a408b65d332d4160c4d2b583552233ccf2aa73ef2006a1429d44c3a9c54c0 | quote: ### Monthly £3.50 GBP
  - [4] 2026-11-07: the cart configuration page for pid 41 prices monthly, quarterly, semi-annual and annual terms, prints no renewal price and shows no out-of-stock notice | capture: sha256:995a408b65d332d4160c4d2b583552233ccf2aa73ef2006a1429d44c3a9c54c0 | quote: ### Monthly £3.50 GBP ### Quarterly £10.50 GBP ### Semi-Annually £21.00 GBP ### Annually £38.50 GBP
- sources:
  - [1] https://speedypage.com/vps
  - [2] https://vpspricetracker.com/provider/SpeedyPage/vps
  - [3] https://speedypage.com/
  - [4] https://my.speedypage.com/cart.php?a=add&pid=41
