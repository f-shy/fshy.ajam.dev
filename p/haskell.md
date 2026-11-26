# Hackage

> haskell.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/haskell/ | JSON https://fshy.ajam.dev/api/v1/entity/haskell.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hackage (hackage.haskell.org)

- `storage/hackage` | qualifies-with-caveat | evidence reported | binding none | category registry
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:15:42.695Z (live) | stale on 2026-12-10
- url https://hackage.haskell.org
- disagrees on verdict: `storage/hackage` says qualifies-with-caveat, `storage/hackage-2` says fails-quota
- free tier: No published per-package or total quota found on the upload page or the server API. Uploads are permanent: 'Upload and publish a package permanently' and 'You can only upload a package version once and this cannot be undone'. Real large package verified: pandoc-3.5.tar.gz is 7,483,625 bytes. Packages must be `cabal sdist` output (gzipped tar with package.cabal). | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The upload page names no per-package size limit. It states that each package added to the index has a cost of operation and maintenance.
- retention: A package version can be uploaded only once and this cannot be undone. The operators retain the right to remove packages that are not under licenses that are open source in spirit, or that conflict with their ability to operate the service. | source: [1] | note: not stated
- egress: Free. Content is served from hackage.haskell.org and the hackage-content.haskell.org CDN. No billing, no bandwidth meter. | metered: no
- identity: email | detail: You can modify various settings for your account, including changing the email address and password, setting email notification preferences, as well as creating authentication tokens, at the [account management page](https://hackage.haskell.org/users/account-management).
- interface: rest
- limits note: per-object-cap: none documented; 7.4 MB verified, and the 100 MB-class limits seen in other ecosystems are not stated here - likely a server-side request size limit that is undocumented. IMPORTANT retention property: uploads are immutable and permanent (no delete, no re-upload of the same version), which is exactly what an archive workload wants. request-rate: not documented.
- interface detail: rest
- tooling: `cabal upload` / `stack upload` (write), `hup` (a dedicated upload client, hackage.haskell.org/package/hup), Hackage server API at hackage-origin.haskell.org/api (open, 62,403-byte route listing), plain HTTPS tarball GET (read).
- composes with: Each upload must be a Cabal sdist tarball, the page requires the code and other material to be under an open source license, and a package version can be uploaded only once.
- reliability: Immutable by design - a bad upload cannot be deleted, which is irreversibility risk in the other direction. No documented byte ceiling means the ceiling is empirical and could change without notice. Read path is plain static files and reliable.
- notes: the same as the free tier
- evidence note: part of the free tier
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, 7,483,625 bytes
  - [3] 2026-10-21: probe: GET -> 200, 62,403 bytes (open route listing)
  - [1] 2026-10-21: 'Upload and publish a package permanently ... You can only upload a package version once and this cannot be undone'
  - [1] 2026-11-09: The upload page states that a package version cannot be uploaded twice. | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: You can only upload a package version once and this cannot be undone
  - [4] 2026-11-09: The accounts page ties an account to an email address and password. | capture: sha256:c5b5a1be518cffd75408f6a6997a60954be23becbe2ef31510435aa89de0ee87 | quote: You can modify various settings for your account, including changing the email address and password, setting email notification preferences, as well as creating authentication tokens, at the [account management page](https://hackage.haskell.org/users/account-management).
  - [1] 2026-11-25: the upload page reserves the right to remove packages | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: we retain the right to remove packages that are not under licenses that are open source in spirit, or that conflict with our ability to operate this service.
  - [1] 2026-11-25: a published package version cannot be uploaded again | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: You can only upload a package version once and this cannot be undone
  - [1] 2026-11-25: the open source license requirement | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: The code and other material you upload and distribute via this site must be under an
  - [1] 2026-11-25: the page frames uploads as a cost to the operators and states no size limit | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: has a cost of operation and maintenance associated to it
  - [1] 2026-11-25: the page states the once-only upload quoted in the field and no quota | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: You can only upload a package version once and this cannot be undone
- sources:
  - [1] https://hackage.haskell.org/upload
  - [2] https://hackage.haskell.org/package/pandoc-3.5/pandoc-3.5.tar.gz
  - [3] https://hackage-origin.haskell.org/api
  - [4] https://hackage.haskell.org/accounts

## hackage (haskell)

- `storage/hackage-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:03.171Z (live) | stale on 2026-12-04
- url https://hackage.haskell.org/upload
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
  - [1] 2026-11-19: the upload page documents permanent package publication with no stated size or quota number | capture: sha256:d664270ca30c27c50bdbcc1b80b302bac32b3bb4ecbc5e7abb900b76cc05717e | quote: Upload and publish a package permanently
  - [2] 2026-11-19: the upload handler source shows no size guard in the package-processing path | capture: sha256:7d57859162080413fc664fa87eb38f3b5bf53aa88f7deb9b848b8815b429f036 | quote: let processPackage :: LazyByteString -> IO (Either ErrorResponse (UploadResult, BlobStorage.BlobId))
- sources:
  - [1] https://hackage.haskell.org/upload
  - [2] https://raw.githubusercontent.com/haskell/hackage-server/master/src/Distribution/Server/Features/Upload.hs
