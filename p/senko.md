# Senko Digital

> senko.digital | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/senko/ | JSON https://fshy.ajam.dev/api/v1/entity/senko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Senko Digital

- `compute/senko-digital` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T17:40:53.068Z (live) | stale on 2026-12-08
- url https://senko.digital/budget-vps
- price parsed USD 2.58/mo
- free tier: EUR 2.29 per month for DE-BUDGET-1 in Frankfurt: 1 vCPU at 2.7 to 3.7 GHz, 1 GB DDR4, 10 GB NVMe, 125 Mbps port, 4 TB traffic, KVM, 1 IPv4 plus /64 IPv6, basic L3/L4 DDoS protection. Read 2026-11-07 the four Frankfurt budget rows render 'Out of stock' and the four Helsinki rows at the same prices show Order links; on the 2026-10-23 read the reverse held. The budget ladder is EUR 4.49 (2 vCPU / 2 GB / 20 GB / 250 Mbps / 8 TB), EUR 6.59 (3 / 3 / 30 / 375 Mbps / 12 TB) and EUR 8.59 (4 / 4 / 40 / 500 Mbps / 16 TB). | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 4 TB a month on the 125 Mbps budget row, rising to 16 TB on the 4 vCPU row and 85 TB on DE-EPYC-16; no overage price stated | metered: yes | free allowance: 4 TB per month | source: [1]
- identity: email | detail: the register form asks for a first name, a last name, an email address, a password and a country, and states 'The selected country affects which payment methods are available'; GitHub and Google sign-up are offered; no card, phone or ID field
- interface: rest
- limits:
  - volume-quota (binding): 4 TB a month on a 125 Mbps port is the stated allowance, and 125 Mbps can move about 1.35 TB a day, so the monthly byte cap binds first on a busy host; no overage price is stated on the page read. [1]
- limits note: 4 TB a month on a 125 Mbps port is the stated allowance, and 125 Mbps can move about 1.35 TB a day, so the monthly byte cap binds first on a busy host; no overage price is stated on the page read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: own order flow with OS choice across Debian, Ubuntu, AlmaLinux, Rocky, CentOS Stream, Oracle Linux; no API documented on the page read
- composes with: EUR 2.29 for 1 GB, 10 GB of NVMe and 4 TB in Frankfurt is the cheapest documented European row among documented hosts, and the 4 TB allowance makes it usable for moving bytes rather than only for pinging
- reliability: no reliability event recorded
- notes: Source: vps.today index row ('Senko Digital | 10 GB NVMe | 1 GB | 1 x 2.7 GHz | 125 Mbit/s | KVM IPv6 DDoS ! | 209 .'), then the vendor's budget page, which prices the same row at EUR 2.29. The Helsinki stock state matters: the same price is listed there and cannot be ordered. Rendering and provenance: currency written as EUR, and a price the page prints as '2,29 ' is joined as EUR 2.29.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - monthly_price: EUR 2.29 per month for DE-BUDGET-1 and FI-BUDGET-1; EUR 4.49 for the 2 GB rows, EUR 6.59 for the 3 GB rows and EUR 8.59 for the 4 GB rows
  - standard_line_eur: the standard line (senko.digital/virtual-servers, Helsinki) reads EUR 4.49 (FI-EPYC-1: 2 GB DDR5 / 30 GB / 500 Mbps / 10 TB), EUR 8.89 (FI-EPYC-2: 4 GB / 60 GB / 15 TB), EUR 17.59 (FI-EPYC-4: 8 GB / 120 GB / 1 Gbps / 25 TB), EUR 26.19 (FI-EPYC-6: 12 GB / 180 GB / 35 TB), EUR 34.49 (FI-EPYC-8: 16 GB / 240 GB / 45 TB) and EUR 68.19 (FI-EPYC-16: 32 GB / 480 GB / 85 TB)
  - annual_price: not published: the budget and standard pages print only per-month prices; the order form behind the login sells longer periods at unverified prices
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: monthly; the order links carry BILLmanager period parameters for longer terms behind the login, so their prices are unverified
  - stock: DE-BUDGET-1 to DE-BUDGET-4 render 'Out of stock'; FI-BUDGET-1 to FI-BUDGET-4 show Order links (read 2026-11-07; the reverse held on 2026-10-23)
  - cart_price: unverified: behind a sign-up - the BILLmanager order form answers an Authorization page with no price (probe:cart-senko-6233)
  - price_on_page: EUR 2.29/month for DE-BUDGET-1
  - renewal_usd: not published: the plan card and its stock state are all the page prints for the row
