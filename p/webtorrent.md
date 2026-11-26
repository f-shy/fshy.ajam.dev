# bittorrent

> webtorrent.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webtorrent/ | JSON https://fshy.ajam.dev/api/v1/entity/webtorrent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bittorrent / webtorrent seeding

- `storage/bittorrent-webtorrent-seeding` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://webtorrent.io/
- free tier: none reachable: Same structural failure as Hypercore: no host, no quota, no persistence guarantee. WebTorrent needs an active seeder (you) and browser peers; a torrent with no seeder is a 0-byte download.… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Same structural failure as Hypercore: no host, no quota, no persistence guarantee. WebTorrent needs an active seeder (you) and browser peers; a torrent with no seeder is a 0-byte download.…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Same structural failure as Hypercore: no host, no quota, no persistence guarantee. WebTorrent needs an active seeder (you) and browser peers; a torrent with no seeder is a 0-byte download.…
- sources:
  - [1] https://webtorrent.io/
