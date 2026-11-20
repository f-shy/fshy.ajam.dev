# wireguard-ws

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-n0madic/ | JSON https://fshy.ajam.dev/api/v1/entity/github-n0madic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wireguard-ws

- `egress/wireguard-ws` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/n0madic/wireguard-ws
- price USD 0
- free tier: no service and no account; a fork of wireguard-go with a WebSocket transport | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account | country: None
- interface: cli
- binding note: both ends must run the fork and the server needs a TLS certificate; there is no hosted service to attach to
- interface detail: wireguard-ws wg0 with WG_WS=1
- tooling: go build; TLS certificates for the server side
- composes with: composes with any host where the operator can run the forked binary at both ends; no CDN is documented as tested.
- reliability: client defaults to skipping certificate verification (WG_WS_INSECURE=1); no releases, one author
- notes: The interesting property is that the transport change happens inside the WireGuard implementation, so the interface and the configuration stay standard: this is the closest thing to a wrapper that a .conf-only router could accept, if the router ran the fork. It does not, so in practice the fork must run on a Linux host at both ends. Zero stars and no releases make it a reference for the approach rather than a deployment.
- evidence note: the repository has no releases and no stars, so the rung cannot rise without a build and a measured run
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: "Fully compatible with standard wg and wg-quick tools"; WG_WS=1 switches the transport and the peer endpoint stays host:port
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: over a websocket between two hosts running the fork
  - hosting_requirement: two hosts running the fork, the server one with a TLS certificate
  - last_release: none; last push 2026-06-12
  - stars: 0
- evidence:
  - [1] 2026-10-23: "a fork of wireguard-go with added WebSocket transport support ... Fully compatible with standard wg and wg-quick tools"
  - [2] 2026-10-23: WG_WS=1 with WG_WS_CERT_FILE on the server and WG_WS_INSECURE=1 on a user; clients connect to wss://host:port/ws
  - [1] 2026-10-23: 0 stars, no releases, last push 2026-06-12
- sources:
  - [1] https://github.com/n0madic/wireguard-ws
  - [2] https://raw.githubusercontent.com/n0madic/wireguard-ws/master/README.md
