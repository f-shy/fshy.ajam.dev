# OpenTunnel

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-anomalyco/ | JSON https://fshy.ajam.dev/api/v1/entity/github-anomalyco.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenTunnel

- `egress/opentunnel` | fails-egress | evidence documented | binding none | category hosted blind tls tunnel (tcp 443, tls clienthello only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.143Z (live) | stale on 2026-12-20
- url https://github.com/anomalyco/opentunnel
- price USD 0
- free tier: each client gets a unique <id>.opentunnel.xyz subdomain and TLS is terminated locally | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance or price is published on the first-party README; the hosted relay carries visitor TCP 443 bytes over a bridge.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: a client claims a route by hostname; no account is described in the README. | country: None
- interface: cli
- binding note: The relay routes by TLS SNI in the ClientHello message; non-TLS traffic and UDP packets are not routed.
- interface detail: npm client.
- tooling: vendor client (TypeScript).
- composes with: Web ingress for a free VM, with client-side TLS termination.
- reliability: The first-party README describes a hosted Rust relay on Fly.io with PlanetScale MySQL and ZeroSSL ACME certificates; no Cloudflare Workers beta or temporary AWS relay is described.
- notes: Blind TLS relay on Cloudflare Workers with an AWS relay for inbound TCP. Interesting shape, no UDP.
- evidence note: The first-party README has a LICENSE file now and describes a hosted blind TLS relay on Fly.io that reads only the TLS ClientHello and carries no published byte allowance. No hosted free byte allowance is stated.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No byte allowance or price is published in the README.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'It accepts public TCP on 443 and reads only the TLS ClientHello. A tunnel hostname is carried, still encrypted, over the tunnel bridge WebSocket'
  - [1] 2026-11-19: the first-party repository describes a hosted blind TLS relay that carries visitor bytes over a bridge to a local client | capture: sha256:95dc972e78f06e5760d85ac185c09ec39961bcb6204a8bebbfb453ddb2e9b876 | quote: The hosted service is one Rust binary, `crates/opentunnel-server`, on Fly.io
  - [1] 2026-11-19: the hosted relay accepts public TCP 443, reads only the ClientHello and publishes no byte allowance | capture: sha256:95dc972e78f06e5760d85ac185c09ec39961bcb6204a8bebbfb453ddb2e9b876 | quote: It accepts public TCP on 443 and reads only the TLS ClientHello.
  - [1] 2026-11-19: the hosted relay carries visitor bytes and publishes no allowance in the README | capture: sha256:95dc972e78f06e5760d85ac185c09ec39961bcb6204a8bebbfb453ddb2e9b876 | quote: It accepts public TCP on 443 and reads only the TLS ClientHello.
  - [1] 2026-11-19: the current first-party hosted architecture is a Rust binary on Fly.io, not the old Workers and AWS relay | capture: sha256:95dc972e78f06e5760d85ac185c09ec39961bcb6204a8bebbfb453ddb2e9b876 | quote: The hosted service is one Rust binary, `crates/opentunnel-server`, on Fly.io
  - [1] 2026-11-19: the first-party README describes the current hosted relay and no byte allowance | capture: sha256:95dc972e78f06e5760d85ac185c09ec39961bcb6204a8bebbfb453ddb2e9b876 | quote: The hosted service is one Rust binary, `crates/opentunnel-server`, on Fly.io
- sources:
  - [1] https://github.com/anomalyco/opentunnel
