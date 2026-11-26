# InferAll

> inferall.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inferall/ | JSON https://fshy.ajam.dev/api/v1/entity/inferall.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InferAll

- `inference/inferall` | qualifies | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://inferall.ai/docs
- free tier: Free NVIDIA NIM open models at USD 0 in and USD 0 out, alongside a free trial whose requests must name a routable model to stay free. | unit: tokens | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account for the trial; the USD 0 open models are reached with the same key
- interface: rest
- limits:
  - volume-quota (binding): the NVIDIA NIM open models are billed at USD 0 in and USD 0 out [1]
  - request-rate: a free-trial request must name a model the gateway can route, or it is not free [1]
- endpoint: https://api.inferall.ai/v1
- tooling: the Anthropic SDK pointed at the gateway with two environment variables
- composes with: the USD 0 model set is the scarce link, and an unnamed model silently leaves the free path
- reliability: a trial request without a model name is not free, which is a silent cost rather than an error
- evidence:
  - [1] 2026-11-18: NVIDIA NIM open models are USD 0 in and USD 0 out, and a free-trial call must name a routable model | capture: sha256:86202baf4524341ecc3ece56d116bf15af07ae145482b49a5a59c7210741f499 | quote: # Free NVIDIA NIM open models: $0 in, $0 out
- sources:
  - [1] https://inferall.ai/docs
