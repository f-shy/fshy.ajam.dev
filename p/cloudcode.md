# CloudCode.ONE

> cloudcode.one | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudcode/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudcode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudCode.ONE

- `inference/cloudcode` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://cloudcode.one
- free tier: No free allowance is stated on the pricing page read on 2026-11-18: it is pay-as-you-go, topping up credit from USD 2 with no monthly commitment, for GLM-5.3 with a 1M-token context window. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: credit is topped up before use, from USD 2
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit topped up from USD 2 with no monthly commitment [1]
- endpoint: https://api.cloudcode.one/v1
- tooling: the vendor's coding client against GLM-5.3
- composes with: the prepaid balance is the scarce link, and there is no allowance to start from
- reliability: a single-model service, so the whole subscription depends on GLM-5.3 staying available
- evidence:
  - [1] 2026-11-18: billing is pay-as-you-go from USD 2 with no monthly commitment and no stated free allowance | capture: sha256:b4a86afb448342768ee734c5a364c11965bc582415c9676dafcbf56730bc51cb | quote: - Pay only for what you use — top up from $2, no monthly commitment.
- sources:
  - [1] https://cloudcode.one
