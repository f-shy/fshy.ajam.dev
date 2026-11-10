# urlreader.dev

> urlreader.dev | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/urlreader/ | JSON https://fshy.ajam.dev/api/v1/entity/urlreader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## urlreader.dev

- `crawler-scraper/urlreader` | dead | evidence measured | binding request-rate | category reader and extractor API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-22
- url https://urlreader.dev/
- free tier: none: the host does not resolve | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: nothing was asked for
- interface: unknown
- limits:
  - request-rate (binding): no name resolution, so no request [1]
- interface detail: no DNS record
- tooling: not established
- composes with: the same as tooling
- reliability: curl exit 6, could not resolve host, on 2026-10-22
- notes: Listed in catalogues of free reader services. Testing confirms the service endpoint is unreachable, preventing unauthenticated retrieval.
- evidence note: one call; the name did not resolve
- evidence:
  - [2] 2026-10-22: curl exit 6, `Could not resolve host`: the service named in second-hand lists does not exist at that name
- sources:
  - [1] https://urlreader.dev/
  - [2] https://urlreader.dev/https://example.com
