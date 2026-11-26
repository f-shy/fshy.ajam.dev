# AnonFile

> anonfiles.info | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anonfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/anonfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnonFile (anonfiles.info)

- `debrid/anonfiles-info` | dead | evidence measured | binding none | category anonymous file host (AnonFiles-branded clone) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:21:35.239Z (live) | stale on 2026-12-26
- url https://anonfiles.info/
- free tier: none reachable: the page claims '20 GB filesize limit and unlimited bandwidth' but the origin refuses TCP | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The claim is readable in the search index and the host does not answer.
- per-object cap: 20 GB claimed, unreachable | source: [1]
- retention: not reached | source: [1]
- egress: not assessed | metered: no | source: [1]
- identity: anonymous | detail: No signup was reached; the host refused the connection.
- interface: unknown
- limits note: Connection refused at the TCP layer, which is a stronger finding than a 4xx: the host is not listening.
- binding note: Nothing binds because the host refuses connections.
- interface detail: unverified: no page could be read; the request path refused the host as non-public on 2026-11-25
- tooling: Nothing to drive.
- composes with: Nothing to chain.
- reliability: unverified: the request path refused the host as non-public on 2026-11-25 (403); routes tried: page reader and a direct HTTPS GET (403 not a public host)
- notes: The 20 GB claim in the search index is stale; the origin is not listening.
- evidence note: Measured death: ConnectionRefusedError on the upload POST.
- extras:
  - error: ConnectionRefusedError
- evidence:
  - probe:https://anonfiles.info/upload 2026-10-23: multipart POST -> ConnectionRefusedError [WinError 10061], no HTTP status at all
  - probe:https://anonfiles.info/ 2026-11-25: the host was refused on the current network path; no HTTP answer was received | capture: sha256:cb284ceabb46c7001c8921b26a859c30495993dc6a2da2a38ecb04ae965b837d | quote: "error_detail": "URLError: <urlopen error Tunnel connection failed: 403 not a public host>"
  - probe:https://anonfiles.info/ 2026-11-25: no HTTP response was obtained from the host | capture: sha256:cb284ceabb46c7001c8921b26a859c30495993dc6a2da2a38ecb04ae965b837d | quote: "error": "transport"
  - probe:https://anonfiles.info/ 2026-11-25: the probe targeted the record's first-party URL; no page was served | capture: sha256:cb284ceabb46c7001c8921b26a859c30495993dc6a2da2a38ecb04ae965b837d | quote: "url": "https://anonfiles.info/"
- sources:
  - [1] https://anonfiles.info/
