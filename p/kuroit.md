# Kuroit

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kuroit/ | JSON https://fshy.ajam.dev/api/v1/entity/kuroit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kuroit

- `compute/kuroit` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:35.517Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Kuroit/vps
- free tier: GBP 3.00/month (vendor cart 2026-11-07): 1 vCore Intel Gold 6148, 1 GB DDR4 RAM, 15 GB SSD/NVMe, 1 TB bandwidth, 1 Gbps port with 10 Gbps a GBP 2.50 add-on, IPv4 and IPv6, Toronto. The cart prices every term it offers the same - 1, 3, 6 and 12 months at GBP 3.00/month, no prepay discount - with GBP 0.00 setup and GBP 3.00 total due today, so the 12-month term totals GBP 36.00 (12 x GBP 3.00). The cart accepted the add with no stock warning, so the plan is in stock. No renewal price is published. The tracker lists a cheaper GBP 2.25/month plan (2 cores, 2,048 MB RAM, 25 GB NVMe, 10 Gbps, Toronto) whose card still carries no order link, so GBP 3.00 stays the cheapest offer the page presents as orderable. The vendor homepage states VPS servers start at 3 GBP a month, with the pound sign written GBP for ASCII. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month included per the vendor cart ('1TB Bandwidth'); extra bandwidth is bought through a slider in the cart whose price the page computes client-side and is not readable in the served HTML; no overage price or policy page read | metered: yes | free allowance: 1 TB | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 1 TB a month is the whole egress budget on the GBP 3.00 plan; the 15 GB NVMe disk is the second limit. [1]
- limits note: 1 TB a month is the whole egress budget on the GBP 3.00 plan; the 15 GB NVMe disk is the second limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: my.kuroit.com runs the user area and per-location WHMCS store pages; kuroit.com documents a CLI and API access; the Toronto store page answered 403 (bot challenge) to automated retrieval, so no plan table was read from the store itself.
- composes with: GBP 3.00 for 1 GB RAM and 15 GB NVMe is a scheduler or a crawler front end, not a store: 1 TB a month is the entire egress budget, so the archive and the served pages have to live on a host with either a large monthly allowance or no metering
- reliability: no reliability event recorded
- notes: Kuroit provides global VPS hosting across North America, Europe, and Asia.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
- evidence:
  - [1] 2026-10-22: Kuroit card, with the pound sign written GBP for ASCII: the price line prints 3.00 with the pound sign and '/ month'; the rest quotes verbatim as '1 Intel Cores (shared)', '1,024 MB RAM', '15 GB NVMe', '1,024 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'Toronto Canada'. The raw HTML carries a live order link /offer/1804245/Kuroit/CA_AVA_1_15GB_Disk_1vCore_1GB_RAM
  - [1] 2026-10-22: the cheaper card, priced 2.25 in the same currency and quoted verbatim as '2 Intel Cores (shared)', '2,048 MB RAM', '25 GB NVMe', '10 Gbps port speed', 'Toronto Canada', has its Go control rendered as a span with class 'button_card button_bar_short button_bar_right button_disabled', so no order link is published for it
  - [2] 2026-10-22: product grid quoted, with the pound sign written GBP for ASCII: 'VPS Servers ... Starting at GBP 3/Month' and 'Storage Servers ... Starting at GBP 3/Month'; the page also documents a CLI ('kuro deploy --region ind-jal') and names 12 locations including Toronto and Auckland
  - [3] 2026-11-07: the tracker's order link resolves to the vendor's WHMCS cart (the page's own final URL is my.kuroit.com/cart.php?a=confproduct&i=0), which prices CA-AVA-1 at GBP 3.00 for the 1-month term | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: 1 Month Price - £3.00 GBP
  - [3] 2026-11-07: the cart prices the 12-month term at GBP 3.00, the same as every other term | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: 12 Month Price - £3.00 GBP
  - [3] 2026-11-07: the cart's summary shows Setup Fees GBP 0.00 | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: <span class="pull-left float-left">Setup Fees:</span> <span class="pull-right float-right">£0.00 GBP</span>
  - [3] 2026-11-07: the cart's Total Due Today is GBP 3.00 | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: <span class="amt">£3.00 GBP</span> <span>Total Due Today</span>
  - [3] 2026-11-07: the cart's product line names the plan CA-AVA-1 | 15GB Disk - 1vCore - 1GB RAM in the Toronto CA group | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: CA-AVA-1 | 15GB Disk - 1vCore - 1GB RAM
  - [1] 2026-11-07: the tracker's current card prices the same plan GBP 3.00/month with 1,000 GB/month bandwidth, 1 Gbps port, IPv4 + IPv6, Toronto | capture: sha256:ad03421b49c93f3a81d88ba18c581e29f51ebb02d3eeac509fe7108b44bc1fcf | quote: ### Kuroit — £3.00 / month cpu 1 Intel Cores (shared) ram 1,024 MB RAM disk 15 GB NVMe bandwidth 1,000 GB/month bandwidth rj45 1 Gbps port speed inet IPv4 + IPv6 city Toronto Canada
  - [1] 2026-11-07: the GBP 2.25 card's Go control still carries no link, so it stays unorderable from the tracker | capture: sha256:ad03421b49c93f3a81d88ba18c581e29f51ebb02d3eeac509fe7108b44bc1fcf | quote: [Info](https://vpspricetracker.com/info/1840466/Kuroit/LE_SALE_Toronto_CA_2vCore_2GB_RAM_25GB_Space)Go
  - [3] 2026-11-07: the vendor cart's plan description states 1TB Bandwidth | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: 1TB Bandwidth
  - [3] 2026-11-07: the cart prices CA-AVA-1 at GBP 3.00 on the 1-month and 12-month terms with a GBP 3.00 total due today, and accepted the add with no stock warning | capture: sha256:5dda6b97fe478cd51bfdf7e4a43d714223ce0a1cf5dea4403d21239f7ed914f5 | quote: 1 Month Price - £3.00 GBP ... 12 Month Price - £3.00 GBP ... Total Due Today
- sources:
  - [1] https://vpspricetracker.com/provider/Kuroit/vps
  - [2] https://www.kuroit.com/
  - [3] https://vpspricetracker.com/offer/2112644/Kuroit/CA_AVA_1_15GB_Disk_1vCore_1GB_RAM
