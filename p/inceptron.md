# Inceptron

> inceptron.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inceptron/ | JSON https://fshy.ajam.dev/api/v1/entity/inceptron.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inceptron

- `inference/inceptron` | paid-only | evidence unverified | binding none | category serverless inference endpoint, keyed
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-03
- url https://docs.inceptron.io
- free tier: unverified: the captured Get Started page shows only an OpenAI-compatible keyed API call and states no free tier, price, or free-token allowance | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1] | note: no pricing or free-tier statement on the page read
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key (INCEPTRON_API_KEY) is required; signup fields not stated on the Get Started page
- interface: rest
- binding note: no limit is published on the page read
- endpoint: https://api.inceptron.io/v1
- tooling: an OpenAI-compatible client with INCEPTRON_API_KEY
- composes with: pairs with an OpenAI-compatible agent through a key; no free route is documented on the page read
- reliability: no reliability event recorded
- notes: no self-serve free offer is documented; recorded to stop rediscovery. A pricing route could not be located from the docs page.
- evidence note: only the Get Started call examples were readable; no pricing or free-allowance statement was found on this first-party page
- evidence:
  - [1] 2026-11-18: the API is keyed and OpenAI-compatible with no free offer stated | capture: sha256:19ed00a70a185802b80548f2a76e038b02ca3d36fc8c1b81c181203d1653a9f8 | quote: Deploy your first AI application in minutes. Leverage our serverless platform to scale effortlessly.
- sources:
  - [1] https://docs.inceptron.io
