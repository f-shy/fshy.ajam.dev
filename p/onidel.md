# Onidel

> onidel.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onidel/ | JSON https://fshy.ajam.dev/api/v1/entity/onidel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Onidel

- `compute/onidel` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.718Z (live) | stale on 2026-11-22
- url https://onidel.com/services/premium-vps
- price parsed USD 4.95/mo
- free tier: Per the vendor's own plans API (api.cloud.onidel.com/instance_plans, USD, Sydney): ONI-1 at USD 4.95/month billed monthly, USD 3.96/month billed annually (USD 47.52 a year), USD 3.71/month biennially, USD 3.46/month triennially, USD 0.0074 hourly: 1 vCPU, 2 GB RAM, 20 GB NVMe, 1 TB data in the apac region (2 TB in na, 3 TB in eu) on a 1 Gbps port. Locations: Sydney, Melbourne, Singapore, Ho Chi Minh City, Amsterdam, New York. Stock: not published; the plans API exposes no stock field and the deploy flow at cloud.onidel.com requires an account. Renewal: not published; the plans API prints no renewal price. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: monthly allocation covering inbound and outbound, poolable per region; overage at USD 3/TB, quoted from the vendor FAQ | metered: yes | free allowance: 1 TB a month on the entry plan in apac; 2 TB in na and 3 TB in eu, per the plans API's data_by_region | price per TB: USD 3 per TB | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month on the entry plan in the apac region (2 TB in na, 3 TB in eu), per the vendor's plans API. The vendor FAQ states the allocation covers both inbound and outbound traffic, can be pooled across VMs in one region, and that overage costs USD 3/TB; inbound counting against the allowance halves the usable crawl volume. [1]
- limits note: 1 TB a month on the entry plan in the apac region (2 TB in na, 3 TB in eu), per the vendor's plans API. The vendor FAQ states the allocation covers both inbound and outbound traffic, can be pooled across VMs in one region, and that overage costs USD 3/TB; inbound counting against the allowance halves the usable crawl volume.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: documented REST API at developers.onidel.com and a control panel at cloud.onidel.com; snapshots and scheduled backups (the 2 most recent retained, downloadable), custom ISO, noVNC console, cloud firewall, BGP session and floating IP; backup storage billed at USD 0.1/GB/month
- composes with: USD 4.95 a month, USD 3.96 on the annual term (USD 47.52 a year), for 2 GB of RAM and 20 GB of NVMe with 1 TB of transfer in Melbourne is the cheapest Australian presence at this price, and the documented API plus snapshot and backup path make it deployable as a worker without a wrapper. The 1 TB inbound-and-outbound cap keeps it off a serving path.
- reliability: the vendor states a 99.9 percent network and power uptime SLA with credits claimable within 48 hours of a qualifying incident, and a 7-day money-back guarantee for a service that is faulty or misrepresented but not for change of mind, quoted from the FAQ
- notes: or docs/ (searched both trees for onidel, no hit). The plan table renders client-side, but the page's JS bundle calls api.cloud.onidel.com/instance_plans, which returns the full plan list with per-cycle prices and per-region data allowances; the entry-plan numbers are now the vendor's own. Conflicting labels worth resolving: the vendor meta description says 'dedicated vCPU' while the tracker row says '(shared)'; the plans API does not state either. Stock is not published: the plans API has no stock field and deploy requires an account.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: USD 4.95/month for ONI-1
  - renewal_usd: not published: the plans API prints the per-cycle prices and no renewal price
