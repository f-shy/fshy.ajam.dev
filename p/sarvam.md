# Sarvam AI

> sarvam.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sarvam/ | JSON https://fshy.ajam.dev/api/v1/entity/sarvam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sarvam AI

- `inference/sarvam` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.sarvam.ai/api/getting-started/pricing
- free tier: Free credits: 'Sarvam offers ₹100 worth of free credits for every verified user on signup'; credits are universal and never expire, and are used across any API. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a verified user account; 'verified user' gate stated but no card or phone detail given
- interface: rest
- limits:
  - volume-quota (binding): INR 100 free credits at signup, never expire [1]
  - request-rate: 50 req/min default language models on Pay as you go [1]
- endpoint: https://api.sarvam.ai/v1
- tooling: Sarvam SDK and OpenAI-compatible clients
- composes with: a one-time INR 100 credit balance is the scarce link; after exhaustion requests fail with 402
- reliability: credits never expire; 402 insufficient_quota_error after exhaustion is separate from a 429 rate limit
- notes: One-time free credit balance documented; no public read path was probed.
- evidence:
  - [1] 2026-11-18: free credits are granted on signup and never expire | capture: sha256:b3f47211364a6c2f2c042765a22becc3c4c6a4434b8d4e2757773f69d8be19cf | quote: Sarvam offers ₹100 worth of free credits for every verified user on signup.
- sources:
  - [1] https://docs.sarvam.ai/api/getting-started/pricing
