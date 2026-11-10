# packagist

> packagist.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/packagist/ | JSON https://fshy.ajam.dev/api/v1/entity/packagist.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## packagist (php/composer)

- `storage/packagist` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://packagist.org/about
- free tier: None reachable: It is an index, not a store. /about states packages are described by composer.json in 'your package's git/svn/. repository'. Packagist hosts metadata only and dist URLs point back at GitHu. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: It is an index, not a store. /about states packages are described by composer.json in 'your package's git/svn/.. repository' — Packagist hosts metadata only and dist URLs point back at…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It is an index, not a store. /about states packages are described by composer.json in 'your package's git/svn/.. repository' — Packagist hosts metadata only and dist URLs point back at…
  - [2] 2026-10-21: cited as the basis of the rejection: It is an index, not a store. /about states packages are described by composer.json in 'your package's git/svn/.. repository' — Packagist hosts metadata only and dist URLs point back at GitHu
- sources:
  - [1] https://packagist.org/about
  - [2] https://repo.packagist.org/p2/monolog/monolog.json
