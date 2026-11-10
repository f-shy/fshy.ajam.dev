# ioc.exchange

> ioc.exchange | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ioc/ | JSON https://fshy.ajam.dev/api/v1/entity/ioc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ioc.exchange — Mastodon, 1.32 GiB video / 80 MB image, open registration

- `storage/ioc-exchange-mastodon-1-32-gib-video-80-mb-image-open-re` | fails-quota | evidence reported | binding per-object-cap | category fediverse-mastodon
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ioc.exchange
- free tier: Unlimited per-account; per-file video_size_limit=1419430400 (1.32 GiB), image_size_limit=83886080 (80 MiB). | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-file video_size_limit=1419430400 (1.32 GiB | bytes: 1417339207 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-file video_size_limit=1419430400 (1.32 GiB [1]
- limits note: per-object-cap 1.32 GiB video / 80 MiB image; per-account unlimited; request-rate 30 media posts / 30 min/user.
- interface detail: rest
- tooling: Mastodon REST API v1 + OAuth2.
- composes with: Second instance in the sweep with a deliberately relaxed 1+ GiB cap; a good failover when infosec.exchange throttles, since the throttle is per-instance-per-account you can parallelise across the two.
- reliability: Security-research instance, Glitch fork, open signup, healthy.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Unlimited per-account; per-file video_size_limit=1419430400 (1.32 GiB), image_size_limit=83886080 (80 MiB).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: GET -> 200, image_size_limit=83886080, video_size_limit=1419430400, registrations.enabled=true, registrations=true
  - [2] 2026-10-21: probe: GET -> 200, max_toot_chars=11000
- sources:
  - [1] https://ioc.exchange/api/v2/instance
  - [2] https://ioc.exchange/api/v1/instance
