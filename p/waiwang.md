# WaiWang.Men

> waiwang.men | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/waiwang/ | JSON https://fshy.ajam.dev/api/v1/entity/waiwang.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WaiWang.Men

- `egress/waiwang-men` | fails-quota | evidence documented | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://waiwang.men/
- price USD 0
- free tier: US Buffalo: mappings per user 5; server bandwidth shared 1000M; server traffic 1T (one-way); supported ports 80, 443, 20000-50000. [translated] | unit: TB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Server traffic 1T, one-way, per the node table. Whether that is a decimal TB or a TiB is not stated.; ingress: udp | metered: yes | free allowance: Server traffic 1T, one-way, per the node table. Whether that is a decimal TB or a TiB is not stated. | source: [1]
- identity: anonymous | detail: The page publishes the privilege port and password per node; no account is required to use a node. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 TB one-way per server [1]
  - request-rate: 5 mappings per user [1]
- binding note: if the operator means TiB it passes. There is no other cap in the way.
- interface detail: Standard frpc against a published node, privilege port and password.
- tooling: any frpc
- composes with: A 1 TB one-way free frp node that can carry a WG UDP tunnel, if the 2019-era node is still up.
- reliability: Weekly restart at 03:00 Monday; node IPs were blocked at national level twice in 2019.
- notes: The closest free frp endpoint to the volume bar, and anonymous. Its history section is the useful part: a 2019 note says a user running a proxy got 222.222.0.0/8 blocked wholesale, which is the blast radius of a shared free endpoint. Node pages date from 2019 and the server version is 0.60.0, so uptime today is unproven.
- evidence note: The node table is on the page today. A clarification of TB versus TiB, or a measured month, would move the verdict.
- extras:
  - wg_path: inside-udp
  - wg_detail: The page introduces frp as supporting tcp, udp, http and https and gives a privilege port, an xtcp port and a monitor port per node; a WG datagram can be proxied on a port in 20000-50000.
  - ingress: udp
  - volume_tib_month: 0.909
  - volume_stated: Server traffic 1T, one-way, per the node table. Whether that is a decimal TB or a TiB is not stated.
  - bytes_transit: yes
  - transit_note: WaiWang.Men nodes carry the datagrams.
- evidence:
  - [1] 2026-10-23: US Buffalo node: 1000M shared, 1T one-way traffic, 5 mappings, ports 20000-50000, public privilege password
  - [1] 2026-10-23: Dallas and Russia nodes also list 1T one-way traffic at 100M shared
- sources:
  - [1] https://waiwang.men/
