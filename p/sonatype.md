# sonatype

> sonatype.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sonatype/ | JSON https://fshy.ajam.dev/api/v1/entity/sonatype.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sonatype nexus repository cloud (hosted)

- `storage/sonatype-nexus-repository-cloud` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.sonatype.com/en/sonatype-cloud.html
- free tier: None reachable: Hosted Nexus is a paid, sales-led deployment: 'Contact the Sonatype sales team for the right deployment option'. No free hosted tier exists. Only the self-hosted Community Edition is free. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: Hosted Nexus is a paid, sales-led deployment: 'Contact the Sonatype sales team for the right deployment option'. No free hosted tier exists — only the self-hosted Community Edition is free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hosted Nexus is a paid, sales-led deployment: 'Contact the Sonatype sales team for the right deployment option'. No free hosted tier exists — only the self-hosted Community Edition is free.
- sources:
  - [1] https://help.sonatype.com/en/sonatype-cloud.html

## Maven Central (Sonatype Central Portal / Central Publisher)

- `storage/maven-central` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://central.sonatype.com
- free tier: No total storage quota, but as of 2026 a monthly publishing quota per organization on three metrics, with thresholds set at the ~90th percentile: 1,167 files / 78 MB release size / 7 releases per month at p90, rising to 17,724 / 1,808 MB / 50 at p99. The 1 GB archive upload limit is the per-request cap. Commercial-nature artefacts require the paid Publisher Pro tier from Oct 1 2026 regardless of volume. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GB per upload | bytes: 1000000000 | source: [1] | note: not stated
- retention: 30-day grace period on breach, then new releases refused | days: 30 | source: [1] | note: not stated
- egress: Free and unmetered, Cloudflare-fronted. Probe: repo1.maven.org jar GET -> 200, Server: cloudflare, CF-RAY present, no auth. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 1 GB per upload [1]
- limits note: 1 GB per upload archive. Monthly per-org: file count, total release size, release count (see table). 30-day grace period on breach, then new releases refused. Signed artefacts only; namespace ownership must be proven. Published artefacts remain downloadable forever ('Already-published artifacts are never affected').
- interface detail: rest
- tooling: Upload via Central Portal archive upload (zip/tar.gz up to 1 GB following Maven repo layout) or the maven-deploy-plugin; download via plain GET on repo1.maven.org/maven2/<group>/<artifact>/<version>/<file>. Every Java build tool is a client. No rclone backend.
- composes with: Weakest chain in the field because the new quota is per organization per month: 78 MB/month at the p90 threshold means a new org yields ~78 MB/month of headroom. Unlimited free orgs would multiply it, but each org requires a verified namespace and a GPG-signed artefact chain, so the setup cost per GB is the worst here.
- reliability: Data never vanishes (already-published artefacts are explicitly exempt from any enforcement). The failure mode is publishing stopping after the grace period. A bulk writer will hit the release-size threshold in the first month and be blocked. This quota regime is new (2026) and the page says thresholds 'may be adjusted as we learn'.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No total storage quota, but as of 2026 a monthly publishing quota per organization on three metrics, with thresholds set at the ~90th percentile: 1,167 files / 78 MB release size / 7 releases per month at p90, rising to 17,724 / 1,808 MB / 50 at p99. The 1 GB archive upload limit is the per-request cap. Commercial-nature artefacts require the paid Publisher Pro tier from Oct 1 2026 regardless of volume.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: monthly thresholds table ('90th | 1,167 | 78 | 7' ... '99th | 17,724 | 1,808 | 50'); 'These limits are evaluated as hard thresholds against an organization's usage during the current calendar month'; 'Commercial-nature artifacts require Maven Central Publisher Pro from October 1, 2026'
  - [2] 2026-10-21: 'You can upload an archive up to 1GB in size'
  - [3] 2026-10-21: probe: GET -> 200, Content-Length: 657952, Server: cloudflare
- sources:
  - [1] https://central.sonatype.org/publish/maven-central-publishing-limits/
  - [2] https://central.sonatype.org/publish/publish-portal-upload/
  - [3] https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar

## Sonatype Nexus Repository — Community Edition (self-hosted)

- `storage/sonatype-nexus-repository-community-edition` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.sonatype.com/products/sonatype-nexus-repository/download
- free tier: Free, self-hosted, no storage quota: 'There is no cost to use Sonatype Nexus Repository Community Edition'; the feature matrix marks 'Unlimited Nexus Repository Deployments' as included. Storage is your blob store, so the ceiling is your disk. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free by construction (self-hosted). Serve through Cloudflare or your own CDN at your own cost. | metered: no
- identity: anonymous
- interface: rest, webdav
- limits note: No published byte limit, but Sonatype positions CE as 'a small team solution ... with modest usage' and tells larger users to buy Pro. Pro-only features include cloud blob stores (S3/Azure/GCS), so CE is stuck on local disk. Raw repositories can hold arbitrary files but there is no public anonymous sharing story as clean as Cloudsmith's.
- interface detail: rest (Nexus REST API v1), native protocols for maven/npm/pypi/nuget/docker/raw/helm/apt/yum, WebDAV-ish raw repos
- tooling: `curl -u` against `/service/rest/v1/components`, `mvn deploy`, `npm publish`, `twine upload`, `docker push`; a well-documented REST API for scripting.
- composes with: Same as any self-hosted manager: unlimited instances × your disk. The version that matters for this brief is that nothing in Nexus meters bytes, so a single instance on a cheap VPS with a big volume gives unbounded logical storage. But you buy the volume.
- reliability: Mature and stable; the only 'limit' is a licensing/positioning nudge, not a technical cut-off. Data does not vanish.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: read live: 'There is no cost to use Sonatype Nexus Repository Community Edition. You can get started for free, no credit card is required'; 'designed to be a small team solution that can be used for free with modest usage'
  - [2] 2026-10-21: read live: 'Unlimited Nexus Repository Deployments' ticked for Community Edition; 'Cloud Blob Storage (AWS S3, Azure, GCS)' is Pro-only
  - [3] 2026-10-21: read live: 'Nexus Repository Community Edition: Free, self-hosted artifact management'
- sources:
  - [1] https://www.sonatype.com/products/sonatype-nexus-oss-download
  - [2] https://help.sonatype.com/en/nexus-repository-feature-matrix.html
  - [3] https://help.sonatype.com/en/nexus-repository-tiers-and-feature-availability.html
