# urlscan.io

> urlscan.io | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/urlscan/ | JSON https://fshy.ajam.dev/api/v1/entity/urlscan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## urlscan.io

- `crawler-scraper/urlscan` | qualifies-with-caveat | evidence measured | binding request-rate | category archive
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:02:38.436Z (live) | stale on 2027-01-02
- url https://urlscan.io/
- free tier: keyless, counted per IP address: 500 searches a day (100 an hour, 30 a minute) and 500 result retrievals a day (250 an hour, 20 a minute), at most 100 results a search | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: a free account (API Only) raises the daily quotas to 1,000 searches, 10,000 result requests, 5,000 public, 1,000 unlisted and 50 private scans
- per-object cap: not applicable: the unit is a scan | source: [2]
- retention: scan results are public unless unlisted | source: [2]
- egress: not applicable: JSON and the scanned DOM | metered: no | source: [2]
- identity: anonymous | detail: search and result retrieval answer with no key at per-IP quotas; submitting scans and the larger free quotas need a user account and an API key
- interface: rest
- limits:
  - request-rate (binding): keyless search 30 a minute, 100 an hour and 500 a day per IP address [1]
  - request-rate (binding): keyless result retrieval 20 a minute, 250 an hour and 500 a day per IP address [1]
- limits note: a keyless search answer carries X-Rate-Limit headers scoped to ip-address, with a concurrency limit of 10
- binding note: keyless search: 30 a minute and 500 a day per IP address
- interface detail: REST search and result APIs
- tooling: REST with an API-Key header or none; X-Rate-Limit headers on each rate-limited answer; a quotas endpoint at /api/v1/quotas
- composes with: Provides historical scan snapshots alongside Cloudflare URL Scanner, retrieving historical page captures when general web archives contain no records.
- reliability: no reliability event recorded
- notes: A scan is a page's DOM and resource list as somebody else's browser saw it, which is why it is the only source for a page that a challenge keeps from every live fetch.
- evidence note: keyless quotas measured on the quotas and search endpoints; the free account's quotas read on the pricing page
- evidence:
  - [3] 2026-10-22: 200, 1,953 bytes, results[] with a canonical URL, no key
  - probe:https://urlscan.io/api/v1/quotas 2026-10-30: keyless quotas are counted per IP address: search 30 a minute, 100 an hour, 500 a day; retrieve 20 a minute, 250 an hour, 500 a day; at most 100 results a search | capture: sha256:dd409d5ce5df91c62fcd1fff0dbc9430a201d9c0b93374db614e75d0d4e15057 | quote: "scope": "ip-address"
  - [4] 2026-10-30: the free plan allows 1,000 searches a day; the same table lists 10,000 result requests, 5,000 public, 1,000 unlisted and 50 private scans | capture: sha256:7b464be57c209cecc893c3922810d655d364dfb5ec8ebadabba751557fc4a009 | quote: Only syntactically correct searches count against your quota. | 1,000 | 12,500 | 150,000 | 500,000 | 500,000 |
  - [4] 2026-10-30: the Free plan costs USD 0 | capture: sha256:7b464be57c209cecc893c3922810d655d364dfb5ec8ebadabba751557fc4a009 | quote: | Monthly Price | $0 | N/A | $1,250 | $2,500 | $5,000 |
  - probe:https://urlscan.io/api/v1/search/?q=domain:example.com&size=1 2026-10-30: the keyless search answered 200 with X-Rate-Limit-Limit 30 a minute, scope ip-address and concurrency limit 10 | capture: sha256:fa6a902132858259d927be964b1ef254623c6c0125aa4e9d5c785ab611198252 | quote: "x-rate-limit-concurrency-limit": "10"
  - [5] 2026-10-30: calls with no account get small quotas; the full API wants an account and a key | capture: sha256:e122a22f0fe8a83066b201e3509be6e045737c2a63c0ea8e802a0ff7a40ef67a | quote: Unauthenticated users only receive minor quotas for API calls.
  - [6] 2026-10-30: the quotas endpoint reports the caller's limits | capture: sha256:89f264ea8998a0afe18f0e0ed113b8f1814233da97ff733fb3797f4171361903 | quote: You can query your current limits and quotas via the [API Quotas](https://urlscan.io/api/v1/quotas) endpoint.
  - [7] 2026-10-30: a search with no account returns at most 100 results | capture: sha256:638fd59e8850b556922eb68f928436fe5029f626d273d1d606ccbfd15d2a2d80 | quote: Anon Users: 100 results max
  - [6] 2026-10-30: unauthenticated requests are limited per IP address | capture: sha256:89f264ea8998a0afe18f0e0ed113b8f1814233da97ff733fb3797f4171361903 | quote: Either `user` (with cookie or API-Key header) or `ip-address` for unauthenticated requests.
  - probe:https://urlscan.io/api/v1/search/?q=domain:example.com&size=1 2026-10-30: the keyless search API answered 200 with a 30-a-minute limit | capture: sha256:fa6a902132858259d927be964b1ef254623c6c0125aa4e9d5c785ab611198252 | quote: "x-rate-limit-limit": "30"
  - [1] 2026-11-01: the quotas endpoint, read with no key, answers scope ip-address with search limits of 500 a day, 100 an hour and 30 a minute | capture: sha256:3051cba5e2da76d2ad4bbb1467e9a992d6b50d88f42d3a9dc686d15306eedbf4 | quote: "scope": "ip-address", "limits": { "search": { "day": { "limit": 500, "percent": 0, "remaining": 500, "used": 0 }, "hour": { "limit": 100, "percent": 0, "remaining": 100, "used": 0 }, "minute": { "limit": 30,
  - [1] 2026-11-01: the same keyless answer limits result retrieval to 500 a day, 250 an hour and 20 a minute | capture: sha256:3051cba5e2da76d2ad4bbb1467e9a992d6b50d88f42d3a9dc686d15306eedbf4 | quote: "retrieve": { "day": { "limit": 500, "percent": 0, "remaining": 500, "used": 0 }, "hour": { "limit": 250, "percent": 0, "remaining": 250, "used": 0 }, "minute": { "limit": 20,
  - [1] 2026-11-01: the same keyless answer caps a search at 100 results | capture: sha256:3051cba5e2da76d2ad4bbb1467e9a992d6b50d88f42d3a9dc686d15306eedbf4 | quote: "maxSearchResults": 100,
- sources:
  - [1] https://urlscan.io/api/v1/quotas
  - [2] https://urlscan.io/
  - [3] https://urlscan.io/api/v1/search/?q=domain:example.com&size=1
  - [4] https://urlscan.io/pricing/
  - [5] https://urlscan.io/docs/api/
  - [6] https://docs.urlscan.io/pages/api-rate-limits
  - [7] https://urlscan.io/blog/2021/12/02/search-api-limitations-for-free-users/
