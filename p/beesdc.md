# Qingting Map

> beesdc.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beesdc/ | JSON https://fshy.ajam.dev/api/v1/entity/beesdc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qingting Map (beesdc)

- `egress/qingting-map` | fails-identity | evidence documented | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID yes, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.beesdc.com/
- price USD 0
- free tier: The free edition includes 1 mapping, 1 Mbps, 1 GB per month. [translated] | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 GB per month on the free edition.; ingress: udp | metered: yes | free allowance: 1 GB per month on the free edition. | source: [1]
- identity: national-id | detail: The page says 'complete real-name verification, install the client' before a public mapping can be created. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB per month [1]
  - per-ip-shaping: 1 Mbps [1]
- binding note: 1 GB per month is about 0.0009 TiB; the 1 Mbps cap alone would also cap a month at roughly 0.32 TB.
- interface detail: Vendor client for routers, NAS and desktops.
- tooling: vendor client
- composes with: Too small for anything but a webhook test.
- reliability: No reliability report found.
- notes: Also called flynat on its own page. Two independent blocks: 1 GB and real-name.
- evidence note: Both the quota and the real-name precondition are in the vendor's own text today.
- extras:
  - wg_path: inside-udp
  - wg_detail: The page states TCP and UDP coverage and says TCP/UDP dual protocol covers mainstream multiplayer games; a WG datagram can ride a UDP mapping.
  - ingress: udp
  - volume_tib_month: 0.00091
  - volume_stated: 1 GB per month on the free edition.
  - bytes_transit: yes
  - transit_note: beesdc relays the traffic.
- evidence:
  - [1] 2026-10-23: free edition is 1 mapping, 1 Mbps, 1 GB per month, and real-name verification is required
- sources:
  - [1] https://www.beesdc.com/
