# archive.today

> archive.ph | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archive-2/ | JSON https://fshy.ajam.dev/api/v1/entity/archive-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## archive.today

- `crawler-scraper/archive-today` | dead | evidence measured | binding request-rate | category archive
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-22
- url https://archive.ph/
- free tier: no account and no key stated; a 429 was the answer to the first followed request | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the allowance is not published anywhere reachable
- per-object cap: not applicable: the unit is a capture | source: [2]
- retention: captures are kept indefinitely, which is the service's purpose | source: [2] | note: not independently established
- egress: not applicable: it answers HTML | metered: no | source: [2]
- identity: anonymous | detail: no account was asked for
- interface: rest
- limits:
  - request-rate (binding): 429 on the first followed request; no published allowance [1]
- limits note: an unpublished allowance is worse than a small one: there is no threshold to design against
- interface detail: an HTML route, /newest/<url>; no JSON API
- tooling: none published
- composes with: Nothing chains to it: the only programmatic route answers a challenge
- reliability: 429 with a 59,077-byte challenge page on the first followed request
- notes: The 2035 timestamp in the redirect is the finding worth keeping: a caller that trusts the redirect records a capture that does not exist. Three routes, three refusals, so the class is closed for programmatic use.
- evidence note: Three endpoint calls executed on 2026-10-22 without reading a landing page.
- evidence:
  - [1] 2026-10-22: 302 to https://archive.ph/20351231145959/http://example.com/, a timestamp in 2035, so the redirect names no real capture
  - [1] 2026-10-22: 429 with 59,077 bytes when the redirect was followed
  - [3] 2026-10-22: 301 with a zero byte body
- sources:
  - [1] https://archive.ph/newest/https://example.com
  - [2] https://archive.ph/
  - [3] https://archive.today/
