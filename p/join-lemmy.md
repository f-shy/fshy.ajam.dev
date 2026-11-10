# Lemmy + pict-rs

> join-lemmy.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/join-lemmy/ | JSON https://fshy.ajam.dev/api/v1/entity/join-lemmy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lemmy + pict-rs — per-instance image store, no per-user quota

- `storage/lemmy-pict-rs-per-instance-image-store-no-per-user-quota` | fails-quota | evidence reported | binding per-object-cap | category fediverse-lemmy
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://join-lemmy.org/docs/administration/configuration.html
- free tier: No per-user quota in Lemmy's own schema — the bound is pict-rs (the separate Rust image server) and the instance's disk. Upload is gated per-instance by the `image_upload` / `image_mode` local-site flag rather than by bytes. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap set by pict-rs (`max_file_size`, commonly 40 MB | bytes: 40000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap set by pict-rs (`max_file_size`, commonly 40 MB [1]
- limits note: per-object-cap set by pict-rs (`max_file_size`, commonly 40 MB); no per-user byte quota; per-instance disk.
- interface detail: rest
- tooling: Lemmy API v3: POST /api/v3/pictrs/image (multipart) or /api/v3/upload; needs a JWT from POST /api/v3/user/login. pict-rs itself exposes POST /image on its own port (often 8080). On instances that expose it, that is a cleaner upload path than the Lemmy API.
- composes with: Lemmy is the weakest of the family: most large instances now REQUIRE an application (lemmy.world registration_mode = 'RequireApplication'), and `image_mode` is frequently set to block uploads entirely or to proxy-only. Multiplier depends entirely on finding a permissive instance.
- reliability: Registration gated on the big instances. Also note Lemmy stores federated/remote images too, so operator disk fills from other people's content, which is why uploads get turned off.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No per-user quota in Lemmy's own schema — the bound is pict-rs (the separate Rust image server) and the instance's disk. Upload is gated per-instance by the `image_upload` / `image_mode` local-site flag rather than by bytes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, local_site.registration_mode='RequireApplication', version 0.19.19-9-gc55dd1b1a; local_site carries NO image upload size field (only image_mode/enable_nsfw-style flags) — confirms the quota lives in pict-rs, not Lemmy
  - [1] 2026-10-21: pict-rs is a separate service; 'Generate thumbnails for external post urls and store them persistently in pict-rs. This also increases storage usage.'
- sources:
  - [1] https://join-lemmy.org/docs/administration/configuration.html
  - [2] https://lemmy.world/api/v3/site
