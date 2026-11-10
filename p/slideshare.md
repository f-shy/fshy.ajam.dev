# SlideShare

> slideshare.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/slideshare/ | JSON https://fshy.ajam.dev/api/v1/entity/slideshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SlideShare

- `storage/slideshare` | fails-egress | evidence reported | binding per-object-cap | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.slideshare.net
- free tier: 300 MB max per file (PDF/PPT/DOC), 300 slides for presentations; account-level storage not published. Uploads are currently disabled service-wide. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 300 MB max per file | bytes: 300000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Public viewing is free, but SlideShare has no direct-file download for viewers; slides are served as rendered images inside a JS viewer. | metered: no
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 300 MB/file [1]
- limits note: 300 MB/file; 300 slides; no videos; hard requirement of an active Scribd account in good standing.
- interface detail: wrapper-only
- tooling: No API; web upload only, and that form is offline.
- composes with: 300 MB/record x unlimited records would be workable, but uploads are unavailable, so the multiplier is currently zero.
- reliability: Own help centre states: 'Slideshare presentation uploads are unavailable right now'. The ingest path is down, so this is not a storage target at all today.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 300 MB max per file (PDF/PPT/DOC), 300 slides for presentations; account-level storage not published. Uploads are currently disabled service-wide.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Your file's total size cannot exceed 300 MB'; 'limited to a maximum of 300 slides'
  - [2] 2026-10-21: 'Slideshare presentation uploads are unavailable right now.'
- sources:
  - [1] https://support.scribd.com/hc/en-us/articles/360055259612-Supported-SlideShare-file-formats-and-sizes
  - [2] https://support.scribd.com/hc/en-us/articles/360055667671-Uploading-content-to-Slideshare