- evidence:
  - [1] 2026-10-23: cheapest row quoted: 'DE-BUDGET-1', 'vCPU1 vCPU 2.7-3.7 GHz', 'Memory1 GB DDR4', 'Storage10 GB NVMe', 'Network125 Mbps', 'Traffic4 TB', 'LocationGermanyFrankfurt', '1 x IPv4 included', '/64 IPv6', '2,29 € per month'
  - [1] 2026-10-23: stock state quoted: 'FI-BUDGET-1 … 2,29 € per month … Out of stock', and the same for FI-BUDGET-2 to FI-BUDGET-4, while 'DE-BUDGET-1 … Order' and the larger Frankfurt rows show 'Order'; ladder 'DE-BUDGET-2 … 4,49 €', 'DE-BUDGET-3 … 6,59 €', 'DE-BUDGET-4 … 8,59 €'
  - [2] 2026-10-23: standard line quoted: 'DE-EPYC-1 … 1 vCPU 3.3-5.0 GHz … 2 GB DDR5 ECC … 30 GB NVMe … 500 Mbps … Трафик 10 TB … 4,49 €'; 'DE-EPYC-2 … 4 GB … 60 GB … 15 TB … 8,89 €'; 'DE-EPYC-16 … 16 vCPU … 32 GB … 480 GB … 85 TB … 68,25 €' (read through a search rendering of the vendor URL, not a direct fetch)
  - [1] 2026-11-07: the budget page's raw markup carries the row prices and specs with the stock states (read 2026-11-07) | capture: sha256:3f5382e1bf17a495ad9e5b9656f42cf48aa39de8380169dfb0d80c6916ee6683 | quote: €<!-- -->2,29</span>
  - [1] 2026-11-07: the cheapest budget row prints 2,29 € | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: 2,29 € per month Out of stock
  - [3] 2026-11-07: the standard page's raw markup carries the FI-EPYC ladder (read 2026-11-07) | capture: sha256:15a15e7a53a1d3cab45e44ad69fe658861d831c1060f9deeba4e6c0efdf8e35f | quote: price_value">17,59
  - probe:cart-senko-6233 2026-11-07: the order form answers an Authorization page and prints no price | capture: sha256:1ea38830bc5a1a95b91c844c222751936c6703a147dfcf5dae044e23eab9a4c4 | quote: "title": "Authorization"
  - [1] 2026-11-07: the plan card and its stock state are all the page prints for the row | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: 2,29 € per month Out of stock
  - [1] 2026-11-07: the order link carries period parameters but no prices | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: [Order](https://my.senko.digital/billmgr?datacenter=8&fperiod=1&period_1460=1&period_1481=1&period_2095=1&period_2115=1&period_6233=1&period_6257=1&period_6279=1&period_6301=1&pricelist=6233&startform=v2.vds.order.param&project=2)
  - [1] 2026-11-07: DE-BUDGET-1 renders Out of stock on 2026-11-07 | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: 2,29 € per month Out of stock
  - [1] 2026-11-07: FI-BUDGET-1 shows a live Order link on 2026-11-07 | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: [Order](https://my.senko.digital/billmgr?datacenter=8&fperiod=1&period_1460=1&period_1481=1&period_2095=1&period_2115=1&period_6233=1&period_6257=1&period_6279=1&period_6301=1&pricelist=6233&startform=v2.vds.order.param&project=2)
  - [3] 2026-11-07:  | capture: sha256:47015bd0cc66373af7f3b309695595b8b41cc24cc0f7a57e55598c401951ad7f | quote: 17,59 €
  - probe:cart-senko-6233 2026-11-07: the cart answers an Authorization page and prints no price | capture: sha256:1ea38830bc5a1a95b91c844c222751936c6703a147dfcf5dae044e23eab9a4c4 | quote: "title": "Authorization"
  - [4] 2026-11-07: the register form's required fields, read 2026-11-07 | capture: sha256:8ac6118cbb4306a708df40509756596cc9a980bbeb45161e10cb94f1912bf585 | quote: First name\* Last name\* Email address \* Password\*
  - [1] 2026-11-07: the DE-BUDGET-1 row's shape, traffic, price and stock state, read 2026-11-07 | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: Memory1 GB DDR4 Storage10 GB NVMe Nested VTNo Network125 Mbps Traffic4 TB LocationGermanyFrankfurt ProtectionBasic (L3-L4) KVM 1 x IPv4 included /64 IPv6 3.7 GHz 2,29 € per month Out of stock
  - [1] 2026-11-07: the budget page prices DE-BUDGET-1 EUR 2.29 per month | capture: sha256:0345fd3dfd1dd6105bec5cb7d9c9bab6c316016da3565074a9e4ec1a4548800e | quote: 2,29 € per month Out of stock
- sources:
  - [1] https://senko.digital/budget-vps
  - [2] https://senko.digital/ru/virtual-servers
  - [3] https://senko.digital/virtual-servers
  - [4] https://my.senko.digital/billmgr?func=register&lang=en&redirect=pricelist%3D6233%26project%3D2%26startform%3Dv2%252Evds%252Eorder%252Eparam%26startpage%3Dvds
