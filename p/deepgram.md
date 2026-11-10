# Deepgram

> deepgram.com | Compute, Inference; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deepgram/ | JSON https://fshy.ajam.dev/api/v1/entity/deepgram.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Deepgram (Compute)

- `compute/deepgram` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-23T07:52:00.000Z (live) | stale on 2026-11-23
- url https://deepgram.com/pricing
- free tier: 'Free $200 Credit' with 'No minimums. No expiration. No credit card required.' on the pricing page; the terms state 'Credits expire upon the closing or termination of your Account or cancellation or termination of your subscription to the Subscription Services.' | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no credit card required at signup, per the pricing page; the signup console is JavaScript-only and was not exercised
- interface: rest
- limits:
  - request-rate (binding): concurrency binds before the money runs out: on Pay As You Go speech-to-text is 'Up to 50 for the REST API' and 'Up to 150 for the WSS API', text-to-speech 'Up to 45', and audio intelligence 'Up to 10', so a parallel batch of hundreds of files waits on connection slots while 200 dollars of credit sits unspent. [1]
- limits note: concurrency binds before the money runs out: on Pay As You Go speech-to-text is 'Up to 50 for the REST API' and 'Up to 150 for the WSS API', text-to-speech 'Up to 45', and audio intelligence 'Up to 10', so a parallel batch of hundreds of files waits on connection slots while 200 dollars of credit sits unspent.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 200 of credit composes with CI runners: build jobs fetch audio and post to the REST endpoint up to the 50-connection concurrency ceiling.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The vendor contradicts itself on expiry: the pricing FAQ says the credit is 'available until you use it up' and contrasts it with free tiers that 'expire after 12 months', while the managing-projects documentation says promotional credits expire one year from signup. A third-party deal page reports both readings and advises planning for 12 months (grabaicredits.com, 2026, reported). Treat the 12-month reading as the safe one; the console balance is the only authority for a given account. The 'over 700 hours' figure is the vendor's, and 775 hours is a division at the pre-recorded Nova-3 rate. Re-read on 2026-10-23: the pricing page states no expiration and the terms end the balance at account closure, so the 12-month caution above remains the safe reading.
- extras:
  - facets.class: credit-large-enough-for-real-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Every new account receives $200 in free credit, which is equivalent to approximately 43,000 minutes (over 700 hours) of transcription using our Nova model', quoted from the pricing FAQ
  - [1] 2026-10-22: the Pay As You Go plan block prints 'No minimums. No expiration.' and 'No credit card required', quoted
  - [1] 2026-10-22: Nova-3 Monolingual pre-recorded listed at '$0.0043/min' and Nova-3 Multilingual at '$0.0052/min' on the pay-as-you-go column, quoted
  - [1] 2026-10-22: concurrency table: 'Speech-to-Text Up to 50 for the REST API, Up to 150 for the WSS API' and 'Audio Intelligence Up to 10 for the REST API', quoted
  - [2] 2026-10-23: 'Credits expire upon the closing or termination of your Account or cancellation or termination of your subscription to the Subscription Services.', quoted; the pricing page states 'No minimums. No expiration. No credit card required.'
- sources:
  - [1] https://deepgram.com/pricing
  - [2] https://deepgram.com/terms

## Deepgram (Inference)

- `inference/deepgram` | trial-only | evidence documented | binding volume-quota | category speech-to-text, text-to-speech and voice-agent API, one-time signup credit
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
- url https://deepgram.com/pricing
- free tier: Free USD 200 credit on the Pay as you go plan with no minimums, no expiration and no credit card required; the vendor puts it at roughly 43,000 minutes, over 700 hours, of Nova-3 transcription. One-time, not a monthly allowance. Rates drawn from it: Nova-3 monolingual pre-recorded USD 0.0043 per minute, Aura-2 text-to-speech USD 0.030 per 1k characters, Voice Agent Standard USD 0.075 per minute. | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: models on the pricing page: speech-to-text Flux STT and Nova-3 (plus Whisper Large pre-recorded), text-to-speech Flux TTS, Aura-2 and Aura-1, and a Voice Agent API that bundles speech-to-text, a managed language model and text-to-speech at one per-minute rate
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no credit card ('No credit card needed'); the signup page offers Google, GitHub, Azure or an email address with a password; unverified: whether a phone number or an email confirmation step follows the form
- interface: rest
- limits:
  - volume-quota (binding): USD 200 free credit, one-time, with no expiration stated on the pricing page; the terms state that credits expire upon the closing or termination of the account, and that once the initial credits are used a Pay As You Go account must enroll in auto-load or buy… [1]
  - request-rate: Pay as you go allows 150 concurrent streaming speech-to-text connections and 45 concurrent Voice Agent connections; limits apply per project, and a secondary project on a self-serve account is limited to a single concurrent stream [2]
