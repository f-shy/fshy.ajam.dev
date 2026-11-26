# Zenserp

> zenserp.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zenserp/ | JSON https://fshy.ajam.dev/api/v1/entity/zenserp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zenserp

- `crawler-scraper/zenserp` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-30T10:46:44.796Z (live) | stale on 2026-11-30
- url https://zenserp.com/pricing-plans/
- free tier: 50 free searches a month on the Free plan, USD 0, free forever; Google Search only on Free | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: Bing, Yandex, DuckDuckGo and the image, news, maps and shopping verticals start at the Small plan. Only successful requests are billed.
- per-object cap: not applicable | source: [1]
- retention: the 50 searches renew monthly | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: the signup form asks for a name, an email, a password, a postal address, a country and a VAT ID field, behind a Turnstile check; the Stripe card block renders only for a plan priced above 0, so the Free plan takes no card
- interface: rest
- limits:
  - request-rate (binding): 50 searches a month on Free; Small USD 49.99 a month for 25,000 [1]
  - request-rate (binding): standard plans are asked not to exceed 400 concurrent connections [1]
- binding note: the 50-a-month quota binds long before 400 concurrent connections
- interface detail: GET https://app.zenserp.com/api/v2/search with an apikey query parameter or header
- endpoint: part of interface detail
- tooling: plain HTTP GET with an apikey query parameter or request header
- composes with: A small recurring Google SERP allowance for spot checks beside a larger search leg; the Small plan at USD 49.99 for 25,000 is the paid step
- reliability: a keyless call answered 403 with a no-apikey message; 403 also marks an exhausted monthly quota
- notes: Part of the APILayer suite. Email notices fire at 90% and 100% of the monthly limit, and request errors do not count against it.
- evidence note: the 50 searches a month and the concurrency guidance are quoted from the pricing page, and the no-card finding rests on the signup page's own markup, which shows the card block only for a priced plan; no keyed search was made, so the read path is unprobed
- evidence:
  - [1] 2026-10-30: the Free plan is 50 searches a month | capture: sha256:621465002172ff88f216383dae6743f0d2747deaec0b323510721bca4b87e5b3 | quote: Start with 50 free searches a month, then pick a plan for the volume you need.
  - [1] 2026-10-30: 50 searches a month on Free, 25,000 on Small | capture: sha256:621465002172ff88f216383dae6743f0d2747deaec0b323510721bca4b87e5b3 | quote: | Searches per month | 50 | 25,000 | 100,000 | 250,000 | 500,000 | 1,000,000 |
  - [1] 2026-10-30: the Free plan covers Google only | capture: sha256:621465002172ff88f216383dae6743f0d2747deaec0b323510721bca4b87e5b3 | quote: | Bing, Yandex, DuckDuckGo | — Not included | ✓ Included |
  - [1] 2026-10-30: standard plans are asked to stay under 400 concurrent connections | capture: sha256:621465002172ff88f216383dae6743f0d2747deaec0b323510721bca4b87e5b3 | quote: For our standard plans, we encourage not to exceed 400 concurrent connections.
  - [2] 2026-10-30: the home page states 50 free searches a month | capture: sha256:051df5be02627b469bf2087fd8b7598a55110ea62be9fdfe4d624c11aa848997 | quote: We believe in fair pricing. Hence, we offer you 50 free searches per month. No strings attached!
  - [3] 2026-10-30: the Stripe billing block on the signup page renders only for a plan priced above 0 | capture: sha256:2c65d595c21a33d994b0de7bcfc366a73015c207df61133afa38d9fff2f6ece8 | quote: <div class="row justify-content-center" v-if="selectedPlan && selectedPlan.price > 0">
  - [4] 2026-10-30: a third-party review states the Free tier needs no card | capture: sha256:9ea559d389e834a1e026a01b6dbdfcdbe0832a7e17d3bf453ca3dc6910aa6d39 | quote: the Free tier costs you nothing, and doesn’t demand that you put credit card information on file
  - [5] 2026-10-30: the API base URL | capture: sha256:6fc4fbf572cd73a6c772a0b5f70aa3781d9fb71fb794d85a00ceb464da0497e1 | quote: The base URL is app.zenserp.com/api/v2.
  - probe:app.zenserp.com/api/v2/search 2026-10-30: a keyless call answered 403 with a no-apikey message | capture: sha256:cecda1fe00219f25c73a037330954bfb34fccfbf279170878b539c0b27511d4f | quote: {"error":"No apikey provided."}
- sources:
  - [1] https://zenserp.com/pricing-plans/
  - [2] https://zenserp.com/
  - [3] https://app.zenserp.com/register?plan=free
  - [4] https://www.addictivetips.com/web/real-time-serps-scraping-zenserp/
  - [5] https://zenserp.com/llms.txt
