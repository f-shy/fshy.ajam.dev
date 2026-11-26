# Linceris

> linceris.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linceris/ | JSON https://fshy.ajam.dev/api/v1/entity/linceris.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Linceris

- `compute/linceris` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-07T11:15:47.348Z (live) | stale on 2026-12-08
- url https://linceris.com/premium-vps
- free tier: EUR 14.99/month for VPS Package 1 in Frankfurt: 2 cores on an AMD Ryzen 9 5950X at 3.4 to 4.9 GHz, 4 GB DDR4, 50 GB NVMe Gen4, a 1 Gbps uplink with unlimited bandwidth under a fair-use term, DDoS protection through DataForest.net, one dedicated IPv4 with a custom DNS entry, and free additional IPs on request. Package 2 is EUR 24.99 for 3 cores, 8 GB and 100 GB; Package 3 is EUR 34.99 for 4 cores, 12 GB and 150 GB; Package 4 is EUR 54.99 for 5 cores, 16 GB and 200 GB; Package 5 is EUR 64.99 for 6 cores, 24 GB and 250 GB, all on the same Ryzen 9 5950X at DDR4 and 1 Gbps. The offer thread of 2026-10-22 sells the same first package at half this price with code FIRSTORDER50 and calls that 'this recurring price'. Order page read 2026-11-07: the cart prices the plan a cent above the page figure on its only billing cycle, monthly, with no setup fee, and the plan is orderable; no annual figure is published. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited bandwidth under a fair-use term, behind a 1 Gbps uplink; the fair-use threshold is not quantified | metered: no | free allowance: unlimited under fair use at 1 Gbps | source: [1]
- identity: any-phone
- interface: rest
- limits:
  - per-ip-shaping (binding): bandwidth is unlimited under a fair-use term, so no byte counter binds and the 1 Gbps uplink is the stated ceiling. The fair-use wording is the real limit and it is not quantified anywhere read. [1]
- limits note: bandwidth is unlimited under a fair-use term, so no byte counter binds and the 1 Gbps uplink is the stated ceiling. The fair-use wording is the real limit and it is not quantified anywhere read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM through VirtFusion with quick OS deploys, a client dashboard, a Discord ticket system and a live chat; no API is documented on the pages read
- composes with: EUR 14.99 for 2 dedicated Ryzen 9 5950X cores, 4 GB of DDR4 and a 1 Gbps port with a half-price first-order code at entry; a fair-use clause with no number is the reason to test the port before scheduling a nightly transfer against it
- reliability: no reliability event observed: the company was registered in March 2026 and the thread is its first offer post, so there is no operating history to read.
- notes: The vendor page read 2026-10-22 and the offer thread agreed on every specification: a Ryzen 9 9950X at 4.3 to 5.7 GHz, DDR5, a 10 Gbps uplink, and EUR 7.50 monthly with code FIRSTORDER50, which the thread calls 'this recurring price'. The page read 2026-11-07 prints a lower CPU model, DDR4, a 1 Gbps uplink and a higher list price on every package, so the thread's figures no longer match the vendor's own page; the cart prices Package 1 monthly one cent above the page figure. Open: what 'fair usage' caps, and whether FIRSTORDER50 recurs on renewal or only on the first invoice despite the wording.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 50
  - monthly_price: EUR 14.99 per month on the marketing page; the cart prices the same plan EUR 15.00 monthly with no setup fee
  - annual_price: not published: the cart's billing-cycle selector offers exactly one term, monthly
  - renewal_price: not published: no page read prints a renewal price; the cart's only printed price is the monthly term
  - billing_term: monthly only: the cart's cycle selector holds a single option (EUR 15.00EUR Monthly)
  - stock: in stock: the cart accepted Package 1 and rendered the configurator (Order, Step 1 of 3) with a free setup fee
  - cart_price: EUR 15.00 per month, no setup fee, from the cart read at cart.php?a=confproduct&i=0 with a warmed session; the marketing page's EUR 14.99 is one cent lower
