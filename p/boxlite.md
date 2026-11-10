# BoxLite Cloud

> boxlite.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxlite/ | JSON https://fshy.ajam.dev/api/v1/entity/boxlite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BoxLite Cloud

- `compute/boxlite-cloud` | paid-only | evidence documented | binding per-object-cap | category cloud VM | tier smallest box: 1 vCPU / 1 GiB / 10 GiB
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T02:11:00.000Z (live) | stale on 2026-11-24
- url https://boxlite.ai/
- price parsed USD 48.62/mo
- free tier: USD 100 in free credits, so you can build and run against Cloud before spending anything of your own. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit
- per-object cap: per-box ceiling of 4 vCPU, 32 GiB of memory and 120 GiB of storage on every plan
- retention: Around 10 GiB of real disk per box, and 'Packages, files and environment are still there after a stop and a start'. | source: [1]
- egress: No egress price and no transfer allowance are published on the page read; metered is recorded as false because nothing is known to be charged per gigabyte, which is an absence of evidence, not a promise of free traffic. | metered: no | free allowance: not stated | source: [1]
- identity: card | detail: A prepaid wallet funds usage and paid top-ups are refundable within 14 days; the card type, hold and debit terms were not stated on the page read. Unverified.
- interface: rest
- limits:
  - per-object-cap (binding): 4 vCPU, 32 GiB and 120 GiB per box on every plan [1]
- limits note: the included allowance resets each cycle, so the meter is the plan and not a signup grant; a stopped box keeps billing disk until deletion
- binding note: The shape ceiling is 4 vCPU, but the deciding wall is the rate: USD 0.0504 per vCPU-hour and USD 0.0144 per GiB-hour put the smallest box at USD 48.62 a month.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: No free lane fits this provider: the cheapest start is USD 19 a month on Starter with USD 30 of included usage. Free network traffic still matters for the egress topic, because the same workload on bunny.net would pay USD 0.01 per GB in Europe.
- reliability: Files survive a stop and a start; no reliability event observed.
- notes: Check of the vendor's own arithmetic: 0.0504 + 0.0144 + 10 x 0.00018 = USD 0.0666/hour, which is exactly the headline 'smallest box' figure, so the rate card and the summary agree. At 730 h: 0.0666 x 730 = USD 48.62. The docs page (docs.boxlite.ai/cloud/pricing) returned a JavaScript shell on two attempts, so the plan table (Starter USD 19/month with USD 30 of quota, Pro USD 149, Max USD 499) is unverified among evaluated providers.
- evidence note: The rates, the smallest box, the per-box ceilings, the USD 100 credit and the persistence sentence are quoted from the vendor's own page read. What would raise it: the egress terms and the payment method, neither of which is on that page.
- extras:
  - facets.class: paid-only
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 20
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 10
  - billing_model: per-second
  - term: prepaid wallet, monthly plans optional
  - m10h_usd: 19.98
  - m24h_usd: 48.62
  - price_arithmetic: (0.0504 + 0.0144 + 10 x 0.00018) = USD 0.0666/hour x 730 = USD 48.62; x 300 (10 h/day) = USD 19.98. 2 vCPU / 4 GiB / 10 GiB would be USD 0.1752/hour = USD 127.90 a month.
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.ports: not stated on the page read
  - session_cap.restart_required: no
  - session_cap.note: no wall-clock cap stated; a stopped box keeps its files
- evidence:
  - [1] 2026-10-22: '$100 in free credits on sign-up, no card required', and coupon codes redeem for credits
  - [2] 2026-10-22: Small 1 vCPU / 1 GiB / 10 GiB at USD 0.0666 per hour and USD 47.95 for 30 days running against USD 1.30 for 30 days stopped; Medium 2 / 4 / 20 at USD 0.1620 per hour; Large 4 / 8 / 50 at USD 0.3258 per hour; compute billing stops at the stop request and disk billing at the delete request
  - [3] 2026-10-22: 'Nothing else is metered: no charge for network traffic, API requests, mounted volumes, preview URLs, or boot time', no minimum billable duration and no rounding up to the hour
  - [4] 2026-10-22: Starter USD 19 per month carries USD 30 of usage and 20 boxes, Pro USD 149 carries USD 250 and 100 boxes, Max USD 499 carries USD 900; concurrency is the cap that pushes a 40-box fleet to Pro
  - [5] 2026-10-23: 'Plans come with a usage allowance that resets each cycle; anything beyond it draws from a prepaid wallet.', quoted; the plan table starts at Starter at USD 19 a month
  - [1] 2026-10-24: quoted: 'Pay as you go — $0.0666 per hour, smallest box. No subscription.'; '- 1 vCPU · 1 GiB memory · 10 GiB disk'; 'CPU — $0.0504 per vCPU·hour'; 'Memory — $0.0144 per GiB·hour'; 'Disk — $0.00018 per GiB·hour'
  - [1] 2026-10-24: quoted: 'Every box is a virtual machine with its own Linux kernel, sized when you create it — up to 4 vCPU and 32 GiB of memory. Hardware isolation, not a shared kernel.'
  - [1] 2026-10-24: quoted: 'Packages, files and environment are still there after a stop and a start, so you are not rebuilding the world on every boot.' and 'Start with $100 in free credits'
- sources:
  - [1] https://boxlite.ai/
  - [2] https://docs.boxlite.ai/cloud/box-costs
  - [3] https://docs.boxlite.ai/cloud/pricing
  - [4] https://docs.boxlite.ai/cloud/plans
  - [5] https://www.boxlite.ai/
