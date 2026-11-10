# George DC

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/george-dc/ | JSON https://fshy.ajam.dev/api/v1/entity/george-dc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## George DC

- `compute/george-dc` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:33.098Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/George_DC/vps
- price parsed USD 6.6/mo
- free tier: The vendor's cheap-VPS page (2026-11-07) lists only the Dallas EPYC line: GeorgeLite USD 6.60 per month, or USD 5.50 a month with annual payment (2 vCPU, 4 GB DDR4, 80 GB NVMe, unmetered bandwidth, 1 Gbps port, 1 IPv4 plus a /64 IPv6, KVM); GeorgePro USD 13.20 per month or USD 10.33 with annual; GeorgeFlex USD 24.00 per month or USD 20.00 with annual. The GeorgeStarter Las Vegas plan and the tracker's yearly row, both read 2026-10-22, are not re-confirmed by today's page: GeorgeStarter is no longer listed, and the tracker row stays unverified at the vendor. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the vendor's own plans state unmetered bandwidth; the tracker states a 2,000 GB monthly allowance for the yearly plan it lists. No overage rate is published | metered: no | free allowance: unmetered as stated by the vendor; 2 TB a month as stated by the tracker | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): the tracker states 2,000 GB a month for the yearly plan; the vendor's own plans state unmetered bandwidth on a 1 Gbps port, so the byte wall depends on which plan is real and is unverified [1]
- limits note: the tracker states 2,000 GB a month for the yearly plan; the vendor's own plans state unmetered bandwidth on a 1 Gbps port, so the byte wall depends on which plan is real and is unverified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, a client area and a status page; benchmark output is published per plan. No API documented on the pages read
- composes with: if the yearly plan the tracker lists exists at USD 10.99 it is the cheapest 4 GB machine among evaluated providers by a wide margin, which is why it is worth a second look rather than a dismissal; as sold on the vendor's own page at USD 4.60 a month it is competitive but not exceptional.
- reliability: no reliability event recorded
- notes: The tracker's yearly plan was not found on the cheap-VPS page or on the promotions page, both read the same day, so the headline figure is reported and the vendor's own prices are carried beside it. The promotions page runs a countdown that had already expired at zero, which is a reason to doubt that any price on it is live. verification criteria: whether the USD 10.99 yearly plan still exists, which needs the order form or the vendor directly.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 40
  - monthly_usd: 6.6
  - annual_usd: 66.0
  - renewal_usd: not published: the plan cards print no renewal price and the carts price nothing (out of stock)
  - term: monthly USD 6.60, or annual at USD 5.50/mo (USD 66.00 a year) as the card states; the cart prices nothing because the product is out of stock
  - in_stock: no: the GeorgeLite and GeorgePro order pages answer the WHMCS out-of-stock page and price nothing
  - cart_url: https://desk.georgedatacenter.com/store/dallas-amd-7443p/georgelite
  - cart_note: the WHMCS store answers 200 with an 'Out of Stock' page for GeorgeLite and GeorgePro alike and prices nothing; the session-warmed cart probes found no price string in either body
- evidence:
  - [1] 2026-10-22: row quoted from the Cheapest VPSs table: 'starting at $10.99 per year', '$0.92 / month', 'yearly Service', '2 Intel Cores (shared)', '4,000 MB RAM', '40 GB NVMe', '2,000 GB/month bandwidth', '1 Gbps port speed', 'U.S.A.'
  - [2] 2026-10-22: 'GeorgeStarter' card: '$4.60 /monthly', 'or $3.83/mo with annual payment', '2 vCPU', '4GB DDR4', '80 GB NVMe', 'Unmetered Bandwidth', 'Port 1Gigabit', '1 IPV4 /64 IPV6', KVM, in Las Vegas
  - [3] 2026-10-22: the promotions page is headed 'Exclusive Yearly Promotions' with a countdown at zero, and its first listing is a 4 vCPU / 8GB DDR3 / 3TB HDD Las Vegas plan at '$10.00 / mon' with 'Only 1 units left'
  - [2] 2026-11-07: today's cheap-VPS page prices GeorgeLite at USD 6.60 monthly and no longer lists GeorgeStarter | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: $6.60 /monthly
  - [2] 2026-11-07: the GeorgeLite card prices USD 6.60 a month | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: $6.60 /monthly
  - [2] 2026-11-07: the GeorgeLite card prices the annual term at USD 5.50 a month | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: or $5.50/mo with annual payment
  - [2] 2026-11-07: the page's order lines state no contract and print no renewal figure | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: No contract required, cancel any time
  - [2] 2026-11-07: the card states the two billing terms | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: or $5.50/mo with annual payment
  - [4] 2026-11-07: the vendor's own store suspends orders for GeorgeLite | capture: sha256:4ad5255b0e31f250814d261af3f010036dfa968b102f582cb2b28b1ab3c41bb8 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available
  - [2] 2026-11-07: the cheap-VPS page's Order Now button for GeorgeLite links this store page | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: [Order Now](https://desk.georgedatacenter.com/store/dallas-amd-7443p/georgelite)
  - probe:https://desk.georgedatacenter.com/store/dallas-amd-7443p/georgepro 2026-11-07: the GeorgePro cart probe found the out-of-stock marker and no price, matching the GeorgeLite probe | capture: sha256:63292032e02a1592824bddbea06d1f52e39ff8254f55c8aa739473b0642268e5 | quote: "stock": ["out of stock"]
  - probe:https://desk.georgedatacenter.com/store/dallas-amd-7443p/georgelite 2026-11-07: the session-warmed GeorgeLite cart resolves but carries no price string, only the out-of-stock marker | capture: sha256:02cb0ea243f3afb582bff038e6def341f0f0fd36e6f1505fad11fe09e4b8d5d3 | quote: "verdict": "no-price"
  - [2] 2026-11-07: the Dallas line's entry card still prices USD 6.60 monthly, and the page now also prints annual rates | capture: sha256:b8567a8eadeac9136c0c350309646b67397578c3a1b6710af5a2723b6a2be5b7 | quote: $6.60 /monthly
- sources:
  - [1] https://vpspricetracker.com/provider/George_DC/vps
  - [2] https://www.georgedatacenter.com/cheapvps.php
  - [3] https://www.georgedatacenter.com/promo.php
  - [4] https://desk.georgedatacenter.com/store/dallas-amd-7443p/georgelite
