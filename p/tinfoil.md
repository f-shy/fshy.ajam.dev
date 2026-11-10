# Tinfoil

> tinfoil.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tinfoil/ | JSON https://fshy.ajam.dev/api/v1/entity/tinfoil.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tinfoil

- `compute/tinfoil` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:14.889Z (live) | stale on 2026-11-22
- url https://tinfoil.sh
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan and no price appear in the extracted body; capacity is the vendor's own multi-GPU infrastructure [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes verifiably private inference on the vendor's own multi-GPU hardware, with no plan or price. That confirms paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an inference API answers tokens; there is no machine to hold
  - free_tier_kind: none
  - granularity.min_billed_s: 3600
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Featured in a Llama case study as the only multi-GPU infrastructure offering production-ready, verifiably private AI' with a 'Supported hardware' section; no plan and no price in the extracted body
- sources:
  - [1] https://tinfoil.sh
