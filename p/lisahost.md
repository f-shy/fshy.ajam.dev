# lisahost

> lisahost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lisahost/ | JSON https://fshy.ajam.dev/api/v1/entity/lisahost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## lisahost

- `compute/lisahost` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T17:40:53.065Z (live) | stale on 2026-12-08
- url https://www.lisahost.com/
- price parsed USD 5.25/mo
- free tier: CNY 35 per month as a limited-time price against CNY 50 list, for the US CN2 GIA basic plan: 1 core, 1 GB RAM, 20 GB SSD, 500 GB of traffic a month, one dedicated public IPv4. A CNY 2 one-day trial exists with 1 core, 1 GB, 10 GB SSD and 1 GB of traffic. The page's third block offers further plans from CNY 25 a month without naming their shape. The vendor sells the same catalogue for Hong Kong, Taiwan, Korea, Japan, Vietnam, Singapore, the United States, Germany and the United Kingdom. Order page read 2026-11-07: the cart refuses both the plan and the trial as out of stock, and the cart-side product card prices the basic plan per quarter against a struck list; no annual figure is printed on any page read. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB a month on the CNY 35 row and 1 GB on the trial; no overage price stated | metered: yes | free allowance: 500 GB per month | source: [1]
- identity: email | detail: the register form requires an email address and a password (a country select is present but hidden); no phone or name field; read 2026-11-07
- interface: rest
- limits:
  - volume-quota (binding): 500 GB a month on the CNY 35 row and 1 GB on the CNY 2 trial, both stated on the card, so the byte allowance is the wall; the page states no overage price. [1]
- limits note: 500 GB a month on the CNY 35 row and 1 GB on the CNY 2 trial, both stated on the card, so the byte allowance is the wall; the page states no overage price.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS cart and client area (cart.php); no API documented on the page read
- composes with: CNY 35 for a US CN2 GIA box with a residential-grade IP pool on the same account is the cheapest way among evaluated providers to test whether a target treats a Chinese-optimised route differently from a plain one.
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing ('lisahost VPS'), then the vendor page. The CNY 25 floor is stated without a shape, so it is not classified as a plan. verification criteria: the configuration behind the CNY 25 row and whether the CNY 35 price renews at CNY 50. Rendering and provenance: currency written as CNY.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - monthly_price: CNY 35 per month on the homepage card for the US CN2 GIA basic plan (1 core / 1 GB / 20 GB SSD / 500 GB of traffic), printed against a struck CNY 50 list as a limited-time price
  - annual_price: not published: no page read prints an annual figure; the cart-side product card prices the quarterly term
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: the homepage card prices monthly (月付); the cart-side product card prices the same basic plan per quarter (每季) at CNY 122.00 against a struck CNY 60, limited to 20 units
  - stock: out of stock: the cart refuses the basic plan and the trial with '此配置缺货中, 请选择其他配置购买' - ordering suspended until restocking
  - cart_price: no cart price: the cart answers an out-of-stock notice for the basic plan and for the trial; the cart-side group page card carries the plan's quarterly price
  - price_on_page: CNY 35/month for the US CN2 GIA basic plan (against a struck CNY 50 list)
  - renewal_usd: not published: the cart-side card prints a term price and no renewal figure
