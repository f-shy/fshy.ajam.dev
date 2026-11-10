# Residential-IDC

> residential-service.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/residential-service/ | JSON https://fshy.ajam.dev/api/v1/entity/residential-service.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Residential-IDC (residential-service.com)

- `ip-proxy/residential-idc-us-vds` | paid-only | evidence documented | binding none | category ISP-registered VPS | tier US RCN VDS and US Windstream VDS
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:35:32.672Z (live) | stale on 2026-12-04
- url https://residential-service.com/index.php?rp=%2Fstore%2Fus-rcn-vds
- free tier: No free tier. The store lists US RCN VDS (Ashburn, Virginia) and US Windstream VDS (Chicago, Illinois), each 'Starting at $15.00 USD per month', with a 100 Mbps peak port, a free choice of configuration, and the notice that proxy and large-scale relay use is banned. The RCN product page answered an out-of-stock notice on 2026-11-03. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The product page for US RCN VDS states the item is out of stock and orders are suspended.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a rented machine and its address, not stored bytes | source: [1]
- egress: The store rows state a 100 Mbps peak port and no byte allowance or overage price, so whether traffic is capped is unverified. | metered: no | free allowance: unverified: no byte allowance stated on the store rows | source: [1]
- identity: email | detail: The labels of the individual fields were not rendered in the capture, so whether a phone number or a postal address is required is unverified. The kind records an email as the floor.
- interface: unknown
- limits:
  - per-ip-shaping: 100 Mbps peak bandwidth on both US lines [1]
- limits note: Stock is the deciding fact: the RCN product page states the item is out of stock and orders are suspended.
- binding note: No byte or request limit is stated, so none binds. What decides the record is stock and the registration class of the delivered address.
- interface detail: A virtual dedicated server (VDS) with one fixed address; the access method is not stated on the store rows read. The store rows state 'no mainland China optimisation, pure international network'.
- tooling: An SSH or RDP client, whichever the image supports, plus a proxy or tunnel daemon the user installs on the machine. The vendor's store rows ban 'airport' proxy services and large-scale proxy access, so a heavy relay use is out of the offer's terms as written. The vendor publishes no proxy endpoint and no API on the pages read.
- composes with: A Worker opens an outbound connection to the server's fixed address and the server makes the upstream request, so the upstream sees the registered network of the test addresses instead of AS13335 (RCN and Windstream registrants in ARIN).
- reliability: A forum review list rates the vendor's RCN line as middling-to-good address quality with a small port that needs a relay. Stock was zero on the RCN product when read.
- notes: Registry lookups of the two published test addresses on 2026-11-03: 64.20.4.1 is a WINDSTREAM assignment announced by AS7029 Windstream Communications, so the registrant and the announcing network agree and name an access ISP. 67.103.169.0 is an RCN assignment announced by AS20115 Charter Communications, so the registrant is RCN and the announcing network is Charter. In both cases the registrant is a consumer-network operator and not a hosting company. They are published test addresses, not delivered ones. The RCN product page states the item is out of stock, so the RCN line could not be bought on the day.
- evidence note: Prices, ports, stock and the published test addresses are documented from the vendor's store pages. The registry reading of the two test addresses is measured with ARIN RDAP and RIPEstat on published test addresses, not on delivered ones. The forum rating is reported. Identity fields are unverified.
- extras:
  - rung: 5
  - rung_note: The offer is a claim about the registration class and the registry lookups tested exactly that on the two published test addresses.
