# Spaceflight News API

> spaceflightnewsapi.net | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spaceflightnewsapi/ | JSON https://fshy.ajam.dev/api/v1/entity/spaceflightnewsapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Spaceflight News API (SNAPI)

- `data-apis/spaceflight-news-api` | qualifies | evidence documented | binding request-rate | category news search API | tier Free (no key)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:50.592Z (live) | stale on 2026-12-03
- url https://api.spaceflightnewsapi.net/v4/docs/
- free tier: Free for everyone with no API key: articles, blogs and ISS reports from many spaceflight news sites, up to 500 results a request, 5 requests a second for anonymous callers. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: No daily or monthly request quota is stated; the only published limit is the anonymous throttle of 5 requests a second. The importer checks for new data every 10 minutes. The project asks commercial users to consider supporting it through Patreon or a donation.
- per-object cap: 500 results a request: a limit above 500 is answered with 500 results and a next link at limit=500 | source: [2] | note: The offset parameter is at most 10,000; further back, filter on published_at_lt with the published_at of the last result.
- retention: the full archive is served: the article list counted 36741 articles when read | source: [3]
- egress: not applicable | metered: no | source: [3]
- identity: anonymous | detail: No account and no key: a plain GET answered HTTP 200 with articles.
- interface: rest, graphql
- limits:
  - request-rate (binding): 5 requests a second for anonymous callers [4]
  - retention-clamped: a limit above 500 is clamped to 500 results a request probe:https://api.spaceflightnewsapi.net/v4/articles/?limit=2000
  - per-object-cap: offset at most 10,000; filter on published_at_lt to go further back [2]
- binding note: 5 requests a second is the only published limit; 36741 articles at 500 results a request is 74 requests (36741 / 500, rounded up).
- interface detail: REST over HTTPS at api.spaceflightnewsapi.net/v4 (articles, blogs, reports, info) with an OpenAPI 3 schema at /v4/schema/, and a GraphQL endpoint at /v4/graphql/
- endpoint: https://api.spaceflightnewsapi.net/v4/articles/
- tooling: any HTTP client or GraphQL client; the OpenAPI schema generates a client
- composes with: Article, blog and report metadata with a summary, the source URL and Launch Library 2 launch and event ids; the full article is fetched from the source URL by a crawler.
- reliability: Responses carry cache-control max-age 600; the throttle for anonymous callers is stated in the project changelog and was not exercised by a burst.
- notes: Storage: no storage or caching limit is stated in the documentation or the FAQ. Bulk path: page the article list at limit=500 with offset up to 10,000, then filter on published_at_lt with the published_at of the last result; 74 requests cover 36741 articles.
- evidence note: The no-key access and the page-size clamp were read from live answers; the 5 requests a second throttle is read from the project changelog and was not exercised, so the record stays documented.
- evidence:
  - [1] 2026-11-02: the API is free for everyone | capture: sha256:6727f7d4eeb5d68a785c49d2dcbe241b98864e3f4d6ad1470a661ef5c22de1d8 | quote: Yes, SNAPI is fully free to use for everyone.
  - [1] 2026-11-02: no API key is needed | capture: sha256:6727f7d4eeb5d68a785c49d2dcbe241b98864e3f4d6ad1470a661ef5c22de1d8 | quote: No API key is required to use SNAPI.
  - [1] 2026-11-02: new articles appear within 10 minutes | capture: sha256:6727f7d4eeb5d68a785c49d2dcbe241b98864e3f4d6ad1470a661ef5c22de1d8 | quote: The importer runs every 10 minutes to check for new data, so new articles can take up to 10 minutes to appear in the API.
  - [4] 2026-11-02: anonymous requests are throttled to 5 per second | capture: sha256:c3ffbd2485f5afb3d590848d847edef658d4590d93bac86e6a33aad10126ff51 | quote: Update API throttling settings to limit anonymous requests to 5 per second
  - [2] 2026-11-02: the offset parameter is at most 10,000, with published_at_lt for going further | capture: sha256:9404d81642bc28208880f59d9a694c3068375e0b553da309f39532c97d334a03 | quote: The initial index from which to return the results, at most 10,000.
  - [3] 2026-11-02: a GraphQL endpoint is offered beside REST | capture: sha256:3e0b91a97475a1f36bbbf229c89afdfa49af3e2357e01f4227cf7aee27881a17 | quote: The Spaceflight News API also has GraphQL support available!
  - probe:https://api.spaceflightnewsapi.net/v4/articles/?limit=1 2026-11-02: a keyless GET answered with articles and counted 36741 of them | capture: sha256:78ac46775a76ee181b4fe71494f5f482989c464083fdf2b3bb90cccaf6e6c23f | quote: {"count":36741,
  - probe:https://api.spaceflightnewsapi.net/v4/articles/?limit=2000 2026-11-02: a request for limit=2000 was clamped: the next link is at limit=500 | capture: sha256:343b519086f583279b4da4e2fbc157276b257e8626bcb056b22d10ee5fc5f831 | quote: "next":"https://api.spaceflightnewsapi.net/v4/articles/?limit=500&offset=500"
- sources:
  - [1] https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_SNAPI.md
  - [2] https://api.spaceflightnewsapi.net/v4/schema/
  - [3] https://api.spaceflightnewsapi.net/v4/docs/
  - [4] https://github.com/TheSpaceDevs/spaceflightnewsapi/blob/main/CHANGELOG.md
