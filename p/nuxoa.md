# NUXOA

> nuxoa.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nuxoa/ | JSON https://fshy.ajam.dev/api/v1/entity/nuxoa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NUXOA

- `compute/nuxoa` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://nuxoa.de/
- free tier: EUR 95/month for an Intel Xeon E5-2640 v4 in Frankfurt: 10 cores and 20 threads, 64 GB DDR4, 1 TB SAS, a 1 Gbit/s uplink, 200 TB of monthly traffic, 1 IPv4 and a /64 IPv6, DDoS protection, an OS auto-installer and no setup fee, in firstcolo FRA4. Higher rows: EUR 110 for an E5-2620 v4 with 8 cores, 128 GB and 512 GB of NVMe on 10 Gbit/s; EUR 120 for a Ryzen 7 5700X with 8 cores, 64 GB and 1 TB of NVMe; EUR 150 for a Ryzen 9 5950X with 16 cores, 128 GB and 1 TB of NVMe; EUR 160 for either an E5-2680 v4 with 14 cores and 256 GB or a Ryzen 7 9700X with 64 GB DDR5. The thread states the configurations are available for business customers only, and that all listed prices are recurring monthly rental prices in EUR excluding VAT, on one-month contracts paid in advance that renew monthly unless cancelled. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 200 TB a month on every configuration; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 200 TB per month | source: [2]
- identity: email | detail: not read: signup requirements unverified; the offer thread states the configurations are 'available for business customers only', which is an eligibility term and not a signup term
- interface: rest, cli
- limits:
  - volume-quota (binding): 200 TB a month on every configuration, which averages about 634 Mbit/s and therefore sits close to the 1 Gbit/s uplink on the entry row: on that row the port and the counter are within a factor of two, and on the 10 Gbit/s rows the counter binds. No overage price and no post-allowance throttle are stated. [1]
- limits note: 200 TB a month on every configuration, which averages about 634 Mbit/s and therefore sits close to the 1 Gbit/s uplink on the entry row: on that row the port and the counter are within a factor of two, and on the 10 Gbit/s rows the counter binds. No overage price and no post-allowance throttle are stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor advertises RIPE services, IP transit and an OS auto-installer, and runs its own AS51202; no API or CLI is documented on the pages read
- composes with: EUR 95 a month for 10 cores and 20 threads with 64 GB, 1 TB of disk and 200 TB of traffic provides low dedicated server pricing and a 200 TB transfer allowance. Service is restricted to business customers.
- reliability: no reliability event recorded
- notes: The thread prints its own euro-to-dollar figures next to each price and this record quotes them rather than converting. The vendor site is a German business-hosting site with no public price list for dedicated servers, so nothing here is first-party. Unverified: whether the business-customers-only term means a registered company at order or at invoice, since that decides whether the cheapest row among documented hosts is reachable at all.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 20
  - facets.shape.ram_gib: 64
  - facets.shape.disk_gib: 1024
- evidence:
  - [2] 2026-10-22: the offer thread quoted: 'Intel Xeon E5-2640 v4 - EUR 95/month approx US$106.35 ... 10 cores / 20 threads ... 64 GB DDR4 RAM ... 1 TB SAS ... 1 Gbit/s uplink ... Location: firstcolo FRA4, Frankfurt'; 'Included with every server listed below: 200 TB monthly traffic, 1 IPv4 address and a /64 IPv6 subnet, Premium DDoS protection, OS auto-installer, Dedicated bare-metal hardware, No setup fee'; 'The configurations below are available for business customers only'
  - [1] 2026-10-22: the vendor site answered 200 with German business-hosting navigation (Linux and Windows servers, web hosting, cloud workstations, RIPE services, IP transit, DDoS protection, reselling) and carries no dedicated server table and no price, so the figures rest on the forum post
- sources:
  - [1] https://nuxoa.de/
  - [2] https://lowendtalk.com/discussion/222107/frankfurt-dedicated-servers-from-95-mo-ryzen-xeon-nuxoa
