# Lulu

> lulu.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lulu/ | JSON https://fshy.ajam.dev/api/v1/entity/lulu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lulu

- `storage/lulu` | fails-egress | evidence reported | binding none | category Print-on-demand book fulfilment
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.lulu.com
- free tier: No hard file limit. Own help page: 'We technically do not have a file limit for projects; however, the larger a file is, the longer it will take to process. We recommend keeping your interior file below 1 GB.' | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No public download path for the source file. Lulu hosts it for print production, not for retrieval. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: no stated cap; PDF only for print interiors, EPUB/PDF for ebooks; retail partners reject >100 MB.
- interface detail: Web upload only.
- tooling: Web; no API for file ingest.
- composes with: Accepts book manuscript uploads without digital download or programmatic retrieval paths.
- reliability: The uploaded file is not served back to you or anyone else — it exists only to be printed. A host that gives storage but not your bytes back is not storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No hard file limit. Own help page: 'We technically do not have a file limit for projects; however, the larger a file is, the longer it will take to process. We recommend keeping your interior file below 1 GB.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'We technically do not have a file limit for projects... We recommend keeping your interior file below 1 GB'; 'If you are publishing an ebook in Global Distribution, online retailers will often reject files over 100 MB'
- sources:
  - [1] https://help.lulu.com/en/support/solutions/articles/64000255480-publishing-the-basics
