# LanEmu/P2PVPN

> gitlab.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitlab-monsterovich/ | JSON https://fshy.ajam.dev/api/v1/entity/gitlab-monsterovich.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LanEmu/P2PVPN

- `egress/lanemu-p2pvpn` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.341Z (live) | stale on 2026-12-20
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
- evidence note: First-party GitLab project page read on 2026-11-19; it describes a server-less (decentralized) P2P VPN with no hosted endpoint or published byte allowance, so the list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: LanEmu is a 2023+ continuation of . It uses Bittorrent trackers for matchmaking/rendezvous, and then routes traffic in a peer-to-peer VLAN via OpenVPN's TAP dri
  - [2] 2026-11-19: the first-party project page describes a server-less P2P VPN with no hosted endpoint or byte allowance | capture: sha256:b765ed87c3295783dd2cfa857aa0e5109a216f635d21e65034d9af11f66e9fed | quote: Server-less (decentralized) Virtual Private Network (Open-source alternative to Hamachi, Radmin, ZeroTier, etc.)
  - [2] 2026-11-19: the first-party page replaces the list sentence as the basis for the egress finding | capture: sha256:b765ed87c3295783dd2cfa857aa0e5109a216f635d21e65034d9af11f66e9fed | quote: Server-less (decentralized) Virtual Private Network (Open-source alternative to Hamachi, Radmin, ZeroTier, etc.)
  - [2] 2026-11-19: the first-party page describes server-less software with no hosted endpoint | capture: sha256:b765ed87c3295783dd2cfa857aa0e5109a216f635d21e65034d9af11f66e9fed | quote: Server-less (decentralized) Virtual Private Network (Open-source alternative to Hamachi, Radmin, ZeroTier, etc.)
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://gitlab.com/Monsterovich/lanemu
