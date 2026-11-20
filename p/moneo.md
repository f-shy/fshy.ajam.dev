# Moneo

> moneo.one | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/moneo/ | JSON https://fshy.ajam.dev/api/v1/entity/moneo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Moneo

- `inference/moneo` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://moneo.one/
- free tier: A free trial balance is granted to new users without a card, but access is through a Telegram account and ongoing use requires a USD 10+ subscription paid in USDT or USDC. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: a Telegram account is required to start, which needs a phone number; no card at signup
- interface: rest
- limits:
  - volume-quota (binding): free trial balance for new users; subscription from USD 10 paid in USDT or USDC [1]
- endpoint: https://api.moneo.one/v1
- composes with: the trial balance is the only free route and needs a Telegram account
- reliability: the service routes through third-party accounts, so access can disappear without notice
- evidence:
  - [1] 2026-11-18: new users receive a trial balance without linking a card | capture: sha256:52b5fc4eb83c67a86cac2c02c09d62b2479d3a01eafd096039107634ae3d3b6f | quote: Новые пользователи получают пробный баланс без привязки карты.
- sources:
  - [1] https://moneo.one/
