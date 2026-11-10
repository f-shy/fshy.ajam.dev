# npm public registry

> npmjs.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/npmjs/ | JSON https://fshy.ajam.dev/api/v1/entity/npmjs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## npm public registry (registry.npmjs.org)

- `storage/npm-public-registry` | qualifies | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.npmjs.com
- free tier: No total storage quota, no per-account package cap ('Unlimited public packages'. Npm Pro page), no cap on versions per package. The only bounds are per-artefact and per-packument: empirically ~200 MB per tarball (no documented figure anywhere) and 100 MB per packument (the accumulated metadata document for all versions of one package). | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: | Append-only and durable. 2018 tarballs still serve with the original Last-Modified. | source: [1] | note: not stated
- egress: Free and unmetered, Cloudflare-fronted. Probe: GET of a 70 MB tarball returned Server: cloudflare, Cache-Control: 'public, immutable, max-age=31557600', Accept-Ranges: bytes; ranged GET returned 206 Partial Content. No auth, no signed URL, no expiry. | metered: no
- identity: email
- interface: rest, rclone, cli
- limits note: ~200 MB per tarball (413 Payload Too Large above that: one reporter hits it at 200 MB, pretendard's 229.9 MB tarball was rejected with E413; a 70 MB tarball serves fine). 100 MB per packument before compression — this is a version-count cap, not a byte cap. Publish is rate limited (429s reported in CI, github.com/npm/cli/issues/8507); exact rate not published. Versions are immutable and cannot be deleted after 72h unless the package has <300 weekly downloads and a single maintainer (unpublish policy). An unpublish frees the name's version slot only for new versions, never reuses a version string.
- interface detail: rest
- tooling: Two-verb REST: PUT /:pkg with a JSON body containing base64 _attachments (or the standard npm publish flow), GET /:pkg/-/:pkg-:ver.tgz for the blob. Named clients: npm CLI, libnpmpublish (github.com/npm/libnpmpublish), and purpose-built chunking wrappers. Gist github.com/yulioaj290/e81d3a59ec00247f00ec34db378fae6c (shell script that splits a file into N MB chunks, publishes each as its own npm package, adds the rest as dependencies of chunk 1, and emits an unzip script), indexzero/npm-publish-split-stream (4 stars, streams a publish request without buffering). No rclone backend.
- composes with: Unlimited public packages per account with unlimited versions per package. Version counts are bounded by the 100 MB packument size limit. Individual tarballs allow up to approximately 200 MB per package release.
- reliability: Append-only and durable. 2018 tarballs still serve with the original Last-Modified. Two hard failure modes for a bulk workload: silent 413 at ~200 MB (undocumented, so budget 150 MB), and packument bloat refusing all new versions for the whole package once it crosses 100 MB. Automated mass publishing gets 429'd.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Unlimited public packages'
  - [2] 2026-10-21: the 100 MB packument limit explained with the Drizzle ORM outage (June 2026); 'the NPM registry will simply refuse any new versions from being published'
  - [3] 2026-10-21: 'once my package goes above 200MB I receive this error ... 413 Payload Too Large - PUT https://registry.npmjs.org/'
  - [4] 2026-10-21: pretendard 229.9 MB tarball -> npm ERR! code E413
  - [5] 2026-10-21: 72h / <300 downloads / single-owner deletion rules; 'Registry data is immutable'
  - [6] 2026-10-21: probe: HEAD -> 200, Content-Length: 70026530, Cache-Control: public, immutable, max-age=31557600, Server: cloudflare
  - withheld 2026-10-21: probe: GET same URL with Range: bytes=0-1023 -> 206 Partial Content, Content-Range: bytes 0-1023/70026530
  - [7] 2026-10-21: probe: GET -> 200, Content-Length: 11180437 (packument already 11 MB, i.e. 11% of the 100 MB ceiling, for a metadata-only package)
  - [8] 2026-10-21: probe: anonymous PUT -> 404 Not Found, i.e. publishing requires a token (no anonymous writes)
- sources:
  - [1] https://www.npmjs.com/products/pro
  - [2] https://www.vlt.io/blog/packument-size-limits
  - [3] https://github.com/npm/documentation/issues/1691
  - [4] https://github.com/npm/cli/issues/4794
  - [5] https://docs.npmjs.com/policies/unpublish/
  - [6] https://registry.npmjs.org/onnxruntime-node/-/onnxruntime-node-1.20.1.tgz
  - [7] https://registry.npmjs.org/@types/node
  - [8] https://registry.npmjs.org/kimi-probe-abc-123
