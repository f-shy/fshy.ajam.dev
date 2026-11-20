# Scrapingdog

> scrapingdog.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrapingdog/ | JSON https://fshy.ajam.dev/api/v1/entity/scrapingdog.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scrapingdog

- `crawler-scraper/scrapingdog` | fails-quota | evidence documented | binding request-rate | category search and fetch API
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:01:52.277Z (live) | stale on 2026-12-03
- url https://www.scrapingdog.com/pricing/
- free tier: 100 free credits on the FREE plan (USD 0, forever), no credit card; a Google search costs 5 credits, so the 100 credits are 20 Google searches | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1] | note: The pricing table lists the 100 in its Monthly credits row, while the documentation states the free plan includes 200 requests a month; the two first-party pages disagree.
- per-object cap: not applicable | source: [1]
- retention: unverified: whether a free account's credits renew each month is behind a sign-up; the pricing FAQ says credits reset on the next billing date, and the home page lists the 100 free credits as a 7-day free trial | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: the signup form asks for an email address, marked 'Please use your work email address', a password and a referral source; no credit card required
- interface: rest
- limits:
  - request-rate (binding): 100 credits: 20 Google SERP or Brave Search requests at 5 credits, 10 advanced Google requests at 10 credits; the LITE plan is USD 40 a month for 200K credits [1]
  - request-rate (binding): 1 concurrent request on the FREE plan; exceeding the concurrency limit answers 429 [2]
