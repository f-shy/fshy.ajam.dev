# TokenRouter

> tokenrouter.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokenrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/tokenrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TokenRouter

- `inference/tokenrouter` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://www.tokenrouter.com/docs/tokenrouter-feature-guide/
- free tier: A personal balance funds all requests and is topped up on the Balance page; no standing free inference allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an account with a topped-up balance is required; no free tier stated
- interface: rest
- limits:
  - volume-quota (binding): personal or enterprise balance, topped up before use; no free tier stated [1]
- endpoint: https://api.tokenrouter.com/v1
- composes with: the prepaid balance is the scarce link
- reliability: the service warns that the balance must be kept sufficient to avoid interruption
- evidence:
  - [1] 2026-11-18: TokenRouter uses a prepaid personal or enterprise balance with no published free allowance | capture: sha256:e402c77a43a4af971ac1fdf0312e1b78982a826b382d3add75145fed0be4b375 | quote: | Balance Management | Personal balance | Unified enterprise balance |
- sources:
  - [1] https://www.tokenrouter.com/docs/tokenrouter-feature-guide/