- evidence:
  - [1] 2026-11-03: the store labels the product a native residential IP | capture: sha256:e2217675be6131cb89d0b1ca007a7f14822d66b383e6f2496d57d16e77a3fa88 | quote: 原生住宅IP
  - [1] 2026-11-03: the product starts at $15.00 USD per month | capture: sha256:e2217675be6131cb89d0b1ca007a7f14822d66b383e6f2496d57d16e77a3fa88 | quote: $15.00 USD
  - [1] 2026-11-03: the vendor publishes the RCN test address 67.103.169.0 | capture: sha256:e2217675be6131cb89d0b1ca007a7f14822d66b383e6f2496d57d16e77a3fa88 | quote: 测试IP：67.103.169.0
  - [1] 2026-11-03: the vendor publishes the Windstream test addresses 64.20.4.1 and 64.20.5.1 | capture: sha256:e2217675be6131cb89d0b1ca007a7f14822d66b383e6f2496d57d16e77a3fa88 | quote: 测试IP：64.20.4.1、64.20.5.1
  - [1] 2026-11-03: airport proxy services and large-scale proxy access are banned | capture: sha256:e2217675be6131cb89d0b1ca007a7f14822d66b383e6f2496d57d16e77a3fa88 | quote: 禁止机场及大规模代理接入
  - [2] 2026-11-03: the US RCN VDS product page states the item is out of stock and orders are suspended | capture: sha256:b4d048b7712fca65bac2a2ae3af7bbaafde23eab1fad45c02d7654d3b33366d2 | quote: 目前该项目缺货，所以订购已被暂停，直到重新补货
  - [3] 2026-11-03: registration requires confirming the currency is USD or no products are shown | capture: sha256:b3dc41fa1ff7839020c4cd4ad391219f5d4061e4e6d492aedb3376e08d03116c | quote: 注册时请确认货币为USD，否则将不会显示产品
  - probe:67.103.169.0 2026-11-03:  | capture: sha256:3d306611e4ef53ced281a97e0030ba8d057f5b560750c90400f4eb10f080b2a5 | quote: "name" : "RCN"
  - probe:ripe-67.103.169.0 2026-11-03: RIPEstat network-info: the RCN test address is announced by AS20115 | capture: sha256:8fb441d12a7fb212185604ec0ebc89a6fa0d640ac9092e731c8bf15223ec9d89 | quote: "asns":["20115"]
  - probe:AS20115 2026-11-03: RIPEstat as-overview: AS20115 holder is Charter Communications | capture: sha256:20b86cadeeba4a11cb4feee4c3cc42b88ac97b71d400fac8875f2378e9beeb28 | quote: CHARTER-20115 - Charter Communications LLC
  - probe:64.20.4.1 2026-11-03:  | capture: sha256:f6df8a656d0ac092c21adf7ed940610c8e3fe07b38960bbf7988f8033ec051b3 | quote: "name" : "WINDSTREAM"
  - probe:ripe-64.20.4.1 2026-11-03: RIPEstat network-info: the Windstream test address is announced by AS7029 | capture: sha256:6465d4fc3745432f93105e198f881913bb0ba9ee60b0341679e374b6dbf21592 | quote: "asns":["7029"]
  - probe:AS7029 2026-11-03: RIPEstat as-overview: AS7029 holder is Windstream Communications | capture: sha256:7e746b195499e7b3fce561b09cbe11b6522d70e1fa5f47bc104e25c4dc8cc561 | quote: WINDSTREAM - Windstream Communications LLC
  - [4] 2026-11-03: a forum review list says the vendor uses RCN as its ISP with middling-to-good address quality | capture: sha256:d87221c7a0ade538abdee839d90e04a75a376eb9e055f9afce7daeb8a53a2416 | quote: 使用 RCN ISP，IP质量中上
  - [4] 2026-11-03: the same list says the port is small and needs a relay line | capture: sha256:d87221c7a0ade538abdee839d90e04a75a376eb9e055f9afce7daeb8a53a2416 | quote: 带宽口小，需配线路鸡
- sources:
  - [1] https://residential-service.com/index.php?rp=%2Fstore%2Fus-rcn-vds
  - [2] https://residential-service.com/index.php?rp=%2Fstore%2Fus-rcn-vds%2Frcn-vds
  - [3] https://residential-service.com/register.php
  - [4] https://www.nodeseek.com/post-321780-1
