# OpenFrp

> openfrp.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openfrp/ | JSON https://fshy.ajam.dev/api/v1/entity/openfrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenFrp

- `egress/openfrp` | qualifies-with-caveat | evidence reported | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://www.openfrp.net/
- price USD 0
- free tier: Free users: 2 tunnels, 12 Mbps limit, traffic claimable by daily check-in. [translated from a forum roundup] | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Traffic is claimed by daily check-in; no monthly byte figure appears on the home page or in the roundup.; ingress: udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: Email registration on the panel; the roundup says domestic nodes require real-name verification while overseas nodes do not. | country: None
- interface: cli, rest
- limits:
  - per-ip-shaping: 12 Mbps [1]
  - volume-quota (binding): daily check-in grant, amount unpublished [1]
- binding note: The published speed cap would allow about 3.9 TB per month, so the check-in byte grant is the constraint that decides whether 1 TiB is reachable.
- interface detail: frpc client plus a documented panel API.
- tooling: frpc, Docker image, web panel and an API
- composes with: UDP tunnel at 12 Mbps, enough for 1 TiB/month only if the check-in grant is large.
- reliability: No free-tier reliability statement could be read; the roundup does not report breaks.
- notes: Chinese FRP service supporting TCP and UDP port forwarding. Account management and quota verification operate within a client-side web application.
- evidence note: console.openfrp.net is a JavaScript shell that returns no text to the reader, so the free-tier table could not be read directly.
- extras:
  - wg_path: inside-udp
  - wg_detail: The vendor home page lists 'TCP / UDP tunnels' as a product feature, which is the transport a WG datagram needs.
  - ingress: udp
  - volume_stated: No byte figure is published by the vendor. Third-party summaries of the free quota give 2 tunnels, 1.00 GB per month and 12 Mbps; the number is reported, not documented.
  - bytes_transit: yes
  - transit_note: OpenFrp nodes relay the datagrams.
- evidence:
  - [2] 2026-10-23: the product supports TCP and UDP tunnels
  - [1] 2026-10-23: 2 tunnels, 12 Mbps, check-in traffic
  - [3] 2026-10-23: Tunnel-type table: 'UDP | Bedrock (Geyser) | 19132 | example.com:19132 | CNAME (the port cannot be hidden)' [translated]
  - [4] 2026-10-23: 'Free users have a clear quota: at most 2 tunnels, 1 GB of traffic per month, 12 Mbps up and down' [translated, third party]
- sources:
  - [1] https://www.nodeseek.com/post-570663-1
  - [2] https://www.openfrp.net/
  - [3] https://docs.openfrp.net/use/configuration/minecraft
  - [4] https://nav.eyosc.com/sites/7227.html
