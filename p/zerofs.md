# ZeroFS

> zerofs.link | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zerofs/ | JSON https://fshy.ajam.dev/api/v1/entity/zerofs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeroFS

- `storage/zerofs` | qualifies-with-caveat | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zerofs.link
- free tier: Unlimited storage for active files; no file size limit. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Files inactive for 15 days are deleted. | days: 15 | source: [1] | note: not stated
- egress: No stated bandwidth cap; no speed limit claimed on the uploader. | metered: no
- identity: anonymous
- interface: s3, rest, webdav, rclone
- limits note: No file size limit. Files inactive for 15 days are deleted. No login required.
- interface detail: rest
- tooling: Anonymous browser uploader with region selector. No public REST API, rclone, WebDAV, or S3 backend is documented. Optional account identifier tracks uploaded files.
- composes with: Account-less uploads, so unlimited identities; the binding constraint is the 15-day inactivity deletion, which needs a re-access cron per file. At unlimited file size this is >= 500 GB per 'unit' trivially.
- reliability: Very new, looks like a Buzzheavier-style clone (same 'we only act on local court orders' posture, same lost-ID-never-recovered model). 15-day inactivity window makes it unusable for cold archive without active touching; untested for sustained throughput.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'File size limit? None.' / 'How much storage? Unlimited for active files.' / 'Are files deleted? Yes. If a file is inactive for 15 days, it's gone.'
  - [2] 2026-10-21: probe: GET -> 200
- sources:
  - [1] https://zerofs.link/faq/
  - [2] https://zerofs.link/
