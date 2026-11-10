# Apply.Build

> apply.build | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apply/ | JSON https://fshy.ajam.dev/api/v1/entity/apply.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apply.Build

- `compute/apply-build` | qualifies-with-caveat | evidence documented | binding per-object-cap | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:20:49.284Z (live) | stale on 2026-12-05
- url https://apply.build/
- free tier: 'Free tier: 0.5 vCPU and 512 MiB' and 'No credit card. It stays active when you add paid packages, and after you cancel them.' Paid capacity is sold in packages: 'One package is 1 vCPU, 1 GiB of memory and 10 GB of storage' at 'EUR 5 a month each', split across apps and databases, with per-app sizes from '0.25 vCPU and 256 MiB up to 2 vCPU and 2 GiB' and 'Ephemeral disk per app, 2.5 to 20 GB'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Per-app egress cap by size: Tiny 2.5 MB/s, Small 5 MB/s, Medium 10 MB/s, Large 20 MB/s; ingress uncapped; fair-use terms apply to all traffic. No per-GB egress allowance and no overage price is published: 'There's no usage billing, and traffic spikes don't show up on your invoice.' | metered: no | source: [1]
- identity: email | detail: no card: the pricing page states 'No credit card. It stays active when you add paid packages, and after you cancel them.' No hold exists on the free tier because no payment method is taken. The signup form itself is not quoted in the record, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated; a card appears only when a paid package is bought.
- interface: unknown
- limits:
  - per-object-cap (binding): the free tier is one account-wide ceiling of 0.5 vCPU and 512 MiB, so a second app divides the same half-core and nothing scales past it without a package. [1]
- limits note: the free tier is one account-wide ceiling of 0.5 vCPU and 512 MiB, so a second app divides the same half-core and nothing scales past it without a package.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the cheapest paid step is EUR 1.25 a month for 0.25 vCPU and 256 MiB, so a second always-on small process costs less than a coffee while the free 0.5 vCPU covers the first.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev describes '0.5 vCPUs / 512 MiB RAM, European servers, automatic firewall' and the vendor agrees on the shape, so the gap is small. What the aggregator omits: the free allowance survives cancellation of paid packages, and the paid floor is EUR 1.25 for a quarter of a package. No sleep timer is published for the free tier, which would make it one of the few free PaaS tiers that does not scale to zero.
- extras:
  - facets.class: floor-price
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 0.5
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: 'Free tier: 0.5 vCPU and 512 MiB' and 'No credit card. It stays active when you add paid packages, and after you cancel them.', quoted
  - [1] 2026-10-22: 'You buy resource packages at EUR 5 a month each. One package is 1 vCPU, 1 GiB of memory and 10 GB of storage', with a worked bill line 'Tiny - 0.25 vCPU, 256 MiB - EUR 1.25', quoted
  - [1] 2026-10-22: 'Each app gets its own micro-VM' and the per-app range '0.25 vCPU and 256 MiB up to 2 vCPU and 2 GiB per app', quoted
  - [2] 2026-11-04: the pricing page states fair-use terms for all traffic and no fixed cap on incoming traffic | capture: sha256:abeab97501c06c022a38c3d141e91a20045c37f3c10ef09c5a20cd21281b225b | quote: Incoming traffic has no fixed cap; fair-use terms apply to all traffic.
  - [2] 2026-11-04: per-size egress rate cap listed under the app size on the pricing page | capture: sha256:abeab97501c06c022a38c3d141e91a20045c37f3c10ef09c5a20cd21281b225b | quote: 2.5 MB/s egress
  - [2] 2026-11-04: per-size egress rate cap listed under the app size on the pricing page | capture: sha256:abeab97501c06c022a38c3d141e91a20045c37f3c10ef09c5a20cd21281b225b | quote: 5 MB/s egress
  - [2] 2026-11-04: per-size egress rate cap listed under the app size on the pricing page | capture: sha256:abeab97501c06c022a38c3d141e91a20045c37f3c10ef09c5a20cd21281b225b | quote: 10 MB/s egress
  - [2] 2026-11-04: per-size egress rate cap listed under the app size on the pricing page | capture: sha256:abeab97501c06c022a38c3d141e91a20045c37f3c10ef09c5a20cd21281b225b | quote: 20 MB/s egress
  - [1] 2026-11-04: no usage billing, so no per-GB overage price is published | capture: sha256:e8aa9e1275a6e0156e82238c10de7099240c5a5f0f07b6b6c73f7743bc8217c0 | quote: There's no usage billing, and traffic spikes don't show up on your invoice.
- sources:
  - [1] https://apply.build/
  - [2] https://apply.build/pricing
