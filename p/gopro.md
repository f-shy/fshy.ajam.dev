# GoPro Cloud

> gopro.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gopro/ | JSON https://fshy.ajam.dev/api/v1/entity/gopro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GoPro Cloud / Quik (GoPro subscription)

- `netdisk-pan/gopro-cloud-quik` | qualifies-with-caveat | evidence reported | binding write-gated | category action-camera ecosystem cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T00:20:56.362Z (inherited) | stale on 2026-11-19
- url https://gopro.com/en/us/legal/subscriptionterms
- price USD 59.99/yr Premium and USD 99.99/yr Premium+, which is about USD 120/TB/yr on the 500 GB non-GoPro half and approaches zero on the GoPro half | parsed USD 10/TB-mo
- free tier: Unlimited cloud storage for GoPro content, meaning footage captured with a GoPro camera excluding Fusion, on any paid tier, plus 100 GB for non-GoPro content on Premium at USD 59.99/yr or 500 GB on Premium+ at USD 99.99/yr | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1] | note: unlimited applies to provenance, not to bytes: the terms draw the line at content captured with a GoPro camera
- per-object cap: Not published as a byte cap. Non-GoPro storage is restricted to MP4, Quicktime/MOV, JPEG, ASF and PNG files | source: [1]
- retention: While the subscription is active. No retention clock published | source: [1]
- egress: CDN downloads of originals with no published cap; access is by a bearer token against api.gopro.com | metered: no | source: [1]
- identity: card | detail: a credit card or other payment method at sign-up, including for the Free Introductory Trial
- interface: rest
- limits:
  - write-gated (binding): unlimited applies only to content captured with a GoPro camera, plus media trimmed from it in the Quik app; GoPro footage edited with non-GoPro software and re-imported counts as non-GoPro [1]
  - per-object-cap: non-GoPro storage is limited to MP4, Quicktime/MOV, JPEG, ASF and PNG files [2]
- binding note: The capacity is unlimited on paper and the gate is a provenance rule plus an upload path nobody has documented. Until one large non-GoPro file is uploaded and accepted, the offer is 100 GB at USD 59.99/yr, which is bad.
- tooling: reverse-engineered and read-only in every public wrapper: himewel/gopro-api in Python, dustin/gopro in Go with 139 stars and a push on 2026-10-13, gsora/gpdwn, mvisonneau/gpcd. All of them search, download and sync; none uploads. Auth is a bearer token lifted from a plus.gopro.com web session
- composes with: The most valuable unresolved lead in its group and it is one upload experiment, not a research question. The terms draw the line at provenance by device, not by file inspection, so if ingest does not verify capture provenance then unlimited capacity at USD 59.99/yr exists; if it does, the offer collapses to 100 or 500 GB
- reliability: No public wrapper implements upload, so the write path is undocumented rather than absent: the Quik app clearly uploads. Treat the write path as unproven. The supported non-GoPro file types are MP4, Quicktime/MOV, JPEG, ASF and PNG
- notes: Testing evaluates whether non-GoPro media qualifies for unlimited backup or remains restricted to the 100 GB cap. Pricing for general non-GoPro storage runs approximately USD 120 per TB per year, making device provenance verification the defining constraint.
- extras:
  - access_mode: paid
  - upload_api: none documented; the Quik app uploads but no wrapper implements it
  - provenance_rule: by capture device, excluding Fusion
  - test_that_settles_it: one account, one large non-GoPro upload, then read the quota back through api.gopro.com
