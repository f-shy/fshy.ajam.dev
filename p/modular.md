# Modular

> modular.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modular/ | JSON https://fshy.ajam.dev/api/v1/entity/modular.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Modular

- `inference/modular` | paid-only | evidence documented | binding volume-quota | category inference cloud, pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://docs.modular.com/models
- free tier: no free tier: shared endpoints are serverless pay-as-you-go on multi-tenant infrastructure and are available to all organizations; no free token allowance is published | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Modular Cloud organization and API key are required; signup fields not stated on the models page
- interface: rest
- limits:
  - volume-quota (binding): shared endpoints are serverless pay-as-you-go; no free allowance is published [1]
- binding note: no free tokens stated, so payment binds first
- endpoint: https://api.modular.com/v1
- tooling: an OpenAI-compatible key and the Modular CLI
- composes with: pairs with an OpenAI-compatible agent on a pay-as-you-go balance
- reliability: no reliability event recorded
- notes: five models have shared serverless endpoints; the rest need dedicated deployments; no free tier appears.
- evidence:
  - [1] 2026-11-18: shared endpoints are serverless pay-as-you-go | capture: sha256:6ee968db3665f486215379a8ddffba241fb6640a0f6320f5b08d0ddb60291b15 | quote: Shared endpoints provide serverless, pay-as-you-go inference on multi-tenant infrastructure. They are automatically available to all organizations.
- sources:
  - [1] https://docs.modular.com/models
