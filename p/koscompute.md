# Kosmik Compute

> koscompute.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/koscompute/ | JSON https://fshy.ajam.dev/api/v1/entity/koscompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kosmik Compute

- `inference/kosmik` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://koscompute.com
- free tier: EUR 10 in free credits on signup, with an OpenAI-compatible EU-hosted API. Qwen 3.8 27B is priced at USD 0.35 per million input tokens after the credit. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account at app.koscompute.com/sign-up to receive the EUR 10 credit; the page states self-service with no waiting
- interface: rest
- limits:
  - volume-quota (binding): EUR 10 free credits on signup; Qwen 3.8 27B at USD 0.35 per million input tokens afterwards [1]
- endpoint: https://api.koscompute.com/v1
- tooling: an OpenAI-compatible base URL with a KOSCOMPUTE_API_KEY and the standard OpenAI SDK
- composes with: the one-off EUR 10 signup credit binds before the per-token prices
- reliability: the default chat model uses rented spare GPU capacity and may be unavailable while cards are rented; 429, 503 and 504 require retry per Retry-After
- notes: the only free allowance is a one-off EUR 10 signup credit, after which usage is per-token paid
- evidence:
  - [1] 2026-11-18: signup grants EUR 10 in free credits; the API is OpenAI-compatible and hosted in the EU with no data retention | capture: sha256:18c27904aebee8b3065bf17102cf3539ab7aebf9b95e5e2c378fb928facdd908 | quote: Get €10 in free credits when you sign up to try our API for free.
- sources:
  - [1] https://koscompute.com