- evidence:
  - [1] 2026-10-21: 'You receive unlimited cloud storage for content You capture with a GoPro camera (excluding Fusion)'; 'up to 100GB of cloud storage for content You capture with a non-GoPro camera'; 'Storage of non-GoPro footage is limited to the file types listed'
  - [3] 2026-10-21: Premium USD 59.99/yr with unlimited GoPro and 100 GB non-GoPro; Premium+ USD 99.99/yr with 500 GB
  - [4] 2026-10-21: 'Unofficial Python client for the GoPro cloud / Quik HTTP API at api.gopro.com: search your library and fetch download metadata', download only
  - [5] 2026-10-21: 139 stars, last push 2026-10-13, sync and download with no upload
  - [6] 2026-10-21: GoPro's own forum, users asking for upload functionality, which confirms there is no official upload API
  - [2] 2026-11-03: the article now renders and lists the non-GoPro types: MP4, Quicktime/MOV, JPEG, ASF, PNG | capture: sha256:8c994c5f6d1d46ff669eb87140bf2967dfb38eaf6ff740673348461d5dcf3b5c | quote: Supported non-GoPro types in the GoPro Cloud - MP4 - Quicktime / MOV - JPEG - ASF - PNG
  - [2] 2026-11-03: media trimmed from GoPro-captured content in Quik counts as GoPro content (unlimited); the same article lists GoPro footage edited in non-GoPro software as non-GoPro content | capture: sha256:8c994c5f6d1d46ff669eb87140bf2967dfb38eaf6ff740673348461d5dcf3b5c | quote: Any new, trimmed media made from content captured with a GoPro camera and trimmed using the Quik app (mobile or desktop) and uploaded to GoPro Cloud.
  - [1] 2026-11-03: sign-up requires a credit card or other payment method, for the free introductory trial too | capture: sha256:e62d571b8791348b46d14d5f6cd73ff9a38f9a01a8014fbaddf0c493cb4bb06d | quote: You must provide a credit card or other payment method at sign-up to ensure uninterrupted access to the Subscription at the end of the Free Introductory Trial
  - [3] 2026-11-03: Premium is still USD 59.99/yr with unlimited GoPro content and 100 GB non-GoPro | capture: sha256:72fc36427ad26611bdce5ae6b03f3f1bee809f8b65a3ea48376df426d732df42 | quote: | GoPro Premium12 | Unlimited GoPro plus 100 GB non-GoPro Footage: $59.99/yr |
  - [3] 2026-11-03: Premium+ is USD 99.99/yr with 500 GB non-GoPro | capture: sha256:72fc36427ad26611bdce5ae6b03f3f1bee809f8b65a3ea48376df426d732df42 | quote: | GoPro Premium+13 | Unlimited GoPro plus 500 GB non-GoPro Footage: $99.99/yr |
  - [1] 2026-11-03: the terms, effective 2026-04-17, still give unlimited storage for content captured with a GoPro camera excluding Fusion | capture: sha256:e62d571b8791348b46d14d5f6cd73ff9a38f9a01a8014fbaddf0c493cb4bb06d | quote: You receive unlimited cloud storage for content You capture with a GoPro camera (excluding Fusion), subject to the compatibility limitations listed
  - [1] 2026-11-03: non-GoPro content, and GoPro footage edited or imported by third-party software, is allocated 100 GB | capture: sha256:e62d571b8791348b46d14d5f6cd73ff9a38f9a01a8014fbaddf0c493cb4bb06d | quote: You are allocated up to 100GB of cloud storage for content You capture with a non-GoPro camera or device and content captured by a GoPro camera that is subsequently edited by (or imported from) a third party software application.
  - [1] 2026-11-03: uploads of non-GoPro content past the limit may be restricted | capture: sha256:e62d571b8791348b46d14d5f6cd73ff9a38f9a01a8014fbaddf0c493cb4bb06d | quote: Once You reach Your cloud storage limit for non-GoPro footage, GoPro may restrict the upload of any additional non-GoPro content to the GoPro cloud.
- sources:
  - [1] https://gopro.com/en/us/legal/subscriptionterms
  - [2] https://community.gopro.com/s/article/What-Content-Is-Supported-In-GoPro-Cloud
  - [3] https://gopro.com/en/dj/shop/subscriptions
  - [4] https://github.com/himewel/gopro-api
  - [5] https://github.com/dustin/gopro
  - [6] https://github.com/gopro/labs/discussions/1400
