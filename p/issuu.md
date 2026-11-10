# Issuu

> issuu.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/issuu/ | JSON https://fshy.ajam.dev/api/v1/entity/issuu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Issuu

- `storage/issuu` | fails-quota | evidence reported | binding none | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://help.issuu.com/hc/en-us/articles/16000719341595-Changes-to-free-Basic-plan-Limitation-on-the-amount-of-published-documents
  - [2] https://help.issuu.com/api/v2/help_center/en-us/articles/16000719341595.json
  - [3] https://help.issuu.com/hc/en-us/articles/12363338934939-What-happens-to-my-publications-when-I-downgrade-to-Issuu-s-free-Basic-plan
