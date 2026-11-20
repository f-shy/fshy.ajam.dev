# Mitos

> mitos.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mitos/ | JSON https://fshy.ajam.dev/api/v1/entity/mitos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mitos

- `compute/mitos` | paid-only | evidence documented | binding per-object-cap | category microVM (Firecracker), forked sandboxes | tier pay-as-you-go, 1 vCPU / 1 GiB / no storage
- needs card no, phone no, ID no, institution no | verified 2026-10-24T02:11:00.000Z (live) | stale on 2026-11-24
- url https://mitos.run/pricing
- price USD 0.00 per TB (egress free) | parsed USD 42.34/mo
- free tier: USD 100 of signup credit, no card; prepaid top-ups after that. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit
- per-object cap: not applicable
- retention: Storage is metered at USD 0.073/GiB-month; a paused sandbox costs nothing to run and keeps its state. | source: [1]
- egress: Egress is free: 'data transfer out is free' and 'Egress Free no egress fees'. | metered: no | free allowance: unmetered | source: [1]
- identity: email | detail: Free signup credit of USD 100 with no card; prepaid top-ups after that. No hold stated.
- interface: cli, rest
- limits:
  - per-object-cap (binding): rates are illustrative and can change at general availability [1]
- binding note: The wall is that hosted Mitos is in early access with illustrative rates, so the price itself is provisional; behind that, USD 0.046/vCPU-hour is 7x the VPS-class rate.
- interface detail: the `mitos` CLI drives create, exec, file IO, fork and terminate; host state is early access and the engine is open source under Apache 2.0
- tooling: the mitos CLI or the engine on your own Kubernetes cluster; no SSH sentence was read
- composes with: A forked-microVM service optimised for swarms that idle between model calls, priced per second with no charge while paused: wrong shape for one always-on box, and USD 42.34 a month at 1 vCPU / 1 GiB if it were held up.
- reliability: Hard spend caps are on by default: a runaway org suspends at the cap instead of billing on.
- notes: 730-hour arithmetic at 1 vCPU / 1 GiB: 0.046 x 730 = USD 33.58 compute + 0.012 x 730 = USD 8.76 memory = USD 42.34, before storage. That is 14.5x Krova's 1 vCPU / 1 GiB. The product is designed for the opposite workload: pay nothing while paused, so a 24/7 box is the worst case for it.
- evidence note: Rates, the no-idle-charge rule, free egress and the illustrative-rates caveat are quoted from the pricing page read. What lowers it: the vendor itself says the rates are illustrative, so the 730-hour figure may not survive general availability.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - billing_model: per-second
  - term: prepaid, no commitment
  - m10h_usd: 17.4
  - m24h_usd: 42.34
  - price_arithmetic: 1 vCPU x 0.046 + 1 GiB x 0.012 = USD 0.058/hour; x 730 = USD 42.34 at 24/7; x 300 (10 h/day) = USD 17.40. Storage adds 0.073 per GiB-month.
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.ports: not stated on the pricing page
  - session_cap.restart_required: no
  - session_cap.note: no cap stated; paused sandboxes bill nothing while paused
- evidence:
  - [1] 2026-10-24: quoted: 'Compute · vCPU $0.046 / vCPU-hour Memory · RAM $0.012 / GiB-hour Storage $0.073 / GiB-month Egress Free no egress fees'
  - [1] 2026-10-24: quoted: 'Hosted Mitos is in early access. Rates here are illustrative; final rates land at general availability.' and 'No idle charge ... Paused sandboxes cost nothing to run.'
  - [1] 2026-10-24: quoted: '$100 to start. Free signup credit, no card. Prepaid top-ups after that.'
- sources:
  - [1] https://mitos.run/pricing
