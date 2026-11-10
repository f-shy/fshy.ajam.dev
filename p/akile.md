# Akile

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akile/ | JSON https://fshy.ajam.dev/api/v1/entity/akile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Akile

- `compute/akile` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:02.757Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Akile/vps
- price parsed USD 1.87/mo
- free tier: Akile TWHinet_Mini_NAT at 12.50 per month (the page prints a yen/yuan sign before the figure and gives the starting price as 149.99 per year in the same symbol), billed yearly: 1 Intel core (shared), 1,024 MB RAM, 6 GB NVMe, 1,000 GB/month bandwidth, 0.2 Gbps port, IPv4 NAT, Taiwan. Second row VNPT_NAT_Starter at 13.24 per month with 512 MB, 5 GB, 500 GB/month and a 0.2 Gbps port in Vietnam; third JPHyper_Lite at 14.99 per month with 1,536 MB, 10 GB, 1,000 GB/month and a 2.5 Gbps port in Japan. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: metered: the tracker row states a 1,000 GB/month allowance per plan; no first-party egress term was read because the vendor pages rendered no text | metered: yes | free allowance: 1,000 GB/month on the cheapest row (third party) | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1,000 GB/month on a 0.2 Gbps NAT port; the monthly byte allowance is reached long before the port is, and the IPv4 is shared NAT so inbound service is not possible without a port-forward. [1]
- limits note: 1,000 GB/month on a 0.2 Gbps NAT port; the monthly byte allowance is reached long before the port is, and the IPv4 is shared NAT so inbound service is not possible without a port-forward.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor site is a JavaScript store at akile.ai/shop/server?areaId=<n> and the tracker links a per-plan info page, so a client would have to drive the store's own API
- composes with: a NAT IPv4 at 0.2 Gbps suits a control plane, a scheduler or an outbound crawler egress point in Asia; it cannot serve inbound traffic and cannot move bulk bytes
- reliability: no reliability event recorded
- notes: Two vendor paths were read and both were a wall for price text: https://akile.ai/ returned 200 with extraction 'none' and https://akile.ai/shop/server?areaId=6 returned the navigation only, so the number here is the tracker's and stays at confidence reported. The currency is CNY: the tracker's info page states 'The currency is CNY.' (2026-11-07); 149.99 per year and 12.50 per month are consistent with each other at 12x. the rows dated 2026-10-22 carry the fetching tool's own timestamp; the rows dated 2026-11-07 carry captures of the same pages read again. one render of the Taiwan store page settles the NAT port-forward terms.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 6
  - stock: out of stock: the tracker's info pages mark 'In stock now | ✘' for all three rows the record names — TWHinet_Mini_NAT, VNPT_NAT_Starter and JPHyper_Lite (collected 2026-11-06); the vendor's shop renders no stock state to a non-JS reader
  - term: yearly: the tracker marks the row 'yearly Service' and its info page states 'The latest yearly price was ¥149.99'
  - annual_cny: 149.99
  - monthly_cny: not published: the vendor sells the yearly term and prints no monthly rate; the tracker's row normalizes the yearly price to ¥12.50 a month
  - renewal_cny: not published: no page prints a renewal price
  - cart_url: https://akile.ai/shop/server?type=traffic&areaId=6&nodeId=31&planId=980 (the tracker's offer link; the shop is a JavaScript app and renders no price to a non-JS reader)
  - price_on_page: CNY 12.50/month for TWHinet_Mini_NAT (the tracker's normalized monthly figure of the yearly CNY 149.99; the vendor's shop renders no price to a non-JS reader)
