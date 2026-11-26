# nokeep

> nokeep.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nokeep/ | JSON https://fshy.ajam.dev/api/v1/entity/nokeep.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nokeep

- `inference/nokeep` | paid-only | evidence documented | binding request-rate | category inference gateway (public test key)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://nokeep.ai/docs/test-key
- free tier: `sk-nokeep-test` is a public key anyone can use. It checks your request the way a real key does, then answers with one fixed line instead of the model, for free. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: the test key is public and needs no signup, but it does not serve model inference
- interface: rest
- limits:
  - request-rate (binding): 20 requests a minute from one address; the fixed reply never reaches a model [1]
- endpoint: https://nokeep.ai/v1
- composes with: No free model inference: the key is a connectivity check that returns one fixed line and writes no call log.
- reliability: 429 rate_limited with Retry-After above 20 requests a minute
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: the public test key is free but returns a fixed line and never reaches a model | capture: sha256:611b26c164c1292b9a1ed4bd17c42d38bbe68ebac1888ec0e81c80321a6e5b86 | quote: `sk-nokeep-test` is a public key anyone can use. It checks your request the way a real key does, then answers with one fixed line instead of the model, for free.
- sources:
  - [1] https://nokeep.ai/docs/test-key
