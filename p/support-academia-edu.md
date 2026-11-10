# academia.edu

> support.academia.edu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/support-academia-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/support-academia-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## academia.edu

- `storage/academia-edu` | fails-quota | evidence reported | binding per-object-cap | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:31:28.056Z (live) | stale on 2026-11-19
- url https://support.academia.edu/hc/en-us/articles/360043383793-How-to-upload-a-document-to-Academia
- free tier: Per-file cap 100MB; no total quota is stated in the articles read | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: Files must be 100MB or less | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 100MB per file [1]
- binding note: per-file cap of 100MB and document-type formats only; no total quota is stated in the articles read
- interface detail: not documented
- tooling: unverified: whether an upload API exists; the documented path is the browser upload flow, which includes a CAPTCHA step
- composes with: not recorded
- reliability: Per-file cap 100MB; document-type formats only (no video upload); uploads are for sharing documents with the world, so it does not hold arbitrary bytes
- notes: the same as reliability
- evidence note: The 2026-11-03 evidence rows read https://support.academia.edu/hc/en-us/articles/360043383793-How-to-upload-a-document-to-Academia (100MB per-file cap, upload to a public audience, CAPTCHA step) and https://support.academia.edu/hc/en-us/articles/360043384893 (no video upload). The identity requirement is a default, not read from a vendor page, so the rung stays reported.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: upload flow documented but no quota anywhere in the help centre; documents are public-by-design and tied to an academic identity. No API
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: upload flow documented but no quota anywhere in the help centre; documents are public-by-design and tied to an academic identity. No API
  - [1] 2026-11-03: the per-file upload cap is 100MB | capture: sha256:86c90bb5659576a4c7996af55a9e212e9cb8a5c325226d9d0714131a85d8f54b | quote: File sizes too large. Files must be 100MB or less.
  - [2] 2026-11-03: video files cannot be uploaded; only document-type formats are accepted | capture: sha256:137caccd1d9f7950981861ce0b2d272bdf467ed551b51a5178781f1919ab6a2e | quote: It's not possible to upload video files to Academia, but you can add links to videos from YouTube or Vimeo to your paper details.
  - [1] 2026-11-03: uploaded documents are published to a public audience | capture: sha256:86c90bb5659576a4c7996af55a9e212e9cb8a5c325226d9d0714131a85d8f54b | quote: You can use the steps below to upload any document type you want to share with the world; it doesn't have to be a paper!
  - [1] 2026-11-03: the documented upload flow has a CAPTCHA step | capture: sha256:86c90bb5659576a4c7996af55a9e212e9cb8a5c325226d9d0714131a85d8f54b | quote: Complete the CAPTCHA to confirm you're not a robot.
  - [1] 2026-11-03: the binding constraint is a per-file cap on document-type uploads; no identity gate beyond an account was read | capture: sha256:86c90bb5659576a4c7996af55a9e212e9cb8a5c325226d9d0714131a85d8f54b | quote: File sizes too large. Files must be 100MB or less.
  - [1] 2026-11-03: the per-file cap is 100MB | capture: sha256:86c90bb5659576a4c7996af55a9e212e9cb8a5c325226d9d0714131a85d8f54b | quote: File sizes too large. Files must be 100MB or less.
  - [1] 2026-11-04: the per-file upload cap is 100MB | capture: sha256:c7205ec4bcf6db3c3ae5000d701b92b6c72ed5c5418fba2877f647f1416a5668 | quote: File sizes too large. Files must be 100MB or less.
- sources:
  - [1] https://support.academia.edu/hc/en-us/articles/360043383793-How-to-upload-a-document-to-Academia
  - [2] https://support.academia.edu/hc/en-us/articles/360043384893

## academia.edu — data upload

- `storage/academia-edu-data-upload` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.academia.edu/hc/en-us/articles/360043383793-How-to-upload-a-document-to-Academia
- free tier: none reachable: Same category error as ResearchGate, one step worse: it is a paper-sharing site with premium paywalls and no repository function, no DOI, and no documented byte quota because it was never… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Same category error as ResearchGate, one step worse: it is a paper-sharing site with premium paywalls and no repository function, no DOI, and no documented byte quota because it was never…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Same category error as ResearchGate, one step worse: it is a paper-sharing site with premium paywalls and no repository function, no DOI, and no documented byte quota because it was never…
  - [2] 2026-10-21: cited as the basis of the rejection: Same category error as ResearchGate, one step worse: it is a paper-sharing site with premium paywalls and no repository function, no DOI, and no documented byte quota because it was never de
- sources:
  - [1] https://support.academia.edu/hc/en-us/articles/360043383793-How-to-upload-a-document-to-Academia
  - [2] https://support.academia.edu/hc/en-us/categories/360003163373-Academia-Free-Features
