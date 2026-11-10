# OpenAerialMap

> hotosm.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hotosm/ | JSON https://fshy.ajam.dev/api/v1/entity/hotosm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenAerialMap (HOT / Open Imagery Network)

- `storage/openaerialmap` | qualifies-with-caveat | evidence reported | binding per-object-cap | category open drone/satellite imagery commons
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://imagery.hotosm.org/contribute
- free tier: Free hosting for anyone with nowhere to publish. The rewrite of the uploader is explicitly scoped to 'Handle files up to 100GB with resume capability, using S3 multipart upload with presigned URLs (direct browser-to-S3)'. No per-account total published; the catalog holds 21,460 datasets. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 GB/file | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. And note the two-tier model: providers who already have cloud storage can 'Register a catalog', in which case OAM stores only metadata and links out ('Indexing uses none of your bandwidth and gives OAM no rights over the imagery'). | metered: no
- identity: email | detail: Email. Sign in with a Google account (documented third-party walkthrough: 'Sign in using your google account'), no affiliation or review.
- interface: cli
- limits:
  - per-object-cap (binding): 100 GB/file [1]
- limits note: geospatial raster only (GeoTIFF/COG orthomosaics); target 100 GB/file with resumable S3 multipart; account needed for API access and upload
- interface detail: uploader web app at upload.imagery.hotosm.org; STAC API at api.imagery.hotosm.org/stac; eoAPI (raster/vector/stac) behind it
- tooling: stactools-hotosm; STAC client; no CLI uploader yet
- composes with: Output is a COG + STAC item, i.e. cloud-native GeoTIFF. Directly readable with GDAL/rio-tiler and range-friendly. But the payload must be an orthomosaic with georeferencing.
- reliability: The uploader has undergone rewrites for large file support. No public API upload endpoints were responsive during testing on 2026-10-21.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'If you cannot host imagery yourself, upload it'; the catalog-registration path stores metadata only
  - [1] 2026-10-21: 'Handle files up to 100GB with resume capability, using S3 multipart upload with presigned URLs'; new API api.imagery.hotosm.org
  - [3] 2026-10-21: 200, {"meta":{..."found":21460},"results":[{..."uuid":"https://oin-hotosm-temp.s3.amazonaws.com/...tif"}]}
  - [4] 2026-10-21: live STAC collections (cop-dem-glo-30, ...)
  - withheld 2026-10-21: api.openaerialmap.org/{upload,uploads,api/upload,upload/} — 404 on all four (no documented REST upload endpoint reached)
- sources:
  - [1] https://github.com/hotosm/openaerialmap/discussions/258
  - [2] https://imagery.hotosm.org/contribute
  - [3] https://api.openaerialmap.org/meta?limit=1
  - [4] https://api.imagery.hotosm.org/stac/collections
