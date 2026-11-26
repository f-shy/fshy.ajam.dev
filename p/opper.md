# Opper

> opper.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opper/ | JSON https://fshy.ajam.dev/api/v1/entity/opper.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Opper

- `inference/opper` | qualifies-with-caveat | evidence documented | binding none | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://opper.ai/pricing
- free tier: Sign-up needs no credit card: an API key is issued immediately and free models work in the playground and the API; premium models need a card, and token rates are passed through at cost with a 3% credit-purchase fee. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign-up needs no credit card and issues an API key straight away
- interface: rest
- limits:
  - volume-quota: free models usable without a card; no published standing free request allowance [1]
- endpoint: https://api.opper.ai/v3/compat
- composes with: no fixed free allowance is published, so the free model list is the constraint
- reliability: the free model lineup is not published as a standing quota and can change
- notes: Organizations with no card are capped at 60 management requests per minute and 3 active management keys.
- evidence:
  - [1] 2026-11-18: sign-up needs no card and free models work through the API | capture: sha256:af3f3098bd1707d13555f6111f3b10c0323fc13fecca764bd169a6b7c4e2584f | quote: Sign up needs no credit card: you get an API key straight away and the free models work in the playground and the API.
- sources:
  - [1] https://opper.ai/pricing
