# arena-tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-dc-holdings-spa/ | JSON https://fshy.ajam.dev/api/v1/entity/github-dc-holdings-spa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## arena-tunnel

- `egress/arena-tunnel` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/dc-holdings-spa/arena-tunnel
- price USD 0
- free tier: no service and no account; AGPL-3.0 source with static binaries, described as "Free public ingress through any CDN" | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the tunnel's ceiling is the CDN's, and the README states none; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account for the DIY path; the vendor's own deployment adds a browser pairing flow with a signed-in identity | country: None
- interface: cli
- binding note: the constraint is a WireGuard server host plus a way to publish an HTTP port, which is the same host requirement as every other wrapper
- interface detail: arena-tunnel client and arena-tunnel-server
- tooling: single Go binary per platform, cloudflared or any HTTP publisher in front
- composes with: the intended composition is cloudflare-tunnel Free in front of arena-tunnel-server, which makes an HTTP-only hosted tunnel carry WireGuard for the first time without a paid plan.
- reliability: new and lightly used; client needs root for the TUN device; one WebSocket per session means a dropped TCP connection restarts the tunnel
- notes: The clearest statement's central problem: "Most free CDNs (Cloudflare Free, Fastly, Bunny) only proxy HTTP/WS", so WireGuard has to be framed into WebSocket to use them. Released two days before this read, four stars, single purpose. It still needs the WireGuard server host, so its claim of no VPS rental assumes the reader already has somewhere to put the server half. Frame-per-datagram framing avoids putting a length-prefixed stream in the datagram path, but the websocket still rides TCP.
- evidence note: Software design documented. Live throughput over WebSocket tunnels through Cloudflare remains unmeasured.
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "encapsulating each WireGuard UDP datagram inside one binary WebSocket frame"; a user runs wireguard-go locally and the server hands frames to a local WireGuard interface
  - ingress: tcp
  - volume_stated: not applicable; the tunnel's ceiling is the CDN's, and the README states none
  - bytes_transit: yes
  - transit_note: through cloudflared and Cloudflare's edge, then to the server half
  - hosting_requirement: a WireGuard server host plus cloudflared or another HTTP publisher; a user half needs root for a TUN device
  - last_release: v1.2.1 2026-10-21
  - stars: 4
- evidence:
  - [1] 2026-10-23: "punches a WireGuard VPN through any HTTP/HTTPS path - including a free Cloudflare Tunnel. No VPS rental" and "one WS binary frame <-> one UDP datagram"
  - [1] 2026-10-23: the DIY section: "Requires a running WireGuard server on the same host and a way to publish your HTTP port (cloudflared tunnel, ngrok, etc.)"
  - [1] 2026-10-23: "Latency cost: ~80-150 ms one-way through a free CF tunnel from most of LATAM" - the author's own figure, not reproduced
  - [1] 2026-10-23: release v1.2.1 published 2026-10-21; last push 2026-10-23; 4 stars
- sources:
  - [1] https://github.com/dc-holdings-spa/arena-tunnel
