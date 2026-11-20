# Algolia

> algolia.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/algolia/ | JSON https://fshy.ajam.dev/api/v1/entity/algolia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Algolia

- `storage/algolia` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:02.296Z (live) | stale on 2026-12-04
- url https://www.algolia.com/
- free tier: 50,000 records on the Free/Build plan (100K on the paid Grow tier); 10,000 search requests/month | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Algolia's pricing page documents a per-record size limit: the Free plan lists a 10 KB maximum size per record, and the paid plans list 'Avg 10KB/Record max 100KB'. | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Search requests are the meter, not bytes. 10,000 search requests/month is ~333/day. The most op-limited of the storage providers compared. | metered: no
- identity: email
- interface: rest, cli
- limits note: 50K records; 10K search requests/month; avg 10 KB/record, max 100 KB/record; JSON only (no binary. Base64 must be embedded in a string attribute and bloats the record); indexing operations are separately rate-limited.
- interface detail: rest
- tooling: REST API, official SDKs for ~15 languages, `algolia` CLI, InstantSearch widgets; records are JSON only
- composes with: 50K records x ~10 KB average = ~500 MB of usable payload per app. Several free apps would need several accounts. Record-size guidance is 'Avg 10KB/Record max 100KB', so the absolute ceiling is 50K x 100 KB = 5 GB, and that requires exceeding the size guidance.
- reliability: Extremely reliable CDN-backed search, but it is a search index, not a store: records are tokenized and stored in an inverted index, so storing base64 blobs both inflates size ~33% and destroys index performance. Not usable as blob storage in practice.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50,000 records on the Free/Build plan (100K on the paid Grow tier); 10,000 search requests/month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free ... 50K records included'; '100K records included then $0.40 per additional 1K records' (Grow); '10K search requests/month'; 'Avg 10KB/Record max 100KB'
  - [1] 2026-11-19: Algolia publishes a per-record size column: 10 KB on Free and 'Avg 10KB/Record max 100KB' on the paid plans | capture: sha256:3b41f16582fefda517b2a9a1b8ad3565e1e4ee6fbd0dd9dbc7161238a32bffe7 | quote: Maximum Size per Record 10 KB Avg 10KB/Record max 100KB
  - [1] 2026-11-19: the Free plan still includes 50K records and 10K search requests per month | capture: sha256:3b41f16582fefda517b2a9a1b8ad3565e1e4ee6fbd0dd9dbc7161238a32bffe7 | quote: - 10K search requests/month - 50K records included
- sources:
  - [1] https://www.algolia.com/pricing/
