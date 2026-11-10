# Shuttle

> shuttle.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shuttle/ | JSON https://fshy.ajam.dev/api/v1/entity/shuttle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shuttle

- `compute/shuttle` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:01.471Z (live) | stale on 2026-11-22
- url https://www.shuttle.dev
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan and no price are published; deployment is driven by a CLI against the vendor's AWS infrastructure [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22. It is a Rust deployment platform on AWS with no published plan or price, which confirms paid-only and explains it: the free path is the toolchain
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an app is deployed as a service; the page states no clock
  - free_tier_kind: none
  - reclassified_from: dead
  - ps.price: resources are declared as annotations on the code
  - ps.durability: managed AWS resources
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the app is deployed
  - net.out: yes
  - net.in: yes
  - net.ports: HTTPS
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Your code is packaged and sent to Shuttle where it is compiled and deployed' with 'Shuttle provisions and configures the resources you need' and 'build complex and scalable apps on industry-standard AWS products', quoted; no plan and no price
- sources:
  - [1] https://www.shuttle.dev
