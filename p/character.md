# character.ai

> character.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/character/ | JSON https://fshy.ajam.dev/api/v1/entity/character.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## character.ai

- `storage/character-ai` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.060Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/character.md
- free tier: None reachable: No document/file storage product at all. Text persona chat only. Nothing to store. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the External Character.AI OpenAPI spec states no per-object size cap | note: not applicable
- retention: stated-absent: the External Character.AI OpenAPI spec states no retention period for stored bytes
- egress: stated-absent: the External Character.AI OpenAPI spec states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the External Character.AI OpenAPI spec defines /chat/completions and /character/{character_id}/greeting/ and no file or object storage endpoint
- tooling: not documented
- composes with: stated-absent: the External Character.AI OpenAPI spec defines chat and greeting endpoints and states no byte-storage chaining mechanism
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No document/file storage product at all — text persona chat only. Nothing to store.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: No document/file storage product at all — text persona chat only. Nothing to store.
  - [1] 2026-11-19: the first-party product description is an interactive-entertainment chat service with no document or file storage offering, consistent with the recorded rejection | capture: sha256:368c2bed3eb14b53a02db2320332d06d85b6ba0527f387063bc1263a1d995c47 | quote: Character.AI empowers people to connect, learn, and tell stories through interactive entertainment.
  - [2] 2026-11-19: the External Character.AI OpenAPI spec defines chat completion and character greeting endpoints and no file or object storage endpoint | capture: sha256:256c9f25f906ed3f5bc736f6f12a4903c31619225dd07b1178c61ed5216b8097 | quote: /chat/completions:
  - [2] 2026-11-19: the spec's paths are chat and character greeting, not byte storage | capture: sha256:256c9f25f906ed3f5bc736f6f12a4903c31619225dd07b1178c61ed5216b8097 | quote: /character/{character_id}/greeting/:
  - [2] 2026-11-19: the spec describes a chat-completion API and states no retention term | capture: sha256:256c9f25f906ed3f5bc736f6f12a4903c31619225dd07b1178c61ed5216b8097 | quote: title: External Character.AI - OpenAPI 3.0
- sources:
  - [1] https://character.ai/about
  - [2] https://raw.githubusercontent.com/character-ai/openapi/main/openapi.yaml
