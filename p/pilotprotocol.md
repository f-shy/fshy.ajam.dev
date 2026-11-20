# Pilot Protocol

> pilotprotocol.network | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pilotprotocol/ | JSON https://fshy.ajam.dev/api/v1/entity/pilotprotocol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pilot Protocol

- `egress/pilot-protocol` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category udp-level agent overlay software | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.144Z (live) | stale on 2026-12-20
- url https://pilotprotocol.network/
- price USD 0
- free tier: Pilot is a UDP-level networking stack for autonomous agents. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No hosted free byte allowance is published; the first-party site describes peer-to-peer tunnels with an encrypted relay fallback and a wallet payment layer.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'Every agent on Pilot can download a free wallet app'; trust is a per-peer handshake, not an account. | country: None
- interface: cli
- binding note: Software and protocol, not a service: there is no hosted public port, and the wallet layer suggests paid relays rather than a free allowance.
- interface detail: CLI and library
- tooling: Go library and CLI.
- composes with: Needs a host.
- reliability: Relay fallback depends on peers that accept the traffic.
- notes: UDP-native but not an ingress: peers find each other through STUN and relay.
- evidence note: The first-party site states the network is peer-to-peer with an encrypted relay fallback, private by default behind a trust handshake, and that the public backbone is run free of charge with self-hosting available; no hosted free byte allowance is published.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: none
  - volume_stated: No allowance is published; the network is peer-to-peer with relay fallback and a payment layer.
  - bytes_transit: overlay-only
  - transit_note: peer relays
- evidence:
  - [1] 2026-10-23: 'UDP-level networking stack for autonomous agents'; 'L3 / L4 - IP - UDP / TCP'; free wallet app
  - [1] 2026-11-19: the first-party site describes peer-to-peer tunnels with relay fallback and publishes no hosted free byte allowance | capture: sha256:2f592143685c89021aa0c857aaccc9bd3846e0d8c102876cd1a6f907c64c288a | quote: The daemon gets through NAT with STUN and hole punching, and falls back to an encrypted relay.
  - [1] 2026-11-19: the first-party site describes peer tunnels and relay fallback with no published free byte allowance | capture: sha256:2f592143685c89021aa0c857aaccc9bd3846e0d8c102876cd1a6f907c64c288a | quote: The daemon gets through NAT with STUN and hole punching, and falls back to an encrypted relay.
  - [1] 2026-11-19: the first-party site describes a free-to-use public backbone run by its operators with a self-hosting option | capture: sha256:2f592143685c89021aa0c857aaccc9bd3846e0d8c102876cd1a6f907c64c288a
  - [1] 2026-11-19: the first-party site gives install steps for a daemon and CLI the user runs | capture: sha256:2f592143685c89021aa0c857aaccc9bd3846e0d8c102876cd1a6f907c64c288a | quote: Install the daemon and `pilotctl` in one line.
  - [1] 2026-11-19: the first-party site describes the user-installed daemon and a peer-to-peer network with no hosted byte allowance | capture: sha256:2f592143685c89021aa0c857aaccc9bd3846e0d8c102876cd1a6f907c64c288a | quote: Install the daemon and `pilotctl` in one line.
- sources:
  - [1] https://pilotprotocol.network/
