# OVHcloud Rise

> ovh.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ovh/ | JSON https://fshy.ajam.dev/api/v1/entity/ovh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OVHcloud Rise

- `compute/ovhcloud-rise` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T05:18:21.037Z (live) | stale on 2026-12-26
- url https://eu.api.ovh.com/1.0/order/catalog/public/eco?ovhSubsidiary=IE
- free tier: The catalogue lists RISE-LE-1 (planCode 27risele01-v1) at EUR 34.99 a month on a 1 Gbps bandwidth option, with a 12-month total of EUR 398.89 and a EUR 0.00 installation fee on that term. RISE-1 is EUR 56.99 a month and EUR 649.69 for 12 months; RISE-2 and RISE-S are EUR 64.99 a month each. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: RISE-1 addon families offer memory ram-32g, ram-64g and ram-128g ECC, storage from softraid-2x512nvme to softraid-2x3840nvme, and bandwidth 'bandwidth-1000-unguaranteed-rise-gen2'; RISE-2 offers 'bandwidth-1000-rise-gen2', 'bandwidth-2000-rise-gen2' and 'bandwidth-3000-rise-gen2'; RISE-S carries a single 64 GB DDR5 on-die ECC 3600 option and 2x512 NVMe | metered: yes | source: [1]
- identity: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): On RISE-1 the 1 Gbps port is catalogued as unguaranteed; RISE-2 is the first model where 1, 2 or 3 Gbps can be bought as a guaranteed rate. [1]
- limits note: On RISE-1 the 1 Gbps port is catalogued as unguaranteed; RISE-2 is the first model where 1, 2 or 3 Gbps can be bought as a guaranteed rate.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A Ryzen 7 9700X with 64 GB of DDR5 for EUR 64.99 a month is the newest single-socket hardware found at this price in this category, and its 12-month term at no installation fee makes it a cheaper yearly commitment than the kimsufi range that is currently sold out.
- reliability: no reliability event recorded
- notes: It also corrects a reading that the whole OVH eco catalogue is exhausted: nineteen of twenty-six KS plan codes are unavailable on this date and the surviving stock is Asia-Pacific and North American, while RISE-1 is available in seven European and North American datacenters. The installation fee is the part a price comparison usually drops: on monthly billing RISE-1 costs EUR 113.98 in the first month and EUR 56.99 after, so a two-month trial costs twice the headline. Traffic is null because the catalogue carries a port rate and no volume term, and the OVH dedicated pages did not restate an unlimited allowance for this range.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: Intel Xeon-E 2386G
  - facets.shape.vcpu: 6
  - facets.shape.threads: 12
  - facets.shape.ram_gib: 32
  - facets.shape.disk: 2 x 512 GB NVMe
  - facets.shape.bandwidth_mbit: 1000
  - facets.shape.price_eur_month: 56.99
  - facets.shape.price_eur_month_12m: 54.14
  - facets.shape.setup_fee_eur: 56.99
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: planCode 24rise01-v2 'RISE-1 | Intel Xeon-E 2386G' at 56.99 EUR a month with a phase-0 one-time charge of 56.99 and a 12-month total of 649.69; 24rise02-v2 'RISE-2 | Intel Xeon-E 2388G' at 64.99; 25rises01-v2 'RISE-S | AMD Ryzen 7 9700X' at 64.99 with a 12-month total of 740.89
  - [1] 2026-10-22: RISE-1 addon families offer memory ram-32g, ram-64g and ram-128g ECC, storage from softraid-2x512nvme to softraid-2x3840nvme, and bandwidth 'bandwidth-1000-unguaranteed-rise-gen2'; RISE-2 offers 'bandwidth-1000-rise-gen2', 'bandwidth-2000-rise-gen2' and 'bandwidth-3000-rise-gen2'; RISE-S carries a single 64 GB DDR5 on-die ECC 3600 option and 2x512 NVMe
  - [2] 2026-10-22: RISE-1 returns 1H-high or 1H-low stock at bhs, fra, gra, lon, rbx, sbg and waw, with 72H windows at most of them; RISE-S returns gra=1H-high and rbx=1H-high plus bhs=1H-low
  - [1] 2026-11-25: the catalogue names RISE-LE-1 and gives the RISE-LE-1, RISE-1 and 12-month rental prices | capture: sha256:4226f41c3ced38bffc0d1b5ab007ffc2b437bea4002c37a8bc1347b932e41e89 | quote: "planCode": "27risele01-v1", "invoiceName": "RISE-LE-1" ... "formattedPrice": "€ 34.99" ... "formattedPrice": "€ 398.89" ... "planCode": "24rise01-v2" ... "formattedPrice": "€ 56.99" ... "formattedPrice": "€ 649.69"
  - [1] 2026-11-25: the catalogue still names RISE-LE-1 and states its monthly and 12-month prices | capture: sha256:4226f41c3ced38bffc0d1b5ab007ffc2b437bea4002c37a8bc1347b932e41e89 | quote: "planCode": "27risele01-v1", "invoiceName": "RISE-LE-1" ... "formattedPrice": "€ 34.99" ... "formattedPrice": "€ 398.89"
- sources:
  - [1] https://eu.api.ovh.com/1.0/order/catalog/public/eco?ovhSubsidiary=IE
  - [2] https://eu.api.ovh.com/1.0/dedicated/server/datacenter/availabilities?planCode=24rise01-v2
