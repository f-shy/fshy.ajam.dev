# NeuroVault

> neurovault.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neurovault/ | JSON https://fshy.ajam.dev/api/v1/entity/neurovault.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeuroVault

- `storage/neurovault` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://neurovault.org
- free tier: Free, no published per-file or per-account cap found on the site or FAQ (silence, not a stated infinity). 715,868 images currently indexed. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Per-object-cap: unstated; scope is restrictive. Statistical maps/parcellations/atlases only. Retention: permanent URLs. | source: [1] | note: not stated
- egress: Free and anonymous. `neurovault.org/media/images/...` serves with `Accept-Ranges: bytes`, `Access-Control-Allow-Origin: *`, no auth. | metered: no
- identity: institution
- interface: rest
- limits note: Per-object-cap: unstated; scope is restrictive. Statistical maps/parcellations/atlases only. Retention: permanent URLs. Read limit: none observed, no CDN in front (bare origin), so throughput is modest.
- interface detail: rest
- tooling: Documented REST API (`/api/images/?format=json`, `/api/collections/`), plus the `pynv`/`nilearn` fetch-atlas path. Upload needs an account but is API-driven.
- composes with: Unlimited collections per account; each image is an independent anonymous object. The API exposes every image's `file` URL and `file_size`, so a caller can enumerate and pull the whole corpus without auth.
- reliability: Single origin behind Cloudflare, small operator; no observed rate limiting but no stated durability guarantee.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: purpose and permanence claims, no size cap offered
  - [2] 2026-10-21: probe: GET -> 200, count: 715868, includes file URL and file_size
  - [3] 2026-10-21: probe: GET -r 0-127 -> 206, Content-Range: bytes 0-127/587261, body starts 1f8b08 (real gzip)
- sources:
  - [1] https://neurovault.org/FAQ
  - [2] https://neurovault.org/api/images/?format=json&limit=1
  - [3] https://neurovault.org/media/images/806/GrandMean.nii.gz
