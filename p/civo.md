# Civo Compute

> civo.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/civo/ | JSON https://fshy.ajam.dev/api/v1/entity/civo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Civo Compute

- `compute/civo` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:27:28.371Z (live) | stale on 2026-12-05
- url https://www.civo.com/pricing
- price parsed USD 21.43/mo
- free tier: USD 250 in credits on signup: 'You are entitled to a Free Trial of the Services to a value of $250 for a period of thirty-one (31) calendar days'. The trial is limited to one per customer. The Kubernetes control plane is free on every cluster; worker nodes bill from USD 0.007440 an hour for 1 core, 1 GB and 30 GB of NVMe. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: egress and ingress fees are free and unlimited, so there is no overage price | metered: no | free allowance: unlimited | source: [2]
- identity: card | detail: a card is required and must be verified before any instance or cluster exists: 'you need a valid payment method on file at all times, and won't be able to create Kubernetes clusters or instances before your card is verified'. The signup form itself asks only for a name, an email address and a password, and virtual or prepaid cards are refused
- interface: cli
- limits:
  - volume-quota (binding): USD 250 of credit over 31 calendar days, one trial per customer [1]
  - per-object-cap: the managed control plane costs nothing; workers bill from $0.007440 an hour at 1 core and 1 GB [2]
- limits note: the trial is 31 days and one per customer; instance quota is published only as an image and a default of 8 vCPU is reported, not documented
- binding note: the 31-day trial window and its USD 250 ceiling end evaluated offerings before any per-hour rate limit is reached.
- interface detail: the Civo CLI is documented; a documented API for the Civo cloud platform authenticated by an API key is also published
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The compute rate card is not linear in cores: Extra Large is 6 cores for $0.119048 while 2X Large is 8 cores for $0.238095, so two Extra Large instances cost the same as one 2X Large and carry 12 cores against 8. Billing rounds up to the full hour and a stopped instance still bills.
- evidence note: The control plane is free on an ongoing basis.
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 30
  - shape.note: Extra Small; $250 covers 33,600 hours of it, which is 4.6 years at one node always on
  - session_cap.restart_required: no
  - session_cap.note: no session cap; a cluster bills per worker hour until the cluster is deleted
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: one-time-credit
  - m10h_usd: 8.93
  - m24h_usd: 21.43
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap. Rates re-read on the vendor pricing page on 2026-10-23.
  - granularity.min_billed_s: 3600
  - burst_x: 2.0
  - burst_bill: min 1 h
  - ps.gib: 30
  - ps.price: included in the worker size, NVMe
  - ps.durability: NVMe on the node
  - ps.on_stop: no
  - ps.on_destroy: no
  - ps.retention: the node's lifetime; a volume survives separately
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - hourly_usd.xSmall: 0.00744
  - hourly_usd.Small: 0.014881
  - hourly_usd.Medium: 0.029762
  - hourly_usd.Large: 0.059524
  - hourly_usd.Extra Large: 0.119048
  - hourly_usd.2X Large: 0.238095
- evidence:
  - [1] 2026-10-23: quoted: 'You are entitled to a Free Trial of the Services to a value of $250 for a period of thirty-one (31) calendar days'
  - [2] 2026-10-23: quoted hourly: xSmall 1 GB/1 core/25 GB $0.007440, Small 2 GB/1 core/25 GB $0.014881, Medium 4 GB/2 cores/50 GB $0.029762, Large 8 GB/4 cores/100 GB $0.059524, Extra Large 16 GB/6 cores/150 GB $0.119048, 2X Large 32 GB/8 cores/200 GB $0.238095
  - [2] 2026-10-23: quoted: 'At Civo, we offer our new customers $250 of free credit for the first month you sign up.' and 'calculated hourly, rounding up to the next full hour'
  - [2] 2026-11-04: egress is free and unlimited | capture: sha256:bbc2f2e8fa434568565a2a7188d0de4d0f0f6dc5bdedfb57005f6d2b639cefbf | quote: Egress and Ingress fees - Free & unlimited.
  - [3] 2026-11-04: a CLI exists | capture: sha256:0b795b47a0abfd465b08d6a3aa60418676b2ceb1a7a3548ec8822d5ec1982f19 | quote: Civo CLI is a tool to manage your Civo.com account from the terminal.
  - [4] 2026-11-04: a documented API exists | capture: sha256:09c3e0d8274e930345b6e6c758b3ddc127027ba3ed8d42308071432e4fcf3dd0 | quote: This is the entire API for the Civo cloud platform.
- sources:
  - [1] https://www.civo.com/legal/terms
  - [2] https://www.civo.com/pricing
  - [3] https://github.com/civo/cli
  - [4] https://www.civo.com/api
