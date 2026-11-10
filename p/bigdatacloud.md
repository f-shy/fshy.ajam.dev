# BigDataCloud

> bigdatacloud.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bigdatacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/bigdatacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BigDataCloud

- `data-apis/bigdatacloud` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.114Z (live) | stale on 2026-12-04
- url https://www.bigdatacloud.com/packages/ip-geolocation
- free tier: IP Geolocation package Free tier: 10k requests a month, no credit card, with every API endpoint and response field of the package | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: each package (IP Geolocation, reverse geocoding and others) has its own independent quota
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an account with no credit card: the sign-up page takes an email address and sends a 6-digit code to it, or signs in with Google or GitHub; a human check can be asked, and after the first sign-in a profile step asks for first name, last name and an optional company
- interface: rest
- limits:
  - volume-quota (binding): 10k requests a month; HTTP 403 past it unless pay-as-you-go is enabled [1]
- tooling: any HTTP client
- composes with: 10k keyed lookups a month with confidence areas and hazard data; other BigDataCloud packages carry their own free quotas on the same account. Bulk path: none stated
- reliability: past the monthly quota the API answers HTTP 403 with the time it may be retried
- notes: Free requests: 10k a month on the IP Geolocation package. Rate limit: not stated; HTTP 403 past the quota. Bulk path: none stated.
- evidence note: unverified: behind a sign-up: a keyed lookup and the response headers of its answer; the package page and the pricing FAQ were quoted on 2026-10-30, and the sign-up text was read from the page script on 2026-11-02
- extras:
  - bulk_path: none stated
  - free_requests: 10k a month
- evidence:
  - [1] 2026-10-30: the free tier is 10k requests a month | capture: sha256:cf71158d8bb7acb7b9ffa9f2c5430ae8c316790fee4d2c05a7afbfbf570ab4b3 | quote: 10k/mo
  - [1] 2026-10-30: no card is needed | capture: sha256:cf71158d8bb7acb7b9ffa9f2c5430ae8c316790fee4d2c05a7afbfbf570ab4b3 | quote: no credit card needed
  - [1] 2026-10-30: an API key is issued at signup | capture: sha256:cf71158d8bb7acb7b9ffa9f2c5430ae8c316790fee4d2c05a7afbfbf570ab4b3 | quote: No credit card · Generous free tier · API key in 30 seconds
  - [2] 2026-10-30: the Free plan has every endpoint and field | capture: sha256:54d4d56b6ebe31f1826dfdbd9adf9643857ace6608031536bf03a1b20923c0f3 | quote: Yes - every plan from Free to Platinum includes full access to all API endpoints and all response fields within that package. The only difference is monthly query volume.
  - [2] 2026-10-30: HTTP 403 past the monthly limit | capture: sha256:54d4d56b6ebe31f1826dfdbd9adf9643857ace6608031536bf03a1b20923c0f3 | quote: By default, once you reach your monthly limit the API returns HTTP 403, with a message telling you when you can try again.
  - [2] 2026-10-30: each package has its own quota | capture: sha256:54d4d56b6ebe31f1826dfdbd9adf9643857ace6608031536bf03a1b20923c0f3 | quote: Yes - each package has its own independent subscription and quota.
  - [3] 2026-11-02: the sign-up page script holds the text of the sign-up steps: an email field, a 6-digit code sent by email, Google and GitHub buttons, a human check and a profile step with first name, last name and an optional company | capture: sha256:dee5f0b853211d007b1ab8d7f191e57f3f6b556c69dcfaef2f6721f466d446b9 | quote: Use your email, Google or GitHub. New here? We'll set up your free account.
  - [3] 2026-11-02: the sign-up page script gives the sign-up text, so only a keyed lookup stays behind a sign-up | capture: sha256:dee5f0b853211d007b1ab8d7f191e57f3f6b556c69dcfaef2f6721f466d446b9 | quote: Use your email, Google or GitHub. New here? We'll set up your free account.
  - [1] 2026-11-02: the Free tier of the IP Geolocation package is 10k requests a month | capture: sha256:cf71158d8bb7acb7b9ffa9f2c5430ae8c316790fee4d2c05a7afbfbf570ab4b3 | quote: 10k/mo
  - [2] 2026-11-02: past the monthly limit the API answers HTTP 403 with a message that says when to retry, and each package has its own independent quota | capture: sha256:54d4d56b6ebe31f1826dfdbd9adf9643857ace6608031536bf03a1b20923c0f3 | quote: By default, once you reach your monthly limit the API returns HTTP 403, with a message telling you when you can try again.
- sources:
  - [1] https://www.bigdatacloud.com/packages/ip-geolocation
  - [2] https://www.bigdatacloud.com/pricing
  - [3] https://www.bigdatacloud.com/_nuxt/BnZKwI5g.js
