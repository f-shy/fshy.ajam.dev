# ttl.sh

> ttl.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ttl/ | JSON https://fshy.ajam.dev/api/v1/entity/ttl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ttl.sh (anonymous ephemeral OCI registry)

- `storage/ttl-sh` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:24.771Z (live) | stale on 2026-12-10
- url https://ttl.sh
- free tier: Free forever. Zero sign-up. | unit: unlimited | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: unverified: https://ttl.sh/ states no per-object size cap | source: [1] | note: unverified: https://github.com/replicatedhq/ttl.sh/blob/main/registry/entrypoint.sh answered HTTP 404 on 2026-11-25; no per-object size cap is stated on https://ttl.sh/ or the deployment README
- retention: Choose your TTL. Default is 1 hour, max is 24 hours. | source: [1] | note: Default is 1 hour, max is 24 hours; no TTL specified defaults to `:1h`.
- egress: Unmetered and anonymous: blobs are 307-redirected to a presigned S3 URL (s3.us-east-1.storage.sh, X-Amz-Expires=1200), so bytes come off object storage, not the registry host. Range requests work. | metered: no
- identity: anonymous | detail: Free forever. Zero sign-up.
- interface: s3-compatible, oci
- limits:
  - per-ip-shaping (binding): 11 MB/s [1]
- limits note: TTL max 24h advertised (:5m/:1h/:6h/:24h), default 1h. Upload is slow (~11 MB/s observed: 1.5GB in 2m11s), so throughput is the practical per-connection cap. _catalog is blocked by nginx (401), tags/list is open.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: oci
- tooling: Any distribution-spec client: oras, docker, skopeo, crane, regctl. Built on zot (per the repo: 'Zot runs an off-the-shelf image ghcr.io/project-zot/zot-linux-amd64 ... points zot at an S3-compatible bucket').
- composes with: Any OCI artifact can be pushed with a TTL without auth, config or an account.
- reliability: Expiry is best-effort: the deployment repo states 'Tag expiry is handled separately and is not yet wired up in this repo', and open issue #151 reports images not expiring. Data WILL vanish at TTL; do not treat as durable. Intermittent connect timeouts observed from this network.
- notes: No account, no quota. "Free forever. Zero sign-up. Push any OCI artifact with a TTL." Storage is bounded only by the TTL, max advertised 24 hours.
- evidence note: the ttl.sh page states the service is free forever with zero sign-up
- evidence:
  - [1] 2026-10-21: read live: 'Free forever. Zero sign-up. Push any OCI artifact with a TTL. No auth, no config, no account.'; 'Choose your TTL. Default is 1 hour, max is 24 hours.'
  - [2] 2026-10-21: probe: POST -> 202 Accepted with Location header, no credentials of any kind
  - withheld 2026-10-21: probe: PATCH .../blobs/uploads/<uuid> with 256MiB random -> 202, Range: 0-1048575; then PUT ?digest=sha256:... -> 201 Created; PUT /v2/probe4941/manifests/24h -> 201; GET /v2/probe4941/manifests/24h -> 200 returning the exact manifest
  - withheld 2026-10-21: probe: 1.5GB anonymous upload -> HTTP/1.1 202 Accepted, Range: 0-1499999999, then commit PUT -> 201 Created, digest sha256:1c5954e1c91f... (no 413, no chunking needed)
  - [3] 2026-10-21: probe: GET blob -> 307 to (presigned, CF/S3-edge served); ranged GET -r 0-1048575 -> 206, 1048576 bytes
  - [4] 2026-10-21: read live: 'Tag expiry is handled separately and is not yet wired up in this repo'; zot-config.json.j2 confirms S3 driver, dedupe:false, retention delay 1h with deleteUntagged
  - [1] 2026-11-09: the page states the service is free with no sign-up | capture: sha256:5c788d1bab655380f8460ae3ef6d2ae0e58dbb5f2905341276dba6c8bb030d8d | quote: Free forever. Zero sign-up.
  - [1] 2026-11-09: the page states the default 1 hour TTL and 24 hour maximum | capture: sha256:5c788d1bab655380f8460ae3ef6d2ae0e58dbb5f2905341276dba6c8bb030d8d | quote: Choose your TTL. Default is 1 hour, max is 24 hours.
  - probe:https://github.com/replicatedhq/ttl.sh/blob/main/registry/entrypoint.sh 2026-11-25: the stale repository path for the nginx upload setting answered HTTP 404 | capture: sha256:93af748c9ce87b12309adf3fa330a6f62a79e8066a6d0e206cf96de1cd5c6be5 | quote: "status": 404
  - [1] 2026-11-25: the default TTL is 1 hour, the maximum is 24 hours and an unspecified TTL becomes :1h | capture: sha256:5c788d1bab655380f8460ae3ef6d2ae0e58dbb5f2905341276dba6c8bb030d8d | quote: Choose your TTL. Default is 1 hour, max is 24 hours. ... No TTL specified? Defaults to `:1h`
  - [1] 2026-11-25: OCI artifacts can be pushed anonymously without config or an account | capture: sha256:5c788d1bab655380f8460ae3ef6d2ae0e58dbb5f2905341276dba6c8bb030d8d | quote: Push any OCI artifact with a TTL. No auth, no config, no account.
- sources:
  - [1] https://ttl.sh/
  - [2] https://ttl.sh/v2/probe<rand>/blobs/uploads/
  - [3] https://s3.us-east-1.storage.sh/ttlsh-registry-data/...?X-Amz-Expires=1200
  - [4] https://github.com/replicatedhq/ttl.sh
