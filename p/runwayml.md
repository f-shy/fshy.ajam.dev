# Runway

> runwayml.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runwayml/ | JSON https://fshy.ajam.dev/api/v1/entity/runwayml.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Runway

- `compute/runway` | trial-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:52.255Z (live) | stale on 2026-12-05
- url https://runwayml.com/pricing
- free tier: Free plan, printed as 'Free forever' with '125 credits' and '125 one-time credits to explore Runway's AI tools'. The paid plans give the conversion: 625 credits is '52s of Gen-4.5, 104s of Gen-4 Turbo, or 78 Gen-4 Images (1080p)', so 125 credits is about 10.4 seconds of Gen-4.5, 20.8 seconds of Gen-4 Turbo, or 15 Gen-4 images. The rate card prices Gen-4.5 at '60 credits/5s' and Aleph 2.0 at '140 credits/5s'. | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): 125 credits is a demo, not a budget: at 60 credits per five seconds of Gen-4.5 the entire free allowance is two five-second clips, and nothing renews, so the second film cannot be made. [1]
- limits note: 125 credits is a demo, not a budget: at 60 credits per five seconds of Gen-4.5 the entire free allowance is two five-second clips, and nothing renews, so the second film cannot be made.
- binding note: the same as limits note
- interface detail: HTTP API documented at docs.dev.runwayml.com, with Node and Python SDK examples
- tooling: the Node SDK `@runwayml/sdk` and a Python SDK, both over the Runway API
- composes with: the free allowance is best spent on images rather than video: 15 Gen-4 images for the same 125 credits is a usable figure set, where 10 seconds of video is a single shot. What breaks: there is no renewal, so a second experiment needs a second account.
- reliability: no reliability event recorded
- notes: Runway offers one-time promotional inference credits upon signup for video generation models.
- extras:
  - facets.class: credit-too-small-for-a-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the Free plan prints 'Free forever' and '125 one-time credits to explore Runway's AI tools', quoted
  - [1] 2026-10-22: '625 credits monthly = 52s of Gen-4.5, 104s of Gen-4 Turbo, or 78 Gen-4 Images (1080p)', quoted, which fixes the per-second rate the free credit buys
  - [1] 2026-10-22: the generation table prints 'Gen-4.5 60 credits/5s' and 'Aleph 2.0 140 credits/5s', quoted
  - [2] 2026-11-03: Runway documents an HTTP API with Node and Python SDKs | capture: sha256:f7def71e4ac0e193a5285af6955684595c379024ffb564e68c70f9a20e8552c0 | quote: directly into your apps, products, platforms and websites through one API.
  - [2] 2026-11-04: the documented client is the @runwayml/sdk package | capture: sha256:f7def71e4ac0e193a5285af6955684595c379024ffb564e68c70f9a20e8552c0 | quote: import RunwayML, { TaskFailedError } from '@runwayml/sdk';
- sources:
  - [1] https://runwayml.com/pricing
  - [2] https://docs.dev.runwayml.com/
