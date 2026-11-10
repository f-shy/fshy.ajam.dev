# RunAnywhere

> runanywhere.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runanywhere/ | JSON https://fshy.ajam.dev/api/v1/entity/runanywhere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunAnywhere

- `compute/runanywhere` | qualifies-with-caveat | evidence reported | binding write-gated | category inference API
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:57.573Z (live) | stale on 2026-11-19
- url https://www.runanywhere.ai/
- free tier: USD 5.0 of one-time credit, from catalog records; unverified against live endpoints | unit: mixed | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
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
- sources:
  - [1] https://www.runanywhere.ai/
  - [2] https://docs.runanywhere.ai/
