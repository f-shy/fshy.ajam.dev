# Internet Archive BitTorrents

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/internet-archive-bittorrents/ | JSON https://fshy.ajam.dev/api/v1/entity/internet-archive-bittorrents.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Internet Archive BitTorrents (webseed swarm)

- `storage/internet-archive-bittorrents` | qualifies-with-caveat | evidence documented | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-11-25T12:15:46.508Z (live) | stale on 2026-12-26
- url https://archive.org/details/torrents
- free tier: Free, unlimited distribution; ~1.4 million items already torrented, 'comprising almost a petabyte of public domain materials'. Egress is unbounded because the swarm and webseeds share the load. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Torrents rely heavily on webseeding: download directly from Archive servers when no peers have the files. The page states no price and no bandwidth limit for torrent or webseed download. | metered: no
- identity: email | detail: The torrent page names no account requirement for downloading. Creating the item that receives an Archive torrent needs a free archive.org account.
- interface: unknown
- limits note: Torrents become obsolete when the item changes, and some or all files then fail to download completely. Clients without Getright-style webseeding, such as rTorrent, cannot download un-seeded Archive torrents. The ._____padding_file directory should be deselected. The trackers bt1.archive.org and bt2.archive.org are closed and track only the Archive's own torrents. A torrent for an item without one is requested by email to info@archive.org.
- interface detail: BitTorrent protocol: .torrent files per item with Getright-style webseeding, tracked by bt1.archive.org and bt2.archive.org
- tooling: A BitTorrent client with Getright-style webseeding support; the Archive generates the .torrent per item and runs the trackers bt1.archive.org and bt2.archive.org.
- composes with: Archive BitTorrents are made automatically for community-contributed items in many collections and updated when the item changes. The torrent falls back on webseeding from Archive servers when no peers have the files.
- reliability: Old torrents for a mutated item loop forever re-downloading mismatched pieces; seeder counts are cached ~5 minutes and include webseeds.
- notes: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
- evidence:
  - [1] 2026-10-21: (snapshot 2026-09-13) — 'over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte'
  - [1] 2026-10-21: 'Our Torrents rely heavily on webseeding ... rTorrent do not support Getright-style webseeding'
  - [1] 2026-10-21: torrents for changed items 'become obsolete ... files will fail to download completely'
  - [1] 2026-11-11: the item count and total size distributed by BitTorrent | capture: sha256:6dc610eddc8675338708dd22f41bbdf6d49b59cce4e1a111231f40d874bf6525 | quote: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
  - [1] 2026-11-19: over 1.4 million items and almost a petabyte are distributed via BitTorrent | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
  - [1] 2026-11-19: Archive torrents rely on webseeding from Archive servers when no peers hold the files | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: This is because our Torrents rely heavily on webseeding (download directly from our servers, when no peers have the files you are seeking).
  - [1] 2026-11-25: torrents are created automatically for community items and updated on change | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Internet Archive BitTorrents are automatically made for community-contributed items in many collections, and automatically updated when item contents or metadata change.
  - [1] 2026-11-25: webseeding downloads directly from Archive servers when no peers hold the files | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: This is because our Torrents rely heavily on webseeding (download directly from our servers, when no peers have the files you are seeking).
  - [1] 2026-11-25: torrents become obsolete when the item changes | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Torrents for Items on the Internet Archive can become obsolete when the Item the Torrent is for changes.
  - [1] 2026-11-25: rTorrent cannot download un-seeded Archive torrents | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Some BitTorrent clients (e.g. rTorrent) do not support Getright-style webseeding, and will not be able to download un-seeded Internet Archive Torrents.
  - [1] 2026-11-25: the Archive trackers track only the Archive's own torrents | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Our trackers are closed (they track our only own torrents).
  - [1] 2026-11-25: the interface is the BitTorrent protocol, which the interface vocabulary has no term for | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
  - [1] 2026-11-25: the Archive runs the trackers bt1 and bt2 | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Yes, Internet Archive torrents are tracked by bt1.archive.org and bt2.archive.org.
  - [1] 2026-11-25: the Archive runs trackers bt1 and bt2 | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Yes, Internet Archive torrents are tracked by bt1.archive.org and bt2.archive.org.
  - [2] 2026-11-25: uploading requires a free archive.org account | capture: sha256:2af054d55dffcd44c8d0693ae3231334ab0a26da635bddc2219a2aa78c8b5d20 | quote: You will need a to register for a free account on archive.org before you can upload.
  - [1] 2026-11-25: over 1.4 million items and almost a petabyte are available via BitTorrent | capture: sha256:cc6a906364f23e9fd29b16b5f325e7ad23486064254d36fb28445c8316116afd | quote: Currently over 1.4 million Archive Items are available via the BitTorrent protocol, comprising almost a petabyte of public domain materials.
- sources:
  - [1] https://help.archive.org/help/archive-bittorrents/
  - [2] https://help.archive.org/help/uploading-a-basic-guide/
