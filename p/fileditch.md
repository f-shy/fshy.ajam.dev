# fileditch old

> fileditch.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fileditch/ | JSON https://fshy.ajam.dev/api/v1/entity/fileditch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileDitch (new.fileditch.com)

- `storage/fileditch` | fails-egress | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.375Z (live) | stale on 2026-12-04
- url https://new.fileditch.com
- free tier: No total storage quota stated; uploader accepts an unbounded number of files. Live uploader JS caps a single file at 155 GiB (constant MAXB = 155*1024*1024*1024, error string 'files over 150 GB are not allowed'). | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 150 GB per file | bytes: 150000000000 | source: [1] | note: not stated
- retention: Files stay online as long as they're being accessed. Only files untouched for 45+ days are ever deleted — and only when we need the space. A broad extension blocklist (php, html, js, exe, dll, apk, sh, py, xml, svg and script types) was recorded previously but is not stated on the page read. | source: [1] | note: not stated
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
  - [1] 2026-11-19: the first-party uploader states a 150 GB per-file cap and a no-account dump host | capture: sha256:87b4cb676833bcc5bd5af0590f1dc207d3eb5ff48e4f1dd68a142aefe91faa4f | quote: or click to browse — up to 150 GB per file
  - [1] 2026-11-19: the first-party page states the retention rule of indefinite while accessed with 45+ day untouched files eligible for deletion | capture: sha256:87b4cb676833bcc5bd5af0590f1dc207d3eb5ff48e4f1dd68a142aefe91faa4f | quote: Files stay online as long as they're being accessed. Only files untouched for 45+ days are ever deleted — and only when we need the space.
- sources:
  - [1] https://new.fileditch.com/
  - [2] https://itsfileditchfiles.st/charlie48/.../probe.bin

## fileditch old domain (fileditch.com)

- `storage/fileditch-old-domain` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.563Z (live) | stale on 2026-12-04
- url https://fileditch.com/
- free tier: none reachable: the root fileditch.com domain serves a first-party notice about a forum blacklist with a link to new.fileditch.com; the upload form and its limits (up to 150 GB per file) live on the new host, so figures quoted from the old domain are stale. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The root fileditch.com domain serves a first-party notice page linking to new.fileditch.com, where the upload form and limits live; the notice also states files stay online while accessed and that only files untouched for 45+ days are deleted when space is needed.
- notes: The root fileditch.com domain serves a first-party notice page linking to new.fileditch.com, where the upload form and its limits live.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale.
  - [2] 2026-10-21: cited as the basis of the rejection: Root domain is now only a meta-refresh stub to new.fileditch.com; all real limits/API live on the new host, so any blog citing fileditch.com figures is stale.
  - [1] 2026-11-19: the old fileditch.com domain still serves a first-party notice page, not a hosted offer | capture: sha256:87b4cb676833bcc5bd5af0590f1dc207d3eb5ff48e4f1dd68a142aefe91faa4f | quote: ⚠️ SimpCity has blacklisted FileDitch
  - [1] 2026-11-19: the first-party notice page carries an upload form on the new host with a 150 GB per-file limit | capture: sha256:87b4cb676833bcc5bd5af0590f1dc207d3eb5ff48e4f1dd68a142aefe91faa4f | quote: up to 150 GB per file
  - [1] 2026-11-19: the first-party notice page describes a 45+ day inactivity retention rule | capture: sha256:87b4cb676833bcc5bd5af0590f1dc207d3eb5ff48e4f1dd68a142aefe91faa4f | quote: Only files untouched for 45+ days are ever deleted
  - [1] 2026-11-19: the old domain serves a notice, not a hosted storage offer | capture: sha256:87b4cb676833bcc5bd5af0590f1dc207d3eb5ff48e4f1dd68a142aefe91faa4f | quote: ⚠️ SimpCity has blacklisted FileDitch
- sources:
  - [1] https://fileditch.com/
  - [2] https://new.fileditch.com
