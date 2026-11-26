# Logits

> logits.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/logits/ | JSON https://fshy.ajam.dev/api/v1/entity/logits.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Logits

- `inference/logits` | paid-only | evidence documented | binding request-rate | category inference gateway (post-trained models)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://logits.com/docs
- free tier: Rate limits: a per-account, per-model rolling-minute budget of 600 requests, 8M input tokens and 2M output tokens. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign up at app.logits.com or book a demo; no self-serve free offer is published
- interface: rest
- limits:
  - request-rate (binding): 600 requests, 8M input tokens and 2M output tokens per minute per account and model [1]
- endpoint: https://api.logits.com/v1
- composes with: No free text inference allowance is stated in the fetched docs; the page only names rate limits and a signup or demo route.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: the docs publish a per-account rolling-minute budget but no free inference allowance | capture: sha256:daf8963c9f5d269d88d6c054d1b0be5a3712272982f71b991283f2bfda163568 | quote: Rate limits: a per-account, per-model rolling-minute budget of 600 requests, 8M input tokens and 2M output tokens.
- sources:
  - [1] https://logits.com/docs
