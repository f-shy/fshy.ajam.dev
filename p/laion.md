# laion

> laion.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/laion/ | JSON https://fshy.ajam.dev/api/v1/entity/laion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## laion (laion-400m / 5b / re-laion-5b)

- `storage/laion` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:14.242Z (live) | stale on 2026-12-04
- url https://laion.ai/
- free tier: none reachable: Read-only corpus publisher, not a host. laion.ai/data/ is a 404; everything is a link out to Hugging Face datasets (excluded as already known). No upload path, no account, no quota of yours | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1]
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Read-only corpus publisher, not a host. laion.ai/data/ is a 404; everything is a link out to Hugging Face datasets (excluded as already known). No upload path, no account, no quota of yours
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Read-only corpus publisher, not a host. laion.ai/data/ is a 404; everything is a link out to Hugging Face datasets (excluded as already known). No upload path, no account, no quota of yours
  - [2] 2026-10-21: cited as the basis of the rejection: Read-only corpus publisher, not a host. laion.ai/data/ is a 404; everything is a link out to Hugging Face datasets (excluded as already known). No upload path, no account, no quota of yours
  - probe:https://laion.ai/data/ 2026-11-19: the cited /data/ path still answers HTTP 404, so the read-only-corpus rejection stands | capture: sha256:6a672d07f5d0c8f2420e4eecc00687cc4b50eb144113ed6eb02a552ca80c2b16 | quote: "status": 404,
  - probe:https://laion.ai/data/ 2026-11-19: the /data/ path that was to hold the offer still answers HTTP 404, so this rejected offer is dead | capture: sha256:6a672d07f5d0c8f2420e4eecc00687cc4b50eb144113ed6eb02a552ca80c2b16 | quote: "status": 404,
  - [1] 2026-11-19: the first-party site describes a research network with no storage sign-up, matching the recorded rejection | capture: sha256:8c06456a740d677eeb73e535021338b0ec8f66c0ec97a4dd32f12578bd457c4b | quote: LAION is a non-profit research network building open datasets, models, and tools for reproducible machine-learning research and public education.
- sources:
  - [1] https://laion.ai/
  - [2] https://laion.ai/data/
