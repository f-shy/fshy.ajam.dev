# openSUSE Build Service

> opensuse.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opensuse/ | JSON https://fshy.ajam.dev/api/v1/entity/opensuse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## openSUSE Build Service (OBS) - build.opensuse.org, public instance

- `storage/opensuse-build-service-build-opensuse-org-public-instanc` | qualifies | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://build.opensuse.org
- free tier: No published storage quota. The user guide states the instance 'can be used by anybody to freely create binaries for any of the supported distributions' and that 'You can store your sources there, build your packages and got them mirrored around the world.' The only quantitative ceilings found are per-file/per-build, not per-project: build disk constraint is expressed as `Constraint: hardware:disk:size unit=G <N>` and users are seen requesting 110 GB for one build (openSUSE forum, 2026-06-16). Observed real object size in the archive: `openSUSE:Factory/kernel-source/linux-7.2.tar.xz` is 160,068,116 bytes, served publicly. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: none documented for source blobs - 160 MB | bytes: 160000000 | source: [1] | note: not stated
- retention: unpublished home projects are subject to admin cleanup, and binaries are pruned per repository/architecture | source: [1] | note: not stated
- egress: Free and mirrored: 'build your packages and got them mirrored around the world' - download.opensuse.org is a public mirror ring. No per-GB accounting, no billing relationship at all for the public instance. | metered: no
- identity: institution
- interface: rest, cli
- limits:
  - per-object-cap (binding): per-object-cap: none documented for source blobs - 160 MB [1]
- limits note: per-object-cap: none documented for source blobs - 160 MB verified; unpublished home projects are subject to admin cleanup, and binaries are pruned per repository/architecture. IMPORTANT: Range requests are NOT honoured on the source endpoint (a bounded 1 MB range GET returned 200 with the full 160,068,116 bytes), so ranged/parallel fetch must be done against download.opensuse.org (mirror ring), not api.opensuse.org.
- interface detail: rest
- tooling: `osc` (CLI, in every openSUSE repo), OBS REST API (`api.opensuse.org/public/...` for anonymous reads, XML), and plain HTTPS download of published repositories from download.opensuse.org. `osc add $URL` stores a remote-source reference; `osc commit` uploads real blobs.
- composes with: unlimited home projects (`home:<user>:<sub>`) x unlimited packages per project x unlimited versions; published repos additionally replicate to every download.opensuse.org mirror at no cost. Sources are retained per package revision (the API exposes rev/vrev, e.g. osc 'rev=517 vrev=485'), so a single package with N commits holds N copies of the blob server-side. Multiply by unlimited free openSUSE accounts. This is the packaging-native equivalent of GitHub Releases, with a global mirror CDN attached.
- reliability: API source endpoint silently ignores Range and streams the whole object - will blow up any client that assumes 206. Home projects are explicitly deprioritised: 'home repos are by default low hanging fruit, other projects take priority'. Recorded here only to note the 160 MB verified object and the no-Range behaviour.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: probe: GET -> 200 XML listing, entry linux-7.2.tar.xz size=160068116
  - [3] 2026-10-21: probe: GET -> 200, content-length 160068116, application/octet-stream (real bytes, anonymous, no auth)
  - withheld 2026-10-21: probe: ranged GET bytes 0-1048575 on same URL -> 200 with 160068116 bytes (Range ignored)
  - [1] 2026-10-21: 'You can store your sources there, build your packages and got them mirrored around the world.'
  - [4] 2026-10-21: 2026-06 user sets `Constraint: hardware:disk:size unit=G 110` for a single build
  - [5] 2026-10-21: 'You may not share API tokens to exceed OBS's rate limitations.'
- sources:
  - [1] https://openbuildservice.org/help/manuals/obs-user-guide/cha-obs-best-practices-upstream
  - [2] https://api.opensuse.org/public/source/openSUSE:Factory/kernel-source
  - [3] https://api.opensuse.org/public/source/openSUSE:Factory/kernel-source/linux-7.2.tar.xz
  - [4] https://forums.opensuse.org/t/disk-space-constraint/194432
  - [5] https://en.opensuse.org/openSUSE:Build_Service_Terms_of_Service
