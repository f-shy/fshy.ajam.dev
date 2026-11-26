# mmpan.net

> mmpan.net | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mmpan/ | JSON https://fshy.ajam.dev/api/v1/entity/mmpan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mmpan.net

- `netdisk-pan/mmpan-net` | dead | evidence measured | binding write-gated | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:15:14.533Z (live) | stale on 2026-12-18
- url https://mmpan.net/
- free tier: anonymous guest read of 0 root entries; no account and no payment | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: source: [1]
- retention: source: [1]
- egress: served through cloudflare; the reader pays nothing | metered: no | source: [1]
- identity: anonymous
- interface: rest, webdav
- limits:
  - write-gated (binding): no write offered probe:https://mmpan.net/api/fs/put
- interface detail: rest
- composes with: a fetch substrate: point a cache and two mirrors at it, never a write tier
- reliability: Answers the AList API and returns HTTP 200 on /api/fs/list with no usable body, so there is nothing to read.
- notes: the same as reliability
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - fronting_cdn: cloudflare
  - advertised_write_flag: no
  - write_content_bypass: absent
  - base_path: /
  - first_seen: 2024-01-20
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
- evidence:
  - probe:https://mmpan.net/api/public/settings 2026-10-22: HTTP 200, JSON carrying a code field, site_title '?'
  - probe:https://mmpan.net/api/fs/list 2026-11-19: the /api/fs/list endpoint still returns the SPA HTML shell rather than a JSON listing, so the API read path yields no usable body | capture: sha256:a48204b1515b162463494b75d0bef474cbc92da9c6b1340f23124240420ea0a6 | quote: <meta name="generator" content="Alist V2" />
  - [2] 2026-11-26: the first-party API response headers carry server: cloudflare | capture: sha256:27893e5f5c807272c4d0726f926d864c382935284646b2eeea591cdb4255408b | quote: server: cloudflare
- sources:
  - [1] https://mmpan.net/
  - [2] https://mmpan.net/api/public/settings
