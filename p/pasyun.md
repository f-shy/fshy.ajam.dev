# 帕斯云Nat

> pasyun.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pasyun/ | JSON https://fshy.ajam.dev/api/v1/entity/pasyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 帕斯云Nat (Pasyun NAT)

- `compute/pasyun-nat4-dc1-1` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category NAT VPS | tier 荷兰Nat4-DC1-1
- needs card unknown, phone no, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://cloud.pasyun.com/cart?fid=3&language=english
- price parsed USD 0.45/mo
- free tier: No free tier. 荷兰Nat4-DC1-1 is CNY 3.00 a month, printed '¥3 元 / 月'. The order summary on the configure page totals '¥3.00' and offers monthly, quarterly, semiannual, annual, biennial and triennial cycles, but only the monthly figure is published before a cycle is chosen. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the terms state '服务将在到期/欠费 2-5 天后删除', that is the service is deleted 2 to 5 days after expiry or non-payment | days: 5 | source: [2]
- egress: unlimited traffic under fair use, printed '流量：不限 (合理使用)' | metered: no | free allowance: unlimited under fair use, with no byte figure published | source: [3]
- identity: email | detail: email registration only. The registration page is headed '邮箱注册' and its fields are an email address, a graphic captcha, an emailed code, a password and a confirmation, with a tick for the terms. No phone field, no national ID field and no company field were present in the form source read. Payment rails could not be read without an account, so whether a card is required at the payment step is not established.
- interface: ssh
- limits:
  - per-ip-shaping (binding): 3 forwarded ports on the shared IPv4; the listing states the product supports custom port forwarding, and the port count is the number the buyer chooses the plan by [1]
  - volume-quota: no byte allowance; unlimited under fair use, with sustained peak-bandwidth use limited to 10 to 50 percent of the stated peak after two hours [2]
