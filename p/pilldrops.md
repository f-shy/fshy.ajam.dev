# PillDrops

> pilldrops.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pilldrops/ | JSON https://fshy.ajam.dev/api/v1/entity/pilldrops.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PillDrops

- `compute/pilldrops` | qualifies-with-caveat | evidence documented | binding retention-clamped | category microVM (KVM) sandbox with a persistent workstation | tier Personal
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:53.357Z (live) | stale on 2026-12-26
- url https://pilldrops.com/pricing
- price parsed USD 122.39/mo
- free tier: Start free with $5 of usage credit and no card; the Free tier is 5 concurrent sandboxes, a 4 h maximum session, 2 vCPU / 2 GB RAM / 2 GB disk, all templates and SDKs, no persistent workstation | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit, not hours: USD 5 of usage at the published per-second rates
- per-object cap: not applicable: the unit is a machine, not an object; the billed shape is 2 vCPU / 4 GB / 10 GB on Personal
- retention: unknown: Personal and Pro each include '1 persistent workstation', and a paused sandbox bills storage only at USD 0.15 per GB-month, but no page read states how long a paused workstation survives before deletion | source: [1]
- egress: Not published. The pricing page lists three meters only - vCPU-seconds, GB-seconds of RAM, and GB-months of storage - and states no traffic allowance or per-GB rate. The plans are 'bring-your-own-key' and sell the machine, not model usage. | metered: no | source: [1]
- identity: email | detail: Start free with a $5 usage credit and no card. Account creation collects an email address and, depending on the sign-in method, a name and profile identifier; no phone number or identity document is asked for. Card types and any authorisation hold for paid plans are not stated on the pages read.
- interface: rest, cli
- limits:
  - retention-clamped (binding): 30 active hours a month on Personal (100 on Pro), a 4 h maximum session on the free tier and 24 h on Pro [1]
  - volume-quota: USD 5 of usage credit on the free tier, no card [1]
- limits note: The 30-hour monthly allowance is wall-clock, not a byte quota, and it is the number that decides the plan: 30 hours is 4% of a month. Storage is billed separately at USD 0.15 per GB-month even while the workstation is paused.
- binding note: The plan's 30 active hours and the 4 h (free) / 24 h (Pro) session cap clamp runtime before any byte quota could; beyond the allowance the meter runs at USD 0.1656 an hour, which is USD 120.89 for a month.
- interface detail: An HTTP API with Python and JS SDKs, a CLI and an MCP server; preview URLs proxy a sandbox port. A free Apache 2.0 self-host server exists as the last resort, installed and run by the user on a Linux machine.
- tooling: The hosted plan uses the vendor's SDK, CLI and MCP with an API key. The free Apache 2.0 self-host server is the last resort; the user installs and runs it on a rented or free Linux machine.
- composes with: The hosted USD 3 Personal plan buys 30 active hours a month of a 2 vCPU / 4 GB machine, with USD 5 of credit on the free tier; a paused sandbox bills USD 0.15 per GB-month of storage. The free Apache 2.0 self-host server is the last resort.
- reliability: Every plan is bring-your-own-model-key, so the machine outlives a provider rate limit but the agent stops when the key's quota does; no suspension or data-loss event was observed.
- notes: Arithmetic at 24/7 on the Personal shape: vCPU 2 × 0.0000140 × 3600 = USD 0.1008 an hour; RAM 4 × 0.0000045 × 3600 = USD 0.0648 an hour; together USD 0.1656 an hour × 730 = USD 120.888; plus storage 10 GB × USD 0.15 = USD 1.50, so USD 122.39 a month. At 300 hours it is USD 49.68 + 1.50 = USD 51.18. The USD 3 plan is therefore a bundle of 30 hours, and the page's own 'rule of thumb' (USD 0.13 an hour for a 2 vCPU / 2 GB sandbox) matches the meters. Region, hosting and the maximum session length on Personal (only free 4 h and Pro 24 h are stated) are unverified.
- evidence note: Prices, meters, plan allowances and the no-card claim are all from the vendor's pricing page read. The 24/7 figure is arithmetic on those published meters, not a quoted total: it is what the same shape costs if run continuously outside the allowance. What would raise it: a probe that runs a sandbox for an hour and reads the billed amount.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 10
  - billing_model: hourly
  - term: monthly plan allowances plus per-second metering
  - m10h_usd: 51.18
  - m24h_usd: 122.39
  - price_arithmetic: (2 × 0.0000140 + 4 × 0.0000045) × 3600 = USD 0.1656/hr; × 730 h = USD 120.888; + 10 GB × USD 0.15 storage = USD 1.50; total USD 122.39. × 300 h = USD 49.68 + 1.50 = USD 51.18.
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.ports: not documented on the page read
  - session_cap.wall_clock_min: 240
  - session_cap.restart_required: no
  - session_cap.note: 4 h max session on free, 24 h on Pro; checkpoints preserve filesystem state
  - aggregator_note: sandboxprices.com carries PillDrops in the picker with no modelled total and ranks it nowhere; its own note says paid-plan availability and sandbox limits conflict, which the vendor page read resolves: plans are on sale at USD 3 and USD 12.
