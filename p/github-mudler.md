# EdgeVPN

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-mudler/ | JSON https://fshy.ajam.dev/api/v1/entity/github-mudler.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EdgeVPN

- `egress/edgevpn` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.217Z (live) | stale on 2026-12-20
- url https://github.com/mudler/edgevpn
- price USD 0
- free tier: Fully decentralized, statically built P2P VPN on libp2p. No central server; peers discover each other via DHT. Supports file transfer and sharing TCP services between peers without a VPN interface. Apache 2.0 License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. libp2p P2P VPN over a DHT.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: libp2p P2P VPN over a DHT. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Fully decentralized, statically built P2P VPN on libp2p. No central server; peers discover each other via DHT. Supports file transfer and sharing TCP services b
  - [2] 2026-11-19: the project README describes a decentralized P2P VPN the user installs and runs with no central server; no hosted egress allowance is offered | capture: sha256:dc57ab5f3056a60005e29a583c1a835e1ea26af256cea6ba932255d672f551d3 | quote: Every token is unique and identifies the network, no central server setup, or specifying hosts ip is required.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/mudler/edgevpn
