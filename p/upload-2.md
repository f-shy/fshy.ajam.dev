# Upload.ee

> upload.ee | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upload-2/ | JSON https://fshy.ajam.dev/api/v1/entity/upload-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Upload.ee

- `debrid/upload-ee` | fails-quota | evidence documented | binding per-object-cap | category file host (anonymous 50 days, registered 120 days) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:23:20.852Z (live) | stale on 2026-12-05
- url https://www.upload.ee/
- free tier: Maximum filesize 100 megabytes; no waiting time; anonymous files expire 50 days and registered users files 120 days after the last download. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 100 megabytes per file | source: [1]
- retention: anonymous files expire after 50 days; registered users files after 120 days after the last download | days: 50 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: Anonymous files are stated, so no account is needed to upload; logged-in users may upload three files at once.
- interface: unknown
- limits:
  - per-object-cap (binding): maximum filesize 100 megabytes [1]
  - retention-clamped: anonymous files expire after 50 days [1]
- binding note: A 100 MB ceiling binds a large archive first.
- interface detail: Web upload with a gallery and file listing; no API was read.
- tooling: Browser upload.
- composes with: Anonymous uploads are accepted; the 100 MB cap is the same for all users.
- reliability: No status page was read.
- evidence note: Cap and expiry read on the vendor home page.
- evidence:
  - [1] 2026-11-03: the file cap is 100 MB | capture: sha256:9b3adefc4973c9be88fc26ef9b7b7b8e421a84d47a5aee5af1d8de60fb014061 | quote: Maximum filesize 100 megabytes (MB)
  - [1] 2026-11-03: anonymous files expire after 50 days, registered after 120 | capture: sha256:9b3adefc4973c9be88fc26ef9b7b7b8e421a84d47a5aee5af1d8de60fb014061 | quote: Anonymous files expire 50 days and registered users' files expire 120 after last download
  - [1] 2026-11-04: no API is published there | capture: sha256:9b3adefc4973c9be88fc26ef9b7b7b8e421a84d47a5aee5af1d8de60fb014061 | quote: Uploading of up to 3 simultaneous files for logged in users
- sources:
  - [1] https://www.upload.ee/
