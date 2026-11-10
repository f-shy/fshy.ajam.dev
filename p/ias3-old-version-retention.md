# IAS3 old-version retention

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ias3-old-version-retention/ | JSON https://fshy.ajam.dev/api/v1/entity/ias3-old-version-retention.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IAS3 old-version retention (x-archive-keep-old-version)

- `storage/ias3-old-version-retention` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://archive.org/developers/ias3.html
- free tier: No quota of its own. It multiplies the 1TB item limit by however many versions you PUT. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free (history files are served through the same item path) | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: s3, rclone
- limits note: For multipart the header must be set at multipart-complete time; each version re-enters the per-item queue.
- interface detail: s3
- tooling: raw IAS3 PUT header; rclone does not expose it, so a thin curl/requests shim is needed
- composes with: A 20TiB cold archive can be stored as ~20 versions of a 1TB item if the payload changes, or used as a free append-only version store per key. Combined with x-archive-cascade-delete:1 for cleanup.
- reliability: Unofficial-ish surface: documented but not exposed by any major client, so it is untested at scale and easy to orphan copies with.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-21: 'For multipart, the x-archive-keep-old-version header must be specified at the time the multipart upload is completed'
- sources:
  - [1] https://archive.org/developers/ias3.html
