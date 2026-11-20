# Filester

> filester.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filester/ | JSON https://fshy.ajam.dev/api/v1/entity/filester.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filester

- `debrid/filester` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (free, anonymous uploads, REST API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://filester.me/faq
- price unverified: no paid tier page was readable
- free tier: Up to 10 GB per file; files that get no downloads within 35 days are deleted; no file type is blocked. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: No total storage figure is printed.
- per-object cap: Up-to 10GB, subject to be changed without any prior notice if it gets abused, or we decide to increase it. | bytes: 10737418240 | source: [1] | note: bytes = 10 x 1024^3; the vendor may change the cap without notice.
- retention: As long as files have downloads it will be kept as long as the site is running. Files that do not get downloads within 35 days will get deleted. | days: 35 | source: [1] | note: The 35 days restart with each download.
- egress: No download allowance printed; registered users get view and download counts. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The FAQ states 'Anonymous uploads cannot be manually deleted', so anonymous upload exists; registered users get a dashboard and password protection.
- interface: rest
- limits:
  - per-object-cap: 10 GB per file, changeable without notice [1]
  - retention-clamped (binding): deleted after 35 days with no download [1]
- binding note: A file nobody downloads within 35 days is deleted, which bounds how long an upload can be left unattended.
- interface detail: The FAQ says an API exists for uploading files and managing folders; the API documentation page was not read.
- tooling: REST API per the FAQ; the API page was not read.
- composes with: 10 GB anonymous uploads kept as long as they are downloaded at least once in 35 days: a download counter keeps a file alive.
- reliability: No paid tier page was found: the /pricing URL answered HTTP 404 on 2026-11-03.
- evidence note: FAQ read on 2026-11-03. Paid tier unverified: no price page exists at /pricing.
- evidence:
  - [1] 2026-11-03: the per-file cap is 10 GB | capture: sha256:90227a7194e201f189828293d103e99c0a00966fee98246a7d76b9cfeee04a65 | quote: Up-to 10GB, subject to be changed without any prior notice if it gets abused, or we decide to increase it.
  - [1] 2026-11-03: 35-day no-download deletion | capture: sha256:90227a7194e201f189828293d103e99c0a00966fee98246a7d76b9cfeee04a65 | quote: Files that do not get downloads within 35 days will get deleted.
  - [1] 2026-11-03: anonymous uploads exist | capture: sha256:90227a7194e201f189828293d103e99c0a00966fee98246a7d76b9cfeee04a65 | quote: Anonymous uploads cannot be manually deleted.
- sources:
  - [1] https://filester.me/faq
