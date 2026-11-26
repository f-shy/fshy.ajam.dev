# Outer Labs

> outerlabs.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/outerlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/outerlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Outer Labs

- `inference/outerlabs` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://outerlabs.ai/docs
- free tier: Sign up and verify your email. New accounts start with $5 of credit and no card is required. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: email signup and verification; no card at registration
- interface: rest
- limits:
  - volume-quota (binding): USD 5 of starting credit; a hold sized by max_tokens is placed on every request [1]
- endpoint: https://api.outerlabs.ai/v1
- composes with: A one-time signup credit rather than a standing free allowance.
- reliability: 402 when the balance cannot cover a request hold; nothing is queued
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Outer Labs grants USD 5 of signup credit after email verification with no card | capture: sha256:f38da669b617513e0e66e1df48abf7c900f534093b13932219cecb080f07aab8 | quote: Sign up and verify your email. New accounts start with $5 of credit and no card is required.
- sources:
  - [1] https://outerlabs.ai/docs
