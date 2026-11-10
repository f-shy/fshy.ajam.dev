# Mage.space uploads

> mage.space | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mage/ | JSON https://fshy.ajam.dev/api/v1/entity/mage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mage.space uploads

- `storage/mage-space-uploads` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mage.space
- free tier: 100 MB per upload, 30-day life. No account-level storage allowance is offered. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per upload | bytes: 100000000 | source: [1] | note: not stated
- retention: 100 MB per upload, 30-day life | days: 30 | source: [1] | note: not stated
- egress: Signed URL, expiring; 'the file lives 30 days (url_expires_at), like every input and result'. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB per upload [1]
  - retention-clamped: retention ('Results and inputs | Kept 30 days [1]
- limits note: per-object-cap 100 MB ('One media input | 100 MB, whether fetched, decoded, or uploaded'); 15-minute upload-URL life; 30-day retention ('Results and inputs | Kept 30 days'); request body 4.5 MB; 20 generations in flight; 10 API keys/account.
- interface detail: rest
- tooling: POST /v1/uploads -> signed PUT URL (valid 15 min), then reference `url` in a generate request. Paid in gems.
- composes with: None worth having: 100 MB x 30 days. Only useful as an input staging area for generations, not as storage.
- reliability: Edge rate limiting during bursts; 429s are expected and uncharged.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 MB per upload, 30-day life. No account-level storage allowance is offered.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'up to 100 MB ... The upload URL is valid for 15 minutes; the file lives 30 days'
  - [1] 2026-10-21: limits table: 'One media input | 100 MB', 'Results and inputs | Kept 30 days'
- sources:
  - [1] https://docs.mage.space/api/limits
  - [2] https://docs.mage.space/api/endpoints/create-upload
