# Chutes

> chutes.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chutes/ | JSON https://fshy.ajam.dev/api/v1/entity/chutes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chutes (Compute)

- `compute/chutes` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://chutes.ai/news/community-announcement-february
- free tier: The free tier is retired. Announcement quoted: 'we introduced an Early Access perk that provided 200 requests per day for free ... the program is no longer sustainable in its current form and will be discontinued', with the 200-request quota removed for TEE models on 27 February 2026 and 'fully retired' on 15 March 2026. The pricing page now lists pay-as-you-go with 'no subscription, no minimum' plus Plus at USD 10 per month and Pro at USD 20 per month. | unit: requests | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous | detail: nothing beyond a chosen username: 'You can sign up with Google or GitHub, or just pick a username and Chutes mints a fingerprint credential', and 'Connecting a Bittensor wallet is optional; you do not need one to use the platform'. No email, no phone, no card and no ID is required on that path, which is why the kind is anonymous rather than email. No hold exists because no payment method is taken at signup; debit and prepaid acceptance are not stated, and paying for tokens afterwards is not described.
- interface: cli
- limits:
  - volume-quota (binding): The free 200-requests-per-day lane ended on 15 March 2026, so the first request now requires a funded balance; the cheapest lane left is pay-as-you-go. [1]
- limits note: The free 200-requests-per-day lane ended on 15 March 2026, so the first request now requires a funded balance; the cheapest lane left is pay-as-you-go.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The wallet-optional signup is the useful fact: a username plus a fingerprint credential reaches a Bittensor-market inference endpoint with no wallet and no card, so once any balance exists this is the cheapest documented token rate found in this class for TEE-hosted inference.
- reliability: no reliability event recorded
- notes: REFUTATION plus a documentation contradiction notable. Chutes' own starter guide says a Bittensor wallet is optional, while its GitHub README and its CLI reference still say 'you must have a Bittensor wallet and hotkey' for registration. The web signup path is the one that works without a wallet; the CLI path is the one that assumes one. A reader who follows the CLI first will wrongly conclude this is wallet-gated. The free tier, however, is genuinely gone, which is the fact that matters for a zero-budget client.
- extras:
  - facets.class: decentralized-inference
  - facets.shape.gpu_class: TEE-hosted inference; private deploy from USD 1.80 per hour
- evidence:
  - [1] 2026-10-22: announcement dated 2026-02-27 states the 200 requests per day free perk is discontinued, TEE access removed at once, and the plan fully retired on 15 March 2026
  - [2] 2026-10-22: current pricing lists pay-as-you-go with no minimum, Plus at USD 10 per month, Pro at USD 20 per month, and private deployment GPU rates from USD 1.80 per hour with a deploy fee starting at USD 5.40
  - [3] 2026-10-22: quoted: 'You can sign up with Google or GitHub, or just pick a username and Chutes mints a fingerprint credential ... Connecting a Bittensor wallet is optional; you do not need one to use the platform'
  - [4] 2026-10-22: catalog of 14 models as of 2026-10-22, all reporting confidential_compute true; cheapest Mistral-Nemo at USD 0.0245 per million input and USD 0.0978 per million output tokens
- sources:
  - [1] https://chutes.ai/news/community-announcement-february
  - [2] https://chutes.ai/pricing
  - [3] https://chutes.ai/docs/guides/starter-guide
  - [4] https://chutes.ai/llms.txt

## Chutes (Inference)

- `inference/chutes` | paid-only | evidence documented | binding volume-quota | category serverless inference, pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://chutes.ai
- free tier: no free allowance stated: pay only for tokens and GPU time, top up a balance, no subscription or minimum commitment | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account is created at chutes.ai/signup; no card or phone field is stated on the apex page
- interface: rest
- limits:
  - volume-quota (binding): top-up balance; per-token and per-second GPU billing, no subscription [1]
- binding note: no free token allowance, so a funded balance binds first
- endpoint: https://llm.chutes.ai/v1
- tooling: an OpenAI-compatible key and the Chutes SDK/CLI
- composes with: pairs with an OpenAI-compatible agent on a topped-up balance; no published free route
- reliability: no reliability event recorded
- notes: the apex and docs publish pay-as-you-go only; no free tier is stated.
- evidence:
  - [1] 2026-11-18: pay only for tokens and GPU time, no subscription | capture: sha256:c83ffd8c626db562894a77f8c214693158a85b87fcb4f2acec093150ee45965c | quote: Pay only for the tokens and GPU time you use. No subscription, no minimum commitment.
- sources:
  - [1] https://chutes.ai
