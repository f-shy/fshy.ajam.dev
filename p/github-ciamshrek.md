# wormhole-vpn

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-ciamshrek/ | JSON https://fshy.ajam.dev/api/v1/entity/github-ciamshrek.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wormhole-vpn

- `egress/wormhole-vpn` | self-hosted, last resort | verdict paid-only | evidence documented | binding volume-quota | category tool (wireguard transport) | tier paid
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/ciamshrek/wormhole-vpn
- price USD 5 per month, Workers paid plan | parsed USD 5/mo
- free tier: no free tier: the README requires "Cloudflare account (Workers paid plan, $5/mo)" | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the Worker plan is priced per month, not per byte, and the README states no transfer figure; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: a Cloudflare account on the Workers paid plan at $5/mo, which needs a payment method | country: None
- interface: cli
- limits:
  - volume-quota (binding): no figure stated; the Workers paid plan is billed per request and duration beyond the included allowance [1]
- binding note: the Worker sits in the data path and every datagram becomes Worker work, so the plan's request and duration billing is what fails first at sustained volume; the README states no figure for it
- interface detail: wrangler deploy plus a 12 MB Go bridge
- tooling: Go bridge plus pnpm and wrangler; a CA certificate must be installed on each device
- composes with: composes with a Cloudflare account and a paid Workers plan, and with cloudflare-tunnel only if the Worker is fronted by one.
- reliability: the Worker terminates and re-originates TLS, so every upstream connection is intercepted by design; single maintainer, no releases
- notes: Experimental proxy design routing WireGuard connections through Cloudflare Workers. Requires paid Cloudflare Workers subscriptions for WebSocket and network routing.
- evidence note: Workers-based proxy architecture and WebSocket encapsulation are documented in project source code.
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: device runs a stock WireGuard client against localhost:51820, a Go bridge (wireguard-go plus gvisor netstack) forwards over one WebSocket to a Cloudflare Durable Object
  - ingress: tcp
  - volume_stated: not applicable; the Worker plan is priced per month, not per byte, and the README states no transfer figure
  - bytes_transit: yes
  - transit_note: through a Cloudflare Durable Object, which sees the plaintext of every intercepted connection
  - hosting_requirement: no locally owned host, but a Cloudflare Workers paid plan at $5/mo, and a device able to run the Go bridge
  - last_release: none; last push 2026-04-06
  - stars: 2
- evidence:
  - [1] 2026-10-23: "Cloudflare account (Workers paid plan, $5/mo)" in the prerequisites
  - [1] 2026-10-23: the architecture line: stock WireGuard client, Go bridge over a single WebSocket, Durable Object, TLS MITM, then fetch() upstream
  - [1] 2026-10-23: 2 stars, no releases, last push 2026-04-06; the description calls it "Very rough"
- sources:
  - [1] https://github.com/ciamshrek/wormhole-vpn
