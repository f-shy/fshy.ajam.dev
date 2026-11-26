# evroc

> evroc.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/evroc/ | JSON https://fshy.ajam.dev/api/v1/entity/evroc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## evroc

- `compute/evroc` | paid-only | evidence documented | binding request-rate | category shared model inference API and dedicated GPU instances | tier Shared Models (per-token)
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:14.726Z (live) | stale on 2026-12-25
- url https://docs.evroc.com/products/think/concepts.html
- free tier: evroc's own documentation states Shared Models have 'no minimum spend' and bill 'per million tokens (input and output separately)'; some models also support cached input tokens at a reduced rate. The API is at https://models.think.evroc.com/v1 with 16 models listed by models.dev. No always-free token allowance is published on evroc's own pages. A separate GPU-VM campaign page advertises 'Get €500 free credits', with no terms for the Think API on that page. | unit: tokens | metered on: request-count | read on: 2026-11-24 | source: [1] | note: The 500-euro credit is on the GPU VM campaign page, not on the Think Models pricing documentation, and its eligibility is not stated there. Per-token figures for specific models are published by models.dev, a third-party catalogue; evroc's own pricing documentation states the billing shape but no per-model rate table was found on evroc's own pages.
- per-object cap: Not an object store: the unit is tokens through an OpenAI-compatible inference API. models.dev lists context windows from 448 tokens for Whisper models to 524,288 for GLM-5.2, and output limits from 448 to 262,144 tokens. | source: [2] | note: Dedicated Model Instances use instance sizes such as 1-b200-27c-240g; GPU VMs offer 1 to 8 GPUs per instance.
- retention: The shared inference API holds no user objects: a request is billed by tokens and no storage or retention period is stated. Dedicated Model Instances run continuously until the user deletes them. | source: [1] | note: No retention clause was read on the Think documentation pages.
- egress: No egress charge or allowance is stated on evroc's Think documentation or its cloud-services pages. The object-storage calculator on evroc's own site prices 1 GB of storage at EUR 0.02 per month and 0 GB downloaded monthly at EUR 0.00 outbound, but no Think API egress term is published. | metered: no | source: [1]
- identity: email | detail: evroc's sign-up page at https://signup.evroc.com/ renders only 'Get started with evroc', a log-in link and a link to speak to a Cloud Specialist; no fields were visible in the captured page. The user documentation says 'You create an API key, pick a model from the supported models list', so an account and a key are required before a request. Which registration fields the signup form asks for is unverified: behind an incomplete signup form.
- interface: rest, cli
- limits:
  - request-rate (binding): rate limits apply to Shared Models; HTTP 429 when too many requests and 503 under high load, with Retry-After; the exact thresholds are subject to change [3]
  - write-gated: the API is team-scoped and a key is required: an unauthenticated GET to https://models.think.evroc.com/v1/models answered 401 with 106 bytes on 2026-11-24 probe:https://models.think.evroc.com/v1/models
- limits note: evroc states the service is busiest 09-17h European time and recommends non-interactive work outside those hours. The exact request thresholds are not published.
- binding note: The shared endpoint's rate limit binds first because its thresholds are undisclosed and can change, and the service returns 429 or 503 under load; the per-token charge is a price, not a capacity ceiling.
- interface detail: OpenAI-compatible REST API at https://models.think.evroc.com/v1 with standard clients and LangChain; the evroc CLI manages model instances and API keys.
- endpoint: part of the free tier
- tooling: Standard OpenAI-compatible clients, LangChain and the evroc CLI; the models.dev package is @ai-sdk/openai-compatible.
- composes with: A shared model endpoint can be swapped in for another OpenAI-compatible backend with a configuration change, while dedicated GPU instances give predictable hourly cost for a pinned model.
- reliability: Shared Models are busiest 09-17h European time; the service answers 429 when rate limited and 503 with no server available under high load, with a Retry-After header. The exact thresholds are not published and may change.
- notes: Hosted inference service: evroc operates the GPUs and the user calls an API, so nothing is installed or maintained by the user. The Think Shared Models tier has no always-free token allowance on evroc's own pages; the 500-euro credit is a GPU VM campaign offer with unstated eligibility. A separate Dedicated Model Instances tier bills per GPU-hour and is not priced here. The signup form fields could not be read and are unverified.
- evidence note: The billing shape, no-minimum-spend statement, API endpoint, rate-limit statuses and busy hours are quoted from evroc's own documentation read 2026-11-24; the 500-euro credit is quoted from evroc's GPU VM campaign page. The 401 on the models endpoint is from a probe registered with --probe. Signup fields could not be read, and no per-model rate table was found on evroc's own pages, so those are left unverified.
- extras:
  - billing_model: per-million-token for Shared Models; per GPU-hour for Dedicated Model Instances
  - free_tier_kind: campaign-credit
  - price_note: evroc's own Think documentation states the shape (input/output per million tokens, cached input at a reduced rate) but no first-party per-model rate table was captured; models.dev reports third-party per-model rates such as $0.114 / $0.114 for multilingual E5.
  - signup_status: signup entry page captured; registration fields unverified
  - model_count: 16
