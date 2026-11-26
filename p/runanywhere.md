# RunAnywhere

> runanywhere.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runanywhere/ | JSON https://fshy.ajam.dev/api/v1/entity/runanywhere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunAnywhere

- `compute/runanywhere` | qualifies-with-caveat | evidence reported | binding write-gated | category inference API
- identity a placeholder: card and phone unknown | verified 2026-11-18T04:58:05.489Z (live) | stale on 2026-12-03
- url https://www.runanywhere.ai/
- free tier: USD 5.0 of one-time credit, from catalog records; unverified against live endpoints | unit: mixed | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - write-gated (binding): access is a sign-in and a credit purchase; no plan or rate is published on the page [1]
- interface detail: the `wally` CLI, and one API key against an OpenAI-compatible endpoint at https://inference.runanywhere.ai/v1
- tooling: the `wally` CLI (installed by script, then `wally account login`); any OpenAI client against the endpoint
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and is a sign-in prompt with a single call to action. It publishes no price and no free allowance, so the USD 5 credit still rests on documented records card
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page states nothing about a session
  - free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Sign in, buy credits, run.' quoted; the page is a 1,389-byte sign-in and credit prompt with no plan, no rate and no free allowance
  - [2] 2026-11-03: access is by CLI or an API key against an OpenAI-compatible endpoint | capture: sha256:6d941002e0998386a32bf620fee4cef311736dd7b2d6c8078489ede8ca38caea | quote: You reach them with the `wally` CLI or with one API
  - [2] 2026-11-04: access is the wally CLI or one API key against an OpenAI-compatible endpoint | capture: sha256:6d941002e0998386a32bf620fee4cef311736dd7b2d6c8078489ede8ca38caea | quote: You reach them with the `wally` CLI or with one API
  - [2] 2026-11-04: the endpoint URL | capture: sha256:6d941002e0998386a32bf620fee4cef311736dd7b2d6c8078489ede8ca38caea | quote: `https://inference.runanywhere.ai/v1`
  - [1] 2026-11-18: not stated | capture: sha256:50a3c96f16004438490f1a1ffaab96abec5ceda0733e4b2ad5e8a60ddb7169d4 | quote: # We make the best open models faster and cheaper to run, for everyone.
- sources:
  - [1] https://www.runanywhere.ai/
  - [2] https://docs.runanywhere.ai/

## Wally

- `inference/wally` | paid-only | evidence documented | binding volume-quota | category inference gateway (cloud and local)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.runanywhere.ai/wally-cloud/quickstart
- free tier: Cloud usage bills against prepaid credits. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: browser sign-in with Google or GitHub and a separately entitled Cloud key
- interface: rest
- limits:
  - volume-quota (binding): prepaid credits; 403 insufficient_credit when the account is out of credit [1]
- endpoint: https://inference.runanywhere.ai/v1
- composes with: No free inference allowance is published in the fetched cloud quickstart.
- reliability: 429 capacity or rate limit with Retry-After when present
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Wally Cloud bills inference against prepaid credits and signs in through Google or GitHub with no free tier stated | capture: sha256:f2dd4df49bf887c9fa1d11d56cbd36b42c97eea76b154cebf9df11f0c366ff8d | quote: Cloud usage bills against prepaid credits.
- sources:
  - [1] https://docs.runanywhere.ai/wally-cloud/quickstart
