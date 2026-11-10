# PillDrops

> pilldrops.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pilldrops/ | JSON https://fshy.ajam.dev/api/v1/entity/pilldrops.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PillDrops

- `compute/pilldrops` | qualifies-with-caveat | evidence documented | binding retention-clamped | category microVM (KVM) sandbox with a persistent workstation | tier Personal
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:54:08.000Z (live) | stale on 2026-11-24
- url https://pilldrops.com/pricing
- price parsed USD 122.39/mo
- free tier: Start free with a $5 usage credit and no card; the Free tier is 5 concurrent sandboxes, 4 h max session, 2 vCPU / 2 GB RAM / 2 GB disk, all templates and SDKs, no persistent workstation | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit, not hours: USD 5 of usage at the published per-second rates
- per-object cap: not applicable: the unit is a machine, not an object; the billed shape is 2 vCPU / 4 GB / 10 GB on Personal
- retention: unknown: Personal and Pro each include '1 persistent workstation', and a paused sandbox bills storage only at USD 0.15 per GB-month, but no page read states how long a paused workstation survives before deletion | source: [1]
- egress: Not published. The pricing page lists three meters only - vCPU-seconds, GB-seconds of RAM, and GB-months of storage - and states no traffic allowance or per-GB rate. The plans are 'bring-your-own-key' and sell the machine, not model usage. | metered: no | source: [1]
- identity: email | detail: 'Start free with a $5 usage credit and no card' and 'No card. One pip install pilldrops away.' Card types for the paid plans, any authorisation hold, and whether a debit or prepaid card is accepted are not stated on the page read.
- interface: rest, cli
- limits:
  - retention-clamped (binding): 30 active hours a month on Personal (100 on Pro), a 4 h maximum session on the free tier and 24 h on Pro [1]
  - volume-quota: USD 5 of usage credit on the free tier, no card [1]
- limits note: The 30-hour monthly allowance is wall-clock, not a byte quota, and it is the number that decides the plan: 30 hours is 4% of a month. Storage is billed separately at USD 0.15 per GB-month even while the workstation is paused.
- binding note: The plan's 30 active hours and the 4 h (free) / 24 h (Pro) session cap clamp runtime before any byte quota could; beyond the allowance the meter runs at USD 0.1656 an hour, which is USD 120.89 for a month.
- interface detail: Python SDK, MCP server, templates, and a Telegram bridge on the paid plans. The product is an agent-running machine, not a shell you SSH into.
- tooling: The vendor's SDK and MCP; a Telegram bridge for the paid tiers. No SSH or generic compute interface was documented on the page read.
- composes with: The USD 3 Personal plan buys 30 workstation hours a month of a 2 vCPU / 4 GB machine, which is the cheapest way documented to keep a small always-warm environment for an agent - but it is 30 hours, not 730, and the metered rate beyond that is USD 0.1656 an hour.
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
  - [1] 2026-10-24: quoted: '$0.0000140 per vCPU-second, $0.0000045 per GB RAM-second, $0.15 per GB-month storage' and 'a paused sandbox bills storage only'
  - [1] 2026-10-24: identity: 'Start free with a $5 usage credit and no card'
  - [2] 2026-10-24: quoted: 'Compute is metered per second: $0.0000140 per vCPU-second and $0.0000045 per GB of RAM-second, plus $0.15/GB-month storage', and '$5 in free credits. No card.'
- sources:
  - [1] https://pilldrops.com/pricing
  - [2] https://pilldrops.com/
