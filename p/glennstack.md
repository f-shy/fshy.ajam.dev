# CrafterBin

> glennstack.dev | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/glennstack/ | JSON https://fshy.ajam.dev/api/v1/entity/glennstack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CrafterBin

- `debrid/crafterbin` | qualifies | evidence measured | binding per-object-cap | category anonymous temporary file host with a server-side URL pull (0x0.st clone) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://crafterbin.glennstack.dev
- price USD 0
- free tier: max_size = 512.0 MiB, no account, and two mutually exclusive form fields: 'file' for a local upload and 'url' for a remote pull. | unit: bytes | metered on: none | read on: 2026-10-23 | source: [1] | note: The retention is a function of size, published as a formula, not a flat number.
- per-object cap: max_size = 512.0 MiB | bytes: 536870912 | source: [1]
- retention: retention = min_age + (max_age - min_age) * pow((1 - file_size / max_size), 3), with min_age 7 days and max_age 365 days; a small file therefore approaches a year and a 512 MiB file gets 7 days. 'expires' can be set in hours or as an ms epoch. | days: 365 | source: [1] | note: For the 1 MiB probe the formula gives about 362 days, so 365 is the ceiling the service allows and the actual value is size-dependent.
- egress: Downloads are served from crafterbin.glennstack.dev with no byte counter; the X-Token response header carries a management token for deletion. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account, no email, no cookie. The reply body is the URL and the X-Token header is the only credential, for deletion of that one object.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 512 MiB per file [1]
  - retention-clamped: 7 days for a 512 MiB file, about 365 days for a tiny one; the size decides [1]
  - request-rate: not published; the operator is a single hobby instance on Hunchentoot/Caddy [1]
- limits note: The retention formula is quoted from the service's own plain-text interface page, which is the whole documentation.
- binding note: 512 MiB is the hard stop for a single object; at 1 TiB a month that is 2 048 uploads, and the retention curve means the largest objects, which are the ones an archive needs, expire first at 7 days.
- interface detail: POST multipart/form-data to the bare host with field 'file', or field 'url' to have the server fetch a link. 'secret' (no value) asks for a long unguessable id; 'expires' takes hours or an ms epoch.
- endpoint: https://crafterbin.glennstack.dev
- tooling: curl -F'file=@x' or curl -F'url=https://...' https://crafterbin.glennstack.dev; the service is 0x0.st-shaped, so an existing 0x0.st client works after a hostname change
- composes with: It is the only anonymous host among debrid providers that both stores a local file and pulls a URL server-side, so a user can hand it a URL and never upload the bytes itself, and its size-scaled retention gives small files the longest life of anything measured here.
- reliability: A single hobby instance behind Caddy on Hunchentoot, with no published rate limit; the service runs on one privately operated server, so an outage is silent and unannounced.
- notes: Remote URL retrieval operating without account registration. Files are stored on a single community instance, so retention depends on server availability.
- evidence note: Both paths measured in on 2026-10-23: a multipart local upload and a 'url' field pull from a Catbox link, each read back at 1 048 576 bytes with a matching SHA-256.
- probe:
  - upload_bytes: 1048576
  - download_bytes: 1048576
  - match: yes
  - status: 200
- extras:
  - remote_pull_measured: yes
  - management: X-Token response header, used with the delete endpoint
  - runtime: Hunchentoot 1.3.1 behind Caddy
- evidence:
  - probe:https://crafterbin.glennstack.dev 2026-10-23: POST field 'file' -> HTTP 200 body https://crafterbin.glennstack.dev/h2cZ; X-Token present in the response headers
  - probe:https://crafterbin.glennstack.dev/h2cZ 2026-10-23: read-back 1 048 576 bytes, sha256 da0099c231f1182a5d411c8ac5149dfb7a2e3578a3970928490cb78ba92aecc9, full-body hash matched
  - probe:https://crafterbin.glennstack.dev/OF3N 2026-10-23: server-side pull: POST field 'url'=https://files.catbox.moe/6hir65.bin returned OF3N with no bytes sent from here, and the read-back was 1 048 576 bytes with the same sha256. That proves the server obtained the object; whether it stored a copy or proxied the origin at read time was not distinguished, and the object is still live at the origin
  - [1] 2026-10-23: max_size = 512.0 MiB, min_age 7 days, max_age 365 days, the retention formula, and the 'url' field documented as 'remote URL' and 'mutually exclusive with file'
- sources:
  - [1] https://crafterbin.glennstack.dev
