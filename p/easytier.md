# EasyTier

> easytier.cn | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/easytier/ | JSON https://fshy.ajam.dev/api/v1/entity/easytier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EasyTier

- `egress/easytier` | fails-egress | evidence documented | binding none | category mesh vpn software with community relays | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:23:41.181Z (live) | stale on 2026-12-26
- url https://easytier.cn/en/
- price USD 0
- free tier: A simple, secure, decentralized networking solution | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published; community relay nodes are voluntary infrastructure with no quota.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; peers join by network name and secret. | country: None
- interface: cli
- binding note: Software plus volunteer relays: no hosted endpoint and no published capacity, so reliability rather than a quota is what fails at 1 TiB/month.
- interface detail: CLI plus web console
- tooling: easytier-core and GUI.
- composes with: Needs two hosts; the relay is the free part.
- reliability: Community relay capacity is unpriced and unaccountable.
- notes: Strong transport list (WG, QUIC, UDP) but every path needs a host at each end and a relay that somebody else is paying for.
- evidence note: P2P mesh VPN with community relay support. Protocol and CLI features are documented in source repository.
- extras:
  - wg_path: none
  - ingress: none
  - volume_stated: No allowance is published; community relay nodes are voluntary infrastructure with no quota.
  - bytes_transit: overlay-only
  - transit_note: direct or community relay
- evidence:
  - [1] 2026-10-23: 'Supports UDP, IPv6 traversal'; 'WireGuard encryption'; 'Supports TCP / UDP / WS / WSS / WG / QUIC / FakeTCP'
  - [1] 2026-11-25: the page's own description; it states no allowance and no price | capture: sha256:f61ca043fc83eb0420ba9acc6485750b3f40a4effef5f613e413488c9458a084 | quote: A simple, secure, decentralized networking solution
  - [1] 2026-11-25: the page describes software with no allowance and no price | capture: sha256:f61ca043fc83eb0420ba9acc6485750b3f40a4effef5f613e413488c9458a084 | quote: A simple, secure, decentralized networking solution
- sources:
  - [1] https://easytier.cn/en/
