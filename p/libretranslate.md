# LibreTranslate hosted

> libretranslate.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/libretranslate/ | JSON https://fshy.ajam.dev/api/v1/entity/libretranslate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LibreTranslate hosted (libretranslate.com)

- `inference/libretranslate-hosted` | paid-only | evidence documented | binding none | category machine translation API, hosted, paid API key only | tier Pro
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:34:02.146Z (live) | stale on 2026-12-04
- url https://portal.libretranslate.com/
- free tier: none: the hosted API at libretranslate.com needs a paid API key (Pro USD 29 a month, Business USD 58 a month); the vendor offers no free trial and no free low-volume key | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: the keyless GET /frontend/settings of the hosted service reports keyRequired true, so the hosted translate endpoint refuses callers without a key. A 7 day money-back guarantee exists on the paid plans
- per-object cap: 2,000 characters per request (the hosted service's charLimit setting) | source: [2]
- retention: not applicable: a translation endpoint stores nothing for the caller
- egress: metered: no
- identity: card | detail: the keys are bought through Stripe checkout links on the portal page; the checkout page was not opened, so that the payment method is a card is inferred from the Stripe checkout and unverified
- interface: rest
- limits:
  - per-object-cap: 2,000 characters per request [2]
  - request-rate: bursts of up to 80 translations / minute on Pro; 200 translations / minute on Business; translations are unlimited [1]
- binding note: no free allowance exists to bind; the paid key is the gate, and the 2,000 character request size is the only per-call cap
- tooling: REST API: POST https://libretranslate.com/translate with q, source, target and api_key. Hosted offer first: the paid Pro and Business keys; self-hosted option last: the user installs and runs the open-source server (pip install libretranslate) on a rented or free machine, which is not what this record prices
- composes with: none: no free allowance to chain; the self-hosted option is the free route and ranks after every hosted offer
- reliability: a single hosted operator; the vendor states that a free low-volume key was tried in the past and stopped as not sustainable
- notes: Supported languages: GET /languages answers without a key and lists language codes from en to vi, among them sq, ar, zh-Hans, zh-Hant, pt-BR, ru and uk (the list is longer than the language names that the home page menu shows). Character limit per request: 2,000. Keyless: no; the web page loads without a key but the translate API reports keyRequired true.
- evidence note: the price, the absence of a free tier or trial and the request rates are quoted from the vendor's portal; the 2,000 character limit and the key requirement are read from the service's own settings endpoint; the payment method of the checkout is unverified.
- self hosted: no
- evidence:
  - [1] 2026-11-03: the Pro plan, the only entry tier, costs USD 29 a month | capture: sha256:5faca395d09c7d380c4aa69b944bb774235bec1ade10c1624e23bae4403c946f | quote: $29 / month
  - [1] 2026-11-03: the vendor offers no free trial | capture: sha256:5faca395d09c7d380c4aa69b944bb774235bec1ade10c1624e23bae4403c946f | quote: No, but we have a 7 days money-back guarantee.
  - [1] 2026-11-03: the vendor declines to give free low-volume keys | capture: sha256:5faca395d09c7d380c4aa69b944bb774235bec1ade10c1624e23bae4403c946f | quote: While we would love to offer low volume keys free of charge, it's just not sustainable for us (we tried in the past).
  - [1] 2026-11-03: Pro allows bursts of 80 translations a minute | capture: sha256:5faca395d09c7d380c4aa69b944bb774235bec1ade10c1624e23bae4403c946f | quote: Bursts of up to 80 translations / minute
  - [1] 2026-11-03: Business allows bursts of 200 translations a minute | capture: sha256:5faca395d09c7d380c4aa69b944bb774235bec1ade10c1624e23bae4403c946f | quote: Bursts of up to 200 translations / minute
  - [1] 2026-11-03: the purchase is a Stripe checkout link | capture: sha256:5faca395d09c7d380c4aa69b944bb774235bec1ade10c1624e23bae4403c946f | quote: [verified_user Buy](https://buy.stripe.com/28o2aVfoOeQM4wM5km)
  - probe:libretranslate.com/frontend/settings 2026-11-03: the hosted service reports that a key is required | capture: sha256:64d93ec7d14934fdd76a3fdcd0657c153b2de27bfb8ec1c0daa547717fbbfeff | quote: "keyRequired":true
  - probe:libretranslate.com/frontend/settings 2026-11-03: the hosted service sets a 2,000 character limit | capture: sha256:64d93ec7d14934fdd76a3fdcd0657c153b2de27bfb8ec1c0daa547717fbbfeff | quote: "charLimit":2000
  - [3] 2026-11-03: the managed hosting route is an API key from the portal, passed as api_key | capture: sha256:206dda91661bc3b9ee0fdfefa9d5a84cb52ca44c59e992cb7889622c6ccf84ce | quote: curl -X POST https://libretranslate.com/translate -d q="Hello" -d source=en -d target=es -d api_key=xxxxx
  - probe:libretranslate.com/languages 2026-11-03: the keyless languages list includes Chinese in simplified script as the code zh-Hans | capture: sha256:7e53b5d53a1004b462540fe40708d9ae8da92665258fb5d846df9089bf5ca569 | quote: "zh-Hans"
- sources:
  - [1] https://portal.libretranslate.com/
  - [2] https://libretranslate.com/frontend/settings
  - [3] https://docs.libretranslate.com/
