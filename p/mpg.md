# edmond

> mpg.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mpg/ | JSON https://fshy.ajam.dev/api/v1/entity/mpg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## edmond (max planck, edmond.mpdl.mpg.de)

- `storage/edmond` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:31.167Z (live) | stale on 2026-12-04
- url https://edmond.mpdl.mpg.de/api/dataverses/:root/storage/quota?showInherited=true
- free tier: No quota defined for this collection. The former edmond.mpdl.mpg.de hostname now redirects to edmond.mpg.de, whose native Dataverse quota API returns this message. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: edmond.mpdl.mpg.de redirects to edmond.mpg.de. The current host answers the Dataverse REST API (version 6.10.1 mpdl-develop) and the root quota endpoint states no quota is defined for the collection.
- notes: 308 permanent redirect to edmond.mpg.de on every path.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: 308 permanent redirect to edmond.mpg.de on every path.
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 308 permanent redirect to edmond.mpg.de on every path.
  - [2] 2026-10-21: cited as the basis of the rejection: 308 permanent redirect to edmond.mpg.de on every path.
  - [3] 2026-11-19: the current hostname answers the native Dataverse version API | capture: sha256:1956037fa5d5ed7337c09b44b746fa7df5e8fe3509a8831326fc2184e4c4c69f | quote: {"status":"OK","data":{"version":"6.10.1 mpdl-develop - 9ac2b3676a","build":null}}
  - [4] 2026-11-19: the current hostname's quota API states no quota is defined for this collection | capture: sha256:79bd00cb93d25986fb1a700b3b3b1ad6cf4fe5e421a1c4bd099a9174ce47d0fc
- sources:
  - [1] https://edmond.mpdl.mpg.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://edmond.mpg.de/api/
  - [3] https://edmond.mpg.de/api/info/version
  - [4] https://edmond.mpg.de/api/dataverses/:root/storage/quota?showInherited=true
