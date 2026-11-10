# Cartesia

> cartesia.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cartesia/ | JSON https://fshy.ajam.dev/api/v1/entity/cartesia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cartesia (Compute)

- `compute/cartesia` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
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
- sources:
  - [1] https://cartesia.ai/pricing

## Cartesia (Free)

- `inference/cartesia` | qualifies-with-caveat | evidence documented | binding volume-quota | category text-to-speech and speech-to-text API, monthly free credit pool | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
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
- interface detail: REST (POST /tts/bytes and sibling TTS and STT routes) and WebSocket at api.cartesia.ai, versioned by a Cartesia-Version header; Python and JavaScript quickstarts
- endpoint: https://api.cartesia.ai
- tooling: raw HTTP and WebSocket with an API key (sk_car_...) from the playground, or the Python and JavaScript quickstarts
- composes with: the monthly pool covers the speech-to-text side of a demo better than the text-to-speech side, because 20K credits is about 1h 51m of Ink-2 transcription but only about 27 minutes of Sonic-3.6 speech; run it from a free CI job for small voice-over or transcription batches. Unlike a one-time credit it renews each month.
- reliability: a Free-plan request over the concurrency limit fails with 429 instead of queuing
- evidence note: the credit pool, the credit costs, the converted minutes and the concurrency table are quoted from vendor pages; rollover on Free and the card requirement at signup are unverified.
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
- sources:
  - [1] https://cartesia.ai/pricing
  - [2] https://docs.cartesia.ai/use-the-api/concurrency-limits-and-timeouts
  - [3] https://docs.cartesia.ai/build-with-cartesia/tts-models/latest
  - [4] https://docs.cartesia.ai/
  - [5] https://docs.cartesia.ai/api-reference/tts/bytes
  - [6] https://play.cartesia.ai/sign-up
