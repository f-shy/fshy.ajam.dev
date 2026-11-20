# SparrowCodes

> sparrowcodes.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sparrowcodes/ | JSON https://fshy.ajam.dev/api/v1/entity/sparrowcodes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SparrowCodes

- `inference/sparrowcodes` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway (free model)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://sparrowcodes.com/models/sparrow/free
- free tier: Free coding model: 50 requests a day, up to 64000 tokens of context per request. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is required; the signup gate for the free model is not stated on the captured page
- interface: rest
- limits:
  - volume-quota (binding): 50 requests a day; 64,000-token context; 8,192-token maximum output [1]
- endpoint: https://api.sparrowcodes.com/v1
- composes with: The free model is sparrow/free at USD 0 per 1M input and output tokens. Whether signup needs a card is unverified.
- reliability: the page states free models may keep request data
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: SparrowCodes offers a sparrow/free coding model at 50 requests a day with 64K context | capture: sha256:a840ac6a9dede1bb5d42e8ff0605e169945f7774d76cb7fd36444b1dd3cfe7a4 | quote: Free coding model: 50 requests a day, up to 64000 tokens of context per request.
- sources:
  - [1] https://sparrowcodes.com/models/sparrow/free
