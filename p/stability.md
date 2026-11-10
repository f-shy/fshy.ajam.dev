# Stability AI

> stability.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stability/ | JSON https://fshy.ajam.dev/api/v1/entity/stability.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stability AI (Compute)

- `compute/stability-ai` | trial-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://platform.stability.ai/pricing
- free tier: 'Get started with 25 free credits', where '1 credit equals $0.01', so the free allowance is USD 0.25 of API usage. At the listed per-call prices that is 3 images on Stable Diffusion 3.5 Large (6.5 credits), 3 images on Stable Image Ultra (8), 10 on SD 3.5 Flash (2.5), 3 audio generations of up to six minutes on Stable Audio 3.0 (8 credits), or 27 SDXL 1.0 images at the 0.9-credit floor. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): USD 0.25 of credit is 25 hundredths of a dollar: the largest single useful output is three six-minute audio clips or three Ultra images, and one Creative Upscaler call at 60 credits costs more than two free accounts. [1]
- limits note: USD 0.25 of credit is 25 hundredths of a dollar: the largest single useful output is three six-minute audio clips or three Ultra images, and one Creative Upscaler call at 60 credits costs more than two free accounts.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 25 credits allow testing API integration. The allowance is one-time and does not renew, while generating 100 images on SD 3.5 Flash requires 250 credits.
- reliability: no reliability event recorded
- notes: Stability AI provides an initial one-time promotional grant of 25 API credits (approximately USD 0.25 in model generation value) for testing developer endpoints.
- extras:
  - facets.class: credit-too-small-for-a-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Get started with 25 free credits' and '1 credit equals $0.01', quoted from the page's own pricing notes
  - [1] 2026-10-22: the image table prices 'Stable Image Ultra ... 8', 'Stable Diffusion 3.5 Large ... 6.5', 'Stable Diffusion 3.5 Flash ... 2.5', 'SDXL 1.0 ... From 0.9', quoted
  - [1] 2026-10-22: the audio table prices 'Stable Audio 3.0 ... Generate up to six minutes ... 8' credits, quoted
- sources:
  - [1] https://platform.stability.ai/pricing

## Stability AI (Inference)

- `inference/stability-ai` | trial-only | evidence documented | binding volume-quota | category image, audio and 3D generation API, one-time signup credit
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
- url https://platform.stability.ai/pricing
- free tier: 25 free credits for a new account, where 1 credit equals USD 0.01, so the grant is USD 0.25 of API usage; one-time, and the getting-started guide ties the grant to creating the account with Google's social login. At the listed per-call prices 25 credits buys 3 calls of Stable Diffusion 3.5 Large (6.5 credits each), 3 of Stable Image Ultra (8), 10 of Stable Diffusion 3.5 Flash (2.5) or 3 of Stable Audio 3.0 (8, up to six minutes of audio each). | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: models: Stable Image Ultra, Stable Diffusion 3.5 Large, Large Turbo, Medium and Flash, Stable Image Core, SDXL 1.0 from 0.9 credits, Stable Audio 3.0 and 2.5, and upscale, edit, control and 3D services. After the free credits, credits are bought at USD 1 per 100 credits. unverified: whether the free credits expire
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account on a username and password, or a Google account; the getting-started guide says creating the account with Google's social login grants the 25 free credits; no card is needed for the grant, and credits beyond it are bought on the billing dashboard; unverified: whether a phone number or a verification step is asked, and whether a username-and-password account also receives the grant
- interface: rest
- limits:
  - volume-quota (binding): 25 free credits per new account, one-time; 1 credit is USD 0.01, so the grant is USD 0.25 [1]
  - request-rate: 150 requests per 10 seconds per API key; exceeding it returns 429 followed by a timeout of 60 seconds [2]
