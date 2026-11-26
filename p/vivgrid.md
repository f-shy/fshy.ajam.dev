# Vivgrid

> vivgrid.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vivgrid/ | JSON https://fshy.ajam.dev/api/v1/entity/vivgrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vivgrid

- `inference/vivgrid` | paid-only | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://vivgrid.com/pricing
- free tier: Free plan is USD 0 to start with pay-as-you-go model usage at 5M TPM and 100 RPM and 1-day API log retention; model usage is billed per token at each model's listed rate, so there is no free token allowance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in at the console to start on the Free plan; no card stated at signup
- interface: rest
- limits:
  - request-rate (binding): Free plan: 5M TPM and 100 RPM; usage billed per token [1]
- endpoint: https://api.vivgrid.com/v1
- composes with: the absence of free tokens and the 100 RPM cap bind first
- reliability: the Free plan has no included token credit and is rate limited to 5M TPM / 100 RPM
- evidence:
  - [1] 2026-11-18: the Free plan is pay-as-you-go with no included token allowance | capture: sha256:d497f5765d6f6592432ba74ceeb35b850518fbf96a4e94112ddbeeda522ebf76 | quote: Pay-as-you-go model usage
- sources:
  - [1] https://vivgrid.com/pricing
