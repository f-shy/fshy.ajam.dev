# IAS3 old-version retention

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ias3-old-version-retention/ | JSON https://fshy.ajam.dev/api/v1/entity/ias3-old-version-retention.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IAS3 old-version retention (x-archive-keep-old-version)

- `storage/ias3-old-version-retention` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T12:15:44.836Z (live) | stale on 2026-12-10
- url https://archive.org/developers/ias3.html
- free tier: No quota of its own. It multiplies the 1TB item limit by however many versions you PUT. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Guidance, not an enforced cap: a single file in an item should not be larger than ~500 to ~700 GB, with 500 GB the recommended limit. | source: [1] | note: The same help page recommends items with fewer than 10,000 files, where the files do not exceed 1TB; the API allows up to 250,000 files.
- retention: PUT and DELETE do not keep old versions unless the x-archive-keep-old-version:1 header is sent. | source: [1] | note: For multipart uploads the header must be specified when the multipart upload is completed..
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
  - [1] 2026-11-19:  | capture: sha256:467a16d2e9fc7150fbf1ca1ddaeedf3c9ea54b0827e14939343fa4a811c5848c | quote: Normally PUT and DELETE do not keep old versions of files around. To have the archive keep old versions of the object you can add the header: `x-archive-keep-old-version:1` Saved versions will be placed in `history/files/$key.~N~`
  - [2] 2026-11-25: the Internet Archive help centre advises a single file stay under about 500 to 700 GB | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [2] 2026-11-25: files in an item are recommended not to exceed 1TB | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: We recommend creating items that have less than 10,000 files, and where the files do not exceed 1TB.
  - [1] 2026-11-25: old versions are kept only when the header is set | capture: sha256:467a16d2e9fc7150fbf1ca1ddaeedf3c9ea54b0827e14939343fa4a811c5848c | quote: Normally PUT and DELETE do not keep old versions of files around. To have the archive keep old versions of the object you can add the header: `x-archive-keep-old-version:1`
  - [1] 2026-11-25: for multipart the header is set at completion | capture: sha256:467a16d2e9fc7150fbf1ca1ddaeedf3c9ea54b0827e14939343fa4a811c5848c | quote: (For multipart, the `x-archive-keep-old-version` header must be specified at the time the multipart upload is completed)
- sources:
  - [1] https://archive.org/developers/ias3.html
  - [2] https://help.archive.org/help/uploading-troubleshooting/
