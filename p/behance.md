# behance

> behance.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/behance/ | JSON https://fshy.ajam.dev/api/v1/entity/behance.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## behance

- `storage/behance` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:57.619Z (live) | stale on 2026-12-04
- url https://help.behance.net/hc/en-us/articles/9510593419035
- free tier: none reachable: 500 MB per file for project asset types and unlimited projects, but Behance renders display images at 1400px/2800px so the source file is not what is served. No upload API, Adobe-account… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: under 500MB for accepted file types | source: [1] | note: 500MB ceiling on accepted file types stated on the first-party help page
- retention: not stated on the Behance help pages | source: [1] | note: not stated on the Behance help pages
- egress: not stated on the Behance help pages | metered: no
- identity: email
- interface: browser
- interface detail: browser project pages; no upload API stated on the first-party help pages
- tooling: web browser (no upload API stated on the first-party help pages)
- composes with: project pages render display images at fixed resolutions, so the source file is not served as uploaded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 500 MB per file for project asset types and unlimited projects, but Behance renders display images at 1400px/2800px so the source file is not what is served. No upload API, Adobe-account…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 500 MB per file for project asset types and unlimited projects, but Behance renders display images at 1400px/2800px so the source file is not what is served. No upload API, Adobe-account…
  - [2] 2026-10-21: cited as the basis of the rejection: 500 MB per file for project asset types and unlimited projects, but Behance renders display images at 1400px/2800px so the source file is not what is served. No upload API, Adobe-account gat
  - [1] 2026-11-19: Behance still documents a 500MB per-file limit for project assets | capture: sha256:60894f881eae7851293f09dd347e334a835e03b66dc0fb09d9fc477603f3c391 | quote: We accept the following file types as long as they are under 500MB.
  - [2] 2026-11-19: the guide addresses browser image uploads without naming an API or CLI tool | capture: sha256:2325af6799a54853127e1eccbc9c0a488079ac11e6d2ea65e1beb9e09fcd2ff9 | quote: We do not accept images larger than 50MB.
  - [2] 2026-11-19: the service re-renders images rather than serving original bytes | capture: sha256:2325af6799a54853127e1eccbc9c0a488079ac11e6d2ea65e1beb9e09fcd2ff9 | quote: We display images all images at 1400px wide in the Project View and up to 2800px in the Lightbox View which is triggered when you click on an image.
- sources:
  - [1] https://help.behance.net/hc/en-us/articles/9510593419035
  - [2] https://help.behance.net/hc/en-us/articles/204484614
