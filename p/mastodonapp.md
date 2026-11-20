# mastodonapp.uk

> mastodonapp.uk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mastodonapp/ | JSON https://fshy.ajam.dev/api/v1/entity/mastodonapp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mastodonapp.uk / mstdn.social / mastodon.social and the stock-Mastodon mass — 100 MiB per object, unlimited per account

- `storage/mastodonapp-uk-mstdn-social-mastodon-social-and-the-stoc` | fails-quota | evidence documented | binding per-object-cap | category fediverse-mastodon
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:03:55.918Z (live) | stale on 2026-12-04
- url https://mastodonapp.uk
- free tier: Per-account UNLIMITED. Per-file: 103809024 bytes = 99 MiB (video), 16 MiB image on almost every stock instance. mastodonapp.uk raises the IMAGE cap to 99 MiB too, which is the unusual bit. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file: 103809024 bytes = 99 MiB | bytes: 103809024 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Media is offloaded to plain S3-compatible buckets behind the instance domain. Verified on two live instances: mastodon.world serves from `s3.eu-central-2.wasabisys.com/mastodonworld/..` (Wasabi), mstdn.jp serves from `img.mstdn.jp/media_attachments/files/..`. | metered: no
- identity: email | detail: mastodonapp.uk sign-up steps: accept rules, your details, confirm email, review by the moderators; no phone or card step is listed
- interface: rest, cli
- limits:
  - per-object-cap (binding): Per-file: 103809024 bytes = 99 MiB [1]
- limits note: mastodonapp.uk: image_size_limit and video_size_limit both 103809024 bytes (99 MiB), 4 media attachments per status; per-account unlimited and the API call rates are unverified on this host
- interface detail: rest
- tooling: Mastodon REST API v1; `toot` CLI; Mastodon.py; Mastodon-API clients in every language.
- composes with: Standard Mastodon instances enforce per-file limits (typically 40 to 99 MiB) and rate limits (30 uploads per 30 minutes) rather than aggregate account quotas. Media is hosted by instance storage nodes and distributed via federation.
- reliability: Registration state varies per instance and flips often. Mastodon.social, mstdn.social, mstdn.jp, mastodon.world, mastodon.gamedev.place all reported registrations=true at probe time; mas.to, fosstodon.org, chaos.social, toot.community, mastodon.online reported false. Re-probe before relying on any one.
- notes: the same as the free tier
- evidence note: documented: the image and video size limits and the attachments per status are quoted from https://mastodonapp.uk/api/v2/instance; the sign-up steps from https://mastodonapp.uk/auth/sign_up; the image size limit of a stock instance from https://mastodon.social/api/v2/instance; the media upload rate limit from https://docs.joinmastodon.org/api/rate-limits/ (read 2026-11-03)
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Per-account UNLIMITED. Per-file: 103809024 bytes = 99 MiB (video), 16 MiB image on almost every stock instance. mastodonapp.uk raises the IMAGE cap to 99 MiB too, which is the unusual bit.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: GET -> 200, image_size_limit=103809024, video_size_limit=103809024, registrations.enabled=true
  - [2] 2026-10-21: probe: GET -> 200, image_size_limit=16777216, video_size_limit=103809024, registrations.enabled=true
  - [3] 2026-10-21: probe: GET -> 200, 16777216/103809024, registrations.enabled=true
  - [4] 2026-10-21: probe: HEAD media URL -> 200, image/png, 1640544 bytes, Cache-Control: public, max-age=315576000, immutable; origin URL = s3.eu-central-2.wasabisys.com/mastodonworld/media_attachments/files/117/479/508/370/053...
  - [5] 2026-10-21: probe: HEAD ... -> 200, image/png, 1557834 bytes, Cache-Control: public, max-age=315576000, immutable
  - [6] 2026-11-03: mastodonapp.uk sign-up is accept rules, your details, confirm email, then review by the moderators | capture: sha256:cee6b3ce8335a2486b7e68f5acaa8385387b8a23514bfad5744bdb57618b0e23 | quote: 3. Confirm email
  - [6] 2026-11-03: the fourth sign-up step is review by the moderators | capture: sha256:cee6b3ce8335a2486b7e68f5acaa8385387b8a23514bfad5744bdb57618b0e23 | quote: 4. Our review
  - [1] 2026-11-03: mastodonapp.uk allows 4 media attachments per status | capture: sha256:086ae85328e0fb5e011867e9d53c2d6aa47436b33f7b8c0b6936be69063c4145 | quote: "statuses":{"max_characters":1000,"max_media_attachments":4,"characters_reserved_per_url":23}
  - [1] 2026-11-03: mastodonapp.uk states an image size limit of 103809024 bytes | capture: sha256:086ae85328e0fb5e011867e9d53c2d6aa47436b33f7b8c0b6936be69063c4145 | quote: "image_matrix_limit":70000000,"image_size_limit":103809024,"supported_mime_types":["image/jpeg"
  - [1] 2026-11-03: mastodonapp.uk states a video size limit of 103809024 bytes | capture: sha256:086ae85328e0fb5e011867e9d53c2d6aa47436b33f7b8c0b6936be69063c4145 | quote: "video_size_limit":103809024},"polls"
  - [2] 2026-11-03: mastodon.social states an image size limit of 16777216 bytes | capture: sha256:9d955bfd49108168251de6c74a5ec1fd64c8793eaf2c61f5289d5e484f624f65 | quote: "image_matrix_limit":33177600,"image_size_limit":16777216,"supported_mime_types":["image/jpeg"
  - [7] 2026-11-03: the Mastodon documentation lists 30 media uploads per 30 minutes | capture: sha256:d9a0f690a68b1a02055a7ebb4485f1dc75ad6fae6869149940fb12be5464489e | quote: `POST /api/v1/media` can be called 30 times within 30 minutes.
  - [1] 2026-11-03: the vendor page was read and quoted on 2026-11-03: mastodonapp.uk allows 4 media attachments per status | capture: sha256:086ae85328e0fb5e011867e9d53c2d6aa47436b33f7b8c0b6936be69063c4145 | quote: "statuses":{"max_characters":1000,"max_media_attachments":4,"characters_reserved_per_url":23}
- sources:
  - [1] https://mastodonapp.uk/api/v2/instance
  - [2] https://mastodon.social/api/v2/instance
  - [3] https://mstdn.jp/api/v2/instance
  - [4] https://mastodon.world
  - [5] https://img.mstdn.jp/media_attachments/files/117/478/448/419/166/526/original/dc54343aadba4cee
  - [6] https://mastodonapp.uk/auth/sign_up
  - [7] https://docs.joinmastodon.org/api/rate-limits/
