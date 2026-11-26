# Marginalia Search

> marginalia-search.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/marginalia-search/ | JSON https://fshy.ajam.dev/api/v1/entity/marginalia-search.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Marginalia Search

- `crawler-scraper/marginalia` | dead | evidence measured | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-22
- url https://marginalia-search.com/
- free tier: a free key by email, and a public key with an unpublished shared limit | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a query | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable: HTML; a JSON format is not served | metered: no | source: [1]
- identity: anonymous | detail: the public key route needs nothing
- interface: rest
- limits:
  - request-rate (binding): the public key hits a shared limit whose number is unpublished
- interface detail: a web search page; the documented JSON format is not returned
- tooling: not established
- composes with: Nothing chains to it until a JSON route answers
- reliability: The host moved and the old one answers an interstitial
- notes: Three routes, three failures, and the middle one is the expensive shape: a 200 with the wrong content type. A programmatic caller gets HTML and no error.
- evidence:
  - [2] 2026-10-22: 302 to https://marginalia-search.com/search
  - [3] 2026-10-22: 200 but the body is HTML: format=json is ignored
  - [4] 2026-10-22: 200, 1,023 bytes, an error page titled Wait For A Moment
- sources:
  - [1] https://marginalia-search.com/
  - [2] https://search.marginalia.nu/search?query=free+storage
  - [3] https://marginalia-search.com/search?query=free+storage&format=json
  - [4] https://old-search.marginalia.nu/search?query=free+storage&format=json
