# udp2raw

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-wangyu/ | JSON https://fshy.ajam.dev/api/v1/entity/github-wangyu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## udp2raw

- `egress/udp2raw` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/wangyu-/udp2raw
- price USD 0
- free tier: no service and no account; source and pre-built static binaries | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; both ends are hosts the operator controls | country: None
- interface: cli
- binding note: the constraint is a root Linux host with raw socket access at both ends, outside the seven-kind vocabulary
- interface detail: udp2raw_amd64 -s / -c
- tooling: static binaries for x86, ARM, Android and some OpenWrt routers
- composes with: only composes with a host rented or obtained free, such as a free-tier VM, and adds nothing to a hosted tunnel.
- reliability: needs root and iptables rules (-a), which is a common silent failure; the README states it survives reconnects and keeps UDP conversations valid
- notes: Encapsulates UDP traffic over fake TCP or raw ICMP headers to bypass firewall throttling. Operates via raw socket manipulation; incompatible with standard Layer 7 reverse proxies or CDNs, requiring a dedicated remote server running udp2raw.
- evidence note: a measured run through a named path would raise it; no throughput number is published
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "A Tunnel which turns UDP Traffic into Encrypted FakeTCP/UDP/ICMP Traffic by using Raw Socket"; WireGuard rides inside it because WireGuard is the UDP traffic
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: the bytes cross both hosts, with the far host forwarding to the WireGuard listener
  - hosting_requirement: two root Linux hosts, one of them publicly reachable; fake-TCP needs raw sockets at both ends and cannot pass a managed HTTP forwarder
  - last_release: 20230206.0 2023-02-07
  - stars: 8577
- evidence:
  - [1] 2026-10-23: "turns UDP Traffic into Encrypted FakeTCP/UDP/ICMP Traffic by using Raw Socket" and "Linux host ... with root access"
  - [1] 2026-10-23: the two-sided invocation: server '-s -l0.0.0.0:4096 -r 127.0.0.1:7777 --raw-mode faketcp' and client '-c -l0.0.0.0:3333 -r44.55.66.77:4096'
  - [1] 2026-10-23: release 20230206.0 published 2023-02-07; last push 2025-10-12; 8577 stars
  - [2] 2026-10-23: WireGuard names udp2raw as one of the projects that can transform its UDP packets into TCP
- sources:
  - [1] https://github.com/wangyu-/udp2raw
  - [2] https://www.wireguard.com/known-limitations/
