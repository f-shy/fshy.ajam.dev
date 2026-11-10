# fileditch old

> fileditch.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fileditch/ | JSON https://fshy.ajam.dev/api/v1/entity/fileditch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileDitch (new.fileditch.com)

- `storage/fileditch` | fails-egress | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://new.fileditch.com
- free tier: No total storage quota stated; uploader accepts an unbounded number of files. Live uploader JS caps a single file at 155 GiB (constant MAXB = 155*1024*1024*1024, error string 'files over 150 GB are not allowed'). | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 150 GB per file | bytes: 150000000000 | source: [1] | note: not stated
- retention: Extension blocklist is broad (php, html, js, exe, dll, apk, sh, py, xml, svg, iso-adjacent script types). .bin/.parquet/.npy/.zip/.7z are fine. Retention: indefinite while accessed; only 45+ day untouched files are reclaim candidates. | source: [1] | note: not stated
- egress: Unmetered direct download links, no bandwidth product at all. No paid tier is sold, so there is no egress meter to trip. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 150 GB per file [1]
- limits note: 155 GiB / 150 GB per file (live JS constant). 128 MiB chunks, 6 parallel. Extension blocklist is broad (php, html, js, exe, dll, apk, sh, py, xml, svg, iso-adjacent script types). .bin/.parquet/.npy/.zip/.7z are fine. Retention: indefinite while accessed; only 45+ day untouched files are reclaim candidates.
- interface detail: rest
- tooling: chunked.php REST protocol, fully scriptable and keyless: POST ?action=init&filename=&size= -> {id, chunk_size}, POST ?action=chunk&id=&i= with raw body, POST ?action=finish&id= -> {url}. 128 MiB chunks, PARALLEL=6 in the shipped client.
- composes with: Account-less upload breaks the per-account quota model entirely: every file is independent, so chain = unlimited files x 155 GiB. Only per-IP rate limits and the retention clock bind.
- reliability: Upload path works headlessly today; download path is Cloudflare-Turnstile gated (403 cf-mitigated: challenge on the itsfileditchfiles.st host even with Range + browser UA), so a non-browser client can write but not read.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No total storage quota stated; uploader accepts an unbounded number of files. Live uploader JS caps a single file at 155 GiB (constant MAXB = 155*1024*1024*1024, error string 'files over 150 GB are not allowed').
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: live JS: const MAXB = 155*1024*1024*1024 and errItem 'files over 150 GB are not allowed'
  - withheld 2026-10-21: probe: POST chunked.php?action=init&filename=probe.bin&size=1048576 -> 200 {"success":true,"id":"a54f...","chunk_size":134217728,"total_chunks":1}
  - [2] 2026-10-21: probe: chunk upload -> 200 {"success":true,"i":0}; finish -> 200 {"url":"","size":1048576}
  - withheld 2026-10-21: probe: GET that URL -> 403 Cf-Mitigated: challenge (Cloudflare Turnstile), 5669 bytes of challenge HTML
- sources:
  - [1] https://new.fileditch.com/
  - [2] https://itsfileditchfiles.st/charlie48/.../probe.bin

## fileditch old domain (fileditch.com)

- `storage/fileditch-old-domain` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://fileditch.com/
- free tier: none reachable: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale.
  - [2] 2026-10-21: cited as the basis of the rejection: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale.
- sources:
  - [1] https://fileditch.com/
  - [2] https://new.fileditch.com
