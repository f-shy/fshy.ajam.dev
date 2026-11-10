# LanEmu/P2PVPN

> gitlab.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitlab-monsterovich/ | JSON https://fshy.ajam.dev/api/v1/entity/gitlab-monsterovich.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LanEmu/P2PVPN

- `egress/lanemu-p2pvpn` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://gitlab.com/Monsterovich/lanemu
- price USD 0
- free tier: LanEmu is a 2023+ continuation of . It uses Bittorrent trackers for matchmaking/rendezvous, and then routes traffic in a peer-to-peer VLAN via OpenVPN's TAP drivers; effectively a decentralized peer-to-peer mesh VPN. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. TAP-based P2P VLAN over BitTorrent trackers.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: TAP-based P2P VLAN over BitTorrent trackers. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: LanEmu is a 2023+ continuation of . It uses Bittorrent trackers for matchmaking/rendezvous, and then routes traffic in a peer-to-peer VLAN via OpenVPN's TAP dri
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://gitlab.com/Monsterovich/lanemu
