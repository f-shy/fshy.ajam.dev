# Vancine

> vancine.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vancine/ | JSON https://fshy.ajam.dev/api/v1/entity/vancine.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vancine

- `inference/vancine` | paid-only | evidence documented | binding none | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://vancine.com/docs
- free tier: After signing up, an initial token is automatically generated. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign up to receive a token; the fetched page does not state a free credit
- interface: rest
- limits:
  - volume-quota: token pricing is exposed at GET /api/pricing; no amount was readable in the captured pages [1]
- endpoint: https://vancine.com/v1
- composes with: No free text inference allowance is published in the fetched docs; the /api/pricing route was refused, so any price figure is unverified.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Vancine issues an initial API token after signup and prices tokens through a public pricing endpoint, with no free allowance stated | capture: sha256:bdf9ad259055b21a972d79c99166137c80132244fe2da6045d727fd21d8880b4 | quote: After signing up, an initial token is automatically generated.
- sources:
  - [1] https://vancine.com/docs
