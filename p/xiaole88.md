# 小乐的网盘

> xiaole88.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xiaole88/ | JSON https://fshy.ajam.dev/api/v1/entity/xiaole88.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 小乐的网盘

- `netdisk-pan/share-xiaole88-com` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:08.145Z (live) | stale on 2026-12-11
- url https://share.xiaole88.com/
- free tier: anonymous guest read of 15 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through Tengine; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://share.xiaole88.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier Read-only. Useful as an Android TV software mirror and not as capacity
- reliability: 15 root entries, provider Onedrive, on AList v3.40 behind Tengine. A pooled-tenant export like al.chirmyram.com but without Cloudflare in front, so no edge cache.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: Onedrive
  - fronting_cdn: tengine
  - advertised_write_flag: no
  - permission_bitmask: 2
  - base_path: /
  - listing_sha256: 91421213
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-19T03:44:11.619Z
  - consecutive_failures: 1
  - aliases: 小乐的网盘 (share.xiaole88.com) — public AList, Android TV software
- evidence:
  - probe:https://share.xiaole88.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '小乐的网盘'
  - probe:https://share.xiaole88.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 15 root entries; write:false, write_content_bypass:None, provider:Onedrive
  - probe:https://share.xiaole88.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55 | quote: "checked_at": "2026-11-11T00:20:12.827Z"
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55 | quote: "listing_sha256": "91421213"
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55 | quote: "alive": true
  - probe:https://share.xiaole88.com/ 2026-11-19: this run's probes disagreed: one returned the full mount list and others returned proxy tunnel 502 errors, so the host is flapping | capture: sha256:afdbfe17288b5253e0f2850d6f4a71ceecaebfacd1cf207eabd1294966c21526 | quote: "consecutive_failures": 1
  - probe:https://share.xiaole88.com/ 2026-11-19: the successful mount-list probe returned the recorded hash 91421213, so the listing itself is unchanged | capture: sha256:afdbfe17288b5253e0f2850d6f4a71ceecaebfacd1cf207eabd1294966c21526 | quote: "listing_sha256": "91421213"
  - probe:https://share.xiaole88.com/ 2026-11-19: the successful mount-list probe that returned 15 entries was taken at this instant | capture: sha256:afdbfe17288b5253e0f2850d6f4a71ceecaebfacd1cf207eabd1294966c21526 | quote: "checked_at": "2026-11-19T03:44:11.619Z"
- sources:
  - [1] https://share.xiaole88.com/
