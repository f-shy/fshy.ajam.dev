# xREL.v3

> xrel.to | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xrel/ | JSON https://fshy.ajam.dev/api/v1/entity/xrel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xREL.v3

- `debrid/xrel` | qualifies-with-caveat | evidence documented | binding none | category scene release database (metadata and NFO, no download links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:47:02.741Z (live) | stale on 2026-12-26
- url https://www.xrel.to/
- price USD 0
- free tier: Release lists are readable without an account. The JSON API at api.xrel.to returned HTTP 403 and a bot challenge. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: release metadata, not an object | source: [1]
- retention: records persist; the release lists carry dated entries per category (console, TV, movies), newest first | source: [1]
- egress: no byte allowance: the site serves NFO text, screenshots and metadata, not files | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: The HTML lists were readable without an account. The API's authentication requirement was not established beyond the 403 challenge.
- interface: rest
- limits:
  - request-rate: no published limit on the pages read; the v2 API still answers HTTP 403 to an anonymous read [2]
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
  - [1] 2026-11-25: the site serves the xREL.v3 release database | capture: sha256:2e4a568b2772e54d55647fdce584257f050b4443933ec850db56eb6ff6a43de9 | quote: xREL.v3
  - [1] 2026-11-25: release lists carry the size of each scene release | capture: sha256:2e4a568b2772e54d55647fdce584257f050b4443933ec850db56eb6ff6a43de9 | quote: 8749 MB
  - [1] 2026-11-25: the HTML surface links NFO text without a download | capture: sha256:2e4a568b2772e54d55647fdce584257f050b4443933ec850db56eb6ff6a43de9 | quote: NFO ansehen
  - probe:https://api.xrel.to/v2/ 2026-11-25: the documented v2 API answered HTTP 403 on a fresh read | capture: sha256:b4558187c0bdae578a98b38c0d2752706ec064cabd01a942c47457f769d5b013 | quote: "status": 403
- sources:
  - [1] https://www.xrel.to/
  - [2] https://api.xrel.to/v2/
  - [3] https://api.xrel.to/v2/index.html
