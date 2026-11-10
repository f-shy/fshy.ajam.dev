# zipbox

> zipbox.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zipbox/ | JSON https://fshy.ajam.dev/api/v1/entity/zipbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zipbox

- `compute/zipbox` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier prepaid
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T01:52:56.000Z (live) | stale on 2026-11-24
- url https://zipbox.ai/pricing
- price parsed USD 20/mo
- free tier: 'Every new account can get $25 in credit with a one-time $5 top-up. A positive balance is what boots a machine. Top up by card; the card is saved for auto top-up.' | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: A deposit match, not a grant: USD 5 must be paid by card first. 'Credits are prepaid and non-refundable.'
- per-object cap: Four sizes: 'Tiny 1 vCPU · 2 GB RAM · 20 GB disk $0.0068 $5', 'Small 2 vCPU · 4 GB · 80 GB $0.0137 $10', 'Medium 4 vCPU · 8 GB · 160 GB $0.0274 $20', 'Large 6 vCPU · 16 GB · 320 GB $0.0548 $40'. | source: [1] | note: The per-month column is the 24/7 price at that size.
- retention: 'Paused boxes cost $0.' No deletion timer for a paused box is stated. | source: [1]
- egress: No egress charge or allowance is stated on the pricing page. | metered: no | source: [1]
- identity: card | detail: A card is required for the USD 5 top-up before any credit lands, and 'the card is saved for auto top-up'. No hold amount is stated; the charge is a real USD 5, not an authorisation.
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 25 credit requires a one-time USD 5 top-up [1]
  - volume-quota (binding): Medium 4 vCPU / 8 GB / 160 GB at USD 0.0274 an hour, USD 20 a month [1]
- limits note: The balance also pays for model and API calls made through platform keys, so compute and inference compete for the same USD 25.
- binding note: The prepaid balance is the only limit: USD 25 at USD 0.0274 an hour is 912 hours, and nothing else in the published terms stops a box running.
- interface detail: web console and API; the platform also bills model and API calls through the same balance
- tooling: web dashboard; per-box itemised model and API spend
- composes with: a cheap 4 vCPU box whose balance also pays for model calls, so an agent and its inference share one wallet
- reliability: 'A positive balance is what boots a machine', so a zero balance stops the box rather than billing overage.
- notes: USD 25 at Medium's USD 0.0274 is 912 hours, so the match buys 1.25 months of a 4 vCPU / 8 GB / 160 GB machine for USD 5 out of pocket, which is the lowest cash cost for a 4 vCPU month anywhere among documented hosts. It is card-gated at signup and the balance is shared with inference, so it is not a free tier.
- evidence note: Sizes, rates, the top-up requirement and the non-refundable term are on the pricing page read. Not established: whether the USD 25 is granted once per account or once per person, and whether a paused box is retained indefinitely.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 160
  - billing_model: per-second from a prepaid balance
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: paused boxes cost nothing; no cap published
  - keep_rate.value: 0.0
  - keep_rate.basis: paused boxes cost USD 0, quoted
  - keep_rate.source: https://zipbox.ai/pricing
  - persistent_storage.included_gib: 80
  - persistent_storage.price_gib_month: included
  - persistent_storage.durability: survives pause
  - persistent_storage.survives_stop: yes
  - persistent_storage.max_retention: unpublished
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: unstated
  - free_tier_kind: top-up-match
  - m10h_usd: 8.22
  - m24h_usd: 20.0
  - price_arithmetic: 0.0274/h x 730 = 20.00; 25 / 0.0274 = 912.4 h
  - price_note: Small shape, USD 0.0137 per hour, billed per second while running.
  - price_basis: 10 h/day x 30 = 300 h; 24/7 x 30 = 730 h
  - burst_x: 1.0
  - term: prepaid
  - credit_usd: 25
  - cash_to_unlock_usd: 5
  - credit_months_at_shape: 1.25
  - credit_hours_at_shape: 912.4
  - credit_expiry: not stated; credits are non-refundable
- evidence:
  - [1] 2026-10-22: Tiny USD 0.0068 (1 vCPU/2 GB/20 GB), Small USD 0.0137 (2/4/80), Medium USD 0.0274 (4/8/160), Large USD 0.0548 (6/16/320)
  - [1] 2026-10-22: USD 25 in credit with a one-time USD 5 top-up; paused boxes cost USD 0; card saved for auto top-up
  - [1] 2026-10-24: quoted: 'Every new account can get $25 in credit with a one-time $5 top-up. A positive balance is what boots a machine. Top up by card; the card is saved for auto top-up.'; 'Medium 4 vCPU · 8 GB RAM · 160 GB disk $0.0274 $20'; 'Paused boxes cost $0.'; 'Credits are prepaid and non-refundable.'
- sources:
  - [1] https://zipbox.ai/pricing
