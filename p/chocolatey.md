# Chocolatey Community

> chocolatey.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chocolatey/ | JSON https://fshy.ajam.dev/api/v1/entity/chocolatey.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chocolatey Community Repository

- `storage/chocolatey-community-repository` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://community.chocolatey.org
- disagrees on identity_kind: `storage/chocolatey-community-repository` says institution, `storage/chocolatey-community-repository-2` says email
- free tier: 200 MB hard per package: 'NOTE: 200MB is the maximum size of a package on the Chocolatey Community Repository. The package must download larger tools from a vendor site or mirror, or if possible, create semi-embedded packages.' | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 200 MB | bytes: 200000000 | source: [1] | note: not stated
- retention: per-object-cap: 200 MB per .nupkg. retention: indefinite for moderated packages; unlisted packages remain downloadable | source: [1] | note: not stated
- egress: Free serving, but every package is human-moderated before publication (CPMR rule set, VirusTotal scanning). | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-object-cap: 200 MB [1]
- limits note: per-object-cap: 200 MB per .nupkg. retention: indefinite for moderated packages; unlisted packages remain downloadable. request-rate: push is rate-limited per API key; moderation queue is the real gate.
- interface detail: rest
- tooling: `choco push` (write, needs API key), `choco install/download` (read), NuGet v2 OData at community.chocolatey.org/api/v2/. No rclone backend.
- composes with: unlimited packages x unlimited versions x 200 MB, but each package is virus-scanned and moderated. The 2 GB NuGet limitation means large content must be fetched at install time from elsewhere - which is the opposite of storage.
- reliability: 200 MB plus mandatory malware scanning plus human moderation. Cannot hold large binaries at all - Chocolatey's own docs route >2 GB content to external hosting.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 200 MB hard per package: 'NOTE: 200MB is the maximum size of a package on the Chocolatey Community Repository. The package must download larger tools from a vendor site or mirror, or if possible, create semi-embedded packages.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '200MB is the maximum size of a package on the Chocolatey Community Repository.'
  - [2] 2026-10-21: 'Chocolatey is built on top of NuGet, which itself does not gracefully handle packages that contain files over 2GB'
  - [3] 2026-10-21: probe: GET -> 200, 408 bytes (NuGet v2 OData service document live)
- sources:
  - [1] https://github.com/chocolatey-community/chocolatey-packages/blob/master/CONTRIBUTING.md
  - [2] https://docs.chocolatey.org/en-us/guides/create/create-large-files-package/
  - [3] https://community.chocolatey.org/api/v2/

## chocolatey community repository (community.chocolatey.org)

- `storage/chocolatey-community-repository-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.chocolatey.org/en-us/community-repository/moderation/package-validator/rules/cpmr0028/
- disagrees on identity_kind: `storage/chocolatey-community-repository` says institution, `storage/chocolatey-community-repository-2` says email
- free tier: none reachable: 150 MB max per package, moderation on every push, and active rate-limiting at ~100 installs/hour average with manual IP blocks that 'will not automatically expire'. Not a storage target. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: 150 MB max per package, moderation on every push, and active rate-limiting at ~100 installs/hour average with manual IP blocks that 'will not automatically expire'. Not a storage target.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 150 MB max per package, moderation on every push, and active rate-limiting at ~100 installs/hour average with manual IP blocks that 'will not automatically expire'. Not a storage target.
  - [2] 2026-10-21: cited as the basis of the rejection: 150 MB max per package, moderation on every push, and active rate-limiting at ~100 installs/hour average with manual IP blocks that 'will not automatically expire'. Not a storage target.
- sources:
  - [1] https://docs.chocolatey.org/en-us/community-repository/moderation/package-validator/rules/cpmr0028/
  - [2] https://docs.chocolatey.org/en-us/community-repository/community-packages-disclaimer/
