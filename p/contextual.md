# Contextual AI reranker API

> contextual.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/contextual/ | JSON https://fshy.ajam.dev/api/v1/entity/contextual.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Contextual AI reranker API

- `inference/contextual-ai-rerank` | trial-only | evidence documented | binding volume-quota | category rerank API, one-time free credit on signup | tier On-Demand
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
- url https://contextual.ai/pricing
- free tier: new signups receive USD 25 in free credits, USD 50 with a work email; the rerank API launch post states the first USD 50 as 1 billion tokens. Rerank-v2 costs USD 0.05 per million tokens and Rerank-v2-mini USD 0.02 | unit: credits | metered on: request-count | read on: 2026-11-03 | source: [1] | note: the credit is USD and is shared with the vendor's agent and parse products; whether the USD 25 credit applies to the standalone rerank endpoint is stated only by the launch post for the work-email case
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account on the vendor's app; a work email earns USD 50 where another address earns USD 25; the billing page asks for a card only to add credits; unverified: the sign-up form fields, because the app page could not be read
- interface: rest
- limits:
  - volume-quota (binding): USD 25 of free credit (USD 50 with a work email), one-time; at USD 0.05 per million tokens USD 25 covers 500 million rerank-v2 tokens (derived), and the launch post states USD 50 as 1 billion tokens [1]
  - per-object-cap: one request may carry at most 400,000 tokens in total, and the query, instruction and any single document with its metadata at most 8,000 tokens [2]
  - request-rate: unverified: no requests-per-minute figure for the standalone rerank endpoint was found on the pages read [2]
- binding note: the one-time USD credit is spent first; no request-rate figure is published for the rerank endpoint
- endpoint: https://api.contextual.ai/v1/rerank
- tooling: POST https://api.contextual.ai/v1/rerank with a bearer key; Python SDK; the reranker weights are also on Hugging Face
- composes with: a rerank-only offer: it takes the candidates that any embedding API or keyword search returned as the first stage
- reliability: no reliability event recorded; the free credit does not renew
- notes: derived: USD 25 / USD 0.05 per million tokens = 500 million tokens of rerank-v2
- evidence note: the credit amounts, prices and request caps are quoted from vendor pages; the standalone-rerank rate limit and the sign-up form are unverified.
- evidence:
  - [1] 2026-11-03: new signups receive USD 25 in free credits, USD 50 with a work email | capture: sha256:bdcbc58cd0b6053041f0e5b5da47b25c544b638334152ae756159005b68263b7 | quote: Yes. New signups receive \$25 in free credits (\$50 with a work email) to build and query agents.
  - [3] 2026-11-03: the rerank API launch post gives the first USD 50, stated as 1 billion tokens, free for a business email | capture: sha256:aa3977ee7be4855e6e8064def367ef086e409668ebe170800a2120d76aa652eb | quote: The first $50 (1 billion tokens) are free when you sign up with a business email.
  - [4] 2026-11-03: the rerank-v2 price per million tokens | capture: sha256:27487884b66b0ce13835117252e968a26642007bd98499e6421bcb1a9f500978 | quote: - Rerank-v2: $0.05 per million tokens
  - [4] 2026-11-03: the rerank-v2-mini price per million tokens | capture: sha256:27487884b66b0ce13835117252e968a26642007bd98499e6421bcb1a9f500978 | quote: - Rerank-v2-mini: $0.02 per million tokens
  - [2] 2026-11-03: per-request caps of 400,000 tokens in total and 8,000 tokens per query, instruction and document | capture: sha256:fa1f93673abbe72063c1bd69376f2cdd882290cc6a2991179cdfd0c22b49e935 | quote: The total request cannot exceed 400,000 tokens. The combined length of the query, instruction and any document with its metadata must not exceed 8,000 tokens.
  - [5] 2026-11-03: a card is asked for when topping up credits | capture: sha256:43fa7c24ba7ef2089be2a5e9209f78ebb5e3e21837e4e8980fecebb216dd72a5 | quote: 2. Add a valid credit card under Payment Methods if you haven't already
  - probe:https://api.contextual.ai/v1/rerank 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 503, so the endpoint is failing | capture: sha256:76e5a6deb20602b217392df098092e9b0ab53506a2939b9e62f8a03cdfb24cb8 | quote: "status": 503
- sources:
  - [1] https://docs.contextual.ai/reference/faq.md
  - [2] https://docs.contextual.ai/api-reference/rerank/rerank.md
  - [3] https://contextual.ai/blog/rerank-v2
  - [4] https://contextual.ai/pricing
  - [5] https://docs.contextual.ai/admin-setup/pricing-billing.md
