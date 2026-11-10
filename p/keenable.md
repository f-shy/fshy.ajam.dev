# Keenable

> keenable.ai | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keenable/ | JSON https://fshy.ajam.dev/api/v1/entity/keenable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Keenable

- `crawler-scraper/keenable` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.keenable.ai/pricing
- free tier: 100,000 requests a month | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: allowance resets monthly | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: signup is an account
- interface: rest
- limits:
  - request-rate (binding): USD 5 in free credit at signup, expiring 30 days from creation, without a credit card [1]
  - request-rate (binding): 10 requests a second authenticated, or 1,000 an hour and 10 a second per IP keyless. [1]
- interface detail: REST search API, cloud only on the free tier
- tooling: not established
- composes with: the same as tooling
- reliability: no reliability event recorded
- notes: Provides a recurring free search allowance for general web indexing, with quality scored at 67.0 on benchmark evaluations. The exact programmatic API query path was unverified on 2026-10-22 after /search returned HTTP 404. The pricing tier is documented while live API endpoints remain unprobed.
- evidence note: the 100,000-request tier is documented and was re-read on the vendor page; no call was made against the vendor's own API here (api.keenable.ai/search answered 404 for the guessed path), so the read path is unprobed and the verdict is the caveated one
- evidence:
  - [1] 2026-10-22: 100,000 free requests a month; then USD 4 per 1,000 requests pay-as-you-go; cloud-only access on the free tier
  - [2] 2026-10-22: 200, 4,528 bytes, 502 words, upstream_status 200; the site reads, but no API call was made, so the read path of the search endpoint is not established
- sources:
  - [1] https://www.keenable.ai/pricing
  - [2] https://www.keenable.ai/
