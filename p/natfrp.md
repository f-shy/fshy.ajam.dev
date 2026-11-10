# SakuraFrp

> natfrp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/natfrp/ | JSON https://fshy.ajam.dev/api/v1/entity/natfrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SakuraFrp

- `egress/sakurafrp` | fails-identity | evidence documented | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID yes, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.natfrp.com/
- price USD 0
- free tier: Tunnel speed limit 10 Mibps; 2 tunnels; 5 GiB traffic per month; daily check-in grants free traffic. [translated] | unit: GiB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 GiB per month on the free plan, plus whatever the daily check-in adds; the pricing page does not state the check-in amount.; ingress: udp | metered: yes | free allowance: 5 GiB per month on the free plan, plus whatever the daily check-in adds; the pricing page does not state the check-in amount. | source: [1]
- identity: national-id | detail: Real-name verification is mandatory: the FAQ says to buy a verification slot, enter name and ID number, then scan a QR code in the Alipay app with face check, and that it costs CNY 1. A Telegram status post dated 2024-07-09 says overseas nodes also require it from that date. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 5 GiB per month [1]
  - per-ip-shaping: 10 Mibps per tunnel [1]
- binding note: 5 GiB per month is about 200 times below 1 TiB, so the byte quota fails long before the 10 Mibps shaper could matter.
- interface detail: Vendor launcher for Windows/Linux/Android/OpenWRT, or a standard frpc config; the docs publish an API token page.
- tooling: vendor launcher or frpc plus wg-quick on the local side
- composes with: Carries a WG handshake from a CGNAT box to a WG server on a free VM only if a UDP-enabled node is used and the 5 GiB lasts.
- reliability: A Telegram status post says mainland nodes refuse to start a tunnel from a non-mainland client IP; some nodes carry a 'no UDP' marker.
- notes: Two blocks, either one decisive: 5 GiB per month, and an Alipay real-name check that requires a mainland Chinese identity document. Forum roundups describe the traffic as 'claimable by daily check-in', which matches the vendor page but understates that the base allowance is 5 GiB. The overseas-node exemption claimed in the nodeloc roundup is contradicted by the vendor's own 2024-07-09 status post.
- evidence note: The quota and the real-name procedure are both on vendor pages read. Raising the rung would need a probe of an actual UDP tunnel.
- extras:
  - wg_path: inside-udp
  - wg_detail: Help docs list a UDP tunnel type with per-tunnel options (no_budp2, bandwidth_limit), and the Palworld guide says to pick the UDP tunnel type and to avoid servers marked 'no UDP'. A WG datagram fits inside that UDP tunnel; no WG conf is issued.
  - ingress: tcp+udp
  - volume_tib_month: 0.0049
  - volume_stated: 5 GiB per month on the free plan, plus whatever the daily check-in adds; the pricing page does not state the check-in amount.
  - bytes_transit: yes
  - transit_note: SakuraFrp nodes carry the datagrams; the local service terminates them.
- evidence:
  - [1] 2026-10-23: free plan is 10 Mibps, 2 tunnels, 5 GiB per month
  - [2] 2026-10-23: real-name verification is mandatory, costs CNY 1, uses Alipay face check and an ID number
  - [3] 2026-10-23: a UDP tunnel type exists with its own option set
  - [4] 2026-10-23: servers can be marked 'no UDP'; a user must pick a node without that marker
  - [5] 2026-10-23: 'To use NetherNet you must tunnel both TCP and UDP' and the tunnel form takes 'Tunnel type: UDP' [translated]
- sources:
  - [1] https://www.natfrp.com/
  - [2] https://doc.natfrp.com/faq/realname.html
  - [3] https://doc.natfrp.com/frpc/manual
  - [4] https://doc.natfrp.com/game/palworld.html
  - [5] https://doc.natfrp.com/game/mc/bedrock.html
