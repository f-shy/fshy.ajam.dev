# Pendra

> pendra.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pendra/ | JSON https://fshy.ajam.dev/api/v1/entity/pendra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pendra

- `inference/pendra` | paid-only | evidence documented | binding none | category inference gateway (self-hosted worker)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://pendra.ai/pricing
- free tier: Rent on-demand GPU workers by the hour, pay as you go | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: free account at console.pendra.ai; the free tier needs the user's own GPU hardware for a worker
- interface: rest
- limits:
  - write-gated: Free plan includes 1 self-hosted worker; on-demand GPUs bill hourly; Pro is GBP 99 a month [1]
- endpoint: https://api.pendra.ai/api/v1
- composes with: The free tier serves inference only from a worker the user installs on their own GPU; Pendra hosts no free inference allocation. The models.dev free-model list reflects that per-account worker catalogue.
- reliability: requests to a model not installed on any worker return an error
- notes: the same as composes with
- self hosted: no
- evidence:
  - [1] 2026-11-18: Pendra's free plan provides one self-hosted worker and hourly on-demand GPU rental, with no hosted free inference | capture: sha256:33c15dd02a24a3707a72d6765f277e8b28551ec3ee37216519cf3ced32346c8b | quote: Rent on-demand GPU workers by the hour, pay as you go
- sources:
  - [1] https://pendra.ai/pricing
