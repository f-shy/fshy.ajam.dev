# HydroShare

> hydroshare.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hydroshare/ | JSON https://fshy.ajam.dev/api/v1/entity/hydroshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HydroShare (CUAHSI)

- `storage/hydroshare` | fails-quota | evidence reported | binding write-gated | category research-data-repository
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.hydroshare.org
- free tier: 20 GB automatic on account creation, with an increase process that is explicitly designed to succeed: 'if needed, request reasonable quota increase … all reasonable requests will be approved subject to system capacity limitations'. No absolute ceiling is published. The only stated limit is capacity. So the honest number is 20 GB default with an unbounded-by-documentation increase path, and any 500 GB+ claim depends on a human granting it. A second lever: on publish, the storage is transferred off the author's quota — . 'CUAHSI will assume the burden of storage for published resources'. So publishing frees the quota for reuse. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and anonymous. Verified: the resource data endpoint serves a bagit zip to a logged-out client with no credentials. | metered: no
- identity: email | detail: email
- interface: s3, rest
- limits:
  - write-gated (binding): approved subject to system capacity limitations' [1]
  - write-gated (binding): reviewed' but are a manual queue [1]
- limits note: write-gated on the increase (email a human), and the quota is small by default. Discipline mismatch: it is a hydrology repository, so non-hydrology payloads are off-genre even though nothing technically enforces it.
- interface detail: rest
- tooling: HS REST API at /hsapi/ returns JSON from /hsapi/resource/?format=json without authentication. A documented external storage mount feature allows registering resources whose objects reside in external S3 or iRODS storage, functioning as a metadata and DOI catalog layer.
- composes with: Resources are unlimited; quota is per-user and transferable ('The quota holder … can be transferred between owner[s]'). Publishing moves the bytes off your quota onto CUAHSI's, then the freed 20 GB is reusable — so the pattern is publish-then-refill, repeated. Community/group resources can pool several members' quotas.
- reliability: US NSF-funded repository operated via CUAHSI. Anonymous BagIt downloads are operational. Quota increase requests undergo manual review.
- notes: 20 GB automatic on account creation, with an increase process that is explicitly designed to succeed: 'if needed, request reasonable quota increase … all reasonable requests will be approved subject to system capacity limitations'. No absolute ceiling is published. The only stated limit is capacity. So the honest number is 20 GB default with an unbounded-by-documentation increase path, and any 500 GB+ claim depends on a human granting it. A second lever: on publish, the storage is transferred off the author's quota — 'CUAHSI will assume the burden of storage for published resources'. So publishing frees the quota for reuse.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB automatic on account creation, with an increase process that is explicitly designed to succeed: 'if needed, request reasonable quota increase … all reasonable requests will be approved subject to system capacity limitations'. No absolute ceiling is published — the only stated limit is capacity. So the honest number is 20 GB default with an unbounded-by-documentation increase path, and any 500 GB+ claim depends on a human granting it. A second lever: on publish, the storage is transferred off the author's quota — 'CUAHSI will assume the burden of storage for published resources' — so publishing frees the quota for reuse.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: opened: 'The automatic quota allocation upon account creation is 20 gigabytes … request reasonable quota increase … all reasonable requests will be approved subject to system capacity limitations'; 'once a resource is published … CUAHSI will assume the burden of storage for published resources.'
  - [2] 2026-10-21: opened: 'Browsing and downloading public resources requires no account, and creating an account to upload, manage, and publish resources is also free.'
  - [3] 2026-10-21: PROBED: curl -> HTTP 200, 137,978 bytes of JSON. Anonymous REST read works.
  - [4] 2026-10-21: PROBED: curl -> HTTP 200, 211,663 bytes, body begins with the ZIP magic 'PK\x03\x04' and contains 999b9319…/bagit.txt. So the metadata endpoint returns a real bagit archive, not a stub — the object comes back.
  - [5] 2026-10-21: PROBED: curl -> 200 but content-type application/json, 143 bytes — this specific path is an API descriptor, not the bytes. Distinguishing the two endpoints matters: /hsapi/resource/<id>/?format=json is the one that yields the archive.
- sources:
  - [1] https://help.hydroshare.org/about-hydroshare/policies/quota/
  - [2] https://casrai.org/guides/cuahsi-hydroshare-hydrology-data-repository
  - [3] https://www.hydroshare.org/hsapi/resource/?format=json
  - [4] https://www.hydroshare.org/hsapi/resource/999b9319ec304924b3f3113ad75ffc23/?format=json
  - [5] https://www.hydroshare.org/resource/999b9319ec304924b3f3113ad75ffc23/data/contents/