- binding note: 3 forwarded ports is the smallest inbound budget of any row among documented hosts, so a WireGuard listener plus SSH consumes two thirds of it before anything else runs.
- interface detail: LXC guest; the product is sold with a hostname and a root password at order time, and the vendor's knowledgebase has a NAT SSH login guide
- tooling: any SSH client; the vendor's own Chinese-language control panel
- composes with: a 256 MB box at CNY 3 a month with 3 forwarded ports, bought with an email address alone, which makes it the cheapest monthly-billed machine among documented hosts that needs no card and no phone
- reliability: the terms state there is no refund and no withdrawal of balance ('我们不提供退款服务，充值后无法原路退回'), that a wrong region or a GFW-blocked IP is not grounds for a refund, and that data is not backed up; the marketing page claims '99.9% 在线时间' and '接近99.98%的在线率' with no measurement published
- notes: The cheapest monthly-billed machine among documented hosts, and the one with the lowest identity cost: CNY 3.00 a month is USD 0.4498 at the ECB reference rate of 6.6702 CNY per USD read, and the registration form asks for an email address and nothing else. That combination is rare - the other sub-dollar rows in documented records either need a card (TierHive's USD 3 top-up) or are annual-only. Three things hold it to a caveat rather than a clean qualify. First, 3 forwarded ports is the smallest inbound budget found, so a WireGuard listener and SSH use two of them. Second, the terms refuse refunds in every circumstance including a GFW-blocked IP, and delete the service 2 to 5 days after expiry, so the money is at risk from the first month. Third, no legal entity is named anywhere read: the site describes a brand founded in 2020 and a hosting history from 2016, and prints no company name, registration number or address. Payment rails could not be read, because the cart demands login before it shows a payment method, so whether a card is needed at checkout is unestablished and the email-only claim covers registration only. No page read mentions IPv6 for this product, so the IPv6 column is a dash rather than a no: the third-party comparison tables that list Pasyun as 'IPv4 NAT + IPv6' were not treated as evidence. Unverified: one look at the logged-in payment page, and a ticket asking whether the ports carry UDP.
- evidence note: price, shape, port count, bandwidth and the unlimited-traffic line are quoted from the vendor's own listing and its configure page read; the deletion window and the fair-use shaping rule are quoted from the vendor's own terms page read; the registration form is quoted from the form source read. Not documented: the payment rails, because the cart asks for login before showing a payment method; whether the 3 ports carry UDP; and whether any IPv6 address is included, because no page read mentions IPv6 for this product.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.25
  - shape.disk_gib: 1
  - billing_model: monthly
  - term: monthly, with quarterly to triennial cycles offered
  - m10h_usd: 0.45
  - m24h_usd: 0.45
  - price_arithmetic: CNY 3.00 a month / 6.6702 CNY per USD = USD 0.4498 a month, from the ECB reference rate read on 2026-10-24 with rate date 2026-10-23. Billed monthly, so the money out of pocket each month is CNY 3.00. VPS billing: the machine bills whether it runs or not, so the 10 h/day and 24/7 figures are identical.
  - out_of_pocket_usd: 0.45
  - renewal_usd: same rate; no separate renewal price is published, and the terms state no refund
  - fx: CNY 6.6702 per USD, api.frankfurter.app/latest read 2026-10-24, rate date 2026-10-23
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 3 forwarded ports on the shared IPv4, custom forwarding supported
  - network_out.static_ip: no
  - udp: not stated: no page read says whether the 3 forwarded ports carry UDP
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: not established: the cart requires login before it shows a payment method
  - card_hold: not stated on any page read
  - checkout_fields: email, captcha, emailed code and password at registration; no phone, ID or company field
  - stock: not stated: the listing and the configure page publish no stock count
  - cart_url: https://cloud.pasyun.com/cart?action=configureproduct&pid=37
  - cart_works: priced: the configure page rendered the line item '荷兰Nat4-DC1-1: ¥3.00' with '总价: ¥3.00'
  - product_url: https://cloud.pasyun.com/cart?fid=3&language=english
  - signup_url: https://cloud.pasyun.com/register
  - cart_url_note: the buy link on the listing resolves to the configure page and that page priced the plan at CNY 3.00 in its order summary. The cart was not taken to a payment step, so the payment rails are unknown.
  - other_plans: 荷兰Nat4-DC1-2 CNY 4 for 384 MB and 4 ports; DC1-3 CNY 5 for 512 MB and 5 ports; DC1-4 CNY 6 for 768 MB and 6 ports; DC1-5 CNY 8 for 1 GB and 8 ports; DC1-6 CNY 10 for 1 GB and 10 ports; DC1-7 CNY 15 for 1 GB, 2 GB disk and 15 ports; DC1-8 CNY 20 for 1 GB, 2 GB disk and 15 ports at 10 Gbps. All 1 core, unlimited traffic under fair use.
  - other_regions: the same group page lists 荷兰DC2, 德国DC3, 英国DC1, 摩尔多瓦DC1, 俄罗斯DC1, 乌克兰DC1, 葡萄牙DC1 and 西班牙DC1 as separate product families
- evidence:
  - [1] 2026-10-24: quoted plan: '荷兰Nat4-DC1-1 CPU：1核 内存：256M 硬盘：1G 带宽：50mbps 端口：3个 流量：无限 ¥3 元 / 月' with the buy link 'https://cloud.pasyun.com/cart?action=configureproduct&pid=37'
  - [1] 2026-10-24: quoted product description: '荷兰Nat4 共享IPv4 支持自定义端口转发' and the notice 'Nat4不保证大陆连通性，如果被GFW阻止，请使用代理连接！'
  - [3] 2026-10-24: quoted order summary: '荷兰Nat4-DC1-1: ¥3.00 ... 内存: 256MB ... 端口: 3个 ... 流量: 不限 (合理使用) ... 总价: ¥3.00' with cycles '月 季 半年 年 两年 三年'
  - [3] 2026-10-24: quoted restriction: '禁止DD系统 v2board MTProxyTLS 查到封机' and '不保证大陆连通性 如果被GFW阻止 请使用代理连接'
  - [4] 2026-10-24: the registration page is headed '邮箱注册' and lists only '邮箱', '图形验证码', '发送验证码', '密码', '确认密码', '注册'; the form source carries the fields email, captcha, code, password and checkPassword, with no phone, national ID or company field
  - [2] 2026-10-24: quoted: '服务将在到期/欠费 2-5 天后删除' and '我们不提供退款服务，充值后无法原路退回，我们将拒绝退款' and '延迟太高，IP被墙均不支持更换区域和退款'
  - [2] 2026-10-24: quoted fair-use rule: '服务标示带宽为峰值带宽（非独享带宽），请不要长期占用，否则会被限速峰值带宽的 10%-50% *长时间 = 2小时及以上'
  - [5] 2026-10-24: quoted history claim: '我们2016年开始涉及虚拟主机，2019年涉及云服务器，于 2020 年成立新品牌"帕斯云Nat"' - a brand, with no legal entity named
- sources:
  - [1] https://cloud.pasyun.com/cart?fid=3&language=english
  - [2] https://cloud.pasyun.com/tos.html
  - [3] https://cloud.pasyun.com/cart?action=configureproduct&pid=37
  - [4] https://cloud.pasyun.com/register
  - [5] https://cloud.pasyun.com/
