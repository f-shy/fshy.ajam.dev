# CheapestToken

> cheapest-token.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cheapest-token/ | JSON https://fshy.ajam.dev/api/v1/entity/cheapest-token.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CheapestToken

- `inference/cheapest-token` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://cheapest-token.com/docs
- free tier: No free allowance is stated. An account and a prepaid API key are created in the console, and usage bills from the prepaid wallet at the published model prices. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account and a prepaid API key in the console
- interface: rest
- limits:
  - volume-quota (binding): prepaid wallet billed at the published per-model prices [1]
- endpoint: https://api.cheapest-token.com/v1
- tooling: an sk- key connected through OpenCode or an OpenAI-compatible client
- composes with: the prepaid wallet is the scarce link; no free text tier is published
- reliability: a key can be revoked at any time from the console; usage draws from the prepaid wallet
- notes: no standing free inference allowance is published; the prepaid wallet funds all usage
- evidence:
  - [1] 2026-11-18: an account and a prepaid API key are required; usage bills from a prepaid wallet at the published model prices | capture: sha256:695091668074c53251b5865ac0ff2c8864a3c9a0683a557c94128e41ed54a294 | quote: Create an account and a prepaid API key in the console
- sources:
  - [1] https://cheapest-token.com/docs
