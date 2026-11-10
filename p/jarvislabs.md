# Jarvislabs

> jarvislabs.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jarvislabs/ | JSON https://fshy.ajam.dev/api/v1/entity/jarvislabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jarvislabs

- `compute/jarvislabs` | paid-only | evidence documented | binding none | category GPU cloud | tier per-minute, no free tier
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T08:50:28.019Z (live) | stale on 2026-12-04
- url https://jarvislabs.ai/pricing
- price parsed USD 36.5/mo
- free tier: no free tier: GPU instances are billed per minute on demand, with a lower spot rate that can be interrupted. Listed hourly rates, on demand / spot: H100 SXM 80GB USD 3.49 / 1.54, A100 80GB USD 1.49 / 0.89, L4 24GB USD 0.44 / 0.29. The page lists no L40S or RTX 4090, states no minimum bill, and does not state in the stored text which GPU count (1, 2, 4 or 8 per instance) the listed rates are for. The smallest shape is a CPU VM at 2 vCPU / 8 GB for USD 0.05 an hour; in-region egress is free | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: No trial, no credit and no free hours on the pricing page.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not stated on the pricing page; storage is billed separately | source: [1]
- egress: 'Egress Free in-region' | metered: no | free allowance: unmetered in-region | source: [1]
- identity: card | detail: a paid account: per-minute billing with no free tier or trial on the pricing page
- interface: unknown
- limits:
  - volume-quota: 0 hours: no free tier [1]
- binding note: no free allowance exists; the first minute is the first charge
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: USD 0.05/hr is USD 36.50 a month at 730 hours for 2 vCPU and 8 GB. It is the cheapest paid CPU hour found among evaluated providers and still not free.
- evidence note: the rates and the absence of a free tier are read from the pricing page. earlier derived per-vCPU and per-GB rates reconcile with the bundle price ($0.012x2 + $0.0032x8 = $0.0496 against $0.05).
- extras:
  - keep_rate: 1.0
  - billing_model: hourly
  - shape.vcpu: 2
  - shape.ram_gib: 8
  - shape.note: cheapest CPU shape; an L4 is USD 0.44/hr and an H100 USD 3.49/hr
  - session_cap.restart_required: no
  - session_cap.note: a paid VM runs until stopped
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.price: $0.10 a GB-month
  - ps.durability: storage volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while billed
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.allowance: egress in-region is free
  - term: per minute
  - m10h_usd: 15.0
  - m24h_usd: 36.5
  - price_arithmetic: USD 0.05/hr x 300 h = USD 15.00 at 10 h/day; x 730 h = USD 36.50 at 24/7
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Per-minute billing, no commitments. Boot a Template in 1.8 seconds or a VM in under 90s. Scale to 8 GPUs per instance.' with 'CPU VMs are priced as $0.012 / vCPU + $0.0032 / GB RAM per hour' and 'Storage $0.10/GB · month', quoted
  - [1] 2026-10-24: quoted: 'Per-minute billing, no commitments. Boot a Template in 1.8 seconds or a VM in under 90s. Scale to 8 GPUs per instance.'
  - [1] 2026-10-24: quoted: 'CPU VM 2 vCPU · 8 GB $0.05' — the cheapest shape
  - [1] 2026-10-24: quoted: 'EgressFreein-region'
  - [1] 2026-10-24: the page contains no free tier and no trial
  - [1] 2026-11-03: on-demand instances are billed per minute and spot instances are interruptible | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: On-demand instances are billed per minute; pause and resume any time. Spot instances cost less but can be interrupted when the capacity is needed, so save your work often.
  - [1] 2026-11-03: the pricing page was read on this date | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: On-demand instances are billed per minute; pause and resume any time. Spot instances cost less but can be interrupted when the capacity is needed, so save your work often.
  - [1] 2026-11-03: H100 SXM 80 GB is USD 3.49 per hour on demand and USD 1.54 spot | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: NVIDIA H100 SXM 80GB 16 200GB $3.49 −56%$1.54
  - [1] 2026-11-03: A100 80 GB is USD 1.49 per hour on demand and USD 0.89 spot | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: NVIDIA A100 80GB 80GB 16 112GB $1.49 −40%$0.89
  - [1] 2026-11-03: L4 24 GB is USD 0.44 per hour on demand and USD 0.29 spot | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: NVIDIA L4 24GB 32 124GB $0.44 −34%$0.29
  - [1] 2026-11-03: the GPU list has no L40S and no RTX 4090; an instance is priced for 1, 2, 4 or 8 GPUs | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: NVIDIA H200, H100, RTX Pro 6000 Blackwell, A100, A30 and L4. Pick 1, 2, 4 or 8 GPUs to price an instance.
  - [1] 2026-11-03: rates outside India are in USD | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: Customers outside India are billed in USD.
  - [1] 2026-11-03: the pricing page confirms per-minute on-demand billing and lists the GPU rates | capture: sha256:e9894bdf207cc93924a68a881eac267a670496f4b69c075ff8ce0ec750d54abf | quote: On-demand instances are billed per minute; pause and resume any time. Spot instances cost less but can be interrupted when the capacity is needed, so save your work often.
- sources:
  - [1] https://jarvislabs.ai/pricing
