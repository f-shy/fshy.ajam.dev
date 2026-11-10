# wstunnel demo

> github.com | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-erebe/ | JSON https://fshy.ajam.dev/api/v1/entity/github-erebe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wstunnel demo relay

- `egress/wstunnel-demo` | trial-only | evidence unverified | binding write-gated | category udp port forward (demo relay, open-source client) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:52:58.387Z (live) | stale on 2026-11-19
- url https://github.com/erebe/wstunnel
- price USD 0
- free tier: You can give it a try with wstunnel demo server | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no allowance published for the demo relay; it is described as a way to check that you can bypass a proxy, not as a service; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: the demo takes a shared password: '-P demo' with wss://ws.erebe.dev, no account | country: None
- interface: cli
- limits:
  - write-gated (binding): the demo server allowlists one tunnel: 'The tunnel is the only one that is going to be allowed.' [1]
- binding note: The demo relay's allowlist is the first thing that fails, before any byte count: the documented example is a single fixed TCP forward, so a reverse UDP binding is not established to be permitted at all.
- interface detail: Documented demo example: wstunnel client -L 'tcp://4443:10.43.0.11:443' -P demo --tls-sni-override=google.fr wss://ws.erebe.dev. Reverse UDP form (client usage, not shown with the demo): -R 'udp://1212:1.1.1.1:53'.
- tooling: wstunnel static binary
- composes with: wstunnel -R udp://51820 on any free VM, or the demo relay if it permits the binding; this is the shape that composes with a free compute lane
- reliability: a shared demo endpoint with no stated capacity; the operator can withdraw it without notice
- notes: The wstunnel client is genuinely capable of a reverse UDP port and is the standard tool for carrying WireGuard over TCP 443. The free part is the demo relay, which is explicitly a courtesy. A self-run wstunnel server removes the courtesy limit but needs a VM of the user's own, so it is the last resort.
- evidence note: Unverified because the demo's UDP permission was not tested and its capacity is unpublished.
- self hosted: no
- extras:
  - wg_path: inside-udp
  - wg_detail: the client carries raw UDP both ways and reverse mode binds a port on the server: 'udp://1212:1.1.1.1:53 => listen on server for incoming udp on port 1212 and forward to cloudflare dns 1.1.1.1 on port 53 from local machine'. Whether the shared demo relay at wss://ws.erebe.dev permits a reverse UDP binding is not documented.
  - ingress: udp
  - volume_stated: no allowance published for the demo relay; it is described as a way to check that you can bypass a proxy, not as a service
  - bytes_transit: yes
  - transit_note: the wstunnel server unwraps the websocket and emits the datagrams
- evidence:
  - [1] 2026-10-23: the demo server, the -P demo shared password, the allowlist sentence, and the -R udp:// reverse UDP form in the client usage block
  - [1] 2026-10-23: repository metadata: 'Tunnel all your traffic over Websocket or HTTP2 - Bypass firewalls/DPI', public, not archived
  - [1] 2026-11-03: the README's demo example is a local-to-remote TCP forward with the shared password demo | capture: sha256:5d0df32b0aa8468f1688fdaefc9633bbc56e016f357303bbfd4b38ec453f888c | quote: wstunnel client -L 'tcp://4443:10.43.0.11:443' -P demo --tls-sni-override=google.fr wss://ws.erebe.dev
  - [1] 2026-11-03: the README offers a demo server for trying the tunnel | capture: sha256:5d0df32b0aa8468f1688fdaefc9633bbc56e016f357303bbfd4b38ec453f888c | quote: You can give it a try with wstunnel demo server.
  - [1] 2026-11-03: the README's demo example says the one tunnel is the only one allowed | capture: sha256:5d0df32b0aa8468f1688fdaefc9633bbc56e016f357303bbfd4b38ec453f888c | quote: The tunnel is the only one that is going to be allowed.
  - [1] 2026-11-04: the README says the demo relay allows only the one documented tunnel | capture: sha256:9b62e462d31565682d1f90eab8d08ef210525dd375287d219dfadc25312a200f | quote: The tunnel is the only one that is going to be allowed.
  - probe:ws.erebe.dev 2026-11-04: the demo host completes a TLS 1.3 handshake on 2026-11-04 presenting a self-signed certificate | capture: sha256:ad0eba00d3842bb79140ee4c9590655ca07255cc355609030f2356bd3d727b32 | quote: "verify_message": "self-signed certificate"
- sources:
  - [1] https://github.com/erebe/wstunnel

## wstunnel

- `egress/wstunnel` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/erebe/wstunnel
- price USD 0
- free tier: no service and no account; the software is a static binary released under an open licence | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume, and the tunnel's ceiling is whatever the host and the network in between allow; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account required. The client connects to an independently operated wstunnel server. | country: None
- interface: cli
- binding note: Requires an external server host running wstunnel with a public IP address.
- interface detail: wstunnel client / wstunnel server subcommands
- tooling: static binary per platform; a systemd unit is the documented server form
- composes with: a websocket upgrade passes through any TCP or HTTP forwarder that does not buffer, so a free HTTP-only hosted tunnel plus a wstunnel server converts a TCP-only path into a WireGuard path; the wstunnel server still has to run somewhere controlled locally.
- reliability: the udp tunnel auto-closes after 30 s idle unless timeout_sec=0; the client sends websocket pings every 30 s by default; MTU must drop to about 1300 or packets fragment
- notes: Tunneling software forwarding TCP and UDP over WebSocket or HTTP/2. Designed to traverse firewalls and reverse proxies; WebSocket mode supports traversal through CDNs.
- evidence note: measured throughput on a named path would raise it; the README carries only a benchmark image with no numbers in text
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: the README ships a WireGuard recipe: server 'wstunnel server --restrict-to localhost:51820 wss://[::]:443' and client "wstunnel client -L 'udp://51820:localhost:51820?timeout_sec=0' wss://my.server.com:443", with the WireGuard peer Endpoint changed to localhost:51820
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume, and the tunnel's ceiling is whatever the host and the network in between allow
  - bytes_transit: yes
  - transit_note: the bytes cross the wstunnel server, then any CDN or forwarder in front of it
  - hosting_requirement: a host with a public address running wstunnel server; a user half runs on the device
  - last_release: v11.1.0 2026-10-19
  - stars: 7122
- evidence:
  - [1] 2026-10-23: the WireGuard recipe, the udp:// forward with timeout_sec, and the server --restrict-to flag
  - [1] 2026-10-23: release v11.1.0 published 2026-10-19, 7122 stars, last push 2026-10-19
  - [2] 2026-10-23: "If you see some throughput issue, be sure to lower the MTU of your wireguard interface ... to something like 1300 or you will endup fragmenting udp packet (due to overhead of other layer)"
- sources:
  - [1] https://github.com/erebe/wstunnel
  - [2] https://raw.githubusercontent.com/erebe/wstunnel/master/README.md