- binding note: 20 Google searches is spent before the 1-request concurrency limit matters
- interface detail: GET https://api.scrapingdog.com/google with api_key and query parameters; one credit pool also serves Bing, Brave Search, Google News, Scholar and a general scraping endpoint
- endpoint: part of interface detail
- tooling: plain HTTP GET with an api_key query parameter
- composes with: Too small to carry search; the same 100 credits buy 100 rotating-proxy page fetches at 1 credit each, which is the better use of the account
- reliability: the pricing page and the documentation disagree on the free allowance, 100 credits against 200 requests a month; failed, blocked and timed-out requests are credited back
- notes: A general scraping API with SERP endpoints rather than a search engine of its own. Every plan reaches every API, so the free credits test Google, Bing and Brave Search parsing as well as page fetches.
- evidence note: the 100 credits, the 1-request concurrency, the per-search credit cost and the no-card statement are quoted from first-party pages; the documentation states a different free allowance, and whether the credits renew monthly is behind a sign-up
- evidence:
  - [1] 2026-10-30: 100 free credits on signup, no credit card | capture: sha256:045d143d0d81d7652230e353e53978df68124f6b5a4034c8245dc72ffc0c7450 | quote: Every account starts with 100 free credits and full access to all APIs, no credit card required.
  - [1] 2026-10-30: the FREE plan column lists 100 monthly credits; LITE lists 200K | capture: sha256:045d143d0d81d7652230e353e53978df68124f6b5a4034c8245dc72ffc0c7450 | quote: | Monthly credits | 100 | 200K | 1M |
  - [1] 2026-10-30: the FREE plan allows 1 concurrent request | capture: sha256:045d143d0d81d7652230e353e53978df68124f6b5a4034c8245dc72ffc0c7450 | quote: | Max concurrency | 1 | 5 | 50 |
  - [1] 2026-10-30: the 100 free credits are 20 Google SERP requests | capture: sha256:045d143d0d81d7652230e353e53978df68124f6b5a4034c8245dc72ffc0c7450 | quote: | Google SERP Light API5 credits / req | 20 reqs |
  - [1] 2026-10-30: the 100 free credits are 100 rotating-proxy fetches | capture: sha256:045d143d0d81d7652230e353e53978df68124f6b5a4034c8245dc72ffc0c7450 | quote: | Rotating proxy1 credit / req | 100 reqs |
  - [1] 2026-10-30: credits reset on the billing date; an exhausted balance answers over-limit | capture: sha256:045d143d0d81d7652230e353e53978df68124f6b5a4034c8245dc72ffc0c7450 | quote: Once your credits are used up, API requests return an over-limit response until they reset on your next billing date.
  - [2] 2026-10-30: the documentation states 200 requests a month on the free plan, which disagrees with the pricing page | capture: sha256:4ea264741d899e45ee3a294e071c0ee7f4725655567e82a7d0f5bdb2023e7a05 | quote: Free plan includes 200 requests / month.
  - [2] 2026-10-30: concurrency is limited per plan and answers 429 over the limit | capture: sha256:4ea264741d899e45ee3a294e071c0ee7f4725655567e82a7d0f5bdb2023e7a05 | quote: Concurrent connections are rate-limited per plan tier. Exceeding limits returns a 429 error.
  - [3] 2026-10-30: the Google search endpoint | capture: sha256:6554f0727034f3bfbd7b89f03c05da8d6ac121d141fddae1899a29aa97a16d19 | quote: Endpoint: `https://api.scrapingdog.com/google`
  - [3] 2026-10-30: a Google search costs 5 credits, 10 advanced | capture: sha256:6554f0727034f3bfbd7b89f03c05da8d6ac121d141fddae1899a29aa97a16d19 | quote: Each successful request costs 5 credits for standard search, or 10 credits for advanced search
  - [4] 2026-10-30: the signup form asks for a work email address | capture: sha256:c20888456c2cdc18ee90d71c1a05e180614cf00ea19fb758657e4a570b786e8d | quote: Please use your work email address.
  - probe:api.scrapingdog.com/google 2026-10-30: a keyless call to the Google endpoint answered 401 | capture: sha256:25ab0ca50b0042f91c02ca36b0dee3d7c649e2f11123b1461bc8d6a7c85dccad | quote: "message":"Unauthorized request, please make sure your API key is valid."
  - [5] 2026-11-01: the home page lists the 100 free credits as a 7-day free trial with no credit card required | capture: sha256:a27da4e2c5863231f6c39a775cc69e2f4f2bc7f1d43b731138c00af0c2753e2d | quote: 7-day free trial - No credit card required - 100 credits free
  - [2] 2026-11-01: the documentation overview states the free plan includes 200 requests a month, the same line as its 2026-07-14 archive copy | capture: sha256:96632e090105bd17d416e7d2ebbfcc1c0adc29b9c9ee8e1054451ac33c1e6905 | quote: Free plan includes 200 requests / month.
  - [6] 2026-11-01: the 2026-07-14 archive copy of the documentation overview already states the free plan includes 200 requests a month | capture: sha256:ff7ccdf735065c9ecb4606625a4c72d45d0ecc95e8de58192be4f806a5dedbc4 | quote: Free plan includes 200 requests / month.
  - [7] 2026-11-01: the 2026-09-05 archive copy of the pricing page states 200 free credits per account, the figure the documentation gives as 200 requests a month; the live page states 100 | capture: sha256:394f6382d5e82b45247f21c4d413800f4331e7e88dd4043af4578a0f138199c8 | quote: Every account starts with 200 free credits and full access to all APIs, no credit card required.
  - [8] 2026-11-01: the 2026-10-08 archive copy of the home page lists the 100 free credits as a 30-day free trial, where the live page says 7-day | capture: sha256:50198df91542eba033fc36eeeb0d1186058d01c1f0def40f4b17809e674ff8e8 | quote: 30-day free trial - No credit card required - 100 credits free
  - [9] 2026-11-01: the vendor's agent onboarding guide says a new account starts on a free trial with no card required | capture: sha256:94ca16311561703d1891a4524189334e65e29920b46eddc82b8ad04aa3a4779b | quote: A new account starts on a free trial with no card required.
  - [1] 2026-11-01: the pricing page lists the FREE plan as USD 0 forever | capture: sha256:e58368b7bd09f6c9105f2ab623220a7c0dd584b89050ae1fd8db244c3156c510 | quote: FREE $0forever
  - [5] 2026-11-01: the home page offers a Sign Up With Google route beside the email signup | capture: sha256:a27da4e2c5863231f6c39a775cc69e2f4f2bc7f1d43b731138c00af0c2753e2d | quote: Try Scrapingdog for Free Sign Up With Google
  - [1] 2026-11-01: the pricing page still states 100 free credits per account and no credit card | capture: sha256:e58368b7bd09f6c9105f2ab623220a7c0dd584b89050ae1fd8db244c3156c510 | quote: Every account starts with 100 free credits and full access to all APIs, no credit card required.
  - [4] 2026-11-01: the signup form still asks for an email address, marked work email | capture: sha256:c20888456c2cdc18ee90d71c1a05e180614cf00ea19fb758657e4a570b786e8d | quote: Please use your work email address.
- sources:
  - [1] https://www.scrapingdog.com/pricing/
  - [2] https://www.scrapingdog.com/documentation/
  - [3] https://www.scrapingdog.com/documentation/google-search-api-documentation/
  - [4] https://api.scrapingdog.com/register
  - [5] https://www.scrapingdog.com/
  - [6] https://web.archive.org/web/20260714213606/https://www.scrapingdog.com/documentation/
  - [7] https://web.archive.org/web/20260905172744/https://www.scrapingdog.com/pricing/
  - [8] https://web.archive.org/web/20261008063559/https://www.scrapingdog.com/
  - [9] https://www.scrapingdog.com/agent-onboarding/SKILL.md
