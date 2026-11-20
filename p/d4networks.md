# D4 Networks

> d4networks.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/d4networks/ | JSON https://fshy.ajam.dev/api/v1/entity/d4networks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## D4 Networks

- `compute/d4-networks` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://d4networks.com/
- free tier: USD 49/year, renewing at USD 49/year with the price locked until cancellation or a plan change, for 2 vCPU, 4 GB RAM and 5 TB of monthly transfer, annual billing only. Disk differs by site: 120 GB of NVMe in Dallas on an AMD EPYC 7543P with a 4 Gbps port, 80 GB in Amsterdam on an EPYC 7C13 with a 2.5 Gbps port, and 80 GB in New York on dual Xeon Gold 6138 with a 2.5 Gbps port. Every site includes a dedicated IPv4, a routed /64 IPv6, DDoS protection and a 99.9 percent SLA with service credits; stock is capped at 40 units in Dallas and 15 in each of the other two. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB a month; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 5 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 5 TB a month counts against both directions by implication of the plan table, and it is the wall before the 4 Gbps Dallas port: 5 TB a month averages about 15 Mbit/s. No overage price and no post-allowance throttle are stated. The annual price is fixed until cancellation, which is why the renewal rate is knowable here and not on most records. [1]
- limits note: 5 TB a month counts against both directions by implication of the plan table, and it is the wall before the 4 Gbps Dallas port: 5 TB a month averages about 15 Mbit/s. No overage price and no post-allowance throttle are stated. The annual price is fixed until cancellation, which is why the renewal rate is knowable here and not on most records.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor page describes provisioning 'from the control panel in about a minute' without naming the panel; it publishes a looking glass, and the thread gives a status page at status.d4networks.com, an ASN of its own (AS14475) and a /22 from ARIN. No API or CLI is documented on either page read
- composes with: USD 49 a year for 4 GB and 120 GB with 5 TB a month, a locked renewal price and a 99.9 percent credit-backed SLA is the best-evidenced cheap plan among evaluated providers, and the Dallas row carries 50 percent more disk than the other two at the same price; the published Geekbench runs (1758 single in Dallas against 1148 in New York) make the site choice a measurable decision rather than a guess.
- reliability: no reliability event observed: the offer is a first post from a company registered in Missouri since 2014, with no operator reports read.
- notes: The thread publishes its own Geekbench 6 links per location, which is the only record among evaluated providers that hands over a benchmark that can be re-run before buying. verification criteria: whether the 40-unit and 15-unit caps are still open, and whether the 4 Gbps Dallas port is shared or per-VM, which the table does not say. The provider page and the thread agree on regions and disagree on nothing that was checked.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 120
- evidence:
  - [2] 2026-10-22: the offer thread quoted: '2 vCPU, 4 GB RAM, 80 to 120 GB NVMe and 5 TB monthly transfer for $49 per year, renewing at $49 per year'; 'The price is locked until you cancel or move to another plan (terms, section 4)'; 'Dallas: $49 per year ... 120 GB NVMe ... 5 TB monthly transfer, 4 Gbps port'; 'Amsterdam: $49 per year ... 80 GB NVMe ... 2.5 Gbps port'; 'New York: $49 per year ... 80 GB NVMe ... 2.5 Gbps port'; 'Limited to 40 units' and 'Limited to 15 units'
  - [1] 2026-10-22: the vendor homepage confirms the three regions and the port classes ('Cloud VPS on ports up to 5 Gbps' for New York, 'up to 10 Gbps' for Dallas, 'up to 5 Gbps' for Amsterdam) and states 'A 99.9% uptime guarantee, backed by service credits', but carries no plan table and no price
- sources:
  - [1] https://d4networks.com/
  - [2] https://lowendtalk.com/discussion/221558/d4-networks-4gb-kvm-80-120gb-nvme-49-year-renews-at-49-dallas-amsterdam-new-york
