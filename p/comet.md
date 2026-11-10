# Comet ML

> comet.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/comet/ | JSON https://fshy.ajam.dev/api/v1/entity/comet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Comet ML (Comet / Opik) — artifact + dataset management

- `storage/comet-ml-artifact-dataset-management` | fails-quota | evidence reported | binding retention-clamped | category mlops-artifacts
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.comet.com
- free tier: No storage allowance at all on the free tier. The free cloud plan is metered in spans, not bytes: 'Up to 10 team members · 25k spans per month · 60-day data retention'. Artifact/dataset management is a paid-MLOps feature; the free plan is the Opik observability product with a 60-day retention clamp. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: The free cloud plan is metered in spans, not bytes: 'Up to 10 team members · 25k spans per month · 60-day data retention' | days: 60 | source: [1] | note: not stated
- egress: Not applicable. There is no free storage pool to egress from. | metered: no
- identity: email | detail: email; academic Pro requires institutional verification.
- interface: rest
- limits:
  - retention-clamped (binding): Retention is the killer: 60 days [1]
- limits note: 25k spans/month, 10 team members, 60-day data retention on Free. Retention is the killer: 60 days is a hard clamp, so this cannot hold an archive even if bytes were free.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Comet_ml Python SDK (log_artifact, log_dataset), plus Opik's own SDK. Self-hostable: github.com/comet-ml/opik is open source, which is the only unlimited path. On your own disks.
- composes with: None. With no free byte allowance, multiplying accounts multiplies zero.
- reliability: Free tier enforces an automatic 60-day retention limit that cannot be overridden by client settings.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No storage allowance at all on the free tier. The free cloud plan is metered in spans, not bytes: 'Up to 10 team members · 25k spans per month · 60-day data retention'. Artifact/dataset management is a paid-MLOps feature; the free plan is the Opik observability product with a 60-day retention clamp.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: Free Cloud '$0 ... Up to 10 team members · 25k spans per month · 60-day data retention'; Pro Cloud '$19 ... 100k spans per month · 60-day data retention'
  - [1] 2026-10-21: read live: 'Our MLOps platform is designed for teams building and training machine learning models, with tools for experiment tracking, dataset management, model versioning' — i.e. dataset management is the MLOps product, not the free Opik one
- sources:
  - [1] https://www.comet.com/site/pricing/
