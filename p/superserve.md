# Superserve

> superserve.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/superserve/ | JSON https://fshy.ajam.dev/api/v1/entity/superserve.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Superserve

- `compute/superserve` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:18.817Z (live) | stale on 2026-12-05
- url https://superserve.ai/pricing
- free tier: Free with $100 of credit, pay-as-you-go after it, up to 20 concurrent sandboxes and no time limit on a sandbox | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page lists compute, memory and retained-storage rates only and says estimates exclude network charges; no transfer allowance or per-GB price is stated | metered: no | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - request-rate (binding): up to 20 concurrent sandboxes on Free, 1,000 on the paid tier [1]
- interface detail: REST API, the `@superserve/cli` CLI and a TypeScript SDK; no SSH found in the docs read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The page states 'No time limit on sandboxes', which is the wall-clock axis, and 20 concurrent sandboxes is the bound
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 'No time limit on sandboxes', quoted; the page states no reap
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · Pay-as-you-go after credit · Up to 20 concurrent sandboxes · No time limit on sandboxes · Usage rates after credit', quoted
  - [1] 2026-11-03: network is charged outside the published rates and no price is stated | capture: sha256:efa4dda5c8cc1626e6bb870e9ef55e55115047e72d8fa63abaf6d334fa5d2b05 | quote: Estimates exclude taxes, network, and external model API charges.
  - [2] 2026-11-03: a CLI exists | capture: sha256:e6b411f14c086ffb7de76253222a35bf52084f9c3f228c31efb8ab3ebc928ca1 | quote: Create sandboxes, run commands, move files and publish ports from your terminal.
  - [2] 2026-11-03: a REST API reference exists | capture: sha256:e6b411f14c086ffb7de76253222a35bf52084f9c3f228c31efb8ab3ebc928ca1 | quote: Creates a sandbox from a template (defaults to `superserve/base` when `from_template` is omitted)
- sources:
  - [1] https://superserve.ai/pricing
  - [2] https://docs.superserve.ai/llms.txt