- evidence:
  - [1] 2026-11-24: Shared Models need no instance, GPU or minimum spend and bill per million tokens with input and output priced separately | capture: sha256:a02120ba9d74c8e9334914d2f04302d9a9b4b68fb78bf2ef113b5d87aa505113 | quote: There's no instance to configure, no GPU to choose, and no minimum spend.
  - [1] 2026-11-24: shared inference is billed per million tokens with input and output separately; dedicated instances bill per GPU-hour | capture: sha256:a02120ba9d74c8e9334914d2f04302d9a9b4b68fb78bf2ef113b5d87aa505113 | quote: Billing | Per million tokens (input/output) | Per GPU-hour
  - [1] 2026-11-24: a shared-model request goes to https://models.think.evroc.com/v1 after an API key is created | capture: sha256:a02120ba9d74c8e9334914d2f04302d9a9b4b68fb78bf2ef113b5d87aa505113 | quote: Shared Models are managed by evroc. You call an OpenAI-compatible API endpoint and pay only for the tokens you use.
  - [1] 2026-11-24: rate limiting policies apply to the shared resource | capture: sha256:a02120ba9d74c8e9334914d2f04302d9a9b4b68fb78bf2ef113b5d87aa505113 | quote: To ensure fair access to a shared resource, rate limiting policies apply
  - [3] 2026-11-24: the exact rate-limit thresholds are not published and may change | capture: sha256:1eb80205ad3b92c139f6c29798c79f865ce07934db4bba12e6711514f6d6de3a | quote: The exact thresholds used for rate limiting are subject to change as necessary to maintain service availability.
  - [4] 2026-11-24: evroc advertises 500 euros of free credits for a first NVIDIA B200 GPU VM on its GPU VM campaign page | capture: sha256:7a5a031f1e680300a1c1e8b1cc8197003de29d99729f5ed858b38a83166bb0b4 | quote: Claim your €500 free credits and launch your first NVIDIA B200 GPU VM today.
  - [5] 2026-11-24: GPU VM compute is pay-as-you-go and billed hourly for what is used | capture: sha256:892c33b1adfb51ad07de587fa6558554b710d1a9e7c3b3e6948e7787ccf4f1c6 | quote: Pay-as-you-go pricing Predictable hourly costs, billed only for what you use.
  - [2] 2026-11-24: the evroc provider exposes 16 models through the OpenAI-compatible base https://models.think.evroc.com/v1 | capture: sha256:99bd06271afb56449d5714b83a5a363a73f50fa3bdaf272c8eef85c6b574239b | quote: https://models.think.evroc.com/v1
  - [2] 2026-11-24: models.dev lists per-million-token input and output prices for evroc models, for example 0.114 dollars each way for the multilingual E5 embeddings model | capture: sha256:99bd06271afb56449d5714b83a5a363a73f50fa3bdaf272c8eef85c6b574239b | quote: $0.114 / $0.114
  - probe:https://models.think.evroc.com/v1/models 2026-11-24: an unauthenticated read of the model list is refused with 401, so an API key gates the endpoint | capture: sha256:96121de64cc3d24712c6edc035e690a9243ece24900aafef6eb9c17020933bb9 | quote: "status": 401
  - [6] 2026-11-24: the captured signup entry page offers only a log-in link and a Cloud Specialist link, with no registration fields visible | capture: sha256:b4afff101bf258c252106c1640b9d38a7f5550383f5656238f4583421ea9d027 | quote: # Get started with evroc
- sources:
  - [1] https://docs.evroc.com/products/think/concepts.html
  - [2] https://models.dev/providers/evroc
  - [3] https://docs.evroc.com/products/think/rate-limiting.html
  - [4] https://web.archive.org/web/2026/https://evroc.com/campaigns/gpu-vm/
  - [5] https://evroc.com/campaigns/gpu-vm/
  - [6] https://signup.evroc.com/
