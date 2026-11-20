# LLMTR

> llmtr.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/llmtr/ | JSON https://fshy.ajam.dev/api/v1/entity/llmtr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LLMTR

- `inference/llmtr` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://llmtr.com/docs/billing/
- free tier: No standing free allowance is published: usage is prepaid credit with an 8% top-up margin; gift credits may be added manually by LLMTR, but there is no self-serve free tier. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: top-up by credit card on a secure checkout; crypto is not accepted
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit only, with an 8% margin added at top-up [1]
- endpoint: https://llmtr.com/v1
- composes with: the account must be funded by card before use
- reliability: gift credits are discretionary and manually assigned, so they are not a standing allowance
- notes: Gift ('Hediye') credits are manually granted, not self-serve.
- evidence:
  - [1] 2026-11-18: topping up credit adds an 8% platform margin, and there is no standing free allowance | capture: sha256:6694d3a4eb436a25b3ad594366e0af4ddbe45982d198e879888fc36345cadd39 | quote: Kredi yüklerken talep edilen tutarın üzerine
- sources:
  - [1] https://llmtr.com/docs/billing/
