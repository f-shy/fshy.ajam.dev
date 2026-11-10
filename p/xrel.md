# xREL.v3

> xrel.to | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xrel/ | JSON https://fshy.ajam.dev/api/v1/entity/xrel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xREL.v3

- `debrid/xrel` | qualifies-with-caveat | evidence documented | binding none | category scene release database (metadata and NFO, no download links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://www.xrel.to/
- price USD 0
- free tier: Release lists are readable without an account. The JSON API at api.xrel.to returned HTTP 403 and a bot challenge. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: release metadata, not an object | source: [1]
- retention: records persist; the release lists carry dated entries per category (console, TV, movies), newest first | source: [1]
- egress: no byte allowance: the site serves NFO text, screenshots and metadata, not files | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: The HTML lists were readable without an account. The API's authentication requirement was not established beyond the 403 challenge.
- interface: rest
- limits:
  - request-rate: no published limit on the pages read; the API returned a 403 bot challenge [2]
- limits note: The challenge is the first obstacle, not a quota: the reader saw 'bot challenge' with a 5-word body at HTTP 403.
- binding note: An API challenge is not one of the seven constraints and no byte quota exists; the API challenge comes first and an unpublished rate would follow.
- interface detail: A documented JSON API under api.xrel.to/v2/ (the v2 index path returned 404 from nginx, and /v2/ returned a 403 challenge), plus HTML release lists per category.
- endpoint: https://api.xrel.to/v2/
- tooling: HTTP client for the API when the challenge permits; otherwise HTML scraping of the release lists. Nothing to download, so no rclone or debrid tool applies.
- composes with: Use it as the metadata layer: given a release name from a DDL index, xREL gives the group, the date, the NFO and the IMDb/TVDB id, which is what makes a release name resolvable to a title.
- reliability: Cloudflare-style bot screening sits in front of the API, so a client that works today can be challenged tomorrow; the HTML surface answered normally.
- notes: Included because it is the metadata layer a DDL pipeline needs to turn 'Some.Release.2026.1080p-GRP' into a title, and because it is the clean example of the debrid challenge rule: HTML readable, API challenged, documented as unverified rather than rejected.
- evidence note: The home page was read on 2026-10-23 and the API challenge was captured. Getting one API response through a permitted client confirms the real endpoint shape and any rate limit.
- extras:
  - api_status_observed: 403
  - challenge: yes
  - has_download_links: no
- evidence:
  - [1] 2026-10-23: live German scene release database, title 'xREL.v3 - Release & NFO Source #1', release lists with NFO links and sizes
  - [2] 2026-10-23: HTTP 403 with a 5-word body: the reader classified it as a bot challenge, so no API content was read
  - [3] 2026-10-23: HTTP 404 from nginx, so that documentation path does not exist
- sources:
  - [1] https://www.xrel.to/
  - [2] https://api.xrel.to/v2/
  - [3] https://api.xrel.to/v2/index.html
