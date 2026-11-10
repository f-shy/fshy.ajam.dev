# ElevenLabs

> elevenlabs.io | Compute, Inference; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/elevenlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/elevenlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ElevenLabs (Compute)

- `compute/elevenlabs` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://elevenlabs.io/pricing
- free tier: Free plan at USD 0 with '10k credits per month'. One shared monthly pool across every product, with the vendor's own per-product rates: 'Text to Speech 1 credit per character; Speech to Text 330 credits per minute; Eleven Music 900 credits per minute; Sound Effects 200 credits per generation; Voice Changer and Voice Isolator 1,000 credits per minute'. 10,000 credits therefore buys either 10,000 characters of TTS (about 10 minutes of audio at the common 1,000 characters a minute), or 30 minutes of speech-to-text, or 50 sound effects, or 5 minutes of voice isolation, per month. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-monthly-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): the monthly credit pool is small and does not roll over on the Free plan: 'Rollover does not apply to the Free plan', so the 10,000 credits are lost at the end of each billing cycle and a batch job larger than 10 minutes of audio cannot be finished across two months. [1]
- limits note: the monthly credit pool is small and does not roll over on the Free plan: 'Rollover does not apply to the Free plan', so the 10,000 credits are lost at the end of each billing cycle and a batch job larger than 10 minutes of audio cannot be finished across two months.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the 10,000 credits compose with a free transcription service by splitting the job: send speech-to-text to a vendor with a larger minute allowance and keep ElevenLabs for the TTS voice, because 330 credits a minute makes this pool the worst value as a transcriber. What breaks: any loop that synthesises more than 10,000 characters a month, which is roughly 10 minutes of speech.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute: no machine, no shell, no GPU is handed over, only metered calls to a hosted voice model. Per-month character cost of the cheapest paid lane for scale: Starter at USD 6 for 30,000 credits is USD 0.20 per 1,000 characters. Open question: whether one email address can hold more than one free workspace; the pricing page does not say and no probe was run against the signup endpoint.
- extras:
  - facets.class: credit-too-small-for-a-workload
  - facets.free_tier_kind: recurring-monthly-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the plan table prints 'Free $0 per month ... 10k credits per month', quoted; and the FAQ confirms 'Free $0 (10,000 credits)'
  - [1] 2026-10-22: 'Text to Speech 1 credit per character; Speech to Text 330 credits per minute; Eleven Music 900 credits per minute; Sound Effects 200 credits per generation; Voice Changer and Voice Isolator 1,000 credits per minute', quoted from the FAQ 'How many credits does each product use?'
  - [1] 2026-10-22: 'Rollover does not apply to the Free plan', quoted from the FAQ 'When do my credits reset, and do unused credits roll over?'
- sources:
  - [1] https://elevenlabs.io/pricing

## ElevenLabs (Free)

- `inference/elevenlabs` | qualifies-with-caveat | evidence documented | binding volume-quota | category text-to-speech and speech-to-text API, monthly free credit pool | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
- url https://elevenlabs.io/pricing/api
- free tier: Free plan at USD 0 with 10,000 credits per month, no credit card required. One shared monthly pool across every product: Text to Speech 1 credit per character on multilingual models (0.5 to 1 credit per character on Flash and Turbo through the API), Speech to Text 330 credits per minute, Eleven Music 900 credits per minute, Sound Effects 200 credits per generation. Free-plan API access is included; the pool resets each billing cycle and does not roll over. | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: models on the API pricing page: text-to-speech Eleven v4, v4 Turbo, v3 and Flash/Turbo families, speech-to-text Scribe v2 and Scribe v2 Realtime, music, sound effects, voice changer and voice isolator. unverified: which of these models the Free plan can call through the API, because the pages read list the Free column only as a credit count
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no credit card ('No credit card required, no commitment'); the signup page offers Sign up with Google or an email with a password; unverified: whether a phone number or an email confirmation step follows the form
- interface: rest
- limits:
  - volume-quota (binding): 10,000 credits per month on the Free plan, shared by every product, with no rollover on the Free plan [1]
  - request-rate: Free plan concurrency: text-to-speech 4 concurrent requests on Flash and Turbo models and 2 on all other models; speech-to-text 8 and realtime speech-to-text 6 [2]
  - write-gated: the Voice Library is not available through the API to free-tier users [3]
