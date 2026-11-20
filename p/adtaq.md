# ADTAQ Storage VPS

> adtaq.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adtaq/ | JSON https://fshy.ajam.dev/api/v1/entity/adtaq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ADTAQ Storage VPS — 2 TB, 30 days free (card-gated)

- `storage/adtaq-storage-vps-2-tb-30-days-free` | trial-only | evidence reported | binding per-ip-shaping | category iaas
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:12:58.760Z (live) | stale on 2026-12-04
- url https://www.adtaq.com/storage-vps/
- free tier: 2 TB HDD, 2 vCPU, 2 GB RAM, 2 TB/month transfer on a 1 Gbps port, USD 20/month; paid ladder USD 10/TB up to 8 TB; the current page offers a 30-day money-back guarantee on the first order. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 30-day trial then $20/mo unless cancelled | days: 30 | source: [1] | note: not stated
- egress: 2 TB/month transfer is included with the 2 TB plan on a 1 Gbps port; beyond the allowance the port slows down rather than billed, and extra transfer is available at USD 1.50/TB. | metered: no | free allowance: 2 TB per month
- identity: card | detail: a credit card given to Stripe at trial signup
- interface: sftp, rsync, ssh, rclone
- limits:
  - per-ip-shaping (binding): 1 Gbps [1]
- limits note: 30-day trial then $20/mo unless cancelled. 6 TB/month egress cap. 2 TB per server; larger trial sizes explicitly refused ('we are not offering free trials for those at this time (nor do we plan to)').
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: sftp
- tooling: Root KVM VPS: full SSH/SFTP/rsync, mountable as rclone sftp remote or with rclone mount + fuse. Host rep explicitly runs KVM + VirtFusion.
- composes with: The one-month free trial is a soft launch limited to 24 users and requires a card given to Stripe; larger plans are excluded.
- reliability: Small Idaho host (Lincoln Freedom Group LLC), Boise datacentre, RAID6. New enough that the soft launch itself was the reliability test; no long-run track record. Trial VPS is deleted if not converted.
- notes: 2 TB HDD (SSD-cached), 2 vCPU, 2 GB RAM, 6 TB/month bandwidth on 1 Gbps. $20/month, FREE for the first month. Paid ladder is $10/TB/month with RAID6 + NVMe cache, up to 4 TB at $40.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 2 TB HDD (SSD-cached), 2 vCPU, 2 GB RAM, 6 TB/month bandwidth on 1 Gbps — $20/month, FREE for the first month. Paid ladder is $10/TB/month with RAID6 + NVMe cache, up to 4 TB at $40.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '$20/MONTH FREE for 1 Month'; 'Stripe is going to ask you for your credit card … Your card WILL NOT be charged unless you keep the server past the 30 day trial'
  - [2] 2026-10-21: current page, 'Storage VPS in Boise, Idaho — $10/TB, RAID6, 10G Uplink'
  - [2] 2026-11-19: the current plan table lists 2 TB storage and 2 TB/month transfer at USD 20/mo | capture: sha256:a1ef314baa354ce7d3d9e7d158f335a3ee14ae0a3a604bc0fe698a63cc8bfc89 | quote: | 2 TB | 2 | 2 GB | 2 TB | 2 TB/mo | 1 Gig | 1 + /64 | $20/mo | $200/yr |
  - [2] 2026-11-19: the current page states excess transfer slows the port instead of billing | capture: sha256:a1ef314baa354ce7d3d9e7d158f335a3ee14ae0a3a604bc0fe698a63cc8bfc89 | quote: Go past your transfer and the port slows down instead of sending you a bill.
  - [2] 2026-11-19: the current 2 TB plan includes 2 TB/month transfer | capture: sha256:a1ef314baa354ce7d3d9e7d158f335a3ee14ae0a3a604bc0fe698a63cc8bfc89 | quote: | 2 TB | 2 | 2 GB | 2 TB | 2 TB/mo | 1 Gig | 1 + /64 | $20/mo | $200/yr |
  - [1] 2026-11-19: the launch thread excludes larger plans from the free trial | capture: sha256:0bc079c972ee9f7effba1ea3682bfed10a7664a5e47f765c5d235949c1647f32 | quote: we are not offering free trials for those at this time (nor do we plan to, sorry)
  - [1] 2026-11-19: the launch thread states the trial requires a credit card given to Stripe | capture: sha256:0bc079c972ee9f7effba1ea3682bfed10a7664a5e47f765c5d235949c1647f32 | quote: Stripe is going to ask you for your credit card in order to allow you to start the Free Trial.
  - [2] 2026-11-19: the current page states a 30-day money-back guarantee on the first order | capture: sha256:a1ef314baa354ce7d3d9e7d158f335a3ee14ae0a3a604bc0fe698a63cc8bfc89 | quote: 30-day money-back guarantee on your first order.
  - [2] 2026-11-19: the current page lists extra transfer at USD 1.50/TB | capture: sha256:a1ef314baa354ce7d3d9e7d158f335a3ee14ae0a3a604bc0fe698a63cc8bfc89 | quote: Extra transfer $1.50/TB
  - [1] 2026-11-19: the launch thread states the card is tied to provisioning | capture: sha256:0bc079c972ee9f7effba1ea3682bfed10a7664a5e47f765c5d235949c1647f32 | quote: we built a provisioning solution that ties Stripe directly to Virtfusion
- sources:
  - [1] https://lowendtalk.com/discussion/186689/adtaq-soft-launch-free-2tb-storage-vps-for-one-month
  - [2] https://www.adtaq.com/storage-vps/
