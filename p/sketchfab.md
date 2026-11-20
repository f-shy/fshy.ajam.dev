# Sketchfab

> sketchfab.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sketchfab/ | JSON https://fshy.ajam.dev/api/v1/entity/sketchfab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sketchfab

- `storage/sketchfab-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:26.831Z (live) | stale on 2026-12-04
- url https://sketchfab.com/plans
- free tier: none reachable: 100 MB per model on Basic (50 MB per the features page); 10 uploads/month although downloadable models do not count. Ingest is a 3D mesh+texture pipeline, so arbitrary files do not survive… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 100 MB per model on Basic (50 MB per the features page); 10 uploads/month although downloadable models do not count. Ingest is a 3D mesh+texture pipeline, so arbitrary files do not survive…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 100 MB per model on Basic (50 MB per the features page); 10 uploads/month although downloadable models do not count. Ingest is a 3D mesh+texture pipeline, so arbitrary files do not survive…
  - [2] 2026-10-21: cited as the basis of the rejection: 100 MB per model on Basic (50 MB per the features page); 10 uploads/month although downloadable models do not count. Ingest is a 3D mesh+texture pipeline, so arbitrary files do not survive a
  - [1] 2026-11-19: Sketchfab's live plans page still exempts downloadable models from the monthly upload limit | capture: sha256:8f479b75a30be66a2e86a4551d96c803ed943ffcc34fc9ffc8920e60bb51dca2 | quote: A model that is downloadable doesn't count against this limit.
  - [2] 2026-11-19: Sketchfab ingest is a 3D mesh API pipeline, not arbitrary file storage | capture: sha256:c4575a8960a0b68bf2b757aeb7b14ecf7de66be2cc311a48dad5fa4db3f9df59 | quote: Via API ([see our API documentation](https://sketchfab.com/developers)).
- sources:
  - [1] https://sketchfab.com/plans
  - [2] https://sketchfab.com/features

## Sketchfab (3D model hosting, Epic Games)

- `storage/sketchfab` | fails-quota | evidence documented | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:26.831Z (live) | stale on 2026-12-20
- url https://sketchfab.com
- free tier: Free 'basic' plan is 10 uploads/month with a per-model cap that the two official pages disagree on: /features says 50 MB for Free / 200 MB Pro / 500 MB Premium, while the /plans comparison table renders 100 MB / 200 MB / 500 MB for basic / pro / custom. Either way the Free cap is 50–100 MB per model (mesh + textures + everything), so the ambiguity does not change the verdict. A model marked downloadable does not count against the monthly upload count. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Per-object-cap 50–100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: Per-object-cap 50–100 MB free (docs conflict, see quota); the binding constraint is the request-rate equivalent of 10 uploads/month; retention is indefinite but content is re-processed into a viewer pipeline, so byte-exactness of textures is not guaranteed for display purposes. | source: [1] | note: not stated
- egress: Free and CDN-served; the original file is retrievable when the author enables download, and there is a Viewer API and oEmbed/iframe embedding. No egress pricing. | metered: no
- identity: email
- interface: rest
- limits:
  - request-rate: 10 uploads/month [1]
  - per-object-cap (binding): Per-object-cap 50–100 MB [1]
- limits note: Per-object-cap 50–100 MB free (docs conflict, see quota); the binding constraint is the request-rate equivalent of 10 uploads/month; retention is indefinite but content is re-processed into a viewer pipeline, so byte-exactness of textures is not guaranteed for display purposes.
- interface detail: rest
- tooling: Documented REST API with bulk upload support ('Bulk uploads: Via API'); community Python/js clients; glTF/OBJ/FBX/PLY/STL and ~25 other formats accepted.
- composes with: 10 uploads/month x ~50–100 MB = 0.5–1 GB/month per account, and the cap only applies to models left non-downloadable. Multiplying accounts is the only path, and the per-object cap never rises above 100 MB.
- reliability: Commercial 3D asset hosting platform with restrictive monthly upload count quotas and small per-file upload caps. Models may be unlisted or disabled by platform moderators.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free 'basic' plan is 10 uploads/month with a per-model cap that the two official pages disagree on: /features says 50 MB for Free / 200 MB Pro / 500 MB Premium, while the /plans comparison table renders 100 MB / 200 MB / 500 MB for basic / pro / custom. Either way the Free cap is 50–100 MB per model (mesh + textures + everything), so the ambiguity does not change the verdict. A model marked downloadable does not count against the monthly upload count.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Max upload size: 50MB for Free accounts, 200MB for Pro accounts, 500MB for Premium accounts'; 'Bulk uploads: Via API'
  - [2] 2026-10-21: free basic plan 'Uploads / month: 10'; 'A model that is downloadable doesn't count against this limit'; compare table renders 'Maximum file size per model: 100MB' for basic, which CONTRADICTS /features' 50 MB — recorded as a docs conflict, verdict unaffected
  - [1] 2026-11-19: Sketchfab's first-party features page was read and captured | capture: sha256:c4575a8960a0b68bf2b757aeb7b14ecf7de66be2cc311a48dad5fa4db3f9df59 | quote: - 50MB for Free accounts
  - [1] 2026-11-19: Sketchfab's features page states a 50 MB max upload size for Free accounts and documents API bulk uploads | capture: sha256:c4575a8960a0b68bf2b757aeb7b14ecf7de66be2cc311a48dad5fa4db3f9df59 | quote: - 50MB for Free accounts
  - [2] 2026-11-19: Sketchfab's live plans page still exempts downloadable models from the monthly upload limit | capture: sha256:8f479b75a30be66a2e86a4551d96c803ed943ffcc34fc9ffc8920e60bb51dca2 | quote: A model that is downloadable doesn't count against this limit.
  - [2] 2026-11-19: Sketchfab's per-model size cap covers the mesh, textures and all bundled files | capture: sha256:8f479b75a30be66a2e86a4551d96c803ed943ffcc34fc9ffc8920e60bb51dca2 | quote: This includes the 3D mesh, textures, and any other files included with the model.
- sources:
  - [1] https://sketchfab.com/features
  - [2] https://sketchfab.com/plans
