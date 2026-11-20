# zilliz cloud

> zilliz.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zilliz/ | JSON https://fshy.ajam.dev/api/v1/entity/zilliz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zilliz cloud / milvus (free tier)

- `storage/zilliz-cloud-milvus` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-20T03:57:27.923Z (live) | stale on 2026-12-05
- url https://docs.zilliz.com/docs/select-zilliz-cloud-service-plan
- free tier: none reachable: The free tier is denominated in Capacity Units (compute), not bytes, and the product stores embeddings rather than arbitrary objects. No blob/object API, no anonymous download, so it fails… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: The free tier is denominated in Capacity Units (compute), not bytes, and the product stores embeddings rather than arbitrary objects. No blob/object API, no anonymous download, so it fails t Re-check 2026-11-20: the source URL https://docs.zilliz.com/docs/select-zilliz-cloud-service-plan answered HTTP 404 ("This page doesn't exist or has been moved."); no first-party page at the cited URL states the tier today.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: The free tier is denominated in Capacity Units (compute), not bytes, and the product stores embeddings rather than arbitrary objects. No blob/object API, no anonymous download, so it fails…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The free tier is denominated in Capacity Units (compute), not bytes, and the product stores embeddings rather than arbitrary objects. No blob/object API, no anonymous download, so it fails…
  - [1] 2026-11-20: the first-party plan page answered HTTP 404 on 2026-11-20, so the quoted plan claim can no longer be re-read at its source | capture: sha256:a363436b3e916287034880ef11e1ab8ca4812bff27509d77cb622c2c47e5944c | quote: This page doesn't exist or has been moved.
- sources:
  - [1] https://docs.zilliz.com/docs/select-zilliz-cloud-service-plan
