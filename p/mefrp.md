# ME Frp

> mefrp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mefrp/ | JSON https://fshy.ajam.dev/api/v1/entity/mefrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ME Frp

- `egress/me-frp` | qualifies-with-caveat | evidence reported | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:54.167Z (live) | stale on 2026-12-04
- url https://www.mefrp.com/
- price USD 0
- free tier: Free users: 2 tunnels, 10 Mbps limit, traffic claimable by daily check-in; real-name verification raises the limit to 25 Mbps. [translated from a forum roundup] | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Traffic is granted by daily check-in; no monthly byte allowance is published in available documentation.; ingress: udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: Account registration is by email; real-name verification is optional and buys a higher speed cap (25 Mbps instead of 10 Mbps) according to the roundup. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 25Mbps bandwidth on the free plan after real-name registration [2]
  - volume-quota (binding): daily check-in grants up to 10GB of traffic [2]
- binding note: The first-party plan page states the free plan grants up to 10GB of traffic per daily check-in, a volume quota that binds; bandwidth is 25Mbps after real-name registration.
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
  - [2] 2026-11-19: the first-party plan page states 25Mbps bandwidth after real-name registration | capture: sha256:f551f4f8c93a90c686c1bcf0c28093ee60b9b9e2e48e4630e1a33824333b173a | quote: 注册实名即享有 25Mbps 双向带宽
  - [2] 2026-11-19: the first-party plan page states daily check-in grants up to 10GB of traffic | capture: sha256:f551f4f8c93a90c686c1bcf0c28093ee60b9b9e2e48e4630e1a33824333b173a | quote: 每日签到最高可得 10GB 流量
  - [2] 2026-11-19: the first-party page publishes the 10GB check-in grant and the 25Mbps bandwidth on the same page | capture: sha256:f551f4f8c93a90c686c1bcf0c28093ee60b9b9e2e48e4630e1a33824333b173a | quote: 每日签到最高可得 10GB 流量
  - [2] 2026-11-19: the binding is a daily check-in volume quota of up to 10GB | capture: sha256:f551f4f8c93a90c686c1bcf0c28093ee60b9b9e2e48e4630e1a33824333b173a | quote: 每日签到最高可得 10GB 流量
  - [2] 2026-11-19: the per-ip-shaping limit is 25Mbps after real-name registration | capture: sha256:f551f4f8c93a90c686c1bcf0c28093ee60b9b9e2e48e4630e1a33824333b173a | quote: 注册实名即享有 25Mbps 双向带宽
- sources:
  - [1] https://www.nodeseek.com/post-570663-1
  - [2] https://www.mefrp.com/
