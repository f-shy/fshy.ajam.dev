# VPS Server

> vpsserver.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsserver/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPS Server (vpsserver.com) — 30-day trial with 1 TB block storage + $100 credit

- `storage/vps-server-30-day-trial-with-1-tb-block-storage-100-cred` | trial-only | evidence reported | binding none | category iaas
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T19:55:25.446Z (live) | stale on 2026-12-10
- url https://www.vpsserver.com/free-vps-server/
- free tier: 1 TB of cloud block storage plus one cloud server worth up to $100, 30 days, 20+ locations. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: no per-object size cap stated on the trial page
- retention: 30 days, then auto-converts to paid at standard rates | days: 30 | source: [1] | note: The free trial gives a virtual private server at no cost for 30 days.
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
  - [1] 2026-11-19: the free trial includes a server worth USD 100, 1 TB block storage and 5 TB outbound traffic | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: The following is included in the free trial: 1 cloud server valued up to $100 with the configuration of your choice 1 TB of cloud block storage 5 TB of outgoing Internet traffic (1 TB in Asia and Australia)
  - [1] 2026-11-19: the trial signup verifies a credit card with a USD 1 to USD 2 charge | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: Upon signing up, a charge of $1 to $2 is initiated to verify the validity of your credit card (this charge will be voided)
  - [1] 2026-11-19: the free trial lasts 30 days | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: Our free VPS hosting gives customers an accessible virtual private server at no cost for 30 days.
  - [1] 2026-11-25: the trial supplies a server at no cost for 30 days | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: Our free VPS hosting gives customers an accessible virtual private server at no cost for 30 days.
  - [1] 2026-11-25: the trial page states a block-volume allowance, not an object-size limit | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: 1 TB of cloud block storage
  - [1] 2026-11-25: the trial lasts 30 days | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: Our free VPS hosting gives customers an accessible virtual private server at no cost for 30 days.
  - [1] 2026-11-25: the trial page gives a volume allowance and no per-object cap | capture: sha256:d065de33443125c87bb3a2e487384e482d56794e4b7450dd9f26966ac8073bf7 | quote: 1 TB of cloud block storage
- sources:
  - [1] https://www.vpsserver.com/free-vps-server/
