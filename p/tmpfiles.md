# tmpfiles.org

> tmpfiles.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tmpfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/tmpfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tmpfiles.org

- `storage/tmpfiles-org` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://tmpfiles.org/
