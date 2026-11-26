# TokenWatt

> tokenwatt.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokenwatt/ | JSON https://fshy.ajam.dev/api/v1/entity/tokenwatt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TokenWatt

- `inference/tokenwatt` | trial-only | evidence documented | binding volume-quota | category inference gateway (prepaid)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://www.tokenwatt.io/api.html
- free tier: We email you a key, a private dashboard link and $1 of credit to try it. One account per email. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an email address receives the key and dashboard link; one account per email
- interface: rest
- limits:
  - volume-quota (binding): USD 1 of credit per email account; requests return 402 until topped up [1]
- endpoint: https://api.tokenwatt.io/v1
- composes with: A one-time trial credit rather than a standing free allowance.
- reliability: 402 when the credit runs out; a wake fee may apply on the H100 host
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: TokenWatt emails a key and USD 1 of trial credit per email account | capture: sha256:33654941003d6a556e33f73f20a118afde479b33b6095d2f9037527eedd8f68c | quote: We email you a key, a private dashboard link and $1 of credit to try it. One account per email.
- sources:
  - [1] https://www.tokenwatt.io/api.html
