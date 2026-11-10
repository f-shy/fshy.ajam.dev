# xbox network

> xbox.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xbox/ | JSON https://fshy.ajam.dev/api/v1/entity/xbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xbox network captures

- `storage/xbox-network-captures` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://news.xbox.com/en-us/2023/09/27/bonus-xbox-update-for-september/
- free tier: none reachable: Policy since 2023-10-01 deletes captures stored on the Xbox network after 90 days. Explicitly a TTL cache, not storage; the intended destination is your own OneDrive. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
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
  - dead_end.failure_class: not-storage
  - dead_end.why: Policy since 2023-10-01 deletes captures stored on the Xbox network after 90 days. Explicitly a TTL cache, not storage; the intended destination is your own OneDrive.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Policy since 2023-10-01 deletes captures stored on the Xbox network after 90 days. Explicitly a TTL cache, not storage; the intended destination is your own OneDrive.
- sources:
  - [1] https://news.xbox.com/en-us/2023/09/27/bonus-xbox-update-for-september/

## XBOX services Title Storage

- `storage/xbox-services-title-storage` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://devdocs.xbox.com/services/xbox-services/storage/title-storage/live-title-storage-overview
- free tier: Trusted Platform: 256 MB per player (Managed Partners) / 64 MB per player (Creators Program). Universal Platform: 64 MB per player. Global: 256 MB. No total-title byte cap published. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 64 MB | bytes: 64000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered separately in the Title Storage docs; access is through Xbox services. | metered: yes
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap: 64 MB [1]
- limits note: Per-object-cap: 64 MB per player on the Creator-Program tier; request-rate: ~60 reads or writes per hour per session, then throttled. Binary must be base64/hex encoded. Retention: not documented as expiring. Data persists with the title.
- interface detail: rest
- tooling: Xbox services REST endpoints + GDK; data must be hex or base64 encoded because Title Storage 'doesn't process encoded data'.
- composes with: 256 MB per player x unlimited players, but the per-write encoding overhead (base64 = +33%) eats the ceiling, and Managed Partner status is a gate for the 256 MB tier.
- reliability: Throttles to roughly one call per minute averaged over an hour-long session, so bulk transfer is painful; the 256 MB tier requires Managed Partner status rather than self-serve signup.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Trusted Platform: 256 MB per player (Managed Partners) / 64 MB per player (Creators Program). Universal Platform: 64 MB per player. Global: 256 MB. No total-title byte cap published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: quota table: 'Trusted Platform | 256 MB per player | 64 MB per player', 'Universal Platform | 64 MB per player', 'Global | 256 MB'; 'a title can make 60 reads or writes at the beginning of a session, but no more for the remainder of the hour'
- sources:
  - [1] https://devdocs.xbox.com/services/xbox-services/storage/title-storage/live-title-storage-overview
