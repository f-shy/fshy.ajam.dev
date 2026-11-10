# Revyl

> revyl.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/revyl/ | JSON https://fshy.ajam.dev/api/v1/entity/revyl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Revyl

- `compute/revyl` | qualifies-with-caveat | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:49.113Z (live) | stale on 2026-11-22
- url https://www.revyl.com
- free tier: a free start on a mobile test-automation service that runs iOS devices in the cloud; no plan or credit is priced on the page | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: runs execute against real iOS devices; the page states no quota [1]
  - write-gated (binding): the free path is a signup; the paid ladder is not rendered on this page [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and offers a free signup with device runs, but the plan table is not in the extracted body. The product is device time rather than a general machine
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: a cloud iOS device
  - shape.note: an iPhone 15 on iOS 17.4 in the page's example
  - session_cap.restart_required: no
  - session_cap.note: a run is a scripted flow against a device, not a machine held open
  - free_tier_kind: allowance
  - ps.price: run state is committed to Atlas and replayable
  - ps.durability: recorded run and device state
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the run record
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Give your coding agent an iPhone.' with '`revyl run checkout-flow --device ios`' and a recorded run showing device, streaming and state committed, plus 'Start free', quoted; no plan or price is rendered
- sources:
  - [1] https://www.revyl.com
