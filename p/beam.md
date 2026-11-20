# Beam

> beam.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beam/ | JSON https://fshy.ajam.dev/api/v1/entity/beam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Beam

- `compute/beam` | paid-only | evidence documented | binding volume-quota | category container and VM sandbox | tier Developer
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T03:25:00.000Z (live) | stale on 2026-11-24
- url https://www.beam.cloud/pricing
- price parsed USD 22.34/mo
- free tier: No signup credit. 'Developer $20/month $20 in credits each month', and 'Unused monthly credits expire at renewal. Extra credits don't expire.' | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: A plan credit equal to the plan fee. Recording it as a credit would double-count the subscription.
- per-object cap: A persistent VM is 'from $0.0306/hr' for '1 vCPU / 1 GiB / 50 GiB root disk' ('1 vCPU $0.0252' plus '1 GiB RAM $0.0054'). Sandboxes are 'from $0.319/hr'. | source: [1] | note: A stopped VM carries no compute charge, which is what makes the 1 vCPU shape usable for less than a full month.
- retention: A stopped VM keeps its root disk; the page prices storage separately at '$0.021 per GB / month'. No deletion timer is stated. | source: [1]
- egress: 'Egress & bandwidth | Free'. | metered: no | free allowance: unmetered | source: [1]
- identity: card | detail: The USD 20 credit is bought with a USD 20 monthly subscription, which requires a card. No hold amount is stated. There is no card-free path to the credit.
- interface: unknown
- limits:
  - volume-quota (binding): USD 20 of credits a month on a USD 20 a month plan; unused credits expire at renewal [1]
  - volume-quota (binding): 1 vCPU USD 0.0252 an hour and 1 GiB USD 0.0054 an hour, so USD 0.0306 an hour for the smallest VM [1]
- limits note: The Developer plan includes one seat; extra seats are USD 25 each on Team.
- binding note: USD 20 against USD 22.34 for a month of the smallest VM is what fails, by USD 2.34, and the credit resets rather than accumulating.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: Stopped VMs keep billing for their root disk and volumes, so a 'stopped' VM is not a free VM.
- notes: Beam appears in credit tables as a USD 20 plan credit and should not: the money and the subscription are the same USD 20, so the row is 'pay USD 20, get USD 20 of VM time'. At USD 0.0306 an hour that is 653 hours, 89% of a month, and the remaining 77 hours cost USD 2.34 out of pocket.
- evidence note: The plan credit, its expiry rule, the VM and sandbox rates and the stopped-VM behaviour are on the pricing page read.
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: cores ( 4 vCPU) and 16 GiB RAM costs $1.77 /hr ( $0.69 GPU + $0.76 CPU + $0.32 RAM , at the GPU-attached rates
  - billing_model: per-second while running
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 50
  - session_cap.restart_required: no
  - session_cap.note: a VM runs until stopped; a stopped VM bills disk only
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: HTTP endpoints and exposed ports
  - free_tier_kind: plan-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 50
  - ps.price: included in the VM rate
  - ps.durability: root disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the VM exists
  - term: monthly
  - m10h_usd: 9.18
  - m24h_usd: 22.34
  - price_arithmetic: 0.0252 + 0.0054 = 0.0306/h; x 730 = 22.34; 20 / 0.0306 = 653.6 h
  - credit_usd: 20
  - credit_months_at_shape: 0.9
  - credit_hours_at_shape: 653.6
  - credit_expiry: monthly; unused credits expire at renewal, purchased credits do not
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Persistent Linux VMs for agents. Billed per second while running, with no compute charges while stopped.' and '1 vCPU $0.0252, 1 GiB RAM $0.0054, 50 GiB root disk Included, Rate $0.0306/hr' and 'Sandboxes from $0.319/hr', quoted
  - [1] 2026-10-24: quoted: 'Developer $20/month $20 in credits each month'; 'Unused monthly credits expire at renewal. Extra credits don't expire.'; '1 vCPU $0.0252', '1 GiB RAM $0.0054', 'Rate $0.0306/hr' for the VM; 'Sandboxes from $0.319/hr'; 'Egress & bandwidth | Free'.
  - [1] 2026-10-24: quoted: 'Developer $20/month $20 in credits each month', 'Unused monthly credits expire at renewal', and the VM rate 'VMs from $0.0306/hr' for '1 vCPU / 1 GiB RAM / 50 GiB root disk'
- sources:
  - [1] https://www.beam.cloud/pricing
