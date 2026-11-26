# BGPTunnel.com

> bgptunnel.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bgptunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/bgptunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BGPTunnel.com

- `egress/bgptunnel` | fails-identity | evidence reported | binding volume-quota | category bgp transit tunnel | tier free
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:23:44.598Z (live) | stale on 2026-12-10
- url https://bgptunnel.com/
- price USD 0
- free tier: BGPTunnel.com offers free IPv4 and IPv6 BGP Transit via GRE and Wireguard Tunnels in various locations for non-commercial and personal networks via AS209533. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no traffic allowance is published on the landing page; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: institution | detail: an account whose email matches the email listed in WHOIS for the ASN the user owns; third-party list: 'Only BGP, bring your own subnet/asn.' | country: None
- interface: cli
- limits:
  - volume-quota (binding): fair use up to 1TB/m is usually okay, determined at the vendor's discretion [2]
  - per-ip-shaping: free tunnels are limited to 100Mbit/s [2]
- binding note: The identity gate (an owned ASN) comes first and is recorded in identity_cost. Once passed, the vendor states fair use up to 1TB/m and a 100Mbit/s limit on free tunnels; 1TB/m is the lower bound.
- interface detail: BGP over GRE tunnels, self-service for ASN holders
- tooling: a GRE interface, BGP daemon and an announced prefix on the client side
- composes with: only after obtaining an ASN and PI space, which is a paid prerequisite; not a path to free ingress on its own.
- reliability: no SLA or allowance published on the landing page.
- notes: This is the successor to tunnelbroker.li and to route48.org. It is a transit product, not a tunnel broker: an ASN and PI space would be needed first, which NetAssist sells for EUR 300/year. That cost is what makes it unusable rather than the service.
- evidence note: the landing page read establishes only a GRE-based BGP transit offer; the ASN requirement and the /126 come from the tunnelbroker.services list. A vendor page naming the prerequisites would raise it.
- extras:
  - wg_path: none
  - wg_detail: the vendor home page names GRE and Wireguard tunnels carrying BGP transit; the tunnels are for ASN holders
  - ingress: tcp+udp
  - volume_stated: no traffic allowance is published on the landing page
  - bytes_transit: yes
  - transit_note: AS209533 announces and carries the customer prefix.
- evidence:
  - [1] 2026-10-23: 'BGPTunnel.com offers free IPv4 and IPv6 Transit via GRE Tunnels in various locations for non-commercial and personal networks via AS209533.'
  - [3] 2026-10-23: 'Only BGP, bring your own subnet/asn.' with a /126 prefix and AS209533
  - [4] 2026-10-23: route48.org now resolves here, which is how the successor was found
  - [2] 2026-11-25: the vendor policy names the account email field and ties it to the ASN's WHOIS | capture: sha256:6c42ee90304f625b7a41b891d77b3a478106a97f8b80805d5af67843552258b1 | quote: -The account email must match the email listed in WHOIS for the ASN.
  - [5] 2026-11-25: sign-up needs an ASN the user owns | capture: sha256:930358789634b766b584ae2041660544f28bf9786e58712709283f12515751e0 | quote: -You must own the ASN you signup with, you cannot use your ISPs ASN or any other random ASN.
  - [1] 2026-11-25: the vendor home page now names GRE and WireGuard tunnels and BGP transit | capture: sha256:58286dbdb86639cc069026064cba59073c1dfaeb008de55d425be0d198999750 | quote: BGPTunnel.com offers free IPv4 and IPv6 BGP Transit via GRE and Wireguard Tunnels in various locations for non-commercial and personal networks via AS209533.
  - [1] 2026-11-25: WireGuard is named on the vendor page | capture: sha256:58286dbdb86639cc069026064cba59073c1dfaeb008de55d425be0d198999750 | quote: BGPTunnel.com offers free IPv4 and IPv6 BGP Transit via GRE and Wireguard Tunnels in various locations for non-commercial and personal networks via AS209533.
  - [2] 2026-11-25: the traffic fair-use level is 1TB per month; the 100Mbit/s line is on the same page | capture: sha256:6c42ee90304f625b7a41b891d77b3a478106a97f8b80805d5af67843552258b1 | quote: Fair use Traffic is determined at our discretion, up to 1TB/m is usually okay.
  - [2] 2026-11-25: free tunnels are shaped at 100 Mbit/s | capture: sha256:6c42ee90304f625b7a41b891d77b3a478106a97f8b80805d5af67843552258b1 | quote: Free tunnels are limited to 100Mbit/s.
  - [2] 2026-11-25: once the ASN gate is passed, traffic is bounded by a 1TB per month fair-use level | capture: sha256:6c42ee90304f625b7a41b891d77b3a478106a97f8b80805d5af67843552258b1 | quote: Fair use Traffic is determined at our discretion, up to 1TB/m is usually okay.
  - [2] 2026-11-25: 100Mbit/s shaping next to the 1TB/m fair-use level | capture: sha256:6c42ee90304f625b7a41b891d77b3a478106a97f8b80805d5af67843552258b1 | quote: Free tunnels are limited to 100Mbit/s.
- sources:
  - [1] https://bgptunnel.com/
  - [2] https://bgptunnel.com/faq-and-aup
  - [3] https://tunnelbroker.services/
  - [4] https://route48.org/
  - [5] https://bgptunnel.com/sign-up
