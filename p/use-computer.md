# use.computer

> use.computer | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/use-computer/ | JSON https://fshy.ajam.dev/api/v1/entity/use-computer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## use.computer

- `compute/use-computer` | paid-only | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:16.040Z (live) | stale on 2026-11-22
- url https://use.computer/
- free tier: no free tier: Apple Silicon Mac minis at $0.90 an hour for an M4, $1.40 for an M4 Pro and $1.75 for an M5 Pro, with warm boots under a second | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.90 an hour for an M4, $1.40 for an M4 Pro and $1.75 for an M5 Pro [1]
  - retention-clamped: a snapshot of the disk state lets fresh clones start from the same point, so state is kept as an image rather than a paused machine [1]
  - per-object-cap: two VMs per Mac, with warm boots under a second [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the hourly rates and the snapshot-and-clone behaviour. There is no free tier, so the record's USD 100 credit is not established and the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.gpu_class: Apple M4
  - shape.gpu_count: 1
  - shape.note: a real Mac mini with two VMs per Mac; M4, M4 Pro and M5 Pro are priced
  - session_cap.restart_required: no
  - session_cap.note: warm boot under a second; the state answer is the snapshot-and-clone path rather than a paused VM
  - free_tier_kind: none
  - granularity.min_billed_s: 86400
  - ps.price: disk state is snapshotted and cloned
  - ps.durability: snapshot of the disk state
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the snapshot
  - net.out: yes
  - net.in: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Real Apple Silicon Mac minis · 2 VMs per Mac · <1s warm boot · M4 $0.90/hr · M4 Pro $1.40/hr · M5 Pro $1.75/hr' with 'Seed a macOS sandbox once: install your tools, sign in, open your apps. Snapshot the disk state, then spin up fresh clones from that exact state', quoted
- sources:
  - [1] https://use.computer/
