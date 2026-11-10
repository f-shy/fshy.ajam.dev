# Pilot Protocol

> pilotprotocol.network | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pilotprotocol/ | JSON https://fshy.ajam.dev/api/v1/entity/pilotprotocol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pilot Protocol

- `egress/pilot-protocol` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category udp-level agent overlay software | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://pilotprotocol.network/
- price USD 0
- free tier: Pilot is a UDP-level networking stack for autonomous agents. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published; the network is peer-to-peer with relay fallback and a payment layer.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'Every agent on Pilot can download a free wallet app'; trust is a per-peer handshake, not an account. | country: None
- interface: cli
- binding note: Software and protocol, not a service: there is no hosted public port, and the wallet layer suggests paid relays rather than a free allowance.
- interface detail: CLI and library
- tooling: Go library and CLI.
- composes with: Needs a host.
- reliability: Relay fallback depends on peers that accept the traffic.
- notes: UDP-native but not an ingress: peers find each other through STUN and relay.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: none
  - volume_stated: No allowance is published; the network is peer-to-peer with relay fallback and a payment layer.
  - bytes_transit: overlay-only
  - transit_note: peer relays
- evidence:
  - [1] 2026-10-23: 'UDP-level networking stack for autonomous agents'; 'L3 / L4 - IP - UDP / TCP'; free wallet app
- sources:
  - [1] https://pilotprotocol.network/
