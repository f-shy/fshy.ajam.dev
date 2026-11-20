# ProxyStacks Relay

> proxystacks.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxystacks/ | JSON https://fshy.ajam.dev/api/v1/entity/proxystacks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ProxyStacks Relay

- `inference/proxystacks` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://proxystacks.com/en/pricing
- free tier: Prepaid USD balance with one-time recharge tiers from USD 10 to USD 500; the balance never expires and there is no free inference allowance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: recharge is a one-time card purchase processed by Waffo Pancake
- interface: rest
- limits:
  - volume-quota (binding): one-time USD 10-500 recharge tiers, metered at published token rates [1]
- endpoint: https://proxystacks.com/v1
- composes with: the prepaid balance is the scarce link
- reliability: calls pause when the balance cannot cover the estimated cost
- evidence:
  - [1] 2026-11-18: Relay is a prepaid USD service with no free inference allowance | capture: sha256:a0ba8abd13bf3c50aed297530f8302fe29a2d463f1cb3411c8f3436d1f7262ec | quote: Prepaid USD balance, metered at published token rates as you go.
- sources:
  - [1] https://proxystacks.com/en/pricing