- evidence:
  - [1] 2026-10-23: cheapest paid row quoted: '美国CN2 GIA精品网络 - 基础版', '￥ 35元', '月付 原价 50 元，限时特价', '1 核 CPU', '1 GB 内存', '20 GB SSD硬盘', '500 GB 流量', '独立公网IP'
  - [1] 2026-10-23: trial and floor quoted: '美国CN2 GIA精品网络 - 试用', '￥ 2元', '1天试用', '1 GB 流量'; '更多选择 ￥ 25元 起 月付'
  - [1] 2026-11-07: the homepage card prices the basic plan CNY 35 monthly with its shape and 500 GB allowance | capture: sha256:dccf117dc4a37e089a4867c07256606156fc0293a47c7f2b7c0bcd0c6f474e1c | quote: ￥ 35元 月付 原价~~50~~元，限时特价 - 1 核 CPU - 1 GB 内存 - 20 GB SSD硬盘 - 500 GB 流量 - 独立公网IP
  - [1] 2026-11-07: the homepage card prices the basic plan CNY 35 monthly | capture: sha256:dccf117dc4a37e089a4867c07256606156fc0293a47c7f2b7c0bcd0c6f474e1c | quote: ￥ 35元 月付 原价~~50~~元，限时特价 - 1 核 CPU - 1 GB 内存 - 20 GB SSD硬盘 - 500 GB 流量 - 独立公网IP
  - probe:lisahost-g10 2026-11-07: the cart-side card prices the basic plan 122.00 yuan per quarter | capture: sha256:5f524760c8c9beae5b6da0b5338b930959bb9c2b3f2f17f21a8cc3d30b8de31f | quote: <span class="display-4 mb-0 text-center price-cls">122.00元</span>
  - probe:lisahost-g10 2026-11-07: the cart-side card prints a term price and no renewal figure | capture: sha256:5f524760c8c9beae5b6da0b5338b930959bb9c2b3f2f17f21a8cc3d30b8de31f | quote: <span class="display-4 mb-0 text-center price-cls">122.00元</span>
  - probe:lisahost-g10 2026-11-07: the cart-side card prices 122.00 yuan with the per-quarter term beside it | capture: sha256:5f524760c8c9beae5b6da0b5338b930959bb9c2b3f2f17f21a8cc3d30b8de31f | quote: <span class="display-4 mb-0 text-center price-cls">122.00元</span> </div> <span class="text-small text-muted"> 每季
  - probe:lisahost-p7 2026-11-07: the cart refuses the basic plan as out of stock | capture: sha256:5176082dad7e77eadf8a53cf9bf222661224d9a04c154a175c549ea6b05812d8 | quote: 此配置缺货中, 请选择其他配置购买
  - probe:lisahost-p7 2026-11-07: the cart suspends ordering until restocking and prints no price | capture: sha256:5176082dad7e77eadf8a53cf9bf222661224d9a04c154a175c549ea6b05812d8 | quote: 目前该项目缺货，所以订购已被暂停，直到重新补货。
  - probe:lisahost-p23 2026-11-07: the cart refuses the CNY 2 trial as out of stock too | capture: sha256:107627b6a4a2e114483759ce39556ae6ae5e833a19592d1d2cb63c9486ab1a43 | quote: 此配置缺货中, 请选择其他配置购买
  - [2] 2026-11-07: the register form's email field | capture: sha256:f9835df8eeb6c294b687f6fc883b53cafaaae87354baa5787d3a5939c642a37d | quote: <input type="email" name="email" id="inputEmail" class="form-control" value="">
  - [1] 2026-11-07: the entry plan's price, term, shape and 500 GB allowance are unchanged on 2026-11-07 | capture: sha256:dccf117dc4a37e089a4867c07256606156fc0293a47c7f2b7c0bcd0c6f474e1c | quote: ￥ 35元 月付 原价~~50~~元，限时特价 - 1 核 CPU - 1 GB 内存 - 20 GB SSD硬盘 - 500 GB 流量 - 独立公网IP
  - [1] 2026-11-07: the homepage card prices the US CN2 GIA basic plan CNY 35 monthly | capture: sha256:dccf117dc4a37e089a4867c07256606156fc0293a47c7f2b7c0bcd0c6f474e1c | quote: ￥ 35元 月付 原价~~50~~元，限时特价 - 1 核 CPU - 1 GB 内存 - 20 GB SSD硬盘 - 500 GB 流量 - 独立公网IP
- sources:
  - [1] https://www.lisahost.com/
  - [2] https://www.lisahost.com/register.php
