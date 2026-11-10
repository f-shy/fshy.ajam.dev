# currencylayer

> currencylayer.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/currencylayer/ | JSON https://fshy.ajam.dev/api/v1/entity/currencylayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## currencylayer (APILayer)

- `data-apis/currencylayer` | fails-quota | evidence documented | binding volume-quota | category currency exchange rate API (168 currencies and metals) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://currencylayer.com/
- free tier: Free plan, USD 0: 100 API requests a month, daily updates, historical rates, HTTPS. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: One request is any call with a valid key; time-frame and change queries and many currencies in one call count as one. The next plan up, Basic, is USD 14.99 a month for 10,000 requests. The pricing FAQ says quotes refresh every 60 minutes on Free and Basic, the general FAQ says every day on Free; the plan card says daily updates.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the 100 requests a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The free sign-up form asks for first name, last name, email, password, address, postal code, country and city (state in some countries), with a Turnstile check. The card block of the form is marked paid-only and hidden.
- interface: rest
- limits:
  - volume-quota (binding): 100 requests a month on the Free plan [1]
- limits note: Rate per minute: not stated on the pages read. The timeframe endpoint spans up to 365 days; whether the Free plan includes it was not readable, because the plan table lost its check and cross marks. Bulk path: none on the free plan.
- binding note: 100 requests a month is spent in days of testing, and no per-minute rate is published.
- interface detail: GET /live and /historical with an access_key; /timeframe, /convert and /change are other endpoints, and their plan gate was not read
- endpoint: https://api.currencylayer.com/live
- tooling: any HTTP client
- composes with: 100 requests a month is a test allowance; a daily rate pull uses about 30, so little is left for history.
- reliability: At 100 percent of the allowance the FAQ says overage fees apply, and the plan table lists an Overage line; what the Free plan does past 100 requests was not read.
- notes: Free requests: 100 a month. Rate limit: no per-minute rate stated on the pages read. Bulk path: none on the free plan.
- evidence note: Quota, refresh and licence fields are read from the home page and FAQ; the sign-up fields are read from the form markup of the free sign-up page. The documentation pages did not read in full. No key was created.
- extras:
  - bulk_path: none on the free plan
  - free_requests: 100 a month
- evidence:
  - [1] 2026-11-02: the Free plan card lists 100 API calls | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec | quote: - 100 API Calls
  - [1] 2026-11-02: the Free plan card lists daily updates | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec | quote: - Daily Updates
  - [1] 2026-11-02:  | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec
  - [1] 2026-11-02: the Free plan card lists historical rates | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec | quote: - Historical Rates
  - [1] 2026-11-02: the Free plan card lists no support | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec | quote: - No Support
  - [2] 2026-11-02: the sign-up page lists the first plan, Free, at 100 requests a month | capture: sha256:ae4ad24072ba12cc4d80c5350b2a7ff28371ac85792c0934a97706e36fe5af04 | quote: <div class="signup-v2-plan-requests">100 Requests / month</div>
  - [3] 2026-11-02: the free allowance is 100 API requests a month | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: As soon as you or your application requires more than 100 API Requests per month
  - [3] 2026-11-02: any call with a key counts as one request | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: Accessing any type of currencylayer forex data using a valid API Access Key counts as one "API Request".
  - [3] 2026-11-02: the Free plan refreshes every day | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: every day (Free Plan)
  - [3] 2026-11-02: past 100 percent overage fees apply | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: After reaching 100% of the allowance, overages fees will apply
  - [1] 2026-11-02: paid plans start at USD 14.99 a month | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec | quote: Subscriptions Plans starting at Startup-friendly USD 14.99 per month
  - [2] 2026-11-02: the sign-up form asks for a first name | capture: sha256:ae4ad24072ba12cc4d80c5350b2a7ff28371ac85792c0934a97706e36fe5af04 | quote: <label for="first_name">First Name<span class="signup-v2-required" aria-hidden="true">*</span></label>
  - [2] 2026-11-02: the sign-up form asks for an email address | capture: sha256:ae4ad24072ba12cc4d80c5350b2a7ff28371ac85792c0934a97706e36fe5af04 | quote: <label for="email_address">Email<span class="signup-v2-required" aria-hidden="true">*</span></label>
  - [2] 2026-11-02: the sign-up form requires a postal code | capture: sha256:ae4ad24072ba12cc4d80c5350b2a7ff28371ac85792c0934a97706e36fe5af04 | quote: <label for="post_code">Postal Code<span class="signup-v2-required" aria-hidden="true">*</span></label>
  - [2] 2026-11-02: the card block of the sign-up form is marked paid-only and hidden | capture: sha256:ae4ad24072ba12cc4d80c5350b2a7ff28371ac85792c0934a97706e36fe5af04 | quote: <div class="signup-v2-card-block" data-paid-only hidden>
  - [2] 2026-11-02: the sign-up form carries a Turnstile check | capture: sha256:ae4ad24072ba12cc4d80c5350b2a7ff28371ac85792c0934a97706e36fe5af04 | quote: <div class="cf-turnstile"
  - [3] 2026-11-02: the timeframe endpoint spans up to 365 days | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: maximum range of up to 365 days
  - [3] 2026-11-02: the API covers 168 currencies and metals | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: a total of 168 world currencies and precious metals
  - [1] 2026-11-02: Basic allows 10,000 requests | capture: sha256:8aa63437918d403386a45e7c492cbb76f1094826510fff6cff65de344b04cbec | quote: - 10,000 Requests
  - [3] 2026-11-02: time-frame and change queries and many currencies count as one request | capture: sha256:b21ca8068ff197c04eb75fd1cc4b4ae795d313939b9dca6ec24acdc5ccb595c7 | quote: Unlike most other providers, any API Endpoint or feature requested (including Time-Frame & Currency-Change Queries, as well as requesting multiple currencies at once) counts as only one API Request.
  - [4] 2026-11-02: the pricing FAQ says quotes refresh every 60 minutes on Free and Basic | capture: sha256:12ef8bf83555876ee73d5615196bc7aa945c2c47fe8831448382a64279f6d56c | quote: quotes are refreshed every 60 minutes (Free & Basic Plan)
  - [5] 2026-11-02: the docs list a historical endpoint | capture: sha256:b03bd7e0fca128837d7fa5bc556591cf5a94c5efc493e6e26e5c55491e61eabf | quote: | `/historical` | Retrieve FX rates on a specific date |
  - [5] 2026-11-02: the docs list a live endpoint | capture: sha256:b03bd7e0fca128837d7fa5bc556591cf5a94c5efc493e6e26e5c55491e61eabf | quote: | `/live` | Fetch real-time rates |
- sources:
  - [1] https://currencylayer.com/
  - [2] https://currencylayer.com/signup/free
  - [3] https://currencylayer.com/faq
  - [4] https://currencylayer.com/pricing/
  - [5] https://docs.apilayer.com/currencylayer/docs/api-documentation
