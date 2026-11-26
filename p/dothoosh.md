# DotHoosh

> dothoosh.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dothoosh/ | JSON https://fshy.ajam.dev/api/v1/entity/dothoosh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DotHoosh

- `inference/dothoosh` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://gateway.dothoosh.com/docs
- free tier: No free allowance is stated on the docs read 2026-11-18: the user creates an account, charges the wallet in tomans, creates a key and sends the first request. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an account with a wallet charged in tomans is required before a key can call models
- interface: rest
- limits:
  - request-rate: per-key RPM, TPM and concurrency limits; wallet charged in tomans before use [1]
  - volume-quota (binding): the binding constraint named on the first-party page [1]
- endpoint: https://gateway.dothoosh.com/v1
- tooling: an OpenAI/Anthropic-compatible key (dh_) with per-key RPM/TPM/concurrency caps
- composes with: the funded-wallet requirement is the scarce link; no free text tier is published
- reliability: the gateway does not store prompt/response text, only metadata; provider free pools are not published
- evidence:
  - [1] 2026-11-18: the wallet must be charged in tomans before the first request | capture: sha256:433f767ce9a9208a3702321ac78983c69c4aebf75cec31686f47f19479c52b81 | quote: حساب بسازید، کیف پول را به تومان شارژ کنید
- sources:
  - [1] https://gateway.dothoosh.com/docs
