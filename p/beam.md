# Beam

> beam.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beam/ | JSON https://fshy.ajam.dev/api/v1/entity/beam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Beam

- `compute/beam` | paid-only | evidence documented | binding volume-quota | category container and VM sandbox | tier Developer
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T11:38:10.230Z (live) | stale on 2026-12-25
- url https://www.beam.cloud/pricing
- price parsed USD 22.34/mo
- free tier: No signup credit. 'Developer $20/month $20 in credits each month', and 'Unused monthly credits expire at renewal. Extra credits don't expire.' | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: A plan credit equal to the plan fee. Recording it as a credit would double-count the subscription.
- per-object cap: The smallest persistent VM is $0.06/hr for 1 vCPU at $0.05/hr and 1 GiB RAM at $0.01/hr; sandboxes are also from $0.06/hr. Storage is not billed yet. | source: [1] | note: A stopped VM carries no compute charge, which is what makes the 1 vCPU shape usable for less than a full month.
- retention: A stopped VM keeps its disk and discs RAM and processes; storage is not billed yet, with a planned rate of $0.0001 per GB-hour and no free allowance. The Developer plan retains logs for 30 days. | source: [1]
- egress: 'No. There are no egress or bandwidth fees on any plan.' | metered: no | free allowance: unmetered | source: [1]
- identity: card | detail: The USD 20 credit is bought with a USD 20 monthly subscription, which requires a card. No hold amount is stated. There is no card-free path to the credit.
- interface: ssh, cli, rest
- limits:
  - volume-quota (binding): USD 20 of credits a month on a USD 20 a month plan; unused credits expire at renewal [1]
  - volume-quota (binding): 1 vCPU USD 0.05 an hour and 1 GiB RAM USD 0.01 an hour, so USD 0.06 an hour for the smallest VM [1]
- limits note: The Developer plan includes one seat and 30 concurrent vCPUs; log retention is 30 days.
- binding note: USD 20 against USD 22.34 for a month of the smallest VM is what fails, by USD 2.34, and the credit resets rather than accumulating.
- interface detail: VMs are reached over SSH through an authenticated tunnel with the CLI or a local SSH key, with Python and JavaScript SDKs and an API token for automation; sandboxes and endpoints have HTTP URLs.
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
  - [1] 2026-11-24: the Developer plan costs USD 20 a month and returns USD 20 of credits | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: $20/month$20 in credits each month
  - [1] 2026-11-24: the smallest VM's compute rate is USD 0.06 an hour, billed per second | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: Compute rate$0.06/hr$0.0000167/sec
  - [1] 2026-11-24: storage is currently unbilled and the planned rate is USD 0.0001 per GB-hour with no free allowance | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: Storage is not billed yet. Planned: $0.0001 per GB-hour of data stored, with no free allowance.
  - [1] 2026-11-24: Beam charges no egress or bandwidth fee on any plan | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: No. There are no egress or bandwidth fees on any plan.
  - [2] 2026-11-24: VMs are reached over SSH through an authenticated tunnel | capture: sha256:f9d165c93899df2d1d5b5fe1063878b99ba9735897676fe7d244f4f742685f8b | quote: SSH connects as root through an authenticated Beam tunnel. You do not need to expose an SSH port publicly.
  - [3] 2026-11-24: registration requires a name, a valid email address and billing information where required | capture: sha256:858e42de759953266d2ce71fee1269b2f279bd4448aa9da1ac5aa6e2b8d44802 | quote: 2.1 Registration. You must provide accurate, complete, and current information when you register and keep it up to date, including your name, a valid email address, and billing information where required.
  - [1] 2026-11-24: the Developer plan allows 30 concurrent vCPUs | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: | Concurrent vCPUs | 30 vCPUs | 1,000 vCPUs | Custom |
  - [1] 2026-11-24: the smallest VM's CPU is priced at USD 0.05 an hour on the Performance tier | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: 1 vCPU$0.05
  - [1] 2026-11-24: a GiB of RAM is priced at USD 0.01 an hour | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: 1 GiB RAM$0.01
  - [1] 2026-11-24: sandboxes and VMs both start at USD 0.06 an hour and H100s at USD 3.00 an hour | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: Sandboxes from $0.06/hrVMs from $0.06/hrH100s from $3.00/hr
  - [1] 2026-11-24: a stopped VM carries no compute charge | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: Persistent Linux VMs for agents. Billed per second while running, with no compute charges while stopped.
  - [1] 2026-11-24: log retention is 30 days on the Developer and Team plans | capture: sha256:72e71e3c536be567967a63c664a5f349fc0dc409162d8f129fc18caa2df7eeaa | quote: | Log Retention | 30 Days | 30 Days | 1 Year |
  - [3] 2026-11-24: a plan that incurs fees requires a payment method on file | capture: sha256:858e42de759953266d2ce71fee1269b2f279bd4448aa9da1ac5aa6e2b8d44802 | quote: You must keep a valid payment method on file for any plan that incurs Fees.
- sources:
  - [1] https://www.beam.cloud/pricing
  - [2] https://docs.beam.cloud/v2/vm/processes.md
  - [3] https://docs.beam.cloud/v2/security/terms-and-conditions
