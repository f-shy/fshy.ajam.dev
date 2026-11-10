# RamNode

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ramnode/ | JSON https://fshy.ajam.dev/api/v1/entity/ramnode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RamNode

- `compute/ramnode` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.serverhunter.com/offer/ramnode-1024mb-cvz/
- free tier: USD 10.00/month for 1024MB CVZ plan in New York: 4 cores at 2.3 GHz on Intel E5, 1 GB RAM, 200 GB HDD, 1,000 Mbit uplink, 3 TB traffic, OpenVZ, no setup fee. Cloud VPS plans start from $4/month on the homepage. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 3 TB a month per the tracker row. The vendor homepage claims 'no surprise egress bills' with no allowance printed | metered: yes | free allowance: 3 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 3 TB a month is the allowance on the row. The vendor's front page advertises 'no surprise egress bills' without a figure, so the tracker is the only source for the number and it is third-party. [1]
- limits note: 3 TB a month is the allowance on the row. The vendor's front page advertises 'no surprise egress bills' without a figure, so the tracker is the only source for the number and it is third-party.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the homepage states 'Fast deployment via GUI, API, or CLI. Terraform ready. Ansible ready.' and 'Full API for each VPC', and names OpenStack as the cloud platform
- composes with: 200 GB of HDD for USD 10 is the cheapest disk-per-dollar row among documented hosts outside the storage topic, and the OpenVZ row is the wrong one to take for it: OpenVZ shares a host kernel, so the 200 GB belongs on the vendor's KVM cloud line, which the homepage prices from USD 4 without a spec sheet
- reliability: no reliability event recorded
- notes: RamNode standard OpenVZ plans start at USD 10.00 monthly for 1 GB RAM, 200 GB HDD, and 3 TB transfer on a 1 Gbps port. Cloud VPS plans start from USD 4.00 monthly on KVM infrastructure.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 200
- evidence:
  - [1] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Monthly price USD 10.00, 'Product type VPS', 'Virtualization type OpenVZ', 'Stock In stock', 'Processor cores 4 cores', 'Processor speed 2.3 GHz', 'Processor 1x Intel E5', 'Memory amount 1 GB', 'Total HDD Capacity 200 GB', 'Uplink 1,000 Mbit', 'Traffic 3 TB', 'Location New York, New York, United States of America'
  - [2] 2026-10-22: the homepage states 'Cloud VPS plans starting at $4/mo' and 'RamNode Cloud VPS from $4/mo. KVM with NVMe, hourly billing, IPv4 included, and no surprise egress bills. 99.99% uptime across US and EU', with the plan table behind https://ramnode.com/pricing, which was not fetched
  - [3] 2026-10-22: the guessed VPS path returned 404 ('Oops! Page not found'); the homepage is the page that was read
- sources:
  - [1] https://www.serverhunter.com/offer/ramnode-1024mb-cvz/
  - [2] https://ramnode.com/
  - [3] https://www.ramnode.com/vps/
