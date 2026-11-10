# LangSmith Sandboxes

> langchain.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/langchain/ | JSON https://fshy.ajam.dev/api/v1/entity/langchain.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LangSmith Sandboxes

- `compute/langsmith-sandbox` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:14.175Z (live) | stale on 2026-12-05
- url https://www.langchain.com/pricing
- free tier: one free seat and one free Serverless (Small) deployment; runtime compute bills at 0.0675 LSU a vCPU-hour beyond it | unit: objects | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: no egress allowance or overage price on the pricing page or the sandboxes docs page; non-Enterprise organizations get restricted egress to a managed allowlist by default | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): 1 free seat and 1 free Serverless (Small) deployment [1]
  - request-rate (binding): runtime compute bills at 0.0675 LSU a vCPU-hour [1]
  - per-object-cap: trace ingestion and trace event limits apply per plan and are documented separately [1]
- interface detail: Python and TypeScript SDK, and a Sandbox CLI (build snapshots, manage sandboxes, open consoles, tunnel TCP ports); no REST reference read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The free tier unit is deployment count rather than execution hours.
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: Use Serverless for background or latency-tolerant agents it scales to zer
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: one serverless deployment; the page states no session clock
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$0 / seat per month' with 'Maximum of 1 seat (free)' and '1 free Serverless (Small) deployment included' plus 'Runtime Compute · 0.0675 LSU / vCPU-hr', quoted
  - [2] 2026-11-03: egress is restricted by default and no volume allowance or price is stated | capture: sha256:8b6d0d079d965490b9ffe333f33b974bc5cc468e6c3bd15da49f10d5ae98d25e | quote: Restricted egress applies to non-Enterprise organizations by default and to organizations that request it.
  - [2] 2026-11-03: an SDK exists; the CLI card beside it covers the command line | capture: sha256:8b6d0d079d965490b9ffe333f33b974bc5cc468e6c3bd15da49f10d5ae98d25e | quote: Create and manage sandboxes programmatically with the Python or TypeScript SDK.
- sources:
  - [1] https://www.langchain.com/pricing
  - [2] https://docs.langchain.com/langsmith/sandboxes

## langsmith datasets/traces as storage

- `storage/langsmith-datasets-traces-as-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.langchain.com/pricing
- free tier: none reachable: Free Developer plan is 5,000 base traces/month with 14-day base-trace retention, 1 seat, 1 workspace. Storage is billed as traces, not bytes, and the retention window is shorter than any… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Free Developer plan is 5,000 base traces/month with 14-day base-trace retention, 1 seat, 1 workspace. Storage is billed as traces, not bytes, and the retention window is shorter than any…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free Developer plan is 5,000 base traces/month with 14-day base-trace retention, 1 seat, 1 workspace. Storage is billed as traces, not bytes, and the retention window is shorter than any…
  - [2] 2026-10-21: cited as the basis of the rejection: Free Developer plan is 5,000 base traces/month with 14-day base-trace retention, 1 seat, 1 workspace. Storage is billed as traces, not bytes, and the retention window is shorter than any arc
- sources:
  - [1] https://www.langchain.com/pricing
  - [2] https://docs.langchain.com/langsmith/usage-and-billing