- binding note: USD 0.25 of one-time credit is gone after a handful of calls, long before the 150 requests per 10 seconds rate limit matters
- interface detail: REST API authenticated with a bearer API key in the Authorization header; up to 10 active keys per account
- tooling: raw HTTP with an API key created on the platform dashboard
- composes with: 25 credits is a smoke test for a wrapper rather than a dataset: it proves an API key works end to end and nothing more. A batch of 100 Stable Diffusion 3.5 Flash images costs 250 credits, ten times the grant.
- reliability: the grant is tied to the Google social-login signup in the getting-started guide, while the pricing page and the key-lookup article say only that new accounts receive 25 free credits
- evidence note: the 25 credit grant, the credit price, the per-call credit costs and the rate limit are quoted from vendor pages; credit expiry, the card-free statement and the extra signup steps are unverified.
- evidence:
  - [1] 2026-11-03: 25 free credits to get started | capture: sha256:d085394b8395aba1023973fb336c093d03b75feb26f4c1f7dbc89592cbf7d99a | quote: > Get started with 25 free credits. Check your credit balance and purchase additional credits on your account page.
  - [1] 2026-11-03: 1 credit equals USD 0.01 | capture: sha256:d085394b8395aba1023973fb336c093d03b75feb26f4c1f7dbc89592cbf7d99a | quote: > Credit pricing for Stability AI API services, including Stable Image, Stable Audio, and 3D models. 1 credit equals $0.01.
  - [1] 2026-11-03: Stable Image Ultra costs 8 credits per call | capture: sha256:d085394b8395aba1023973fb336c093d03b75feb26f4c1f7dbc89592cbf7d99a | quote: | [Stable Image Ultra](https://docs.stability.ai/api-reference/generate/stable-image-ultra.md) | Flagship image service based on Stable Diffusion 3.5 Large, offering the highest quality and detail | 8 |
  - [1] 2026-11-03: Stable Diffusion 3.5 Flash costs 2.5 credits per call | capture: sha256:d085394b8395aba1023973fb336c093d03b75feb26f4c1f7dbc89592cbf7d99a | quote: | [Stable Diffusion 3.5 Flash](https://docs.stability.ai/api-reference/generate/stable-diffusion-35.md) | The distilled version of Stable Diffusion 3.5 Medium, for fast, high-quality images | 2.5 |
  - [1] 2026-11-03: Stable Audio 3.0 costs 8 credits for up to six minutes of audio | capture: sha256:d085394b8395aba1023973fb336c093d03b75feb26f4c1f7dbc89592cbf7d99a | quote: | [Stable Audio 3.0](https://docs.stability.ai/api-reference/stable-audio/text-to-audio.md) | Generate up to six minutes high-quality audio with coherent structure from text prompts or audio samples | 8 |
  - [3] 2026-11-03: the 25 free credits are granted when the account is created with Google's social login | capture: sha256:b2aba28738cbf61b8a87cd8e7883490986e4ae7371bc848c3b636aa733dc78f6 | quote: Google account. Creating your account with Google's social login will grant you `25` free [credits](#credits)!
  - [3] 2026-11-03: an account can be created with a username and password or a Google account | capture: sha256:b2aba28738cbf61b8a87cd8e7883490986e4ae7371bc848c3b636aa733dc78f6 | quote: First, you'll need to create an account with us.
  - [4] 2026-11-03: new accounts receive 25 free credits | capture: sha256:01cf19144b7e445cf25b80fbe7a6b1df6b11d0f6cad1986c44993969a710899f | quote: New accounts receive 25 free credits for initial testing and evaluation purposes.
  - [2] 2026-11-03: the API is limited to 150 requests per 10 seconds | capture: sha256:e48bf149223ff93c7b6b306d52cf3a0ac99c05b6cc5193745af81fd4faa1560f | quote: Stability AI's API has a rate limit of** 150 requests per 10 seconds.**
  - [2] 2026-11-03: exceeding the limit returns 429 and a 60 second timeout | capture: sha256:e48bf149223ff93c7b6b306d52cf3a0ac99c05b6cc5193745af81fd4faa1560f | quote: Exceeding this limit results in a 429 response, followed by a **timeout lasting 60 seconds. **To maximize efficiency and prevent timeouts, consider the following strategies.
  - [3] 2026-11-03: credits beyond the grant are bought at USD 1 per 100 credits | capture: sha256:b2aba28738cbf61b8a87cd8e7883490986e4ae7371bc848c3b636aa733dc78f6 | quote: a rate of \$1 USD per 100 credits.
  - [3] 2026-11-03: requests authenticate with the API key in the Authorization header | capture: sha256:b2aba28738cbf61b8a87cd8e7883490986e4ae7371bc848c3b636aa733dc78f6 | quote: API key in via the `Authorization` header.
  - [4] 2026-11-03: an account can hold up to 10 active API keys | capture: sha256:01cf19144b7e445cf25b80fbe7a6b1df6b11d0f6cad1986c44993969a710899f | quote: 3. Use the “+” icon to generate a new API key (you can have up to 10 active keys at a time).
- sources:
  - [1] https://platform.stability.ai/pricing
  - [2] https://kb.stability.ai/knowledge-base/api-key-rate-limit-information
  - [3] https://docs.stability.ai/getting-started.md
  - [4] https://kb.stability.ai/knowledge-base/where-can-i-find-my-api-key