- evidence:
  - [1] 2026-10-22: vendor plan block quoted: 'VPS Package 1', 'Dedicated Cores', 'EUR 14.99/mo', '2 Cores AMD Ryzen 9 9950X 4.3 / 5.7 GHz', '4GB DDR5 RAM', '50GB NVMe Gen4 SSD Storage', '10Gbps Unlimited Bandwidth (Fair Usage)', 'Dataforest.net DDoS Protection'; page location line: 'Frankfurt am Main, Germany'
  - [2] 2026-10-22: the offer thread states: 'Use promo code FIRSTORDER50 to get this recurring price!'; 'CPU: 2 Cores (AMD Ryzen 9 9950X 4.3 / 5.7 GHz) ... RAM: 4 GB DDR5 ... Storage: 50 GB NVMe Gen4 ... Price: EUR 7.50 monthly (approx $8.15 USD) with code FIRSTORDER50'; 'Network Connectivity: 10Gbps Uplink | Unlimited Bandwidth (Fair Usage) | AS201129'; the company states it was registered in Casablanca, Morocco in March 2026
  - [1] 2026-11-07: the vendor page read 2026-11-07 prices Package 1 at EUR 14.99 and prints the 5950X, DDR4 and 1 Gbps shape | capture: sha256:fdd4908ae393ac8e2b6eb42e8db049326520c754f7b5c417f7f4a098864bb224 | quote: 2 Cores** AMD Ryzen 9 5950X 3.4 / 4.9 GHz - 4GB DDR4 RAM - 50GB NVMe Gen4 SSD Storage - 1Gbps Unlimited Bandwidth (Fair Usage)
  - [1] 2026-11-07: the page prints a 1 Gbps uplink with unlimited fair-use bandwidth | capture: sha256:fdd4908ae393ac8e2b6eb42e8db049326520c754f7b5c417f7f4a098864bb224 | quote: 1Gbps Unlimited Bandwidth (Fair Usage)
  - [1] 2026-11-07: the page prints a 1 Gbps uplink | capture: sha256:fdd4908ae393ac8e2b6eb42e8db049326520c754f7b5c417f7f4a098864bb224 | quote: 1Gbps Unlimited Bandwidth (Fair Usage)
  - [1] 2026-11-07: the vendor page read 2026-11-07 prints the 5950X, DDR4 and 1 Gbps shape | capture: sha256:fdd4908ae393ac8e2b6eb42e8db049326520c754f7b5c417f7f4a098864bb224 | quote: 2 Cores** AMD Ryzen 9 5950X 3.4 / 4.9 GHz - 4GB DDR4 RAM - 50GB NVMe Gen4 SSD Storage - 1Gbps Unlimited Bandwidth (Fair Usage)
  - [2] 2026-11-07: the offer thread names the 9950X, DDR5, the 10 Gbps uplink and the EUR 7.50 coupon price | capture: sha256:25b65e91ba02eb53faa2cadcc1362660a64813d29bb5119c0bf2ee944f03c80b | quote: - CPU: 2 Cores (AMD Ryzen 9 9950X 4.3 / 5.7 GHz) - RAM: 4 GB DDR5 RAM - Bandwidth: 10Gbps Unlimited Bandwidth (Fair Usage) - Price: €7.50 monthly (~$8.15 USD) with code `FIRSTORDER50`
  - [3] 2026-11-07: registration requires a phone number | capture: sha256:0fbb0722ad6bc256b42446db511429074af9e8a132ab878371249b2914925339 | quote: <input type="tel" name="phonenumber" id="inputPhone" class="field" placeholder="Phone Number" value="" autocomplete="tel" required>
  - [3] 2026-11-07: the register form's required phone field | capture: sha256:0fbb0722ad6bc256b42446db511429074af9e8a132ab878371249b2914925339 | quote: <input type="tel" name="phonenumber" id="inputPhone" class="field" placeholder="Phone Number" value="" autocomplete="tel" required>
  - [4] 2026-11-07: the cart's only cycle prices Package 1 at EUR 15.00 monthly | capture: sha256:405d96815beea87b2980ad10a97e01019389cf6bfe0fa13bf1d3bf662f6ceba2 | quote: €15.00EUR Monthly
  - [4] 2026-11-07: the cart's cycle selector holds a single option | capture: sha256:405d96815beea87b2980ad10a97e01019389cf6bfe0fa13bf1d3bf662f6ceba2 | quote: <option value="monthly" selected>
  - [4] 2026-11-07: the cart's only printed price is the monthly term | capture: sha256:405d96815beea87b2980ad10a97e01019389cf6bfe0fa13bf1d3bf662f6ceba2 | quote: €15.00EUR Monthly
  - [4] 2026-11-07: the cart rendered the order configurator for Package 1 | capture: sha256:405d96815beea87b2980ad10a97e01019389cf6bfe0fa13bf1d3bf662f6ceba2 | quote: Order &middot; Step 1 of 3
  - probe:linceris-cart-body 2026-11-07: the cart prices Package 1 EUR 15.00 on its monthly cycle | capture: sha256:405d96815beea87b2980ad10a97e01019389cf6bfe0fa13bf1d3bf662f6ceba2 | quote: Choose Billing Cycle €15.00EUR Monthly
  - [5] 2026-11-07: the warmed-cookie cart read resolved the store page to the configurator cart and priced it | capture: sha256:e869af7616c2382459f14c72a0d76c44321b0f7394ea07ba39c9863365d9540b | quote: "final_url": "https://dashboard.linceris.com/cart.php?a=confproduct&i=0"
  - [1] 2026-11-07: the entry plan's shape, price and fair-use uplink are as the page prints them on 2026-11-07 | capture: sha256:fdd4908ae393ac8e2b6eb42e8db049326520c754f7b5c417f7f4a098864bb224 | quote: 2 Cores** AMD Ryzen 9 5950X 3.4 / 4.9 GHz - 4GB DDR4 RAM - 50GB NVMe Gen4 SSD Storage - 1Gbps Unlimited Bandwidth (Fair Usage)
- sources:
  - [1] https://linceris.com/premium-vps
  - [2] https://lowendtalk.com/discussion/222269/linceris-com-frankfurt-ryzen-9-9950x-kvm-vps-10gbps-dataforest-ddos-protection-free-ips
  - [3] https://dashboard.linceris.com/register.php
  - [4] https://dashboard.linceris.com/cart.php?a=confproduct&i=0
  - [5] https://dashboard.linceris.com/index.php/store/premium-vps/package-1
