# Zo Computer

> zo.computer | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zo/ | JSON https://fshy.ajam.dev/api/v1/entity/zo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zo Computer

- `compute/zo-computer` | trial-only | evidence documented | binding retention-clamped | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:18.390Z (live) | stale on 2026-12-05
- url https://www.zo.computer/pricing
- free tier: a 14-day free trial with limited usage and 100 GB of cloud storage, holding 1 unit; after the trial the account drops to recovery only, and paid plans from $10 keep Zo awake with memory across sessions | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.zo.computer/pricing lists disk, CPU, memory, services and domains per plan and no egress allowance or overage price | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - retention-clamped (binding): the trial runs 14 days and then the account is recovery only; a paid plan is what keeps Zo awake [1]
  - per-object-cap: 100 GB of cloud storage on the free trial, with 1 unit held [1]
  - request-rate: usage is limited during the trial; paid plans add monthly AI credits [1]
- interface detail: public API and a tool reference, a desktop app, and the agent chat in the browser; no SSH or CLI stated on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the 14-day trial, what it holds, and that the account becomes recovery-only afterwards. The state answer is explicit: the trial is not a pause
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 8
  - shape.note: the $10 paid plan is 2 vCPU and 8 GB; $40 is 4 vCPU and 16 GB; the trial's shape is not stated
  - session_cap.restart_required: no
  - session_cap.note: the trial is 14 days and ends in recovery-only rather than a pause; a paid plan keeps the workspace awake and gives it memory across sessions
  - free_tier_kind: trial
  - granularity.min_billed_s: 0
  - ps.gib: 100
  - ps.price: 100 GB of cloud storage included on the trial
  - ps.durability: workspace files, Sites and Services
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: recovery only after 14 days
  - net.out: yes
  - net.in: yes
  - net.ports: Sites and Services
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free Trial is useful for light work; paid plans keep Zo awake, give it memory across sessions, and include monthly AI credits.' with 'Limited usage during 14-day trial', '14-day trial; then recovery only', '1 during trial', and the paid shapes '2 vCPUs, 8GB RAM' at $10 a month and '4 vCPUs, 16GB RAM' at $40, quoted
  - [1] 2026-11-03: the pricing table lists disk and no egress or bandwidth row | capture: sha256:1558460e282aee6e6d62fd5b89d8585aa442fa2172b1b6bcad79566dcddcac99 | quote: | Disk storage | 100GB disk | 100GB disk | 100GB disk | 100GB disk |
  - [2] 2026-11-03: a public API exists | capture: sha256:46fd0afa5c36f7f91f4dafcee6f1c248e65020cec70839ada1f6d87c600fe570 | quote: Exact details for Zo's tools and public API.
- sources:
  - [1] https://www.zo.computer/pricing
  - [2] https://www.zo.computer/reference
