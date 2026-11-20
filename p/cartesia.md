# Cartesia

> cartesia.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cartesia/ | JSON https://fshy.ajam.dev/api/v1/entity/cartesia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cartesia (Compute)

- `compute/cartesia` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T04:58:13.795Z (live) | stale on 2026-12-19
- url https://cartesia.ai/pricing
- free tier: Free plan at USD 0 with '20K credits / month' plus '$1 prepaid agents / month'. The plan table converts that for you: Sonic-3.6 text to speech gets '~27' minutes a month at '2' concurrent requests, Ink-2 speech to text gets '~1h 51m' a month at '8' concurrent requests, and managed agents get 17 minutes at USD 0.06 a minute. The FAQ gives the unit: 'Sonic text-to-speech: One minute of audio generation requires 750-800 credits. 1 credit equals 1 character' and 'Ink speech-to-text: 3 credits equals 1 second of audio'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-monthly-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 27 minutes of generated speech a month, then the pool is empty; the 2-request TTS concurrency ceiling means a batch of short clips still cannot be pushed in one afternoon without queueing, but the volume runs out first. [1]
- limits note: 27 minutes of generated speech a month, then the pool is empty; the 2-request TTS concurrency ceiling means a batch of short clips still cannot be pushed in one afternoon without queueing, but the volume runs out first.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free plan here covers the STT side of a demo better than the TTS side, because 20,000 credits at 3 credits a second is 1h51m of transcription while the same pool is only 27 minutes of speech. What breaks: any repeated synthesis, since 27 minutes a month does not accumulate and the plan is monthly rather than annual.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The vendor converts credits to minutes on the page, so the figure is theirs. Rollover exists but caps at 2x the monthly rate, which on a 20,000-credit pool adds at most 27 more minutes of speech. Not established: whether a card is demanded at signup; The 17 free agent minutes carry a phone-number line item at USD 0.014 a minute for Cartesia-provisioned numbers, which the free allocation does not cover if a number is requested.
- extras:
  - facets.class: credit-too-small-for-a-workload
  - facets.free_tier_kind: recurring-monthly-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the plan block prints '$0 /mo ... 20K credits / month ... $1 prepaid agents / month' for the Free plan, quoted
  - [1] 2026-10-22: the comparison table prints 'Sonic-3.6 Minutes included monthly ~27' with 'Concurrent requests 2', and 'Ink-2 Hours included monthly ~1h 51m' with 'Concurrent requests 8', quoted
  - [1] 2026-10-22: 'One minute of audio generation requires 750-800 credits. 1 credit equals 1 character' and 'Ink speech-to-text: 3 credits equals 1 second of audio', quoted
  - [1] 2026-10-22: 'Free Plan - 17 minutes' of agent calls at '$0.06 per minute', quoted from 'How many voice agent minutes do I get per plan?'
  - [1] 2026-11-18: not stated | capture: sha256:35f8674e86c69f5fcc3a40076d32d8649ebd3077a4a1e6b564df9cb1d88b577f | quote: # Pricing for every stage.
- sources:
  - [1] https://cartesia.ai/pricing

## Cartesia (Free)

- `inference/cartesia` | qualifies-with-caveat | evidence documented | binding volume-quota | category text-to-speech and speech-to-text API, monthly free credit pool | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-18T04:36:12.034Z (live) | stale on 2026-12-19
- url https://cartesia.ai/pricing
- free tier: Free plan at USD 0 a month with 20K credits per month plus USD 1 of prepaid voice-agent usage per month. The credits are spent on text-to-speech at 1 credit per character (about 750 to 800 credits per minute of audio, which the plan table puts at about 27 minutes of Sonic-3.6 a month) or on speech-to-text at 3 credits per second of audio (about 1h 51m of Ink-2 a month); the USD 1 of agent usage is about 33 minutes at USD 0.03 a minute, before telephony and language-model usage. | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: models: text-to-speech sonic-3.6 (44 languages; sonic-3.5 and sonic-3 also accepted by the API) and speech-to-text Ink-2; managed voice agents. unverified: whether unused Free credits roll over, because the pricing page describes rollover only in terms of paid plans
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the signup form asks for a first name, last name, email address and password, or a GitHub or Google account; the pricing page names no card for the Free plan and the signup form shows none; unverified: whether a phone number, a card or a verification step is asked after the form
- interface: rest
- limits:
  - volume-quota (binding): 20K credits per month on the Free plan, shared by text-to-speech and speech-to-text, plus USD 1 per month of prepaid voice-agent usage; with overages off, new requests are blocked once the credits run out [1]
  - request-rate: Free plan concurrency: 2 concurrent text-to-speech requests and 8 concurrent speech-to-text requests; on Free plans a request over the limit returns 429 immediately, where paid plans queue it [2]
