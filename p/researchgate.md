# researchgate full-text

> researchgate.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/researchgate/ | JSON https://fshy.ajam.dev/api/v1/entity/researchgate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## researchgate — data upload as storage

- `storage/researchgate-data-upload-as-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:03.329Z (live) | stale on 2026-12-04
- url https://www.researchgate.net/post/How_to_upload_a_document
- free tier: none reachable: Not a data repository and never was. Per-file limits are tiny and the platform is a publication-profile site: forum answers document an 80 MB document cap and a 512 MB video cap, and their… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Not a data repository and never was. Per-file limits are tiny and the platform is a publication-profile site: forum answers document an 80 MB document cap and a 512 MB video cap, and their…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a data repository and never was. Per-file limits are tiny and the platform is a publication-profile site: forum answers document an 80 MB document cap and a 512 MB video cap, and their…
  - [2] 2026-10-21: cited as the basis of the rejection: Not a data repository and never was. Per-file limits are tiny and the platform is a publication-profile site: forum answers document an 80 MB document cap and a 512 MB video cap, and their o
  - [3] 2026-10-21: cited as the basis of the rejection: Not a data repository and never was. Per-file limits are tiny and the platform is a publication-profile site: forum answers document an 80 MB document cap and a 512 MB video cap, and their o
  - [3] 2026-11-19: data upload requires registration, so there is no anonymous free storage tier | capture: sha256:da89ebe567a25b5c8ecdd36934a2963d6dc4409642584e07771d5f380aa0f0d5 | quote: Permission to upload data on ResearchGate is limited to registered ResearchGate members.
  - [4] 2026-11-19: signup uses an institutional email address | capture: sha256:f87fb98da2cd6e663a002d84e08fe43e14346176c6150a55164f8c7bc7eb1ffd | quote: ResearchGate is a professional network for active scientists and researchers. We ask that you sign up with your institutional email address to help us easily verify your involvement in current research.
- sources:
  - [1] https://www.researchgate.net/post/How_to_upload_a_document
  - [2] https://faqs.tips/post/what-do-you-think-of-uploading-your-high-quality-video-lectures-here-on-rg.html
  - [3] https://help.researchgate.net/research-and-publications/data
  - [4] https://help.researchgate.net/getting-started/signing-up-for-researchgate

## researchgate full-text upload

- `storage/researchgate-full-text-upload` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:06.369Z (live) | stale on 2026-12-04
- url https://help.researchgate.net/hc/en-us/articles/360015872812-What-is-the-maximum-file-size-for-uploads
- free tier: none reachable: no published per-file or per-account quota; uploads are gated to works you are an author of, and the help centre article for max file size 404s. Reviewer removed the only machine-readable… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: unverified: https://help.researchgate.net/hc/en-us/articles/360015872812-What-is-the-maximum-file-size-for-uploads answered HTTP 404 on 2026-11-19; no published per-file or per-account quota; routes tried: first-party capture returned 404, direct probe confirmed 404
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: no published per-file or per-account quota; uploads are gated to works you are an author of, and the help centre article for max file size 404s. Reviewer removed the only machine-readable…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: no published per-file or per-account quota; uploads are gated to works you are an author of, and the help centre article for max file size 404s. Reviewer removed the only machine-readable…
  - probe:https://help.researchgate.net/hc/en-us/articles/360015872812-What-is-the-maximum-file-size-for-uploads 2026-11-19: the file-size help article answered HTTP 404 | capture: sha256:3df15a6849734d863b8c5926e0801e90eeb55e038bf5cb856dc11662bdbc6922 | quote: "status": 404
  - [1] 2026-11-19: the max file size help article no longer exists at its published URL | capture: sha256:d1c2e7e290e41c46f761e1548455e32bcf1e44321a450d35236faea7bec5fdff | quote: This page may have been moved, renamed, or deleted.
- sources:
  - [1] https://help.researchgate.net/hc/en-us/articles/360015872812-What-is-the-maximum-file-size-for-uploads
