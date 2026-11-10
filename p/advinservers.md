# Advin Servers KVM Storage VPS

> advinservers.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/advinservers/ | JSON https://fshy.ajam.dev/api/v1/entity/advinservers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Advin Servers KVM Storage VPS

- `storage/advin-servers-kvm-storage-vps` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://advinservers.com/vps
- price $2.50/TB/mo at both tiers ($25 for 10.24 TB, $50 for 20.48 TB). At 5 TB: the 5.12 TB rung at $15/mo = $2.93/TB. Cheapest large-footprint option on paper, but not purchasable. | parsed USD 2.5/TB-mo
- free tier: Kansas City: Storage 1 2,560 GB / Storage 2 5,120 GB / Storage 3 10,240 GB / Storage 4 20,480 GB, each as 20 GB NVMe boot + HDD, 10 Gbps. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
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
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.50/TB/mo at both tiers ($25 for 10.24 TB, $50 for 20.48 TB). At 5 TB: the 5.12 TB rung at $15/mo = $2.93/TB. Cheapest large-footprint option on paper, but not purchasable.
- evidence:
  - [1] 2026-10-21: plan tables including the KVM Storage tab
  - [2] 2026-10-21: 'KVM Storage VPS 4 plans, none orderable today' with $10/$15/$25/$50 for 2.56/5.12/10.24/20.48 TB
  - [3] 2026-10-21: provider offer thread, '$4/TB HDD Storage VPS' in the title
  - [4] 2026-10-21: 'This offer is currently out of stock'
- sources:
  - [1] https://advinservers.com/vps
  - [2] https://stackrates.ai/hosting/advinservers/
  - [3] https://lowendtalk.com/discussion/218436/
  - [4] https://www.serverhunter.com/offer/advin-servers-kvm-storage-vps-storage-1/
