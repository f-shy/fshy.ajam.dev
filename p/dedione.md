# DediOne

> dedione.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dedione/ | JSON https://fshy.ajam.dev/api/v1/entity/dedione.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DediOne

- `compute/dedione` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:03:40.580Z (live) | stale on 2026-12-26
- url https://dedione.com/store/los-angeles-kvm-vps-global
- free tier: LAX.VPS.INTL.2C1G20G $3.99 USD Monthly - 2 CPU vCores - 1GB RAM - 20GB SSD Storage - 1TB Monthly Transfer - 1Gbps Port Speed - 1 IPv4 + 2 IPv6 | unit: GB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The order flow was not entered, so the payment and identity fields are not established. The vendor also runs lotteries that give a free machine for a year with a stated renewal at USD 12.99, which is a promotional route rather than an account tier.
- interface: unknown
- limits:
  - volume-quota (binding): The 1 TB monthly transfer at 1 Gbps is the binding term: sustained full-port traffic would exhaust it in about 2.2 hours, so the shape is a service box rather than a transfer engine. The China-optimised variant of the same 2 vCPU / 1 GiB shape costs USD 7.99, double. [1]
- limits note: The 1 TB monthly transfer at 1 Gbps is the binding term: sustained full-port traffic would exhaust it in about 2.2 hours, so the shape is a service box rather than a transfer engine. The China-optimised variant of the same 2 vCPU / 1 GiB shape costs USD 7.99, double.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 3.99 is below the usual floor for a 2 vCPU machine with a dedicated IPv4, and it composes with free egress via a CDN in front, which removes the 1 TB cap from the serving path.
- reliability: no reliability event recorded
- notes: New to earlier readings. This is evaluated offerings's cheapest monthly dedicated-IPv4 machine that is documented on the vendor's own order page, and the China-optimised twin at double the price is the honest comparison for a mainland audience. Whether the USD 12.99 annual plan still exists on 2026-10-22 is not established: the forum post that states it is from 2025 and the current store shows monthly terms only.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: order page lists LAX.VPS.INTL.2C1G20G at $3.99 USD monthly with 2 CPU, 1GB RAM, 20GB SSD, 1TB transfer, 1Gbps port, 1 IPv4 plus 2 IPv6, quoted
  - [2] 2026-10-22: the China Direct Optimized page sells the same 2 vCPU / 1 GiB / 20 GB shape at $7.99 USD monthly on AS4134, AS4837 and AS58453, quoted
  - [3] 2026-10-22: the vendor's own lottery post states the free machine renews at $12.99/yr and that an unrenewed machine is suspended two days after expiry and deleted three days after
  - [1] 2026-11-25: the order page lists the LAX.VPS.INTL.2C1G20G plan at $3.99 USD Monthly with 2 CPU, 1GB RAM, 20GB SSD, 1TB transfer, 1Gbps port and 1 IPv4 plus 2 IPv6 | capture: sha256:04c94b2fa9b18c3b52b1d57fa76a83770b6830519a987a40e50fbe26c309aee0 | quote: LAX.VPS.INTL.2C1G20G $3.99 USD Monthly - 2 CPU vCores - 1GB RAM - 20GB SSD Storage - 1TB Monthly Transfer - 1Gbps Port Speed - 1 IPv4 + 2 IPv6
  - [1] 2026-11-25: the order page prints the disk size as 20GB, a decimal unit | capture: sha256:04c94b2fa9b18c3b52b1d57fa76a83770b6830519a987a40e50fbe26c309aee0 | quote: - 20GB SSD Storage
- sources:
  - [1] https://dedione.com/store/los-angeles-kvm-vps-global
  - [2] https://dedione.com/store/los-angeles-kvm-vps-cn
  - [3] https://www.nodeseek.com/post-473404-58
