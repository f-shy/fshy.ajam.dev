# OpenPond Cloud Sandboxes

> openpond.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openpond/ | JSON https://fshy.ajam.dev/api/v1/entity/openpond.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenPond Cloud Sandboxes

- `compute/openpond` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:14.183Z (live) | stale on 2026-12-05
- url https://openpond.ai/pricing
- free tier: a Free tier with limited monthly hosted usage, and credits addable at any time without a subscription; $10 a month buys 10 concurrent cloud sandboxes | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page meters sandbox compute per second and durable storage per GiB-month and states no egress allowance or price | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): limited monthly hosted usage on Free; 10 concurrent cloud sandboxes on the $10 tier [1]
  - write-gated: credits can be added at any time with no subscription, so the free tier's ceiling is a balance rather than a plan [1]
- interface detail: CLI (npx openpond), desktop app, web, TUI and Slack or Microsoft Teams; no sandbox REST reference read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states a free tier with limited monthly hosted usage and credit top-ups without a subscription. The free tier's amount is stated only as 'limited', so no figure is invented
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: hosted usage is metered monthly; the page states no session clock
  - free_tier_kind: allowance
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free. Upgrade for more projects, team access, and concurrent cloud sandboxes. Add credits whenever you need more hosted usage.' with 'Limited monthly usage included' on Free and '$10 in monthly hosted usage' plus 'Up to 10 concurrent cloud sandboxes' on the next tier, quoted
  - [1] 2026-11-03: the sandbox meter is compute time; no egress meter is listed | capture: sha256:a7a6893d401369a60f1efe27f1ff001ffec9fe277368749e7f87c9eefa50f002 | quote: Sandbox compute
  - [2] 2026-11-03: a CLI exists | capture: sha256:99d464ae11fe3790007884d54d1b778ec7cd0f989c1cf3eaa7382afa51a73f89 | quote: - [OpenPond CLI](https://openpond.ai/products/cli): Run `npx openpond@latest` to start from the terminal.
- sources:
  - [1] https://openpond.ai/pricing
  - [2] https://openpond.ai
