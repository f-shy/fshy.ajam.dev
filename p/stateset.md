# StateSet Sandbox

> stateset.app | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stateset/ | JSON https://fshy.ajam.dev/api/v1/entity/stateset.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StateSet Sandbox

- `compute/stateset` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox | tier Hobby, shared sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:18.817Z (live) | stale on 2026-12-05
- url https://sandbox.stateset.app/pricing
- free tier: Hobby is USD 0 a month 'plus usage, billed per second', including 5 vCPU-hours and 420 memory GB-hours each month, 20 GB of network egress and 5,000 sandbox creations. | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: monthly vCPU-hours, reset each month
- per-object cap: max sandbox runtime 45 minutes on Hobby, 24 hours on Pro; 10 concurrent sandboxes on Hobby, 50 on Pro
- retention: Not stated on the pricing page: a 45-minute maximum runtime means nothing survives a session unless the sandbox is durable, and durable sandboxes are listed as 'Not available' on Hobby. | source: [1]
- egress: 20 GB of network egress included each month on Hobby (100 GB Pro, 1,000 GB Team); overage is USD 0.15 per GB on Hobby and Pro and USD 0.12 per GB on Team | metered: yes | free allowance: 20 GB | price per TB: USD 150 | source: [1]
- identity: card | detail: The Hobby plan is USD 0 plus usage, which normally needs a card on file to meter beyond the included hours; no card, hold or debit statement was read on the pricing page. Unverified.
- interface: rest
- limits:
  - retention-clamped (binding): 45 minutes maximum sandbox runtime on Hobby, 24 hours on Pro (USD 49/month) [1]
- binding note: A 45-minute wall-clock cap reaps the machine before a monthly budget can matter, so the cap is the wall and price is irrelevant.
- interface detail: REST API (api.sandbox.stateset.app), Node.js SDK and Python SDK; no CLI or SSH found in the docs read
- tooling: not stated
- composes with: not established
- reliability: Shared sandboxes 'burst on Spot capacity at the lowest price and can be preempted', which is an interruption that cannot be scheduled around.
- notes: No 730-hour figure exists to record because the product cannot run for 730 hours: 45 minutes is the Hobby cap and 24 hours the Pro cap. The byline prices the reference 4 vCPU / 8 GB shared sandbox at USD 0.028/hour, which would be USD 20.44 at 730 h if it could run that long - it cannot.
- evidence note: The runtime caps, concurrency, included hours and the spot-preemption sentence are quoted from the pricing page read. The unit rates, the card requirement and SSH access are not established.
- extras:
  - keep_rate: 1.0
  - billing_model: per-second
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.note: the shared reference sandbox the page headlines
  - session_cap.wall_clock_min: 45
  - session_cap.restart_required: yes
  - session_cap.note: 45 minutes on Hobby, 24 hours on Pro (USD 49/month)
  - network_out.allow_outbound: yes
  - network_out.ports: not stated on the pricing page
  - free_tier_kind: credit
  - burst_x: 1.0
  - burst_bill: $5e-07 per start
  - term: monthly plan plus usage
  - price_arithmetic: Not computable as a 24/7 figure: the Hobby cap is 45 minutes per sandbox and the Pro cap is 24 hours, so no shape can be held for 730 h. At the headline USD 0.028/hour for 4 vCPU / 8 GB, 730 h would be USD 20.44 if it were purchasable.
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: '$25 in trial credits. No credit card required' with '$0.028/hour', 'Pay for the time a sandbox runs, not a rounded-up hour', '$25 trial ≈ 892 hours' of a '4 vCPU · 8 GB shared sandbox', and 'Explicit CPU, memory, and sandbox lifetime limits', quoted
  - [1] 2026-10-24: quoted: 'Hobby ... Limits ... Max sandbox runtime 45 minutes ... Concurrent sandboxes 10 ... Durable sandboxes Not available'; 'Pro $49/month ... Max sandbox runtime 24 hours'
  - [1] 2026-10-24: quoted: 'Shared sandboxes burst on Spot capacity at the lowest price and can be preempted; dedicated sandboxes get guaranteed CPU and memory, billed on 50% of their size ($0.2984/hour for the same size on Pro).'
  - [1] 2026-11-03: egress overage is USD 0.15 per GB on Hobby and Pro, USD 0.12 on Team | capture: sha256:c2c754f9a3c3edb65fb7e7a00ef76268df0fa7c7ecdbe589e3e5dc414ad3b134 | quote: | Network egress per GB | $0.15 | $0.15 | $0.12 |
  - [1] 2026-11-03: Team includes 1,000 GB of egress | capture: sha256:c2c754f9a3c3edb65fb7e7a00ef76268df0fa7c7ecdbe589e3e5dc414ad3b134 | quote: - 1,000 GB Network egress
  - [3] 2026-11-03: REST API and two SDKs | capture: sha256:9df0e87bc8020fbbf0b4cebba0cbf16fa7c22a9c09996babbf434b1cdfd81793 | quote: Create, execute, and manage sandboxes using the REST API, Node.js SDK, or Python SDK.
- sources:
  - [1] https://sandbox.stateset.app/pricing
  - [2] https://sandbox.stateset.app/
  - [3] https://sandbox.stateset.app/docs/getting-started
