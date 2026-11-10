# TheNews API

> thenewsapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thenewsapi/ | JSON https://fshy.ajam.dev/api/v1/entity/thenewsapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TheNews API

- `data-apis/thenewsapi` | qualifies-with-caveat | evidence documented | binding request-rate | category news search API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:50.592Z (live) | stale on 2026-12-03
- url https://www.thenewsapi.com/pricing
- free tier: Free plan, USD 0: 100 requests daily, 3 articles per news request, top stories, all news and similar-news endpoints, real-time and historical data. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Each call to access or search news data adds 1 request to the daily usage. The headlines endpoint is documented as available on the Standard plan and above. The next plan up is Basic at USD 19 a month for 2,500 requests daily and 25 articles per request.
- per-object cap: 3 articles per news request on the Free plan; an article carries a snippet of its first 60 characters, not the body | source: [2] | note: A result set cannot exceed 20,000 articles, so the highest page is 20,000 divided by the page size.
- retention: no retention or history window is stated for the Free plan; the pricing page lists historical data on every plan | source: [1]
- egress: not applicable | metered: no | source: [2]
- identity: email | detail: The pages say no billing details are required on the free plan.
- interface: rest
- limits:
  - request-rate (binding): 100 requests daily on the Free plan [1]
  - request-rate (binding): unverified: a per-minute limit exists (HTTP 429 for too many requests in the past 60 seconds) and its size is read from the X-RateLimit-Limit header, which needs a key [2]
  - per-object-cap: 3 articles per request on the Free plan; at most 20,000 articles in one result set [2]
- binding note: 100 requests a day is met first; at 3 articles a request that is at most 300 articles a day.
- interface detail: REST over HTTPS at api.thenewsapi.com/v1/news (top, all, similar, uuid, sources); the key goes in the api_token parameter; answers are UTF-8 JSON with dates in UTC
- endpoint: https://api.thenewsapi.com/v1/news/all
- tooling: any HTTP client
- composes with: Article metadata with a title, a description, a 60-character snippet, the source URL and a uuid; the full article is fetched from the source URL by a crawler.
- reliability: Over the daily usage the API answers HTTP 402 usage_limit_reached, and over the per-minute limit HTTP 429 rate_limit_reached; a call with no token answered HTTP 401 invalid_api_token.
- notes: Storage: no caching or storage limit is stated on the documentation, pricing or FAQ pages; the uuid of each article is meant to be stored and used to fetch it again. Bulk path: none; paging stops at 20,000 articles a result set, 3 articles a request on Free.
- evidence note: Quota, article cap, snippet length, error codes and register fields are read from first-party pages; a call with no token answered HTTP 401, so the free key was not exercised. A call with a free key would move this to measured.
- evidence:
  - [1] 2026-11-02: the Free plan allows 100 requests daily | capture: sha256:325b82c251d1536c2550203a8a253615a3fe54c4fa6e4a7ab46b9a1ad20a30be | quote: - 100 requests daily
  - [1] 2026-11-02: the Free plan returns 3 articles per news request | capture: sha256:325b82c251d1536c2550203a8a253615a3fe54c4fa6e4a7ab46b9a1ad20a30be | quote: - 3 articles / news request
  - [1] 2026-11-02: Basic, the next plan up, is USD 19 a month | capture: sha256:325b82c251d1536c2550203a8a253615a3fe54c4fa6e4a7ab46b9a1ad20a30be | quote: $ 19.00 /mo
  - [3] 2026-11-02: the free plan needs no payment details | capture: sha256:e31220e166c6f74dc04413cbf60f670c069b801fa0ad78ccf5bd17788f80d2ec | quote: Our service is 100% free to use on our free plan - no payment details are required.
  - [3] 2026-11-02: every API call that accesses or searches news data counts as 1 request against the daily usage | capture: sha256:e31220e166c6f74dc04413cbf60f670c069b801fa0ad78ccf5bd17788f80d2ec | quote: Each time the API is used to access or search news data, 1 API request is added to your daily usage.
  - [3] 2026-11-02: only a short snippet of each article is returned, with its link | capture: sha256:e31220e166c6f74dc04413cbf60f670c069b801fa0ad78ccf5bd17788f80d2ec | quote: We only provide a short snippet of articles along with their links.
  - [2] 2026-11-02: the snippet is the first 60 characters of the article body | capture: sha256:d331bf76217b393a8bb1791e7e9e64d4b1af548d178fcf45cf48295ef2050016 | quote: | `data > snippet` | The first 60 characters of the article body. |
  - [2] 2026-11-02: each article has a uuid that is meant to be stored and used to fetch the article again | capture: sha256:d331bf76217b393a8bb1791e7e9e64d4b1af548d178fcf45cf48295ef2050016 | quote: | `data > uuid` | The unique identifier for an article in our system. Store this and use it to find specific articles using our single article endpoint. |
  - [2] 2026-11-02: a result set cannot exceed 20,000 articles | capture: sha256:d331bf76217b393a8bb1791e7e9e64d4b1af548d178fcf45cf48295ef2050016 | quote: Note that the max result set can't exceed 20,000.
  - [2] 2026-11-02: too many requests in the past 60 seconds answer HTTP 429, with the limit in a response header | capture: sha256:d331bf76217b393a8bb1791e7e9e64d4b1af548d178fcf45cf48295ef2050016 | quote: | `rate_limit_reached` | `429` | Too many requests in the past 60 seconds. Rate limit and remaining requests can be found on the `X-RateLimit-Limit` header. |
  - [2] 2026-11-02: the usage limit of the plan answers HTTP 402 | capture: sha256:d331bf76217b393a8bb1791e7e9e64d4b1af548d178fcf45cf48295ef2050016 | quote: | `usage_limit_reached` | `402` | Usage limit of your plan has been reached. Usage limit and remaining requests can be found on the `X-UsageLimit-Limit` header. |
  - [4] 2026-11-02: the register form asks for an email address | capture: sha256:bb4f15371636db7561033084d9bc3217c679306dc6984efb174ce32fd0958996 | quote: Email address *
  - probe:https://api.thenewsapi.com/v1/news/top 2026-11-02: a call with no token answers HTTP 401 invalid_api_token | capture: sha256:731fc0c9352caf5d9231fe45c3bacebf2bf456c6311d32e41beb81532083031e | quote: {"error":{"code":"invalid_api_token","message":"An invalid API token was supplied."}}
- sources:
  - [1] https://www.thenewsapi.com/pricing
  - [2] https://www.thenewsapi.com/documentation
  - [3] https://www.thenewsapi.com/faq
  - [4] https://www.thenewsapi.com/register
