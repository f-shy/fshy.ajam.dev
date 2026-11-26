# Euronodes

> euronodes.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/euronodes/ | JSON https://fshy.ajam.dev/api/v1/entity/euronodes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Euronodes

- `compute/euronodes` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:06.321Z (live) | stale on 2026-12-08
- url https://euronodes.com/cloud
- price parsed USD 5.12/mo
- free tier: The first row of the vendor's own VPS table: 2 vCores, 4 GB RAM, 100 GB SSD, 20 TB of bandwidth, at EUR 4.54 per month with IPv6 only or EUR 5.24 per month with a dedicated IPv4. The page states 'Dedicated IP (+EUR 0.70) - IPv6 always included', which is exactly the EUR 0.70 gap between the two figures, and the page's structured data marks the offer set as InStock. The next rows are 4 vCores / 8 GB at EUR 7.98, 4 vCores / 16 GB at EUR 16.14, 8 vCores / 16 GB at EUR 19.51, 16 vCores / 32 GB at EUR 38.63, 16 vCores / 64 GB at EUR 50.02 and 32 vCores / 128 GB at EUR 117.12. Locations offered are Portugal and Czech Republic, with Limassol, Frankfurt, Lisbon, Madrid and Prague named in the footer. The tracker lists the same two prices for Lisbon but gives 30,720 GB a month where the vendor states 20 TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 20 TB a month included on every plan; the page advertises no bandwidth overage fees and does not publish a per-TB rate | metered: yes | free allowance: 20 TB a month | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): 20 TB a month is the stated allowance on every row of the table; the page claims 'no hidden fees, bandwidth overages, or surprise charges' but publishes no overage rate, so what happens above 20 TB is unverified [1]
- limits note: 20 TB a month is the stated allowance on every row of the table; the page claims 'no hidden fees, bandwidth overages, or surprise charges' but publishes no overage rate, so what happens above 20 TB is unverified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with full root, custom ISO installation and a Plesk panel API named in the navigation; SSH plus the panel, no VPS API documented on the page read
- composes with: 2 vCores, 4 GB and 100 GB of SSD with 20 TB a month for EUR 4.54 is the best memory-per-euro of the European hosts among evaluated providers, and the 20 TB ceiling is wide enough to run a crawler that also serves bytes.
- reliability: no reliability event recorded
- notes: Prices are recorded in EUR.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 100
  - price_on_page: EUR 4.54/month: the entry 2 vCores / 4 GB row (IPv6 only); EUR 5.24/month with a dedicated IPv4
  - renewal_note: not published: the pricing page read on 2026-11-07 prints a monthly price per row and no renewal price
- evidence:
  - [1] 2026-10-22: first table row quoted: '2 vCores', '4 GB', '100 GB', '20 TB', and a price cell holding two spans, IPv6-only 'EUR 4.54' and with-IP 'EUR 5.24'
  - [1] 2026-10-22: the label above the table reads 'Dedicated IP (+EUR 0.70) - IPv6 always included', and the page title is 'VPS Servers Europe - Uncapped CPU from EUR 4.54/mo'
  - [1] 2026-10-22: structured data on the page: 'priceCurrency: EUR, lowPrice: 4.54, highPrice: 117.12, offerCount: 8, availability: InStock', areaServed Lisbon and Prague
  - [1] 2026-11-07: the first table row prices the 2 vCores / 4 GB entry at EUR 4.54 IPv6-only and EUR 5.24 with a dedicated IPv4 | capture: sha256:e75bc0372343f1a0db78ae066862d3e513e156c93f42aadab96a5ea260da677b | quote: | 2 vCores | 4 GB | 100 GB | 20 TB | €4.54€5.24 |
- sources:
  - [1] https://euronodes.com/cloud
