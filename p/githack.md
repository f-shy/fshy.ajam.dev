# raw.githack.com

> githack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/githack/ | JSON https://fshy.ajam.dev/api/v1/entity/githack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## raw.githack.com (CDN for GitHub/GitLab/Bitbucket raw files)

- `storage/raw-githack-com` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://raw.githack.com/
- free tier: No quota of its own; ceiling is GitHub's 100 MiB hard repo file block. Probed a 50,901,339-byte GitHub file: HTTP 200, full length, sha256 fd112e5b… . A 3,408,573-byte file came back with sha256 55fb913b… — byte-identical to jsDelivr's copy of the same file, which is the cleanest proof it does not re-encode. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: GitHub's 100 MiB | bytes: 104857600 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, no account, no key. Cloudflare-fronted with permanent per-URL caching on the tag/commit form. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-ip-shaping: 1 TiB/day [1]
  - per-object-cap (binding): per-object-cap: GitHub's 100 MiB [1]
- limits note: Per-object-cap: GitHub's 100 MiB repo block is the real ceiling (50 MB proven). commit-ref must be used for permanence; branch refs are re-fetched within minutes. HTML is gated behind an interstitial confirmation page. Irrelevant for blobs, fatal if you need to serve HTML.
- interface detail: rest
- tooling: Two URL forms: raw.githack.com/<owner>/<repo>/<branch|tag>/<path> (development, minutes of cache) and rawcdn.githack.com/<owner>/<repo>/<tag|commit>/<path> (production, cached permanently). Plain GET.
- composes with: Serves GitHub files at 50 MB where jsDelivr's /gh/ stops at 20 MB. That is the single most useful number here, because it doubles the shard size on an otherwise identical origin. Use rawcdn.githack.com for immutable shards and jsDelivr /gh/ as a second mirror for the smaller ones.
- reliability: Small independent operator. Its own homepage says it serves 479M+ requests and 46 TB+ of traffic monthly, which is ~0.2% of the 1 TiB/day requirement, so treat it as a mirror, never the primary. A branch-ref URL 301s to raw.githubusercontent.com (i.e. it silently stops being a CDN and bills GitHub instead).
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: HTTP 200, 50,901,339 bytes, sha256 fd112e5b… (probed)
  - [3] 2026-10-21: 3,408,573 bytes, sha256 55fb913b… identical to the jsDelivr copy (probed)
  - [4] 2026-10-21: HTTP 301 → raw.githubusercontent.com (branch form degrades to a redirect, probed)
  - [1] 2026-10-21: 'Serving 479M+ requests and 46TB+ of traffic monthly'; 'Files are cached permanently based on the URL, query string is ignored'
- sources:
  - [1] https://raw.githack.com/
  - [2] https://raw.githack.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb
  - [3] https://raw.githack.com/P3TERX/GeoLite.mmdb/download/GeoLite2-Country.mmdb
  - [4] https://raw.githack.com/MetaCubeX/meta-rules-dat/release/geoip.dat
