# Scribd

> scribd.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scribd/ | JSON https://fshy.ajam.dev/api/v1/entity/scribd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scribd

- `storage/scribd` | fails-egress | evidence reported | binding per-object-cap | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.scribd.com
- free tier: 100 MB max per document; no published account-level document or storage cap ("you can continue to upload more documents ... as often as you like"). Effectively per-record 100 MB x unlimited records. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB/file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not free-at-scale and not scriptable: downloads are gated by the uploader's setting and often by a Scribd subscription; there is no public direct-file URL, and pages are served as HTML viewer assets. | metered: no
- identity: email
- interface: rclone
- limits:
  - per-object-cap (binding): 100 MB/file [1]
- limits note: 100 MB/file; upload requires a registered, in-good-standing account; uploader agreement grants Scribd rights to restrict access/download and to "train machine learning ... models" on content; conversion failures on large or layered PDFs.
- interface detail: wrapper-only
- tooling: No working public API. The official client github.com/scribd/rscribd was archived in Oct 2019; community libs (JSCRIBD, rscribd) are dead against the current site. No rclone backend.
- composes with: 100 MB/record x unlimited records is the right shape, but the chain needs a browser-driven uploader and the download side is paywalled, so it can store but not serve.
- reliability: Uploaded documents get converted and can fail conversion; download availability is controlled by Scribd policy, not the uploader, so retrieval can be revoked unilaterally.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 MB max per document; no published account-level document or storage cap ("you can continue to upload more documents ... as often as you like"). Effectively per-record 100 MB x unlimited records.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Scribd supports multiple file formats, with a maximum size of 100MB'
  - [1] 2026-10-21: 'Scribd supports documents up to 100 megabytes in size'
  - [3] 2026-10-21: 'We reserve the right to restrict access to view or to download your Content'
  - [4] 2026-10-21: 'Scribd's official API client library (github.com/scribd/rscribd) was archived by the owner on October 24, 2019'
- sources:
  - [1] https://support.scribd.com/hc/en-us/articles/210134586-Troubleshooting-uploads-and-conversions
  - [2] https://support.scribd.com/hc/en-us/articles/210134786-Uploading-a-document-to-Scribd
  - [3] https://support.scribd.com/hc/en-us/articles/210129466-Uploader-Agreement-for-Scribd-and-Slideshare
  - [4] https://scraperly.com/scrape/scribd
