# Posit Cloud

> posit.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/posit/ | JSON https://fshy.ajam.dev/api/v1/entity/posit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Posit Cloud

- `compute/posit-cloud-free` | qualifies-with-caveat | evidence documented | binding volume-quota | category notebook runtime | tier Cloud Free
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://posit.cloud/plans
- free tier: USD 0 forever: 25 compute hours a month, 1 GB maximum RAM, 1 CPU, 1 hour maximum execution, 25 projects and 3 concurrent projects | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: The only provider among documented hosts that publishes a monthly compute-hour counter.
- per-object cap: not applicable: the unit is a session, not an object
- retention: 25 projects persist on the free plan; the pricing page states no expiry | source: [1]
- egress: no egress allowance or price published | metered: no | source: [1]
- identity: email | detail: a Posit Cloud account; the plans page states no card for Cloud Free
- interface: rest, cli
- limits:
  - volume-quota (binding): 25 compute hours per month, then the plan stops [1]
  - volume-quota (binding): 1 hour maximum execution per run [1]
- binding note: 25 hours a month is four hours a week, and the 1-hour execution cap means no single job can use even one day of it
- interface detail: RStudio and Jupyter projects in a browser
- tooling: the web IDE; project files and a console
- composes with: 25 hours a month of 1 GB R or Python for small scripted jobs, capped at one hour per execution
- reliability: no reliability event recorded
- notes: 1 GB RAM is the smallest shape among documented hosts. The 1-hour execution cap rules it out for anything long, and 25 hours a month is the tightest published allowance after Binder.
- evidence note: every number is from the vendor's plan table read. Nothing was run, so enforcement is unproven.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00 on Cloud Free; the paid Basic tier is USD 25 a month for 150 hours and 8 GB
  - free_tier_kind: free-forever-with-quota
  - unattended: no
  - unattended_mechanism: unverified: no scheduler is described on the plans page, and the 1-hour execution cap bounds any run
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: 1 hour maximum execution on Cloud Free
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted: '| Compute Hours | 25 hours per month |' for Cloud Free
  - [1] 2026-10-24: quoted from the plan row, Free column first: '| Max RAM | 1 GB | 8 GB | 32 GB | 16 GB | 1 GB |' and '| Max CPU | 1 CPU | 2 CPUs | 8 CPUs | 4 CPUs | 1 CPU |'
  - [1] 2026-10-24: quoted: '| Max Execution | 1 hour |' for Cloud Free
  - [1] 2026-10-24: quoted from the plan rows, Free column first: '| Projects | 25 | Unlimited | Unlimited | Unlimited | 25 |' and '| Concurrent Projects | 3 | Unlimited | Unlimited | Unlimited | 3 |'; the Free column header reads '$0 / forever'
- sources:
  - [1] https://posit.cloud/plans
