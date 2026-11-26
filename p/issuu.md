# Issuu

> issuu.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/issuu/ | JSON https://fshy.ajam.dev/api/v1/entity/issuu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Issuu

- `storage/issuu` | fails-quota | evidence reported | binding none | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:06.405Z (live) | stale on 2026-12-04
- url https://issuu.com
- free tier: Free Basic plan (since 2025-05-29): 5 published documents max, each capped at 50 MB and 10 pages. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Reader-facing views are free and CDN-served, but documents beyond the 5 allowance stay hosted yet become "inaccessible to readers". So serving capacity is not proportional to stored bytes. | metered: yes
- identity: email
- interface: rest
- limits note: 5 published docs; 50 MB per document; 10 pages per document; only the 5 most recent remain publicly readable; cannot choose which 5.
- interface detail: rest
- tooling: Issuu API v2 exists (OAuth, upload/publish endpoints) with an official SDK github.com/issuu/issuu-api-sdk; API v1 is deprecated in favour of v2. API access does not lift the free-plan document caps.
- composes with: 5 documents x 50 MB = 250 MB per account at best; unlimited accounts gives 250 MB units. Hopeless next to 10 TiB.
- reliability: Documents over the allowance are silently made unreadable (still stored, retrievable only by the logged-in publisher), so public serving breaks without any error.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free Basic plan (since 2025-05-29): 5 published documents max, each capped at 50 MB and 10 pages.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Free Basic users are now limited to 5 published documents, with each document restricted to a maximum of 50MB in size and 10 pages'
  - [3] 2026-10-21: downgrade behaviour, publications stay hosted but unreadable
  - [1] 2026-11-19: the free Basic plan is capped at 5 published documents of at most 50 MB and 10 pages each | capture: sha256:d795f965d172dc36d6780ac8bfdd3d6336660b33a2cce5113ab7e31cbbde42e4 | quote: Free Basic users are now limited to 5 published documents, with each document restricted to a maximum of 50MB in size and 10 pages.
  - [3] 2026-11-19: downgrade to Basic leaves 5 documents of 10 pages and 50 MB each readable | capture: sha256:6d8c841976391ba2adc94ea7621ed376d4dbe5003447698d4d625fcc6806fd81 | quote: Issuu’s Basic plan limits document uploads to a maximum of 5 published documents, with each document restricted to 10 pages and a file size of 50MB.
- sources:
  - [1] https://help.issuu.com/hc/en-us/articles/16000719341595-Changes-to-free-Basic-plan-Limitation-on-the-amount-of-published-documents
  - [2] https://help.issuu.com/api/v2/help_center/en-us/articles/16000719341595.json
  - [3] https://help.issuu.com/hc/en-us/articles/12363338934939-What-happens-to-my-publications-when-I-downgrade-to-Issuu-s-free-Basic-plan
