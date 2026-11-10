# Privex

> privex.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privex/ | JSON https://fshy.ajam.dev/api/v1/entity/privex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Privex (Privex Inc.)

- `compute/privex-vnano-se-ssd-ipv6` | qualifies | evidence documented | binding volume-quota | category IPv6-only VPS | tier VNANO-SE-SSD
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://pay.privex.io/order/package/vnano-se-ssd
- price parsed USD 0.99/mo
- free tier: No free tier. VNANO-SE-SSD is USD 0.99 a month with a USD 0.00 setup fee, printed '$0.00 setup fee $0.99 / mo'. A 7-day refund policy applies to VPS products. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the order form states 'VPS's are suspended after 5 days overdue, and data is removed after 25 days' | days: 25 | source: [2]
- egress: 0.25 TB a month, printed 'Traffic cap: 0.25 TB/month', on a 100 Mbps port described as 'BC2' | metered: yes | free allowance: 0.25 TB a month | source: [1]
- identity: email | detail: the order form carries the fields email, name, hostname, os, ssh_keys, qty, referral, usecase, notes and a terms tick, with no card field, no address field, no phone field and no national ID field. Payment is cryptocurrency only: the order page states 'For payment we currently accept HIVE, HBD, BTC, BCH, LTC, XMR, EOS and DOGE' and 'We do NOT accept any fiat methods currently', so no card is taken and there is no authorisation hold to state.
- interface: ssh
- limits:
  - volume-quota (binding): 0.25 TB (250 GB) a month of traffic [1]
  - per-ip-shaping: no IPv4 address at all; the machine is reachable only over IPv6, and the order form states 'This package does not include an IPv4 address' [1]
- binding note: 250 GB a month is the tightest allowance among documented hosts after WAPAC's 500 GB counted both ways, and at 100 Mbps a sustained transfer reaches it in under six hours.
- interface detail: IPv6-only KVM guest, Debian 12, provisioned in 5 to 10 minutes, with an SSH key supplied on the order form
- tooling: any SSH client over IPv6; an order form that takes an SSH public key; DNS64 and NAT64 run by the vendor so IPv4-only hosts are reachable through a translated address
- composes with: the cheapest IPv6-only machine among documented hosts that is in stock, from a seller with an allocated AS and a company that names itself, and the only one that ships a NAT64 gateway so IPv4-only hosts such as GitHub still resolve
- reliability: port scanning and IPFS in the German and Finnish regions cause automatic suspension; no uptime figure published
- notes: The cleanest IPv6-only row in this category, and the only one that solves the problem IPv6-only machines actually have. USD 0.99 a month for 256 MB, 5 GB SSD, a 100 Mbps port and 250 GB a month, in Sweden, in stock, with a USD 0.00 setup fee. The reason it beats the cheaper Axivora row is not price: it is that Privex runs its own DNS64 resolver and NAT64 gateway and pre-configures the micro VPS to use them, so an IPv4-only host such as GitHub still resolves. The vendor documents the mechanism, including the well-known 64:ff9b::/96 prefix, so this is a documented capability rather than an inference. Payment is cryptocurrency only and the order form states that plainly, which removes the card question entirely: there is no card field and no fiat rail, so there is no hold to state. The entity is corroborated two ways beyond the vendor's own words: an allocated AS210083 whose registered holder reads 'Privex Privex Inc.', and a contribution agreement in the vendor's own public repository describing 'the corporate entity Privex Inc. registered in Belize City, Belize'. What is not established: the Belize Companies registry record itself, which was reachable but was not queried by name in verification; and whether the 250 GB cap counts in one direction. One reliability note worth carrying: the vendor states port scanning or IPFS in the German and Finnish regions causes automatic suspension without warning, so the Swedish region this plan sits in is the safer choice. The 256 MB with Debian 12 is small but the plan family scales to 512 MB at USD 1.99.
- evidence note: price, shape, traffic cap, the no-IPv4 warning, the order-form fields, the payment rails and the termination interval are quoted from the vendor's own order pages read; the DNS64 and NAT64 behaviour is quoted from the vendor's own article read; the entity is corroborated by an allocated AS holder name in RIPEstat. The Belize registry was reached but not queried by name, so 'registered in Belize' rests on the vendor's own statement plus the AS holder.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.25
  - shape.disk_gib: 5
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 0.99
  - m24h_usd: 0.99
  - price_arithmetic: USD 0.99 a month billed monthly with a USD 0.00 setup fee, so the money out of pocket each month is USD 0.99. No conversion needed. VPS billing: the machine bills whether it runs or not, so the 10 h/day and 24/7 figures are identical.
  - out_of_pocket_usd: 0.99
  - renewal_usd: USD 0.99 a month; no separate renewal price published
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: no IPv4 at all; the IPv6 address answers on any port, and a DNS64 plus NAT64 gateway gives outbound reachability to IPv4-only hosts
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /64
  - udp: not stated in words for this plan, but the vendor documents a NAT64 gateway and the machine has an unrestricted IPv6 address, so UDP over IPv6 is available; no page read says it explicitly for the VNANO tier
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: cryptocurrency only: HIVE, HBD, BTC, BCH, LTC, XMR, EOS and DOGE; the order page states 'We do NOT accept any fiat methods currently'
  - card_hold: not applicable: no card is taken at all
  - checkout_fields: email, name, hostname, OS, SSH public key, quantity, referral, use case, notes and a terms tick; no card, address, phone or ID
  - stock: orderable: the package page renders the full order form with the price and no out-of-stock marker on 2026-10-24
  - cart_url: https://pay.privex.io/order/package/vnano-se-ssd
  - cart_works: priced: the package page renders the selected package, the USD 0.99 monthly price and the order form together
  - product_url: https://pay.privex.io/order/choose-server-nojs
  - signup_url: https://pay.privex.io/order/package/vnano-se-ssd
  - cart_url_note: Privex has no separate cart step: the package page is the order form, and it priced the plan at USD 0.99 a month with a USD 0.00 setup fee when read.
  - other_plans: VNANO-SE-HDD USD 0.99 for 256 MB and 40 GB HDD; VNANO-SE-NVME USD 1.49 for 256 MB and 5 GB NVMe; VMICRO-SE-HDD and VMICRO-SE-SSD USD 1.99 for 512 MB and 80 GB HDD or 10 GB SSD; VMICRO-SE-NVME USD 3.49; V1-IPV6-SE-SSD USD 3.99 for 1 GB and 1 TB a month. All IPv6-only, all Sweden.
  - regions: Sweden, The Netherlands, Germany, Finland and the USA (North Carolina) for the wider catalogue; the IPv6-only micro family read is Sweden
