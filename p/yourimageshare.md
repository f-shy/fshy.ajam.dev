# YourImageShare URL uploader

> yourimageshare.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yourimageshare/ | JSON https://fshy.ajam.dev/api/v1/entity/yourimageshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YourImageShare URL uploader

- `debrid/yourimageshare` | qualifies-with-caveat | evidence documented | binding per-object-cap | category URL-to-host relay for images and video (server fetches, re-hosts, returns a direct link) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://yourimageshare.com/tools/upload-from-url
- price USD 0
- free tier: 'This URL uploader takes a link to an image or video that is already online and uploads it for you. You do not download the file first, and you do not need an account.' Price: Free. Account: Not needed. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: Batch of up to 40 URLs per upload, one per line.
- per-object cap: 'Maximum file size | 200MB per file'. | bytes: 209715200 | source: [1]
- retention: unverified: the page markets 'a permanent direct link' but publishes no retention period or deletion policy on this page. | source: [1]
- egress: Direct links to the re-hosted copy; no byte allowance or hotlink policy stated on this page. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: 'Account: Not needed' in the feature table, and no login field in the flow.
- interface: unknown
- limits:
  - per-object-cap (binding): 200 MB per file [1]
  - request-rate: 40 URLs per upload; no daily count stated [1]
- limits note: The type whitelist is the tighter constraint than either number: no archives, no documents, no audio.
- binding note: 200 MB per media file binds long before any count could: a monthly transfer of 1 TiB would need 5,243 files, and any archive over 200 MB cannot pass at all.
- interface detail: A web form taking up to 40 URLs per submit, returning a page link, direct link, embed code, HTML, BBCode and Markdown per file. No API documentation. Allowed types: JPG, PNG, GIF, WEBP, AVIF, BMP, TIFF, HEIC, HEIF and MP4, WEBM, AVI.
- tooling: Browser. The automated path is blocked: a plain HTTP client got HTTP 403 with a challenge signature, so a wrapper needs a real browser session.
- composes with: It moves an image or clip from a dying host to a live one without using local bandwidth, which is the cheapest fix for hotlink-blocked or expiring media. It is not usable for archives or datasets.
- reliability: The site refuses non-browser clients (HTTP 403 with a challenge on a plain GET), so unattended use needs a browser driver. Re-hosted copies depend on this operator's retention, which is unpublished.
- notes: The cleanest anonymous URL-pull found, and the narrowest: media only, 200 MB. It answers 'no install, no account' for one file type class and nothing else.
- evidence note: The caps and the type list are quoted from the live page; the 403 is measured. No URL was actually re-hosted, so the flow itself is untested.
- extras:
  - urls_per_upload: 40
  - allowed_types: JPG, PNG, GIF, WEBP, AVIF, BMP, TIFF, HEIC, HEIF, MP4, WEBM, AVI
  - bot_gate: HTTP 403 to a plain client
- evidence:
  - [1] 2026-10-23: 'Account: Not needed', 'URLs per upload: Up to 40', 'Maximum file size: 200MB per file', and the image/video type whitelist
  - probe:https://yourimageshare.com/tools/upload-from-url 2026-10-23: a plain client is refused: HTTP 403, 5525 bytes, sha256 a2abe9fc99966465..., challenge detected
- sources:
  - [1] https://yourimageshare.com/tools/upload-from-url
