# Marketaux

> marketaux.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/marketaux/ | JSON https://fshy.ajam.dev/api/v1/entity/marketaux.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Marketaux

- `data-apis/marketaux` | qualifies-with-caveat | evidence documented | binding request-rate | category financial news API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:50.592Z (live) | stale on 2026-12-03
- url https://www.marketaux.com/pricing
- free tier: Free plan, USD 0: 100 requests daily, 3 articles per news request, global market news with entity metadata; the Market Stats endpoints allow 0 entities per stat request. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Each call to access financial news or analysis data adds 1 request to the daily usage. The entity-stats, trending-entities and time-series endpoints are documented as available on Standard and above. The next plan up is Basic at USD 29 a month for 2,500 requests daily and 20 articles per request.
- per-object cap: 3 articles per news request on the Free plan; an article carries a short snippet of its body, not the body | source: [2] | note: A result set cannot exceed 20,000 articles; the source and entity list endpoints return 50 rows a page.
- retention: no history window is stated for the Free plan | source: [1]
- egress: not applicable | metered: no | source: [2]
- identity: email | detail: The pages say no billing details are required on the free plan.
- interface: rest
- limits:
  - request-rate (binding): 100 requests daily on the Free plan [1]
  - request-rate (binding): unverified: a per-minute limit exists (HTTP 429 for too many requests in the past 60 seconds) and its size is read from the X-RateLimit-Limit header, which needs a token [2]
  - per-object-cap: 3 articles per request on the Free plan; at most 20,000 articles in one result set [2]
- binding note: 100 requests a day is met first; at 3 articles a request that is at most 300 articles a day.
- interface detail: REST over HTTPS at api.marketaux.com/v1 (news/all, news/similar, news/uuid, news/sources, entity search and metadata lists); the token goes in the api_token parameter; answers are UTF-8 JSON with dates in UTC
- endpoint: https://api.marketaux.com/v1/news/all
- tooling: any HTTP client
- composes with: News articles tagged with the stock, index, currency and crypto entities they mention, with a sentiment score for each entity; the full article is fetched from the source URL by a crawler.
- reliability: Over the daily usage the API answers HTTP 402 usage_limit_reached, and over the per-minute limit HTTP 429 rate_limit_reached; a call with no token answered HTTP 401.
- notes: Storage: no caching or storage limit is stated on the documentation, pricing or FAQ pages; the uuid of each article is meant to be stored and used to fetch it again. Bulk path: none; paging stops at 20,000 articles a result set, 3 articles a request on Free.
- evidence note: Quota, article cap, error codes and register fields are read from first-party pages; a call with no token answered HTTP 401, so the free token was not exercised. A call with a free token would move this to measured.
- evidence:
  - [1] 2026-11-02: the Free plan allows 100 requests daily | capture: sha256:24947a94ef9cb7255fbeaa8338a8cfec1866ae0ca4c3a1a8cf01bb01d1dfaa57 | quote: - 100 requests daily
  - [1] 2026-11-02: the Free plan returns 3 articles per news request | capture: sha256:24947a94ef9cb7255fbeaa8338a8cfec1866ae0ca4c3a1a8cf01bb01d1dfaa57 | quote: - 3 articles / news request
  - [1] 2026-11-02: the Free plan gets no entities per stat request, so the stats endpoints are not usable on it | capture: sha256:24947a94ef9cb7255fbeaa8338a8cfec1866ae0ca4c3a1a8cf01bb01d1dfaa57 | quote: - 0 entities per stat request
  - [1] 2026-11-02: Basic, the next plan up, is USD 29 a month | capture: sha256:24947a94ef9cb7255fbeaa8338a8cfec1866ae0ca4c3a1a8cf01bb01d1dfaa57 | quote: $ 29.00 /mo
  - [3] 2026-11-02: the free plan needs no payment details | capture: sha256:3c25bcdfb44b484bfb39e6562ba2bdee20d9ea465704a4449b55b319a31bc7df | quote: Our service is 100% free to use on our free plan - no payment details are required.
  - [3] 2026-11-02: every API call that accesses financial news or analysis data counts as 1 request against the daily usage | capture: sha256:3c25bcdfb44b484bfb39e6562ba2bdee20d9ea465704a4449b55b319a31bc7df | quote: Each time the API is used to access financial news or analysis data, 1 API request is added to your daily usage.
  - [3] 2026-11-02: only a short snippet of each article is returned, with its link | capture: sha256:3c25bcdfb44b484bfb39e6562ba2bdee20d9ea465704a4449b55b319a31bc7df | quote: We only provide a short snippet of articles along with their links.
  - [2] 2026-11-02: a result set cannot exceed 20,000 articles | capture: sha256:3944d0a6351ddd2ecf52efe13273a443ae8bb55012a6dafdcfbdd70e81f1f31d | quote: Note that the max result set can't exceed 20,000.
  - [2] 2026-11-02: the entity stats endpoints are available on Standard and above | capture: sha256:3944d0a6351ddd2ecf52efe13273a443ae8bb55012a6dafdcfbdd70e81f1f31d | quote: ## Entity Stats (time series) Available on: Standard and above
  - [2] 2026-11-02: too many requests in the past 60 seconds answer HTTP 429, with the limit in a response header | capture: sha256:3944d0a6351ddd2ecf52efe13273a443ae8bb55012a6dafdcfbdd70e81f1f31d | quote: | `rate_limit_reached` | `429` | Too many requests in the past 60 seconds. Rate limit and remaining requests can be found on the `X-RateLimit-Limit` header. |
  - [2] 2026-11-02: the usage limit of the plan answers HTTP 402 | capture: sha256:3944d0a6351ddd2ecf52efe13273a443ae8bb55012a6dafdcfbdd70e81f1f31d | quote: | `usage_limit_reached` | `402` | Usage limit of your plan has been reached. Usage limit and remaining requests can be found on the `X-UsageLimit-Limit` header. |
  - [2] 2026-11-02: each article has a uuid that is meant to be stored and used to fetch the article again | capture: sha256:3944d0a6351ddd2ecf52efe13273a443ae8bb55012a6dafdcfbdd70e81f1f31d | quote: | `data > uuid` | The unique identifier for an article in our system. Store this and use it to find specific articles using our single article endpoint. |
  - [4] 2026-11-02: the register form asks for an email address | capture: sha256:17533f90d56edc3d72a345e9b440406a8d8d44bfe09c9ba8f6c9ed0dd939296b | quote: Email address *
  - probe:https://api.marketaux.com/v1/news/all 2026-11-02: a call with no token answers HTTP 401 | capture: sha256:b5cbd27c79ef202e82722ffa01ad5fc7187845f29b222e07742abd9c8aac2a39 | quote: "status": 401
- sources:
  - [1] https://www.marketaux.com/pricing
  - [2] https://www.marketaux.com/documentation
  - [3] https://www.marketaux.com/faq
  - [4] https://www.marketaux.com/register
