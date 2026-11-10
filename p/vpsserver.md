# VPS Server

> vpsserver.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsserver/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPS Server (vpsserver.com) — 30-day trial with 1 TB block storage + $100 credit

- `storage/vps-server-30-day-trial-with-1-tb-block-storage-100-cred` | trial-only | evidence reported | binding none | category iaas
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.vpsserver.com/free-vps-server/
- free tier: 1 TB of cloud block storage plus one cloud server worth up to $100, 30 days, 20+ locations. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 30 days, then auto-converts to paid at standard rates | days: 30 | source: [1] | note: not stated
- egress: Includes 5 TB outbound transfer (1 TB in Asia and Australia), followed by metered overage rates. | metered: yes
- identity: card | detail: card
- interface: rest, sftp, rsync, ssh, rclone
- limits note: 30 days, then auto-converts to paid at standard rates. Config must fit inside $100. Card verification charge $1–$2.
- interface detail: rest
- tooling: Root KVM + block volume; SSH/SFTP/rsync, so rclone sftp. The block volume can be attached and served over any protocol you install.
- composes with: Single trial per customer and the page is explicit that the $1–$2 card authorisation is the gate that limits repeated signups. Not repeatable without new cards.
- reliability: Reseller-grade infrastructure (20+ DCs, KVM); trial endpoints are commonly rate-limited or suspended for sustained outbound. No data-vanishing reports found, but no long-run evidence either.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB of cloud block storage plus one cloud server worth up to $100, 30 days, 20+ locations.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The following is included in the free trial: 1 cloud server valued up to $100 … 1 TB of cloud block storage … 5 TB of outgoing Internet traffic (1 TB in Asia and Australia)'
  - withheld 2026-10-21: same page — 'a charge of $1 to $2 is initiated to verify the validity of your credit card … Your service type will change from trial to paid when it ends.'
- sources:
  - [1] https://www.vpsserver.com/free-vps-server/
