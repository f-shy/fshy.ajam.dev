# Retzor

> retzor.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/retzor/ | JSON https://fshy.ajam.dev/api/v1/entity/retzor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Retzor

- `compute/retzor` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T17:40:53.067Z (live) | stale on 2026-12-08
- url https://retzor.com/virtual-servers/
- price parsed USD 3.38/mo
- free tier: EUR 3 per month for 1 vCPU, 1 GB ECC REG, 15 GB NVMe, 10 Gbps port with 5 TB included, one IPv4, on Intel Xeon Gold 6240R with VMware, valid in any of the proposed locations. The high-frequency line in Russia (Moscow) is EUR 4 per month for 1 vCPU, 1 GB, 20 GB NVMe at 1 Gbps with 5 TB. The page title states a starting price of EUR 2 per month while the cheapest row in either table is EUR 3, so the title and the table disagree. Three, six and twelve month terms carry 5, 10 and 15 percent off. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB a month on every row, 10 Gbps on the Xeon Gold line and 1 Gbps on the high-frequency line; no overage price stated | metered: yes | free allowance: 5 TB per month | source: [1]
- identity: email | detail: unverified: the register form answered no readable content on 2026-11-07; the form renders only in JavaScript and its fields are not established. The order form and cart sit behind a BILLmanager login
- interface: rest
- limits:
  - volume-quota (binding): 5 TB a month is stated on every row, and the port is 10 Gbps on the Xeon line and 1 Gbps on the high-frequency line, so the byte allowance is reached long before the port saturates. [1]
- limits note: 5 TB a month is stated on every row, and the port is 10 Gbps on the Xeon line and 1 Gbps on the high-frequency line, so the byte allowance is reached long before the port saturates.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: VNC access, resource scaling from the control panel; no public API documented on the page read
- composes with: 5 TB a month on a 10 Gbps port for EUR 3 is the widest pipe per euro among documented hosts, and the location list includes the Netherlands, Moscow and Czechia, so it can serve European egress without a second provider
- reliability: no reliability event recorded
- notes: Source: vps.today index row, then the vendor page. The index names three locations (, ( ), ) and the vendor page says the tariffs are valid in any proposed location without listing them. The EUR 2 in the title is unsupported by the tables read. Rendering and provenance: currency written as EUR.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - monthly_price: EUR 3 per month for the 1 vCPU / 1 GB / 15 GB NVMe Xeon Gold 6240R row; EUR 4 per month for the 1 vCPU / 1 GB / 20 GB NVMe high-frequency row
  - annual_price: not published: no page prints an annual total; term discounts of 5, 10 and 15 percent for 3, 6 and 12 month orders are the only term pricing
  - annual_derived_eur: EUR 30.60 for the 12-month term on the EUR 3 row
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: monthly, with 3, 6 and 12 month orders at 5, 10 and 15 percent off
  - stock: no stock state is printed on the page; every row shows a live Buy link
  - cart_price: unverified: behind a sign-up - the BILLmanager order form answers an Authorization page with no price (probe:cart-retzor-78); the register form renders only in JavaScript
  - price_on_page: EUR 3/month for the 1 vCPU / 1 GB / 15 GB NVMe Xeon Gold 6240R row
  - renewal_usd: not published: the discounts are the only term pricing printed; no renewal figure appears
- evidence:
  - [1] 2026-10-23: cheapest row quoted: '1 vCPU | 1 GB ECC REG | 10 gbps (5TB) | 15 GB NVMe | 3 €/month'; second table '1 vCPU | 1 GB ECC REG | 1 gbps (5TB) | 20 GB NVMe | 4 €/month' for Russia (Moscow)
  - [1] 2026-10-23: page title 'VPS Hosting Plans - Starting at €2/month' against a table whose lowest row is '3 €/month'; term discounts quoted: 'discounts of 5/10/15% are provided with an order period of 3/6/12 months'
  - [1] 2026-11-07: the plan table prices the cheapest Xeon row at 3 €/month | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: | 1 vCPU | 1 GB ECC REG | 10 gbps (5TB) | 15 GB NVMe | 3 €/month | | Buy |
  - [1] 2026-11-07: the page prints percentage term discounts, not an annual figure | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: For these tariffs, discounts of 5/10/15% are provided with an order period of 3/6/12 months, respectively.
  - [1] 2026-11-07: the 12-month term carries the largest discount, 15 percent | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: For these tariffs, discounts of 5/10/15% are provided with an order period of 3/6/12 months, respectively.
  - [1] 2026-11-07: the discounts are the only term pricing printed; no renewal figure appears | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: For these tariffs, discounts of 5/10/15% are provided with an order period of 3/6/12 months, respectively.
  - [1] 2026-11-07: the term ladder is printed on the page | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: For these tariffs, discounts of 5/10/15% are provided with an order period of 3/6/12 months, respectively.
  - [1] 2026-11-07: the cheapest row ends in a live Buy link | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: | 1 vCPU | 1 GB ECC REG | 10 gbps (5TB) | 15 GB NVMe | 3 €/month | | Buy |
  - probe:cart-retzor-78 2026-11-07: the cart answers an Authorization page and prints no price | capture: sha256:00c4c18528942770471bcd049db562e4df544236b261f7bbd2c0e5000e5219a7 | quote: "title": "Authorization"
  - [2] 2026-11-07: the order form is reached only through a login or a registration | capture: sha256:5bfd686ffe618634e02438f47e408309436692fe54cf8955f707a5b19d858b3b | quote: If you don't have an account [Register](https://billing.retzor.com/billmgr?func=register&lang=en&redirect=pricelist%3D78%26project%3D1%26startform%3Dvds%252Eorder%26startpage%3Dvds)
  - [1] 2026-11-07: the page title still states a EUR 2 starting price while the cheapest row is EUR 3 (2026-11-07) | capture: sha256:538957524520a7f09345782969e418c519a4b36521883f5267ebddb2c5ed246f | quote: VPS Hosting Plans - Starting at €2/month | Retzor.com
  - [1] 2026-11-07: the cheapest row and its 5 TB allowance are unchanged on 2026-11-07 | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: | 1 vCPU | 1 GB ECC REG | 10 gbps (5TB) | 15 GB NVMe | 3 €/month | | Buy |
  - [1] 2026-11-07: the cheapest row, its price and its live Buy link are unchanged on 2026-11-07; the fresh capture is byte-identical to the capture the record holds | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: | 1 vCPU | 1 GB ECC REG | 10 gbps (5TB) | 15 GB NVMe | 3 €/month | | Buy |
  - [1] 2026-11-07: the plan table prices the cheapest Xeon row EUR 3 per month | capture: sha256:a52b1d5e2fe744fd6c2a697c9a5498343c642913c861c5e03a4fc2f230de25b1 | quote: | 1 vCPU | 1 GB ECC REG | 10 gbps (5TB) | 15 GB NVMe | 3 €/month | | Buy |
- sources:
  - [1] https://retzor.com/virtual-servers/
  - [2] https://billing.retzor.com/billmgr?startpage=vds&startform=vds.order&pricelist=78&project=1
