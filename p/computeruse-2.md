# ComputerUse.space

> computeruse.space | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/computeruse-2/ | JSON https://fshy.ajam.dev/api/v1/entity/computeruse-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ComputerUse.space

- `compute/computeruse-space` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:40.243Z (live) | stale on 2026-11-22
- url https://computeruse.space/
- free tier: no free tier: desktop time is sold in 30-day blocks from $24.99, and stopping an agent does not delete its files | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $24.99 per 30 days for 8 GB of RAM and 80 GB of storage; $39.99 for 16 GB and 150 GB [1]
  - per-object-cap: the 30-day block is a prepaid rental; renewal draws from prepaid credit [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing section was read on 2026-10-22 and prices 30-day blocks rather than free hours. The record's free-tier claim is contradicted, so the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.ram: 8
  - shape.disk: 80
  - shape.note: 8 GB RAM and 80 GB of customer storage; the larger block is 16 GB and 150 GB
  - session_cap.restart_required: no
  - session_cap.note: the unit is a 30-day rental; stopping an agent keeps its files
  - free_tier_kind: none
  - ps.gib: 80
  - ps.price: bundled in the 30-day block
  - ps.durability: the page separates what stays on disk from what ends with a process, and says a workspace reset must remove it before another customer gets the computer
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$24.99 / 30 days' for 8 GB of RAM and 80 GB of storage, '$39.99 / 30 days' for 16 GB and 150 GB, 'Automatically renews from prepaid credit', and 'Does stopping an agent delete its files? No.', quoted
- sources:
  - [1] https://computeruse.space/
