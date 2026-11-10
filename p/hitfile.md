# Hitfile

> hitfile.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hitfile/ | JSON https://fshy.ajam.dev/api/v1/entity/hitfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hitfile

- `storage/hitfile` | qualifies-with-caveat | evidence inferred | binding per-ip-shaping | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://hitfile.net
- free tier: Homepage headline: 'Your free and unlimited file storage'. No numeric total quota published anywhere on the site. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads capped ~5 GB/day at roughly 55-60 KB/s; Turbo 40 GB/day, 600 GB/month. No per-GB charge. | metered: no | free allowance: 600 GB per month
- identity: anonymous
- interface: ftp
- limits:
  - per-ip-shaping (binding): 60 KB/s [1]
- limits note: Per-file cap not published on the pages read (unverified). Retention ends on 'storage time expiration'. Free speed ~55-60 KB/s, one download per IP with queueing.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: wrapper-only
- tooling: Same Turbobit-family stack (Uploader app, FTP). No documented public API.
- composes with: Sister host of Turbobit with the same 'unlimited volume' claim; chain = N email accounts, serving bounded by per-IP/day caps.
- reliability: Blog/inventory claim only. 'unlimited' is a headline, with no docs page stating it and no per-file number anywhere. Treat the quota as unverified.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Your free and unlimited file storage'
  - [2] 2026-10-21: 'In free mode, however, the maximum file download is approximately 55-60 Kbytes/s'; Turbo 40 GB/day, 600 GB/month
  - [2] 2026-10-21: 'storage time expiration' listed as a removal reason; no per-file cap stated (unverified: not published)
- sources:
  - [1] https://hitfile.net/
  - [2] https://hitfile.net/faq
