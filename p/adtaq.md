# ADTAQ Storage VPS

> adtaq.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adtaq/ | JSON https://fshy.ajam.dev/api/v1/entity/adtaq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ADTAQ Storage VPS — 2 TB, 30 days free (card-gated)

- `storage/adtaq-storage-vps-2-tb-30-days-free` | trial-only | evidence reported | binding per-ip-shaping | category iaas
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.adtaq.com/storage-vps/
- free tier: 2 TB HDD (SSD-cached), 2 vCPU, 2 GB RAM, 6 TB/month bandwidth on 1 Gbps. $20/month, FREE for the first month. Paid ladder is $10/TB/month with RAID6 + NVMe cache, up to 4 TB at $40. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 30-day trial then $20/mo unless cancelled | days: 30 | source: [1] | note: not stated
- egress: Includes 6 TB per month premium bandwidth at 1 Gbps. Overage is metered. Cloudflare proxying is not included. | metered: yes | free allowance: 6 TB per month
- identity: card | detail: card
- interface: sftp, rsync, ssh, rclone
- limits:
  - per-ip-shaping (binding): 1 Gbps [1]
- limits note: 30-day trial then $20/mo unless cancelled. 6 TB/month egress cap. 2 TB per server; larger trial sizes explicitly refused ('we are not offering free trials for those at this time (nor do we plan to)').
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: sftp
- tooling: Root KVM VPS: full SSH/SFTP/rsync, mountable as rclone sftp remote or with rclone mount + fuse. Host rep explicitly runs KVM + VirtFusion.
- composes with: One trial per customer (Stripe ties card to VirtFusion provisioning. 'our provisioning solution ties Stripe directly to Virtfusion'). The flow ties each card to one provisioning record, so a second trial needs a second card and this is NOT repeatable at scale.
- reliability: Small Idaho host (Lincoln Freedom Group LLC), Boise datacentre, RAID6. New enough that the soft launch itself was the reliability test; no long-run track record. Trial VPS is deleted if not converted.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 2 TB HDD (SSD-cached), 2 vCPU, 2 GB RAM, 6 TB/month bandwidth on 1 Gbps — $20/month, FREE for the first month. Paid ladder is $10/TB/month with RAID6 + NVMe cache, up to 4 TB at $40.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '$20/MONTH FREE for 1 Month'; 'Stripe is going to ask you for your credit card … Your card WILL NOT be charged unless you keep the server past the 30 day trial'
  - [2] 2026-10-21: current page, 'Storage VPS in Boise, Idaho — $10/TB, RAID6, 10G Uplink'
- sources:
  - [1] https://lowendtalk.com/discussion/186689/adtaq-soft-launch-free-2tb-storage-vps-for-one-month
  - [2] https://www.adtaq.com/storage-vps/
