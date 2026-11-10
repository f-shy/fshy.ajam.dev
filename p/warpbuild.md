# WarpBuild

> warpbuild.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/warpbuild/ | JSON https://fshy.ajam.dev/api/v1/entity/warpbuild.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WarpBuild (GitHub Actions runners)

- `compute/warpbuild` | paid-only | evidence documented | binding request-rate | category macOS host
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T02:22:59.202Z (live) | stale on 2026-12-11
- url https://www.warpbuild.com/pricing
- free tier: No free allowance is published: the FAQ says a payment method is added when an account reaches its free usage or credit limits, and no page states the size of that free usage. Hosted Linux x86 runners are USD 0.004 a minute for 2 vCPU and 8 GB and USD 0.008 for 4 vCPU and 16 GB; the ARM64 2 vCPU runner is USD 0.003; BYOC runners are USD 0.002 a minute. | unit: none | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: an email address: "you can sign up with your email and start using WarpBuild immediately. You will be need to add a payment method when you hit the free usage or credit limits"
- interface: unknown
- limits:
  - request-rate (binding): USD 0.004 a minute for a hosted 2 vCPU / 8 GB Linux x86 runner, USD 0.008 for 4 vCPU / 16 GB, and USD 0.002 a minute for BYOC [1]
  - per-object-cap: cache storage is USD 0.20 a GB-month; SAML SSO is USD 250 a month [1]
  - request-rate (binding): no free allowance is published; the FAQ only names a free usage or credit limit that a payment method ends [1]
- limits note: no hard concurrency limit: the page says each builder profile is shared across jobs, and it sells no job cap or queue limit
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The plan grid priced at USD 0.004 a minute for 2 vCPU and USD 0.008 for 4 vCPU on the day it was read, with ARM64 2 vCPU at USD 0.003, cache storage at USD 0.20 a GB-month and BYOC at USD 0.002 a minute. No free allowance is published, so a reader cannot size the free usage the FAQ refers to; the USD 0.003 entry that names 2 vCPU is the ARM64 row, not the x86 one.
- evidence note: The whole plan grid, the BYOC rate and the FAQ identity answer are read from the vendor own pricing page. Raise by signing up with email only and reading the credit or usage limit the dashboard shows.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 8
  - shape.note: the entry runner at $0.003 to $0.004 a minute; the ladder runs to 32 vCPU and 128 GB
  - session_cap.restart_required: no
  - session_cap.note: a runner is allocated per job and billed per minute; no concurrency limit is enforced
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.price: $0.025 an hour per snapshot
  - ps.durability: snapshot
  - ps.on_stop: no
  - ps.on_destroy: no
  - ps.retention: until the snapshot is deleted
  - net.out: yes
  - net.in: yes
  - net.ports: networking is provided via Tailscale
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: a per-minute runner table: '2vCPU, 8GB RAM $0.004', '4vCPU, 16GB RAM $0.008', '32vCPU, 128GB RAM $0.064', a cheaper '2vCPU, 8GB $0.003' tier, Apple Silicon rows at '$0.08' for 6 vCPU and 14 GB, and 'Each builder profile is shared across jobs using that profile. There is no hard concurrency limit.' quoted
  - [1] 2026-11-10: hosted 2 vCPU Linux x86 runners are USD 0.004 a minute | capture: sha256:1090ba0555392e915d690044981cce32f456762095020c56db5512dc82215f51 | quote: 2vCPU, 8GB RAM | $0.004
  - [1] 2026-11-10: hosted 4 vCPU Linux x86 runners are USD 0.008 a minute | capture: sha256:1090ba0555392e915d690044981cce32f456762095020c56db5512dc82215f51 | quote: 4vCPU, 16GB RAM | $0.008
  - [1] 2026-11-10: BYOC runners are USD 0.002 a minute | capture: sha256:1090ba0555392e915d690044981cce32f456762095020c56db5512dc82215f51 | quote: Linux Runners | $0.002/min
  - [1] 2026-11-10: signup needs an email and no card until the free usage limit is reached | capture: sha256:1090ba0555392e915d690044981cce32f456762095020c56db5512dc82215f51 | quote: No, you can sign up with your email and start using WarpBuild immediately.
  - [1] 2026-11-10: the ARM64 2 vCPU runner is USD 0.003 a minute | capture: sha256:1090ba0555392e915d690044981cce32f456762095020c56db5512dc82215f51 | quote: Linux from $0.003/min
- sources:
  - [1] https://www.warpbuild.com/pricing
