# Privatemode AI

> privatemode.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privatemode/ | JSON https://fshy.ajam.dev/api/v1/entity/privatemode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Privatemode AI

- `inference/privatemode-ai` | trial-only | evidence documented | binding volume-quota | category confidential inference API, one-time free token quota
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://docs.privatemode.ai/pricing/
- free tier: a one-time free quota of 5 million tokens for new organizations; after it is exhausted, pay-as-you-go or Enterprise is required; rate limits are 200,000 prompt tokens/min, 20,000 completion tokens/min, 500,000 cached prompt tokens/min and 40 requests/min | unit: tokens | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an account and API key are set up in the portal; the rate-limits page says a payment card may be needed to unlock the initial quota before inference requests
- interface: rest
- limits:
  - volume-quota (binding): one-time Initial Token Quota of 5,000,000 tokens; HTTP 402 once exhausted [2]
  - request-rate: 200,000 prompt tokens/min, 20,000 completion tokens/min, 500,000 cached prompt tokens/min, 100 audio min/min, 40 requests/min [2]
- binding note: the 5,000,000-token one-time quota is finite and ends the free tier, so it binds before the per-minute rate
- endpoint: http://localhost:8080/v1
- tooling: the Privatemode SDK, a local proxy (OpenAI- and Anthropic-compatible) at localhost:8080, a desktop proxy app and a browser web app
- composes with: pairs with OpenAI- and Anthropic-compatible agents through the local proxy; the scarce link is a one-time quota that may need a card to unlock
- reliability: the free tier is a trial; after the quota is exhausted the API returns HTTP 402 until pay-as-you-go is enabled
- notes: 5M one-time tokens is an expiring-style trial quota rather than a standing tier, and the card requirement for unlock is stated in the rate-limits page.
- evidence:
  - [1] 2026-11-18: new organizations get a one-time 5 million token free quota | capture: sha256:4ff1f6d3bba6799122dfcccc478995a6010f7141da3ad0791f5f1e54901d862a | quote: Privatemode uses usage-based pricing. New organizations receive a one-time free quota of 5 million tokens.
  - [2] 2026-11-18: a card may be needed to unlock the initial quota, after which HTTP 402 is returned | capture: sha256:aad67c6c273882c594cc2b91e1b62fbe562b1cea9311d79002c9d4f487a7bd80 | quote: You may need to add a payment card in the portal to unlock this quota before making inference requests.
- sources:
  - [1] https://docs.privatemode.ai/pricing/
  - [2] https://docs.privatemode.ai/rate-limits/
