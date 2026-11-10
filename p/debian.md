# Debian

> debian.org | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debian/ | JSON https://fshy.ajam.dev/api/v1/entity/debian.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debian Salsa (salsa.debian.org) - GitLab with Generic package registry

- `storage/debian-salsa-gitlab-with-generic-package-registry` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://salsa.debian.org
- free tier: No published total-storage quota, but a fully published per-object table on the instance-configuration page. Package registry per-file caps: Generic 5 GiB, Conan 3 GiB, Maven 3 GiB, PyPI 3 GiB, Terraform 1 GiB, npm/NuGet 500 MiB, Helm 5 MiB. Core GitLab: max push size '-' (unlimited), max attachment 20 MiB, job artifact 750 MiB, pages 300 MiB, snippet 50 MiB, import remote file 10 GiB, download file 5 GiB. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-file caps: Generic 5 GiB | bytes: 5368709120 | source: [1] | note: not stated
- retention: per-object-cap: 5 GiB per Generic package file; 750 MiB per CI artifact; 300 MiB Pages. retention: indefinite for packages and repos (no pruning policy published on this page) | source: [1] | note: not stated
- egress: Free. Debian-hosted infrastructure with no billing, no per-GB meter, and package/registry downloads served straight from the instance. No Cloudflare dependency to worry about. | metered: no
- identity: institution
- interface: ssh, git
- limits:
  - write-gated: reviewed due to the high volume of spam registrations [1]
  - write-gated: approved [1]
  - per-object-cap (binding): per-file caps: Generic 5 GiB [1]
- limits note: per-object-cap: 5 GiB per Generic package file; 750 MiB per CI artifact; 300 MiB Pages. retention: indefinite for packages and repos. Documentation publishes rate limit sections for Files, Users, Groups, and Projects APIs. New user registrations are manually reviewed due to spam volumes.
- interface detail: git
- tooling: Full GitLab: `git` over SSH/HTTPS, GitLab Generic Package API (`PUT /projects/:id/packages/generic/:package_name/:version/:file_name`), CI runners, `glab`/`lab` CLIs, `python-gitlab`. Max push size is '-' (unlimited) which is the interesting cell - the per-object cap is on the registry, not on git.
- composes with: Unlimited projects per account x 5 GiB per Generic-package file x unlimited files per package version x unlimited versions. Plus unlimited-size git pushes as a second surface. The binding limit is account creation, not storage.
- reliability: Manual registration review is the whole story - it converts account-farming from an API call into a queue measured in days, which is fatal for the 'unlimited free orgs' pattern that made the Google-Drive-service-account trick work. Once in, the surface is clean and standard GitLab. Public read is fine (project pages and package downloads are anonymous).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '## Size Limits ... Maximum push size | - ... Maximum job artifact size | 750 MiB'; '## Package registry ... Generic | 5 GiB'
  - [2] 2026-10-21: 'New user registrations are manually reviewed due to the high volume of spam registrations. It may take a few days before a new account is approved.'
  - [1] 2026-10-21: 'There are several size limits in place for the package registry.' (table as quoted in quota)
- sources:
  - [1] https://salsa.debian.org/help/instance_configuration
  - [2] https://salsa.debian.org/users/sign_up

## debian snapshot

- `storage/debian-snapshot` | fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:11.230Z (live) | stale on 2026-12-05
- url https://snapshot.debian.org/
- free tier: none reachable: Read-only ingest of the Debian archive; no user write path at any size. 172 TB is theirs, not yours. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- evidence note: The front page of snapshot.debian.org, re-read on 2026-11-03, says the archive holds 172 TB and describes a read-only history of old Debian packages with no upload path. The registration detail in identity_cost stays a default, not a page reading.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Read-only ingest of the Debian archive; no user write path at any size. 172 TB is theirs, not yours.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Read-only ingest of the Debian archive; no user write path at any size. 172 TB is theirs, not yours.
  - [1] 2026-11-03: the archive holds 172 TB of Debian package data | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: Snapshot is currently holding 172TB of data.
  - [1] 2026-11-03: the service is a read-only history of the Debian archive | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: The snapshot archive is a wayback machine that allows access to old packages based on dates and version numbers.
  - [1] 2026-11-04: the archive holds 172 TB of Debian package data | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: Snapshot is currently holding 172TB of data.
  - [1] 2026-11-04: the service is a read-only history of the Debian archive with no upload path described | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: The snapshot archive is a wayback machine that allows access to old packages based on dates and version numbers.
