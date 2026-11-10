# Narwhal Cloud

> fuckip.me | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fuckip/ | JSON https://fshy.ajam.dev/api/v1/entity/fuckip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Narwhal Cloud (独角鲸云, fuckip.me)

- `compute/narwhal-cloud-nat` | dead | evidence documented | binding per-ip-shaping | category NAT VPS | tier not published
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://fuckip.me/
- free tier: No price is published anywhere reachable without an account. A Chinese blog post dated 2024 describes the plans as about CNY 1.3 a month and roughly USD 1.7 a year for 1 core, 128 MB and 500 GB, but that is a third-party post and not the vendor's own page. The vendor's own landing page states only '提供高性价比的便宜 NAT VPS 服务' (high value cheap NAT VPS). | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: no deletion interval after expiry was published | source: [2]
- egress: not published on any page reachable without an account, so whether traffic is metered is unknown; recorded as unmetered with that caveat rather than as a claim | metered: no | free allowance: not published | source: [1]
- identity: email | detail: registration at dash.fuckip.me/register offers only 'Continue with Google' and 'Continue with GitHub' plus a terms tick. There is no email-and-password form, so the identity cost is a Google or GitHub account rather than an email address. No card, phone, address or ID field is requested at registration. Payment rails are not published on any page reachable without an account.
- interface: ssh
- limits:
  - per-ip-shaping (binding): shared IPv4 with port forwarding, with custom forwarding rules supported; no port count published [1]
- binding note: the product is defined entirely by a shared IPv4 and forwarded ports, and neither the port count nor the price is published, so there is nothing to price or size.
- interface detail: NAT VPS with shared IPv4 and port forwarding, per the vendor's own description; the panel is at dash.fuckip.me
- tooling: any SSH client; a web dashboard; the vendor publishes its upstream supplier list
- composes with: not usable as a priced row: the vendor publishes no plan, no price and no stock anywhere a buyer can reach without an account, and registration is OAuth-only
- reliability: no uptime figure published
- notes: The vendor operates as an infrastructure reseller sourcing from upstream providers including VmRack, Oracle Cloud, BandwagonHost, Hytron, and HyeHost.
- evidence note: the absence of a published price, the OAuth-only registration, the shared-IPv4 port-forwarding model, the terms and the supplier list are all quoted from the vendor's own pages read. The CNY 1.3 and USD 1.7 figures in the notes are a third-party blog post and are marked as reported, not used as a price.
- extras:
  - billing_model: unknown
  - term: unknown
  - price_arithmetic: not computed: no price is published on any page reachable without an account. The third-party figure of about CNY 1.3 a month is reported, is from a 2024 post, and is not used in arithmetic. A dash rather than a guess.
  - renewal_usd: not published
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: shared IPv4 with custom port forwarding; no count published
  - network_out.static_ip: no
  - udp: not stated: no page read says whether the forwarded ports carry UDP
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: not published: a Chinese blog reports a WeChat QR top-up before ordering, but that is reported and not read from the vendor
  - card_hold: not stated on any page read
  - checkout_fields: Google or GitHub OAuth plus a terms tick; no email, card, address, phone or ID field
  - stock: not published anywhere reachable without an account
  - cart_works: unknown
  - product_url: https://fuckip.me/
  - signup_url: https://dash.fuckip.me/register
  - cart_url_note: recorded as null because no cart or product URL is published; the only route to a plan is an OAuth login to the dashboard, which does not create.
  - upstreams: VmRack (US Los Angeles, CN2 GIA / AS9929 / CMIN2), Oracle Cloud, BandwagonHost, Hytron, HyeHost (UK, AS47272), PDXNET (UK and Europe, AS52025), HostDzire and ZLIDC
- evidence:
  - [1] 2026-10-24: the landing page states only '独角鲸云 Narwhal Cloud 提供高性价比的便宜 NAT VPS 服务。支持共享IP与端口转发，是个人项目、网络测试及极客实验首选。' - no plan, no price and no stock figure anywhere in the body
  - [3] 2026-10-24: quoted product description: 'NAT VPS（共享IP服务器）是一种通过网络地址转换（NAT）技术共享公网 IPv4 地址的虚拟服务器 ... 通过预分配或自定义的公网端口映射（Port Forwarding）来访问内部服务' and '我们也支持自定义端口转发规则' - a port count is not stated
  - [4] 2026-10-24: the registration page offers only 'Continue with GoogleContinue with GitHub' and a terms tick, with no email or password fields
  - [2] 2026-10-24: 
  - [5] 2026-10-24: quoted: 'Narwhal Cloud is built on top of elite global infrastructure providers', listing VmRack, Oracle Cloud, BandwagonHost, Hytron, HyeHost, PDXNET, HostDzire and ZLIDC - so the seller is a reseller over other hosts' infrastructure rather than an operator
  - [6] 2026-10-24: reported, not measured: '所有套餐几乎都是超级便宜0.18美元月付，1.7x美元左右年付 ... 换算成人民币月付1.3元一个月 ... 一般套餐都是1核/128M/500G流量' and '后台需要先充值，在购买，可以微信扫码充值后刷新页面可以看到余额' - a third-party blog post dated 2024, four years of price drift from today
- sources:
  - [1] https://fuckip.me/
  - [2] https://fuckip.me/terms
  - [3] https://fuckip.me/zh/index.html
  - [4] https://dash.fuckip.me/register
  - [5] https://fuckip.me/suppliers
  - [6] https://www.jzbk.net/1600.html
