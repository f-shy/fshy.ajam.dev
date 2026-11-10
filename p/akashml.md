# AkashML

> akashml.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akashml/ | JSON https://fshy.ajam.dev/api/v1/entity/akashml.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AkashML (Akash Chat API)

- `inference/akashml` | trial-only | evidence documented | binding volume-quota | category inference endpoint, decentralised GPU network, trial credit behind a payment method
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:21:07.039Z (live) | stale on 2026-12-05
- url https://akashml.com/
- free tier: Trial credits are granted when a payment method is verified during onboarding; the amount is not stated on the current documentation pages. A launch post of 22 November 2025 stated 'New accounts receive $100 in AI token credits'. Trial credits expire; purchased credits do not. | unit: none | metered on: unstated | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an email address (or a Google or GitHub sign-in) is verified at signup, and a payment method must be verified during onboarding before trial credits are granted; payments run through Stripe
- interface: rest
- limits:
  - request-rate: unpublished platform-wide; each API key carries optional caps set by its owner for requests per minute, tokens per minute and concurrent requests, and a request over a cap returns HTTP 429 with X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset and Retry-After headers [1]
  - volume-quota (binding): trial credit of unstated size that expires; HTTP 402 is returned when credits run out; unverified: behind a sign-up [1]
- binding note: the trial credit balance is the only free resource and it expires; once spent, every request needs purchased credit
- endpoint: https://api.akashml.com/v1/chat/completions
- tooling: OpenAI-compatible REST at https://api.akashml.com/v1 and an Anthropic-compatible Messages endpoint at https://api.akashml.com/anthropic; any SDK with a custom base URL
- composes with: a drop-in base URL for OpenAI and Anthropic clients once a payment method is on file; the documentation carries a Claude Code guide that points the Messages endpoint at open models
- reliability: no reliability event recorded
- notes: chat.akash.network is a browser chat front end whose API Access entry points at akashml.com, where the API is served. Its terms allow use without an account, with rate limiting and IP-based access controls; no numeric limit is published. Its models page lists two text models and one image generation model (AkashGen).
- evidence note: documentation pages only; the size of the current trial credit sits behind the signed-in dashboard and is unverified
- evidence:
  - [1] 2026-10-28: the quick start places adding a payment method before trial credits are received | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: 2. Add a payment method during onboarding to receive trial credits.
  - [1] 2026-10-28: signup is an account verified by email | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: 1. Create an account at [akashml.com/login](https://akashml.com/login) and verify your email.
  - [1] 2026-10-28: trial credits expire and purchased credits do not | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: Credit pools have optional expiration dates. Trial credits expire; purchased credits do not.
  - [1] 2026-10-28: each API key can carry a requests-per-minute cap; no platform-wide figure is stated | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: - Rate limit (RPM) — Maximum requests per minute.
  - [1] 2026-10-28: a request over a cap returns 429 | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: | `429` | Rate limit exceeded |
  - [1] 2026-10-28: an empty balance returns 402 | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: | `402` | Insufficient credits |
  - [1] 2026-10-28: the API is OpenAI-compatible with an Anthropic-compatible Messages endpoint | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: integrate via the OpenAI-compatible REST API at `api.akashml.com` and the Anthropic-compatible Messages endpoint at `api.akashml.com/anthropic`
  - [2] 2026-10-28: payment methods are card payments processed by Stripe | capture: sha256:d38c7aae5b63d81b4474dc2dd4a52918455ad9a3e5840bc0ae2cee275bba92ce | quote: AkashML uses Stripe for payment processing
  - [3] 2026-10-28: a launch post of 22 November 2025 stated USD 100 in credits for new accounts; the current documentation does not repeat the amount | capture: sha256:cd45c201c2846a25390e24fa3a7aed3e590ca49817ec03cab2a32d9ed7c6dbcc | quote: New accounts receive $100 in AI token credits, which can be used across all supported models in both the Playground and the API platform.
  - [4] 2026-10-28: the AkashChat web app links its API Access entry to akashml.com | capture: sha256:72623f9f709cfa57e2f06b1723b3883972c1701575b93f2b3349ed87adab038d | quote: [API Access](https://akashml.com/)
  - [5] 2026-10-28: the catalogue prices per 1M tokens; the cheapest listed text row is openai/gpt-oss-20b at USD 0.02 input and USD 0.10 output | capture: sha256:e770c2ade5e9c7ed355f77ab667b6c94ca1c4d924a665100ac139fee858f2ebc | quote: | `openai/gpt-oss-20b` | 131K | $0.02 | $0.10 | — |
  - [6] 2026-11-04: the browser chat can be used without an account, subject to rate limiting | capture: sha256:2bfd3a0fc03629872edbc63e69aeb2a68b2ce16581cd1bef33c01e485383e54e | quote: Anonymous users may use the Service with rate limiting without marketing consent requirements
  - [6] 2026-11-04: anonymous browser chat use is limited by IP address | capture: sha256:2bfd3a0fc03629872edbc63e69aeb2a68b2ce16581cd1bef33c01e485383e54e | quote: Anonymous usage is subject to IP-based access controls
  - [7] 2026-11-04: the chat models page lists two text models and the AkashGen image generation model | capture: sha256:f04f4bc6e54e5f9f07f862861de44847d14838bfd96e3d0bd30cdfadc18a6eba | quote: Generate images using AkashGen
  - [1] 2026-11-04: trial credits are granted after onboarding; their size is not on the public pages | capture: sha256:fa3fbd14d4e415cbc0e229d45af4b2fa77c884570eec2989e6d44de7bda6e09a | quote: 2. Add a payment method during onboarding to receive trial credits.
  - probe:https://api.akashml.com/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:ed76abe983af4870cdf50718c5f6530f7d0112335550032ecad36c67a7723c2a | quote: "status": 401
- sources:
  - [1] https://akashml.com/docs/getting-started/introduction
  - [2] https://akashml.com/docs/platform/settings
  - [3] https://akash.network/blog/akashml-managed-ai-inference-on-the-decentralized-supercloud/
  - [4] https://chat.akash.network/
  - [5] https://akashml.com/docs/platform/models
  - [6] https://chat.akash.network/terms/
  - [7] https://chat.akash.network/models
