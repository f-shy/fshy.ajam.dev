# nostr-vpn

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-mmalmi/ | JSON https://fshy.ajam.dev/api/v1/entity/github-mmalmi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nostr-vpn

- `egress/nostr-vpn` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/mmalmi/nostr-vpn
- price USD 0
- free tier: Tailscale-style private mesh VPN using Nostr identities and signed network rosters, with a FIPS-backed data plane. Supports MagicDNS, subnet routes and exit nodes, with a Rust CLI/daemon and native desktop/mobile apps. MIT License. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Tailscale-shaped mesh with a FIPS data plane.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Tailscale-shaped mesh with a FIPS data plane. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Tailscale-style private mesh VPN using Nostr identities and signed network rosters, with a FIPS-backed data plane. Supports MagicDNS, subnet routes and exit nod
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/mmalmi/nostr-vpn
