# Kunavo

> kunavo.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kunavo/ | JSON https://fshy.ajam.dev/api/v1/entity/kunavo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kunavo

- `inference/kunavo` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://kunavo.com/docs/quickstart
- free tier: No free allowance is stated on the quickstart read 2026-11-18: signup with Google or email magic link, then pay-as-you-go from a $10 minimum top-up; the balance never expires. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: signup via Google or email, then a $10 top-up (crypto or local-currency wallets; cards not yet enabled)
- interface: rest
- limits:
  - volume-quota (binding): $10 minimum top-up, pay-as-you-go, balance never expires; volume bonuses above $100 [1]
- endpoint: https://api.kunavo.com/v1
- tooling: an OpenAI-compatible key (sk-kn-) after a $10 top-up
- composes with: the $10 minimum top-up is the scarce link; no free text tier is published
- reliability: volume bonuses apply to larger top-ups; no free allowance is documented
- evidence:
  - [1] 2026-11-18: the account is pay-as-you-go from a $10 minimum top-up | capture: sha256:b7a7baa190745ce8792c07617def5a3cd3ed9f45cb2867193f8fad14288043b0 | quote: It's pay-as-you-go and starts from a $10 top-up
- sources:
  - [1] https://kunavo.com/docs/quickstart
