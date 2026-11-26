# 延时の奇妙网盘

> yanshiqwq.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yanshiqwq/ | JSON https://fshy.ajam.dev/api/v1/entity/yanshiqwq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 延时の奇妙网盘 (data.yanshiqwq.cn)

- `netdisk-pan/data-yanshiqwq-cn` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:33.830Z (live) | stale on 2026-12-17
- url https://data.yanshiqwq.cn/
- free tier: anonymous guest read of the whole mount list, and a write on one path; no account, no payment, no published quota | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: Between 100 MiB and 110 MiB based on HTTP 413 responses from the fronting CDN. No official cap is published. | source: [1]
- retention: until the operator's disk or Cloudflare account fails; no TTL, no SLA, no notice | source: [1]
- egress: served through Cloudflare; the reader pays nothing and the operator pays nothing per byte | metered: no | source: [1]
- identity: anonymous | detail: no registration, no token, no cookie; /api/me returns a guest session with role 1 and permission 256
- interface: rest, webdav
- limits:
  - write-gated (binding): Writable on the guest path only. Calling /api/fs/remove returns HTTP 403, preventing deletion of uploaded files. probe:https://data.yanshiqwq.cn/api/fs/remove
  - per-object-cap: HTTP 413 from fronting CDN between 100 MiB and 110 MiB
  - per-ip-shaping: ~1.9 MB/s up, ~1.0 MB/s down on a home uplink
- binding note: The write is real but undeletable, capped by the CDN body limit, and rate-limited by one home uplink, so the binding constraint is the gate on writing at all, not a quota.
- interface detail: rest
- endpoint: https://data.yanshiqwq.cn/api/fs/put
- tooling: OpenList v4.2.7 REST (/api/fs/*) and its WebDAV endpoint; rclone's alist backend speaks the same REST
- composes with: the only verified write in 170 hosts: a 4 KiB PUT, a GET, and a SHA-256 match. Useful as a one-object staging area, not as capacity. One instance on one operator's disk, so a second account carries no second allowance here.
- reliability: One volunteer's home disk behind Cloudflare. No quota, no SLA, no delete, and the bytes are world-listable once written.
- notes: The only host of 170 that accepted a write and gave the bytes back. It passes the zero-byte oracle with 'file exists', reports permission 256 with no bit 3, and is writable only because a per-path meta overrides the role. Probes left 32-byte files named *-r6probe.bin in its root, because delete is denied.
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: verified
  - upstream_provider: unknown
  - fronting_cdn: cloudflare
  - advertised_write_flag: yes
  - first_seen: 2026-10-21
  - last_verified_alive: 2026-11-25T02:34:33.368Z
  - permission_bitmask: 256
  - bit3_upload: no
  - write_content_bypass: yes
  - listing_sha256: 8b066b5f
  - observations[0].at: 2026-10-21T00:00:00Z
  - observations[0].state: listed
  - observations[0].writable: yes
  - observations[1].at: 2026-10-22T03:21:00Z
  - observations[1].state: listed
  - observations[1].entries: 27
  - observations[1].writable: yes
  - observations[2].at: 2026-10-22T03:37:00.574Z
  - observations[2].state: listed
  - observations[2].entries: 27
  - observations[2].writable: yes
  - aliases: 延时の奇妙网盘 (data.yanshiqwq.cn) — public OpenList instance, WRITABLE
  - consecutive_failures: 0
- evidence:
  - probe:https://data.yanshiqwq.cn/api/fs/list 2026-10-22: HTTP 200, code 200, 27 root entries, write:true and write_content_bypass:true, provider:unknown
  - probe:https://data.yanshiqwq.cn/api/fs/put 2026-10-22: PUT of 32 bytes returned {"code":200,"message":"success"} and GET /p/ returned the same 32 bytes with a matching SHA-256
  - [2] 2026-10-22: OpenList v4.2.7, build 2026-10-15, allow_indexed false, allow_mounted false
  - probe:https://data.yanshiqwq.cn/api/me 2026-10-22: guest session, role 1, permission 256 = bit 8 (WebDAV read) only, with no bit 3; the write is granted by a per-path meta, not by the bitmask
  - probe:https://data.yanshiqwq.cn/ 2026-11-11:  | capture: sha256:9ee485117b1d2f478de46a5384c8bc90abd11bd30fbb0c5570b14eefb36c0b01
  - probe:https://data.yanshiqwq.cn/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:9ee485117b1d2f478de46a5384c8bc90abd11bd30fbb0c5570b14eefb36c0b01
  - probe:https://data.yanshiqwq.cn/ 2026-11-11:  | capture: sha256:9ee485117b1d2f478de46a5384c8bc90abd11bd30fbb0c5570b14eefb36c0b01 | quote: "checked_at": "2026-11-11T00:20:03.505Z"
  - probe:https://data.yanshiqwq.cn/ 2026-11-19:  | capture: sha256:2a7e7698870ff7e7ee52bd1f02c2de5f5751be8aa96a128a0e6c64cd5ee8d14b | quote: "checked_at": "2026-11-19T03:33:35.044Z"
  - probe:https://data.yanshiqwq.cn/ 2026-11-19: the host answered and its listing hash stayed 8b066b5f with no failures | capture: sha256:2a7e7698870ff7e7ee52bd1f02c2de5f5751be8aa96a128a0e6c64cd5ee8d14b | quote: "checked_at": "2026-11-19T03:33:35.044Z"..."listing_sha256": "8b066b5f"..."consecutive_failures": 0
  - probe:https://data.yanshiqwq.cn/ 2026-11-25: a fresh anonymous probe of data.yanshiqwq.cn answered the settings, session and mount-list requests at this timestamp | capture: sha256:584efaf271c55279e30b70cebdf37d8e93a2fa5a309af4400008818a99cd43a7 | quote: "probed_at": "2026-11-25T02:34:33.368Z"
  - probe:https://data.yanshiqwq.cn/ 2026-11-25: the fresh probe completed the anonymous settings, session and mount-list requests at data.yanshiqwq.cn | capture: sha256:584efaf271c55279e30b70cebdf37d8e93a2fa5a309af4400008818a99cd43a7 | quote: "alive": true
  - probe:https://data.yanshiqwq.cn/ 2026-11-25: the fresh anonymous root listing of data.yanshiqwq.cn hashed to the recorded value, so the listing is unchanged | capture: sha256:584efaf271c55279e30b70cebdf37d8e93a2fa5a309af4400008818a99cd43a7 | quote: "listing_sha256": "8b066b5f"
  - probe:https://data.yanshiqwq.cn/ 2026-11-25: the re-probe of this host was taken at this instant | capture: sha256:28cfc5baa1bed071ba6c2649f2fb0b55b710b011d2f8316e522728ff2afb288b | quote: "checked_at": "2026-11-25T01:38:28.687Z"
  - probe:https://data.yanshiqwq.cn/ 2026-11-25: the anonymous root listing still hashes to 8b066b5f with 5 entries | capture: sha256:28cfc5baa1bed071ba6c2649f2fb0b55b710b011d2f8316e522728ff2afb288b | quote: "guest": true ... "root_entries": 5 ... "listing_sha256": "8b066b5f"
  - probe:https://data.yanshiqwq.cn/ 2026-11-25: the re-probe answered as an anonymous guest, so registration is not needed | capture: sha256:28cfc5baa1bed071ba6c2649f2fb0b55b710b011d2f8316e522728ff2afb288b | quote: "guest": true
- sources:
  - [1] https://data.yanshiqwq.cn/
  - [2] https://data.yanshiqwq.cn/api/public/settings
