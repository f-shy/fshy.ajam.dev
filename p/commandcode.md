# CommandCode

> commandcode.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/commandcode/ | JSON https://fshy.ajam.dev/api/v1/entity/commandcode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CommandCode

- `inference/commandcode` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://commandcode.ai/docs/provider
- free tier: No free allowance is stated on the pricing page read on 2026-11-18: the Provider plan starts at USD 15 a month plus a USD 1.01 processing fee, and pay-as-you-go starts with USD 15 of API credit and no monthly minimum. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the plan is billed monthly or topped up as credit
- interface: rest
- limits:
  - volume-quota (binding): USD 15 of API credit to start, then top-ups, with no monthly minimum on the pay-as-you-go path [1]
- endpoint: https://api.commandcode.ai/provider/v1
- tooling: the vendor CLI and its provider endpoint
- composes with: the monthly plan plus a processing fee is the scarce link, and the fee is charged whether or not the month is used
- reliability: a fixed processing fee sits on top of the plan price, so a short month still costs the fee
- evidence:
  - [1] 2026-11-18: the Provider plan is USD 15 a month plus a USD 1.01 processing fee, and pay-as-you-go starts from USD 15 of credit | capture: sha256:1b2ea5ea52beb13b48c8d9355ef014f947fbe5c1ff6ddfb770a545767a167afc | quote: The [Provider](https://commandcode.ai/provider) plan starts at $15/month + $1.01 processing fee. Pay as you go, no markup.
- sources:
  - [1] https://commandcode.ai/docs/provider
