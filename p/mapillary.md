# Mapillary

> mapillary.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mapillary/ | JSON https://fshy.ajam.dev/api/v1/entity/mapillary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mapillary (Meta)

- `storage/mapillary` | qualifies-with-caveat | evidence reported | binding request-rate | category crowdsourced street-level imagery
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mapillary.com
- free tier: 'unlimited storage' per Mapillary's own blog: 'Mapillary offers unlimited storage and makes imagery publicly available ... any organization, public or private, can store and host their archive of street-level imagery at no cost.' No published per-account byte cap. 2.4 billion images hosted. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free for all use, including commercial, since the Meta acquisition (2020). But API reads are rate-limited, not byte-metered. | metered: no
- identity: email | detail: Email. Confirmed: graph.mapillary.com with no token returns {"message":"Invalid OAuth 2.0 Access Token","code":190}, and signup is a Meta/Facebook or email account with a free developer token; no affiliation check. help.mapillary.com article 'An Introduction to Mapillary' says 'All you need to start contributing is your smartphone and our mobile app.'.
- interface: graph, cli
- limits:
  - request-rate (binding): 50,000 requests/minute [1]
  - request-rate (binding): 50,000 requests/DAY [1]
- limits note: per-image: 200 MP resolution ceiling, landscape orientation, EXIF GPS + timestamp required. Read side: graph.mapillary.com 50,000 requests/minute/app; tiles.mapillary.com 50,000 requests/DAY. The forum thread 'Can and does someone replicate the Mapillary images database?' states outright that the free plan's 50,000-image limit blocks bulk re-download.
- binding note: calls are bounded rather than bytes, which is fatal to a nightly job on a monthly counter
- interface detail: Graph API at graph.mapillary.com (images, map features, detections); upload via mapillary_tools CLI or Desktop Uploader
- tooling: `mapillary_tools` (pip), Mapillary Desktop Uploader, official Python SDK, MapillaryJS
- composes with: Writes are geographically anchored, so this is a corpus, not a bucket. Read path returns tile/thumb URLs; a normal CDN in front works, but origin fetch is token-gated.
- reliability: Uploads are unmetered, while bulk retrieval is rate-limited to 50,000 vector tile requests per day via API.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 200 with {"error":{"message":"Invalid OAuth 2.0 Access Token","type":"MLYApiException","code":190}} (token-gated read, confirmed live)
  - [3] 2026-10-21: 'No, Mapillary is 100% free to use—for any use case! ... we have open-sourced our imagery'
  - [4] 2026-10-21: 'upper limit of 200 MP to image resolution'
  - [5] 2026-10-21: 50,000 requests/minute/app on graph.mapillary.com
  - [6] 2026-10-21: 'The rate limit for tiles is 50,000 requests per day'
  - withheld 2026-10-21: blog.mapillary.com 2024-07-08 — 'Mapillary offers unlimited storage' search snippet only
- sources:
  - [1] https://blog.mapillary.com/update/2024/07/08/expanding-public-street-level-imagery-access.html
  - [2] https://graph.mapillary.com/images?fields=thumb_2048_url&limit=1
  - [3] https://help.mapillary.com/hc/en-us/articles/8348198426396-Mapillary-FAQ
  - [4] https://help.mapillary.com/hc/en-us/articles/115001472029
  - [5] https://forum.mapillary.com/t/hitting-request-limit/5820
  - [6] https://forum.mapillary.com/t/receiving-html-response-instead-of-json/8336
