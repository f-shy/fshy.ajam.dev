# HostNoc

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostnoc/ | JSON https://fshy.ajam.dev/api/v1/entity/hostnoc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostNoc

- `compute/hostnoc` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://lowendtalk.com/discussion/221867/additional-10-off-first-month-promo-code-let10-dedicated-servers-from-24-95-mo
- free tier: Six dedicated machines under USD 100, each on a 1 Gbps unmetered port with full root, a dedicated IP and DDoS protection: an Intel Xeon E3-1230 v2 at 4 cores / 8 threads with 16 GB DDR3 and a 1 TB HDD in Los Angeles at USD 24.95 a month recurring; an Intel Xeon L3426 at 4 cores / 8 threads with 16 GB and 2 x 2 TB in Paris at USD 25.72; an i7-4790K at 4 cores / 8 threads with 32 GB and 2 x 1 TB in Dusseldorf at USD 39.95; an E3-1245 v2 with 32 GB DDR4 and 2 x 480 GB SSD in Montreal at USD 54.99; and a Xeon D-1521 with 16 GB, a 512 GB NVMe and 4 x 4 TB in Montreal. The vendor states the recurring price does not jump after the first month. | unit: GiB | metered on: wall-clock | read on: 2026-10-08 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): The 1 Gbps port is the ceiling and the traffic claim is unmetered with no published fair-use rate, so the throttle is discretionary rather than a stated quota. [1]
- limits note: The 1 Gbps port is the ceiling and the traffic claim is unmetered with no published fair-use rate, so the throttle is discretionary rather than a stated quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A Paris machine at USD 25.72 with a 1 Gbps unmetered port and 4 TB of disk is the cheapest European dedicated entry found among evaluated providers, and it pairs with the OVH or Hetzner object storage that charges per byte rather than per port.
- reliability: no reliability event recorded
- notes: The CPU of the entry machine is a 2012 Ivy Bridge part, so per-thread throughput is about a third of a current Ryzen, which is the comparison brief asks for and the reason the OVH SYS-1 at EUR 29.99 is a better compute buy at a similar price.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: Intel Xeon E3-1230 v2
  - facets.shape.vcpu: 4
  - facets.shape.threads: 8
  - facets.shape.ram_gib: 16
  - facets.shape.disk: 1 x 1 TB HDD SATA
  - facets.shape.bandwidth_mbit: 1000
  - facets.shape.traffic: unmetered
  - facets.shape.price_usd_month: 24.95
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 
  - [1] 2026-10-22: 
  - [1] 2026-10-22: 
- sources:
  - [1] https://lowendtalk.com/discussion/221867/additional-10-off-first-month-promo-code-let10-dedicated-servers-from-24-95-mo
