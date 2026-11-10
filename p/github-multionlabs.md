# Wireport

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-multionlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/github-multionlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wireport

- `egress/wireport` | self-hosted, last resort | verdict paid-only | evidence documented | binding volume-quota | category self-hosted WireGuard ingress | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/MultionLabs/wireport
- price USD 0
- free tier: 'Self-hosted ingress proxy & VPN tunnel. Securely exposes private local & Docker-based services to the Internet, with free, automatically renewable SSL certificates.' MIT licensed; no vendor quota. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published; the gateway host's own egress is the limit.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: Self-hosted open-source software: no vendor account at all. | country: None
- interface: cli
- limits:
  - volume-quota (binding): the software imposes no byte meter; what runs out is the monthly allowance of the host it runs on, and that host is a separate provider [1]
- binding note: the software imposes no byte meter; what runs out is the monthly allowance of the host it runs on, and that host is a separate provider
- interface detail: 'wireport service publish --local http://10.0.0.2:3000 --public https://demo.example.com:443'
- tooling: wireport CLI, Docker, docker labels
- composes with: the same free-tier VPS shape as Pangolin and Wiredoor: one host, one WireGuard mesh, public ports bound on the host
- reliability: the gateway is a single public Linux host; losing it loses every published service
- notes: Found by the required search 'wireguard ingress public', not on the supplied list. The README body carries the L4 TCP/UDP claim; the gateway port list came from the search index snippet, so that row is one rung weaker than the rest.
- evidence note: A published UDP service through a real gateway would raise this to measured.
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: 'Powered by WireGuard, CoreDNS and Caddy'. The CLI or Docker labels drive the tunnel; no .conf export is documented.
  - ingress: tcp+udp
  - volume_stated: No allowance is published; the gateway host's own egress is the limit.
  - bytes_transit: yes
  - transit_note: the gateway terminates and relays; the bytes cross its public NIC both ways
- evidence:
  - [1] 2026-10-23: 'Reverse proxy with support for HTTP(S) 1/2/3, WebSocket, gRPC (over HTTP/2) and TCP/UDP (Layer-4)'; 'Powered by WireGuard, CoreDNS and Caddy'
  - [2] 2026-10-23: the gateway is 'a Linux-based machine with Docker installed, a public IP address, and the following open ports: 80/tcp, 443/tcp, 4060/tcp, 51820/udp and 32420-32421/tcp+udp', via the search index snippet of the README
- sources:
  - [1] https://github.com/MultionLabs/wireport
  - [2] https://github.com/MultionLabs/wireport/
