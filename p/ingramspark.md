# IngramSpark

> ingramspark.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ingramspark/ | JSON https://fshy.ajam.dev/api/v1/entity/ingramspark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IngramSpark

- `storage/ingramspark` | fails-egress | evidence reported | binding per-object-cap | category Print-on-demand book distribution
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ingramspark.com
- free tier: 1.5 GB via web upload ('web upload for files up to 1.5 GB, zip/stuff compression accepted'); user guide says files should not exceed 1.6 GB; ebook interiors 100 MB or less. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 1.5 GB | bytes: 1500000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: None. File exists for print production. | metered: no
- identity: email | detail: email
- interface: ftp
- limits:
  - per-object-cap (binding): per-object-cap 1.5 GB [1]
- limits note: per-object-cap 1.5 GB (web), 1.6 GB stated maximum; ebook interior 100 MB; cover image upload 5 MB.
- interface detail: Web upload; FTP for larger.
- tooling: Web/FTP.
- composes with: 1.5 GB ingest with zero retrieval = archive-blind. Not usable.
- reliability: Same rule-2/rule-4 failure as Lulu: write-only, with no read-back path. Also charges a per-title setup fee for some paths.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1.5 GB via web upload ('web upload for files up to 1.5 GB, zip/stuff compression accepted'); user guide says files should not exceed 1.6 GB; ebook interiors 100 MB or less.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'web upload for files up to 1.5 GB (zip/stuff compression accepted)'
  - [2] 2026-10-21: 'Size: 100MB or less' for ebook interiors; 'an image that is 5MB or less' for covers
  - [3] 2026-10-21: IngramSpark user guide: 'A file size should not exceed 1.6 GB'
- sources:
  - [1] https://www.ingramspark.com/hubfs/downloads/file-creation-guide.pdf
  - [2] https://www.ingramspark.com/blog/file-requirements-for-ebooks
  - [3] https://www.scribd.com/document/908999722/User-Guide
