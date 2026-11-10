# Self-hosted Synapse media repository

> matrix-org.github.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/matrix-org-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/matrix-org-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Self-hosted Synapse media repository

- `storage/self-hosted-synapse-media-repository` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html
- free tier: Unbounded. `max_upload_size` defaults to 50M and can be set to any value; storage and media retention are entirely operator-controlled. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Bandwidth depends on host server allocation. Fronting endpoints with caching CDNs allows media caching to reduce origin egress traffic. | metered: no
- identity: institution
- interface: s3, rest, webdav, rclone
- limits note: `max_upload_size` default 50M; reverse proxy must be raised too (nginx default body size bites first). `media_retention.local_media_lifetime` / `remote_media_lifetime` can silently delete anything not accessed within the window.
- interface detail: rest
- tooling: Synapse (Python) or Dendrite/Conduit; standard Matrix media API so rclone's `s3`/`webdav`-adjacent tooling plus any Matrix SDK works. Admin media API allows listing and purging media per user/room.
- composes with: Not a free provider. The multiplier angle is that media is content-addressed and deduplicated by Synapse, and federation lets you push copies to other homeservers as a second replica.
- reliability: Default installs are safe; the risk is operator misconfiguration. Enabling media_retention turns the repo into a TTL cache. Federation media cache is the first thing purged.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Unbounded — `max_upload_size` defaults to 50M and can be set to any value; storage and media retention are entirely operator-controlled.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'max_upload_size — The largest allowed upload size in bytes... Defaults to 50M.'
  - [1] 2026-10-21: 'media_retention ... control whether media will be purged if it has not been accessed in a given amount of time'
- sources:
  - [1] https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html
