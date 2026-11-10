# Lizard

> lizard.build | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lizard/ | JSON https://fshy.ajam.dev/api/v1/entity/lizard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lizard

- `compute/lizard` | trial-only | evidence documented | binding volume-quota | category container and VM sandbox | tier Pro
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T01:52:56.000Z (live) | stale on 2026-11-24
- url https://lizard.build/pricing
- price parsed USD 23.65/mo
- free tier: 'Pro costs $19 a month and includes $19 in monthly credits for the whole platform.' The only free path is a trial: 'Pro starts with a 7-day trial and $5 in trial credits. You need a card to start it, but we charge nothing during the 7 days.' | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: A plan credit equal to the plan fee, and a card-gated trial. There is no grant.
- per-object cap: 'Sandboxes come in three sizes ... Small (2 vCPU, 4 GB RAM) at $0.0162/hour, Medium (4 vCPU, 8 GB RAM) at $0.0324/hour, and Large (8 vCPU, 16 GB RAM) at $0.0648/hour.' During the trial the sandbox limit is 5. | source: [1] | note: 'They use the same CPU, memory and storage rates as other resources and count toward the $19 of included usage.'
- retention: A successful pause stops compute charges; Persistent Volumes storage continues to be billed while data is kept. | source: [1]
- egress: Sandbox egress has no separate per-GB charge, with '2 TB per account over a rolling 30 days' included; apps and databases pay the per-GB rate. | metered: yes | free allowance: 2 TB over a rolling 30 days for sandboxes | source: [1]
- identity: card | detail: 'You need a card to start it, but we charge nothing during the 7 days.' No hold amount is stated. The card is charged USD 19 when the trial ends unless cancelled.
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 19 monthly credit included in a USD 19 monthly fee [1]
  - volume-quota (binding): sandbox egress 2 TB per account over a rolling 30 days [1]
- limits note: At USD 0.0324 an hour a Medium sandbox costs USD 23.65 for a month, which is more than the USD 19 credit, so the plan cannot hold a Medium up for 730 hours either.
- binding note: The USD 19 credit against USD 23.65 a month for the 4 vCPU size is what fails; the 2 vCPU size at USD 11.83 fits with USD 7 to spare.
- interface detail: REST API and CLI; sandbox create takes a millisecond lifetime
- tooling: lizard CLI, SDK, REST; templates include codex, claude, opencode, pi, desktop
- composes with: 2 TB of included egress per account makes it the natural host for a crawler that serves what it collects
- reliability: When the credit is spent, running apps, databases and Sandboxes pause and no new ones can be created; the data is kept but the service stops.
- notes: At USD 0.0324 an hour the Medium sandbox is USD 23.65 a month, so the USD 19 credit is 586 hours; the Small at USD 0.0162 is USD 11.83 a month and 1,173 hours, so USD 19 covers a full month with about USD 7 spare. The 7-day trial is card-gated, which makes this a paid row.
- evidence note: Plan, credit, sandbox sizes, rates, the trial terms and the egress allowance are on the pricing page read.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - billing_model: per-second, monthly plan credit
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: billed 'including idle time'; a pause stops compute charges
  - keep_rate.value: 0.0
  - keep_rate.basis: a pause stops compute charges
  - keep_rate.source: https://lizard.build/pricing
  - persistent_storage.included_gib: 5
  - persistent_storage.price_gib_month: persistent volumes billed separately
  - persistent_storage.durability: paused sandbox keeps data
  - persistent_storage.survives_stop: yes
  - persistent_storage.max_retention: unpublished
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - free_tier_kind: plan-credit
  - m10h_usd: 9.72
  - m24h_usd: 23.65
  - price_arithmetic: 0.0324/h x 730 = 23.65; 19 / 0.0324 = 586 h; small 0.0162 x 730 = 11.83
  - price_note: Small shape at the live USD 0.0162 per hour.
  - price_basis: 10 h/day x 30 = 300 h; 24/7 x 30 = 730 h
  - burst_x: 1.0
  - shape_small.vcpu: 2
  - shape_small.ram_gib: 4
  - term: monthly
  - credit_usd: 19
  - credit_months_at_shape: 0.8
  - credit_hours_at_shape: 586
  - credit_expiry: monthly; the plan fee and the credit are the same money
- evidence:
  - [1] 2026-10-22: Small (2 vCPU, 4 GB) USD 0.0162/h, Medium (4/8) USD 0.0324/h, Large (8/16) USD 0.0648/h, billed per second including idle
  - [2] 2026-10-22: sizes carry a /workspace disk of 5, 20 and 50 GB; egress included to 2 TB per account per rolling 30 days
  - [2] 2026-10-22: raw API default lifetime timeoutMs 0 (no expiration); SDK and CLI default 5 minutes; a command does not reset the deadline
  - [1] 2026-10-22: 7-day trial with USD 5 in trial credits and a card required; Pro USD 19 a month with USD 19 included
  - [1] 2026-10-22: 'Pro starts with a 7-day trial and $5 in trial credits. You need a card to start it, but we charge nothing during the 7 days, and you can cancel before the trial ends', quoted
  - [1] 2026-10-22: sandbox sizes and rates, quoted: Small 2 vCPU / 4 GB at $0.0162 an hour, Medium 4 / 8 at $0.0324, Large 8 / 16 at $0.0648, billed per second including idle time
  - [1] 2026-10-24: quoted: 'Pro costs $19 a month and includes $19 in monthly credits'; 'Pro starts with a 7-day trial and $5 in trial credits. You need a card to start it, but we charge nothing during the 7 days'; 'Small (2 vCPU, 4 GB RAM) at $0.0162/hour, Medium (4 vCPU, 8 GB RAM) at $0.0324/hour, and Large (8 vCPU, 16 GB RAM) at $0.0648/hour'; 'the included allowance is 2 TB per account over a rolling 30 days'.
- sources:
  - [1] https://lizard.build/pricing
  - [2] https://lizard.build/docs/platform/limits/
