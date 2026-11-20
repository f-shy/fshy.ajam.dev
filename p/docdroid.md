# DocDroid

> docdroid.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docdroid/ | JSON https://fshy.ajam.dev/api/v1/entity/docdroid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DocDroid

- `storage/docdroid` | fails-egress | evidence reported | binding retention-clamped | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:31.792Z (live) | stale on 2026-12-04
- url https://www.docdroid.com
- free tier: Free/Standard account: 10 uploads per 24h, no document-count or storage figure published; Pro is "Unlimited Documents" for $19/month (3-day trial). Home page now flags free uploads as "Restricted Demo Mode". Only you can view them. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 60 requests/min; 10 uploads/24h standard (1,000/24h Pro); documents deleted after 60 days without views (third-party report); free sharing disabled. | days: 60 | source: [1] | note: not stated
- egress: Free tier cannot publish a public link at all: "Restricted Demo Mode. Only you can view your uploaded documents. To share documents with others, your need a Pro subscription." Pro is metered by subscription, not by GB. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - retention-clamped (binding): deleted after 60 days [1]
- limits note: 60 requests/min; 10 uploads/24h standard (1,000/24h Pro); documents deleted after 60 days without views (third-party report); free sharing disabled.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Real REST API (OpenAPI 3.0, v1.2.0) at https://www.docdroid.com/api with OAuth2 or personal access tokens: POST/GET/PUT/DELETE /document, webhooks, analytics. No rclone backend.
- composes with: Weak: 10 uploads/day x unlimited free accounts, but free documents are invisible to anyone else, so it only works as private storage and is capped by the 24h upload rate, not by bytes.
- reliability: Free-tier documents expire on inactivity and are never publicly served; the API is well-documented but the free tier is deliberately useless for serving.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free/Standard account: 10 uploads per 24h, no document-count or storage figure published; Pro is "Unlimited Documents" for $19/month (3-day trial). Home page now flags free uploads as "Restricted Demo Mode" — only you can view them.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Standard accounts: 10 uploads per 24h'; 'There is general limit of 60 requests per minute'; '429 Too Many Requests'
  - [2] 2026-10-21: 'Restricted Demo Mode. Only you can view your uploaded documents. To share documents with others, your need a Pro subscription.'
  - [3] 2026-10-21: Pro: 'Unlimited Documents', 3 day free trial, $19/month
  - [4] 2026-10-21: 'Free tier documents are deleted after 60 days without views'
  - [5] 2026-10-21: probe: POST -F file=@t.pdf -> 405 Method Not Allowed
  - [1] 2026-11-19: standard accounts are still limited to 10 uploads per 24h | capture: sha256:c0a618fea6d2c6c3c23bba1b54bd20f3cbaa6aa00cc89c4f30545c5b1c4cbd77 | quote: - Standard accounts: 10 uploads per 24h
  - [1] 2026-11-19: the API still has a 60 requests/minute general limit | capture: sha256:c0a618fea6d2c6c3c23bba1b54bd20f3cbaa6aa00cc89c4f30545c5b1c4cbd77 | quote: There is general limit of 60 requests per minute. Additional, the number of uploads is limited:
  - [2] 2026-11-19: the free tier still cannot publish a shareable public link without Pro | capture: sha256:368c15ae715623619ef4d4d1743fb741652e4c30ff23fc78dec1ec78874ccc2a | quote: Only you can view your uploaded documents. To share documents with others, your need a Pro subscription.
  - [3] 2026-11-19: Pro still offers unlimited documents | capture: sha256:19c39ec6566ee8e3846a8d5ed6fcee5cdcd799f7723b034f0996b94bd94626b1 | quote: - Unlimited Documents
- sources:
  - [1] https://www.docdroid.com/apidocs
  - [2] https://www.docdroid.com/
  - [3] https://www.docdroid.com/pricing
  - [4] https://listicler.com/tools/docdroid
  - [5] https://www.docdroid.com/upload
