# Serververse Network Transit

> serververs.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serververs/ | JSON https://fshy.ajam.dev/api/v1/entity/serververs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Serververse Network Transit

- `egress/serververse-network-transit` | paid-only | evidence documented | binding volume-quota | category routed public IPv4 over WireGuard | tier transit
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://docs.serververs.com/labs/ip-transit/begin
- price unverified: no price on /nt, /network, the docs, or the store product page
- free tier: No free tier named. The product is sold through a store: "Checkout stays in sync with the store - the price you see on /nt is the price you pay at store.serververs.com." That store page carries no price. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published on the docs, the /nt page, the /network page or the store product page.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: A dashboard login at labs.serververs.com issues the install command; the signup form and payment step were not read. | country: None
- interface: cli, rest
- limits:
  - volume-quota (binding): unpublished [2]
- binding note: With no published allowance, the first thing that fails at 1 TiB/month is the vendor's own judgement rather than a counter. The beta status is the bigger risk: "Network Transit is currently in beta. Breaking changes may occur between minor versions."
- interface detail: Install command plus dashboard; "Manage your account and tunnels from your own scripts. Premium feature."
- tooling: one-line installer; customer API as a premium feature
- composes with: Designed exactly for this shape: a Linux box anywhere gets a routed public IP without moving into a datacentre.
- reliability: Beta service with breaking changes between minor versions; no uptime figure published.
- notes: serververse.io does not answer; the live brand is serververs.com, with docs.serververs.com and store.serververs.com. The install-command design is the notable part: it removes the config-file step entirely, which is why wg_path is registration-api rather than native-conf.
- evidence note: Registration API flow and service features are documented. Commercial pricing and transfer allowances are unverified.
- extras:
  - wg_path: registration-api
  - wg_detail: Provisioning is a token, not a file: "Your personalised install command - including your provisioning token - is generated for you" and "Serververse provisions your tunnel on the edge network and your server receives a routable public IP." The transport is named: "Traffic is routed through the Serververse edge network over a secure WireGuard tunnel". A customer API exists as a premium feature.
  - ingress: tcp+udp
  - volume_stated: No allowance is published on the docs, the /nt page, the /network page or the store product page.
  - bytes_transit: yes
  - transit_note: The vendor's edge network announces and routes the address.
- evidence:
  - [2] 2026-10-23: token-based install command, WireGuard transport, routable public IP on a machine behind NAT, beta status
  - [1] 2026-10-23: two buy paths, IP lease and transit, both sold through the store; no price shown
  - [3] 2026-10-23: the product page exists and carries marketing copy but no price
- sources:
  - [1] https://serververs.com/nt
  - [2] https://docs.serververs.com/labs/ip-transit/begin
  - [3] https://store.serververs.com/products/network-transit
