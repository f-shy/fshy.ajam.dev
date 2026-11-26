# Rev AI

> rev.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rev/ | JSON https://fshy.ajam.dev/api/v1/entity/rev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rev AI

- `compute/rev-ai` | trial-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:52.255Z (live) | stale on 2026-12-05
- url https://www.rev.ai/pricing
- free tier: Pay-as-you-go with 'Free credits equivalent to 5 hours of Reverb ASR (free credits can be used for all products)'. Reverb Transcription is USD 0.20 an hour, so the grant is USD 1.00 of usage: 5 hours of Reverb English, or 200 minutes of Whisper Large at USD 0.005 a minute, or 333 minutes of Forced Alignment at USD 0.003 a minute. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): USD 1.00 of credit is the whole allowance: five hours of the cheapest English model, or three hours twenty minutes if the work needs Whisper Large, and nothing renews. [1]
- limits note: USD 1.00 of credit is the whole allowance: five hours of the cheapest English model, or three hours twenty minutes if the work needs Whisper Large, and nothing renews.
- binding note: the same as limits note
- interface detail: HTTP API with reference documentation at docs.rev.ai/api, and official Java, Node and Python SDKs listed at docs.rev.ai/sdk
- tooling: official Java, Node and Python SDKs (docs.rev.ai/sdk); the page names no CLI
- composes with: Five hours of Reverb provides audio transcription allowance with a 15-second minimum per audio clip. The grant is denominated in hours for a single model and does not transfer to alternative models.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The direct read of rev.ai/pricing returned a JavaScript shell with no price text; the quotes above come from the search index rendering of the same vendor URL on the same day, which is the vendor's text but retrieved indirectly. A third-party review (aiappstacker.com) reported the same 5-hour grant, corroborating it. Not established: whether a card is demanded at signup.
- extras:
  - facets.class: credit-too-small-for-a-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Free credits equivalent to 5 hours of Reverb ASR (free credits can be used for all products)', quoted from the pay-as-you-go block
  - [1] 2026-10-22: 'Reverb Transcription $0.20 per hour', 'Whisper Large Transcription $0.005 per minute', 'Forced Alignment $0.003 per minute', all 'Rounded up to the nearest second, 15 second minimum', quoted
  - [2] 2026-11-03: Rev AI documents an HTTP API with SDKs | capture: sha256:33bdd869978b3befe5859ee0e94364d40f38ab0a9dd25274ef8024cd23637ce3 | quote: Learn how to transcribe audio using Python and the Rev AI API.
  - [3] 2026-11-04: Rev AI lists official Java, Node and Python SDKs | capture: sha256:6774c86eaee1a51e881acb178f0234e241bad6bf094f48bf8e270d64ab80cb60 | quote: [Java SDK](https://docs.rev.ai/sdk/java)
  - [2] 2026-11-04: Rev AI documents an API reference | capture: sha256:192c231b259dd18a7097190345e98afce348748e1fe29f38f0b8f4c88bceb2ee | quote: Access detailed API reference documentation.
- sources:
  - [1] https://www.rev.ai/pricing
  - [2] https://docs.rev.ai/
  - [3] https://docs.rev.ai/sdk
