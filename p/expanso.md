# Expanso

> expanso.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/expanso/ | JSON https://fshy.ajam.dev/api/v1/entity/expanso.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Expanso

- `compute/expanso` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.expanso.io/
- free tier: Bacalhau-derived pipelines that 'run on your own nodes, where the data is created', positioned for enterprise data control and edge AI inference, with a hosted console at cloud.expanso.io. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The product assumes nodes the customer operates, and the analysis assumes no local hardware, so the first failure is the premise rather than a price. [1]
- limits note: The product assumes nodes the customer operates, and the analysis assumes no local hardware, so the first failure is the premise rather than a price.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Only with a rented node: the agent could run on a paid VM, which turns a zero-cost edge product into a paid-VM product.
- reliability: no reliability event recorded
- notes: Bacalhau, the open-source compute-over-data project this descends from, allowed free job submission to public nodes; that route was not checked and may still exist. A rented small VM plus the open-source agent is the only composition that needs no owned hardware.
- self hosted: yes
- extras:
  - facets.class: paid-cloud
- evidence:
  - [1] 2026-10-22: 'Expanso runs pipelines on your own nodes, where the data is created'; calls to action are a login and a demo booking, with no published plan
  - [1] 2026-10-22: workloads named are AI inference, threat detection and log processing, all at the edge
- sources:
  - [1] https://www.expanso.io/
