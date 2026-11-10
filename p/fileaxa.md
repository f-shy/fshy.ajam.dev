# FileAxa

> fileaxa.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fileaxa/ | JSON https://fshy.ajam.dev/api/v1/entity/fileaxa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileAxa

- `storage/fileaxa` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://fileaxa.com
- free tier: Free registered: 488 GB storage, 10,000 Mb (10 GB) per file; free (unregistered) row has no storage pool | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB/file | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: capped: free registered 5 GB/day download volume; Premium 60 GB/day, Premium Pro 120 GB/day | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-ip-shaping: 5 GB/day [1]
  - per-object-cap (binding): 10 GB/file [1]
- limits note: 10 GB/file; 5 GB/day egress on free; 488 GB pool; anonymous uploads are disabled by the platform ('uploads are not enabled for your account type')
- interface detail: rest
- tooling: XFileSharing Pro; API key endpoint live at /api/upload/server (returns {"status":400,"msg":"Invalid key"} without one); PolyUploader covers it
- composes with: 488 GB per free registration x N registrations; family partners combine into TBs (UpZur 1,953 GB + FileAxa 488 GB + Mega4up 183 GB = 2.6 TB across three signups)
- reliability: registration page returns 403 to automated clients (human-verification step gate) and anonymous uploads are refused outright, so the quota is only reachable with a scripted/manual signup
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free registered: 488 GB storage, 10,000 Mb (10 GB) per file; free (unregistered) row has no storage pool
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: 10000 Mb max upload, storage '—'; Registered: 10000 Mb, 488 GB, 5 GB/day download
  - [2] 2026-10-21: probe: GET -> 200 {"status":400,"msg":"Invalid key"} (API exists, key-gated)
  - [3] 2026-10-21: probe: POST utype=anon -> [{"file_code":"undef","file_status":"uploads are not enabled for your account type"}]
- sources:
  - [1] https://fileaxa.com/premium.html
  - [2] https://fileaxa.com/api/upload/server?utype=anon
  - [3] https://s31.fileaxa.com/cgi-bin/upload.cgi
