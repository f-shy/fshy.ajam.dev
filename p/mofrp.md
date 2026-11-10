# MoFrp

> mofrp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mofrp/ | JSON https://fshy.ajam.dev/api/v1/entity/mofrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MoFrp

- `egress/mofrp` | qualifies-with-caveat | evidence unverified | binding none | category tcp+udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:52:57.443Z (live) | stale on 2026-11-19
- url https://www.mofrp.com/
- price USD 0
- free tier: MoFrp promises a permanently free basic service; the free tier is a check-in traffic model, where signing in each day grants additional traffic. [translated] | unit: bytes | metered on: unstated | read on: 2026-10-23 | source: [1] | note: [translated] Users who sponsor nodes receive more bandwidth and a larger traffic quota; the page gives no figure.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte figure is published on the marketing pages: traffic is granted by a daily check-in whose amount the site does not state, and the detail sits behind the console login at console.mofrp.com.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Not established. console.mofrp.com/login serves a password login and console.mofrp.com/register redirects to the same login page, so no field list was visible. The token 'email' is the shape most likely for a console of this kind and is not a reading; treat the gate as unknown until an account is attempted. | country: None
- interface: cli, rest
- limits:
  - volume-quota: daily check-in traffic; amount not published [1]
- binding note: No constraint can be named: the free allowance is not published, so neither the quota nor the shaper can be shown to bind first. A check-in-only model normally lands near a few GB per month, which would fail on volume.
- interface detail: Web panel for tunnel config, a Go client with no dependencies, and a documented API at /api/v3/tunnels.
- tooling: Go single-binary client on Windows/macOS/Linux/Docker, plus a documented REST API; wg-quick on the local box
- composes with: Supports email registration and UDP port forwarding via check-in allowance.
- reliability: None established; the vendor states tunnels persist as long as the terms are kept.
- notes: Chooses no number at all on the public pages, which is itself the finding: the whole commercial surface is the console. Listed as a candidate to test with one throwaway account rather than dismissed.
- evidence note: Protocol architecture and free service tier are documented. Bandwidth quotas and port assignments require account login.
- extras:
  - wg_path: inside-udp
  - wg_detail: The site lists TCP / UDP / HTTP / HTTPS / Websocket / P2P as the protocol stack, so a WG datagram can ride a UDP tunnel. No WG config is issued.
  - ingress: udp
  - volume_stated: No byte figure is published on the marketing pages: traffic is granted by a daily check-in whose amount the site does not state, and the detail sits behind the console login at console.mofrp.com.
  - bytes_transit: yes
  - transit_note: Vendor relays, domestic and overseas nodes.
- evidence:
  - [1] 2026-10-23: free service, protocol stack TCP/UDP/HTTP/HTTPS/Websocket/P2P, check-in traffic model, domestic and overseas nodes
  - [1] 2026-11-03: [translated] the free tier is a daily check-in traffic model, and users who sponsor nodes get more bandwidth and a larger traffic quota; no figure is given | capture: sha256:b71d68cfe66916f67baa54875996e2c4dcee59c3357aedfc0ec327e5def6cc5f | quote: MoFrp 采用签到流量制，每天签到即可获得额外流量。同时，赞助节点的用户将获得更高的带宽和更多的流量配额。
  - [1] 2026-11-03: [translated] a user is written in Go and runs as a single file with no dependencies | capture: sha256:b71d68cfe66916f67baa54875996e2c4dcee59c3357aedfc0ec327e5def6cc5f | quote: Go 语言编写，单文件运行，无依赖。
  - [1] 2026-11-03: [translated] the protocol stack is TCP, UDP, HTTP, HTTPS, Websocket and P2P | capture: sha256:b71d68cfe66916f67baa54875996e2c4dcee59c3357aedfc0ec327e5def6cc5f | quote: TCP / UDP / HTTP / HTTPS / Websocket / P2P。无论是建站还是开服，统统搞定。
  - [1] 2026-11-04: the free tier is a daily check-in traffic model with no figure stated | capture: sha256:b71d68cfe66916f67baa54875996e2c4dcee59c3357aedfc0ec327e5def6cc5f | quote: MoFrp 采用签到流量制，每天签到即可获得额外流量。同时，赞助节点的用户将获得更高的带宽和更多的流量配额。
- sources:
  - [1] https://www.mofrp.com/
