# gitea.com

> gitea.com | Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitea/ | JSON https://fshy.ajam.dev/api/v1/entity/gitea.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gitea cloud

- `storage/gitea-cloud` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:24.329Z (live) | stale on 2026-11-18
- url https://about.gitea.com/products/cloud/
- free tier: none reachable: Commercial managed Gitea. 30-day free trial only, storage is a paid add-on pack, and the 'unlimited network traffic' feature is unlimited-bandwidth-at-throttled-speed rather than free… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Outgoing traffic is unlimited in volume but each plan has a high-speed quota, after which a speed restriction applies to outgoing traffic only; incoming traffic is free and unlimited. unverified: the quota size and the restricted speed are not stated on the vendor pages. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the 2026-11-03 read covered the Gitea Cloud release announcement on about.gitea.com (a per-plan high-speed traffic quota, then a speed restriction on outgoing traffic; incoming traffic free and unlimited); the trial length and the paid storage pack are not stated on it
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Commercial managed Gitea. 30-day free trial only, storage is a paid add-on pack, and the 'unlimited network traffic' feature is unlimited-bandwidth-at-throttled-speed rather than free…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Commercial managed Gitea. 30-day free trial only, storage is a paid add-on pack, and the 'unlimited network traffic' feature is unlimited-bandwidth-at-throttled-speed rather than free…
  - [2] 2026-10-21: cited as the basis of the rejection: Commercial managed Gitea. 30-day free trial only, storage is a paid add-on pack, and the 'unlimited network traffic' feature is unlimited-bandwidth-at-throttled-speed rather than free egress
  - [2] 2026-11-03: outgoing traffic is throttled after a per-plan high-speed quota | capture: sha256:a6ddba63a751b290b2d25a801dbaf82110334c7d5552bdff2b93bfe5fc9f0d5d | quote: Plans now include a quota for high-speed traffic, and once that quota is reached, an appropriate speed restriction will apply only to outgoing traffic leaving your Gitea Cloud instance
  - [2] 2026-11-03: incoming traffic is free and unlimited | capture: sha256:a6ddba63a751b290b2d25a801dbaf82110334c7d5552bdff2b93bfe5fc9f0d5d | quote: traffic going into your instance remains completely free and unlimited
- sources:
  - [1] https://about.gitea.com/products/cloud/
  - [2] https://about.gitea.com/news/gitea-cloud-release-12/

## gitea.com (hosted gitea)

- `storage/gitea-com` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gitea.com/v2/
- free tier: none reachable: No container registry endpoint at all: GET https://gitea.com/v2/ returns 404. Gitea's cloud offering is a 30-day trial, and the self-hosted product is free software, not free storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: No container registry endpoint at all: GET https://gitea.com/v2/ returns 404. Gitea's cloud offering is a 30-day trial, and the self-hosted product is free software, not free storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No container registry endpoint at all: GET https://gitea.com/v2/ returns 404. Gitea's cloud offering is a 30-day trial, and the self-hosted product is free software, not free storage.
  - [2] 2026-10-21: cited as the basis of the rejection: No container registry endpoint at all: GET https://gitea.com/v2/ returns 404. Gitea's cloud offering is a 30-day trial, and the self-hosted product is free software, not free storage.
- sources:
  - [1] https://gitea.com/v2/
  - [2] https://about.gitea.com/products/cloud/

## gitea.com (official hosted instance)

- `storage/gitea-com-2` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gitea.com/api/v1/version
- free tier: none reachable: Instance is live and registration is open, but the container registry is not exposed: /v2/ returns 404 (not 401), and /api/v1/packages returns 404. Only the git side is usable, with no… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Instance is live and registration is open, but the container registry is not exposed: /v2/ returns 404 (not 401), and /api/v1/packages returns 404. Only the git side is usable, with no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Instance is live and registration is open, but the container registry is not exposed: /v2/ returns 404 (not 401), and /api/v1/packages returns 404. Only the git side is usable, with no…
  - [2] 2026-10-21: cited as the basis of the rejection: Instance is live and registration is open, but the container registry is not exposed: /v2/ returns 404 (not 401), and /api/v1/packages returns 404. Only the git side is usable, with no publi
  - [3] 2026-10-21: cited as the basis of the rejection: Instance is live and registration is open, but the container registry is not exposed: /v2/ returns 404 (not 401), and /api/v1/packages returns 404. Only the git side is usable, with no publi
- sources:
  - [1] https://gitea.com/api/v1/version
  - [2] https://gitea.com/v2/
  - [3] https://gitea.com/api/v1/packages?limit=3

## self-hosted gitea/forgejo as a route around the quota

- `storage/self-hosted-gitea-forgejo-as-a-quota-bypass` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.gitea.com/administration/config-cheat-sheet/
- free tier: none reachable: Gitea and Forgejo default every package limit to -1 (no limit): LIMIT_TOTAL_OWNER_SIZE -1, LIMIT_SIZE_GENERIC -1, LIMIT_SIZE_CONTAINER -1; Forgejo quota.ENABLED defaults false and… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Gitea and Forgejo default every package limit to -1 (no limit): LIMIT_TOTAL_OWNER_SIZE -1, LIMIT_SIZE_GENERIC -1, LIMIT_SIZE_CONTAINER -1; Forgejo quota.ENABLED defaults false and…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Gitea and Forgejo default every package limit to -1 (no limit): LIMIT_TOTAL_OWNER_SIZE -1, LIMIT_SIZE_GENERIC -1, LIMIT_SIZE_CONTAINER -1; Forgejo quota.ENABLED defaults false and…
  - [2] 2026-10-21: cited as the basis of the rejection: Gitea and Forgejo default every package limit to -1 (no limit): LIMIT_TOTAL_OWNER_SIZE -1, LIMIT_SIZE_GENERIC -1, LIMIT_SIZE_CONTAINER -1; Forgejo quota.ENABLED defaults false and quota.defa
- sources:
  - [1] https://docs.gitea.com/administration/config-cheat-sheet/
  - [2] https://forgejo.org/docs/latest/admin/config-cheat-sheet/
