# Veertu Anka Build Cloud

> veertu.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/veertu/ | JSON https://fshy.ajam.dev/api/v1/entity/veertu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Veertu Anka Build Cloud

- `compute/anka-build-cloud` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:09.739Z (live) | stale on 2026-11-22
- url https://docs.veertu.com/anka/licensing/
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: the trial licence is 30 days; a commercial licence is a yearly subscription priced per host and host model, not per core [1]
  - write-gated (binding): a licence key must be activated against Veertu's licensing server, which the host must reach over the internet [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the licensing page was read on 2026-10-22 and states a 30-day trial licence and a host-count licence model. There is no free tier beyond the trial, which confirms paid-only
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon host
  - shape.note: licensing is per host and host model; the VM runs on Apple hardware a user owns
  - session_cap.restart_required: no
  - session_cap.note: the 30-day clock is on the licence, not on a VM; a VM's own lifetime is unbounded
  - free_tier_kind: trial
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Trial licenses for Anka products is valid for 30 days from the date of trial registration' and 'Anka Licensing for Apple Silicon machines is determined based on host count and host model and not on CPU core count', quoted
- sources:
  - [1] https://docs.veertu.com/anka/licensing/
