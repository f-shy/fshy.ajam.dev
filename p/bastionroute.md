# BastionRoute

> bastionroute.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bastionroute/ | JSON https://fshy.ajam.dev/api/v1/entity/bastionroute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BastionRoute

- `egress/bastionroute` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding volume-quota | category udp relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://bastionroute.io/
- price USD 0
- free tier: A deliberately minimal forwarding fabric for WireGuard endpoints operating behind CGNAT, mobile networks and other NAT environments. No price, plan or allowance is published; the repository is v0.1.0-alpha. | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published. The relay is described as seeing connections, timing, traffic volume, frame sizes and connection state, but no cap is named.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The README defines no authentication or accounts: BastionRoute intentionally does not define encryption, authentication, authorization, payload schemas, or application semantics. | country: None
- interface: cli, unknown
- limits:
  - volume-quota (binding): no published allowance; relay capacity unknown [1]
- binding note: With no meter published and an alpha relay, the first failure at 1 TiB/month would be relay capacity or availability, not a stated cap.
- interface detail: Relay plus shim binaries; the README describes a multi-shim architecture with no command reference.
- tooling: Shim plus relay from GitHub; no packaged client.
- composes with: Run the relay on a free VM and the shim next to the WireGuard endpoint; the free VM gets a UDP path it would not otherwise have.
- reliability: Alpha, single author, no authentication layer; the site itself says a hostile relay can drop, delay or disrupt traffic.
- notes: Open-source UDP relay designed to forward WireGuard connections from behind CGNAT. Open-source software with no commercial hosted service; deployment requires a virtual machine.
- evidence note: Only the project's own README, site and a Show HN post exist; no hosted signup and no pricing page were found. Running the relay would move this to measured.
- self hosted: yes
- extras:
  - wg_path: inside-udp
  - wg_detail: Its stated purpose is to carry WireGuard: the endpoint establishes an outbound WebSocket connection; the relay forwards opaque traffic; WireGuard remains the endpoint-to-endpoint security layer. The relay carries UDP datagrams as binary WebSocket frames.
  - ingress: udp
  - volume_stated: No allowance is published. The relay is described as seeing connections, timing, traffic volume, frame sizes and connection state, but no cap is named.
  - bytes_transit: yes
  - transit_note: A self-run or third-party relay forwards opaque frames between peers.
- evidence:
  - [1] 2026-10-23: A forwarding fabric for WireGuard endpoints behind CGNAT: outbound WebSocket, opaque forwarding, WireGuard as the trust boundary; no price or plan.
  - [2] 2026-10-23: v0.1.0-alpha; relays UDP datagram streams between outbound-connected peers over WebSocket; defines no authentication.
  - [3] 2026-10-23: Show HN submission for an outbound-initiated WebSocket relay fabric for UDP; the item's own timestamp could not be retrieved from the HN API.
- sources:
  - [1] https://bastionroute.io/
  - [2] https://github.com/klauscam/BastionRoute/blob/main/README.md
  - [3] https://news.ycombinator.com/item?id=48856767
