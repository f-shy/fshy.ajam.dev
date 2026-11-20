# Selfhosted Gateway

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-hintjen/ | JSON https://fshy.ajam.dev/api/v1/entity/github-hintjen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Selfhosted Gateway

- `egress/selfhosted-gateway` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.956Z (live) | stale on 2026-12-20
- url https://github.com/hintjen/selfhosted-gateway
- price USD 0
- free tier: Self-hosted Docker-native alternative to Cloudflare Tunnel/ngrok. Reverse Proxy-over-VPN (RPoVPN) using WireGuard, Caddy and NGINX to expose local docker-compose services to the Internet with automatic HTTPS. AGPL-3.0 License. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. WireGuard plus Caddy and NGINX; the aggregator says HTTP/TCP/UDP.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: WireGuard plus Caddy and NGINX; the aggregator says HTTP/TCP/UDP. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Self-hosted Docker-native alternative to Cloudflare Tunnel/ngrok. Reverse Proxy-over-VPN (RPoVPN) using WireGuard, Caddy and NGINX to expose local docker-compos
  - [2] 2026-11-19: First-party README: the gateway is entirely self-hosted and self-managed; no hosted endpoint is offered. | capture: sha256:6db0af8873839b81ce957de30397d0b474d549bd21dd585bf099754ad2b4b46a | quote: Entirely self-hosted and self-managed, includes local and remote tunneling components.
  - [2] 2026-11-19: The tool provisions tunnels on infrastructure the operator supplies; no hosted allowance is provided. | capture: sha256:6db0af8873839b81ce957de30397d0b474d549bd21dd585bf099754ad2b4b46a | quote: This project automates the provisioning of Reverse Proxy-over-VPN (RPoVPN) WireGuard tunnels with Caddy and NGINX.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/hintjen/selfhosted-gateway