- binding note: the 10,000 credits per month pool is shared by every product and does not roll over on the Free plan, so it runs out before the 2-request concurrency cap matters
- interface detail: HTTP and WebSocket requests from any language; official Python and Node.js libraries
- endpoint: https://api.elevenlabs.io
- tooling: official Python (pip install elevenlabs) and Node.js (@elevenlabs/elevenlabs-js) libraries, or raw HTTP and WebSocket with an API key created in the account settings
- composes with: 10,000 credits a month is about 10,000 characters of text-to-speech, enough for short voice-over or a TTS smoke test inside a free CI job; the speech-to-text rate of 330 credits per minute makes this pool poor value for transcription, so send transcription to a service with a larger allowance and keep this pool for the voice.
- reliability: unused Free-plan credits are lost at the end of each billing cycle
- notes: a USD 1 first-month Starter offer on the pricing page is a paid plan, not a free tier; the Startup Grants program is a separate record in the compute topic
- evidence note: the 10,000 credit pool, the per-product credit costs, the no-rollover rule, the concurrency tables and the card-free signup are quoted from vendor pages; the model set open to the Free plan through the API is unverified.
- evidence:
  - [1] 2026-11-03: the Free plan includes 10,000 credits | capture: sha256:88559518bc57544f239661e144ef1442ce879c836120a1984b4a2a2fb549fc50 | quote: Monthly price and included credits per plan: Free $0 (10,000 credits); Starter $6 (30,000 credits);
  - [1] 2026-11-03: one shared credit pool across every product | capture: sha256:88559518bc57544f239661e144ef1442ce879c836120a1984b4a2a2fb549fc50 | quote: All products draw from one shared monthly credit pool, so the same credits can be spent on any of them and using one leaves fewer for the others.
  - [1] 2026-11-03: the credit cost per product | capture: sha256:88559518bc57544f239661e144ef1442ce879c836120a1984b4a2a2fb549fc50 | quote: Approximate credit costs are: Text to Speech 1 credit per character; Speech to Text 330 credits per minute; Eleven Music 900 credits per minute; Sound Effects 200 credits per generation;
  - [1] 2026-11-03: unused credits do not roll over on the Free plan | capture: sha256:88559518bc57544f239661e144ef1442ce879c836120a1984b4a2a2fb549fc50 | quote: Rollover does not apply to the Free plan.
  - [1] 2026-11-03: Flash and Turbo models cost 0.5 to 1 credit per character through the API | capture: sha256:88559518bc57544f239661e144ef1442ce879c836120a1984b4a2a2fb549fc50 | quote: For V2 Flash/Turbo English and V2.5 Flash/Turbo Multilingual models, discounted pricing applies for API usage, costing between 0.5 and 1 credit per character.
  - [1] 2026-11-03: the credit allowance resets each billing cycle | capture: sha256:88559518bc57544f239661e144ef1442ce879c836120a1984b4a2a2fb549fc50 | quote: Your credit allowance resets at the start of each billing cycle, which begins on the day you subscribed.
  - [4] 2026-11-03: API pay-as-you-go rates for speech-to-text, Scribe and Scribe realtime, per hour | capture: sha256:7c6d71e08609e2772a620f75425149619761310cfce1c942efdb64e71bf3da82 | quote: Speech to Text $0.22 per hour (Scribe) or $0.39 per hour (Scribe realtime)
  - [5] 2026-11-03: API endpoints are available on the free plan | capture: sha256:39b061b106a6c1f3b1fb3d48af21c94f88fc2542d0d9d9636e7ba6cfff629faa | quote: Most of our API endpoints are available for all plans, including the free plan.
  - [3] 2026-11-03: the Voice Library is not available through the API on the free tier | capture: sha256:a55f3fb0fa0ad62f96bd079a0b3f3158070973d714c0812e4d5c53be5684fac8 | quote: The voice library is not available via the API to free tier users.
  - [2] 2026-11-03: Free plan text-to-speech concurrency is 4 on Flash and Turbo and 2 on other models | capture: sha256:12863600a98331fa9199e174c87de3bf4296cb8fd4aaed1aaa9754b6bc793b49 | quote: | Free | 4 | 2 |
  - [6] 2026-11-03: Free plan speech-to-text concurrency is 8 and realtime 6 | capture: sha256:45a0da1d57480e438664cbbc9beec8db2fad5e1260263e27d76b911a48cbf195 | quote: | Free | 8 | 6 |
  - [7] 2026-11-03: the API is reachable over HTTP and WebSocket with official Python and Node.js libraries | capture: sha256:2127afa5154e150e1773681bdb4cbdca5aa84babd230c72f4730a5136cf4777c | quote: You can interact with the API through HTTP or Websocket requests from any language, via our official Python bindings or our official Node.js libraries.
  - [8] 2026-11-03: the free plan needs no credit card | capture: sha256:b9165bfed60b9fd98eab6a61f8458cb55240e430f48df655e42f03a46930f069 | quote: No credit card required, no commitment.
  - [9] 2026-11-03: the signup page offers a Google route and an email route | capture: sha256:66820da7468ff539149023906530c91286fbc2cb7a30ef42cea72e47227238af | quote: Sign up with Google
  - probe:https://api.elevenlabs.io 2026-11-10: a POST to the bare host https://api.elevenlabs.io, with no path and no key, answered HTTP 404 with the body {"detail": "Not Found"}; no API route was requested, so the route was not tested | capture: sha256:183d23c8f1683fc04a44629ed68176a6e97955e37fa50915e1884a2a638452d5 | quote: "status": 404
