# Wholesale Internet

> wholesaleinternet.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wholesaleinternet/ | JSON https://fshy.ajam.dev/api/v1/entity/wholesaleinternet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wholesale Internet

- `compute/wholesale-internet` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.wholesaleinternet.net/dedicated/
- free tier: Preconfigured dedicated servers with free setup, listed monthly: a Core 2 Duo at 2 cores / 2 threads with 4 GB DDR2, a 250 GB SATA disk, 100 Mbit unmetered and 1 usable IPv4 for USD 9.00 a month, and an i7-2600 at 4 cores / 8 threads with 16 GB DDR3, 1 TB SATA, 1 Gbit unmetered and 5 usable IPv4 for USD 25.00. The top of the list is a Dual Xeon E5-2696v3 at 36 cores / 72 threads with 128 GB DDR4 and 2 x 4 TB SSD for USD 199.00, also with free setup and 1 Gbit unmetered. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: This is the lowest published monthly price documented for a whole machine, and it is a 2007-era Core 2 Duo with DDR2, so the comparison this category asks for is unforgiving: documented records prices Hetzner Cloud CX23 at USD 6.49 with 20 TB of egress included, so USD 9 buys 33 percent more money and nothing more that a compute-bound job wants. | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): The port speed is the ceiling on the USD 9 machine at 100 Mbit; on every machine from USD 25 up it is 1 Gbit, and the hardware generation binds before the network does. [1]
- limits note: The port speed is the ceiling on the USD 9 machine at 100 Mbit; on every machine from USD 25 up it is 1 Gbit, and the hardware generation binds before the network does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A USD 9 whole machine with 5 usable IPv4 addresses on the USD 25 tier is the cheapest place among documented hosts to terminate a set of outbound connections that need distinct source addresses, and it composes with a cheap bulk-storage host for the data it collects.
- reliability: no reliability event recorded
- notes: The USD 25 i7-2600 tier is the first row where a dedicated box beats a VPS on raw threads per dollar. The USD 199 36-core tier is USD 0.114 per thread-month, which is the number worth carrying to a scheduling decision. Nothing on the page states a minimum term, a power allowance or an IPMI policy, and those three remain unestablished.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: Intel Core 2 Duo
  - facets.shape.vcpu: 2
  - facets.shape.threads: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk: 250 GB SATA
  - facets.shape.bandwidth_mbit: 100
  - facets.shape.traffic: unmetered
  - facets.shape.price_usd_month: 9.0
  - facets.shape.setup_fee_usd: 0
  - facets.shape.ipv4_included: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Intel Core 2 Duo Preconfigured 1.6GHz or faster - 1 processor 2 Cores / 2 Threads | 4GB DDR2 | 250GB SATA | 100mbit Unmetered | 1 usable IPv4 Address | $9.00/month | FREE Setup'
  - [1] 2026-10-22: 'I7-2600 Preconfigured 2.8 GHz / 3.8 Turbo - 1 processor 4 cores / 8 threads | 16GB DDR3 | 1TB SATA | 1Gbit unmetered | 5 usable IPv4 Address | $25.00/month | FREE Setup'
  - [1] 2026-10-22: 'Dual Xeon E5-2696v3 128GB 2x4TB SSD Preconfig 2.30GHz / 3.6GHz Turbo 36 Cores / 72 threads | 128GB DDR4 | 2x 4TB SSD | 1Gbit unmetered | $199.00/month | FREE Setup'
  - [1] 2026-10-22: 'i7-8700K 32GB RAM 1TB NVME Preconfig 3.7GHz / 4.7GHz Turbo 6 Cores / 12 Threads | 32GB DDR4 | 1TB NVME | 1Gbit unmetered | $59.00/month'
- sources:
  - [1] https://www.wholesaleinternet.net/dedicated/
