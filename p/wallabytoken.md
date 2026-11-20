# Wallaby

> wallabytoken.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wallabytoken/ | JSON https://fshy.ajam.dev/api/v1/entity/wallabytoken.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wallaby

- `inference/wallaby` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://wallabytoken.com/docs
- free tier: A free trial credit on registration, enough for dozens of test calls, with no card needed; the first top-up is USD 5 and later top-ups start at USD 10. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: registration with email, password, a verification code by email and a quick human check, and no card for the trial credit
- interface: rest
- limits:
  - volume-quota (binding): a trial credit sized for dozens of test calls, with the first top-up at USD 5 [1]
- endpoint: https://api.wallabytoken.com/v1
- tooling: an OpenAI-compatible base URL with a prepaid balance
- composes with: the trial credit is the scarce link before the USD 5 first top-up
- reliability: a balance that never expires, so the only loss is the trial credit being small
- evidence:
  - [1] 2026-11-18: registration grants a free trial credit for dozens of test calls with no card, and the first top-up is USD 5 | capture: sha256:f7b94cf39ac56737d9f46e701c3ec994ab4028e1ca143082e61a40a700cec0d4 | quote: - Register — [create an account](https://api.wallabytoken.com/register): email, password, a verification code by email, and a quick human check. New accounts get $0.50 of free trial credit, enough for dozens of test calls. No card needed.
- sources:
  - [1] https://wallabytoken.com/docs