- evidence:
  - [1] 2026-10-22: row quoted: 'Akile - 12.50 / month', 'yearly Service', 'cpu 1 Intel Cores (shared)', 'ram 1,024 MB RAM', 'disk 6 GB NVMe', 'bandwidth 1,000 GB/month bandwidth', 'rj45 0.2 Gbps port speed', 'inet IPv4 (NAT)', 'city Taiwan'; section header: 'These are the cheapest VPSs currently offered by Akile, starting at 149.99 per year'
  - [1] 2026-10-22: second and third rows: '13.24 / month' 512 MB / 5 GB / 500 GB per month / 0.2 Gbps / Vietnam; '14.99 / month' 1,536 MB / 10 GB / 1,000 GB per month / 2.5 Gbps / Japan
  - [2] 2026-10-22: 
  - [1] 2026-11-07: the tracker still lists the ¥12.50 a month row with the 1 Intel core, 1,024 MB RAM, 6 GB NVMe, 1,000 GB/month and 0.2 Gbps figures the record states, and the ¥149.99 a year starting price | capture: sha256:2423b24e0ccb95cd76515caecf1537efae702eb07d351edfab8972465f78de84 | quote: ### Akile — ¥12.50 / month
  - [1] 2026-11-07: the tracker still prints the ¥12.50 a month row with the shape and the 1,000 GB a month allowance the record states | capture: sha256:2423b24e0ccb95cd76515caecf1537efae702eb07d351edfab8972465f78de84 | quote: ### Akile — ¥12.50 / month yearly Service cpu 1 Intel Cores (shared) ram 1,024 MB RAM disk 6 GB NVMe bandwidth 1,000 GB/month bandwidth rj45 0.2 Gbps port speed inet IPv4 (NAT) city Taiwan
  - [3] 2026-11-07: the tracker's info page names the currency the record left as the printed symbol | capture: sha256:a3b0ae1af17ae8fad44d29de6c3cf9a21ffc0a14581000a17c3e6631721b2f0c | quote: The currency is CNY.
  - [3] 2026-11-07: the tracker marks the plan out of stock | capture: sha256:a3b0ae1af17ae8fad44d29de6c3cf9a21ffc0a14581000a17c3e6631721b2f0c | quote: | In stock now | ✘ |
  - [4] 2026-11-07: the tracker marks the VNPT_NAT_Starter row out of stock | capture: sha256:f9765d0ded6bacd5a34456992c7bf45b149449e4d948fec1651acc3363498716 | quote: | In stock now | ✘ |
  - [4] 2026-11-07: the tracker's yearly price for VNPT_NAT_Starter is ¥158.88 | capture: sha256:f9765d0ded6bacd5a34456992c7bf45b149449e4d948fec1651acc3363498716 | quote: The latest yearly price was ¥158.88, collected on November 6.
  - [5] 2026-11-07: the tracker marks the JPHyper_Lite row out of stock | capture: sha256:bafcedd316fb1709bd1ed7ae5400e47d22136f7c87bd810280cf3a5a7cc768b7 | quote: | In stock now | ✘ |
  - [5] 2026-11-07: the tracker collects a monthly ¥14.99 and an annual series at ¥12.50 a month normalized for JPHyper_Lite | capture: sha256:bafcedd316fb1709bd1ed7ae5400e47d22136f7c87bd810280cf3a5a7cc768b7 | quote: ⬤ monthly: ¥14.99 ⬤ annual / 12: ¥12.50
  - [3] 2026-11-07: the plan's term is yearly and its price is ¥149.99 | capture: sha256:a3b0ae1af17ae8fad44d29de6c3cf9a21ffc0a14581000a17c3e6631721b2f0c | quote: The latest yearly price was ¥149.99, collected on November 6.
  - [3] 2026-11-07: the tracker's collected yearly price | capture: sha256:a3b0ae1af17ae8fad44d29de6c3cf9a21ffc0a14581000a17c3e6631721b2f0c | quote: The latest yearly price was ¥149.99, collected on November 6.
  - [1] 2026-11-07: the tracker's normalized monthly figure | capture: sha256:2423b24e0ccb95cd76515caecf1537efae702eb07d351edfab8972465f78de84 | quote: ### Akile — ¥12.50 / month
  - [3] 2026-11-07: the page prints one yearly price and no renewal line | capture: sha256:a3b0ae1af17ae8fad44d29de6c3cf9a21ffc0a14581000a17c3e6631721b2f0c | quote: The latest yearly price was ¥149.99, collected on November 6.
  - [6] 2026-11-07: the tracker's offer link resolves to the vendor's shop page for the plan | capture: sha256:b041e47254e275939454db3c7385b808ea2dc8ad748073259441ad3ddf815ef6 | quote: x-web-final-url: https://akile.ai/shop/server?type=traffic&areaId=6&nodeId=31&planId=980
  - [1] 2026-11-07: the tracker's printed row | capture: sha256:2423b24e0ccb95cd76515caecf1537efae702eb07d351edfab8972465f78de84 | quote: ### Akile — ¥12.50 / month
  - [3] 2026-11-07: the tracker's info page names the currency the record's notes left as the printed symbol | capture: sha256:a3b0ae1af17ae8fad44d29de6c3cf9a21ffc0a14581000a17c3e6631721b2f0c | quote: The currency is CNY.
  - [1] 2026-11-07: the tracker's printed row carries the monthly figure the record states | capture: sha256:2423b24e0ccb95cd76515caecf1537efae702eb07d351edfab8972465f78de84 | quote: ### Akile — ¥12.50 / month
- sources:
  - [1] https://vpspricetracker.com/provider/Akile/vps
  - [2] https://akile.ai/
  - [3] https://vpspricetracker.com/info/1601602/Akile/TWHinet_Mini_NAT
  - [4] https://vpspricetracker.com/info/1678709/Akile/VNPT_NAT_Starter
  - [5] https://vpspricetracker.com/info/1560821/Akile/JPHyper_Lite
  - [6] https://vpspricetracker.com/offer/1601602/Akile/TWHinet_Mini_NAT
