# Poe

> poe.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/poe/ | JSON https://fshy.ajam.dev/api/v1/entity/poe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Poe

- `inference/poe` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://creator.poe.com/docs/external-applications/openai-compatible-api
- free tier: No standing free API allowance is published: all Poe subscribers use their existing subscription points at no extra cost, and extra points must be purchased; rate limit is 500 requests per minute. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a paid Poe subscription supplies the points used by the API; add-on points are purchased
- interface: rest
- limits:
  - request-rate: 500 requests per minute; usage consumes subscription points [1]
  - volume-quota (binding): the binding constraint named on the first-party page [1]
- endpoint: https://api.poe.com/v1
- composes with: the subscription point balance is the scarce link
- reliability: points are shared with the web app and a 402 is returned when the balance is zero
- notes: 500 requests per minute is documented in the rate-limit headers section.
- evidence:
  - [1] 2026-11-18: API use consumes an existing paid Poe subscription's points rather than a free allowance | capture: sha256:1903158a618410da9d25bacc99ffbd2ae34c288dd4115bf39db884fae0983ed8 | quote: All Poe subscribers can use their existing subscription points with the API at no additional cost.
- sources:
  - [1] https://creator.poe.com/docs/external-applications/openai-compatible-api
