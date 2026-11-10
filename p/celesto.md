# Celesto Cloud

> celesto.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/celesto/ | JSON https://fshy.ajam.dev/api/v1/entity/celesto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Celesto Cloud

- `compute/celesto` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:05.600Z (live) | stale on 2026-12-05
- url https://celesto.ai/pricing
- free tier: a one-time $5 runtime credit valid for 30 days on the Micro size, no card required; Micro is 1 shared vCPU, 2 GB and a 20 GB root disk at $0.015 an hour | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://celesto.ai/pricing prices running time and root disk only and states no egress allowance or overage price; outbound internet access can be turned off per computer | metered: no | source: [1]
- identity: email | detail: 'a one-time $5 runtime credit for 30 days, no card required', quoted from celesto.ai/pricing read 2026-10-22
- interface: cli, ssh
- limits:
  - request-rate: $5 of runtime credit, one time, on the Micro size [1]
  - retention-clamped (binding): the credit is valid for 30 days; a top-up does not end the trial, it just adds a balance [1]
- interface detail: the celesto CLI (including computer ssh), a Python SDK and a TypeScript SDK; no REST reference was read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the trial credit, its 30-day life and the size ladder. It is a trial, so the verdict stays trial-only and the clock is now recorded
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 2
  - shape.disk: 20
  - shape.note: Micro, the default; the ladder runs to XL at 8 vCPU, 32 GB and 100 GB. $5 buys 333 hours of Micro
  - session_cap.restart_required: no
  - session_cap.note: the 30-day clock is on the credit, not on a machine; a root disk is included in each size
  - free_tier_kind: trial
  - burst_x: 1.0
  - ps.gib: 20
  - ps.price: fixed root disk included in the size
  - ps.durability: root disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the machine exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Usage pricing is live. Try Micro with a one-time $5 runtime credit for 30 days, no card required.' and 'Sign up, then start the trial or add at least $2.01 in Settings -> Billing. A top-up does not end an active trial.' and the size table from Micro at $0.015 an hour to XL at $0.160 an hour, quoted
  - [1] 2026-11-03: the estimator prices running time only; no egress allowance or overage price is published | capture: sha256:eba826b8108319bfd4dc5b911bbf3e00d9757d145627433b910e1327bb46f3ce | quote: Running time only. Tax and any card issuer conversion fee are excluded.
  - [2] 2026-11-03: the celesto CLI opens an SSH session to a computer | capture: sha256:dbb5c022cb94640f5d9ab2ce02efa917b8cd506273a82d0f2f8d7f1433f291de | quote: celesto computer ssh einstein
- sources:
  - [1] https://celesto.ai/pricing
  - [2] https://celesto.ai/docs/cloud/cli.md
