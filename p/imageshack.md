# ImageShack

> imageshack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/imageshack/ | JSON https://fshy.ajam.dev/api/v1/entity/imageshack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ImageShack

- `storage/imageshack` | fails-egress | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://imageshack.com
- free tier: Free account with no published image-count or total-byte cap; the metered axis is bandwidth, not storage. 'Paid subscriptions don't impose a fixed file-count limit', and free is the same shape. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: METERED: free 10 GB/month, Basic 100 GB/mo, Pro 1,000 GB/mo, Premium 4,000 GB/mo. Over-limit hotlinks are 'temporarily blocked until your usage resets'. Fails the free-egress filter for serving; fine for cold write. | metered: yes | free allowance: 10 GB per month
- identity: email
- interface: rest
- limits note: 25 MB per image hard. 'Each image you upload must be no more than 25 megabytes in size.'
- interface detail: rest
- tooling: REST upload API plus ShareX/legacy clients, account-level API key. Historically the most-scripted image host (imageshack.us API since 2005).
- composes with: Unlimited free accounts x unmetered storage, but each throttled to 10 GB/mo egress. So shard accounts per serving shard if egress is the constraint.
- reliability: Survived the 2017 Photobucket-style breakage; still operating and still hosting free accounts in 2026. Bandwidth blocking is automatic and resets monthly.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Free account with no published image-count or total-byte cap; the metered axis is bandwidth, not storage. 'Paid subscriptions don't impose a fixed file-count limit', and free is the same shape.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'free account with basic features and a 10 GB monthly bandwidth limit'; 'Each image you upload must be no more than 25 megabytes in size'; 'Paid subscriptions don't impose a fixed file-count limit'
  - [2] 2026-10-21: '25MB file size per image' on paid tiers too
- sources:
  - [1] https://imageshack.com/faq
  - [2] https://imageshack.com/upgrade
