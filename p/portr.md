# portr

> portr.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/portr/ | JSON https://fshy.ajam.dev/api/v1/entity/portr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## portr

- `egress/portr` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category overlay network or advanced tunnel tool | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://portr.dev/
- price USD 0
- free tier: Has a JavaScript/Python admin page and request inspection/replay features. AGPL-3.0 License. Tunneling implemented in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published in the list entry.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. Tunnel HTTP, TCP and WebSocket connections.
- interface detail: not established
- tooling: vendor client
- composes with: Needs an account before any capacity is visible.
- reliability: the same as interface detail
- notes: Tunnel HTTP, TCP and WebSocket connections. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: A vendor page read would raise this to documented; only the aggregator was read for this name.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Has a JavaScript/Python admin page and request inspection/replay features. AGPL-3.0 License. Tunneling implemented in Go.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://portr.dev/
