# upyun.cc

> upyun.cc | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upyun/ | JSON https://fshy.ajam.dev/api/v1/entity/upyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## upyun.cc (云上互联)

- `compute/upyun-sg-nat-2` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category NAT VPS | tier 新加坡NAT 套餐二 (Singapore NAT plan 2)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:44:00.000Z (live) | stale on 2026-11-24
- url https://upyun.cc/store/nat-vpssg
- price parsed USD 1.5/mo
- free tier: No free tier. 新加坡NAT 套餐二 is CNY 10.00 a month: 512 MB RAM, 1 VCPU, 3 GB disk, 5 TB traffic at 500 Mbps, 10 fixed ports (1 SSH + 9 PORT). The page prints 库存 4 (stock 4) beside it, while 套餐一 at CNY 5.00 shows 0 available. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: not stated on any page read; the product page states '此套餐不支持退款' (this plan does not support refunds) and no deletion window for an unpaid service is published | source: [1]
- egress: 5 TB a month at 500 Mbps, and the vendor states the allowance resets free on request: '流量用完可以免费重置，发工单即可。' (when traffic runs out it can be reset free of charge by opening a ticket) | metered: yes | free allowance: 5 TB, resettable by ticket | source: [1]
- identity: email | detail: no card at registration, and no standalone registration form either: the register page states '要注册账户，请购买我们的产品' (to register an account, please purchase our product), so the account is created at checkout. What the checkout asks for was not read, so the card situation at the payment step is unverified rather than absent. No card hold or authorisation amount is stated anywhere read.
- interface: ssh
- limits:
  - per-ip-shaping (binding): 10 fixed ports: '10个固定端口（1SSH+9PORT）' - one reserved for SSH and nine for the buyer [1]
  - volume-quota: 5 TB a month, resettable free by ticket rather than a hard stop [1]
  - pull-count: stock is four units on 套餐二 and zero on 套餐一, so the cheaper rung cannot be bought today [1]
- binding note: nine usable ports is the tightest number, and the box is in Singapore where latency to Europe is high; the 5 TB allowance is not a constraint because it resets on request.
- interface detail: Root on a container over SSH on the dedicated SSH port among the 10 fixed ports. The vendor does not name the virtualization on the plan card; the sibling Japanese product line and the port scheme match the LXC NAT pattern used by its peers.
- tooling: any SSH client; WHMCS-style billing panel; no API documented.
- composes with: USD 1.496 a month for 512 MB and 3 GB with 5 TB of resettable traffic in Singapore, which is the only Singapore NAT row among documented hosts that is both in stock and priced under the line; it sits exactly at the boundary and a weaker exchange rate would push it over.
- reliability: no reliability event observed. The vendor runs a status page at upyun.cc and states on the plan card that the product does not support refunds.
- notes: This row sits exactly on the line: CNY 10.00 converts to USD 1.4959 at the rate used here, which is under USD 1.50 by four thousandths of a dollar. A rate move of 0.3 percent would put it over, and that is the whole reason it is recorded as a caveat rather than a clean qualification - the price is real and the stock is real, but the margin to the threshold is inside the exchange-rate noise. The cheaper CNY 5.00 rung on the same page is out of stock, as is the whole Japanese line, so the in-stock offer is the dearer of the two. The vendor's own traffic term is unusually generous in a way that matters: the allowance resets free on ticket rather than cutting the box off. Not established: the virtualization type, the payment rails, and whether the 9 ports are assigned or chosen. The storefront title is 云上互联, and the same operator name appears in a Chinese NAT vendor index that lists it under JP/SG/FL locations.
- evidence note: the CNY 10.00 monthly price, the shape, the 10-port split, the 5 TB resettable allowance and the stock count of 4 are quoted from the vendor's own store page read. The registration-at-checkout behaviour is quoted from the vendor's own register page. The payment step and the virtualization type were not read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.5
  - shape.disk_gib: 3
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 1.496
  - m24h_usd: 1.496
  - price_arithmetic: CNY 10.00 a month, billed monthly; 10.00 / 6.684864 = USD 1.4959, rounded to USD 1.496. Rate: 1 USD = CNY 6.684864 (open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000). A VPS bills whether it runs or not, so 24/7 and 10 h/day are the same.
  - out_of_pocket_usd: 1.496
  - first_payment_usd: 1.496
  - renewal_usd: same CNY 10.00 a month; no promotional price and no end date printed
  - stock: in stock: the store page prints '4 可用' (4 available) beside 新加坡NAT 套餐二, read 2026-10-24, while 套餐一 prints '0 可用'
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 10 fixed ports on a shared IPv4 (1 SSH + 9 usable); no IPv6 is claimed on this plan card
  - network_out.static_ip: no
  - network_out.ipv6: no
  - signup_url: https://upyun.cc/store/nat-vpssg/xin-jia-po-nat-tao-can-er
  - cart_url: https://upyun.cc/store/nat-vpssg/xin-jia-po-nat-tao-can-er
  - ipv6_only: no
  - nat_config.ports_tcp: 9
  - nat_config.ssh_port_included: yes
  - nat_config.ports_assigned_or_chosen: the page says '10个固定端口（1SSH+9PORT）', which reads as ten fixed ports of which one is reserved for SSH; it does not say whether the buyer chooses the mapping or the provider assigns it
  - payment_methods: not read: the checkout is behind the account
  - card_hold: not established; no hold is stated on any page read
  - checkout_fields: not read
  - udp: not stated on any page read
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = CNY 6.684864
- evidence:
  - [1] 2026-10-24: quoted product block: '新加坡NAT 套餐二 | 4 可用 | 512MB 内存 | 1 VCPU | 3GB 磁盘 | 5TB 流量 | 500Mbps 宽带 | 10个固定端口（1SSH+9PORT）| 流量用完可以免费重置，发工单即可。| 此套餐不支持退款 | CNY 10.00 每月'
  - [1] 2026-10-24: quoted the cheaper rung, out of stock: '新加坡NAT 套餐一 | 0 可用 | 256MB 内存 | 1 VCPU | 2GB 磁盘 | 2TB 流量 | 500Mbps 宽带 | 10个固定端口（1SSH+9PORT）| CNY 5.00 每月'
  - [2] 2026-10-24: the Japanese sibling line is fully sold out: '日本NAT 套餐一 | 0 可用 ... CNY 5.00' and '日本NAT 套餐二 | 0 可用 ... CNY 10.00'
  - [3] 2026-10-24: quoted: '要注册账户，请购买我们的产品' - there is no standalone registration form; the page offers only a login and a password reset
  - [1] 2026-10-24: the per-plan order link, read from the markup: '<a href="/store/nat-vpssg/xin-jia-po-nat-tao-can-er" class="btn btn-success btn-sm btn-order-now" id="product17-order-button">立即订购</a>' - the storefront uses a product slug, not a numeric pid
- sources:
  - [1] https://upyun.cc/store/nat-vpssg
  - [2] https://upyun.cc/store/nat-vps3
  - [3] https://upyun.cc/register.php
