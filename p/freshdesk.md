# Freshdesk

> freshdesk.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freshdesk/ | JSON https://fshy.ajam.dev/api/v1/entity/freshdesk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Freshdesk (helpdesk attachments)

- `storage/freshdesk` | trial-only | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.freshdesk.com
- free tier: Freshworks support states flatly: 'There is no storage limit on the Freshdesk platform. All the data is stored in Cloud.' Per-attachment 20 MB (15 MB on Sprout/trial). | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 15 MB | bytes: 15000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter; attachments are served from `cdn.freshdesk.com` (S3-backed). | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-object-cap: 15 MB [1]
- limits note: per-object-cap: 15 MB (Sprout/trial) to 20 MB per conversation. request-rate: Growth 100 req/min, Pro 400, Enterprise 700, with per-endpoint sub-limits (Ticket Create 50/min on Growth). Retention: 'no storage limit' is unqualified in the article, but the Free Program ends after 6 months.
- interface detail: rest
- tooling: Freshdesk REST API (multipart attachments), Python/PHP samples in `freshworks/fresh-samples` (`create_ticket_attachment.py`). No rclone backend.
- composes with: 'No storage limit' x unlimited free-tier portals would be the best finding in the niche. But the free tier is a 6-month program, not a standing plan, so the realistic multiplier is 6 months x N portals.
- reliability: The 'no storage limit' claim is real and current, but it is a claim about a paid platform. Free access is a 6-month program with 2 agent seats; files >20 MB must be hotlinked from Dropbox/OneDrive, i.e. Freshdesk is not the store.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Freshworks support states flatly: 'There is no storage limit on the Freshdesk platform. All the data is stored in Cloud.' Per-attachment 20 MB (15 MB on Sprout/trial).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'There is no storage limit on the Freshdesk platform.'
  - [2] 2026-10-21: '20 MB/conversation for accounts on the Blossom and above plans. For Sprout and trial accounts ... 15 MB'
  - [3] 2026-10-21: 'available for free for 6 months'
  - [4] 2026-10-21: rate limit tables (Growth 100/min; Enterprise 700/min)
- sources:
  - [1] https://support.freshdesk.com/support/solutions/articles/234965-hi-is-there-a-storage-limit-on-your-platform-
  - [2] https://support.freshdesk.com/support/solutions/articles/196643-what-is-the-size-limit-for-attachments-to-a-ticket-reply-
  - [3] https://partnersupport.freshworks.com/support/solutions/articles/50000010099-explore-freshdesk-free-program-freshdesk-only-
  - [4] https://developers.freshdesk.com/api/
