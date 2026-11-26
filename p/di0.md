# Incudal

> di0.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/di0/ | JSON https://fshy.ajam.dev/api/v1/entity/di0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Incudal (黃帝云VPS)

- `compute/incudal` | dead | evidence documented | binding per-ip-shaping | category NAT VPS | tier official direct NAT (all plans withdrawn)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:34:00.000Z (live) | stale on 2026-11-24
- url https://incudal.di0.uk/
- price parsed USD 0.1871/mo
- free tier: No free tier was ever published. The cheapest advertised plan before closure was CNY 1.25 a month for 1 vCore at 50%, 266 MB of RAM, 2 GB of disk, 300 GB of traffic, one NAT IPv4 and LXC, in Gravelines, France. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the operator announced a full shutdown and stated that self-operated instances are being closed in sequence, with a temporary power-on for backups available on request | source: [2]
- egress: the pre-closure plan card stated 300 GB a month at 1 Gbps on the France entry plan | metered: yes | free allowance: 300 GB | source: [1]
- identity: email | detail: was an account on the Incus panel; the shutdown notice says Alipay and WeChat Pay orders are refunded to source and crypto users submit a USDT BEP20 address, which is what the rails were, not what they are now
- interface: ssh
- limits:
  - per-ip-shaping (binding): one NAT IPv4 per instance on the entry plan [1]
- binding note: moot: the operator has closed, so the first thing that fails is the service existing at all.
- interface detail: LXC or KVM instance with root; the control plane is an Incus-based panel
- tooling: any SSH client, had the service still existed
- composes with: none: the service is closed, so nothing can depend on it
- reliability: closed: the operator published a shutdown notice, refunded Alipay/WeChat orders to source, closed self-operated instances in sequence and kept mail service to the end of the month
- notes: Incudal sold some of the cheapest NAT containers in the market - the France entry plan was CNY 1.25 a month, which at the CBR rate dated 24.10.2026 is USD 0.1871 a month for 266 MB, 2 GB, 300 GB and a NAT IPv4 - and a 2026 gist put the range at USD 0.28 to USD 0.49 a month. All of it is withdrawn. The operator published a shutdown notice, refunded Alipay and WeChat orders to source, asked crypto users for a USDT BEP20 address, and closed self-operated instances in sequence with a temporary power-on offered for backups. The technical corroboration is direct: every path on incudal.com including the apex returns HTTP 530, and the surviving portal at incudal.di0.uk is a JavaScript shell with no catalogue in its HTML. This is the second NAT seller in this corner of the market to close in a year, after KhanWebHost's NATKVM, which is worth noting as a pattern rather than as a comment on any single operator. Not established: the exact date of closure, and whether any third-party 'marketplace' nodes on the Incus panel still sell.
- evidence note: the closure is documented by a third-party report quoting vendor notice, and corroborated by published domains: incudal.com answers HTTP 530 on /, /store, /plans, /instances/create and www, while the remaining portal at incudal.di0.uk is a 2.6 KB JavaScript shell with no plan data; the pre-closure price is a forum claim, not a first-party page read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.2598
  - shape.disk_gib: 2
  - billing_model: monthly (pre-closure)
  - term: monthly (pre-closure)
  - m10h_usd: 0.1871
  - m24h_usd: 0.1871
  - price_arithmetic: CNY 1.25 a month x (12.0557 RUB per CNY / 80.5381 RUB per USD) = CNY 1.25 x USD 0.149689 = USD 0.1871 a month, on the pre-closure list price. Both rates from the CBR table dated 24.10.2026. The figure is recorded for the history of the band, not as an available offer: the service is closed.
  - renewal_usd: not applicable, closed
  - port_mbps: 1000
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: one NAT IPv4 per instance; the port count on the entry plan was not published in the post read
  - network_out.static_ip: no
  - network_out.ipv6: no
  - signup_url: https://incudal.com/
  - cart_url_note: no cart exists: the apex and every store path return HTTP 530
  - nat_config.ports_assigned_or_chosen: unknown
  - udp_forwarding: not stated
  - payment_methods: was Alipay, WeChat Pay and cryptocurrency, per the refund terms in the shutdown notice
  - stock: out of stock permanently: site operations stopped per the shutdown notice, and incudal.com returns HTTP 530 on every path tried on 2026-10-24
  - session_cap.restart_required: no
  - session_cap.note: not applicable, closed
- evidence:
  - [3] 2026-10-24: 
  - [4] 2026-10-24: probe: the remaining portal returns HTTP 200 with a 2,656-byte body that is only a JavaScript shell - three script tags, one stylesheet, one logo - and no plan, price or stock data at all
  - [2] 2026-10-24: quoted shutdown table: '全站运营 | 停止' (site operations stopped), '支付宝/微信订单 | 原路退款' (Alipay/WeChat orders refunded to source), '自营实例 | 陆续关闭' (self-operated instances closed in sequence), '数据备份 | 用户可申请临时开机备份' (users may request a temporary power-on to back up)
  - [1] 2026-10-24: quoted pre-closure offer: 'Gravelines, France | Intel Xeon E5-1650 v3: 1.19 RMB/month ... 1 vCore CPU (50%) / RAM: 266 MB / Storage: 2GB / Bandwidth: 300GB / Port: 1Gbps / IP Address: 1 IPv4 NAT / Virtualization: LXC ... Original price is 1.25 RMB/month'
- sources:
  - [1] https://www.nodeloc.com/t/topic/83298
  - [2] https://ccxxkk.com/126.html
  - [3] https://incudal.com/
  - [4] https://incudal.di0.uk/