- binding note: about 27 minutes of Sonic-3.6 speech or about 1h 51m of Ink-2 transcription per month runs out before the concurrency caps matter
- interface detail: REST (POST /tts/bytes, /tts/sse, /stt and sibling TTS/STT routes; GET /models and GET /v1/agents/models) and WebSockets at api.cartesia.ai, versioned by a Cartesia-Version header; Python and JavaScript quickstarts. No chat/completions or text-completion route is documented in any API version; LLM text generation is available only inside a Managed Agent over wss://api.cartesia.ai/v1/agents/websocket/{agent_id}.
- endpoint: https://api.cartesia.ai
- tooling: raw HTTP and WebSocket with an API key (sk_car_...) from the playground, or the Python and JavaScript quickstarts; the OpenAI SDK is not used against Cartesia; there is no OpenAI-compatible chat endpoint. An OpenAI-compatible shim exists for STT only (POST /audio/transcriptions).
- composes with: the monthly pool covers the speech-to-text side of a demo better than the text-to-speech side, because 20K credits is about 1h 51m of Ink-2 transcription but only about 27 minutes of Sonic-3.6 speech; run it from a free CI job for small voice-over or transcription batches. Unlike a one-time credit it renews each month.
- reliability: a Free-plan request over the concurrency limit fails with 429 instead of queuing
- notes: Completion-route check (2026-11-18): no chat/completions or text-completion route exists on api.cartesia.ai in any of the four documented API versions; the base URL's 405 is expected (allow: GET, a status root). Queue q02 asserted the 405 on 2026-11-09; the existing probe evidence row is dated 2026-11-10; both are recorded claims, and the 405 was reproduced on 2026-11-18.
- evidence note: the credit pool, the credit costs, the converted minutes and the concurrency table are quoted from vendor pages; rollover on Free and the card requirement at signup are unverified. absence of a completion route established from the first-party complete API index (219 pages across four versions) and the full docs dump (zero occurrences of chat/completions and /v1/completions); base-URL 405 and allow: GET reproduced on 2026-11-18. The auth-gated latest.yml spec link returned a login page and was not used as evidence.
- evidence:
  - [1] 2026-11-03: the Free plan includes 20K credits a month | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: 20K credits / month
  - [1] 2026-11-03: Free includes USD 1 of voice-agent usage a month | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: For example, Scale costs $299/month and includes 8M credits plus $299 for voice agents. Free includes $1 for voice agents.
  - [1] 2026-11-03: text-to-speech costs 1 credit per character, about 750 to 800 credits per minute | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: - Sonic text-to-speech: 1 credit per character, about 750 to 800 credits per minute of audio.
  - [1] 2026-11-03: speech-to-text costs 3 credits per second of audio | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: - Ink speech-to-text: 3 credits per second of audio, or $0.39 per hour on the Scale plan.
  - [1] 2026-11-03: the plan table converts the Free speech-to-text allowance to about 1h 51m a month | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: ~1h 51m
  - [1] 2026-11-03: the Free agent allowance is about 33 minutes at the standard rate | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: - Free: 33 minutes
  - [1] 2026-11-03: overages are a paid-plan feature and requests are blocked at zero credits when they are off | capture: sha256:3651cdb5d76b3186f8f9cf9b47b3b3d04a95ebc99129cf4e8d0a583c7095596f | quote: With overages off, new requests are blocked once your credits run out.
  - [2] 2026-11-03: Free plan concurrency is 2 text-to-speech and 8 speech-to-text requests | capture: sha256:c8850547c0e57065cb6ea72a45a156f8023a8c25d1b9598d89918dee94b356af | quote: | Free | 2 | 8 |
  - [2] 2026-11-03: Free plans fail immediately with 429 over the concurrency limit | capture: sha256:c8850547c0e57065cb6ea72a45a156f8023a8c25d1b9598d89918dee94b356af | quote: * Free plans return a `429 Too Many Requests` error immediately.
  - [3] 2026-11-03: sonic-3.6 is the current text-to-speech model with 44 languages | capture: sha256:d3bc20ec15128ff9685559f345a73437c4c4a735a7f7ec505bb5999da38848c2 | quote: Sonic 3.6 (`sonic-3.6`) is our fastest, most natural text-to-speech model, with native support for 44 languages.
  - [4] 2026-11-03: Ink 2 is the speech-to-text model | capture: sha256:2e20f6eb643c12f4ea419e86a89663bb8ab9978fb139c6755a3d734b7937b739 | quote: > Transcribe in real time with Ink 2, with turn detection built in.
  - [4] 2026-11-03: the playground issues an API key | capture: sha256:2e20f6eb643c12f4ea419e86a89663bb8ab9978fb139c6755a3d734b7937b739 | quote: > Try every model in the browser and grab an API key.
  - [5] 2026-11-03: the production API host is api.cartesia.ai | capture: sha256:34132673714776710e65295d7ceb8d82c8e0abec85dc81861a4df2504e75766e | quote: - url: https://api.cartesia.ai
  - [6] 2026-11-03: the signup form asks for an email address | capture: sha256:df263991f58a0928aa4b6c54fd7281007fcfaae17ee9242930b1f09d726341bf | quote: Email address
  - probe:https://api.cartesia.ai 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 405 at the recorded base URL, so the endpoint is not a completion route | capture: sha256:05003e87c022e936f40c68ddd63513507eb854d3b61ac539e41a47e1dd8cb2c2 | quote: "status": 405
  - [7] 2026-11-18: the complete API index across four API versions lists TTS and STT routes and no chat/completions or text-completion route | capture: sha256:16f055d6adfff382bb37aaec073357109b17b07fb79d44a7275c71d99b6b4bab | quote: #### TTS - [Text-to-Speech (Bytes)](https://docs.cartesia.ai/api-reference/tts/bytes.md): Stream audio from a complete transcript ... #### STT - [Realtime Speech-to-Text (Auto)](https://docs.cartesia.ai/api-reference/stt/turns/websocket.md): Realtime speech transcription with built-in turn detection
  - [8] 2026-11-18: the full docs text dump has zero occurrences of chat/completions and /v1/completions; every 'completion' is ordinary prose, so no completion route is documented | capture: sha256:f09bdc3238827742116357b3751b7aed173e8d7ab3102377037500e29750d7dc | quote: 3. Signal completion with `no_more_inputs`, which sends `continue: false` to tell the model no more text is coming.
  - [9] 2026-11-18: the production host is api.cartesia.ai and the speech-generation method is POST /tts/bytes | capture: sha256:34132673714776710e65295d7ceb8d82c8e0abec85dc81861a4df2504e75766e | quote: ````yaml latest.yml POST /tts/bytes openapi: 3.0.1 info: title: Cartesia API version: 0.0.1 servers: - url: https://api.cartesia.ai description: Production security: [] paths: /tts/bytes: post: tags: - Tts summary: Text-to-Speech (Bytes) description: Stream audio from a complete transcript operationId: tts_bytes
  - [10] 2026-11-18: base URL is https://api.cartesia.ai; the same page states Bearer API-key auth and the required Cartesia-Version header in the Findings quotes above | capture: sha256:0b5fa88229e5657ce3980df0f9139226f7bdcd451abd0a5d093126c8ff93c304 | quote: All API requests use the following base URL: `https://api.cartesia.ai`. (For WebSockets the corresponding protocol is `wss://`.)
  - [11] 2026-11-18: LLM models are exposed only for Managed Agents via GET /v1/agents/models, not through a standalone chat/completions route | capture: sha256:52349a8623f5f89063d6ad10047636de53732f2655eca015bd939de6ee3ce718 | quote: Cartesia manages the model integration, so you do not need a provider account or API key. The catalog includes models from OpenAI, Anthropic and Google Gemini.
  - [12] 2026-11-18: a bare GET at the recorded base URL returns a version/status root (HEAD returned HTTP/2 405 with allow: GET), confirming it is not a completion route | capture: sha256:17cd11224d87491c780a4f87aa02fe3653c6eedd46d7992edad68b050e8c09b3 | quote: {"ok":true,"version":"2026-08-14"}
- sources:
  - [1] https://cartesia.ai/pricing
  - [2] https://docs.cartesia.ai/use-the-api/concurrency-limits-and-timeouts
  - [3] https://docs.cartesia.ai/build-with-cartesia/tts-models/latest
  - [4] https://docs.cartesia.ai/
  - [5] https://docs.cartesia.ai/api-reference/tts/bytes
  - [6] https://play.cartesia.ai/sign-up
  - [7] https://docs.cartesia.ai/_llms/en/api.txt
  - [8] https://docs.cartesia.ai/llms-full.txt
  - [9] https://docs.cartesia.ai/api-reference/tts/bytes.md
  - [10] https://docs.cartesia.ai/use-the-api/api-conventions.md
  - [11] https://docs.cartesia.ai/agents/models.md
  - [12] https://api.cartesia.ai
