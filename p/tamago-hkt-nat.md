# Tamago HKT NAT

> Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tamago-hkt-nat/ | JSON https://fshy.ajam.dev/api/v1/entity/tamago-hkt-nat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tamago HKT NAT

- `egress/tamago-hkt-nat` | fails-quota | evidence reported | binding volume-quota | category free nat vps | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://www.nodeseek.com/post-960139-1
- price USD 0
- free tier: HKT.NAT.500M.VPS: 1 vCPU, 0.25 GB RAM, 8 GB NVMe, shared 500 Mbps, 300 GB traffic, 1 shared HKT IPv4, 1 HKT IPv6 SLAAC, 5 custom NAT ports, Debian 12 only. [translated] | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 300 GB of traffic.; ingress: udp | metered: yes | free allowance: 300 GB of traffic. | source: [1]
- identity: email | detail: Not described in the post; NAT VPS signups of this class typically take an email plus a panel account. | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 300 GB [1]
  - per-ip-shaping: 500 Mbps shared [1]
- binding note: 300 GB is about 0.27 TiB, so the byte allowance fails first, at roughly a quarter of the test.
- interface detail: Root SSH on Debian 12.
- tooling: ssh, wg-quick, nftables
- composes with: WG over the IPv6 SLAAC address would avoid the NAT port allocation entirely, if the local network has IPv6.
- reliability: Debian 12 only; a 0.25 GB RAM box is tight for a WG plus anything else.
- notes: Explicit custom NAT ports plus IPv6 SLAAC is the shape that lets WG work without a public IPv4. The 300 GB cap is the blocker. The post is a resale of a free machine, which is itself evidence that these free NAT boxes get traded.
- evidence note: A marketplace post quoting the plan; the vendor page was not read. Vendor confirmation would raise the rung.
- extras:
  - wg_path: native-conf
  - wg_detail: Root on a NAT VPS with 5 custom NAT ports and a routed IPv6; WG can bind a port from the allocated set, or ride IPv6 directly.
  - ingress: udp
  - volume_tib_month: 0.273
  - volume_stated: 300 GB of traffic.
  - bytes_transit: yes
  - transit_note: Hong Kong host carries the traffic.
- evidence:
  - [1] 2026-10-23: 300 GB traffic, 5 custom NAT ports, 500 Mbps shared, free machine
- sources:
  - [1] https://www.nodeseek.com/post-960139-1
