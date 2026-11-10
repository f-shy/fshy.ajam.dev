# Snap Store

> snapcraft.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/snapcraft/ | JSON https://fshy.ajam.dev/api/v1/entity/snapcraft.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Snap Store (api.snapcraft.io / snapcraft.io)

- `storage/snap-store` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://snapcraft.io/store
- free tier: No published total-storage quota and no published per-snap byte cap; the practical ceiling is what the upload tooling survives. Evidence of real large artefacts: `kicad` stable snap is 1,659.5 MB and `android-studio` is 1,657.8 MB in the channel map (both served fine). A 5.5 GB upload attempt returned HTTP 500 and was diagnosed by Canonical as 'a timeout in the object storage load balancers'. 1.7 GB is documented as working; ~5 GB class uploads fail with a server-side timeout. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: not documented, empirically ~1.7 GB | bytes: 1700000000 | source: [1] | note: not stated
- retention: per-object-cap: not documented, empirically ~1.7 GB works and 5.5 GB 500s (object-storage load-balancer timeout). retention: indefinite, full revision history retained (each revision is a separate stored .snap) | source: [1] | note: not stated
- egress: Free and CDN-backed. Downloads go through api.snapcraft.io -> redirect -> a CDN; no billing, no per-download accounting. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - write-gated: application/octet-stream` verified) [1]
  - per-object-cap (binding): per-object-cap: not documented, empirically ~1.7 GB [1]
- limits note: per-object-cap: not documented, empirically ~1.7 GB works and 5.5 GB 500s (object-storage load-balancer timeout). retention: indefinite, full revision history retained (each revision is a separate stored .snap). request-rate: not documented. A 'FATAL ERROR: Data queue size is too large' error hits multi-GB uploads client-side too.
- interface detail: rest
- tooling: `snapcraft upload` / `snapcraft push` (the write path), Snap Store API v2 (`api.snapcraft.io/v2/snaps/info/<name>` with header `Snap-Device-Series: 16`) for metadata, and plain HTTPS GET of the channel-map `download.url` for bytes. No rclone backend; a wrapper would have to speak the snapcraft upload protocol to push.
- composes with: unlimited snaps per publisher account x unlimited revisions per snap (revision history is retained server-side - the forum thread discusses 3 GB across 3 revisions of a 1 GB game). Multiply by unlimited free Ubuntu One accounts. Realistically ~1.6 GB x N revisions x N snaps, but upload reliability degrades well before 5 GB.
- reliability: The write path is the weak link, not storage: multi-GB uploads fail with opaque HTTP 500 ('timeout in the object storage load balancers') and with client-side 'Data queue size is too large'. Bytes are served perfectly once published (`200 77574144 application/octet-stream` verified). Snaps are squashfs images - arbitrary content must be packaged into a snap with a valid snapcraft.yaml, so this is a wrapper-only route.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 5.5 GB upload 500s; Canonical: 'it seems to be related to a timeout in the object storage load balancers'
  - [2] 2026-10-21: 'I'm trying to upload a new version of Kicad, which is 1,7GBytes ... FATAL ERROR: Data queue size is too large'
  - [3] 2026-10-21: probe: GET (Snap-Device-Series: 16) -> channel-map download.size 1,659,5xx,xxx bytes (1.66 GB stored and served)
  - withheld 2026-10-21: probe: GET .../snaps/download/amcUKQILKXHHTlmSa7NMdnXSx02dNeeT_2955.snap with -L -> 200, 77,574,144 bytes, application/octet-stream (core22, real squashfs bytes)
- sources:
  - [1] https://forum.snapcraft.io/t/snap-package-file-size-limit-on-the-store/37450
  - [2] https://forum.snapcraft.io/t/fatal-error-data-queue-size-is-too-large/43875
  - [3] https://api.snapcraft.io/v2/snaps/info/kicad
