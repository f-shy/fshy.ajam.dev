# geoPlugin

> geoplugin.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geoplugin/ | JSON https://fshy.ajam.dev/api/v1/entity/geoplugin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## geoPlugin

- `data-apis/geoplugin` | paid-only | evidence documented | binding volume-quota | category IP geolocation API | tier Basic
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T00:23:42.369Z (live) | stale on 2026-12-03
- url https://www.geoplugin.com/pricing
- free tier: No free plan: the legacy keyless service at geoplugin.net answers HTTP 403 and says the API is no longer available for free use; the pricing page says there is no free trial and the cheapest plan, Basic, allows 100 requests a day at USD 10 a month. | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: Basic is shown as USD 10 a month, or USD 8 a month with the annual option; Starter is USD 25 (1,000 a day), Professional USD 50 (5,000 a day), Business USD 100 (20,000 a day) and Enterprise USD 200 (100,000 a day), each with a cheaper annual price.
- per-object cap: not stated
- retention: not stated for the keyed API | source: [2]
- egress: not applicable | metered: no | source: [1]
- identity: card | detail: registration takes an email address and a password (full name optional) or Google sign-in; every API plan is paid by card or PayPal, and there is no free plan or trial
- interface: rest
- limits:
  - volume-quota (binding): 100 requests a day on the Basic plan, reset at midnight UTC; cached responses do not count [1]
- binding note: The plan's daily count is the only stated limit for the keyed API; past it calls continue but may be throttled.
- interface detail: GET https://api.geoplugin.com/?ip=ADDRESS&auth=KEY and GET https://api.geoplugin.com/me?auth=KEY, with an optional lang parameter; JSON with geoplugin_* fields; a call with no key answers HTTP 400 No API key provided; the legacy http://www.geoplugin.net/json.gp answers HTTP 403
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: No free route: the cheapest keyed plan is Basic, 100 requests a day for USD 10 a month, and cached responses do not count against the daily limit. Bulk path: none stated
- reliability: Third-party reports of the same 403 message date from 2025-09-01.
- notes: Free requests: none; the legacy free endpoint answers HTTP 403. Rate limit: no per-minute limit is stated for the keyed API; the daily count is 100 on Basic. Not stated for the keyed API. Bulk path: none stated.
- evidence note: The legacy endpoint's HTTP 403 answer was read through a fetch, and a keyless call to the keyed API answered HTTP 400. Two third-party reports (2025-09-01 and 2026-02-22) give the same 403 message. No keyed lookup was made.
- extras:
  - bulk_path: none stated
  - free_requests: none
