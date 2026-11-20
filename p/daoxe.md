# DaoXE

> daoxe.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/daoxe/ | JSON https://fshy.ajam.dev/api/v1/entity/daoxe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DaoXE

- `inference/daoxe` | paid-only | evidence documented | binding write-gated | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://daoxe.com/docs/
- free tier: No free allowance is stated on the docs read 2026-11-18: the prerequisite is a logged-in, topped-up account with a created key before any model call. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a logged-in account with a funded balance is required before a key works
- interface: rest
- limits:
  - volume-quota: account must be logged in and topped up before a key can call models [1]
  - write-gated (binding): the binding constraint named on the first-party page [1]
- endpoint: https://daoxe.com/v1
- tooling: an OpenAI/Claude-compatible key created in the account
- composes with: the top-up prerequisite is the scarce link; no free text allowance is published
- reliability: the /pricing route returned an error page on 2026-11-18, so no price table could be read
- evidence:
  - [1] 2026-11-18: a topped-up logged-in account is a prerequisite for key use | capture: sha256:9fee3080d313c8cd98de4a8ffd5c90c98e67fcd36b9b928d342d11cd83c5ea7e | quote: 已登录并充值
- sources:
  - [1] https://daoxe.com/docs/
