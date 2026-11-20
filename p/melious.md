# Melious

> melious.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/melious/ | JSON https://fshy.ajam.dev/api/v1/entity/melious.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Melious

- `inference/melious` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://melious.ai/pricing
- free tier: Pay-as-you-go per token with no minimum spend, or a paid monthly coding subscription from EUR 49; no standing free inference allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: credits are topped up; coding plans are offered to businesses and priced plus VAT
- interface: rest
- limits:
  - volume-quota (binding): pay-as-you-go per token, or EUR 49 / EUR 149 monthly coding plans [1]
- endpoint: https://api.melious.ai/v1
- composes with: the prepaid balance is the scarce link
- reliability: no standing free tier is stated for the inference API
- evidence:
  - [1] 2026-11-18: the inference API is prepaid per token with no minimum and no free allowance | capture: sha256:c899aafb41350eb55575fd291a575054a2ac6499bb1299573895293e8a22e443 | quote: Access the latest open-weight models on a pay-as-you-go basis. No commitments, no minimums. Just top up credits and go.
- sources:
  - [1] https://melious.ai/pricing
