# gost

> gost.run | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gost/ | JSON https://fshy.ajam.dev/api/v1/entity/gost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gost

- `egress/gost` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category overlay network or advanced tunnel tool | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:02.568Z (live) | stale on 2026-12-20
- url https://latest.gost.run/en/
- price USD 0
- free tier: Looks like a comprehensive option. TCP and UDP tunneling. TAP/TUN devices. Load balancing. Web API. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published in the list entry.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. TCP/UDP forwarding.
- interface detail: not established
- tooling: vendor client
- composes with: Needs an account before any capacity is visible.
- reliability: the same as interface detail
- notes: TCP/UDP forwarding. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: A vendor page read would raise this to documented; only the aggregator was read for this name.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Looks like a comprehensive option. TCP and UDP tunneling. TAP/TUN devices. Load balancing. Web API. Written in Go.
  - [2] 2026-11-19: the vendor page gives only source and binary install steps for a user-run tunnel; no hosted egress allowance is published | capture: sha256:765683d7df0a5eb62b80142245666ddfd2ac9fe133261a79e9ffaeeee443d2b1 | quote: git clone https://github.com/go-gost/gost.git
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://latest.gost.run/en/
