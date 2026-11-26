# artstation

> artstation.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/artstation/ | JSON https://fshy.ajam.dev/api/v1/entity/artstation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## artstation

- `storage/artstation` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:55.372Z (live) | stale on 2026-12-04
- url https://help.artstation.com/en/articles/16155253
- free tier: none reachable: Image posts cap at 10,000x10,000 px and the platform re-encodes for the portfolio viewer; free accounts have no meaningful byte quota but no original-byte delivery either. The Pro/Studio… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: images must be greater than 400px X 400px, less than 10,000px X 10,000px and less than 10MB, otherwise they won't upload; uploaded bytes are normalized to JPG at 90% quality at 1920 width | source: [1] | note: not applicable
- retention: stated-absent: the help article states no retention period for uploaded images | source: [1]
- egress: stated-absent: the help article states no egress terms; images are served through a CDN and re-encoded for the viewer | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the help article describes portfolio image hosting and states no programmatic object interface
- tooling: not documented
- composes with: stated-absent: the help article states no way to chain portfolio images into a byte store; images are normalized and original bytes are not delivered except on ArtStation-powered website pages
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Image posts cap at 10,000x10,000 px and the platform re-encodes for the portfolio viewer; free accounts have no meaningful byte quota but no original-byte delivery either. The Pro/Studio…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Image posts cap at 10,000x10,000 px and the platform re-encodes for the portfolio viewer; free accounts have no meaningful byte quota but no original-byte delivery either. The Pro/Studio…
  - [2] 2026-10-21: cited as the basis of the rejection: Image posts cap at 10,000x10,000 px and the platform re-encodes for the portfolio viewer; free accounts have no meaningful byte quota but no original-byte delivery either. The Pro/Studio ups
  - [1] 2026-11-19: ArtStation caps uploads at 10,000 by 10,000 pixels and 10MB and normalizes stored images | capture: sha256:32dcb448c26e96b604d38f9e69283d2f59677a709b4fbeed01863671456c2656 | quote: Please keep in mind that images must be greater than 400px X 400px, less than 10,000px X 10,000px and less than 10MB, otherwise they won't upload.
  - [1] 2026-11-19: the page describes image hosting and states no programmatic interface | capture: sha256:32dcb448c26e96b604d38f9e69283d2f59677a709b4fbeed01863671456c2656 | quote: ArtStation already does an excellent job of hosting images and retaining quality of images.
  - [1] 2026-11-19: the page describes image normalization but states no retention period | capture: sha256:32dcb448c26e96b604d38f9e69283d2f59677a709b4fbeed01863671456c2656 | quote: Generally, assets uploaded to artworks will be normalized using compression, conversion or resizing depending on what you upload.
  - [1] 2026-11-19: the first-party help article states a 10MB and 10,000px per-image limit | capture: sha256:32dcb448c26e96b604d38f9e69283d2f59677a709b4fbeed01863671456c2656 | quote: less than 10,000px X 10,000px and less than 10MB, otherwise they
  - [1] 2026-11-19: the page says originals are not generally delivered, so original bytes are not chainable | capture: sha256:32dcb448c26e96b604d38f9e69283d2f59677a709b4fbeed01863671456c2656 | quote: Some places on ArtStation where images are not compressed - notably on your ArtStation-powered website pages
  - [1] 2026-11-19: the page describes re-encoding for delivery and states no egress allowance | capture: sha256:32dcb448c26e96b604d38f9e69283d2f59677a709b4fbeed01863671456c2656 | quote: ArtStation will convert images to JPG at 90% quality at 1920 width.
- sources:
  - [1] https://help.artstation.com/en/articles/16155253
  - [2] https://magazine.artstation.com/2025/12/new-on-artstation-faster-portfolios-bigger-uploads-better-job-tools/