- sources:
  - [1] https://elevenlabs.io/pricing
  - [2] https://elevenlabs.io/docs/help-center/technical/how-many-text-to-speech-requests-can-i-make-and-can-i-increase-it
  - [3] https://elevenlabs.io/docs/eleven-creative/quickstart
  - [4] https://elevenlabs.io/pricing/api
  - [5] https://help.elevenlabs.io/hc/en-us/sections/14163158308369-API
  - [6] https://help.elevenlabs.io/hc/en-us/articles/33472885290129-How-many-Speech-to-Text-requests-can-I-make-and-can-I-increase-it
  - [7] https://elevenlabs.io/docs/api-reference/introduction
  - [8] https://join.elevenlabs.io/voice-library
  - [9] https://elevenlabs.io/app/sign-up

## ElevenLabs Startup Grants

- `compute/elevenlabs-startup-grants` | fails-identity | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://elevenlabs.io/startup-grants
- free tier: 'Scale for 12 months ... 33,000,000 characters ... That's over 680 hours of Agents usage. More than $5,500+ in value.' The gate is a company: 'The ElevenLabs Grants program is open to all startups or companies with less than 25 employees', 'Only applications with valid business emails will be considered', 'Agencies, consulting firms and SMBs are not eligible', 'One application per company', and the programme requires 'a business or monetization strategy' with 'No short-term or one-off projects'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: term-credit-12-months
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): a review committee decides: the grant is applied for and approved 'in our sole discretion', so a person with an email address alone holds a company-shaped application with no product to show; the 33M characters are unreachable without a company, a business email domain and a monetisation story. [1]
- limits note: a review committee decides: the grant is applied for and approved 'in our sole discretion', so a person with an email address alone holds a company-shaped application with no product to show; the 33M characters are unreachable without a company, a business email domain and a monetisation story.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 33M characters at 1 credit a character is 33,000 minutes of TTS, and the vendor prices that against its own Pro tier: 600,000 credits for USD 99, so 33M credits is about 55 months of Pro. What breaks: the award, not the quota. No chain makes an unapproved application usable.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. Classified as a refutation: the largest per-person voice credit in this market is not reachable by a person. An applicant would need a registered company, a domain email and a product with a monetisation strategy, and even then the decision is discretionary. The value claim of 'USD 5,500+' is the vendor's own arithmetic, not measured.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: term-credit-12-months
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Scale for 12 months ... 33,000,000 characters ... That's over 680 hours of Agents usage. More than $5,500+ in value', quoted
  - [1] 2026-10-22: 'Only applications with valid business emails will be considered' and 'The ElevenLabs Grants program is open to all startups or companies with less than 25 employees at the time of receiving the application', quoted from the eligibility FAQ
  - [1] 2026-10-22: 'After your grant period is over or once you have 10,000 credits left, your plan will automatically convert to a Free plan', quoted: the grant is a clock, not a budget
  - [2] 2026-10-22: the pricing page repeats the offer as '12 Months free ... 33M Characters ... Valid for 12 months', corroborating the size
- sources:
  - [1] https://elevenlabs.io/startup-grants
  - [2] https://elevenlabs.io/pricing
