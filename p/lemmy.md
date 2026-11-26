# lemmy.world

> lemmy.world | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lemmy/ | JSON https://fshy.ajam.dev/api/v1/entity/lemmy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## lemmy.world / lemmy.ml / sh.itjust.works / feddit.org as open upload target

- `storage/lemmy-world-lemmy-ml-sh-itjust-works-feddit-org-as-open` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.635Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/lemmy.md
- free tier: none reachable: The big Lemmy instances either require an application to register (lemmy.world: registration_mode='RequireApplication') or do not publish an upload size in the API at all, because the limit | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: The site rate limit allows 50 images per 3600 seconds; no per-object byte cap is published in the site API. | note: not applicable
- retention: stated-absent: the first-party page states no retention period for uploaded images in the site API response
- egress: stated-absent: the first-party page states no egress terms for stored bytes | metered: no
- identity: email
- interface: rest, graph
- interface detail: HTTP JSON API under /api/v3/ and a federated ActivityPub graph
- tooling: not documented
- composes with: Federation links the instance into the wider Lemmy/ActivityPub network; the site API states no arbitrary byte-storage chaining.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: The big Lemmy instances either require an application to register (lemmy.world: registration_mode='RequireApplication') or do not publish an upload size in the API at all, because the limit
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: The big Lemmy instances either require an application to register (lemmy.world: registration_mode='RequireApplication') or do not publish an upload size in the API at all, because the limit
  - probe:https://lemmy.world/api/v3/site 2026-11-19: lemmy.world still requires an application to register, so the write gate stands | capture: sha256:f2db20246a900b773a2a4a461744746e3a43215ba8d502919782f8ac07dce5b1 | quote: "registration_mode":"RequireApplication"
  - [1] 2026-11-19: the Lemmy World first-party site API reports a RequireApplication registration gate | capture: sha256:e5205d93c3855a4f5b542f4972a8b7741bcde45703674f08e1055cdd92ba13a8 | quote: "registration_mode":"RequireApplication"
- sources:
  - [1] https://lemmy.world/api/v3/site
