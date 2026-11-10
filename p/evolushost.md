# EvolusHost

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/evolushost/ | JSON https://fshy.ajam.dev/api/v1/entity/evolushost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EvolusHost

- `compute/evolushost` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-08T00:54:55.395Z (live) | stale on 2026-11-23
- url https://vpspricetracker.com/provider/EvolusHost/vps
- price parsed USD 5.62/mo
- free tier: The tracker lists EUR 3.99 per month for 1 Epyc core, 2 GB RAM, 32 GB NVMe, 3 TB a month on a 10 Gbps port, in Austria and Germany. That plan is the vendor's own Nano VPS on the EPYC page: EUR 3.99 a month, 1 core, 2 GB RAM, 32 GB of NVMe and 3 TB a month on a 40 Gbit uplink, orderable in EU Central Austria and Germany, and the EPYC line runs from that shape to nine plans topping at 32 cores and 96 GB RAM. The Ryzen line on the Linux VPS page is a separate product that also exists: its cheapest tier is Small VPS at EUR 4.99 per month with 1 core, 2 GB RAM and a 10Gbit 5TB/m network line, deployable in Germany, Austria, Netherlands, London, Salt Lake City and New York, with Medium at EUR 15.99 (2 cores, 4 GB, 50 GB, 7 TB/m) and Large at EUR 29.99 (4 cores, 8 GB, 100 GB, 10 TB/m). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the Nano VPS at EUR 3.99 states 3 TB a month on a 40 Gbit uplink; the Ryzen Small VPS at EUR 4.99 states 5 TB a month on a 10 Gbit uplink; the vendor publishes no overage rate | metered: yes | free allowance: the Nano VPS at EUR 3.99 states 3 TB a month on a 40 Gbit uplink; the Ryzen Small VPS at EUR 4.99 states 5 TB a month on a 10 Gbit uplink; the vendor publishes no overage rate | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): the Nano VPS at EUR 3.99 states 3 TB a month on a 40 Gbit uplink; the Ryzen Small VPS at EUR 4.99 states 5 TB a month on a 10 Gbit uplink; the vendor publishes no overage rate [1]
- limits note: the Nano VPS at EUR 3.99 states 3 TB a month on a 40 Gbit uplink; the Ryzen Small VPS at EUR 4.99 states 5 TB a month on a 10 Gbit uplink; the vendor publishes no overage rate
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with full root and a quick console; the vendor also sells Windows and dedicated lines. No API documented on the pages read
- composes with: the EUR 3.99 EPYC Nano tier exists on the vendor's own EPYC page, so the tracker row is reachable; on memory per euro it is close to the Ryzen Small VPS at EUR 4.99, which states more monthly traffic
- reliability: no reliability event recorded
- notes: Prices are recorded in EUR.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 32
  - price_on_page: EUR 4.99/month: Small VPS
  - renewal_note: not published: the Linux VPS page read on 2026-11-07 prints a monthly price per tier and no renewal price
- evidence:
  - [1] 2026-10-22: row quoted from the Cheapest VPSs table: 'EUR 3.99 / month', '1 Epyc Cores (shared)', '2,048 MB RAM', '32 GB NVMe', '3,000 GB/month bandwidth', '10 Gbps port speed', 'IPv4 + IPv6', 'Austria'
  - [2] 2026-10-22: 'Small VPS' card: 'EUR 4.99 /month', '1 Cores', '2GB Memory', '25GB NVMe Space', 'NETWORK 10Gbit Uplink - 5TB/m', with region buttons for EU Central (Germany, Austria, Netherlands), EU West (London), US West (Salt Lake City) and US East (New York)
  - [3] 2026-10-22: homepage summary card: 'Ryzen VPS Starting at: EUR 4.99 /month, 1 Core, 2GB Memory, 25GB NVMe Space, NETWORK 1Gbit Uplink Shared'
  - [2] 2026-11-07: the vendor's own Linux VPS page prices the Small VPS tier at EUR 4.99 a month | capture: sha256:4b3115caa52b753b1bcb80bf7122998bec5e51c21e4f8c8d1980b1bf35066bcf | quote: Small VPS...€4.99 /month
  - [4] 2026-11-07: the vendor's own EPYC page sells the Nano VPS at EUR 3.99 a month with 1 core, 2 GB RAM, 32 GB NVMe and 3 TB a month on a 40 Gbit uplink, orderable in EU Central Austria and Germany | capture: sha256:f62e20ca791fd6099d5c2bed22961709bbdb75b2dc41a47c6e8f4abeb2bd99ea | quote: Nano VPS Best value-for-money Servers €3.99 /month - EU Central (Austria) - EU Central (Germany) Order now - CPU 1 Cores - RAM 2GB Memory - DISK 32GB NVMe Space - NETWORK 40Gbit Uplink - 3TB/m
- sources:
  - [1] https://vpspricetracker.com/provider/EvolusHost/vps
  - [2] https://evolushost.com/vps/linux
  - [3] https://evolushost.com
  - [4] https://evolushost.com/vps/epyc
