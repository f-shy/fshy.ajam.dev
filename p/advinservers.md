# Advin Servers KVM Storage VPS

> advinservers.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/advinservers/ | JSON https://fshy.ajam.dev/api/v1/entity/advinservers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Advin Servers KVM Storage VPS

- `storage/advin-servers-kvm-storage-vps` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:12:57.316Z (live) | stale on 2026-12-04
- url https://advinservers.com/vps
- price $2.50/TB/mo at both tiers ($25 for 10.24 TB, $50 for 20.48 TB). At 5 TB: the 5.12 TB rung at $15/mo = $2.93/TB. Cheapest large-footprint option on paper, but not purchasable. | parsed USD 2.5/TB-mo
- free tier: Kansas City: Storage 1 2,560 GB / Storage 2 5,120 GB / Storage 3 10,240 GB / Storage 4 20,480 GB, each as 20 GB NVMe boot + HDD, 10 Gbps. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: the direct storage product URL answered HTTP 404 on 2026-11-25; the cited page serves a generic Cloud VPS table with no per-object cap clause.
- retention: source: [1] | note: unverified: the cited page shows a generic Cloud VPS plan table with no file retention clause; the direct storage product URL answered HTTP 404.
- egress: Bundled bandwidth without published overage schedule: 8 TB, 16 TB, 32 TB, and 48 TB per month across tiers. The 20 TB tier provides 48 TB of transfer. | metered: yes | free allowance: 48 TB per month
- identity: card | detail: card
- interface: rest, sftp, rsync, rclone
- limits:
  - per-ip-shaping (binding): 10 Gbps [1]
- limits note: per-object-cap: none. Every storage rung showed sold out on stackrates' October 2026 snapshot and the store page 404s on the direct product URL. The provider has publicly floated '$2.50/TB of HDD, on a monthly commitment' as an ambition (LET 203516 p3).
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: sftp, rsync, rest (self-hosted)
- tooling: rclone SFTP, documented JSON control API (console.advinservers.com/api/v1)
- composes with: A 10 Gbps network port paired with a 20 TB single virtual machine allows hosting a 20 TB archive on a single instance without sharding.
- reliability: Delaware-based provider with approximately 30 nodes in US and EU, 99.9% SLA, 14-day money-back guarantee, and owned hardware. Hardware stock is frequently limited with zero availability across standard tiers.
- notes: High performance cloud compute, powered by KVM. No contract, monthly billed.
- extras:
  - price_verbatim: $2.50/TB/mo at both tiers ($25 for 10.24 TB, $50 for 20.48 TB). At 5 TB: the 5.12 TB rung at $15/mo = $2.93/TB. Cheapest large-footprint option on paper, but not purchasable.
- evidence:
  - [1] 2026-10-21: plan tables including the KVM Storage tab
  - [2] 2026-10-21: 'KVM Storage VPS 4 plans, none orderable today' with $10/$15/$25/$50 for 2.56/5.12/10.24/20.48 TB
  - [3] 2026-10-21: provider offer thread, '$4/TB HDD Storage VPS' in the title
  - [4] 2026-10-21: 'This offer is currently out of stock'
  - [1] 2026-11-09: the cited URL is the generic Standard Cloud KVM page, not the Storage 1-4 plan table | capture: sha256:0ca1ace9b7dda46065c5261f6d10f529f50addd8e9079f2e1ee2a544ad0dff8c | quote: High performance cloud compute, powered by KVM. No contract, monthly billed.
  - [1] 2026-11-11: the page served at the record's URL carries this sentence as its headline | capture: sha256:68dcc7b73b0f9d084e7fc0410462a9b3fef7be4afb7da6723c76a2b367331dba | quote: High performance cloud compute, powered by KVM. No contract, monthly billed.
  - [1] 2026-11-19: the cited URL still serves the generic Standard Cloud page, not the Storage 1-4 plan table | capture: sha256:9ebddfa47f1a7e0c5628199954d7b3f5010cef692b92add993c9fa7354e10f81 | quote: High performance cloud compute, powered by KVM. No contract, billed by the hour.
  - probe:https://advinservers.com/vps/storage-1 2026-11-25: the direct storage product URL answered HTTP 404 | capture: sha256:25466c5043f150001f3207b606dec26f36f2b08de5785b38621361e0bf110fdd | quote: "status": 404
- sources:
  - [1] https://advinservers.com/vps
  - [2] https://stackrates.ai/hosting/advinservers/
  - [3] https://lowendtalk.com/discussion/218436/
  - [4] https://www.serverhunter.com/offer/advin-servers-kvm-storage-vps-storage-1/
