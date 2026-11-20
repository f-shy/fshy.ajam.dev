# usque

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-diniboy1123/ | JSON https://fshy.ajam.dev/api/v1/entity/github-diniboy1123.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## usque

- `egress/usque` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/Diniboy1123/usque
- price USD 0
- free tier: no service and no account; "an open-source reimplementation of the Cloudflare WARP client's MASQUE mode" | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated by this tool; the traffic reaches Cloudflare WARP; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; registration is performed by the tool | country: None
- interface: cli
- binding note: it adds no quota; its value is that it reaches WARP over TCP or HTTP/2 where WireGuard over UDP fails
- interface detail: usque register / enroll / native-tun / socks5 / http-proxy / l4-proxy / port-forward
- tooling: single Go binary; SOCKS5, HTTP, native TUN and port-forward modes
- composes with: composes with any free compute host that blocks WireGuard but allows QUIC or TCP 443, and with the cloudflare-warp record.
- reliability: the README says only the Linux amd64 binary was tested; userspace QUIC is slower than kernel WireGuard by the author's own statement
- notes: Client tool proxying WireGuard over MASQUE (HTTP/3 or HTTP/2) directly to Cloudflare edge infrastructure. Replaces UDP egress from local clients without requiring a self-hosted remote relay server.
- evidence note: a probe through the native tunnel or the SOCKS5 mode would raise it
- self hosted: yes
- extras:
  - wg_path: registration-api
  - wg_detail: it registers its own WARP device and then carries traffic over MASQUE (Connect-IP, RFC 9484) instead of WireGuard, so there is no .conf and no UDP
  - ingress: none
  - volume_stated: not stated by this tool; the traffic reaches Cloudflare WARP
  - bytes_transit: yes
  - transit_note: through Cloudflare's MASQUE endpoint
  - hosting_requirement: none; runs on the device and dials Cloudflare's edge
  - last_release: v4.2.1 2026-07-20
  - stars: 1493
- evidence:
  - [1] 2026-10-23: "leverages the Connect-IP (RFC 9484) protocol" with native tunnel, SOCKS5, HTTP and L4 proxy modes
  - [1] 2026-10-23: "reports that WARP+ doesn't work anymore over WireGuard arose lately" citing wgcf issue 459, and "certain networks block WireGuard, but don't block QUIC"
  - [1] 2026-10-23: release v4.2.1 published 2026-07-20; last push 2026-07-20; 1493 stars
  - [1] 2026-10-23: "MASQUE is userspace, and so is QUIC, the underlying protocol, making the implementation slower"
- sources:
  - [1] https://github.com/Diniboy1123/usque
