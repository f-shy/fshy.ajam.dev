# phoenixNAP dedicated outlet

> phoenixnap.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/phoenixnap/ | JSON https://fshy.ajam.dev/api/v1/entity/phoenixnap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## phoenixNAP dedicated outlet

- `compute/phoenixnap-dedicated-outlet` | paid-only | evidence documented | binding none | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://phoenixnap.com/pncp-usd-esi-all-servers
- free tier: The all-servers price list opens at EUR 89.99 a month for an Intel Xeon E-2186G at 6 cores, 32 GB DDR4 and a 480 GB SSD, and the next rows are EUR 144 for a 4-core E3-1275 v6 with 16 GB. The GPU rows begin at EUR 1,003 for 2 x Xeon Silver 4110 with a Tesla P40 24 GB and EUR 1,259 with a V100 16 GB, both by sales contact rather than self-service. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Nothing states a minimum term, a bandwidth allowance or a setup fee on the list itself. | metered: yes | source: [1]
- identity: card
- interface: unknown
- limits note: Nothing published on this list binds above the scale; the price does. It is roughly three times the OVH SYS-1 for the same core count and RAM.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A GPU row here at EUR 1,003 a month for one P40 is two orders of magnitude past the free and credit lanes in documented records, so the only composition worth noting is that it does not compose.
- reliability: no reliability event recorded
- notes: PhoenixNAP provides dedicated enterprise bare metal servers with custom quote pricing. Entry pricing varies by configuration and term commitments.
- extras:
  - facets.class: refutation
  - facets.shape.cpu: Intel Xeon E-2186G
  - facets.shape.vcpu: 6
  - facets.shape.ram_gib: 32
  - facets.shape.disk: 480 GB SSD
  - facets.shape.price_eur_month: 89.99
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Intel Xeon E-2186G (6x3.8GHz) | 32GB DDR4 | 480GB SSD | EUR 89.99'; 'Intel Xeon E3-1275 v6 (4x3.8GHz) | 16GB DDR4 | 1x1TB SATA III | EUR 144.00'; 'Dual Intel Xeon Silver 4110 (16x2.1GHz) 4-bay | NVIDIA Tesla P40 24GB DDR5 | 64GB DDR4 | 1TB NVMe | 10 Gbps | EUR 1,003.00 | Contact Sales'
  - [2] 2026-10-22: returns HTTP 404, so the pricing path named brief does not exist and the all-servers list is the price source
  - [3] 2026-10-22: a 2015 datasheet still indexed states 'dedicated servers starting at $58/mo' - that figure is eleven years old and does not survive the current price list
- sources:
  - [1] https://phoenixnap.com/pncp-usd-esi-all-servers
  - [2] https://phoenixnap.com/dedicated-servers/pricing
  - [3] https://phoenixnap.com/wp-content/uploads/2015/02/Dedicated-Servers-datasheet.pdf
