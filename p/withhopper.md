# Hopper

> withhopper.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/withhopper/ | JSON https://fshy.ajam.dev/api/v1/entity/withhopper.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hopper

- `inference/hopper` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://withhopper.com/agents/deepseek-v4.1-flash-1017.md
- free tier: New accounts start with USD 5 in credit shared across the account's keys and usage. After it runs out, requests draw from prepaid credit topped up in the console. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign up or sign in at withhopper.com/console/keys and create an API key
- interface: rest
- limits:
  - volume-quota (binding): USD 5 credit on signup, shared across keys; prepaid top-up afterwards [1]
- endpoint: https://api.withhopper.com/v1
- tooling: an OpenAI-compatible base URL with an account API key; no Hopper package is needed
- composes with: the one-off USD 5 signup credit and the prepaid top-up after it bind the offer
- reliability: on 402 the account needs credit; on 429 the caller must honor Retry-After; the test request is a one-off check, not a speed benchmark
- notes: the only free allowance is a USD 5 signup credit shared across keys, after which usage is prepaid
- evidence:
  - [1] 2026-11-18: new accounts start with USD 5 in shared credit; a signup and key are required and further use draws from prepaid credit | capture: sha256:55b1af822cd173130ed3fb729923d40bbce9ddd0a12d9c423c5d1e8b3ddeb900 | quote: New accounts start with **$5 in credit**, shared across the account's keys and usage.
- sources:
  - [1] https://withhopper.com/agents/deepseek-v4.1-flash-1017.md
