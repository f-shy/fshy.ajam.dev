# ME Frp

> mefrp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mefrp/ | JSON https://fshy.ajam.dev/api/v1/entity/mefrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ME Frp

- `egress/me-frp` | qualifies-with-caveat | evidence reported | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://www.mefrp.com/
- price USD 0
- free tier: Free users: 2 tunnels, 10 Mbps limit, traffic claimable by daily check-in; real-name verification raises the limit to 25 Mbps. [translated from a forum roundup] | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Traffic is granted by daily check-in; no monthly byte allowance is published in available documentation.; ingress: udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: Account registration is by email; real-name verification is optional and buys a higher speed cap (25 Mbps instead of 10 Mbps) according to the roundup. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 10 Mbps free, 25 Mbps after real-name [1]
  - volume-quota (binding): daily check-in grant, amount unpublished [1]
- binding note: The byte allowance is a check-in grant of unknown size, so the quota is what fails first and it cannot be shown to reach 1 TiB without measuring the grant.
- interface detail: frpc client, Docker image, web panel.
- tooling: frpc plus a Docker image
- composes with: Same shape as ChmlFrp: a UDP tunnel that can carry a WG datagram, capped at 10 Mbps free.
- reliability: Free-tier throughput depends on a daily claim; a missed day is a metering event, not an outage.
- notes: mefrp.com/pricing returns a 404 today, so the free tier is only described by the forum roundup. The operator's home page claims 69 nodes and 74.33 TB carried, which is consistent with a real service.
- evidence note: The pricing table 404s and the panel is behind a login, so the numbers are the roundup author's. Reading the panel would raise it to documented.
- extras:
  - wg_path: inside-udp
  - wg_detail: frp-family service; UDP tunnels are the transport for a WG datagram.
  - ingress: udp
  - volume_stated: Traffic is granted by daily check-in.
  - bytes_transit: yes
  - transit_note: ME Frp nodes relay the datagrams.
- evidence:
  - [1] 2026-10-23: 2 tunnels, 10 Mbps, check-in traffic, 25 Mbps after real-name
  - [2] 2026-10-23: the service is live and reports 74.33 TB of carried traffic
- sources:
  - [1] https://www.nodeseek.com/post-570663-1
  - [2] https://www.mefrp.com/