- sources:
  - [1] https://snapshot.debian.org/

## Debian snapshot archive (snapshot.debian.org)

- `storage/debian-snapshot-archive` | fails-quota | evidence documented | binding none | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:24:11.228Z (live) | stale on 2026-12-05
- url https://snapshot.debian.org
- free tier: No user storage: snapshot is a read-only archive of the Debian package archives; the site news dated 2024-10-08 says it holds 172 TB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, two sites (Glasklar + LeaseWeb). Netfilter rate limiting was explicitly disabled ('It will be replaced by rate limiting on the HTTP layer'). | metered: no
- identity: anonymous | detail: none: an unauthenticated HTTPS GET of /mr/timestamp/ returned HTTP 200; there is no write path to register for.
- interface: rest, rclone
- limits note: per-object-cap: N/A (read-only). retention: total - every snapshot timestamp from 2005 to present is preserved. request-rate: HTTP-layer rate limiting in place of the old netfilter limit.
- interface detail: rest
- tooling: apt with a dated sources.list entry, `debian-snapshot` machine-usable API at /mr/ (e.g. /mr/timestamp/), plain HTTPS. No rclone backend.
- composes with: None - you cannot add content. Valuable only as a source of old Debian packages for a corpus, not as a place to put your data.
- reliability: Read-only by construction. Included to close the category: Debian's snapshot is a preservation tool, not storage you can use. API verified live.
- notes: No user quota because there is no user write path - snapshot ingests the Debian archive itself. Scale reference from the site's own news: 'Snapshot is currently holding 172TB of data' (2024-10-08), up from 135 TB (2022) and 24 TB (2014), on 2 x 164 TB RAID6 arrays.
- evidence note: The front page of snapshot.debian.org, re-read on 2026-11-03, says the archive holds 172 TB and describes a read-only history of old Debian packages; the unauthenticated GET of /mr/timestamp/ succeeded on the same date. The free-tier and identity fields cite those rows.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No user quota because there is no user write path - snapshot ingests the Debian archive itself. Scale reference from the site's own news: 'Snapshot is currently holding 172TB of data' (2024-10-08), up from 135 TB (2022) and 24 TB (2014), on 2 x 164 TB RAID6 arrays.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Snapshot is currently holding 172TB of data'; 'The Netfilter rate limiting has been disabled ... rate limiting on the HTTP layer'
  - [2] 2026-10-21: probe: GET -> 200 JSON, debian timestamps from 20050312T000000Z onward
  - withheld 2026-10-21: probe: GET /archive/debian/20250101T000000Z/dists/bookworm/Release -> 302 (redirect to a dated snapshot; live)
  - [1] 2026-11-03: the archive holds 172 TB; it is the service's own archive of Debian packages | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: Snapshot is currently holding 172TB of data.
  - probe:snapshot.debian.org 2026-11-03: an unauthenticated GET of /mr/timestamp/ returned HTTP 200 JSON | capture: sha256:c71257fbbb4ee4ffd1db5bda4fea0a2062d6bff280946f8b02854ac5734366c0 | quote: "status": 200
  - [1] 2026-11-03: request limiting moved to the HTTP layer; no threshold is published | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: The Netfilter rate limiting has been disabled. It will be replaced by rate limiting on the HTTP layer, which should be easier for clients to deal with.
  - [1] 2026-11-04: the archive holds 172 TB of Debian package data | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: Snapshot is currently holding 172TB of data.
  - [1] 2026-11-04: the service is a read-only history of the Debian archive with no upload path described | capture: sha256:fbc25938e59979ae067326f45ea1187aa395af49532a52afc9670127e6f5ee00 | quote: The snapshot archive is a wayback machine that allows access to old packages based on dates and version numbers.
- sources:
  - [1] https://snapshot.debian.org/
  - [2] https://snapshot.debian.org/mr/timestamp/
