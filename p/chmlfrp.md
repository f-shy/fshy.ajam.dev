# ChmlFrp

> chmlfrp.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chmlfrp/ | JSON https://fshy.ajam.dev/api/v1/entity/chmlfrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ChmlFrp

- `egress/chmlfrp` | fails-identity | evidence documented | binding per-ip-shaping | category udp port forward | tier free
- needs card no, phone no, ID yes, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.chmlfrp.net/
- price USD 0
- free tier: Free plan: 8 Mbps speed limit, 4 tunnels, 1 free domain, unlimited traffic. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The site says 'free and unlimited traffic, no need to worry about running out', while bandwidth can be limited for what the vendor calls excessive use.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: national-id | detail: The mapping tutorial lists 'registered a ChmlFrp account and completed real-name verification' as a precondition, and says an unverified account shows 'you are not yet real-name verified' on the home page. | country: None
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): 8 Mbps domestic, 32 Mbps international [1]
  - volume-quota: none published; unlimited claimed [1]
- binding note: With no byte quota the rate cap is what bites: 8 Mbps sustained is about 2.6 TB per month, so 1 TiB/month fits under it, but any burst above 8 Mbps is shaped, and bandwidth limiting is also possible.
- interface detail: frpc client plus a documented REST API for nodes and tunnels.
- tooling: frpc with a vendor-issued config; wg-quick on the local side
- composes with: A UDP tunnel on an international node can carry a WG handshake at up to 32 Mbps, enough in principle for 1 TiB/month.
- reliability: Node API exposes a per-node UDP flag, so a node can silently stop carrying UDP; the FAQ documents nodes going offline or being abandoned.
- notes: Free frp provider offering unmetered transfer with a 32 Mbps international bandwidth limit. Registration requires national identity verification.
- evidence note: Unlimited traffic, the 8/32 Mbps split and the real-name precondition are all on vendor pages read. Only a probe could show the shaper's real behaviour.
- extras:
  - wg_path: inside-udp
  - wg_detail: The mapping guide lists TCP, UDP, HTTP and HTTPS as port types, and the public node API returns a per-node 'udp' boolean, so UDP carriage depends on the chosen node.
  - ingress: tcp+udp
  - volume_stated: The site says 'free and unlimited traffic, no need to worry about running out', while bandwidth can be limited for what the vendor calls excessive use.
  - bytes_transit: yes
  - transit_note: ChmlFrp nodes relay the datagrams.
- evidence:
  - [1] 2026-10-23: free plan is 8 Mbps, 4 tunnels, unlimited traffic
  - [2] 2026-10-23: real-name verification is a stated precondition; port type includes UDP
  - [3] 2026-10-23: each node reports whether UDP is allowed
  - [4] 2026-10-23: bandwidth can be limited despite the unlimited-traffic claim
  - [5] 2026-10-23: 'If you are using a TCP or UDP tunnel ... the final address is your-domain:external-port', for example test.domain.cn:12345 [translated]
- sources:
  - [1] https://www.chmlfrp.net/
  - [2] https://docs.chmlfrp.net/docs/use/mapping
  - [3] https://docs.chmlfrp.net/API/v2/Node_operations/node
  - [4] https://docs.chmlfrp.net/terms/terms-of-service.html
  - [5] https://docs.chmlfrp.net/docs/dns/a-record