- binding note: the one-time USD 200 credit is the ceiling; the per-project concurrency caps bind only for streaming and voice-agent loads
- interface detail: REST and WebSocket at api.deepgram.com (North America), with regional hosts api.eu.deepgram.com, api.au.deepgram.com and api.in.deepgram.com
- endpoint: https://api.deepgram.com
- tooling: raw HTTP and WebSocket calls with an API key created in the console
- composes with: the credit pays for batch transcription of recorded audio, which a free CI runner can post file by file, and for text-to-speech; pair it with a free object store for the audio. Streaming and voice-agent loads hit the per-project concurrency caps before the credit is spent.
- reliability: after the initial credit is used, requests need purchased credits or auto-load; the credit is tied to the account and expires if the account is closed
- notes: the pricing page says the credit does not expire while the terms say credits expire on account closure or termination; both are quoted in the evidence
- evidence note: the credit, the card-free signup, the no-expiry statement, the rates and the concurrency caps are quoted from the vendor pricing, signup, terms and rate-limit pages; the signup steps after the form are unverified.
- evidence:
  - [1] 2026-11-03: USD 200 credit, about 43,000 minutes of Nova-3, no expiry stated, no card | capture: sha256:15043fff5a513af5b08add9dbe83bb0ed2a8b31609c71aae401c8a2e1a384114 | quote: Roughly 43,000 minutes, over 700 hours, of Nova-3 transcription. It does not expire, so you can prototype without a clock running. No credit card is required to start.
  - [1] 2026-11-03: the free credit is USD 200 on the Pay as you go plan | capture: sha256:15043fff5a513af5b08add9dbe83bb0ed2a8b31609c71aae401c8a2e1a384114 | quote: Free $200 credit then pay-as-you-go
  - [1] 2026-11-03: Nova-3 pre-recorded costs USD 0.0043 per minute on Pay as you go | capture: sha256:15043fff5a513af5b08add9dbe83bb0ed2a8b31609c71aae401c8a2e1a384114 | quote: | Nova-3 Monolingual | $0.0043 / min | $0.0036 / min | - |
  - [1] 2026-11-03: Aura-2 text-to-speech costs USD 0.030 per 1k characters on Pay as you go | capture: sha256:15043fff5a513af5b08add9dbe83bb0ed2a8b31609c71aae401c8a2e1a384114 | quote: | Aura-2 | $0.030 /1k characters | $0.027 /1k characters | - |
  - [1] 2026-11-03: Voice Agent Standard costs USD 0.075 per minute on Pay as you go | capture: sha256:15043fff5a513af5b08add9dbe83bb0ed2a8b31609c71aae401c8a2e1a384114 | quote: | Standard | $0.075 / min | $0.068 / min | - |
  - [1] 2026-11-03: Pay as you go allows 150 concurrent streaming speech-to-text connections | capture: sha256:15043fff5a513af5b08add9dbe83bb0ed2a8b31609c71aae401c8a2e1a384114 | quote: Requests beyond your limit are queued or rejected. Pay as you go allows 150 concurrent streaming speech-to-text connections and Growth 225; Enterprise limits are set to your peak traffic.
  - [2] 2026-11-03: rate limits are counted per project, not per account or key | capture: sha256:37de9b85346b2e949f9d2d12d48b99103a00457516f28c69e025238d14674d62 | quote: Rate limits apply per project, not per account or API key.
  - [2] 2026-11-03: a secondary project on a self-serve account gets one concurrent stream | capture: sha256:37de9b85346b2e949f9d2d12d48b99103a00457516f28c69e025238d14674d62 | quote: Secondary projects created on a self-serve account are limited to a single concurrent stream by design.
  - [2] 2026-11-03: the Voice Agent API allows 45 concurrent connections on Pay as you go | capture: sha256:37de9b85346b2e949f9d2d12d48b99103a00457516f28c69e025238d14674d62 | quote: | [Voice Agent API](/reference/voice-agent/voice-agent) | Up to 45 concurrent connections | Up to 45 concurrent connections | Up to 45 concurrent connections | Up to 45 concurrent connections |
  - [2] 2026-11-03: the North America API host is api.deepgram.com | capture: sha256:37de9b85346b2e949f9d2d12d48b99103a00457516f28c69e025238d14674d62 | quote: > * North America: `api.deepgram.com`
  - [3] 2026-11-03: the signup page promises USD 200 credit with no card | capture: sha256:6f8a84684c992fd7d4171374e8c2eb0a459f55a42cfa4d392923725822d42258 | quote: Get $200 in credit absolutely free. That's enough to run a standard voice agent for more than 40 hours. No credit card needed.
  - [3] 2026-11-03: the signup form takes an email address | capture: sha256:68a1040600bdfa3d898800eb2a95321035c4c0acbd81a3f6b716b1d750c03608 | quote: Email address
  - [4] 2026-11-03: credits expire when the account is closed or terminated | capture: sha256:ba56073ff7df99797ccac4f1811ecf7f408ea05d88c9aec3b46f7e37799692ea | quote: Credits expire upon the closing or termination of your Account or cancellation or termination of your subscription to the Subscription Services.
  - [4] 2026-11-03: a Pay As You Go account needs auto-load or purchased credits once the initial credits are used | capture: sha256:ba56073ff7df99797ccac4f1811ecf7f408ea05d88c9aec3b46f7e37799692ea | quote: If you are on a Pay As You Go plan, once your initial Credits are used, you must be enrolled in auto-load or purchase additional Credits to continue using the Services.
  - probe:https://api.deepgram.com 2026-11-10: a POST to the bare host https://api.deepgram.com, with no path and no key, answered HTTP 404 with an empty body; no API route was requested, so the route was not tested | capture: sha256:ccdf064ead2fead1bd728c6de34c8dd6fdc8bdf7afcaecf3c112a3e72f1e1f03 | quote: "status": 404
