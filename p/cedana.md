# Cedana

> cedana.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cedana/ | JSON https://fshy.ajam.dev/api/v1/entity/cedana.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cedana

- `compute/cedana` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category other (checkpoint/restore software; not a compute provider)
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:29.860Z (live) | stale on 2026-11-22
- url https://cedana.com/
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no self-serve plan and no hosted compute: the product moves the user's own GPU jobs between the user's own nodes. [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22. It sells checkpoint-and-migrate software for GPUs already in place, so there is no hosted capacity and no free tier to have
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the point of the product is that a job survives a stop: state, including KV cache, is checkpointed and resumed elsewhere
  - persistent_storage.price: a user's own storage
  - persistent_storage.durability: process and GPU memory checkpoint
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: the checkpoint
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Cedana checkpoints the entire running process (GPU memory and CUDA state, including KV cache and in-flight sessions) and resumes it on another node' and 'Native support for SLURM and Kubernetes', quoted; no plan and no price
- sources:
  - [1] https://cedana.com/
