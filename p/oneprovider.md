# OneProvider

> oneprovider.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oneprovider/ | JSON https://fshy.ajam.dev/api/v1/entity/oneprovider.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OneProvider

- `compute/oneprovider` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:03:44.965Z (live) | stale on 2026-12-26
- url https://oneprovider.com/en/dedicated-servers/paris-france
- free tier: €11.99 €7.49 | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: row reads 'Atom C2350 1.7 GHz 2c/2t Benchmark: 523', '4 GB DDR3', '1 x 1 TB (HDD SATA)', '1 Gbps Unmetered Fair Usage Bandwidth', 'EUR 11.99 EUR 7.49', 'Setup Fee: EUR 4.99 EUR 0.00', stock 'Limited' | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): 'Fair Usage Bandwidth' is a discretionary throttle with no published rate: the port is 1 Gbps and nothing states when the fair-use clause is applied. [1]
- limits note: 'Fair Usage Bandwidth' is a discretionary throttle with no published rate: the port is 1 Gbps and nothing states when the fair-use clause is applied.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A EUR 8 to 12 whole machine with a 1 TB disk is the cheapest place to put a job that must run on real hardware, and it pairs with object storage for anything past the single disk.
- reliability: no reliability event recorded
- notes: OneProvider offers dedicated servers across global datacenters, with clearance pricing published per location. Specifications and setup fee waivers vary by region and stock.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: Intel Atom C2350
  - facets.shape.vcpu: 2
  - facets.shape.threads: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk: 1 x 1 TB SATA HDD
  - facets.shape.bandwidth_mbit: 1000
  - facets.shape.traffic: unmetered, fair usage
  - facets.shape.price_eur_month: 11.99
  - facets.shape.price_eur_month_clearance: 7.49
  - facets.shape.setup_fee_eur: 4.99
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: row reads 'Atom C2350 1.7 GHz 2c/2t Benchmark: 523', '4 GB DDR3', '1 x 1 TB (HDD SATA)', '1 Gbps Unmetered Fair Usage Bandwidth', 'EUR 11.99 EUR 7.49', 'Setup Fee: EUR 4.99 EUR 0.00', stock 'Limited'
  - [1] 2026-10-22: row reads 'Xeon E3-1220 3.1 GHz 4c/4t', '16 GB DDR3', '2 x 2 TB HDD SATA', '1 Gbps Unmetered Fair Usage Bandwidth', 'EUR 34.99 EUR 15.99', setup 'EUR 10.00 EUR 0.00'
  - [2] 2026-10-22: 'See all of our 140+ datacenter locations in the world and browse one of your 1500+ server configurations' - the operator resells hardware in 140 locations rather than owning it
  - [1] 2026-11-25: the Paris page lists the Atom C2350 server at EUR 11.99 and EUR 7.49 in its price column | capture: sha256:8f4020ad58caf31951f30077735278c67d374d1d5274e553dc35704f2612e6b2 | quote: €11.99 €7.49
  - [1] 2026-11-25: the Paris page still lists the Atom C2350 server at EUR 11.99 and EUR 7.49 | capture: sha256:8f4020ad58caf31951f30077735278c67d374d1d5274e553dc35704f2612e6b2 | quote: €11.99 €7.49
- sources:
  - [1] https://oneprovider.com/en/dedicated-servers/paris-france
  - [2] https://oneprovider.com/dedicated-servers
