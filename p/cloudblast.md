# CloudBlast

> cloudblast.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudblast/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudblast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudBlast

- `compute/cloudblast` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:30.075Z (live) | stale on 2026-12-08
- url https://cloudblast.io/pricing
- free tier: VMA11 at EUR 3.6/month or EUR 0.0058/hour: 1x AMD EPYC 7C13, 3 GB RAM, 20 GB NVMe, 10 Gbps port with 5 TB of traffic per month, 1 IPv4 plus a /64 IPv6, DDoS protection, sold hourly or prepaid and running in 'four datacenters across the US, Europe and Asia'. The tracker lists the Amsterdam instance at EUR 3.60/month with a 2 Gbps port, so the port speed is the one number the two sources disagree on. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB per month included on VMA11; beyond that EUR 0.01 per GB of traffic leaving the datacenter, or EUR 1.5 per TB bought as an add-on to the bandwidth pool | metered: yes | free allowance: 5 TB/month on VMA11 | source: [1]
- identity: email | detail: not stated
- interface: cli, s3-compatible
- limits:
  - volume-quota (binding): 5 TB of traffic a month included, then EUR 0.01 per GB for traffic leaving the datacenter or EUR 1.5 per TB for add-on bandwidth, so the allowance is metered and the overage is priced [1]
- limits note: 5 TB of traffic a month included, then EUR 0.01 per GB for traffic leaving the datacenter or EUR 1.5 per TB for add-on bandwidth, so the allowance is metered and the overage is priced
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: the pricing page names a 'Workers' product metered per core-hour and per GB-hour with a repository-push deploy, and the VPS line is ordered per plan; no S3 endpoint or CLI is documented on the page
- composes with: 3 GB of RAM on an EPYC core with 5 TB of transfer for EUR 3.6 is a good crawler or small inference client host; the 20 GB NVMe is the limit, and the priced block storage at EUR 0.15 per GB-month makes this a poor archive tier compared with a dedicated storage VPS
- reliability: no reliability event recorded
- notes: The vendor and the tracker agree on price, RAM, disk and traffic and differ on the port (10 Gbps against 2 Gbps), so the vendor figure is recorded in the offer and the tracked figure stays in evidence. CloudBlast also sells a per-second serverless worker at EUR 0.011 per core-hour and EUR 0.004 per GB-hour, which is a different product from the VPS line and is not modelled in this record.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 3
  - facets.shape.disk_gib: 20
  - monthly_eur: 3.6
  - annual_eur: not published: the pricing page prints an hourly rate and a monthly rate with no annual total
  - billing_term: hourly or monthly
  - in_stock: yes
  - cart_note: unverified: behind a sign-up; the Order Now button leads to console.cloudblast.io/create/server, a JavaScript console that prices the plan only for a signed-in account
  - renewal_eur: not published: no page read prints a renewal or month-13 sentence
- evidence:
  - [1] 2026-10-22: plan row quoted: 'VMA11', '1x AMD EPYC 7C13', '3 GB', '20 GB', '10 Gbps 5 TB of traffic per month', 'EUR3.6 /month EUR0.0058/hour'
  - [1] 2026-10-22: extras quoted: 'Traffic One GB leaving the datacenter. EUR0.01 per GB', 'Extra bandwidth ... EUR1.5 per TB', 'IPv4 Address ... EUR2.5 per month', 'Block Storage ... EUR0.15 per GB per month', and 'All plans include 1 IPv4 & /64 IPv6'
  - [2] 2026-10-22: tracker row quoted: 'CloudBlast - EUR3.60 / month', '1 Epyc Cores (shared)', '3,072 MB RAM', '20 GB NVMe', '5,120 GB/month bandwidth', '2 Gbps port speed', 'Amsterdam Netherlands'; info page marks it 'In stock now' and lists Windows 'Yes (unlicensed)'
  - [1] 2026-11-07: the pricing page prices VMA11 at EUR 3.6 a month or EUR 0.0058 an hour | capture: sha256:e5bed064c4236e705d7c32ff50428db4290bc2da0d27dffebf57cf8dec7b4c62 | quote: VMA11
  - [1] 2026-11-07: the pricing page's own schema.org Offer for the EUR 3.60 VPS states availability InStock | capture: sha256:e5bed064c4236e705d7c32ff50428db4290bc2da0d27dffebf57cf8dec7b4c62 | quote: "availability":"https://schema.org/InStock"
  - [1] 2026-11-07: the pricing page still prices VMA11 at EUR 3.6 a month or EUR 0.0058 an hour with 3 GB RAM and 20 GB NVMe | capture: sha256:e5bed064c4236e705d7c32ff50428db4290bc2da0d27dffebf57cf8dec7b4c62 | quote: VMA11
  - [3] 2026-11-07: the console order page renders an empty client-side application shell with no price a read can see | capture: sha256:6402a29291a82a1cc5d19f3b133038e554ba2a5224a3be644404c65da5a0aa77 | quote: <div id="root"></div>
  - [1] 2026-11-07: the page prints the list price and no renewal sentence | capture: sha256:e5bed064c4236e705d7c32ff50428db4290bc2da0d27dffebf57cf8dec7b4c62 | quote: VMA11
  - [1] 2026-11-07: the pricing page still prices VMA11 at EUR 3.6 a month or EUR 0.0058 an hour | capture: sha256:605b6818901505c24a1695c7e704e32f7b104d250d25033dd6247e7d2e1c4368 | quote: | VMA11 | 1x AMD EPYC 7C13 | 3 GB | 20 GB | 10 Gbps 5 TB of traffic per month | €3.6/month€0.0058/hour | Order Now |
  - probe:https://console.cloudblast.io/create/server 2026-11-07: the console order page answers a 2538-byte client-side shell with no price or stock phrase a read can see | capture: sha256:e3885d7d9d1242bf8c6d8769b962cb65f1dd7c875d9fd9ceaa7756b3382de6e0 | quote: no-price
- sources:
  - [1] https://cloudblast.io/pricing
  - [2] https://vpspricetracker.com/provider/CloudBlast/vps
  - [3] https://console.cloudblast.io/create/server
