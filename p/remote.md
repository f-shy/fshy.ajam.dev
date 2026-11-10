# Remote.It

> remote.it | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/remote/ | JSON https://fshy.ajam.dev/api/v1/entity/remote.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Remote.It

- `egress/remote-it` | fails-egress | evidence documented | binding write-gated | category overlay (device network, not a public relay) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://docs.remote.it/features/services/udp
- price USD 0
- free tier: Every plan includes 5 base devices per account | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: no byte quota is published for the free tier; the metered resource is devices, five of them; ingress: none | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account with devices registered to it; the free tier is five devices | country: None
- interface: cli
- limits:
  - write-gated (binding): the peer must run the remote.it agent and be granted access; there is no anonymous public port [2]
- binding note: No quantity binds because the address is not public: the access grant is the gate, and a WireGuard peer that is not a remote.it device cannot reach the service at all.
- interface detail: the remoteit agent registers services; access is through the client's local proxy address
- tooling: remoteit and connectd packages, desktop and mobile clients
- composes with: composes with a fleet of devices you control; does not compose with an arbitrary WireGuard peer
- reliability: connections depend on the vendor's connection broker and on the client agent running on the peer
- notes: Zero-trust remote access platform. Connects client devices via authenticated peer-to-peer tunnels; does not provide open public Layer 4 ingress.
- evidence note: Raise by registering a UDP service and attempting a datagram from a host that is not enrolled in the account, which the documentation says cannot work.
- extras:
  - wg_path: none
  - wg_detail: UDP services exist but are reached through a user's own local proxy, not a public address: 'we provide a local device or proxy address and port where all traffic will be routed to the target device and port'. A peer must run the agent and authenticate.
  - ingress: none
  - volume_stated: no byte quota is published for the free tier; the metered resource is devices, five of them
  - bytes_transit: overlay-only
  - transit_note: traffic is proxied between enrolled devices, not published on a public port
- evidence:
  - [2] 2026-10-23: 'Create a Remote.It UDP service on any port you need', with no default UDP port
  - [3] 2026-10-23: 'we provide a local device or proxy address and port where all traffic will be routed to the target device and port'
  - [1] 2026-10-23: 'Every plan includes 5 base devices per account'
- sources:
  - [1] https://remote.it/pricing/
  - [2] https://docs.remote.it/features/services/udp
  - [3] https://docs.remote.it/introduction/get-started
