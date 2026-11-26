# inlets

> inlets.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inlets/ | JSON https://fshy.ajam.dev/api/v1/entity/inlets.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## inlets

- `egress/inlets` | paid-only | evidence reported | binding none | category tunnel service (hosted) | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://inlets.dev/
- price USD 0
- free tier: Used to be ; now focused on a polished commercial offering. Designed to work well with Kubernetes. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published in the list entry.; ingress: tcp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. Commercial tunnel for Kubernetes.
- interface detail: not established
- tooling: vendor client
- composes with: Needs an account before any capacity is visible.
- reliability: the same as interface detail
- notes: The aggregator says the project moved from open source to a commercial offering. Commercial tunnel for Kubernetes. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: The aggregator says the project moved from open source to a commercial offering. A vendor page read would raise this to documented; only the aggregator was read for this name.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Used to be ; now focused on a polished commercial offering. Designed to work well with Kubernetes.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://inlets.dev/
