# wg-tcp-tunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-arkq/ | JSON https://fshy.ajam.dev/api/v1/entity/github-arkq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wg-tcp-tunnel (arkq)

- `egress/wg-tcp-tunnel` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/arkq/wg-tcp-tunnel
- price USD 0
- free tier: no service and no account; source under MIT | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; a public-IP server and a client | country: None
- interface: cli
- binding note: the constraint is a public-IP server at the far end, outside the vocabulary; the build can also reach the far end through ngrok
- interface detail: wg-tcp-tunnel --src-tcp/--dst-udp on one end, --src-udp/--dst-tcp on the other
- tooling: cmake plus Boost.Asio; systemd and Termux runit units in tree
- composes with: composes with any TCP forwarder that hands over a raw stream, including an ngrok TCP endpoint, and with a plain public-IP host.
- reliability: source-built only; no release artefacts; the ngrok path inherits ngrok's connection accounting
- notes: Tunnel client encapsulating WireGuard over TCP, with built-in support for dialing ngrok TCP endpoints (-DENABLE_NGROK=ON). Requires compiling from source with Boost and CMake.
- evidence note: a measured run through the ngrok path would raise it, and would be the first measurement of a hosted tunnel carrying WireGuard
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "This project is a simple UDP-over-TCP tunneling. The main purpose of it is to allow WireGuard to work over TCP"; server '--src-tcp=0.0.0.0:51820 --dst-udp=127.0.0.1:51820', client '--src-udp=127.0.0.1:51822 --dst-tcp=<SERVER-IP>:51820' with Endpoint = 127.0.0.1:51822
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: the far end forwards into the local WireGuard listener
  - hosting_requirement: a host on a public address running the server half, or an ngrok TCP endpoint in its place
  - last_release: v1.1.2 tag, no release object, last commit 2026-08-28
  - stars: 38
- evidence:
  - [1] 2026-10-23: the purpose sentence, both invocations, and the Endpoint rewrite
  - [1] 2026-10-23: "-DENABLE_NGROK=ON ... --ngrok-api-key=KEY --ngrok-dst-tcp-endpoint=ENDPOINT"; the tunnel can use an NGROK endpoint as its destination
  - [1] 2026-10-23: tags v1.1.2 latest, no GitHub release objects, last commit 2026-08-28; 38 stars
  - [1] 2026-10-23: build options -DENABLE_WEBSOCKET and -DENABLE_RUNIT (Termux service)
- sources:
  - [1] https://github.com/arkq/wg-tcp-tunnel
