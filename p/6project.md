# 6Project

> 6project.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/6project/ | JSON https://fshy.ajam.dev/api/v1/entity/6project.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 6Project

- `egress/6project-org` | qualifies-with-caveat | evidence reported | binding write-gated | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://6project.org/policies
- price USD 0
- free tier: Eligible active accounts can contribute USD 12.50 with a /64 transport prefix or USD 20 with a /80 transport prefix for an additional routed /48. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no traffic allowance is published on the home, request or policy page; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'IPv6 tunnel requests must be submitted through the official form. Review time is typically 1-24 hours. Accurate contact details and technical information are required for provisioning.' | country: None
- interface: cli
- limits:
  - write-gated (binding): requests are reviewed by the 6Project team, typically 1-24 hours, before a tunnel is provisioned [1]
  - retention-clamped: prefixes are issued with annual validity and must be renewed before expiry, with only a short grace period [1]
  - write-gated (binding): review 1 to 24 hours, up to 72 at peak [1]
- binding note: A person reviews each request before anything is provisioned, so that gate is reached before any byte is transferred and it is what fails first at 1 TiB/month. Renewal is the second gate: a prefix that is not renewed annually is removed after a short grace period.
- interface detail: 'A user chooses a tunnel type, selects the preferred PoP, provides the technical information needed for provisioning'
- tooling: OpenVPN, wireguard-tools, or a plain 6in4/GRE/IPIP interface
- composes with: the review gate makes it a slow path to the same result a self-service broker gives in a minute; it is worth it only for the /48 or for the BGP option.
- reliability: 'The tunnel broker operates on a best-effort basis with no guaranteed SLA'; abuse can lead to throttling, suspension or removal.
- notes: The two third-party lists disagree with each other and with the policy page on what is free: tunnelbroker.services says a /64 costs EUR 11.50/year, handwiki says a::/128 costs EUR 1.50 once and a /80 EUR 5.50 once, and the policy page speaks of /64 and /80 accounts as things that already exist when a /48 is bought. A free routed prefix is therefore not established. AS208753, PoPs in Milan, Frankfurt, Vienna, Bradford, Los Angeles, Las Vegas and Wuhan. The routed /48 is USD 12.50 with a /64 transport or USD 20 with a /80, and adds 365 days to the account. The homepage read returned a server-rendered SEO fallback, not the React application; the policies page carried the substance. Re-read 2026-10-23: BGP is available at most locations, and the policies page carries the same sentence as the homepage.
- evidence note: Transports and account review requirements are documented from 6project policy documentation. The prefix allocation and price for free accounts are unconfirmed by vendor documentation, with conflicting third-party listings.
- extras:
  - wg_path: native-conf
  - wg_detail: '6Project provides IPv6 tunnels over OpenVPN, WireGuard, 6in4, GRE, and IPIP.' Whether the WireGuard profile is generated or hand-written is not stated.
  - ingress: tcp+udp
  - volume_stated: no traffic allowance is published on the home, request or policy page
  - bytes_transit: yes
  - transit_note: AS208753 carries the traffic from its own PoPs.
- evidence:
  - [1] 2026-10-23: '6Project provides IPv6 tunnels over OpenVPN, WireGuard, 6in4, GRE, and IPIP.'
  - [1] 2026-10-23: 'IPv6 tunnel requests must be submitted through the official form. Review time is typically 1-24 hours.'
  - [1] 2026-10-23: 'Prefixes are issued with annual validity.'
  - [1] 2026-10-23: a routed /48 costs USD 12.50 with a /64 transport prefix or USD 20 with a /80
  - [2] 2026-10-23: third-party list: '6in4 / GRE Tunnels /64, /80 Prefix', 'Notes: /64 for EUR 11.50/y and /80 for EUR 5.50/y'
  - [3] 2026-10-23: third-party list: '1.50 EUR one-time for ::/128, 5.50 EUR one-time for ::/80'
  - [4] 2026-10-23: community-operated AS208753 broker; 'Available methods can include OpenVPN, WireGuard, SIT, GRE, IPIP, or BGP depending on the selected location'
- sources:
  - [1] https://6project.org/policies
  - [2] https://tunnelbroker.services/
  - [3] https://handwiki.org/wiki/List_of_IPv6_tunnel_brokers
  - [4] https://6project.org/
