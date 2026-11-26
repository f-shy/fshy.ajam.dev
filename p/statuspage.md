# Fauna

> statuspage.io | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/statuspage/ | JSON https://fshy.ajam.dev/api/v1/entity/statuspage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fauna

- `databases-kv/fauna` | dead | evidence measured | binding write-gated | category document database
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-12-22
- url https://fauna.statuspage.io/
- free tier: none. The service is shut down | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the service no longer exists
- retention: the service was shut down on 2025-05-30 | days: 0 | source: [1]
- egress: not applicable: the service no longer exists | metered: no | source: [1]
- identity: anonymous | detail: no registration is possible
- interface: rest
- limits:
  - write-gated (binding): the service shut down on 2025-05-30; no new databases can be created [1]
- interface detail: the service is offline; the FQL API no longer answers
- tooling: none; the recommended path was to export before the shutdown
- composes with: no path: the provider is gone
- reliability: the provider announced in March 2025 that it could not raise the capital to keep running, and shut down on 2025-05-30
- notes: A well-known serverless database whose free tier no longer exists: the service shut down on 2025-05-30. The record stays so that the name is answered with its evidence instead of being researched again.
- evidence note: Fauna's own status page returned 200 with the banner 'The Fauna Service is shut down'.
- evidence:
  - probe:https://fauna.statuspage.io/ 2026-10-22: 200, 2989 bytes, carrying 'The Fauna Service is shut down' and linking the shutdown incident; read 2026-10-22
  - [2] 2026-10-22: the end-of-life FAQ was in search index and now returns 530, consistent with a withdrawn service
- sources:
  - [1] https://fauna.statuspage.io/
  - [2] https://docs.fauna.com/fauna/current/eol-faq/
