# tunelo.net

> tunelo.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunelo/ | JSON https://fshy.ajam.dev/api/v1/entity/tunelo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunelo.net

- `egress/tunelo-net` | fails-egress | evidence documented | binding none | category http tunnel | tier public relay
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:36:40.988Z (live) | stale on 2026-12-04
- url https://tunelo.net/
- price USD 0
- free tier: Free and open source; the tunelo binary defaults to the public relay at tunelo.net:4433 with no account and no signup. No byte cap, rate or paid tier is published. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The site is one page; /pricing, /terms, /docs and /faq return the same page, and it states no byte cap or tolerance.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance, rate or paid tier is published for the public relay; it is described as free and open source.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account, no signup: the client connects to the relay and is assigned a random subdomain. | country: None
- interface: cli
- limits note: No byte cap, concurrency cap or rate limit is stated on the site.
- binding note: No limit is published; the transport is HTTP routed by Host header, so a raw TCP or UDP forward has no path.
- interface detail: One binary: tunelo port PORT opens an HTTPS subdomain of tunelo.net; the binary speaks QUIC to the relay on UDP port 4433.
- tooling: Install script for Linux, macOS and Windows; a single Rust binary that holds the tunnel command, a file server and the relay.
- composes with: Routes by the Host header, so only HTTP and HTTPS traffic reaches the local service; a raw TCP or UDP port has no path.
- reliability: No paid tier exists to buy more.
- notes: A hosted QUIC relay run by the maintainer of the open-source tunelo repository. HTTP tunnels only; the page publishes no byte cap, no tolerance and no paid tier.
- evidence note: A measured transfer through the public relay would show its real byte and rate tolerance; the site publishes none.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No byte allowance is published for the public relay.
  - bytes_transit: yes
  - transit_note: the public relay copies bytes between the visitor's TCP connection and a QUIC stream
- evidence:
  - [1] 2026-11-03: the public relay at tunelo.net:4433 is the default, with no account and no signup | capture: sha256:0c13e0aaadcbd81abf444b4bbd32fcc5b73e42c19ccf32cac4067fa038be252f | quote: The client and relay are fully decoupled. The client defaults to the public relay at `tunelo.net:4433` — or use `--relay` to point at your own. No account, no signup.
  - [1] 2026-11-03: the tunnel connection uses UDP port 4433 (QUIC) | capture: sha256:0c13e0aaadcbd81abf444b4bbd32fcc5b73e42c19ccf32cac4067fa038be252f | quote: UDP port 4433 open for QUIC tunnel connections
  - [1] 2026-11-03: the relay routes by Host header, an HTTP tunnel | capture: sha256:0c13e0aaadcbd81abf444b4bbd32fcc5b73e42c19ccf32cac4067fa038be252f | quote: When a browser hits that URL, the relay peeks at the Host header, finds the matching tunnel, opens a QUIC stream, and does `copy_bidirectional` between the TCP socket and the QUIC stream.
  - [1] 2026-11-03: the site states the price as free and open source; it names no paid tier | capture: sha256:0c13e0aaadcbd81abf444b4bbd32fcc5b73e42c19ccf32cac4067fa038be252f | quote: | Price | Free tier limited | Free & open source |
  - [1] 2026-11-03: the client connects outbound to the relay | capture: sha256:0c13e0aaadcbd81abf444b4bbd32fcc5b73e42c19ccf32cac4067fa038be252f | quote: The tunnel is outbound-only — the client connects to the relay, not the other way around.
  - [2] 2026-11-03: latest release v0.3.0 adds stable subdomains tied to an Ed25519 identity | capture: sha256:bea07059316340c69c782cb95a0d39a08d2daf9f91b4c9a7de2f5b3a5ac7b6a8 | quote: Stable self-owned subdomains via Ed25519 identity
- sources:
  - [1] https://tunelo.net/
  - [2] https://github.com/jiweiyuan/tunelo/releases
