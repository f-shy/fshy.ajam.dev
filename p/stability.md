# Stability AI

> stability.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stability/ | JSON https://fshy.ajam.dev/api/v1/entity/stability.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stability AI (Compute)

- `compute/stability-ai` | trial-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:36.250Z (live) | stale on 2026-12-26
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
  - [1] 2026-11-25: the API gives 25 free credits on signup | capture: sha256:d085394b8395aba1023973fb336c093d03b75feb26f4c1f7dbc89592cbf7d99a | quote: Get started with 25 free credits.
- sources:
  - [1] https://platform.stability.ai/pricing

## Stability AI (Inference)

- `inference/stability-ai` | trial-only | evidence documented | binding volume-quota | category image, audio and 3D generation API, one-time signup credit
- needs card no, phone unknown, ID no, institution no | verified 2026-11-18T05:36:08.308Z (live) | stale on 2026-12-19
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
- interface detail: REST API authenticated with a bearer API key in the Authorization header; up to 10 active keys per account. Current routes are under /v2beta (for example POST /v2beta/stable-image/generate/core; also /v2beta/stable-image/generate/ultra, /v2beta/audio/stable-audio/text-to-audio, /v2beta/3d/stable-fast-3d and GET /v2beta/results/{id}); legacy GET /v1/user/balance. Generation and editing routes take multipart/form-data; result and account routes are GET.
- endpoint: https://api.stability.ai
- tooling: raw HTTP with an API key created on the platform dashboard; first-party OpenAPI 3.1 spec at https://api.stability.ai/v2alpha/openapi; docs at https://docs.stability.ai/api-reference. Example: curl https://api.stability.ai/v2beta/stable-image/generate/core -H "Authorization: Bearer $STABILITY_API_KEY" -F prompt="..." -o out.png
- composes with: 25 credits is a smoke test for a wrapper rather than a dataset: it proves an API key works end to end and nothing more. A batch of 100 Stable Diffusion 3.5 Flash images costs 250 credits, ten times the grant.
- reliability: the grant is tied to the Google social-login signup in the getting-started guide, while the pricing page and the key-lookup article say only that new accounts receive 25 free credits
- notes: endpoint filled from first-party API reference and OpenAPI spec on 2026-11-18; base URL https://api.stability.ai, current routes under /v2beta; docs https://docs.stability.ai/api-reference. The docs.stability.ai/openapi.json link was a login wall; the equivalent spec at api.stability.ai/v2alpha/openapi was used instead. On 2026-11-18 two keyless GETs to /v1/user/account returned HTTP 401, so the route exists and needs a key.
- evidence note: Endpoint, /v2beta prefix, POST/multipart method and bearer auth come from the first-party API reference and the machine-readable OpenAPI spec read on 2026-11-18; the host was probed live (401 with a fake key, 404 on keyless paths). Whether a free-account key completes a generation remains unverified: behind a sign-up.
- probe:
  - records[0].probe_id: stability-ai-20261118
  - records[0].target: https://api.stability.ai/v1/user/account
  - records[0].runs[0].label: run1
  - records[0].runs[0].probed_at: 2026-11-18T05:26:19.614Z
  - records[0].runs[0].status: 401
  - records[0].runs[0].completion: no
  - records[0].runs[0].capture: sha256:c12a77a120963c9a0c5ed96f8cab2e2f97757589519daf8140087dc112431d24
  - records[0].runs[1].label: run2
  - records[0].runs[1].probed_at: 2026-11-18T05:36:08.308Z
  - records[0].runs[1].status: 401
  - records[0].runs[1].completion: no
  - records[0].runs[1].capture: sha256:f1a5eb1dae0242cacef6ff5c9747c10e1352982ea5d98a30ae08a129ddb718eb
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
  - [5] 2026-11-18: the first-party API reference states the API base URL (under the heading "All requests go to:") | capture: sha256:d4b75eb4fc0c279355f806953c7edddd9c069863fe4f360adc46703d51f1c21f | quote: https://api.stability.ai
  - [6] 2026-11-18: the first-party OpenAPI spec names the production server | capture: sha256:26d52792b117c3c71d8fd26aff378f194c5f63367d8ffc0eb591e9ade4c85a18 | quote: "servers":[{"url":"https://api.stability.ai"}]
  - [5] 2026-11-18: the API reference states the v2beta path prefix and the POST method | capture: sha256:d4b75eb4fc0c279355f806953c7edddd9c069863fe4f360adc46703d51f1c21f | quote: Current endpoints live under `/v2beta`, for example `POST /v2beta/stable-image/generate/core`.
  - [5] 2026-11-18: the API reference states bearer-token auth in the Authorization header | capture: sha256:d4b75eb4fc0c279355f806953c7edddd9c069863fe4f360adc46703d51f1c21f | quote: Authenticate every request with your API key in the `Authorization` header, using the `Bearer` scheme:
  - [6] 2026-11-18: the first-party OpenAPI spec defines bearer auth in the Authorization header | capture: sha256:26d52792b117c3c71d8fd26aff378f194c5f63367d8ffc0eb591e9ade4c85a18 | quote: "STABILITY_API_KEY":{"type":"http","scheme":"bearer","description":"Your [Stability API key](https://platform.stability.ai/dashboard/api-keys), sent as a bearer token in the `Authorization` header."}
  - [7] 2026-11-18: a per-endpoint first-party page states the auth header and multipart body format (continued on the next line: `multipart/form-data`,) | capture: sha256:89d8e64934c94b93876eb8a2369334363bedec57390ae87b8fcd8de7bd52d322 | quote: The headers of the request must include an API key in the `authorization` field. The body of the request must be
  - [3] 2026-11-18: the first-party getting-started guide confirms the shared auth mechanism | capture: sha256:b2aba28738cbf61b8a87cd8e7883490986e4ae7371bc848c3b636aa733dc78f6 | quote: All APIs documented on this site use the same authentication mechanism: passing the API key in via the `Authorization` header.
  - probe:https://api.stability.ai/v1/user/account 2026-11-18: a keyless GET to https://api.stability.ai/v1/user/account returned HTTP 401 with body {'id':'053bae9592878554b7d2bd7439ac78ec','message':'missing authorization header','name':'unauthorized'} and no completion in 2595 ms Probe start 2026-11-18T05:26:19.614Z. | capture: sha256:c12a77a120963c9a0c5ed96f8cab2e2f97757589519daf8140087dc112431d24 | quote: a keyless GET to https://api.stability.ai/v1/user/account returned HTTP 401 with body {'id':'053bae9592878554b7d2bd7439ac78ec','message':'missing authorization header','name':'unauthorized'} and no completion in 2595 ms
  - probe:https://api.stability.ai/v1/user/account 2026-11-18: a keyless GET to https://api.stability.ai/v1/user/account returned HTTP 401 with body {'id':'1c59c6716ba45c8cbfd2d92ef96064e8','message':'missing authorization header','name':'unauthorized'} and no completion in 1164 ms Probe start 2026-11-18T05:36:08.308Z. | capture: sha256:f1a5eb1dae0242cacef6ff5c9747c10e1352982ea5d98a30ae08a129ddb718eb | quote: a keyless GET to https://api.stability.ai/v1/user/account returned HTTP 401 with body {'id':'1c59c6716ba45c8cbfd2d92ef96064e8','message':'missing authorization header','name':'unauthorized'} and no completion in 1164 ms
- sources:
  - [1] https://platform.stability.ai/pricing
  - [2] https://kb.stability.ai/knowledge-base/api-key-rate-limit-information
  - [3] https://docs.stability.ai/getting-started.md
  - [4] https://kb.stability.ai/knowledge-base/where-can-i-find-my-api-key
  - [5] https://docs.stability.ai/api-reference/index.md
  - [6] https://api.stability.ai/v2alpha/openapi
  - [7] https://docs.stability.ai/api-reference/generate/stable-image-core.md
