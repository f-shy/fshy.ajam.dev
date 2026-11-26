# tmpfiles.org

> tmpfiles.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tmpfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/tmpfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tmpfiles.org

- `storage/tmpfiles-org` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.437Z (live) | stale on 2026-12-04
- url https://tmpfiles.org
- free tier: no account; 100 MB per file | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered; byte path requires a signed token scraped from the landing page | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB per file [1]
  - per-object-cap (binding): 100 MB/file [1]
- limits note: 100 MB/file; expires in 60 minutes (page rendered 'File expires in 59 minutes'). 10-upload burst all 200.
- interface detail: rest
- tooling: POST /api/v1/upload -F file=@x -> JSON; then GET the /dl/<token>/<id>/<name> URL extracted from the HTML
- composes with: None. 1-hour retention, no accounts.
- reliability: Textbook trap candidate: the API's own returned URL does NOT serve bytes. You must make a second request, scrape a timestamp+hash-signed /dl/ URL, and use that — and the signature expires. Also the API host did not resolve on this machine's DNS (0.0.0.0 answer); needed --resolve. Many resolvers/ISPs sinkhole it.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no account; 100 MB per file
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: POST /api/v1/upload -> 200 {"url":"https://tmpfiles.org/wLA4MTMv84dY/probe.bin"}. GET that URL -> 200 but 2792 B text/html. GET /dl/<id>/<name> -> 200, 2792 B text/html. Only the SIGNED URL parsed out of that HTML (https://tmpfiles.org/dl/1792600426.d39cd846db4b4014/wLA4MTMv84dY/probe.bin) -> 200, 32768 B, sha256 MATCH.
- evidence:
  - withheld 2026-10-21: probe: POST /api/v1/upload -> 200 with /wLA4MTMv84dY/ URL; GET it -> 200 / 2792 B HTML, not the file
  - withheld 2026-10-21: probe: GET signed /dl/1792600426.d39cd846.../ URL -> 200 / 32768 B / sha256 match
  - [1] 2026-11-19: the landing page still states a 100 MB per-file upload cap | capture: sha256:56a2957126c6a8a48df5c9f4ade700e26d5fd84c5d4a9b14be6a5426143efb53 | quote: Upload Files (max 100 MB)
  - [1] 2026-11-19: the landing page states a 60-minute minimum deletion window, so retention is short-lived | capture: sha256:56a2957126c6a8a48df5c9f4ade700e26d5fd84c5d4a9b14be6a5426143efb53 | quote: All files are deleted after 60 minutes 6 hours 24 hours 48 hours
- sources:
  - [1] https://tmpfiles.org/

## tmpfiles.org via normal dns

- `storage/tmpfiles-org-via-normal-dns` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:50.379Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/tmpfiles.md
- free tier: not dead: tmpfiles.org serves a free temporary file hosting upload page; files expire on a 60-minute to 48-hour timer with a 100 MB per-file cap (a paid tier was not assessed). | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: Maximum file size of 100 MiB per upload | note: not applicable
- retention: All files are deleted after 60 minutes 6 hours 24 hours 48 hours
- egress: not stated on https://tmpfiles.org/tos | metered: no
- identity: email
- interface: rest
- interface detail: Multipart HTTP POST to /api/v1/upload with an optional expire field; response gives a file URL.
- tooling: not documented
- composes with: An HTTP upload returns a URL that the caller uses to download the temporary file.
- reliability: Not dead, but effectively unreachable on this machine: DNS answers 0.0.0.0 / :: (sinkholed), so every plain curl fails with 'Could not resolve host'. Worked around with --resolve to the…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Not dead, but effectively unreachable on this machine: DNS answers 0.0.0.0 / :: (sinkholed), so every plain curl fails with 'Could not resolve host'. Worked around with --resolve to the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Not dead, but effectively unreachable on this machine: DNS answers 0.0.0.0 /:: (sinkholed), so every plain curl fails with 'Could not resolve host'. Worked around with --resolve to the Clou
  - [1] 2026-11-19: tmpfiles.org offers free temporary file hosting with a 60-minute to 48-hour expiry and a 100 MB per-file cap | capture: sha256:56a2957126c6a8a48df5c9f4ade700e26d5fd84c5d4a9b14be6a5426143efb53 | quote: All files are deleted after 60 minutes 6 hours 24 hours 48 hours
  - [2] 2026-11-19: tmpfiles.org exposes an HTTP POST upload API | capture: sha256:35a6ca634e8b9cdb4a76a2a64791b0550a5d50c682b8e2d753fa57b4fc4c705c | quote: POST https://tmpfiles.org/api/v1/upload
  - [2] 2026-11-19: the API documents the expire parameter for uploaded files | capture: sha256:35a6ca634e8b9cdb4a76a2a64791b0550a5d50c682b8e2d753fa57b4fc4c705c | quote: Seconds until deletion (60–172800), default 3600
  - [3] 2026-11-19: the first-party terms state a 100 MiB per-upload cap | capture: sha256:733bbbb8dc95448a2dc2d005abb0238f7f094627dba4666fd338abda7c46e925 | quote: Maximum file size of 100 MiB per upload
  - [2] 2026-11-19: the upload API returns a URL for the stored file | capture: sha256:35a6ca634e8b9cdb4a76a2a64791b0550a5d50c682b8e2d753fa57b4fc4c705c | quote: "url": "https://tmpfiles.org/{id}/{name}"
  - [3] 2026-11-19: the terms describe download via generated links but state no egress price or quota | capture: sha256:733bbbb8dc95448a2dc2d005abb0238f7f094627dba4666fd338abda7c46e925 | quote: Download and host files via external URLs
  - [3] 2026-11-19: the first-party terms state a maximum 48-hour retention | capture: sha256:733bbbb8dc95448a2dc2d005abb0238f7f094627dba4666fd338abda7c46e925 | quote: Files may be retained for a maximum of 48 hours
- sources:
  - [1] https://tmpfiles.org/
  - [2] https://tmpfiles.org/api
  - [3] https://tmpfiles.org/tos
