# Neptune.ai

> neptune.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neptune/ | JSON https://fshy.ajam.dev/api/v1/entity/neptune.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Neptune.ai

- `storage/neptune-ai` | dead | evidence reported | binding per-object-cap | category mlops-artifacts
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:48.162Z (live) | stale on 2026-12-04
- url https://neptune.ai
- free tier: No storage allowance published. Pricing documentation specifies experiment counts, run counts, and user seats without storage capacity figures. Artifact storage is not provided as a free resource pool. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: no per-object cap documented because bulk object storage is not the product | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not applicable. | metered: no
- identity: email | detail: email.
- interface: s3-compatible, rest
- limits:
  - per-object-cap (binding): no per-object cap documented because bulk object storage is not the product [1]
- limits note: Metered by tracked runs/months and users rather than bytes; no per-object cap documented because bulk object storage is not the product.
- interface detail: rest
- tooling: neptune Python client (run[...] logging, artifact tracking). Mature but narrower than W&B; no S3-compatible surface.
- composes with: None. No free byte allowance to multiply.
- reliability: Stable. Not a storage provider in any sense relevant to this survey.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No storage allowance published, and the pricing page contained no GB figure at all — the metered dimensions are experiment/run counts and seats. Artifact storage is not offered as a free pool.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: acquired
- evidence:
  - [1] 2026-10-21: read live: the page returned no GB/storage figure (grep for GB|TB|storage returned nothing), i.e. storage is not a priced or granted dimension
  - [1] 2026-11-19: the vendor announced its acquisition by OpenAI on 2025-12-03 and its pricing page no longer serves a standalone price list | capture: sha256:17d9db389c3cd7e97cffe3e9db669602532c787f941267ef129bfce58a095405 | quote: We’re excited to share that OpenAI has entered into a definitive agreement to acquire neptune.ai, strengthening the tools and infrastructure that support progress in frontier research.
  - [1] 2026-11-19: neptune.ai the standalone MLOps artifact vendor has been acquired by OpenAI and no longer offers a standalone pricing page | capture: sha256:17d9db389c3cd7e97cffe3e9db669602532c787f941267ef129bfce58a095405 | quote: We’re excited to share that OpenAI has entered into a definitive agreement to acquire neptune.ai, strengthening the tools and infrastructure that support progress in frontier research.
- sources:
  - [1] https://neptune.ai/pricing
