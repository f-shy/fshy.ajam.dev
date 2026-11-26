# Sealos DevBox

> sealos.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sealos/ | JSON https://fshy.ajam.dev/api/v1/entity/sealos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sealos DevBox

- `compute/sealos-devbox` | paid-only | evidence documented | binding request-rate | category dev environment
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T11:17:49.025Z (live) | stale on 2026-12-26
- url https://sealos.io/pricing/
- free tier: No free tier: fixed monthly resource packages, with a new-user discount on the first paid plan. The Starter package is the entry point: regular price $34, new user price $7/ month on the first paid plan, with 2 vCPU, 2Gi RAM, 10Gi Disk, 10GB Traffic, 4 NodePorts and 100 AI Credits. There is no USD 0 plan. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: card | detail: a card for the first paid plan: the cheapest entry is USD 7 for the first Starter month, then USD 34 a month; first-paid-plan eligibility is confirmed in Cost Center; no free tier or trial is published. Details of what the signup form asks for are unverified from the pages read.
- interface: unknown
- limits:
  - request-rate (binding): a fixed monthly package rather than metered billing: the entry Starter package is 2 vCPU, 2 GiB RAM, 10 GiB disk and 10 GB traffic; the Hobby package is 4 vCPU, 4 GiB RAM, 20 GiB disk and 50 GB traffic [1]
  - per-object-cap: the package's disk and traffic are the ceilings, and platform credits are spent separately [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Re-read 2026-10-24: the page publishes the package prices now, so the record no longer needs to describe them as unstated. Still no free tier.
- evidence note: the pricing page was read on 2026-10-22 and states fixed monthly packages with the resource mix. There is no free tier, so the verdict moves to paid-only, and the fixed-package model is the opposite of per-second billing
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 4
  - shape.disk: 20
  - shape.note: the page's reference package, including 50 GB of traffic
  - session_cap.restart_required: no
  - session_cap.note: a monthly package with no session clock; the package is the bound
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.gib: 20
  - ps.price: included in the monthly package
  - ps.durability: package disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the billing month
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.allowance: 50 GB of traffic in the reference package
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Choose a fixed monthly resource package' and 'Every plan shows the CPU, memory, storage, traffic, and platform credits included in its monthly price', with 'Includes 4 vCPU, 4Gi RAM, 20Gi disk, and 50GB traffic' and '100 / 300 / 800 AI Credits', quoted
  - [1] 2026-10-24: quoted: 'Starter ... Regular price $34 ... New user price $7/ month ... First paid plan purchase - Eligibility confirmed in Cost Center'
  - [1] 2026-11-25: the Starter plan's regular price, new-user price and first-paid-plan condition are stated | capture: sha256:15f4c1daa8764c405a0f2b25e0409b21150cdb51bcc91a5284dd6ab1cf71730e | quote: Regular price $34 New user price $7/ month First paid plan purchase · Eligibility confirmed in Cost Center
  - [1] 2026-11-24: the first-paid-plan discount and regular price | capture: sha256:15f4c1daa8764c405a0f2b25e0409b21150cdb51bcc91a5284dd6ab1cf71730e | quote: Starter For lightweight experiments and existing container workloads. Regular price $34 New user price $7/ month First paid plan purchase
  - [1] 2026-11-24: the Starter package resources | capture: sha256:15f4c1daa8764c405a0f2b25e0409b21150cdb51bcc91a5284dd6ab1cf71730e | quote: Included resources 2 vCPU 2Gi RAM 10Gi Disk 10GB Traffic 4 NodePorts 100 AI Credits
  - [1] 2026-11-24: the first-paid-plan discount is gated on eligibility in Cost Center | capture: sha256:15f4c1daa8764c405a0f2b25e0409b21150cdb51bcc91a5284dd6ab1cf71730e | quote: First paid plan purchase · Eligibility confirmed in Cost Center
  - [1] 2026-11-24: the Hobby package resources | capture: sha256:15f4c1daa8764c405a0f2b25e0409b21150cdb51bcc91a5284dd6ab1cf71730e | quote: Included resources 4 vCPU 4Gi RAM 20Gi Disk 50GB Traffic 8 NodePorts 300 AI Credits
- sources:
  - [1] https://sealos.io/pricing/
