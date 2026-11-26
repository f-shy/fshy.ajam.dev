# cocoapods trunk

> cocoapods.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cocoapods/ | JSON https://fshy.ajam.dev/api/v1/entity/cocoapods.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cocoapods trunk

- `storage/cocoapods-trunk` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:08.914Z (live) | stale on 2026-12-04
- url https://guides.cocoapods.org/making/getting-setup-with-trunk
- free tier: none reachable: Trunk accepts a .podspec (JSON metadata, a few KB) and nothing else; the pod's source is a URL field pointing at your own host. 'pod trunk push [NAME.podspec] will deploy your Podspec to… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Trunk accepts a .podspec (JSON metadata, a few KB) and nothing else; the pod's source is a URL field pointing at your own host. 'pod trunk push [NAME.podspec] will deploy your Podspec to…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Trunk accepts a .podspec (JSON metadata, a few KB) and nothing else; the pod's source is a URL field pointing at your own host. 'pod trunk push [NAME.podspec] will deploy your Podspec to…
  - [1] 2026-11-19: Trunk accepts and publishes only a Podspec, not arbitrary bytes | capture: sha256:491aaa1683ec5c93fd294169cc9ae8052050ae19d80f973fca3d92691c30078b | quote: `pod trunk push [NAME.podspec]` will deploy your Podspec to Trunk and make it publicly available. You can also deploy Podspecs to your own private specs repo with `pod repo push REPO [NAME.podspec]`.
- sources:
  - [1] https://guides.cocoapods.org/making/getting-setup-with-trunk
