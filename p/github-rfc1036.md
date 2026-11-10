# udptunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-rfc1036/ | JSON https://fshy.ajam.dev/api/v1/entity/github-rfc1036.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## udptunnel (rfc1036)

- `egress/udptunnel` | self-hosted, last resort | verdict paid-only | evidence reported | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/rfc1036/udptunnel
- price USD 0
- free tier: no service and no account; a small C program | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account | country: None
- interface: cli
- binding note: Requires dedicated server endpoints at both ends of the tunnel.
- interface detail: udptunnel -s / -c
- tooling: C, built from source
- composes with: composes with a host at each end and nothing else.
- reliability: unauthenticated by design; predates WireGuard and inherits none of its protections at the transport layer
- notes: Legacy tunnel utility wrapping UDP packets over TCP connections without TLS or authentication. Operates point-to-point between two hosts.
- evidence note: the repository README was not read; the description and the WireGuard limitations page are the evidence, so a read of the source would raise it to documented
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "Tunnel UDP packets in a TCP connection"; one side listens for TCP, the other for UDP, and WireGuard's endpoint points at the UDP side
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: through the server half to the UDP listener
  - hosting_requirement: two hosts, one listening on TCP and one forwarding to the local UDP port
  - last_release: no releases; last push 2024-04-22
  - stars: 222
- evidence:
  - [1] 2026-10-23: repository description "Tunnel UDP packets in a TCP connection"; 222 stars; last push 2024-04-22; no releases
  - [2] 2026-10-23: WireGuard names udptunnel alongside udp2raw as a project that can transform its UDP packets into TCP
- sources:
  - [1] https://github.com/rfc1036/udptunnel
  - [2] https://www.wireguard.com/known-limitations/
