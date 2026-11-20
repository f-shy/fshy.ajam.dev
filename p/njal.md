# njalla

> njal.la | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/njal/ | JSON https://fshy.ajam.dev/api/v1/entity/njal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## njalla

- `storage/njalla` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:54.246Z (live) | stale on 2026-12-04
- url https://njal.la/servers/add/30
- free tier: none reachable: not a storage product; the VPS line now offers up to 90 GB disk (VPS 90), with no standalone storage tier on the site | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Not a storage product. Largest published disk on the VPS line is 30 GB; storage-only tier does not exist on the site. Privacy-brand pricing, not capacity pricing.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not a storage product. Largest published disk on the VPS line is 30 GB; storage-only tier does not exist on the site. Privacy-brand pricing, not capacity pricing.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a storage product. Largest published disk on the VPS line is 30 GB; storage-only tier does not exist on the site. Privacy-brand pricing, not capacity pricing.
  - [2] 2026-11-19: the largest published VPS disk is now 90 GB, not 30 GB | capture: sha256:f7eb76ebe07655a4d8f045880c2aa887775cef9133da1e0f696c1a08fd32090e | quote: 90 GB Disk
  - [3] 2026-11-19: Njalla sells privacy-branded VPS and VPN products, not a standalone storage tier | capture: sha256:23d65f21d66432657239cf0dc2c72306598308ceb4cdf883afdc0a0b0c182f33 | quote: Host your mastodon, matrix, nextcloud and blinking under construction gifs with us!
- sources:
  - [1] https://njal.la/servers/add/30
  - [2] https://njal.la/pricing/
  - [3] https://njal.la/
