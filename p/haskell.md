# Hackage

> haskell.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/haskell/ | JSON https://fshy.ajam.dev/api/v1/entity/haskell.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hackage (hackage.haskell.org)

- `storage/hackage` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hackage.haskell.org
- disagrees on identity_kind: `storage/hackage` says institution, `storage/hackage-2` says email
- disagrees on verdict: `storage/hackage` says qualifies-with-caveat, `storage/hackage-2` says fails-quota
- free tier: No published per-package or total quota found on the upload page or the server API. Uploads are permanent: 'Upload and publish a package permanently' and 'You can only upload a package version once and this cannot be undone'. Real large package verified: pandoc-3.5.tar.gz is 7,483,625 bytes. Packages must be `cabal sdist` output (gzipped tar with package.cabal). | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: No published per-package or total quota found on the upload page or the server API. Uploads are permanent: 'Upload and publish a package permanently' and 'You can only upload a package version once and this cannot be undone' | source: [1] | note: not stated
- egress: Free. Content is served from hackage.haskell.org and the hackage-content.haskell.org CDN. No billing, no bandwidth meter. | metered: no
- identity: institution
- interface: rest
- limits note: per-object-cap: none documented; 7.4 MB verified, and the 100 MB-class limits seen in other ecosystems are not stated here - likely a server-side request size limit that is undocumented. IMPORTANT retention property: uploads are immutable and permanent (no delete, no re-upload of the same version), which is exactly what an archive workload wants. request-rate: not documented.
- interface detail: rest
- tooling: `cabal upload` / `stack upload` (write), `hup` (a dedicated upload client, hackage.haskell.org/package/hup), Hackage server API at hackage-origin.haskell.org/api (open, 62,403-byte route listing), plain HTTPS tarball GET (read).
- composes with: unlimited packages x unlimited versions per package (versions are never deleted and the index keeps all of them) x unlimited free Hackage accounts. Content must be a Cabal sdist, but the sdist can contain arbitrary files declared in extra-source-files - so a multi-GB blob can be shipped as a package's data. Multiply: N accounts x M packages x K versions.
- reliability: Immutable by design - a bad upload cannot be deleted, which is irreversibility risk in the other direction. No documented byte ceiling means the ceiling is empirical and could change without notice. Read path is plain static files and reliable.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, 7,483,625 bytes
  - [3] 2026-10-21: probe: GET -> 200, 62,403 bytes (open route listing)
  - [1] 2026-10-21: 'Upload and publish a package permanently ... You can only upload a package version once and this cannot be undone'
- sources:
  - [1] https://hackage.haskell.org/upload
  - [2] https://hackage.haskell.org/package/pandoc-3.5/pandoc-3.5.tar.gz
  - [3] https://hackage-origin.haskell.org/api

## hackage (haskell)

- `storage/hackage-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hackage.haskell.org/upload
- disagrees on identity_kind: `storage/hackage` says institution, `storage/hackage-2` says email
- disagrees on verdict: `storage/hackage` says qualifies-with-caveat, `storage/hackage-2` says fails-quota
- free tier: None reachable: No documented size limit and no documented quota. Could not establish any number from the upload page, the FAQ, or the server source (the upload handler has no size guard visible in Distrib. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: No documented size limit and no documented quota — could not establish any number from the upload page, the FAQ, or the server source (the upload handler has no size guard visible in…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No documented size limit and no documented quota — could not establish any number from the upload page, the FAQ, or the server source the upload handler has no size guard visible in Distrib
  - [2] 2026-10-21: cited as the basis of the rejection: No documented size limit and no documented quota — could not establish any number from the upload page, the FAQ, or the server source the upload handler has no size guard visible in Distrib
- sources:
  - [1] https://hackage.haskell.org/upload
  - [2] https://raw.githubusercontent.com/haskell/hackage-server/master/src/Distribution/Server/Features/Upload.hs
