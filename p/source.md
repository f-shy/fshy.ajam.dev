# Source Cooperative

> source.coop | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/source/ | JSON https://fshy.ajam.dev/api/v1/entity/source.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Source Cooperative (source.coop / data.source.coop)

- `storage/source-cooperative-byte-level-re-probe` | qualifies-with-caveat | evidence reported | binding none | category dataset-hosting
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://source.coop
- free tier: No published byte quota. The platform documents hosting over 5 petabytes of data across 330+ products from 130+ organizations, serving approximately 700 TB per month for public data publishing. Documentation specifies no per-product, per-account, or per-file cap. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered in practice for the reader: anonymous GET with no credentials, Cloudflare in front, R2/Turbo-adjacent CDN headers. No egress meter appears anywhere in the docs. | metered: no
- identity: email | detail: email
- interface: s3, rclone, cli
- limits note: Write-gated. Publishing data requires application to the beta testing program via web form. Future flat pricing is announced for upcoming release. Data repositories are public by default with no private mode.
- interface detail: s3
- tooling: Genuine S3 proxy. Endpoint https://data.source.coop, --no-sign-request for reads. Upload credentials are Source-issued but in AWS format and valid only at the proxy; path is s3://<account-id>/<product-id>/ and you cannot write outside your own prefix. Accepts aws cli, boto3, rclone with a custom endpoint, plus a Source CLI and service accounts for CI.
- composes with: Multiplier is data products per account/org, and orgs can hold team members. Because reads are anonymous and S3-native, this is the cleanest 'someone else's S3 on a real CDN' shape in the whole D area. It can be mounted by AList/rclone and fronted by Cloudflare exactly per §2.1.
- reliability: Beta + announced-but-unpublished pricing means the free window has an unknown end date. Store only data that has a second home.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: PROBED (this is the new evidence): curl -qsS -D - -> HTTP 200, Content-Length: 16187, Accept-Ranges: bytes, ETag, Last-Modified, Server: cloudflare, CF-Cache-Status: DYNAMIC. Downloaded twice and SHA-256 compared: cdd18d37e1af2320c2eaa763a6b70a8258a1ee2e5dc78e558ea0922e981e56d6 on both copies, and 16,187 bytes on disk matches the declared Content-Length — a true roundtrip, not a 200-with-empty-body.
  - withheld 2026-10-21: PROBED: curl -H 'Range: bytes=0-99' on the same object -> HTTP 206 Partial Content, Content-Range: bytes 0-99/16187, 100 bytes body. Range requests work, so resumable/parallel fetches are viable.
  - [3] 2026-10-21: PROBED: curl '' -> real <ListBucketResult> with CommonPrefixes (fields-of-the-world-austria/, -belgium/, -brazil/, …), KeyCount 5, IsTruncated true. Anonymous bucket listing works — the catalogue is enumerable without credentials.
  - [4] 2026-10-21: PROBED: curl '' -> body is literally 'Source Cooperative Data Proxy v2.5.1', not an S3 error. Root listing is disabled but the service identifies itself; useful as a liveness probe.
  - [1] 2026-10-21: opened: 'Hosts over 5 petabytes … Serves approximately 700 terabytes of data transfer per month … Supports over 330 data products from 130+ organizations'; 'Source is currently in beta … publishing data requires applying to be a beta tester.'
  - [5] 2026-10-21: opened: 'Flat pricing … Pricing plans based on data volume and usage will be announced soon.' Confirms unpriced.
  - [6] 2026-10-21: opened: 'The Source Data Proxy provides S3-compatible access to all data hosted on Source Cooperative. You can access data through the proxy without authentication.'
- sources:
  - [1] https://docs.source.coop/what-is-source
  - [2] https://data.source.coop/kerner-lab/fields-of-the-world/README.md
  - [3] https://data.source.coop/kerner-lab?list-type=2&max-keys=5
  - [4] https://data.source.coop/?list-type=2&delimiter=/&max-keys=5
  - [5] https://source.coop/
  - [6] https://docs.source.coop/data-proxy

## Source Cooperative - uncapped public publishing, beta-gated

- `storage/source-cooperative-uncapped-public-publishing-beta-gated` | qualifies-with-caveat | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://source.coop/
- free tier: No published byte cap: 'allowing trusted organizations and individuals to publish data of any kind at any scale'. Case study: Earth Genome publishes 60+ TB. Platform total reported at just over 5 PB. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free public reads through the data proxy at data.source.coop - live probe returned HTTP 200 with Cloudflare in front (CF-RAY present), so reads are CDN-covered. | metered: no
- identity: email | detail: email
- interface: s3
- limits note: Beta: publishing requires acceptance as a beta tester via a Google Form, and BYOB requires Source staff to enable it per account ('contact hello@source.coop'). Public-only by design - 'all data hosted in Source is available to the public'. New products default to Unlisted.
- interface detail: s3
- tooling: Objects served at data.source.coop/<account>/<product>/...; the proxy is open source (Rust, github.com/source-cooperative/data.source.coop). Bring Your Own Bucket (BYOB) points Source at an S3 bucket you own, read via OIDC federation (sts:AssumeRoleWithWebIdentity) with no long-lived secret either side.
- composes with: Per data product, owned by 'an organization or an individual' explicitly. BYOB is the important primitive: it decouples the catalogue/CDN from the bytes, so a free bucket elsewhere becomes a Source product with Cloudflare-fronted reads.
- reliability: Nonprofit (Radiant Earth 501(c)(3) parent) with in-kind AWS/Azure; beta terms can change. Storage itself lives on commodity cloud, so durability is AWS-grade.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Source allows trusted organizations and individuals to publish data of any kind at any scale'; 'apply to be a beta tester'
  - [2] 2026-10-21: 'Data products can be owned by an organization or an individual'; 'By default it uses Source-managed storage... choose a connection in the us-west-2 region'
  - [3] 2026-10-21: 'Source staff must enable' BYOB; OIDC federation, 'Nothing long-lived is stored'
  - [4] 2026-10-21: live probe: HTTP 200, Server: cloudflare, CF-RAY a4e2ac1a8e2fa1b3-KTM
- sources:
  - [1] https://docs.source.coop/
  - [2] https://docs.source.coop/create-a-data-product
  - [3] https://docs.source.coop/bring-your-own-bucket
  - [4] https://data.source.coop/
