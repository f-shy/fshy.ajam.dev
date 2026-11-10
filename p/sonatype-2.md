# maven central

> sonatype.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sonatype-2/ | JSON https://fshy.ajam.dev/api/v1/entity/sonatype-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Maven Central (Sonatype Central Portal) - post-2026 publishing limits

- `storage/maven-central-post-2026-publishing-limits` | fails-quota | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://central.sonatype.org
- free tier: Maven Central introduced hard monthly publishing limits per organization in 2026. Three independent metrics: file count, release size, release count, evaluated as hard thresholds against the current calendar month, with a 30-day grace period on first breach (resets after 2 consecutive below-limit months). Thresholds are set near the top-10% of publishers; the published distribution table gives 90th percentile = 1,167 files / 78 MB release size / 7 releases per month, 99th = 17,724 / 1,808 MB / 50. Separately, from 2026-10-01, any artifact with a 'commercial nature' requires a paid Publisher Pro subscription regardless of volume. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Three independent metrics: file count, release size, release count, evaluated as hard thresholds against the current calendar month, with a 30-day grace period on first breach (resets after 2 consecutive below-limit months) | days: 30 | source: [1] | note: not stated
- egress: Free and effectively unmetered for consumers - repo1.maven.org is a heavyweight CDN. Publishing is what is metered, not download. | metered: no
- identity: email
- interface: rest, rclone
- limits note: per-object-cap: none stated for a single artifact, but release size is the metered metric. request-rate: publishing limits are monthly per-org (file count / release size / release count). retention: indefinite for already-published artifacts - 'Public artifacts already published to Maven Central remain available for download.' Enforcement blocks new releases, not existing storage. Commercial-nature artifacts require Publisher Pro from 2026-10-01.
- interface detail: rest
- tooling: `mvn deploy` / central-publishing-maven-plugin, `gradle` publishing, `curl` to the Central Portal API, and plain HTTPS Maven-layout GETs from repo1.maven.org. No rclone backend.
- composes with: Publishing limits apply per organization per month based on percentile thresholds (~78 MB at p90 and ~1.8 GB at p99), resetting on monthly cycles.
- reliability: The 2026 change is the important signal for the whole niche: the largest free package registry concluded that '10% of namespaces accounted for more than 88% of all files published' and moved to hard monthly thresholds plus a commercial-use gate. Any plan that treats a public registry as a bulk blob store is now rate-limited at ~GB/month/org, not capped at a total. The exact thresholds table and the commercial-nature gate are new.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Maven Central introduced hard monthly publishing limits per organization in 2026. Three independent metrics: file count, release size, release count, evaluated as hard thresholds against the current calendar month, with a 30-day grace period on first breach (resets after 2 consecutive below-limit months). Thresholds are set near the top-10% of publishers; the published distribution table gives 90th percentile = 1,167 files / 78 MB release size / 7 releases per month, 99th = 17,724 / 1,808 MB / 50. Separately, from 2026-10-01, any artifact with a 'commercial nature' requires a paid Publisher Pro subscription regardless of volume.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'These limits are evaluated as hard thresholds against an organization's usage during the current calendar month'; percentile table (p90: 1,167 files / 78 MB / 7 releases; p99: 17,724 / 1,808 MB / 50)
  - withheld 2026-10-21: same page - '30-day grace period rather than immediate enforcement'; 'Commercial-nature artifacts require Maven Central Publisher Pro from October 1, 2026'
  - withheld 2026-10-21: same page - 'Public artifacts already published to Maven Central remain available for download.'
  - [2] 2026-10-21: probe: GET -> 200, 60,219,212 bytes, application/java-archive
- sources:
  - [1] https://central.sonatype.org/publish/maven-central-publishing-limits/
  - [2] https://repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-compiler/1.9.0/kotlin-compiler-1.9.0.jar

## maven central as bulk storage

- `storage/maven-central-as-bulk-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://central.sonatype.org/publish/maven-central-publishing-limits/
- free tier: none reachable: Still no total-storage cap, but 2026 monthly per-organization publishing thresholds (~78 MB release size at p90, ~1.8 GB at p99) plus a commercial-nature gate from 2026-10-01 make sustained | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Still no total-storage cap, but 2026 monthly per-organization publishing thresholds (~78 MB release size at p90, ~1.8 GB at p99) plus a commercial-nature gate from 2026-10-01 make sustained
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Still no total-storage cap, but 2026 monthly per-organization publishing thresholds (~78 MB release size at p90, ~1.8 GB at p99) plus a commercial-nature gate from 2026-10-01 make sustained
- sources:
  - [1] https://central.sonatype.org/publish/maven-central-publishing-limits/
