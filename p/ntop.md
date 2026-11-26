# n2n

> ntop.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ntop/ | JSON https://fshy.ajam.dev/api/v1/entity/ntop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## n2n

- `egress/n2n` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category overlay network or advanced tunnel tool | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:03.342Z (live) | stale on 2026-12-20
- url https://www.ntop.org/products/n2n/
- price USD 0
- free tier: Built on nodes and supernodes. GPL-3.0 license. Written in C. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published in the list entry.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. Layer 2 overlay.
- interface detail: not established
- tooling: vendor client
- composes with: Needs an account before any capacity is visible.
- reliability: The former vendor product page at www.ntop.org/products/n2n/ answered HTTP 404 on 2026-11-19; the first-party GitHub repository documents a user-run supernode.
- notes: Layer 2 overlay. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party GitHub repository read on 2026-11-19; n2n needs a supernode the user runs on a public server and offers no hosted egress allowance. The former vendor page at www.ntop.org/products/n2n/ was unreachable on 2026-11-19; see the measured reliability note.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Built on nodes and supernodes. GPL-3.0 license. Written in C.
  - [3] 2026-11-19: the first-party README says the supernode runs on a server the user supplies, with no hosted egress allowance published | capture: sha256:7f6f936ba12e795c81274f0548419685870808af78f3974ead641a4f9a51111a | quote: You can create your own infrastructure by setting up a supernode on a public server (e.g. a VPS).
  - [3] 2026-11-19: the first-party repository replaces the list sentence as the basis for the egress finding | capture: sha256:7f6f936ba12e795c81274f0548419685870808af78f3974ead641a4f9a51111a | quote: You can create your own infrastructure by setting up a supernode on a public server (e.g. a VPS).
  - probe:https://www.ntop.org/products/n2n/ 2026-11-19: the vendor product page answered HTTP 404 on 2026-11-19 | capture: sha256:92e713170fe2326e2771f0e43497126cbcf0ebeea6dfa9506f21ba75dbefcaeb | quote: "status": 404
  - [3] 2026-11-19: the first-party repository describes a user-run supernode with no hosted egress | capture: sha256:7f6f936ba12e795c81274f0548419685870808af78f3974ead641a4f9a51111a | quote: You can create your own infrastructure by setting up a supernode on a public server (e.g. a VPS).
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://www.ntop.org/products/n2n/
  - [3] https://github.com/ntop/n2n
