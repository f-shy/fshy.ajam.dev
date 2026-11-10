# DedicatedCore

> dedicatedcore.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dedicatedcore/ | JSON https://fshy.ajam.dev/api/v1/entity/dedicatedcore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DedicatedCore — 6 TB storage VPS, 60 days free (3 slots only)

- `storage/dedicatedcore-6-tb-storage-vps-60-days-free` | trial-only | evidence reported | binding none | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dedicatedcore.com
- free tier: 6 TB HDD, 3 vCPU, 4 GB RAM, 10,000 GB bandwidth, dedicated IP. Free for 60 days. Only 3 units existed. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: until the instance is recycled; not persistent | source: [1] | note: not stated
- egress: Includes 10 TB per month transfer. Bandwidth is metered beyond the allowance and Cloudflare proxying is not provided. | metered: no | free allowance: 10 TB per month
- identity: email | detail: email
- interface: sftp, rsync, ssh, rclone
- limits note: Deleted after 60 days.
- interface detail: sftp
- tooling: Root KVM. SSH/SFTP/rsync, so rclone sftp or a local fuse mount works. No object API.
- composes with: Not repeatable. Explicitly 'non-renewable, and the VPS will be deleted at the end of the 60-day period', 3 slots, application via a Google Form, and the thread closed with 'Filled!' within days. This is a marketing gesture, not a capacity source.
- reliability: Deliberately ephemeral: the data is destroyed at day 60 by design. Good for one 6 TB cold-archive burst, worthless as standing storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 6 TB HDD, 3 vCPU, 4 GB RAM, 10,000 GB bandwidth, dedicated IP — free for 60 days. Only 3 units existed.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'DISK SPACE: 6 TB (HDD) … completely free for 60 days'; 'there are only 3 Storage VPS servers available'; 'This free offer is non-renewable, and the VPS will be deleted at the end of the 60-day period.'
- sources:
  - [1] https://lowendspirit.com/discussion/9079/dedicatedcore-exclusive-offer-for-lowendspirit-community-3-free-6-tb-storage-vps-with-dedicated-ip
