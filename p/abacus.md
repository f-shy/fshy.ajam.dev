# Abacus.AI ChatLLM Teams

> abacus.ai | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/abacus/ | JSON https://fshy.ajam.dev/api/v1/entity/abacus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Abacus.AI ChatLLM Teams

- `coding-subs/abacus-chatllm` | paid-only | evidence documented | binding request-rate | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T01:55:58.466Z (live) | stale on 2026-12-11
- url https://abacus.ai/pricing
- price parsed USD 10/mo
- free tier: no free tier. Basic USD 10 a user a month, discounted to USD 7 for the first month, with 20,000 credits a month and 3 AI Agent conversations a month; Pro USD 20 a user a month with 30,000 credits a month and unrestricted Agent and CLI use | unit: none | metered on: request-count | read on: 2026-10-22 | source: [1] | note: The page title states the ladder: 'ChatLLM Pricing | Basic 0, Pro 0 per user a month'. No free tier is offered. Pricing begins at Basic for USD 10.
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: card | detail: a paid subscription at USD 10 or USD 20 a user a month
- interface: cli, rest
- limits:
  - request-rate (binding): Basic: 20,000 credits a month and 3 AI Agent conversations a month. Pro: 30,000 credits a month with unrestricted Agent and CLI use [1]
- binding note: the three Agent conversations a month on Basic bind before the credit balance, so the credit count is the wrong number to size a plan on
- interface detail: the page names a coding IDE, a desktop listener and 'unrestricted use of Coding Agent and CLI' on Pro; no API endpoint is stated on the pricing page
- tooling: the vendor's own IDE and desktop client; a CLI is named on Pro
- composes with: the credit allowance is the scarce link, and the Basic tier's three Agent conversations a month bind long before the 20,000 credits do
- reliability: no reliability event recorded
- notes: This record was unverified at confidence: unverified on the claim that no first-party page had ever priced the product.
- evidence note: both tiers, both prices, both credit allowances and the three-conversation cap are quoted from abacus.ai/pricing read 2026-10-22 at 200 with 144207 bytes.
- extras:
  - monthly_usd: 10
- evidence:
  - [1] 2026-10-22: Basic USD 10 a user a month, USD 7 for the first month, 20,000 credits a month, 3 AI Agent conversations a month, a coding IDE and a desktop listener; Pro USD 20 a user a month, 30,000 credits a month, unrestricted Agent usage and unrestricted Coding Agent and CLI. The page title reads 'ChatLLM Pricing | Basic $10, Pro $20 per user a month'. No free tier appears
  - [1] 2026-11-10: the page states the pricing page states Basic at USD 10 a user a month | capture: sha256:18af0e93af7eeec588864aeca9cd2d11716d21b1f76633e7e229ddb58204a7d7 | quote: Basic $10, Pro $20 per user a month
- sources:
  - [1] https://abacus.ai/pricing
