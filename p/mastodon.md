# mastodon /about/more as a limit source

> mastodon.social | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mastodon/ | JSON https://fshy.ajam.dev/api/v1/entity/mastodon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mastodon /about/more as a limit source

- `storage/mastodon-about-more-as-a-limit-source` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:51.194Z (live) | stale on 2026-12-04
- url https://mastodon.social/about/more
- free tier: none reachable: Mastodon 4.x renders /about/more as a client-side application without static upload limit text in raw HTML responses. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: The instance API states media attachment caps: "image_size_limit":16777216, "video_size_limit":103809024, and "max_media_attachments":4 | source: [1] | note: not applicable
- retention: stated-absent: the /about/more page and instance API describe the server, its rules and media limits but state no retention period for stored bytes | source: [1]
- egress: stated-absent: the /about/more page and instance API state media size caps but no egress price or transfer quota | metered: no
- identity: email
- interface: rest
- interface detail: Instance metadata REST endpoint at /api/v1/instance and a WebSocket streaming API; /about/more is a client-rendered page about the server. Neither states a general byte-storage interface
- tooling: not documented
- composes with: stated-absent: the /about/more page and instance API describe a social-media server with REST and streaming endpoints, but state no way to chain it as general byte storage
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Zero of 20 instances yielded an…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Zero of 20 instances yielded an up
  - [2] 2026-10-21: Zero of 20 instances yielded an up
  - [2] 2026-11-19: the instance API exposes per-attachment media limits as JSON, not the /about/more HTML page | capture: sha256:11ae4598ce0a4538f54225c688de49e827123a503dcdd175d02b78a5f9da39be | quote: "image_size_limit":16777216,"image_matrix_limit":33177600,"video_size_limit":103809024
  - [2] 2026-11-19: the first-party host exposes a documented REST instance endpoint and a streaming API, not a byte store | capture: sha256:963628bd3ed0e46e88594395d1f9cea390458b90df145fe3eba4e5976705aeb4 | quote: "streaming_api":"wss://streaming.mastodon.social"
  - [2] 2026-11-19: the first-party instance API states a 16,777,216-byte per-image limit | capture: sha256:963628bd3ed0e46e88594395d1f9cea390458b90df145fe3eba4e5976705aeb4 | quote: "image_size_limit":16777216
  - [1] 2026-11-19: the about page describes the server and states no retention term | capture: sha256:bfc1eb91ef82f0dcde9646b58a355a6a0e88254d02cdf192dee35d7532ae38fc
- sources:
  - [1] https://mastodon.social/about/more
  - [2] https://mastodon.social/api/v1/instance
