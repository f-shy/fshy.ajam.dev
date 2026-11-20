# Adzuki AI

> adzukiai.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adzukiai/ | JSON https://fshy.ajam.dev/api/v1/entity/adzukiai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Adzuki AI

- `inference/adzuki` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://adzukiai.com/models
- free tier: No free allowance is stated. Input runs from USD 0.0519 per million tokens on doubao-seed-2.0-lite and output from USD 0.19; there is no subscription and no monthly minimum. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: email signup plus a card for the prepaid balance; no phone verification and no Chinese identity check
- interface: rest
- limits:
  - volume-quota (binding): prepaid balance from USD 0.0519 per million input tokens; no subscription or monthly minimum [1]
- endpoint: https://adzukiai.com/v1
- tooling: an OpenAI-compatible base URL and key; no proprietary SDK or local proxy
- composes with: the prepaid card-funded balance is the scarce link; there is no standing free text tier
- reliability: requests are processed on infrastructure in mainland China; failed calls through the provider are not charged
- notes: no free text allowance is published; the pricing page is the first-party model list reached by the /pricing redirect
- evidence:
  - [1] 2026-11-18: signup needs email and card; no phone verification and no Chinese identity check; billing is per token with no subscription | capture: sha256:731042929f68d119e2e561bd6549d567f6263379016dbf8ccf87e98d4da436ab | quote: No. You sign up with an email address and pay by card. There is no phone verification and no Chinese identity check.
- sources:
  - [1] https://adzukiai.com/models
