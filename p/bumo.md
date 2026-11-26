# Bumo Router

> bumo.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bumo/ | JSON https://fshy.ajam.dev/api/v1/entity/bumo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bumo Router

- `inference/bumo` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://bumo.ai/docs/api
- free tier: No free allowance is stated on the API docs read 2026-11-18: the gateway is pay-as-you-go with transparent pricing and purchase on demand. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an API key is created in the user area after an account is funded
- interface: rest
- limits:
  - volume-quota (binding): pay-as-you-go, purchase on demand; no free allowance stated [1]
- endpoint: https://router.bumo.ai/v1
- tooling: OpenAI and Anthropic-compatible keys used by Claude Code, OpenCode, Cline and Kilo Code
- composes with: the prepaid purchase-on-demand model is the scarce link; no free text tier is published
- reliability: no free quota is documented, so availability depends on purchased balance
- evidence:
  - [1] 2026-11-18: the gateway is pay-as-you-go with purchase on demand | capture: sha256:690a5c59a5aff36a828afcee8abeb71f299a56c6b61d340ccfd3c7857253f108 | quote: Transparent and controllable pricing, purchase on demand.
- sources:
  - [1] https://bumo.ai/docs/api
