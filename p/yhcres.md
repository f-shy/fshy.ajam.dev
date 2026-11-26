# 萤火虫资源站

> yhcres.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yhcres/ | JSON https://fshy.ajam.dev/api/v1/entity/yhcres.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 萤火虫资源站

- `netdisk-pan/www-yhcres-top` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:35.337Z (live) | stale on 2026-12-17
- url https://www.yhcres.top/
- free tier: anonymous guest read of 13 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://www.yhcres.top/api/fs/put
- interface detail: rest
- composes with: Read-only retrieval target for specialized router firmware downloads. Functions as an external read repository rather than writable application storage.
- reliability: 13 root entries on OpenList v4.2.7, base_path /public, write:true advertised and denied. An Android-flashing resource site.
- notes: anonymous POST /api/fs/list on / returned code 200 with 13 root entries (listing sha256 296e8611)
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: cloudflare
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 0
  - base_path: /public
  - listing_sha256: 296e8611
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T02:34:43.781Z
  - consecutive_failures: 0
  - aliases: 萤火虫资源站 (www.yhcres.top) — public AList, Android flashing/repair corpus
  - allow_indexed: yes
- evidence:
  - probe:https://www.yhcres.top/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '萤火虫资源站'
  - probe:https://www.yhcres.top/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 13 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://www.yhcres.top/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://www.yhcres.top/ 2026-11-11: the fs/list response carries this error text | capture: sha256:ecf4cb16608c9a4d44e133cfdc356fffaaf49ce50131b6f0201c01704a8a5c90 | quote: "list_failure": "failed get objs: failed get dir: failed to get obj: object not found"
  - probe:https://www.yhcres.top/ 2026-11-11: this run's probe found no listing, so the count is one | capture: sha256:ecf4cb16608c9a4d44e133cfdc356fffaaf49ce50131b6f0201c01704a8a5c90 | quote: "consecutive_failures": 1
  - probe:https://www.yhcres.top/ 2026-11-11: the settings endpoint answered HTTP 200 while the listing did not | capture: sha256:ecf4cb16608c9a4d44e133cfdc356fffaaf49ce50131b6f0201c01704a8a5c90 | quote: "status": 200
  - probe:https://www.yhcres.top/ 2026-11-11:  | capture: sha256:1a815a21d5604d0483979a95c1d5b400c9d7cf8149b172e660661ebcae059f9d | quote: "checked_at": "2026-11-11T01:56:23.251Z"
  - probe:https://www.yhcres.top/ 2026-11-11:  | capture: sha256:1a815a21d5604d0483979a95c1d5b400c9d7cf8149b172e660661ebcae059f9d
  - probe:https://www.yhcres.top/ 2026-11-11: the root listing answered with this entry count and hash | capture: sha256:1a815a21d5604d0483979a95c1d5b400c9d7cf8149b172e660661ebcae059f9d | quote: "listing_note": "anonymous POST /api/fs/list on / returned code 200 with 13 root entries (listing sha256 296e8611)"
  - probe:https://www.yhcres.top/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:1a815a21d5604d0483979a95c1d5b400c9d7cf8149b172e660661ebcae059f9d
  - probe:https://www.yhcres.top/ 2026-11-19: the liveness and mount-list probe checked this host at this instant | capture: sha256:92ffc27f8b73e911752b77300c698ba17f29011814eec0e3fb8db6bdb351dc9a | quote: "checked_at": "2026-11-19T03:43:00.527Z"
  - probe:https://www.yhcres.top/ 2026-11-19: the root listing hashed to the recorded 296e8611 on both runs and the host answered every request | capture: sha256:92ffc27f8b73e911752b77300c698ba17f29011814eec0e3fb8db6bdb351dc9a | quote: "listing_sha256": "296e8611"..."consecutive_failures": 0
  - probe:https://www.yhcres.top/ 2026-11-25: a fresh anonymous probe of www.yhcres.top answered the settings, guest session and mount-list requests at this timestamp | capture: sha256:f3846125b7bd8b2637ae86dbccc0400b91f41682b6bf19864d00cd68c2c90850 | quote: "probed_at": "2026-11-25T02:34:43.781Z"
  - probe:https://www.yhcres.top/ 2026-11-25: the fresh probe completed the anonymous settings, guest session and root mount list, so the new liveness timestamp stands | capture: sha256:f3846125b7bd8b2637ae86dbccc0400b91f41682b6bf19864d00cd68c2c90850 | quote: "alive": true
  - probe:https://www.yhcres.top/ 2026-11-25: the fresh anonymous root listing hashed to the stored value, so the listing is unchanged | capture: sha256:f3846125b7bd8b2637ae86dbccc0400b91f41682b6bf19864d00cd68c2c90850 | quote: "listing_sha256": "296e8611"
  - probe:https://www.yhcres.top/ 2026-11-25: the liveness and mount-list probe checked this host at this instant | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "checked_at": "2026-11-25T01:38:35.555Z"
  - probe:https://www.yhcres.top/ 2026-11-25: the anonymous session reported this base path | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "base_path": "/public"
  - probe:https://www.yhcres.top/ 2026-11-25: the settings response advertised this write flag | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "write_advertised": true
  - probe:https://www.yhcres.top/ 2026-11-25: the probe measured this write-content-bypass flag | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "write_content_bypass": false
  - probe:https://www.yhcres.top/ 2026-11-25: the settings response reported this upstream provider | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "provider": "unknown"
  - probe:https://www.yhcres.top/ 2026-11-25: the probe obtained a guest session without an account | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "guest": true
  - probe:https://www.yhcres.top/ 2026-11-25: the anonymous session reported this permission bitmask | capture: sha256:acaf7be7fa68ba450ddd1c9ce5f05908299726a186e4a74ee73b18231ec7a343 | quote: "permission": 0
- sources:
  - [1] https://www.yhcres.top/
