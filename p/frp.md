# FRP.VIP

> frp.vip | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/frp/ | JSON https://fshy.ajam.dev/api/v1/entity/frp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FRP.VIP

- `egress/frp-vip` | fails-quota | evidence reported | binding per-ip-shaping | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://frp.vip/
- price USD 0
- free tier: Domestic 1M: 1 Mbps, free, 1 port, frps version 0.35.1, note: free trial, one per customer. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Paid tiers say 'unlimited traffic, fair use'; the free tier lists only 1 port and 1 Mbps.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Registration and per-day billing in 'kai coins'; the free tier is limited to one purchase per customer. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): 1 Mbps [1]
  - request-rate: 1 port [1]
- binding note: 1 Mbps sustained is about 0.32 TB per month, so the speed cap fails 1 TiB long before any byte quota could.
- interface detail: frpc with a panel-issued config.
- tooling: frpc 0.35.1
- composes with: Cannot carry 1 TiB/month at 1 Mbps.
- reliability: Runs frps 0.35.1, an old release; nothing about uptime is published.
- notes: The 'unlimited traffic' label is attached to a 1 Mbps pipe, which is the recurring pattern: unlimited bytes at a rate that cannot deliver them. 1 Mbps is 328 GB per month at full duty.
- evidence note: Numbers are from the site's extracted plan table; a direct read of the order page would raise the rung.
- extras:
  - wg_path: inside-udp
  - wg_detail: An frps 0.35.1 endpoint; UDP proxying is an frp feature, but the plan table does not confirm that UDP is enabled for the free port.
  - ingress: udp
  - volume_stated: Paid tiers say 'unlimited traffic, fair use'; the free tier lists only 1 port and 1 Mbps.
  - bytes_transit: yes
  - transit_note: FRP.VIP domestic nodes relay the datagrams.
- evidence:
  - [1] 2026-10-23: free tier is 1 Mbps, 1 port, unlimited traffic claim, one per customer
- sources:
  - [1] https://frp.vip/