- evidence:
  - [2] 2026-10-22: cheapest row: '$3.75 / month', '1 Epyc Cores (shared)', '1,024 MB RAM', '20 GB NVMe', '1,024 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', Melbourne Australia, New York and Amsterdam; header 'starting at $3.75 per month'
  - [1] 2026-10-22: FAQ quoted: 'Each plan includes a monthly bandwidth allocation that covers both inbound and outbound traffic. With bandwidth pooling, all VMs within the same region can share the same pool of bandwidth ... If you exceed your allocation, you can either upgrade your plan or pay for additional bandwidth at $3/TB.'
  - [1] 2026-10-22: page states '99.9% Network & power uptime SLA', '3 replicas Storage durability', '6 locations', 'AMD EPYC', and 'Get 25% bonus credit on your first invoice'; backup storage 'billed separately at $0.1/GB/month'
  - [3] 2026-11-07: the vendor's plans API prices ON-1 at USD 4.95 monthly, 3.96 annually, 3.71 biennially, 3.46 triennially, 0.0074 hourly, with 1 vCPU, 2 GB RAM, 20 GB disk, 1 TB data in apac (2 TB na, 3 TB eu) on a 1 Gbps port | capture: sha256:f80d62f3150a7ca45ee32af6320e1f8b24b8fe75c0fdd770287c49c85836ea34 | quote: {"name":"ONI-1","vcpu":1,"ram":2,"disk":20,"data":1,"data_by_region":{"apac":1,"eu":3,"na":2},"bw":1.0,"prices":{"hourly":0.0074,"monthly":4.95,"quarterly":4.7,"semiannually":4.46,"annually":3.96,"biennially":3.71,"triennially":3.46}}
  - [1] 2026-11-07: the vendor FAQ states the overage price is USD 3 per TB | capture: sha256:969f6ef8c8b8cef9a848c5c595b157574654b1616a03f05466da7e2b9f1ff04c | quote: If you exceed your allocation, you can either upgrade your plan or pay for additional bandwidth at $3/TB.
  - [3] 2026-11-07: the vendor plans API prices ON-1 at USD 4.95 monthly and USD 3.96 on the annual term, with no stock field | capture: sha256:2a0c6305950fa88a79a09b65e8eeedd5738ceb7fdf3cb8f28be2ad54a23e826a | quote: "monthly":4.95,"quarterly":4.7,"semiannually":4.46,"annually":3.96,"biennially":3.71,"triennially":3.46
  - [1] 2026-11-07: the plan table on the vendor page renders client-side from the plans API; the page itself prints no prices | capture: sha256:969f6ef8c8b8cef9a848c5c595b157574654b1616a03f05466da7e2b9f1ff04c | quote: Loading plans
  - [3] 2026-11-07: the vendor plans API prices ONI-1 at USD 4.95 on the monthly term | capture: sha256:f80d62f3150a7ca45ee32af6320e1f8b24b8fe75c0fdd770287c49c85836ea34 | quote: {"name":"ONI-1","vcpu":1,"ram":2,"disk":20,"data":1,"data_by_region":{"apac":1,"eu":3,"na":2},"bw":1.0,"prices":{"hourly":0.0074,"monthly":4.95,"quarterly":4.7,"semiannually":4.46,"annually":3.96,"biennially":3.71,"triennially":3.46}}
  - [3] 2026-11-07: the plans API's name field reads ONI-1 | capture: sha256:f80d62f3150a7ca45ee32af6320e1f8b24b8fe75c0fdd770287c49c85836ea34 | quote: {"name":"ONI-1","vcpu":1,"ram":2,"disk":20,"data":1,"data_by_region":{"apac":1,"eu":3,"na":2},"bw":1.0,"prices":{"hourly":0.0074,"monthly":4.95,"quarterly":4.7,"semiannually":4.46,"annually":3.96,"biennially":3.71,"triennially":3.46}}
  - [3] 2026-11-07: the plans API's prices object lists the billing-cycle prices; no renewal price appears | capture: sha256:f80d62f3150a7ca45ee32af6320e1f8b24b8fe75c0fdd770287c49c85836ea34 | quote: {"name":"ONI-1","vcpu":1,"ram":2,"disk":20,"data":1,"data_by_region":{"apac":1,"eu":3,"na":2},"bw":1.0,"prices":{"hourly":0.0074,"monthly":4.95,"quarterly":4.7,"semiannually":4.46,"annually":3.96,"biennially":3.71,"triennially":3.46}}
  - [3] 2026-11-07: the plans API prices ONI-1 at USD 4.95 monthly with the 1 vCPU / 2 GB / 20 GB shape | capture: sha256:f80d62f3150a7ca45ee32af6320e1f8b24b8fe75c0fdd770287c49c85836ea34 | quote: {"name":"ONI-1","vcpu":1,"ram":2,"disk":20,"data":1,"data_by_region":{"apac":1,"eu":3,"na":2},"bw":1.0,"prices":{"hourly":0.0074,"monthly":4.95,"quarterly":4.7,"semiannually":4.46,"annually":3.96,"biennially":3.71,"triennially":3.46}}
- sources:
  - [1] https://onidel.com/services/premium-vps
  - [2] https://vpspricetracker.com/provider/Onidel/vps
  - [3] https://api.cloud.onidel.com/instance_plans?instance_type=6bcc78c4-07ab-44e6-a5a7-dc64414a1e10&location=Sydney&currency=USD
