# misskey.pm

> misskey.pm | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/misskey-5/ | JSON https://fshy.ajam.dev/api/v1/entity/misskey-5.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## misskey.pm — 9.8 GB per user

- `storage/misskey-pm-9-8-gb-per-user` | fails-quota | evidence reported | binding per-object-cap | category fediverse-misskey
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://misskey.pm
- free tier: 10024 MB ≈ 9.8 GiB per user; maxFileSize 250 MiB. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 250 MiB | bytes: 262144000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free CDN. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 250 MiB [1]
- limits note: per-object-cap 250 MiB; per-user 10024 MB.
- interface detail: rest
- tooling: Misskey API / MiAuth.
- composes with: Open registration. Marginal over calckey.world; listed for breadth of the sweep.
- reliability: Live, open, small.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10024 MB ≈ 9.8 GiB per user; maxFileSize 250 MiB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=10024, maxFileSize=262144000, disableRegistration=false, version 2026.10.0
- sources:
  - [1] https://misskey.pm/api/meta
