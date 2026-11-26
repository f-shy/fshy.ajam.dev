# Kho Nhà Tôm ✨

> t0m.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t0m/ | JSON https://fshy.ajam.dev/api/v1/entity/t0m.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kho Nhà Tôm ✨

- `netdisk-pan/kho-t0m-top` | qualifies-with-caveat | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:33.832Z (live) | stale on 2026-12-17
- url https://kho.t0m.top/
- free tier: anonymous guest read of 4 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): PUT denied at the guest role probe:https://kho.t0m.top/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: 4 root entries, provider Local, AList v3.42.0, Cloudflare-fronted. A Vietnamese-language instance.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: full
  - write_capability: permission-denied
  - upstream_provider: Local
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - permission_bitmask: 0
  - base_path: /
  - listing_sha256: 6d034603
  - first_seen: 2024-01-20
  - last_verified_alive: 2026-11-25T02:34:34.248Z
  - consecutive_failures: 0
- evidence:
  - probe:https://kho.t0m.top/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title 'Kho Nhà Tôm ✨'
  - probe:https://kho.t0m.top/api/fs/list 2026-10-22: anonymous POST /api/fs/list on / returned code 200 with 4 root entries; write:false, write_content_bypass:None, provider:Local
  - probe:https://kho.t0m.top/api/fs/put 2026-10-22: the zero-byte oracle (PUT at an existing directory with Overwrite:false) returned code 403 with message 'permission denied' inside HTTP 200, so the write permission failed and nothing was written
  - probe:https://kho.t0m.top/ 2026-11-11:  | capture: sha256:7b0970459ce47dcf17cc44940fd5ff9f74daff4e12f1bf4827046731eba0ba12
  - probe:https://kho.t0m.top/ 2026-11-11: this host answered every request of this run's probe | capture: sha256:7b0970459ce47dcf17cc44940fd5ff9f74daff4e12f1bf4827046731eba0ba12
  - probe:https://kho.t0m.top/ 2026-11-11:  | capture: sha256:7b0970459ce47dcf17cc44940fd5ff9f74daff4e12f1bf4827046731eba0ba12 | quote: "checked_at": "2026-11-11T00:20:04.595Z"
  - probe:https://kho.t0m.top/ 2026-11-11: the anonymous root listing hashed to this value | capture: sha256:7b0970459ce47dcf17cc44940fd5ff9f74daff4e12f1bf4827046731eba0ba12 | quote: "listing_sha256": "a773ffd4"
  - probe:https://kho.t0m.top/ 2026-11-19:  | capture: sha256:71aeb49dd40608df170a4f1fc06c3091c090cfc313b2315b96bfc85e8eb3aef5 | quote: "checked_at": "2026-11-19T03:34:17.135Z"
  - probe:https://kho.t0m.top/ 2026-11-19: the host answered, its listing hash is now 6d034603, and there were no failures | capture: sha256:71aeb49dd40608df170a4f1fc06c3091c090cfc313b2315b96bfc85e8eb3aef5 | quote: "checked_at": "2026-11-19T03:34:17.135Z"..."listing_sha256": "6d034603"..."consecutive_failures": 0
  - probe:https://kho.t0m.top/ 2026-11-25: a fresh anonymous probe of kho.t0m.top answered the settings, session and mount-list requests at this timestamp | capture: sha256:5b30e948c46a2cce7bced08f353170a80e6826b08237912fbc1f40bc9b541bb7 | quote: "probed_at": "2026-11-25T02:34:34.248Z"
  - probe:https://kho.t0m.top/ 2026-11-25: the fresh probe completed the anonymous settings, session and mount-list requests at kho.t0m.top | capture: sha256:5b30e948c46a2cce7bced08f353170a80e6826b08237912fbc1f40bc9b541bb7 | quote: "alive": true
  - probe:https://kho.t0m.top/ 2026-11-25: the fresh anonymous root listing of kho.t0m.top hashed to the recorded value, so the listing is unchanged | capture: sha256:5b30e948c46a2cce7bced08f353170a80e6826b08237912fbc1f40bc9b541bb7 | quote: "listing_sha256": "6d034603"
  - probe:https://kho.t0m.top/ 2026-11-25: the re-probe of this host was taken at this instant | capture: sha256:dc851be5a060087a8be9dcf30c1bb49e8e11cc212bf59a1585bceec0fa39368b | quote: "checked_at": "2026-11-25T01:38:28.703Z"
  - probe:https://kho.t0m.top/ 2026-11-25: the anonymous root listing still hashes to 6d034603 with 6 entries | capture: sha256:dc851be5a060087a8be9dcf30c1bb49e8e11cc212bf59a1585bceec0fa39368b | quote: "guest": true ... "root_entries": 6 ... "listing_sha256": "6d034603"
  - probe:https://kho.t0m.top/ 2026-11-25: the re-probe answered as an anonymous guest, so registration is not needed | capture: sha256:dc851be5a060087a8be9dcf30c1bb49e8e11cc212bf59a1585bceec0fa39368b | quote: "guest": true
- sources:
  - [1] https://kho.t0m.top/
