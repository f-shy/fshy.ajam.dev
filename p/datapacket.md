# DataPacket

> datapacket.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datapacket/ | JSON https://fshy.ajam.dev/api/v1/entity/datapacket.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataPacket

- `compute/datapacket` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.datapacket.com/dedicated-servers
- free tier: The entry configuration is an AMD EPYC 4245P at 6 cores / 12 threads, 3.9 GHz with 5.4 GHz turbo, 32 MB L3, advertised at 'Starting at $240/mo' with 2,425 servers in stock and one-day delivery. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no byte allowance: bandwidth is a 95th-percentile commitment against the access port, priced by commit rather than per TB | metered: yes | source: [1]
- identity: card | detail: Unverified: no page stating the signup requirement was read; the record's evidence covers the USD 240 entry configuration, the configurator, the live stock counter and the terms — monthly payment "prepaid in full before the start of the respective month", no setup or activation fee, thirty days' written notice. And names no card, email, phone or ID document and no hold. The only identity-adjacent fact is that the monthly plan is prepaid, which establishes a payment relationship without naming the rail.
- interface: unknown
- limits note: No published limit binds above the scale; the entry price does, at eight times the OVH SYS-1 for the same core count.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: One day delivery in nineteen locations is what the price buys here; it is worth nothing when there is no deadline.
- reliability: no reliability event recorded
- notes: A third-party comparison page attributed a USD 14.99 i3/i5 plan on a one-year term to DataPacket; that row does not match this vendor and was not copied. The vendor's own two pages agree on USD 240, which is the figure recorded. The stock count is a live counter: an earlier read recorded 2,425 units and this one 2,397, so it is not a fixed catalogue size. A third-party comparison page attributed a USD 14.99 i3/i5 plan on a one-year term to this vendor; that row does not match the vendor's pages and was not copied. No setup fee is published, and the term runs month to month with 30 days' notice.
- extras:
  - facets.class: refutation
  - facets.shape.cpu: AMD EPYC 4245P
  - facets.shape.vcpu: 6
  - facets.shape.threads: 12
  - facets.shape.price_usd_month: 240
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: '2,425 servers in stock', '1 day server delivery', 'Entry level AMD EPYC 4245P Essential server CPU for general workloads and small-scale applications. Starting at $240/mo'
  - [2] 2026-10-22: 'AMD EPYC 4245P 6 Cores, 12 Threads, 3.9 GHz (5.4 GHz turbo)', 'From $240 /mo'
  - [3] 2026-10-22: the configurator renders locations and delivery windows (Ashburn, Atlanta, Chicago and others in 4 hours; Dallas in 14 days) with no price in the text, which is why the price is taken from the two pages above
  - [1] 2026-10-22: entry card: AMD EPYC 4245P 6 Cores, 12 Threads, 3.9 GHz with CPU Mark: 31,135 and Essential server CPU for general workloads and small-scale applications. Starting at $240/mo
  - [1] 2026-10-22: 2,397 servers in stock, 1 day server delivery, Unshared 50-200 Gbps uplink per server, 99.99%+ SLA, and 67 data centers worldwide
  - [4] 2026-10-22: with CPU 1~1imump1 selected the configurator lists base RAM 32 GB and base 2 x 480 GB SSD with no surcharge, then RAM 64 GB +$95, 128 GB +$285, and storage 2 x 1.92 TB NVMe +$104, and closes with Delivery in 4 hours - New York and $240/month
  - [4] 2026-10-22: the page's embedded catalogue entry id 1~1imump1|32|SSD~480~2| carries generalPrice 240, memory 32, storageId SSD~480~2|, stockCount 98, and per-location uplinkCapacities of 50 Gbps at Ashburn, Calgary, Chicago, Houston, McAllen, Miami, Montreal and New York, 20 at Atlanta, 25 on 6 Boston units and 50 on 3, 10 on 2 Los Angeles units and 50 on 3, and 10 on 1 Vancouver unit and 50 on 6
  - [2] 2026-10-22: AMD EPYC 4245P 6 Cores, 12 Threads, 3.9 GHz, 32 MB L3 Cache, From $240 /mo, and the paired memory part list Crucial/Micron 32 GB DDR5 4,800 MHz
  - [5] 2026-10-22: The initial service term of this Agreement shall begin on the Effective Date, and shall continue indefinitely unless terminated in accordance with the terms of this Agreement.
  - [5] 2026-10-22: All Monthly Plan payments must be prepaid in full before the start of the respective month of Services. The Service Period is the initial thirty (30) consecutive-day period commencing on the Service Activation Date, then calendar months
  - [5] 2026-10-22: no setup or activation fee is named anywhere in the terms read; the only one-off charge is the Supplier's reasonable reinstatement fee if service is reinstituted following a suspension of service
  - [5] 2026-10-22: Access-port capacity (e.g., 40 G/100 G/400 G) must be commensurate with the Customer's 95th-percentile bandwidth commitment.
  - [5] 2026-10-22: The Customer may terminate this Agreement by giving at least 30 days written notice, provided that such notice must expire at the end of the then-current billing period.
- sources:
  - [1] https://www.datapacket.com/dedicated-servers
  - [2] https://www.datapacket.com/hardware/epyc-4245p
  - [3] https://www.datapacket.com/server-configuration
  - [4] https://www.datapacket.com/server-configuration?region=north-america&location=new-york&cpu=1%7E1imump1
  - [5] https://www.datapacket.com/terms-and-conditions