- evidence:
  - [1] 2026-10-24: quoted: 'Personal $3/mo - 1 persistent workstation, 30 active hours / month, 2 vCPU · 4 GB RAM · 10 GB disk, 6 concurrent sandboxes'
  - [2] 2026-10-24: quoted: 'Compute is metered per second: $0.0000140 per vCPU-second and $0.0000045 per GB of RAM-second, plus $0.15/GB-month storage', and '$5 in free credits. No card.'
  - [1] 2026-11-25: the Free tier starts with a USD 5 usage credit and no card, and a paid plan adds a persistent workstation | capture: sha256:d1a7d1522b12c2440f96a2aed5398ce974aad1385b9f624454b028d39236c383 | quote: Start free with a $5 usage credit and no card — a paid plan adds a workstation that persists between sessions.
  - [1] 2026-11-24: the free tier is USD 5 of credit with no card and a paused sandbox bills storage only | capture: sha256:d1a7d1522b12c2440f96a2aed5398ce974aad1385b9f624454b028d39236c383 | quote: Compute is metered per second with no rounding: you pay for the exact vCPU-seconds and GB-seconds a sandbox uses, and a paused sandbox bills storage only. Every run's exact cost appears in your history. Start free with a $5 usage credit and no card — a paid plan adds a workstation that persists between sessions.
  - [3] 2026-11-24: account creation needs an email address and no phone or document is named | capture: sha256:a4a2b03182a05a40415d0d7905f9d636f2119c5395a4896e942d155b4a5b8b71 | quote: When you create an account we collect your email address and, depending on your sign-in method, your name and profile identifier from our authentication provider.
  - [4] 2026-11-24: the hosted offer has an HTTP API with SDKs and a CLI | capture: sha256:7e991a1207ffc65a93431d13494547583373a98683c783d00d464a66ea154661 | quote: Everything on this page is wrapped by the SDKs and CLI — `pip install pilldrops`, `npm i @pilldrops/sdk`, or the `pilldrops` CLI
  - [2] 2026-11-24: a self-host server is offered for the user to install and run on a Linux server | capture: sha256:f5051e219a033e44f1f3e39b3b294d1bc051ecd06892d8304bf831cade441141 | quote: Two minutes on any Linux server. Your data never leaves it.
  - [1] 2026-11-24: the Personal plan includes 30 active hours a month | capture: sha256:d1a7d1522b12c2440f96a2aed5398ce974aad1385b9f624454b028d39236c383 | quote: - 30 active hours / month
  - [1] 2026-11-24: the free tier is USD 5 of credit with no card | capture: sha256:d1a7d1522b12c2440f96a2aed5398ce974aad1385b9f624454b028d39236c383 | quote: $5 credit — no card
  - [4] 2026-11-24: the hosted offer has an HTTP API authenticated by an API key | capture: sha256:7e991a1207ffc65a93431d13494547583373a98683c783d00d464a66ea154661 | quote: Every `/v1` request needs `Authorization: Bearer <key>`. Create keys in the [dashboard](https://pilldrops.com/dashboard#/keys) or via `POST /v1/keys` below. New accounts get $5 free credits.
- sources:
  - [1] https://pilldrops.com/pricing
  - [2] https://pilldrops.com/
  - [3] https://pilldrops.com/privacy
  - [4] https://pilldrops.com/docs
