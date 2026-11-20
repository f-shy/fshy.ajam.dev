# nostr-vpn

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-mmalmi/ | JSON https://fshy.ajam.dev/api/v1/entity/github-mmalmi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nostr-vpn

- `egress/nostr-vpn` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.740Z (live) | stale on 2026-12-20
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
- tooling: The user installs and runs the software; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: Tailscale-shaped mesh with a FIPS data plane. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; the mesh is user-installed software on user-supplied machines, and exit access is an experimental byte-metered marketplace paid in Bitcoin through Cashu, so no free hosted egress allowance is published. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Tailscale-style private mesh VPN using Nostr identities and signed network rosters, with a FIPS-backed data plane. Supports MagicDNS, subnet routes and exit nod
  - [2] 2026-11-19: the first-party README describes exit nodes as an experimental, paid, byte-metered marketplace rather than a free allowance | capture: sha256:6e449b130e74d5400dcd10976a1b7081d42166590f13233b70e22dd3fa34072d | quote: It also includes an experimental marketplace for byte-metered public exit nodes paid in Bitcoin through Cashu.
  - [2] 2026-11-19: the first-party README presents user-installed software that needs no provider account | capture: sha256:6e449b130e74d5400dcd10976a1b7081d42166590f13233b70e22dd3fa34072d | quote: Connect people, servers, and agent hosts without an email, phone number, or VPN provider account.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:6e449b130e74d5400dcd10976a1b7081d42166590f13233b70e22dd3fa34072d | quote: It also includes an experimental marketplace for byte-metered public exit nodes paid in Bitcoin through Cashu.
  - [2] 2026-11-19: the first-party README presents user-installed software that needs no provider account | capture: sha256:6e449b130e74d5400dcd10976a1b7081d42166590f13233b70e22dd3fa34072d | quote: It also includes an experimental marketplace for byte-metered public exit nodes paid in Bitcoin through Cashu.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/mmalmi/nostr-vpn