- sources:
  - [1] https://deepgram.com/pricing
  - [2] https://developers.deepgram.com/reference/api-rate-limits.md
  - [3] https://console.deepgram.com/signup
  - [4] https://deepgram.com/terms

## Deepgram Startup Program

- `compute/deepgram-startup-program` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://deepgram.com/startup-program
- free tier: 'Apply to Deepgram for Startups and get up to $100,000 in credits over 12 months', with applicants required to be 'An AI builder or early-stage startup', 'In production or looking to launch in the next 6 months', and 'Committed to actively building and engaging with our community'. The programme terms add that participation is 'subject to our approval and ongoing eligibility, which we determine in our sole discretion', that applicants must give 'information about your company's funding, product, and team', and that promotional credits 'Expire 12 months from the issue date' and 'Can only be used after you've used up Deepgram's standard signup credits'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: application-gated-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: institution: the applicant must be 'An AI builder or early-stage startup' in production or launching within 6 months, and the application asks for 'information about your company's funding, product, and team', with participation 'subject to our approval and ongoing eligibility'. No card, hold, phone number or ID document is stated in any evidence row: unknown. The reachable substitute is the standard signup credit noted in this record, whose own signup requirement is not in the evidence.
- interface: unknown
- limits:
  - write-gated (binding): a company and a funding story are the entry ticket: the application asks for 'your company's funding, product, and team', the award is discretionary, and the amount is 'up to' USD 100,000 rather than a published figure, so a person with an email address reaches only the standard USD 200 signup credit. [1]
- limits note: a company and a funding story are the entry ticket: the application asks for 'your company's funding, product, and team', the award is discretionary, and the amount is 'up to' USD 100,000 rather than a published figure, so a person with an email address reaches only the standard USD 200 signup credit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: if awarded, USD 100,000 at the Nova-3 pre-recorded rate of USD 0.0043 a minute is about 23 million minutes, which is 388,000 hours of transcription, and no single workload comes close; the standard USD 200 credit recorded separately among evaluated providers is the reachable substitute.
- reliability: no reliability event recorded
- notes: The startup program provides additional credits beyond the standard USD 200 sign-up grant, requiring initial credits to be utilized first.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: application-gated-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Apply to Deepgram for Startups and get up to $100,000 in credits over 12 months', quoted; and the three applicant criteria listed verbatim
  - [2] 2026-10-22: 'Your participation in the Program is subject to our approval and ongoing eligibility, which we determine in our sole discretion' and 'You agree to provide complete and accurate information about your application, including information about your company's funding, product, and team', quoted from the terms page as rendered in the search index
  - [2] 2026-10-22: all promotional credits 'Expire 12 months from the issue date unless otherwise agreed in writing' and 'Can only be used after you've used up Deepgram's standard signup credits', quoted from the terms page as rendered in the search index
- sources:
  - [1] https://deepgram.com/startup-program
  - [2] https://deepgram.com/startup-program-terms-of-service
