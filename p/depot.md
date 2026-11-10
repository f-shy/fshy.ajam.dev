# Depot

> depot.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/depot/ | JSON https://fshy.ajam.dev/api/v1/entity/depot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Depot (GitHub Actions runners)

- `compute/depot` | trial-only | evidence documented | binding retention-clamped | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-10T02:22:59.305Z (live) | stale on 2026-12-11
- url https://depot.dev/pricing
- free tier: No free tier: a 7-day trial, then the Developer plan is USD 20 a month and includes 2,000 GitHub Actions minutes, 2,000 sandbox minutes, 500 container build minutes and 25 GB of cache and registry storage each month; additional GitHub Actions minutes are USD 0.006 a minute for the base 2 vCPU Linux runner. | unit: minutes | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: 2,000 GitHub Actions minutes a month on the USD 20 Developer plan, then USD 0.006 a minute for the base 2 vCPU Linux runner [1]
  - per-object-cap: 25 GB of cache and registry storage on the Developer plan, then USD 0.20 a GB-month [1]
  - retention-clamped (binding): the free window is a 7-day trial; the monthly allowance needs the USD 20 plan [1]
- limits note: the Startup plan at USD 200 a month raises the included GitHub Actions minutes to 20,000 and cache to 250 GB; the Business plan is custom and can run in the customer AWS account
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The 2,000 sandbox minutes and 2,000 GitHub Actions minutes are an allowance included in the USD 20 a month Developer plan, not a grant inside the 7-day trial; the trial is the only free window. The overage rate is USD 0.006 a minute for the base 2 vCPU Linux runner, and cache beyond 25 GB is USD 0.20 a GB-month.
- evidence note: The plan grid, the included allowances and the overage rates are read from the vendor own pricing page. Raise by running a job in the trial and reading the invoice line for a minute beyond the included block.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a 7-day clock on the trial, not on a job
  - free_tier_kind: trial
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 25
  - ps.price: included in the trial, then metered
  - ps.durability: cache and registry
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the trial term
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start for free, scale to any size, and pay per second for what you use' with an included block of '2,000 sandbox minutes', '2,000 GitHub Actions minutes', '500 container build minutes' and '25 GB cache and registry storage', under a 'START A 7-DAY TRIAL' button, quoted
  - [1] 2026-11-10: the Developer plan includes 2,000 GitHub Actions minutes a month | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: 2,000 GitHub Actions minutes
  - [1] 2026-11-10: additional GitHub Actions minutes are USD 0.006 a minute | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: $0.006 / minute
  - [1] 2026-11-10: the Startup plan includes 20,000 GitHub Actions minutes | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: 20,000 GitHub Actions minutes
  - [1] 2026-11-10: a 7-day trial is the only free window | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: START A 7-DAY TRIAL
- sources:
  - [1] https://depot.dev/pricing
