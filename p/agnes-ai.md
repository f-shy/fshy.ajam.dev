# Agnes AI

> agnes-ai.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agnes-ai/ | JSON https://fshy.ajam.dev/api/v1/entity/agnes-ai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Agnes AI

- `inference/agnes` | paid-only | evidence documented | binding volume-quota | category inference subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://agnes-ai.com/en/docs/tokenplan
- free tier: No free tier for text. Input images beyond a model's free allowance incur a fixed fee converted into credits, and paid plans are USD 2.99 and USD 14.99 a month. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a subscription account; the page names no free text allowance
- interface: rest
- limits:
  - volume-quota (binding): image free allowance per model, then a fixed per-image fee in credits [1]
- endpoint: https://apihub.agnes-ai.com/v1
- tooling: an OpenAI-compatible base URL and the vendor console
- composes with: the paid plans are the scarce link, because the free allowance covers input images rather than text
- reliability: the free allowance is on images, so a text client pays from the first call
- evidence:
  - [1] 2026-11-18: input images beyond a model's free allowance carry a fixed fee in credits and plans are USD 2.99 and USD 14.99 a month | capture: sha256:cb8f07a15b467aa5ed78a849d03de86a2e61d1b5fd7d880e0174b579210a1c1d | quote: For image and video tasks, input images beyond the model’s free allowance incur a fixed fee converted into Credits. These excess input-image fees do not receive membership discounts. See [model pricing](https://agnes-ai.com/en/docs/pricing) for each model’s free allowance and excess rate.
- sources:
  - [1] https://agnes-ai.com/en/docs/tokenplan
