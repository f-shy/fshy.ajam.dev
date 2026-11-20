# Anywherelan

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-anywherelan/ | JSON https://fshy.ajam.dev/api/v1/entity/github-anywherelan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Anywherelan

- `egress/anywherelan` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.398Z (live) | stale on 2026-12-20
- url https://github.com/anywherelan/awl
- price USD 0
- free tier: Layer 3 peer-to-peer VPN. Fully mesh, with and an open-source . Built on the libp2p networking stack (QUIC, TCP). Has NAT traversal and relaying support. Its workflow and GUI are similar to , but for networking rather than file transfers. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. libp2p mesh with community coordination servers.
- interface detail: not established
- tooling: The user installs and runs the awl binary; no hosted endpoint is offered.
- reliability: the same as interface detail
- notes: libp2p mesh with community coordination servers. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it states the tool is a peer-to-peer mesh VPN with no coordination server, account or control plane and no hosted endpoint; no allowance is published. The list entry is superseded as the basis.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Layer 3 peer-to-peer VPN. Fully mesh, with and an open-source . Built on the libp2p networking stack (QUIC, TCP). Has NAT traversal and relaying support. Its wo
  - [2] 2026-11-19: the tool is a self-hosted peer-to-peer VPN with no hosted endpoint, account or control plane | capture: sha256:296bbb4b6ad6ca92f732979f49d7640dfc25da50dcd180f59ee7b8a1ed6d83a3 | quote: awl is fully decentralized: no coordination server, no account, no control plane. There is nothing to pay for, nothing to sign up for, nothing that can be shut down from the outside. Everything awl needs is in this repository, under an open-source license.
  - [2] 2026-11-19: all components are in the repository and are installed and run by the user | capture: sha256:296bbb4b6ad6ca92f732979f49d7640dfc25da50dcd180f59ee7b8a1ed6d83a3 | quote: Everything awl needs is in this repository, under an open-source license.
  - [2] 2026-11-19: the first-party README replaces the list sentence as the basis for the egress finding | capture: sha256:296bbb4b6ad6ca92f732979f49d7640dfc25da50dcd180f59ee7b8a1ed6d83a3 | quote: awl is fully decentralized: no coordination server, no account, no control plane. There is nothing to pay for, nothing to sign up for, nothing that can be shut down from the outside. Everything awl needs is in this repository, under an open-source license.
  - [2] 2026-11-19: the software is installed and run by the user and offers no hosted endpoint | capture: sha256:296bbb4b6ad6ca92f732979f49d7640dfc25da50dcd180f59ee7b8a1ed6d83a3 | quote: awl is fully decentralized: no coordination server, no account, no control plane. There is nothing to pay for, nothing to sign up for, nothing that can be shut down from the outside. Everything awl needs is in this repository, under an open-source license.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/anywherelan/awl
