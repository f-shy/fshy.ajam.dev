# Unikraft Cloud

> unikraft.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unikraft/ | JSON https://fshy.ajam.dev/api/v1/entity/unikraft.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unikraft Cloud

- `compute/unikraft-cloud` | paid-only | evidence reported | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:19.000Z (live) | stale on 2026-11-06
- url https://unikraft.com/pricing
- free tier: no free tier stated: capacity with millisecond cold boots where idle infrastructure is not billed | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - retention-clamped (binding): idle infrastructure is not billed; a millisecond cold boot is what makes that possible [1]
  - write-gated: the page refers to plans without pricing them in the extracted body [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: No free tier exists, so the verdict is paid-only.
- evidence note: the pricing page was read on 2026-10-22 and its extracted body carries the idle-billing promise and a plan reference, but no plan table or price, so the free-tier field keeps its earlier source
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: idle infrastructure is not billed, which makes the reap question moot; cold boots are milliseconds
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '## Never Pay for Idle Again' and '### You don't pay for idle infrastructure' with 'Millisecond cold boots = lower overhead' and 'Whether you're testing, scaling, or deploying enterprise workloads, we've got a plan that fits.', quoted
- sources:
  - [1] https://unikraft.com/pricing
