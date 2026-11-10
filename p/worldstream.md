# Worldstream

> worldstream.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/worldstream/ | JSON https://fshy.ajam.dev/api/v1/entity/worldstream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Worldstream

- `compute/worldstream` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.worldstream.com/en/dedicated-servers
- free tier: The cheapest of the 43 entries in the vendor's own offer list: a Fujitsu PRIMERGY RX1330 M3 with an Intel Xeon E3-1230v6 at 4 cores / 8 threads and 3.50 GHz, 16 GB RAM, 1 x 250 GB SSD and a 1 Gbit/s full-duplex port, at EUR 49.00 a month with 50 TB of traffic included and delivery within 2 hours. No setup fee. The banner figure of EUR 104 is the EPYC 4000 series, not the entry point. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 50 TB a month included on the EUR 49 shape; 100 TB is EUR 50 a month more, and unmetered is EUR 99 a month more | metered: yes | free allowance: 50 TB per month on the EUR 49 entry shape | source: [1]
- identity: card | detail: unverified: no page stating the signup requirement was read; the record's evidence covers the dedicated-server prices, the 50 TB traffic inclusion on the EUR 49 entry shape, and the monthly, three-month, six-month, annual and two-year payment-term options, and states nothing about a payment method, an email, a phone or an ID document. The terms page returned 404, so no minimum-term clause was read either
- interface: unknown
- limits:
  - volume-quota (binding): 50 TB a month included on the EUR 49 entry shape [2]
- limits note: No quota binds above the scale on the page; the monthly price does. EUR 104 for a 6-core machine is three and a half times the OVH SYS-1 at EUR 29.99 for the same core count.
- binding note: the EUR 49 shape includes 50 TB a month, and traffic past it is priced at EUR 50 per additional 50 TB
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Its 10 Tbit/s network claim is the only thing that separates it from a EUR 30 machine elsewhere, and a client moving a few terabytes a month cannot use that difference.
- reliability: no reliability event recorded
- notes: The landing banner quotes EUR 104 for the EPYC 4000 series, which is not the cheapest server in the vendor's own offer list; the Xeon E3 entry at EUR 49 is, and its full specification is on /configure/110. The offer list is client-rendered, so only the raw HTML carries it, and the schema.org block on /configure/110 is stale: it still describes the EPYC 4245P at EUR 135 from /configure/156. Prices are EUR with no USD figure published, so no conversion was invented. Unstated rather than absent: the minimum-term clause, because /en/terms-and-conditions returned 404.
- extras:
  - facets.class: refutation
  - facets.shape.cpu: AMD EPYC 4245P
  - facets.shape.vcpu: 6
  - facets.shape.threads: 12
  - facets.shape.price_eur_month: 104
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'AMD EPYC 4000-serie Powerful single-socket performance - Available from 6 cores @ 3.90GHz (4245P) to 12 cores @ 3.40GHz (4465P). From EUR 104 per month. Instantly available. Live within 2 hours'
  - [1] 2026-10-22: 'Worldstream is a Dutch Cloud Infrastructure Provider. With our own data centers, dedicated servers, 10Tbit/s+ network ... at a fixed monthly price'
  - [1] 2026-10-22: Available from 6 cores @ 3.90GHz (4245P) to 12 cores @ 3.40GHz (4465P). From EUR 104 per month. The page prints the euro sign; it is written EUR here.
  - [1] 2026-10-22: Pre-configured Instant Delivery Servers (live within 2 hours), Custom servers, fully configurable (live within 24 hours), and at a fixed monthly price
  - [3] 2026-10-22: page title Intel Xeon E3-1230v6 | Fujitsu PRIMERGY RX1330 M3 | Live within 2 hours and configuration name Fujitsu PRIMERGY RX1330 M3 - Instant Delivery 16GB 1x 250GB SSD
  - [3] 2026-10-22: Specifications for chosen processor: 4 Cores, 8 Threads, 3.50GHz
  - [3] 2026-10-22: meta description: Fujitsu PRIMERGY RX1330 M3 with Intel Xeon E3-1230v6 processor. Dedicated server without set-up fee. Fast delivery within 2 hours. 24/7/365 Worldstream support.
  - [3] 2026-10-22: uplink selector: 1Gbit/s - 50TB marked Included, 1Gbit/s - 100TB at EUR 50.00 /mo, 1Gbit/s - Unmetered at EUR 99.00 /mo, with Our speeds are guaranteed, full-duplex. If you want unlimited traffic, choose unmetered.
  - [3] 2026-10-22: 20 Gbit/s is always included, upgradeable up to 100 Gbit/s.
  - [1] 2026-10-22: the offer list prices configuration 110, Fujitsu PRIMERGY RX1330 M3 - Intel Xeon E3-1230v6 - Instant delivery, at EUR 49.00, the lowest of the 43 entries; the page payload pairs that configuration's hash b1c73c0c31666d196e42863d13631eb5 with 4900 and 5150
  - [3] 2026-10-22: payment-term selector shows Payment every month selected, with Payment every 3 months, Payment every 6 months, Payment every 12 months and Payment every 24 months offered; the page payload carries discountPercentage values of 2, 4, 6 and 8 alongside that set of options
  - [3] 2026-10-22: the page names the panel's controls: You can remotely turn on, (forcibly) reboot or reinstall your server via the Worldstream Portal panel.
  - [4] 2026-10-22: 404, title Page not found, so no terms page was read and no minimum-term clause is recorded
  - [5] 2026-10-22: quoted: 'Fujitsu PRIMERGY RX2540 M2 2x Intel Xeon E5-2620v4 16 Cores, 32 Threads, 2.10GHz | 2x 960GB Enterprise SSD 10x 10TB HDD EUR219.00/monat'
  - [5] 2026-10-22: quoted: 'Dell PowerEdge T640 2x Intel Xeon Gold 5120 28 Cores, 56 Threads, 2.20GHz | 2x 960GB NVMe SSD 18x 12TB HDD EUR628.40/monat'
  - [6] 2026-10-22: the English storage path serves the same generic dedicated-server page as /en/dedicated-servers/ with no plan table; the only figure on it is 'From EUR 104 per month' for an EPYC 4245P compute box
- sources:
  - [1] https://www.worldstream.com/en/dedicated-servers
  - [2] https://www.worldstream.com/en/dedicated-server
  - [3] https://www.worldstream.com/en/dedicated-servers/configure/110
  - [4] https://www.worldstream.com/en/terms-and-conditions
  - [5] https://www.worldstream.com/de/storage-servers/
  - [6] https://www.worldstream.com/en/dedicated-servers/storage/
