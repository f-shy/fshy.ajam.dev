# RAVNIX

> ravnix.gg | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ravnix/ | JSON https://fshy.ajam.dev/api/v1/entity/ravnix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RAVNIX

- `compute/ravnix` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://ravnix.gg/
- free tier: USD 14/year for Xeon-1 in Atlanta: 1 vCPU, 1 GB RAM, 10 GB SSD, 2.5 TB of monthly bandwidth counting both directions, a 500 Mbps port and 1 IPv4. Xeon-2 is USD 24/year for 2 GB, 20 GB and 5 TB; Xeon-4 is USD 34/year for 2 vCPU, 4 GB, 40 GB and 10 TB; the EPYC line offers EPYC-8 at USD 10/month for 4 vCPU, 8 GB, 100 GB, 15 TB and a 5 Gbps port. All promotional prices are stated to be recurring with no setup fee, the promotional plans carry no refunds, and replying to the thread with an order number doubles the monthly bandwidth. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2.5 TB a month counting both directions; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 2.5 TB per month, inbound and outbound combined | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2.5 TB a month on the entry plan, and the thread states the count includes inbound as well as outbound, which halves the usable figure against every other record here that counts outbound only. 2.5 TB a month averages about 8 Mbit/s, so the counter binds far before the 500 Mbps port. [1]
- limits note: 2.5 TB a month on the entry plan, and the thread states the count includes inbound as well as outbound, which halves the usable figure against every other record here that counts outbound only. 2.5 TB a month averages about 8 Mbit/s, so the counter binds far before the 500 Mbps port.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: VirtFusion control panel, Linux and Windows (bring your own licence), custom ISOs, a status page at status.ravnix.gg and a looking glass at atl-lg.ravnix.gg; no API is documented on the pages read
- composes with: USD 14/year is USD 1.17/month for a 1 GB machine, which is the lowest annual rate among documented hosts, and the bidirectional bandwidth count is the reason to read the allowance before treating it as 2.5 TB of outbound; the EPYC-8 row at USD 10/month for 8 GB and 15 TB is the same host's answer for a heavier job
- reliability: the thread states a migration to a new Atlanta data center and a move to HetrixTools monitoring on 2026-10-10, with the status page carrying 'very limited historical data' as a result; that is a monitoring gap and not an outage report
- notes: The vendor page and the thread disagree on location: the page says 'South Carolina' in its banner and the thread says Atlanta, Georgia, migrated six months after the last offer post, so the page is stale rather than the thread. Unverified: which site is live, and whether the doubled-bandwidth offer still stands after the thread ages out. The thread states prices in USD and no conversion was performed.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [2] 2026-10-22: the offer thread, posted October 10, 2026, quoted from its table: 'Xeon-1 | 1 | 1 GB | 10 GB | 2.5 TB | 500 Mbps | $14/yr'; 'Xeon-2 | 1 | 2 GB | 20 GB | 5 TB | 500 Mbps | $24/yr'; 'Xeon-4 | 2 | 4 GB | 40 GB | 10 TB | 500 Mbps | $34/yr'; notes: 'Bandwidth is monthly and counts both inbound and outbound traffic'; 'All promotional prices are recurring, with no setup fees'; 'No refunds for these special promotional plans'; 'Location: ATL1 - Atlanta, USA (AS401486)'
  - [1] 2026-10-22: the vendor page confirms the price band and the site ('South Carolina', 'Starting $4/mo', 'Starting $3/mo', '99.9% Uptime SLA') but carries no plan table and no per-plan figures, and its location line does not match the thread's Atlanta
- sources:
  - [1] https://ravnix.gg/
  - [2] https://lowendtalk.com/discussion/221937/ravnix-is-back-new-atlanta-location-upgraded-network-vps-offers-starting-at-14-year
