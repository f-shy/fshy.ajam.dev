# UnoRouter

> unorouter.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unorouter/ | JSON https://fshy.ajam.dev/api/v1/entity/unorouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UnoRouter

- `inference/unorouter` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://unorouter.com/en/models
- free tier: Several models carry a :free suffix and no price (for example flint-v1.0:free, beam:free and step-5-preview:free), but subscriptions promise less waiting on free models, implying a queue; no standing free request allowance is published. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account is used for the shared balance; no card stated for free models
- interface: rest
- limits:
  - request-rate (binding): free models exist but paid subscriptions reduce waiting; no published free quota [2]
- endpoint: https://api.unorouter.com/v1
- composes with: free models are queued and no standing quota is published
- reliability: free models carry waiting that subscriptions reduce
- evidence:
  - [1] 2026-11-18: UnoRouter lists models with a :free suffix and no price | capture: sha256:08b737feed818d98c295367312a1041de4365b0905abce3f3339133fbb297269 | quote: flint-v1.0:free
- sources:
  - [1] https://unorouter.com/en/models
  - [2] https://unorouter.com/en/pricing
