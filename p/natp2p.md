# NatP2P

> natp2p.cn | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/natp2p/ | JSON https://fshy.ajam.dev/api/v1/entity/natp2p.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NatP2P

- `egress/natp2p` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://natp2p.cn/
- price USD 0
- free tier: Reverse proxy makes an intranet public; hole punching supports TCP and UDP direct connection; aggregated links let one tunnel span several nodes. [translated] | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The page title advertises daily free traffic without check-in, but no byte figure appears on the page body; the FAQ says relay-mode free users have a quota and P2P mode is unlimited in speed.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: A downloadable client and a QQ group for support; no registration flow is described on the page read. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): relay mode quota for free users, amount unpublished [1]
  - request-rate: P2P requires both ends in the same room [1]
- binding note: No byte figure is published, so the relay quota is the only metered thing and its size is unknown; P2P mode avoids the relay but cannot serve an arbitrary public client, so it does not answer the ingress test.
- interface detail: Green-build Windows client download; no API or Linux client is described on the page.
- tooling: vendor Windows client
- composes with: A UDP-capable reverse proxy for a WG listener, with P2P as the fast path between the account's own devices.
- reliability: P2P fails on symmetric NAT and falls back to the metered relay; the vendor recommends the proxy when the room join fails.
- notes: The only provider in the sweep that pairs hole punching with a public reverse proxy, which matters because hole punching alone never gives a stranger a port. Closed source and supported through a QQ group, so durability is unproven.
- evidence note: UDP hole punching and relay quota terms are stated in vendor documentation. Specific numeric quotas are unpublished.
- extras:
  - wg_path: inside-udp
  - wg_detail: The FAQ says P2P mode is not speed-limited and relay mode gives free users a quota; a WG datagram can be carried on a UDP tunnel, but P2P direct connection reaches only peers that joined the same room, not arbitrary internet clients.
  - ingress: udp
  - volume_stated: The page title advertises daily free traffic without check-in, but no byte figure appears on the page body; the FAQ says relay-mode free users have a quota and P2P mode is unlimited in speed.
  - bytes_transit: yes
  - transit_note: Relay nodes carry proxied traffic; direct P2P carries its own.
- evidence:
  - [1] 2026-10-23: TCP and UDP hole punching, reverse proxy, aggregated links; FAQ says P2P is not speed-limited and relay has a free quota
- sources:
  - [1] https://natp2p.cn/
