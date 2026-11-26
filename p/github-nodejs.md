# jsdelivr as storage for release assets

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-nodejs/ | JSON https://fshy.ajam.dev/api/v1/entity/github-nodejs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## jsdelivr as storage for release assets

- `storage/jsdelivr-as-storage-for-release-assets` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.635Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-nodejs.md
- free tier: None reachable: The GitHub proxy only indexes git repo files. Release assets return 404, so the >2 GiB objects that make Releases interesting cannot be fronted by jsDelivr. They stay on GitHub's own Fastly. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: Single GitHub files larger than 20 MB are not supported by default; packages larger than 150 MB are not supported by default. | note: not applicable
- retention: Fetched files are kept permanently in S3: jsDelivr will continue to serve the stored copy forever even if the upstream package is deleted.
- egress: No bandwidth limits and no premium features; it is completely free to use. | metered: no
- identity: email
- interface: browser
- interface detail: URL-based CDN delivery under /gh/user/repo@version/file and /npm/package@version/file
- tooling: not documented
- composes with: A multi-CDN CDN chaining Cloudflare and Fastly with version fallback and a combine endpoint across /gh/ and /npm/ files.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: The GitHub proxy only indexes git repo files. Release assets return 404, so the >2 GiB objects that make Releases interesting cannot be fronted by jsDelivr — they stay on GitHub's own…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: The GitHub proxy only indexes git repo files. Release assets return 404, so the >2 GiB objects that make Releases interesting cannot be fronted by jsDelivr — they stay on GitHub's own…
  - [1] 2026-11-19: a GitHub release asset returns the Not Found page through the jsDelivr gh/ mirror path | capture: sha256:0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5 | quote: Not Found
  - [2] 2026-11-19: the jsDelivr README documents a URL-based CDN interface under /gh/ | capture: sha256:8411932f3ea41d9beb2f10bb8d43b3758a6278928e173de12f4d8cecf2bd7d13 | quote: Load any GitHub release, commit, or branch: /gh/user/repo@version/file
  - [2] 2026-11-19: the jsDelivr README states fetched files are kept permanently in S3 | capture: sha256:8411932f3ea41d9beb2f10bb8d43b3758a6278928e173de12f4d8cecf2bd7d13 | quote: We use a permanent S3 storage to ensure all files remain available even if GitHub goes down or a repository or a release is deleted by its author.
  - [2] 2026-11-19: the jsDelivr README states a 20 MB per-file limit for GitHub files | capture: sha256:8411932f3ea41d9beb2f10bb8d43b3758a6278928e173de12f4d8cecf2bd7d13 | quote: single files larger than 20 MB (in the case of GitHub) are not supported by default
  - [2] 2026-11-19: the jsDelivr README describes a multi-CDN design that chains several CDN providers | capture: sha256:8411932f3ea41d9beb2f10bb8d43b3758a6278928e173de12f4d8cecf2bd7d13 | quote: Unlike the competition, jsDelivr uses multiple CDN providers, resulting in the best possible uptime and performance.
  - [2] 2026-11-19: the jsDelivr README states no bandwidth limit | capture: sha256:8411932f3ea41d9beb2f10bb8d43b3758a6278928e173de12f4d8cecf2bd7d13 | quote: There are no bandwidth limits or premium features, and it's completely free to use.
- sources:
  - [1] https://github.com/nodejs/node/releases/download/v20.0.0/SHASUMS256.txt
  - [2] https://github.com/jsdelivr/jsdelivr/blob/master/README.md
