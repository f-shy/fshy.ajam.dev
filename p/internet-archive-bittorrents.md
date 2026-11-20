# Internet Archive BitTorrents

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/internet-archive-bittorrents/ | JSON https://fshy.ajam.dev/api/v1/entity/internet-archive-bittorrents.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Internet Archive BitTorrents (webseed swarm)

- `storage/internet-archive-bittorrents` | qualifies-with-caveat | evidence documented | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:59.617Z (live) | stale on 2026-12-20
- url https://archive.org/details/torrents
- free tier: Free, unlimited distribution; ~1.4 million items already torrented, 'comprising almost a petabyte of public domain materials'. Egress is unbounded because the swarm and webseeds share the load. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. 'our Torrents rely heavily on webseeding (download directly from our servers, when no peers have the files you are seeking)'. Peers carry the rest at zero cost to anyone. | metered: no
- identity: email
- interface: rest, rclone
- limits note: Torrent is generated server-side only (you do not choose the swarm); obsolete torrents break when the item changes (piece-hash mismatch); rTorrent does not support Getright-style webseeding and will not start; bt1 trackers are rate-limited per IP; ._____padding_file must be deselected.
- interface detail: rest
- tooling: Any BitTorrent client with Getright-style webseed support (qBittorrent, Transmission); IA generates the .torrent per item and runs trackers bt1.archive.org; rclone not involved
- composes with: Combine with #1: upload once via IAS3, then distribute via torrent so a 1TiB/day fetch load is carried by peers + webseed instead of a single HTTP stream. Torrent + webseed is also the only path that can exceed the ~1.7 MB/s per-connection shaping.
- reliability: Old torrents for a mutated item loop forever re-downloading mismatched pieces; seeder counts are cached ~5 minutes and include webseeds.
- notes: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
- evidence:
  - [1] 2026-10-21: (snapshot 2026-09-13) — 'over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte'
  - [1] 2026-10-21: 'Our Torrents rely heavily on webseeding ... rTorrent do not support Getright-style webseeding'
  - [1] 2026-10-21: torrents for changed items 'become obsolete ... files will fail to download completely'
  - [1] 2026-11-11: the item count and total size distributed by BitTorrent | capture: sha256:6dc610eddc8675338708dd22f41bbdf6d49b59cce4e1a111231f40d874bf6525 | quote: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
  - [1] 2026-11-19: over 1.4 million items and almost a petabyte are distributed via BitTorrent | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
  - [1] 2026-11-19: Archive torrents rely on webseeding from Archive servers when no peers hold the files | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: This is because our Torrents rely heavily on webseeding (download directly from our servers, when no peers have the files you are seeking).
- sources:
  - [1] https://help.archive.org/help/archive-bittorrents/
