# Optimistix Tunnel

> optimistixtunnel.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/optimistixtunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/optimistixtunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Optimistix Tunnel

- `egress/optimistix-tunnel` | dead | evidence documented | binding per-ip-shaping | category ssh tunnel (http, tcp, tls) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-10T03:25:21.415Z (live) | stale on 2026-12-11
- url https://optimistixtunnel.com/features/ssh-tunneling/
- price USD 0
- free tier: None: the service is permanently discontinued and all tunnels, subdomains and accounts are no longer active. | unit: none | metered on: none | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte, port-count or session limit is published; the page says only that it is free.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'No signup, no install' per the aggregator; the page says 'No downloads or installations needed - just use the SSH client'. | country: None
- interface: ssh
- limits:
  - per-ip-shaping (binding): Nothing countable is published, so an unpublished tolerance is what fails at 1 TiB/month. Protocol is the hard wall: HTTPS, TCP and TLS over SSH, with no UDP and no WireGuard path. [1]
- binding note: Nothing countable is published, so an unpublished tolerance is what fails at 1 TiB/month. Protocol is the hard wall: HTTPS, TCP and TLS over SSH, with no UDP and no WireGuard path.
- interface detail: SSH remote forwarding.
- tooling: system ssh only.
- composes with: Free TCP ingress for a VM without a card.
- reliability: the vendor page says the service has been permanently discontinued and points readers at Cloudflare Tunnel instead
- notes: The vendor page read on 2026-11-10 says the service has been permanently discontinued and recommends Cloudflare Tunnel; a third-party harness had already recorded the shutdown on 2026-11-05 after a challenge page had once made the site look alive.
- evidence note: Tunnel specifications and protocol support are documented in official repository guides.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: As read on 2026-10-23, before the shutdown: no byte, port-count or session limit was published; the page said only that it was free. The service has since been discontinued (2026-11-10).
  - bytes_transit: yes
  - death.on: 2026-11-10
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: '100% Free'; 'Completely Free to Use'; 'HTTPS / TCP / TLS Tunnel'
  - [2] 2026-10-23: SSH-based, 'HTTPS / TCP / TLS-supported tunnels', no price or plan table
  - [2] 2026-11-10: the service is permanently discontinued | capture: sha256:2ed63246e7ac6e29e053c7448ce6846586444e97e0ce0b037eebdad775641498 | quote: The service has been permanently discontinued, and all tunnels, subdomains and accounts are no longer active.
  - [2] 2026-11-10: the vendor recommends Cloudflare Tunnel instead | capture: sha256:2ed63246e7ac6e29e053c7448ce6846586444e97e0ce0b037eebdad775641498 | quote: we recommend Cloudflare Tunnel
- sources:
  - [1] https://optimistixtunnel.com/features/ssh-tunneling/
  - [2] https://optimistixtunnel.com/
