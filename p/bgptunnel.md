# BGPTunnel.com

> bgptunnel.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bgptunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/bgptunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BGPTunnel.com

- `egress/bgptunnel` | fails-identity | evidence reported | binding none | category bgp transit tunnel | tier free
- needs card no, phone no, ID no, institution yes | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://bgptunnel.com/
- price USD 0
- free tier: BGPTunnel.com offers free IPv4 and IPv6 Transit via GRE Tunnels in various locations for non-commercial and personal networks via AS209533. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no traffic allowance is published on the landing page; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: institution | detail: third-party list: 'Only BGP, bring your own subnet/asn.' The vendor page confirms 'Transit via GRE Tunnels ... for non-commercial and personal networks' but names no account fields. | country: None
- interface: cli
- binding note: Nothing in the vocabulary is reached, because the offer is not a prefix handed to a client: it is transit for a network that already holds an ASN and its own address space. That gate is identity, recorded in identity_cost, and it is passed before any volume is transferred.
- interface detail: BGP over GRE tunnels, self-service for ASN holders
- tooling: a GRE interface, BGP daemon and an announced prefix on the client side
- composes with: only after obtaining an ASN and PI space, which is a paid prerequisite; not a path to free ingress on its own.
- reliability: no SLA or allowance published on the landing page.
- notes: This is the successor to tunnelbroker.li and to route48.org. It is a transit product, not a tunnel broker: an ASN and PI space would be needed first, which NetAssist sells for EUR 300/year. That cost is what makes it unusable rather than the service.
- evidence note: the landing page read establishes only a GRE-based BGP transit offer; the ASN requirement and the /126 come from the tunnelbroker.services list. A vendor page naming the prerequisites would raise it.
- extras:
  - wg_path: none
  - wg_detail: no WireGuard is described on the landing page; the third-party list credits it with WireGuard but the vendor page names GRE tunnels and BGP transit only
  - ingress: tcp+udp
  - volume_stated: no traffic allowance is published on the landing page
  - bytes_transit: yes
  - transit_note: AS209533 announces and carries the customer prefix.
- evidence:
  - [1] 2026-10-23: 'BGPTunnel.com offers free IPv4 and IPv6 Transit via GRE Tunnels in various locations for non-commercial and personal networks via AS209533.'
  - [2] 2026-10-23: 'Only BGP, bring your own subnet/asn.' with a /126 prefix and AS209533
  - [3] 2026-10-23: route48.org now resolves here, which is how the successor was found
- sources:
  - [1] https://bgptunnel.com/
  - [2] https://tunnelbroker.services/
  - [3] https://route48.org/
