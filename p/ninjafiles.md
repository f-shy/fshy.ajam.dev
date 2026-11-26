# Ninja Files

> ninjafiles.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ninjafiles/ | JSON https://fshy.ajam.dev/api/v1/entity/ninjafiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ninja Files

- `debrid/ninjafiles-io` | dead | evidence measured | binding none | category anonymous file host (3 GB claim) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:21:35.239Z (live) | stale on 2026-12-26
- url https://ninjafiles.io/
- free tier: none reachable: the indexed page says 'Maximum upload file size: 3072MB' with no expiry option removed, but the hostname does not resolve | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: NXDOMAIN at the resolver, so no page was served today and the claim is the search index's only.
- per-object cap: 3072 MB claimed, host does not resolve | source: [1]
- retention: not reached | source: [1]
- egress: not assessed | metered: no | source: [1]
- identity: anonymous | detail: No signup was reached.
- interface: unknown
- limits note: A DNS death is the cheapest kind to verify and the easiest to miss: the search index still carries the page.
- binding note: Nothing binds because the name does not resolve.
- interface detail: Name resolution fails; no HTTP request was possible.
- tooling: Nothing to drive.
- composes with: Nothing to chain.
- reliability: unverified: the name did not resolve on 2026-11-25; routes tried: page reader (502 DNS failure), direct HTTPS GET (502 name did not resolve)
- notes: The name still ranks in a 2026 comparison; the domain is gone.
- evidence note: Measured death: getaddrinfo failed for the upload host.
- extras:
  - error: getaddrinfo failed
- evidence:
  - probe:https://ninjafiles.io/upload.php 2026-10-23: multipart POST -> gaierror [Errno 11001] getaddrinfo failed; no HTTP status
  - probe:https://ninjafiles.io/ 2026-11-25: the name still does not resolve; no HTTP answer was received | capture: sha256:cc82394b020d923c9ad92ae096c33b4660441422015241ec68b9f97b68b404bc | quote: "error_detail": "URLError: <urlopen error Tunnel connection failed: 502 the name did not resolve>"
  - probe:https://ninjafiles.io/ 2026-11-25: the probe targeted the record's first-party URL; no page was served | capture: sha256:cc82394b020d923c9ad92ae096c33b4660441422015241ec68b9f97b68b404bc | quote: "url": "https://ninjafiles.io/"
- sources:
  - [1] https://ninjafiles.io/
