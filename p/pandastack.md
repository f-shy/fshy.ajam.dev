# PandaStack

> pandastack.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pandastack/ | JSON https://fshy.ajam.dev/api/v1/entity/pandastack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PandaStack

- `compute/pandastack` | qualifies-with-caveat | evidence documented | binding per-object-cap | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-24T13:21:00.909Z (live) | stale on 2026-12-25
- url https://www.pandastack.ai/pricing/
- free tier: a $5.40 free credit, 1 GiB of persistent volume on Free, no charge for egress or inbound on any plan, and hibernation that writes state to disk and stops CPU and RAM metering | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no charge for outbound transfer on any plan, and inbound is free too; egress is metered for fair use | metered: no | source: [1]
- identity: email
- interface: browser, cli
- limits:
  - request-rate: $5.40 of free credit; a sandbox-hour is metered per second [1]
  - per-object-cap (binding): 1 GiB of persistent volume on Free, 100 GiB on Pro and 2.5 TiB on Team [1]
  - retention-clamped: hibernation writes state to disk and stops metering, and hibernated storage is not billed while that holds [1]
- interface detail: hosted control plane with a management API and a billing portal; the published pricing page does not name the API shape
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing FAQ was read on 2026-10-22 and states the credit, the volume quotas and the hibernate and egress rules. The hibernate answer is the state axis and the egress answer is the network axis, both from one page
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: 1 hour maximum sandbox lifetime on Free; Pro allows up to a 7-day TTL
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.gib: 1
  - ps.price: hibernated state storage is currently included at no extra charge
  - ps.durability: persistent volume plus hibernated state on disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.allowance: egress and inbound are free on every plan, metered for fair use
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'No. Hibernation writes state to disk and stops active vCPU/RAM metering. Storage for hibernated state is currently included at no extra charge.' and 'We don't charge for outbound transfer on any plan, and inbound is free too' and 'What's the $5.40 free credit?' with a Free volume quota of 1 GiB, quoted
  - [1] 2026-11-18:  | capture: sha256:03a1a65ed90849b5c356ff03781a89ff261115eb97c7a087582b20ecaec7d4c1 | quote: 1-hour max sandbox lifetime · Apps & databases exempt
  - [1] 2026-11-24: both directions of transfer are free on every plan, with egress metered for fair use | capture: sha256:d5fbe6cbfd811e2067839cbc6f0b6fc742f2058d0b40ec019335ea044ddb361d | quote: We don't charge for outbound transfer on any plan, and inbound is free too. We do expect fair use — egress is metered so we can see it, and if a workspace's traffic is wildly out of line with normal agent, app, and database workloads we'll get in touch rather than bill you by surprise.
  - [1] 2026-11-24: a hosted control plane operates the sandboxes | capture: sha256:d5fbe6cbfd811e2067839cbc6f0b6fc742f2058d0b40ec019335ea044ddb361d | quote: The control plane records usage at sandbox stop, then submits idempotent Stripe meter events every 60 seconds.
  - [1] 2026-11-24: a hosted billing portal exists | capture: sha256:d5fbe6cbfd811e2067839cbc6f0b6fc742f2058d0b40ec019335ea044ddb361d | quote: Monthly plans can cancel at the billing portal.
  - [1] 2026-11-24: the free plan still carries USD 5.40 of monthly credit and 1 GiB of persistent volume | capture: sha256:d5fbe6cbfd811e2067839cbc6f0b6fc742f2058d0b40ec019335ea044ddb361d | quote: * $5.40 of usage credit / month (≈77 hours with 1 vCPU busy and 1 GiB resident) * 1 persistent volume · 1 GiB
  - [1] 2026-11-24: transfer is free in both directions on every plan | capture: sha256:d5fbe6cbfd811e2067839cbc6f0b6fc742f2058d0b40ec019335ea044ddb361d | quote: We don't charge for outbound transfer on any plan, and inbound is free too.
  - [1] 2026-11-24: a self-hosted core exists in addition to the hosted service | capture: sha256:d5fbe6cbfd811e2067839cbc6f0b6fc742f2058d0b40ec019335ea044ddb361d | quote: Yes. The core is Apache-2.0. You bring machines, networking, observability, and any cloud costs.
- sources:
  - [1] https://www.pandastack.ai/pricing/
