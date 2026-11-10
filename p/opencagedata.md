# OpenCage

> opencagedata.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opencagedata/ | JSON https://fshy.ajam.dev/api/v1/entity/opencagedata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenCage

- `data-apis/opencage` | qualifies-with-caveat | evidence documented | binding volume-quota | category geocoding API | tier free trial (no end date; inactive accounts deleted after three months)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:11.229Z (live) | stale on 2026-12-04
- url https://opencagedata.com/pricing
- free tier: 2,500 geocoding requests a day (forward or reverse, one location per request), a hard limit that resets at 24:00 UTC, at 1 request per second; spreadsheet uploads up to 100 rows; one API key; no credit card | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: every request counts, including bad requests and requests with no result. The cheapest paid steps are a one-time plan of 10,000 requests for EUR 20, usable for up to a year, and the X-Small subscription of 10,000 requests a day at 15 requests a second for EUR 45 a month. Geosearch (autosuggest) has no free amount.
- per-object cap: one location per API request: the API takes no batch; a spreadsheet upload on the free trial is limited to 100 rows, each row counted as one request | source: [1]
- retention: uploaded spreadsheets are deleted after 3 days for free trial users | source: [1] | note: no separate temporary and permanent pricing
- egress: not applicable: a query API metered in requests, not bytes | metered: no | source: [2]
- identity: email | detail: the signup form asks for a name, a company or organization name, an email and a password, behind hCaptcha, or a Google or GitHub sign-up; no credit card for the free trial; the general terms set a minimum age of 18
- interface: rest
- limits:
  - volume-quota (binding): 2,500 requests a day on the free trial, a hard limit reset at 24:00 UTC; past it the API answers HTTP 402 quota exceeded [1]
  - request-rate: 1 request per second on the free trial; faster answers HTTP 429 [1]
  - per-object-cap: one location per request; spreadsheet uploads up to 100 rows on the free trial [1]
- limits note: unverified: the X-RateLimit-Limit header of a live free trial key was not read, since it needs a free trial account; the API page documents it as the total requests the account is limited to over 24 hours for free trials, and its example shows 2500
- binding note: 1 request a second allows far more than 2,500 requests in a day, so the daily hard limit is met first
- interface detail: HTTPS GET to api.opencagedata.com/geocode/v1/json (also xml and geojson) with the key in the key parameter; a request without a key answers HTTP 401 missing API key, and the documented test key answers HTTP 200; responses to free trial and one-time plan keys carry the quota in a rate element and in the X-RateLimit-Limit, X-RateLimit-Remaining and X-RateLimit-Reset headers, which subscription responses do not carry
- endpoint: https://api.opencagedata.com/geocode/v1/json
- tooling: any HTTP client; vendor tutorials for Node.js, PHP, Python and Ruby include parallel request scripts, and a command line tool geocodes CSV files
- composes with: 2,500 storable geocodes a day with no card, so a slow job of about 2,500 addresses a day can build a permanent table; a one-off batch beyond that is the EUR 20 one-time plan of 10,000 requests, or the Geoapify free plan (data-apis/geoapify) at 3,000 a day with a batch endpoint. Bulk path: no bulk path; one location per request and no data download
- reliability: past the daily hard limit the API answers HTTP 402, and a free trial key that keeps requesting past it is disabled with HTTP 403; free trial accounts are deleted after three months of inactivity, and accounts detected as several free trials of one user are fed randomly wrong results
- notes: Bulk path: no bulk path; one location per request, spreadsheet uploads of 100 rows on the free trial, and no data download. The vendor labels the free amount a trial for testing; it has no end date.
- evidence note: the pricing page (in its markdown form), the API reference, the FAQ, the signup form and the terms were quoted on 2026-10-30 and 2026-10-31; a keyless request answered HTTP 401 and the published test key answered HTTP 200 with zero results. No account was opened, so the 2,500 a day was not exercised; a keyed run to the 402 would move it to measured.
- extras:
  - bulk_path: no bulk path