- evidence:
  - [3] 2026-11-02: the legacy geoplugin.net endpoint answers HTTP 403 | capture: sha256:4a84e09ff0e31e55e2e40c090505c5d80acd320dcae2cb0c30e64c7ee09d1162
  - [3] 2026-11-02: the legacy endpoint states that the API is no longer available for free use | capture: sha256:4a84e09ff0e31e55e2e40c090505c5d80acd320dcae2cb0c30e64c7ee09d1162 | quote: geoPlugin API is no longer available for free use. To continue access, please upgrade to a paid plan
  - [4] 2026-11-02: a third-party forum thread was created on 2025-09-01 | capture: sha256:fccb67c2f3520f05cface61c84b5a5897126a0e47222011bc50ce662fb3e39a5 | quote: [September 1, 2025, 2:05am UTC]
  - [4] 2026-11-02: that thread reports the geoPlugin message that the API is no longer available for free use, so the free service had closed by 2025-09-01 | capture: sha256:fccb67c2f3520f05cface61c84b5a5897126a0e47222011bc50ce662fb3e39a5 | quote: is no longer available for free use. To continue access, please upgrade to a paid plan by clicking
  - [5] 2026-11-02: a third-party issue was opened on 2026-02-22 | capture: sha256:f6bebd837295ff871d2d4578f16bda81a83051162cd5885a0454ef2575d30f22 | quote: opened on Feb 22, 2026
  - [5] 2026-11-02: that issue shows the same HTTP 403 JSON answer from geoplugin.net/json.gp | capture: sha256:f6bebd837295ff871d2d4578f16bda81a83051162cd5885a0454ef2575d30f22 | quote: "geoplugin_message": "geoPlugin API is no longer available for free use. To continue access, please upgrade to a paid plan",
  - [1] 2026-11-02: there is no free trial and the cheapest plan allows 100 requests a day | capture: sha256:9fce0c89d507f15990c5b2a3aba75556a624db661313db1feaae48cba2b16fd3 | quote: While we don't offer a free trial, our Basic plan provides an affordable way to test our services with 100 daily requests. You can upgrade at any time once you're ready to scale.
  - [1] 2026-11-02: Basic is shown at 10 and 8 a month for 100 requests a day | capture: sha256:79226bdaa8bd0204807df9965facd9809556df459514ae95cc27e3d7d1517b88 | quote: $ 10 8 /mo 100 requests/day
  - [1] 2026-11-02: the page has a monthly and an annual option, the annual one saving 20% | capture: sha256:973eba5bff01225637583addd82bf6e1bef1b571675046d93b9511340b2a1ab2 | quote: Monthly Annual Save 20%
  - [1] 2026-11-02: Starter is 25 and 20 a month for 1,000 requests a day | capture: sha256:79226bdaa8bd0204807df9965facd9809556df459514ae95cc27e3d7d1517b88 | quote: $ 25 20 /mo 1,000 requests/day
  - [1] 2026-11-02: Professional is 50 and 40 a month for 5,000 requests a day | capture: sha256:79226bdaa8bd0204807df9965facd9809556df459514ae95cc27e3d7d1517b88 | quote: $ 50 40 /mo 5,000 requests/day
  - [1] 2026-11-02: Business is 100 and 80 a month for 20,000 requests a day | capture: sha256:79226bdaa8bd0204807df9965facd9809556df459514ae95cc27e3d7d1517b88 | quote: $ 100 80 /mo 20,000 requests/day
  - [1] 2026-11-02: Enterprise is 200 and 160 a month for 100,000 requests a day | capture: sha256:79226bdaa8bd0204807df9965facd9809556df459514ae95cc27e3d7d1517b88 | quote: $ 200 160 /mo 100,000 requests/day
  - [1] 2026-11-02: the daily limit resets at midnight UTC and cached responses do not count | capture: sha256:9fce0c89d507f15990c5b2a3aba75556a624db661313db1feaae48cba2b16fd3 | quote: Request limits are calculated on a daily basis and reset at midnight UTC. Each API call to our geolocation service counts as one request. Cached responses do not count against your limit.
  - [1] 2026-11-02: past the daily limit calls continue but may be throttled | capture: sha256:9fce0c89d507f15990c5b2a3aba75556a624db661313db1feaae48cba2b16fd3 | quote: If you exceed your daily request limit, API calls will continue to work but may be throttled.
  - [1] 2026-11-02: plans are paid by card or PayPal | capture: sha256:9fce0c89d507f15990c5b2a3aba75556a624db661313db1feaae48cba2b16fd3 | quote: We accept all major credit cards (Visa, MasterCard, American Express, Discover) as well as PayPal.
  - [1] 2026-11-02: the closing button of the pricing page is labelled Start Free Trial and links to the registration page | capture: sha256:79226bdaa8bd0204807df9965facd9809556df459514ae95cc27e3d7d1517b88 | quote: [Start Free Trial](https://www.geoplugin.com/auth/register)
  - [6] 2026-11-02: the documented API needs an API key from the developer dashboard | capture: sha256:1c129d78551a9b14671fd58094b5ddb9081a442d93300e80627bbf909a9b2f73 | quote: GeoPlugin uses API keys to allow access to the API. You can register a new GeoPlugin API key at our [Developer Dashboard.](https://www.geoplugin.com/account)
  - [6] 2026-11-02: the documented request URL carries the key in the auth parameter | capture: sha256:1c129d78551a9b14671fd58094b5ddb9081a442d93300e80627bbf909a9b2f73 | quote: https://api.geoplugin.com/?ip=X.X.X.X&auth=YOUR_API_KEY_HERE
  - [7] 2026-11-02: registration takes an optional full name, an email address and a password | capture: sha256:30878392a9c30cfcb2a72923f067ccc23b75999caa68840c5f3f82cd4b76b64d | quote: Full Name (Optional)Email AddressPassword
  - [7] 2026-11-02: Google sign-up is offered | capture: sha256:30878392a9c30cfcb2a72923f067ccc23b75999caa68840c5f3f82cd4b76b64d | quote: Sign Up with Google
  - [8] 2026-11-02: the pricing blurb on the JSON web service page says no credit card is required | capture: sha256:c4661d16e6c3f04e736c2fd2f33ac770ea17678a906554c207eb6f4a14995f03 | quote: No credit card required
  - [2] 2026-11-02:  | capture: sha256:9c420c9cf634ea6dcf80bd6806d82d607a634c71bfb9acc64b225597b0d4d447 | quote: or by saving the data obtained from lookups for greater than 24 hours.
  - [2] 2026-11-02:  | capture: sha256:9c420c9cf634ea6dcf80bd6806d82d607a634c71bfb9acc64b225597b0d4d447 | quote: Greater than 120 API requests per minute will get you blacklisted for 1 hour, during which time you will receive a “429 Too Many Requests” response.
  - [9] 2026-11-02: the FAQ still describes the free lookup limit of 120 requests a minute | capture: sha256:34f3523b0d223ee66c954ce84904c7ce1c348d01b8725b83598f31660cd368fe | quote: If geoplugin.net was responding perfectly, then stopped, then you have gone over the free lookup limit of 120 requests per minute.
  - [10] 2026-11-02: the home page still says no API key is required | capture: sha256:9ab4f423c34805ef5daed55299c1aaa2d7f2d6b02886e6c1f4b22a0fabb2a843 | quote: No API key required.
  - probe:https://api.geoplugin.com/?ip=8.8.8.8 2026-11-02: a keyless call to api.geoplugin.com answered HTTP 400 | capture: sha256:8cd0d4e5d1e34f3401d8f731881f0d5f25733750bd02327a32dea295027085f3 | quote: "status": 400
  - probe:https://api.geoplugin.com/?ip=8.8.8.8 2026-11-02: the keyed API answers No API key provided to a call with no key | capture: sha256:e863bad2161bc1332a51a005768ff5272f4674febbf8881a376dbfb80f1eaf9b | quote: {"error":"No API key provided."}
- sources:
  - [1] https://www.geoplugin.com/pricing
  - [2] https://www.geoplugin.com/aup
  - [3] http://www.geoplugin.net/json.gp?ip=8.8.8.8
  - [4] https://forums.concretecms.org/t/geolocation-service-is-discontinued/9403
  - [5] https://github.com/viking-gps/viking/issues/357
  - [6] https://www.geoplugin.com/docs
  - [7] https://www.geoplugin.com/auth/register
  - [8] https://www.geoplugin.com/webservices/json
  - [9] https://www.geoplugin.com/faq
  - [10] https://www.geoplugin.com/
