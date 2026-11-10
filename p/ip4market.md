# IP4Market tunnel broker

> ip4market.ru | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip4market/ | JSON https://fshy.ajam.dev/api/v1/entity/ip4market.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP4Market tunnel broker

- `egress/ip4market` | qualifies-with-caveat | evidence reported | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://ipv6.ip4market.ru/
- price USD 0
- free tier: the service rules say 'Servis besplatnyy' (the service is free) and 'Servis dlya chastnogo, nekommercheskogo ispolzovaniya'; the indexed text of the ip4market page says 'Lichnaya set IPv6 /48 v odni ruki' (a personal /48 network) | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: no traffic allowance is published; the rules name only abuse as a reason for blocking; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: a registration on the ip4market site is required; the field list was not read | country: None
- interface: cli
- binding note: Nothing in the vocabulary is published: free, no byte meter, no rate. The gate is a public IPv4 for 6in4 and the non-commercial scope stated in the rules; neither is a volume constraint, so nothing fails at 1 TiB/month.
- interface detail: configuration help pages plus a broker panel; no API described
- tooling: a 6in4 interface on Linux or a router; the site publishes configuration help
- composes with: needs a public IPv4, so it fits a free VM with an IPv4 address.
- reliability: the rules reserve the right to block without warning for hacking or spam.
- notes: Russian-language, one PoP, run since 2018 as an answer to local blocking. The page extraction returned the same 165-word introduction for both the ip4market host and the landing host, so the /48 sentence itself was not read from the DOM; it is the search index's copy of that page. That is the single weakest fact in this record.
- evidence note: the free price and the private non-commercial scope are documented from the vendor's rules page; the /48 size comes from the search engine's indexed text of the ip4market page, because the page as extracted returned only the introductory article. Reading the ip4market page through a browser session would raise it.
- extras:
  - wg_path: none
  - wg_detail: no WireGuard is mentioned on any page read; the service is described as 6in4 encapsulation only
  - ingress: tcp+udp
  - volume_stated: no traffic allowance is published; the rules name only abuse as a reason for blocking
  - bytes_transit: yes
  - transit_note: IP4Market carries the traffic on its own Russian network.
- evidence:
  - [1] 2026-10-23: 'Servis besplatnyy', 'Servis dlya chastnogo, nekommercheskogo ispolzovaniya'
  - [3] 2026-10-23: indexed text: 'Lichnaya set IPv6 /48 v odni ruki' (a personal IPv6 /48 in one pair of hands)
  - [2] 2026-10-23: the service is described as 6in4, encapsulating IPv6 in IPv4
- sources:
  - [1] https://ipv6.ip4market.ru/?page=termsofservice
  - [2] https://ipv6.ip4market.ru/
  - [3] https://tb.ip4market.ru/
