# Karabro tunnelbroker.se

> tunnelbroker.se | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelbroker-3/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelbroker-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Karabro tunnelbroker.se

- `egress/karabro-tunnelbroker-se` | fails-identity | evidence documented | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID yes, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnelbroker.se/order-ipv6
- price USD 0
- free tier: Privat Gratis: upp till 10 Mbit/s fair use, /60 prefix som standard (16 subnat), mojlighet upp till /48 efter behov, pris 0 kr per manad [quoted from a Swedish page with diacritics transliterated to ASCII] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no monthly byte allowance; the free plan is capped at 'Upp till 10 Mbit/s fair use'; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: national-id | detail: 'Vi behover ditt namn, din address och personnummer for att kunna folja svensk lagstiftning' (name, address and Swedish personal identity number), and 'Vi tillater bara endpoint IPv4-adresser som ar registrerade i Sverige och som inte ar klassade som VPN eller Proxyadresser' (only Swedish-registered IPv4 endpoints that are not classified as VPN or proxy). | country: None
- interface: cli
- limits:
  - per-ip-shaping: up to 10 Mbit/s fair use on the free plan [1]
  - write-gated: no automatic provisioning: an order form or an email, then a human builds the tunnel [1]
- binding note: Nothing in the vocabulary fails at 1 TiB/month: 10 Mbit/s sustains about 3.2 TB/month, and no byte quota is published. What fails is identity, before the first byte - a Swedish personal identity number and a Swedish-registered, non-VPN IPv4 endpoint - and the seven kinds have no name for that, so it is recorded in identity_cost and decides the verdict.
- interface detail: an order form or email to karabro.se; the tunnel is built by hand
- tooling: manual: the operator emails the configuration, then wg-quick, GRE or a SIT interface
- composes with: not chainable here: a free VM's IPv4 is almost always outside Sweden or classified as a hosting/VPN address.
- reliability: ports 25 and 465 are blocked by default; no SLA on the free plan ('Ingen SLA och best effort').
- notes: Swedish tunnel broker on AS51519 in Malmo. Free tier provides a WireGuard endpoint with a /60 IPv6 prefix (expandable to /48) at 10 Mbit/s. Registration requires a Swedish personal identity number (personnummer) and a Swedish-registered endpoint IP. Ports 25 and 465 are filtered.
- evidence note: documented from the vendor's Swedish order page read. Nothing here would be raised by a probe, because the account cannot be created without a Swedish identity number.
- extras:
  - wg_path: native-conf
  - wg_detail: WireGuard is one of three tunnel types: 'Vi stjoder foljande tunneltyper: Generic Routing Encapsulation, GRE / Wireguard / 6in4 (SIT)'. The config is written by hand by the operator because there is no automation.
  - ingress: tcp+udp
  - volume_stated: no monthly byte allowance; the free plan is capped at 'Upp till 10 Mbit/s fair use'
  - bytes_transit: yes
  - transit_note: Karabro carries the traffic on AS51519 from Sweden.
- evidence:
  - [1] 2026-10-23: 'Vi behover ditt namn, din address och personnummer for att kunna folja svensk lagstiftning.'
  - [1] 2026-10-23: 'Vi tillater bara endpoint IPv4-adresser som ar registrerade i Sverige och som inte ar klassade som VPN eller Proxyadresser.'
  - [1] 2026-10-23: free plan: 'Upp till 10 Mbit/s fair use', '/60 prefix som standard', 'Pris: 0kr/Manad'
  - [1] 2026-10-23: tunnel types: GRE, Wireguard, 6in4 (SIT); 'Tyvarr har vi inget system for att automatiskt skapa tunnlar'
  - [1] 2026-10-23: ports 25 and 465 are blocked by default
  - [2] 2026-10-23: the service is run by Karabro and is aimed at Swedish internet users
- sources:
  - [1] https://tunnelbroker.se/order-ipv6
  - [2] https://tunnelbroker.se/
