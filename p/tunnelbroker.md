# Tunnelbroker.li

> tunnelbroker.li | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelbroker/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelbroker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tunnelbroker.li (iFog)

- `egress/tunnelbroker-li` | dead | evidence documented | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnelbroker.li/
- price USD 0
- free tier: tunnelbroker.li is closing down and is beeing replaced by BGPTunnel.com for non-commerical tunnels and by ifog.ch for commercial offerings. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not applicable: the service is closing; ingress: none | metered: no | free allowance: none published | source: [2]
- identity: email | detail: not established: no signup page survives in the capture | country: None
- interface: unknown
- binding note: The provider is dead, so no constraint is reached at any volume. The handwiki list still describes it as active with a /64 and WireGuard, which is why the record exists: a reader following that list would spend an evening on a closed service.
- interface detail: not established
- tooling: not applicable
- composes with: not applicable: use route64.org or tahio for the same job
- reliability: closed; the address space and customers were split between a non-commercial and a commercial successor.
- notes: The archived first-party notice is what establishes the closure. iFog GmbH (AS34927) continues under bgptunnel.com and ifog.ch.
- evidence note: documented from the provider's own notice, read through the Wayback capture of 2026-03-15; A fresh capture or a working live page would change this.
- extras:
  - wg_path: unknown
  - wg_detail: the surviving capture names only BGP transit tunnels and does not list transports
  - ingress: none
  - volume_stated: not applicable: the service is closing
  - bytes_transit: no
  - transit_note: not applicable
- evidence:
  - [1] 2026-10-23: 'tunnelbroker.li is closing down and is beeing replaced by BGPTunnel.com for non-commerical tunnels and by ifog.ch for commercial offerings.' (capture of 2026-03-15)
  - [3] 2026-10-23: still listed as active with a /64 and WireGuard support, dated 2024-02-06
- sources:
  - [1] https://web.archive.org/web/20260315143914id_/https://tunnelbroker.li/
  - [2] https://tunnelbroker.li/
  - [3] https://handwiki.org/wiki/List_of_IPv6_tunnel_brokers
