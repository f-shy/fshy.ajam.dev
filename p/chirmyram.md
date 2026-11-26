# OpenList

> chirmyram.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chirmyram/ | JSON https://fshy.ajam.dev/api/v1/entity/chirmyram.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenList

- `netdisk-pan/al-chirmyram-com` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:08:33.682Z (live) | stale on 2026-12-17
- url https://al.chirmyram.com/
- free tier: anonymous guest read of 9 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): no published rate; one operator and a CDN front absorb the read [1]
  - write-gated: PUT denied at the guest role probe:https://al.chirmyram.com/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier A read-only corpus, so there is no multiplication. Useful as a fetch mirror and as the reference implementation of publishing guest credentials and putting Cloudflare in front, which is the transferable part
- reliability: The reference reader. A 7.43 TiB book and comic corpus, Cloudflare-fronted, and a 36,747,196-byte PDF read back at 206 with cf-cache-status HIT. The upstream is a SharePoint tenant, which is why single files reach tens of GiB.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: unknown
  - fronting_cdn: cloudflare
  - advertised_write_flag: yes
  - write_content_bypass: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 0f64ec2f
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T04:07:25.905Z
  - consecutive_failures: 0
  - aliases: 七米蓝仓库 (al.chirmyram.com) — public AList instance, read-only, WebDAV + CF cache HIT
  - largest_listed_directory_bytes: 4058674141521
  - cf_cache_hit: yes
  - guest_credentials: alist:alist
- evidence:
  - probe:https://al.chirmyram.com/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'OpenList'
  - probe:https://al.chirmyram.com/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 9 root entries; write:true, write_content_bypass:False, provider:unknown
  - probe:https://al.chirmyram.com/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://al.chirmyram.com/ 2026-11-11:  | capture: sha256:05b13f5d8a1e09768467258892fbb58c5a5ffb46627813e1763eebeb3dc405ff
  - probe:https://al.chirmyram.com/ 2026-11-11:  | capture: sha256:05b13f5d8a1e09768467258892fbb58c5a5ffb46627813e1763eebeb3dc405ff | quote: "checked_at": "2026-11-11T00:20:01.880Z"
  - probe:https://al.chirmyram.com/ 2026-11-19: the liveness and mount-list probe checked this host at this instant | capture: sha256:f21490628c00c80ce1efcc9e0ceaaa4a9484502f946afa592ef5fc49c8745d19 | quote: "checked_at": "2026-11-19T03:30:55.794Z"
  - probe:https://al.chirmyram.com/ 2026-11-19: the host answered every request of this probe, so the failure count stayed at zero | capture: sha256:f21490628c00c80ce1efcc9e0ceaaa4a9484502f946afa592ef5fc49c8745d19
  - probe:https://al.chirmyram.com/api/public/settings 2026-11-25: a fresh anonymous probe of the AList public settings endpoint of al.chirmyram.com answered at this instant (HTTP 200, JSON, no challenge) | capture: sha256:2fb539aed2c1e1af4f487905b8a83c1c4958442f3be7bb1f6b8c695822daa59b | quote: "probed_at": "2026-11-25T04:07:25.905Z"
  - probe:https://al.chirmyram.com/api/public/settings 2026-11-25: the settings endpoint of al.chirmyram.com answered HTTP 200 to an anonymous request | capture: sha256:2fb539aed2c1e1af4f487905b8a83c1c4958442f3be7bb1f6b8c695822daa59b | quote: "status": 200
  - probe:https://al.chirmyram.com/ 2026-11-25: the fresh anonymous root listing hashed to the recorded value, so the listing is unchanged | capture: sha256:6a51e8585e3a3425ae63166b01ceea71212d586eb453b22ecf2b78fb475888f1 | quote: "listing_sha256": "0f64ec2f"
  - probe:https://al.chirmyram.com/ 2026-11-25: the re-probe of this host was taken at this instant | capture: sha256:cda7ac2cd47b715e96743c52267f26d2f0617deb5d956a643a1129114ec8d38d | quote: "checked_at": "2026-11-25T01:38:28.678Z"
  - probe:https://al.chirmyram.com/ 2026-11-25: the anonymous session, settings and root listing all answered, so no consecutive failure | capture: sha256:cda7ac2cd47b715e96743c52267f26d2f0617deb5d956a643a1129114ec8d38d | quote: "alive": true
  - probe:https://al.chirmyram.com/ 2026-11-25: the anonymous root listing still hashes to 0f64ec2f with 9 entries | capture: sha256:cda7ac2cd47b715e96743c52267f26d2f0617deb5d956a643a1129114ec8d38d | quote: "guest": true, ... "root_entries": 9, ... "listing_sha256": "0f64ec2f"
- sources:
  - [1] https://al.chirmyram.com/
