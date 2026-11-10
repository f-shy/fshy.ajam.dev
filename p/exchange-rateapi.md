# Exchange Rate API

> exchange-rateapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exchange-rateapi/ | JSON https://fshy.ajam.dev/api/v1/entity/exchange-rateapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Exchange Rate API (exchange-rateapi.com)

- `data-apis/exchange-rateapi` | qualifies-with-caveat | evidence documented | binding volume-quota | category currency exchange rate API (alias domain of AllRatesToday) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://exchange-rateapi.com/pricing
- free tier: The pricing page of exchange-rateapi.com redirects to the AllRatesToday pricing page, so the Free plan is the AllRatesToday Free plan: 1 API key, 10 requests a minute, and a lifetime request total whose size is not published. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The home page and the sign-up page of exchange-rateapi.com carry AllRatesToday content and AllRatesToday links. The terms page on exchange-rateapi.com names its own service, Exchange Rate API. See data-apis/allratestoday for the plan numbers.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the request total bounds what a free key can pull | metered: no | source: [1]
- identity: email | detail: The sign-up page is the AllRatesToday page: email and password, or Google or GitHub; no card.
- interface: rest
- limits:
  - volume-quota (binding): the AllRatesToday lifetime total of Free requests; its size is not published [1]
  - request-rate: 10 requests a minute on the Free plan (AllRatesToday pricing page) [1]
- binding note: The lifetime total never resets, so it ends the key before the per-minute rate matters.
- interface detail: the same REST API as AllRatesToday, at allratestoday.com/api/v1/rates with a Bearer key
- endpoint: https://allratestoday.com/api/v1/rates
- tooling: any HTTP client; the same SDKs as AllRatesToday
- composes with: Use the AllRatesToday record data-apis/allratestoday for limits and data-apis/allratestoday-open for the keyless lane; this domain adds no separate quota.
- reliability: The terms on this domain say a call past the plan rate limit answers HTTP 429 and that persistent overuse may lead to suspension.
- notes: Free requests: the AllRatesToday lifetime total, size not published. Rate limit: 10 requests a minute. Bulk path: none on the free key; see data-apis/allratestoday-open. This record and data-apis/allratestoday describe one offer.
- evidence note: The pricing and sign-up pages read here are identical to the AllRatesToday pages, and a fetch of the pricing URL showed a redirect to allratestoday.com. No key was created.
- extras:
  - bulk_path: none on the free key; the keyless AllRatesToday GitHub dataset is the bulk route
  - free_requests: AllRatesToday lifetime total, size not published
- evidence:
  - [1] 2026-11-02: the pricing URL of exchange-rateapi.com ends on the AllRatesToday pricing page | capture: sha256:8c5f96596b81c81b689d61029b7b6ae9cc03d8ccb5a148cda29aef1bce0a9104 | quote: x-web-final-url: https://allratestoday.com/pricing/
  - [2] 2026-11-02: the home page of exchange-rateapi.com is the AllRatesToday home page | capture: sha256:afc837ae635adbc5af3677b6375f768a3c26cfdd48d25cf452a0b2e28e09bbf8 | quote: # AllRatesToday Real-Time Exchange Rate API for Developers
  - [1] 2026-11-02:  | capture: sha256:d0a07874bcfaf54a6f618b2620de68f3f72f16dd607157c69b3b5c2c0281045a
  - [1] 2026-11-02: latest central-bank tables are on the free plan | capture: sha256:d0a07874bcfaf54a6f618b2620de68f3f72f16dd607157c69b3b5c2c0281045a | quote: The latest published rates are available on every plan, including Free.
  - [3] 2026-11-02: the sign-up page read from exchange-rateapi.com offers Google and GitHub | capture: sha256:bc8b8e41cc2ed0d7534f9fe5b815b39f15f5b4e83e900540daf6805cba7d5191 | quote: [Sign up with Google](https://allratestoday.com/api/auth/google) [Sign up with GitHub](https://allratestoday.com/api/auth/github)
  - [4] 2026-11-02: the terms of exchange-rateapi.com ask users to cache responses | capture: sha256:af0025e94d76800dee7a62032d8e2867c9b50427febe7a2f220477cab27712b2 | quote: 3. Cache API responses where appropriate to minimize unnecessary requests.
  - [4] 2026-11-02:  | capture: sha256:af0025e94d76800dee7a62032d8e2867c9b50427febe7a2f220477cab27712b2 | quote: 2.
  - [4] 2026-11-02: past the plan limit the API answers HTTP 429 | capture: sha256:af0025e94d76800dee7a62032d8e2867c9b50427febe7a2f220477cab27712b2 | quote: If you exceed your plan's rate limit, the API will return an HTTP 429 (Too Many Requests) response.
- sources:
  - [1] https://exchange-rateapi.com/pricing
  - [2] https://exchange-rateapi.com/
  - [3] https://exchange-rateapi.com/register
  - [4] https://exchange-rateapi.com/terms
