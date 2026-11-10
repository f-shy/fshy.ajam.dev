# AssemblyAI

> assemblyai.com | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/assemblyai/ | JSON https://fshy.ajam.dev/api/v1/entity/assemblyai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AssemblyAI (Compute)

- `compute/assemblyai` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://assemblyai.com/pricing
- free tier: '$50 in free credits at signup, no credit card required. Concurrency is capped (see above) until you upgrade.' At the Universal-2 pre-recorded rate of USD 0.15 an hour, 50 / 0.15 = 333 hours of transcription. At Universal-3.5 Pro (USD 0.21 an hour) the same credit is 238 hours. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card and no payment method: the FAQ states '$50 in free credits at signup, no credit card required', so no payment method is taken and no hold exists. The evidence does not say which identifier the signup form asks for, so whether an email alone or an email plus a phone is required is not stated; debit and prepaid acceptance are not…
- interface: rest
- limits:
  - request-rate (binding): the free tier caps streaming concurrency at '5 new streams per minute' against 100 for pay-as-you-go, so five live sessions a minute is the real wall on a free account, long before 50 dollars of credit is spent. [1]
- limits note: the free tier caps streaming concurrency at '5 new streams per minute' against 100 for pay-as-you-go, so five live sessions a minute is the real wall on a free account, long before 50 dollars of credit is spent.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free runner plus 333 hours of pre-recorded transcription is enough to transcribe a whole lecture or podcast archive once; pair it with a free object store from the storage lane for the audio, since the credit covers the API and nothing else. What breaks: the 5-stream streaming cap makes live capture useless, and a re-transcription after a model change spends the credit twice.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The page is an llms.txt-shaped 'Authoritative Reference' block dated 'Last updated: 2026-09-28' on the vendor's own pricing URL, so it is the vendor speaking and the rung is documented. The page also warns that 'Defaults can differ between free-tier and paid accounts' and that streaming bills session duration rather than audio duration, which is where a free credit disappears without producing output. Expiry of the USD 50 is not stated on the page; a 12-month read would have to come from the console.
- extras:
  - facets.class: credit-large-enough-for-real-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: '$50 in free credits at signup, no credit card required. Concurrency is capped (see above) until you upgrade', quoted from the FAQ 'What's the free tier?'
  - [1] 2026-10-22: 'Free-tier streaming concurrency: 5 new streams per minute. Pay-as-you-go streaming concurrency: 100 new streams per minute', quoted
  - [1] 2026-10-22: pre-recorded rates 'Universal-3.5 Pro ... $0.21/hr' and 'Universal-2 ... $0.15/hr', quoted; 'Pre-recorded is billed per hour of audio submitted'
  - [1] 2026-10-22: '$50 in free credits, no credit card required' restated in the Key Pricing Facts block, and 'EU region is the same price as US', quoted
- sources:
  - [1] https://assemblyai.com/pricing

## AssemblyAI (Inference)

- `inference/assemblyai` | trial-only | evidence documented | binding volume-quota | category speech-to-text, text-to-speech and LLM gateway API, one-time signup credit
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
- url https://assemblyai.com/pricing
- free tier: USD 50 in free credits at signup, no credit card required; one-time, not a monthly allowance. The credit is spent at the per-model rates: Universal-3.5 Pro pre-recorded USD 0.21 per hour, Universal-2 pre-recorded USD 0.15 per hour, Universal-3.6 Pro Realtime streaming USD 0.45 per hour, text-to-speech USD 15 per 1M characters. Free-tier streaming concurrency is 5 new streams per minute against 100 for pay-as-you-go. | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: models on the pricing page: speech-to-text universal-3-5-pro, universal-2, universal-3-6-pro (streaming), universal-streaming-english and universal-streaming-multilingual; text-to-speech AssemblyAI-TTS-1; an LLM gateway that lists OpenAI, Anthropic, Google and Qwen models at per-token rates. unverified: whether the signup credit also pays for the LLM gateway and the text-to-speech endpoint, because the page states the credit once and names no product scope; unverified: whether the credit expires
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no credit card at signup ('no credit card required'); the signup page offers Continue with Google or Continue with email behind a reCAPTCHA check; unverified: whether a phone number or an email confirmation step follows the form
- interface: rest
- limits:
  - volume-quota (binding): USD 50 in free credits at signup, one-time; the pre-recorded rate is USD 0.15 per hour on Universal-2 and USD 0.21 per hour on Universal-3.5 Pro [1]
  - request-rate: free-tier streaming concurrency is 5 new streams per minute against 100 new streams per minute on pay-as-you-go [1]
