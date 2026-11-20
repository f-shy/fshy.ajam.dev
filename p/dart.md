# pub.dev

> dart.dev | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dart/ | JSON https://fshy.ajam.dev/api/v1/entity/dart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pub.dev (dart/flutter)

- `storage/pub-dev` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:57.506Z (live) | stale on 2026-12-04
- url https://dart.dev/tools/publishing
- free tier: none reachable: 'Keep package size within limits. We recommend less than 100 MB after gzip compression and less than 256 MB uncompressed.' Also 'Publishing is forever' (a permanence plus, but no delete… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [2] | note: not applicable
- retention: not recorded | source: [2]
- egress: not recorded | metered: no
- identity: email | detail: A Google Account is required to publish; it can be a Gmail address or any other email address.
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Keep package size within limits. We recommend less than 100 MB after gzip compression and less than 256 MB uncompressed.' Also 'Publishing is forever' (a permanence plus, but no delete…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Keep package size within limits. We recommend less than 100 MB after gzip compression and less than 256 MB uncompressed.' Also 'Publishing is forever' a permanence plus, but no delete mean
  - [1] 2026-11-19: the current publishing guide recommends limits of 100 MB compressed and 256 MB uncompressed | capture: sha256:26c2cf0a8b1cc64f81942166f327a19006d44e3eca2e87102ac4b0ca7c699552 | quote: - Keep package size within limits. We recommend less than 100 MB after gzip compression and less than 256 MB uncompressed.
  - [1] 2026-11-19: publishing requires a Google Account, which may be any email address | capture: sha256:26c2cf0a8b1cc64f81942166f327a19006d44e3eca2e87102ac4b0ca7c699552 | quote: - Own a [Google Account](https://support.google.com/accounts/answer/27441). Pub uses a Google account to manage package upload permissions. Your Google Account can be associated with a Gmail address or any other email address.
  - probe:https://dart.dev/tools/publishing 2026-11-19: the originally cited URL answered HTTP 404 on 2026-11-19 | capture: sha256:818cb1963a9fd77b2644e6d50a45cd8989f4599c432398cde023f51ae5b9410a | quote: "status": 404
- sources:
  - [1] https://dart.dev/tools/pub/publishing
  - [2] https://dart.dev/tools/publishing
