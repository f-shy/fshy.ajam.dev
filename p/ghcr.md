# GitHub Container Registry

> ghcr.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ghcr/ | JSON https://fshy.ajam.dev/api/v1/entity/ghcr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GitHub Container Registry (GHCR) via ORAS

- `storage/github-container-registry-via-oras-known-numbers-re-veri` | qualifies | evidence documented | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://ghcr.io
- free tier: Container image storage and bandwidth are free: "Container image storage and bandwidth for the Container registry is currently free. If you use Container registry, you'll be informed at least one month in advance of any change to this policy." Ceiling is per-blob, not per-account: "The Container registry has a 10 GB size limit for each layer" and "a 10 minute timeout limit for uploads". | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free/unmetered per the billing page note above; blobs 307-redirect to pkg-containers.githubusercontent.com (Azure Blob, Fastly fronted). | metered: no
- identity: anonymous
- interface: oci
- limits note: 10 GB per layer (per file), 10 minute upload timeout per blob, anonymous PUSH denied, anonymous PULL allowed for public packages. npm/nuget/maven/ruby registries on the same product are NOT free like this. See dead ends.
- interface detail: oci
- tooling: Oras-project/oras (2,474 stars). `oras push` with `--artifact-type`, one file per layer, so the 10 GB/layer cap becomes the per-file cap. Docker/skopeo/crane also work. Androsh7/layerstash (1 star) is a purpose-built 'Data Storage Tool for Docker Hub and GHCR'.
- composes with: unlimited repos x unlimited tags/versions x (10 GB per blob). A 30 TiB corpus = 3,000 x 10 GB ORAS layers, spread over any number of repos/tags; multiply by unlimited accounts and orgs. Effectively unbounded, capped only by upload throughput.
- reliability: Anonymous pull verified end-to-end; nothing expires. The 10-minute upload timeout is the real constraint on large single layers from a slow link. Use several smaller layers.
- notes: the same as the free tier
- evidence note: re-read on 2026-10-22 (HTTP 200, 17000 bytes, sha256 4b3a2c0a26a56c2a). The page states the number in the record. The claim is documented, not measured.
- extras:
  - verified[0].url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 17000
  - verified[0].sha256: 4b3a2c0a26a56c2a4cfd47016d4f6a9c5f388b00b9a4eb57386569eab7a9495b
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [1] 2026-10-22: 10 GB per layer on GHCR. Re-read https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry: HTTP 200, 17000 bytes, sha256 4b3a2c0a26a56c2a.
  - [2] 2026-10-21: 'Container image storage and bandwidth for the Container registry is currently free'
  - [3] 2026-10-21: probe: GET ghcr.io/v2/ -> 401 with www-authenticate: Bearer realm="",service="ghcr.io" (auth flow entry point)
  - withheld 2026-10-21: probe: GET ghcr.io/token?scope=repository:actions/actions-runner:pull (anonymous) -> token len 60; GET /v2/actions/actions-runner/manifests/latest -> 200 index; child manifest -> 200, 10 layers, 543.1 MB total
  - withheld 2026-10-21: probe: GET /v2/actions/actions-runner/blobs/<digest> -r 0-65535 -> 307 to pkg-containers.githubusercontent.com ... -> 206, Content-Range: bytes 0-65535/29765758
  - withheld 2026-10-21: probe: GET ghcr.io/token?scope=repository:test/x:pull,push (anonymous) -> {"errors":[{"code":"DENIED"}]}; POST token with user:PAT basic auth -> 200 {"token":...} (real login flow)
- sources:
  - [1] https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
  - [2] https://docs.github.com/en/billing/concepts/product-billing/github-packages
  - [3] https://ghcr.io/token
