# SearchApi

> searchapi.io | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/searchapi/ | JSON https://fshy.ajam.dev/api/v1/entity/searchapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SearchApi

- `crawler-scraper/searchapi` | trial-only | evidence reported | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:01:53.531Z (live) | stale on 2026-11-17
- url https://www.searchapi.io/pricing
- free tier: 100 free requests on signup, no credit card required; the vendor's launch announcement describes them as complimentary searches for newly registered users; a third-party review states they are granted once, not monthly | unit: requests | metered on: request-count | read on: 2026-11-01 | source: [1] | note: Only searches that answer 200 are charged.
- per-object cap: not applicable | source: [1]
- retention: unverified: no first-party page read states whether the 100 free requests renew; the launch announcement describes them as for newly registered users; third-party pages disagree, one stating one-time and three stating monthly | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: the signup form asks for a full name, an email and a password, or GitHub or Google sign-in; no credit card required
- interface: rest
- limits:
  - request-rate (binding): up to 20% of the plan's credits each hour; on the 100 free requests, 20% of 100 = 20 requests an hour [1]
  - request-rate (binding): 100 free requests; Developer plan USD 40 a month for 10,000 searches, USD 4 per 1,000 [1]
- binding note: the 100 free requests run out before the hourly cap matters: 100 / 20 an hour = 5 hours
- interface detail: GET https://www.searchapi.io/api/v1/search?engine=google with api_key as a query parameter or a Bearer header; Google verticals, Bing, Baidu, Yandex, DuckDuckGo and other engines through the engine parameter
- endpoint: part of interface detail
- tooling: plain HTTP GET with an api_key query parameter or an Authorization: Bearer header
- composes with: A one-time 100-request test of parsed Google and other engine results; the Developer plan at USD 4 per 1,000 is the paid reference
- reliability: a keyless call answered 401 with an invalid-key message; failed requests are not billed
- notes: The paid tiers fall from USD 4 to USD 1 per 1,000 searches at 5 million a month. The hourly cap is a share of the plan's credits, so it scales with the plan.
- evidence note: the 100 free requests, the no-card statement and the hourly cap are first-party; the vendor's launch announcement describes the 100 as complimentary searches for newly registered users, but no first-party page read states whether they renew; that they are granted once and not monthly rests on a third-party review, while three other third-party pages state a monthly free tier; a first-party statement of the cadence would raise it to documented
- evidence:
  - [1] 2026-10-30: the signup grant is 100 free requests | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: Sign up for 100 free requests
  - [1] 2026-10-30: no credit card is required | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: No credit card required. No commitment. Cancel anytime.
  - [1] 2026-10-30: at most 20% of a plan's credits can be used in an hour | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: Please note that you can utilize only up to 20% of your plan's credits each hour.
  - [1] 2026-10-30: the Developer plan costs USD 4 per 1,000 searches | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: $4 per 1,000 searches
  - [1] 2026-10-30: only searches that answer 200 are charged | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: Only successful searches with a 200 status code incur charges.
  - [2] 2026-10-30: the signup offers GitHub and Google sign-in beside a name, email and password form | capture: sha256:77f652767e7b7fc7744b8e2b6bb0d596740d85b110b07d82374f8883abc457af | quote: Sign in with GitHub Sign in with Google
  - [3] 2026-10-30: a third-party review states the 100 requests are one-time | capture: sha256:bb0fe7b4feb65d9ef0a8d99e72b589e9d580e14ee1e253030e2b4099676165f3 | quote: Free tier is 100 requests, one time, with no credit card (SearchApi pricing, verified August 2026)
  - [4] 2026-10-30: the Google search endpoint | capture: sha256:5bb48315846588e16fc19eff797b24f0212ae377f32bd7bcae1b9d6e2f59a027 | quote: GET /api/v1/search?engine=google
  - probe:www.searchapi.io/api/v1/search 2026-10-30: a keyless call answered 401 with an invalid-key message | capture: sha256:69ea80fd39a31364911e0539cc4c4df1ab19272361bd1293572f8c474b998c02 | quote: "error": "Invalid API key."
  - [5] 2026-11-01: the vendor's May 2023 launch announcement describes the 100 free searches as complimentary searches that newly registered users can use to test the platform | capture: sha256:2e5626ef766519b12a6e7ce7772436ea0a173151921015710aace8e1e2a0f9a2 | quote: 100 free searches - newly registered users can test our platform with 100 complimentary searches.
  - [1] 2026-11-01: the pricing page offers 100 free requests on signup and states no credit card is required | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: No credit card required. No commitment. Cancel anytime. Sign up for 100 free requests
  - [1] 2026-11-01: at most 20% of a plan's credits can be used in an hour | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: Please note that you can utilize only up to 20% of your plan's credits each hour.
  - [1] 2026-11-01: the Developer plan costs USD 40 a month for 10,000 searches, USD 4 per 1,000 | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: $4 per 1,000 searches ... $40 / month ... 10,000 Searches
  - [1] 2026-11-01: failed requests are not billed and only searches that answer 200 are charged | capture: sha256:e523b12a00ea900245746a3de70a3870fdba159b39d9a1a2a2012948e2390b6a | quote: Therefore, you won't be billed for failed requests. Only successful searches with a 200 status code incur charges.
  - [2] 2026-11-01: the signup form asks for a full name, an email and a password, with GitHub and Google sign-in beside it | capture: sha256:766e39c41f7771bb030f5a1e3fa6d3e359f94cfb00a1d5e8505e4d7b77e00885 | quote: Full name Email Password (6 characters minimum) ... Sign in with GitHub Sign in with Google
  - [4] 2026-11-01: the Google search endpoint is GET /api/v1/search?engine=google | capture: sha256:5bb48315846588e16fc19eff797b24f0212ae377f32bd7bcae1b9d6e2f59a027 | quote: GET /api/v1/search?engine=google
  - [4] 2026-11-01: the search endpoint takes the api_key as a query parameter or in an Authorization Bearer header | capture: sha256:5bb48315846588e16fc19eff797b24f0212ae377f32bd7bcae1b9d6e2f59a027 | quote: Use it as a query parameter (`https://www.searchapi.io/api/v1/search?api_key=YOUR_API_KEY`) or in the Authorization header (`Bearer YOUR_API_KEY`).
  - probe:www.searchapi.io/api/v1/search 2026-11-01: a keyless call to the search endpoint answered 401 with an invalid-key message | capture: sha256:69ea80fd39a31364911e0539cc4c4df1ab19272361bd1293572f8c474b998c02 | quote: "error": "Invalid API key."
  - [3] 2026-11-01: a third-party review states the 100 requests are one-time | capture: sha256:bb0fe7b4feb65d9ef0a8d99e72b589e9d580e14ee1e253030e2b4099676165f3 | quote: Free tier is 100 requests, one time, with no credit card (SearchApi pricing, verified August 2026)
  - [6] 2026-11-01: a third-party README states the free tier is 100 searches a month, which conflicts with the one-time statement | capture: sha256:72f4bbb330334eea114d4acb012d6acd60706ac747cd76748967b6e313c9dc08 | quote: The free tier is 100 searches a month.
  - [7] 2026-11-01: a third-party README states the free tier includes 100 searches per month, which conflicts with the one-time statement | capture: sha256:ac425602e7de696cd1c486c83d37c1cedeed4481a3465ca9a9af0eb15c96b55d | quote: The free tier includes 100 searches per month
  - [8] 2026-11-01: a third-party package page states the free tier is 100 searches a month, which conflicts with the one-time statement | capture: sha256:e4bcd001b48eff75d94bfb2737ca0c0e918ac46ae20615085ca9a0910fe2fbd1 | quote: Get your API key at searchapi.io (free tier: 100 searches/month).
- sources:
  - [1] https://www.searchapi.io/pricing
  - [2] https://www.searchapi.io/users/sign_up
  - [3] https://webscraping.cc/tool/searchapi/
  - [4] https://www.searchapi.io/docs/google
  - [5] https://www.searchapi.io/announcements/1
  - [6] https://github.com/Byski/mcp-searchapi
  - [7] https://github.com/Crossmint/worldstore-amazon-e2e
  - [8] https://pypi.org/project/llama-index-tools-searchapi/
