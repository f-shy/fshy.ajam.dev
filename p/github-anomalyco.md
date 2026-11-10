# OpenTunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-anomalyco/ | JSON https://fshy.ajam.dev/api/v1/entity/github-anomalyco.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenTunnel

- `egress/opentunnel` | fails-egress | evidence reported | binding none | category hosted blind tls tunnel (tcp 443, tls clienthello only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/anomalyco/opentunnel
- price USD 0
- free tier: each client gets a unique <id>.opentunnel.xyz subdomain and TLS is terminated locally | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance or price is published in the README.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: a client claims a route by hostname; no account is described in the README. | country: None
- interface: cli
- binding note: The relay routes by TLS SNI in the ClientHello message; non-TLS traffic and UDP packets are not routed.
- interface detail: npm client.
- tooling: vendor client (TypeScript).
- composes with: Web ingress for a free VM, with client-side TLS termination.
- reliability: Depends on a Cloudflare TCP Workers beta and a temporary AWS relay.
- notes: Blind TLS relay on Cloudflare Workers with an AWS relay for inbound TCP. Interesting shape, no UDP.
- evidence note: The hosted service is young (MIT declared, no LICENSE file); a published quota would sharpen the binding.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No byte allowance or price is published in the README.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'It accepts public TCP on 443 and reads only the TLS ClientHello. A tunnel hostname is carried, still encrypted, over the tunnel bridge WebSocket'
- sources:
  - [1] https://github.com/anomalyco/opentunnel
