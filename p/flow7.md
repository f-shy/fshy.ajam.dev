# Infer by Flow7

> flow7.org | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flow7/ | JSON https://fshy.ajam.dev/api/v1/entity/flow7.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Infer by Flow7

- `inference/infer` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://infer.flow7.org/opencode
- free tier: No free inference allowance is stated. An account, a verified email and service credit are required before a model can be called; a public skill catalog needs neither account nor API key. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account, verify the email, add service credit; the public skill catalog itself needs no key
- interface: rest
- limits:
  - volume-quota (binding): service credit required before a bounded run; no free token allowance stated [1]
- endpoint: https://infer.flow7.org/v1
- tooling: an OpenAI Responses endpoint reached with an INFER_API_KEY; OpenCode configuration generator and an Agent Skill
- composes with: the service credit and verified email are the scarce links; the free catalog is documentation, not inference
- reliability: status is the callability source and an unavailable model stops a paid run; a bounded live run cost USD 0.013617 across two receipts
- notes: no standing free inference allowance is published; the reachable free path is a public skill catalog, not free model calls
- evidence:
  - [1] 2026-11-18: an account, verified email and service credit are required; the public skill catalog needs neither account nor key but does not provide inference | capture: sha256:108a6e79e5eb593896c062281c1ed1d6ba0309a65e0670cbe868afeee5572426 | quote: Create an account, verify the email, add service credit, and start with a bounded task.
- sources:
  - [1] https://infer.flow7.org/opencode