- binding note: the one-time USD 50 credit is the ceiling for batch work; the 5 new streams per minute cap is a second, separate wall for streaming
- interface detail: REST at https://api.assemblyai.com (upload, transcript submit and poll); streaming over WebSocket at wss://streaming.assemblyai.com/v3/ws; Python and TypeScript SDKs
- endpoint: https://api.assemblyai.com/v2/transcript
- tooling: Python and TypeScript SDKs, and raw HTTP and WebSocket calls with the API key from the dashboard; every model id is set in the speech_models field of the request
- composes with: the credit pays for batch transcription of recorded audio, which a free CI runner can post file by file; pair it with a free object store for the audio, since the credit covers the API and nothing else. The 5 new streams per minute cap makes live capture on the free tier a poor fit.
- reliability: streaming is billed on session duration, not audio duration, so an idle open connection spends credit; the default model can differ between free-tier and paid accounts, so speech_models should be set explicitly
- notes: the pricing page names a streaming v3 endpoint, wss://streaming.assemblyai.com/v3/ws, and states that the v2 realtime endpoint is inactive
- evidence note: the credit, the card-free signup, the rates and the free-tier streaming cap are quoted from the vendor pricing page; the credit's expiry and its scope over the LLM gateway and text-to-speech were not stated and are unverified.
- evidence:
  - [1] 2026-11-03: USD 50 in free credits at signup with no card | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: $50 in free credits at signup, no credit card required. Concurrency is capped (see above) until you upgrade.
  - [1] 2026-11-03: free-tier streaming is capped at 5 new streams per minute | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: Yes. Free tier: 5 new streams per minute. Pay-as-you-go: 100 new streams per minute. Higher concurrency available via enterprise contracts.
  - [1] 2026-11-03: Universal-3.5 Pro pre-recorded costs USD 0.21 per hour | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: | Universal-3.5 Pro | `universal-3-5-pro` | $0.21/hr |
  - [1] 2026-11-03: Universal-2 pre-recorded costs USD 0.15 per hour | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: | Universal-2 | `universal-2` | $0.15/hr |
  - [1] 2026-11-03: the streaming model universal-3-6-pro costs USD 0.45 per hour | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: | Universal-3.6 Pro Realtime | `universal-3-6-pro` | $0.45/hr base |
  - [1] 2026-11-03: text-to-speech is billed at USD 15 per 1M input characters | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: - Text-to-Speech API is billed on input characters: $15 per 1M characters.
  - [1] 2026-11-03: streaming runs on the v3 WebSocket endpoint and the v2 realtime endpoint is inactive | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: > Streaming endpoint: `wss://streaming.assemblyai.com/v3/ws`. The old v2 endpoint (`wss://api.assemblyai.com/v2/realtime/ws`) is inactive.
  - [1] 2026-11-03: streaming is billed on open-session time, idle time included | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: - Streaming is billed per session duration — the time the WebSocket connection is open, not the duration of audio sent. Idle connection time counts.
  - [1] 2026-11-03: the default model can differ between free-tier and paid accounts | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: - Default model selection may differ between free-tier and paid accounts. Always set `speech_models` (plural) explicitly to avoid surprises after upgrading.
  - [1] 2026-11-03: the LLM gateway is one endpoint on the same API key | capture: sha256:bf1da8421b0cdecf04b7d64676072599a15f2d94a10f3aaac7db7b10566820ea | quote: Endpoint: Single unified endpoint, authenticated with your existing AssemblyAI API key. 25+ models from 5 providers.
  - [2] 2026-11-03: the signup form takes an email address | capture: sha256:782ec8f6872422805f6c2b8c233876166bc256426751704b36c084593602e84b | quote: Continue with email
  - [2] 2026-11-03: the signup form sits behind a reCAPTCHA check | capture: sha256:782ec8f6872422805f6c2b8c233876166bc256426751704b36c084593602e84b | quote: Recaptcha requires verification.
  - [3] 2026-11-03: Python and TypeScript SDKs exist for transcription and streaming | capture: sha256:362e8414338322d940742bd730c98b728c835d5506dfc704d797972ba08e9ed8 | quote: Use the Python or TypeScript SDK to integrate transcription, streaming, and voice agents directly into your own codebase.
  - [4] 2026-11-03: the REST API base URL is https://api.assemblyai.com | capture: sha256:75c5ada878c8768b1ff7c9a689652657029430c28a152567c5b1b48566bbb80a | quote: > base_url = "https://api.assemblyai.com"
  - probe:https://api.assemblyai.com/v2/transcript 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:a30a776f0a8dca4cdf91535ff55ac6e73daeccf1de6fd73a96e4a6e9bfff4603 | quote: "status": 401
- sources:
  - [1] https://assemblyai.com/pricing
  - [2] https://www.assemblyai.com/dashboard/signup
  - [3] https://www.assemblyai.com/docs
  - [4] https://assemblyai.com/docs/pre-recorded-audio/getting-started/transcribe-an-audio-file.md
