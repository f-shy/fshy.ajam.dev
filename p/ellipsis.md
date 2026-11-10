# Ellipsis

> ellipsis.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ellipsis/ | JSON https://fshy.ajam.dev/api/v1/entity/ellipsis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ellipsis

- `compute/ellipsis` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T15:51:59.408Z (live) | stale on 2026-12-05
- url https://www.ellipsis.dev/pricing
- free tier: no per-seat fee for the platform; the compute bills to the user's own AWS account at $0.142 a vCPU-hour and $0.024 a GB-hour. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: email: the dashboard signs in with GitHub ('Continue with GitHub'), and the account behind that sign-in is identified by an email address, which its alerts go to. A payment method is required to run anything: the platform sells prepaid credits, and 'A saved payment method alone does not enable automatic recharge.' No phone or identity document is named.
- interface: cli
- limits:
  - request-rate (binding): $0.142 a vCPU-hour and $0.024 a GB-hour, billed by AWS into the user's own account. [1]
  - per-object-cap: support packages run from $5,000 to $15,000 a month and are optional [1]
- interface detail: a CLI; also GitHub, Slack and Linear integrations; a REST API is not named on the docs index
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The platform is free while compute is billed separately.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: one persistent agent per PR, issue or thread; the page states no clock, and AWS bills the compute
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: billed by AWS
  - ps.durability: a user's own AWS account
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: as long as a user keeps it
  - net.out: yes
  - net.in: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Per-seat fees: $0' with 'CPU $0.142 / vCPU-hour - billed by AWS' and 'Memory $0.024 / GB-hour - billed by AWS' and 'Durable conversations. One persistent agent per PR, issue, or thread', quoted
  - [2] 2026-11-03: a CLI starts agent sessions | capture: sha256:13f1d552ed3eeb61fe3edf2e0f03f430155c460b331cb2f6be91f06205a85ccc | quote: Quick start Install the CLI and start an agent session
  - [3] 2026-11-04: the only sign-in offered is a GitHub account, so the identity is an email account behind GitHub | capture: sha256:aa0d3235ce6e6c13a579164276fcba55e4c7f124821f1946a94b7fa39eb13269 | quote: Continue with GitHub
  - [4] 2026-11-04: nothing runs without a prepaid balance | capture: sha256:ac5b24db7f345ddaa564e33112e1090919799d1f2780ab32efef857c69e06e6e | quote: Ellipsis uses prepaid credits. Model usage and compute are paid from your balance.
  - [4] 2026-11-04: a payment method is what a paying account holds, and buying credits needs one | capture: sha256:ac5b24db7f345ddaa564e33112e1090919799d1f2780ab32efef857c69e06e6e | quote: A saved payment method alone does not enable automatic recharge.
- sources:
  - [1] https://www.ellipsis.dev/pricing
  - [2] https://docs.ellipsis.dev
  - [3] https://app.ellipsis.dev/login
  - [4] https://www.ellipsis.dev/docs/pricing
