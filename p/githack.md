# raw.githack.com

> githack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/githack/ | JSON https://fshy.ajam.dev/api/v1/entity/githack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## raw.githack.com (CDN for GitHub/GitLab/Bitbucket raw files)

- `storage/raw-githack-com` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:17.919Z (live) | stale on 2026-12-10
- url https://raw.githack.com/
- free tier: No quota of its own; ceiling is GitHub's 100 MiB hard repo file block. Probed a 50,901,339-byte GitHub file: HTTP 200, full length, sha256 fd112e5b… . A 3,408,573-byte file came back with sha256 55fb913b… — byte-identical to jsDelivr's copy of the same file, which is the cleanest proof it does not re-encode. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: GitHub's 100 MiB | bytes: 104857600 | source: [1] | note: The homepage states permanent per-URL caching and gives no per-file size cap.
- retention: Files are cached permanently based on the URL, query string is ignored | source: [1] | note: CDN URLs are cached permanently based on the exact URL.
- egress: Both URL types are served through Cloudflare's global network. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-ip-shaping: 1 TiB/day [1]
  - per-object-cap (binding): per-object-cap: GitHub's 100 MiB [1]
- limits note: Per-object-cap: GitHub's 100 MiB repo block is the real ceiling (50 MB proven). commit-ref must be used for permanence; branch refs are re-fetched within minutes. HTML is gated behind an interstitial confirmation page. Irrelevant for blobs, fatal if you need to serve HTML.
- interface detail: rest
- tooling: Two URL forms: raw.githack.com/<owner>/<repo>/<branch|tag>/<path> (development, minutes of cache) and rawcdn.githack.com/<owner>/<repo>/<tag|commit>/<path> (production, cached permanently). Plain GET.
- composes with: Use a tag or commit ref in the URL instead of a branch name to serve a new version.
- reliability: unverified: https://raw.githack.com/ answered HTTP 200 on 2026-11-11 but serves the rawgit.hack homepage, which states no storage quota, per-file cap or traffic figure.
- notes: Files are cached permanently based on the URL, query string is ignored
- evidence note: the same as reliability
- evidence:
  - [2] 2026-10-21: HTTP 200, 50,901,339 bytes, sha256 fd112e5b… (probed)
  - [3] 2026-10-21: 3,408,573 bytes, sha256 55fb913b… identical to the jsDelivr copy (probed)
  - [4] 2026-10-21: HTTP 301 → raw.githubusercontent.com (branch form degrades to a redirect, probed)
  - [1] 2026-10-21: 'Serving 479M+ requests and 46TB+ of traffic monthly'; 'Files are cached permanently based on the URL, query string is ignored'
  - [1] 2026-11-11: the homepage states the permanent per-URL caching behaviour | capture: sha256:458b754ffa07d2f35d335738d37d71f6efb1e97e59ba0ebc1a3cc9ef599f34c8 | quote: Files are cached permanently based on the URL, query string is ignored
  - probe:https://raw.githack.com/ 2026-11-11: the cited URL answered HTTP 200 | capture: sha256:a327bc52e25608012ddb803e56be6310d09914ff6b96eb6add561d38eef4a9aa | quote: "status": 200
  - [1] 2026-11-19: the homepage still states permanent per-URL caching | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: Files are cached permanently based on the URL, query string is ignored
  - [1] 2026-11-25: the first-party homepage states permanent per-URL caching and no per-file size cap | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: Files are cached permanently based on the URL, query string is ignored
  - [1] 2026-11-25: the first-party homepage states permanent caching for CDN URLs | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: CDN URLs are cached permanently based on the exact URL, which makes them fast and reliable for production use.
  - [1] 2026-11-25: the first-party homepage states permanent per-URL caching | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: Files are cached permanently based on the URL, query string is ignored
  - [1] 2026-11-25: the first-party homepage documents tag or commit refs for serving new versions | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: To serve a new version, use a tag or commit ref in the URL instead of a branch name — e.g. `/user/repo/TAG/file` instead of `/user/repo/BRANCH/file`.
  - [1] 2026-11-25: the first-party homepage states that both URL types are served through Cloudflare | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: Both URL types are served through [Cloudflare's](https://cloudflare.com/) global network, but they differ in how long they're cached.
  - [1] 2026-11-25: the first-party homepage still states permanent per-URL caching | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: Files are cached permanently based on the URL, query string is ignored
  - [1] 2026-11-25: the first-party homepage still states permanent CDN URL caching | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: CDN URLs are cached permanently based on the exact URL, which makes them fast and reliable for production use.
  - [1] 2026-11-25: the first-party homepage still documents tag or commit URL refs | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: To serve a new version, use a tag or commit ref in the URL instead of a branch name — e.g. `/user/repo/TAG/file` instead of `/user/repo/BRANCH/file`.
  - [1] 2026-11-25: the first-party homepage still states Cloudflare serving for both URL types | capture: sha256:5e592d410d2968781671700b4c10151dbea4b9b23fa79c41f41c776ba9c9a563 | quote: Both URL types are served through [Cloudflare's](https://cloudflare.com/) global network, but they differ in how long they're cached.
- sources:
  - [1] https://raw.githack.com/
  - [2] https://raw.githack.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb
  - [3] https://raw.githack.com/P3TERX/GeoLite.mmdb/download/GeoLite2-Country.mmdb
  - [4] https://raw.githack.com/MetaCubeX/meta-rules-dat/release/geoip.dat
