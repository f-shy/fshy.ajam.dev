# 小乐的网盘

> xiaole88.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xiaole88/ | JSON https://fshy.ajam.dev/api/v1/entity/xiaole88.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 小乐的网盘

- `netdisk-pan/share-xiaole88-com` | dead | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:35.336Z (live) | stale on 2026-12-17
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
  - write_capability: unverified: no write operation was probed; the anonymous guest role is disabled
  - upstream_provider: Onedrive
  - fronting_cdn: tengine
  - advertised_write_flag: no
  - permission_bitmask: 2
  - base_path: /
  - listing_sha256: 91421213
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T01:38:35.273Z
  - last_verified_dead: 2026-11-25T02:34:42.594Z
  - consecutive_failures: 2
  - aliases: 小乐的网盘 (share.xiaole88.com) — public AList, Android TV software
- evidence:
  - probe:https://share.xiaole88.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '小乐的网盘'
  - probe:https://share.xiaole88.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 15 root entries; write:false, write_content_bypass:None, provider:Onedrive
  - probe:https://share.xiaole88.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55 | quote: "checked_at": "2026-11-11T00:20:12.827Z"
  - probe:https://share.xiaole88.com/ 2026-11-11:  | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55
  - probe:https://share.xiaole88.com/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55
  - probe:https://share.xiaole88.com/ 2026-11-11: the anonymous guest session answered and its root listing returned entries, so the instance is reachable without an account | capture: sha256:638022072ba8e93f123df546984b4dbf180bf0fc9bd486fa7ab03b09dcc4ae55 | quote: "alive": true
  - probe:https://share.xiaole88.com/ 2026-11-19: this run's probes disagreed: one returned the full mount list and others returned proxy tunnel 502 errors, so the host is flapping | capture: sha256:afdbfe17288b5253e0f2850d6f4a71ceecaebfacd1cf207eabd1294966c21526 | quote: "consecutive_failures": 1
  - probe:https://share.xiaole88.com/ 2026-11-19: the successful mount-list probe returned the recorded hash 91421213, so the listing itself is unchanged | capture: sha256:afdbfe17288b5253e0f2850d6f4a71ceecaebfacd1cf207eabd1294966c21526 | quote: "listing_sha256": "91421213"
  - probe:https://share.xiaole88.com/ 2026-11-19: the successful mount-list probe that returned 15 entries was taken at this instant | capture: sha256:afdbfe17288b5253e0f2850d6f4a71ceecaebfacd1cf207eabd1294966c21526 | quote: "checked_at": "2026-11-19T03:44:11.619Z"
  - probe:https://share.xiaole88.com/ 2026-11-25: a second consecutive probe found no anonymous mount list at this host | capture: sha256:1c6d657e4320768e37f50a36cbf191ad277393b2730d233ceb4565f5b35c09c0 | quote: "consecutive_failures": 2
  - probe:https://share.xiaole88.com/ 2026-11-25: the fresh probe found no anonymous settings, guest session or root mount list at this host | capture: sha256:1c6d657e4320768e37f50a36cbf191ad277393b2730d233ceb4565f5b35c09c0 | quote: "alive": false
  - probe:https://share.xiaole88.com/ 2026-11-25: the failed re-probe was checked at this instant | capture: sha256:1c6d657e4320768e37f50a36cbf191ad277393b2730d233ceb4565f5b35c09c0 | quote: "checked_at": "2026-11-25T02:34:42.594Z"
  - probe:https://share.xiaole88.com/ 2026-11-25: the probe checked the host settings at this instant | capture: sha256:6f952befdbee3652cda735ea5f58022ed8bb26e50e64d52ef3c5978ca897bcae | quote: "checked_at": "2026-11-25T01:38:35.273Z"
  - probe:https://share.xiaole88.com/ 2026-11-25: an anonymous mount-list request was refused because the guest role is disabled | capture: sha256:166de745b7aca2f94e51d94467691f572fa6a224046023b06119623e360b7eeb | quote: "list_error": "Guest user is disabled, login please"
  - [2] 2026-11-25: the settings response reports that registration is disabled | capture: sha256:01ac03f482a50b2a8060c7f6b72d63c262106855c97890f9044626e18c433126 | quote: "allow_register":"false"
  - probe:https://share.xiaole88.com/api/fs/list 2026-11-25: the anonymous list request returned code 401 because the guest role is disabled, so no write result was measured | capture: sha256:9ac1df64f3a61ca56d4384704c80aa707435ba54e52315978b5aefaf0b3ab75c | quote: "message":"Guest user is disabled, login please"
- sources:
  - [1] https://share.xiaole88.com/
  - [2] https://share.xiaole88.com/api/public/settings