- evidence:
  - [1] 2026-10-30: the free trial is capped at 2,500 requests a day | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial accounts have a hard limit of 2,500 requests per day for testing purposes.
  - [1] 2026-10-30: the daily count resets at 24:00 UTC | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Daily counts reset at 24:00 UTC.
  - [1] 2026-10-30: the free trial rate is 1 request per second | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial accounts are limited to one request per second.
  - [1] 2026-10-30: past the hard limit the API answers HTTP 402 | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: If you send a request after you have reached your hard limit you will receive a `402 - quota exceeded` response
  - [1] 2026-10-30: a free trial that keeps requesting past the limit is disabled with HTTP 403 | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial accounts that continually request beyond the hard limit (if you ignore the `402` response) will eventually be blocked and see a `403 - disabled` response.
  - [1] 2026-10-30:  | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: This applies whether you are on our free-trial, or you have become a paying customer, and even after you stop being a customer.
  - [1] 2026-10-30: there is no separate temporary and permanent pricing | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: All data returns by the API can be stored permanently.
  - [1] 2026-10-30: the API takes one location per request; only a spreadsheet upload is geocoded in bulk | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: We allow manual uploading of a spreadsheet which we geocode row by row, but the API itself does not allow multiple locations per request.
  - [1] 2026-10-30: free trial spreadsheet uploads are limited to 100 rows | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial users are limited to spreadsheets with 100 rows.
  - [1] 2026-10-30: inactive free trial accounts are deleted after three months | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial accounts are deleted after three months of inactivity, after which we have no record of the account.
  - [3] 2026-10-31: the free trial row: 2,500 requests a day at 1 request a second, no price | capture: sha256:3d30775ff3547df6441bebfde14db359a3ce18759f04f2427fb83b05d0a877f7 | quote: | Free trial | 2,500 | 1 | — | — |
  - [3] 2026-10-31: the free trial needs no credit card | capture: sha256:3d30775ff3547df6441bebfde14db359a3ce18759f04f2427fb83b05d0a877f7 | quote: - no credit card required
  - [3] 2026-10-31: the cheapest subscription is X-Small: 10,000 requests a day at 15 a second for EUR 45 a month | capture: sha256:3d30775ff3547df6441bebfde14db359a3ce18759f04f2427fb83b05d0a877f7 | quote: | X-Small | 10,000 | 15 | €45 | €450 |
  - [3] 2026-10-31: the smallest one-time plan is 10,000 requests for EUR 20 | capture: sha256:3d30775ff3547df6441bebfde14db359a3ce18759f04f2427fb83b05d0a877f7 | quote: | Small | 10,000 | 15 | €20 |
  - [2] 2026-10-30: a one-time plan's requests can be used for up to a year | capture: sha256:f92ede0223d1c4cdfb5d86d9f1cbfb0848ae47bacb383533b9c20a89871a9eb6 | quote: You can then use those requests as and when you like for up to a year.
  - [2] 2026-10-30:  | capture: sha256:f92ede0223d1c4cdfb5d86d9f1cbfb0848ae47bacb383533b9c20a89871a9eb6 | quote: Even if you are no longer a customer.
  - [2] 2026-10-30: every request counts, including bad requests and empty results | capture: sha256:f92ede0223d1c4cdfb5d86d9f1cbfb0848ae47bacb383533b9c20a89871a9eb6 | quote: Yes, every request counts as it generates work for us.
  - [4] 2026-10-30: the signup form asks for a company or organization name besides name, email and password | capture: sha256:a0b6843bb1f7498efabb6a1f3b033fe87551d84de164c57c3c9e70c07dc34f5c | quote: Company or organization name \*
  - [4] 2026-10-30: account creation is behind hCaptcha | capture: sha256:a0b6843bb1f7498efabb6a1f3b033fe87551d84de164c57c3c9e70c07dc34f5c | quote: Account creation is protected by hCaptcha
  - [4] 2026-10-30: sign-up through GitHub is offered | capture: sha256:a0b6843bb1f7498efabb6a1f3b033fe87551d84de164c57c3c9e70c07dc34f5c | quote: Sign up with GitHub
  - [5] 2026-10-30: the minimum age is 18 | capture: sha256:bb3cf970c857579d60068d11ec7ab0a1f7022b01c88ad1dae88b653977cafc61 | quote: You must be over 18 years of age to use OpenCage services.
  - [6] 2026-10-30: several free trial accounts of one user are fed randomly wrong results | capture: sha256:adabfd980dc7ac1931056a2fd22d5a33768421029a265d01d09bbfb220b21b8d | quote: But assuming you have no moral qualms about abusing our generous service, be warned that when we see you doing this we will start feeding you back randomly wrong results.
  - probe:https://api.opencagedata.com/geocode/v1/json?q=Zurich#body 2026-10-30: the geocode endpoint answers and refuses a request with no key | capture: sha256:4d8e9e89d65414c0aa823c6ddeea5a2a5fb9a440316fb243bd1038f0baffe0df | quote: "message":"missing API key"
  - probe:https://api.opencagedata.com/geocode/v1/json?q=NOWHERE-INTERESTING#body 2026-10-31: the documented test key gets HTTP 200 and an empty result set from the live endpoint | capture: sha256:cfee6e3b6475e0d7b664cd49339037de78f5bcf531c04d20bb59e38a928010e2 | quote: "status":{"code":200,"message":"OK"}
  - [1] 2026-11-02: the X-RateLimit-Limit header is the account's total requests over the period, 24 hours for free trials | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: | `limit` | `X-RateLimit-Limit` | total number of API requests your account is limited to over given time period (24 hours for free trials) |
  - [1] 2026-11-02: subscription responses carry neither the rate element nor the X-RateLimit headers | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Note: Responses to subscription customers do NOT contain the `rate` section of the response or `X-Ratelimit` HTTP headers, because they do not face hard limits.
  - [1] 2026-11-02: free trial and one-time plan keys face hard limits, so their responses carry the rate headers | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial and one-time plan customers face hard limits. Subscription customers do not.
  - [1] 2026-11-02: the documented example of the rate element shows a limit of 2500 | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: "limit" : 2500,
  - [1] 2026-11-02: the daily count resets at 24:00 UTC | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Daily counts reset at 24:00 UTC.
  - [1] 2026-11-02: past the hard limit the API answers HTTP 402 | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: If you send a request after you have reached your hard limit you will receive a `402 - quota exceeded` response
  - [1] 2026-11-02: the free trial rate is 1 request per second | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial accounts are limited to one request per second.
  - [1] 2026-11-02: above the free trial rate the API may answer HTTP 429 | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: If you exceed the request per second rate you may see a `429 - too many requests` response.
  - [1] 2026-11-02: the free trial is capped at 2,500 requests a day | capture: sha256:62260c3f7104e114af4baf65053e315f1537220ca278d735525d3e11fc92efe8 | quote: Free trial accounts have a hard limit of 2,500 requests per day for testing purposes.
- sources:
  - [1] https://opencagedata.com/api
  - [2] https://opencagedata.com/pricing
  - [3] https://opencagedata.com/pricing.md
  - [4] https://opencagedata.com/users/sign_up
  - [5] https://opencagedata.com/terms
  - [6] https://opencagedata.com/faq
