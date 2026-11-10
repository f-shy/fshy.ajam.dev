# AnonFile

> anonfiles.info | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anonfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/anonfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnonFile (anonfiles.info)

- `debrid/anonfiles-info` | dead | evidence measured | binding none | category anonymous file host (AnonFiles-branded clone) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://anonfiles.info/
- free tier: none reachable: the page claims '20 GB filesize limit and unlimited bandwidth' but the origin refuses TCP | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The claim is readable in the search index and the host does not answer.
- per-object cap: 20 GB claimed, unreachable | source: [1]
- retention: not reached | source: [1]
- egress: not assessed | metered: no | source: [1]
- identity: anonymous | detail: No signup was reached; the host refused the connection.
- interface: unknown
- limits note: Connection refused at the TCP layer, which is a stronger finding than a 4xx: the host is not listening.
- binding note: Nothing binds because the host refuses connections.
- interface detail: No connection: an HTTPS request to the origin was refused on 2026-10-23.
- tooling: Nothing to drive.
- composes with: Nothing to chain.
- reliability: One of several AnonFiles-branded revival sites; this one is not serving.
- notes: The 20 GB claim in the search index is stale; the origin is not listening.
- evidence note: Measured death: ConnectionRefusedError on the upload POST.
- extras:
  - error: ConnectionRefusedError
- evidence:
  - probe:https://anonfiles.info/upload 2026-10-23: multipart POST -> ConnectionRefusedError [WinError 10061], no HTTP status at all
- sources:
  - [1] https://anonfiles.info/