- evidence:
  - [1] 2026-10-24: quoted: 'VNANO-SE-SSD Virtual Server (VPS) Sweden RAM: 256M RAM Disk(s): 5G SSD CPU(s): 1 core Network: 100mbps BC2 Traffic cap: 0.25 TB/month Has IPv4: NO Has IPv6: YES ETA: 5-10 minutes Note: IPv6 Only - Debian 12 $0.00 setup fee $0.99 / mo'
  - [1] 2026-10-24: quoted warning: 'Warning: This package does not include an IPv4 address. To be able to connect to this server, you'll need to have IPv6 connectivity, either on your home network, or on another server which you'd use to connect to this server.'
  - [3] 2026-10-24: quoted sibling plans: 'VNANO-SE-HDD ... 40G HDD ... $0.99 / mo', 'VNANO-SE-NVME ... 5G NVMe ... $1.49 / mo', 'VMICRO-SE-HDD ... 512M RAM ... 80G HDD ... $1.99 / mo', all 'Has IPv4: NO Has IPv6: YES'
  - [2] 2026-10-24: quoted payment rails: 'For payment we currently accept HIVE, HBD, BTC, BCH, LTC, XMR, EOS and DOGE. More to come soon.' and 'We do NOT accept any fiat methods currently.'
  - [2] 2026-10-24: quoted termination: 'VPS's are suspended after 5 days overdue, and data is removed after 25 days.' and 'We offer a 7 day refund policy for VPS's and dedicated servers.' and 'Privex Inc. is a registered company in Belize'
  - [4] 2026-10-24: quoted NAT64 behaviour: 'we operate a DNS64 server which removes the IPv4 (A) records from domains, and creates "fake" IPv6 (AAAA) records. These fake IPv6 addresses are then routed to our NAT64 gateway' and 'Our micro VPS's are pre-configured to use our DNS64 server and NAT64 gateway'
  - [5] 2026-10-24: quoted: 'We are Privex Inc. A small technology company that currently focuses on affordable privacy-minded infrastructure' and 'Privex Inc was founded in early 2017 in the small country of Belize.'
  - [6] 2026-10-24: quoted JSON: "holder":"Privex Privex Inc.", "announced":true - an allocated AS whose registered holder name matches the trading company
- sources:
  - [1] https://pay.privex.io/order/package/vnano-se-ssd
  - [2] https://pay.privex.io/order/
  - [3] https://pay.privex.io/order/choose-server-nojs
  - [4] https://www.privex.io/articles/micro-ipv6-vps-s/
  - [5] https://www.privex.io/about/
  - [6] https://stat.ripe.net/data/as-overview/data.json?resource=AS210083
