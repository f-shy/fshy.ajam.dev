# Tebi

> tebi.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tebi/ | JSON https://fshy.ajam.dev/api/v1/entity/tebi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tebi

- `storage/tebi` | dead | evidence measured | binding none | category S3-compatible object storage, geo-distributed
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:57:50.876Z (live) | stale on 2026-12-20
- url https://tebi.io/pricing
- free tier: dead: the service shut down on March 31, 2026. Former offer, from third-party listings: Free 25 GB storage and 250GB outbound transfer | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1] | note: the former figures come from a third-party list entry removed in January 2026 with the message 'Tebi.io will be shut down'; no first-party pricing page answers.
- per-object cap: unknown: the service is shut down and no first-party limits page answers | source: [2] | note: tebi.io has no A record and www.tebi.io answers NXDOMAIN.
- retention: the service ended on March 31, 2026; the shutdown notice asked users to transfer their data to another provider to avoid data loss | source: [3] | note: the notice text is known from copies posted by its recipients.
- egress: none: the S3 endpoint s3.tebi.io answers NXDOMAIN. Former offer, from third-party listings: 250GB outbound transfer free a month | metered: yes | source: [1]
- identity: card | detail: unverified: the service is gone. A third-party guide from 2023 says the free tier plus pay-as-you-go plan needed a credit card, and an account without one got a 14-day trial.
- interface: s3-compatible
- limits note: no limit applies to a shut-down service
- binding note: the service is gone, so no limit binds
- interface detail: S3-compatible object storage, per the third-party listing; the endpoint hostname s3.tebi.io no longer resolves
- tooling: none works: the S3 endpoint does not resolve
- composes with: none: the service is shut down; it was an S3 origin with a free 25 GB tier.
- reliability: shut down on March 31, 2026: s3.tebi.io and www.tebi.io answer NXDOMAIN and the apex has no A record
- notes: S3-compatible object storage: rejected, the service shut down on 2026-03-31. The tebi.io zone is still delegated (SOA at Hetzner DNS) but holds no host records for the site or the endpoint.
- evidence note: the death is measured by DNS queries on 2026-10-30 (NXDOMAIN for s3.tebi.io and www.tebi.io, no A record for tebi.io) and dated by copies of the vendor's shutdown notice posted by recipients; no first-party page answers.
- evidence:
  - probe:https://8.8.8.8/resolve?name=s3.tebi.io&type=A 2026-10-30: the S3 endpoint s3.tebi.io does not exist in DNS: Status 3 (NXDOMAIN), SOA from the tebi.io zone | capture: sha256:115e9712d25d9a1043ba77a371c14997a783ebe6c0107e9258be8047f8361d0e | quote: "Status":3
  - probe:https://8.8.8.8/resolve?name=www.tebi.io&type=A 2026-10-30: www.tebi.io does not exist in DNS: Status 3 (NXDOMAIN) | capture: sha256:302cee3da84f2331909a3f786a3ab13af92f5f76dde1b3140674c9f2b6df7eb7 | quote: "Status":3
  - probe:https://8.8.8.8/resolve?name=tebi.io&type=A 2026-10-30: the tebi.io apex answers with no A record: an Authority SOA only, no Answer section | capture: sha256:9c86a8cca793a69af189fbf3556a214e9ab93f91fcee5f11254038a0e84064ff | quote: "Question":[{"name":"tebi.io.","type":1}],"Authority"
  - [3] 2026-10-30: a recipient's copy of the vendor's notice dates the shutdown to March 31, 2026 | capture: sha256:6475db1e4909db7530f080dedd055739aeb27666b63cea00a3b7b97a151b4140 | quote: Unfortunately, we are forced to shut down the Tebi.io project on March 31, 2026
  - [3] 2026-10-30: the notice asked users to move their data before the shutdown | capture: sha256:6475db1e4909db7530f080dedd055739aeb27666b63cea00a3b7b97a151b4140 | quote: We ask that you transfer your data to another provider as soon as possible to avoid data loss.
  - [4] 2026-10-30: a second recipient quotes the notice subject naming the March 31 shutdown | capture: sha256:2eb709ebc3c11357fd040dc7cbf6aa7cc78e6c24a4783a9eb4ebd6a132ee3977 | quote: Tebi: project shut down on March 31
  - [1] 2026-10-30: the free-for-dev list removed Tebi because it would be shut down | capture: sha256:c0ac6c0985cde9a2f08de19b44d46c0d24c723c7ec90328a5ff60ac01da7f2ce | quote: Tebi.io will be shut down
  - [1] 2026-10-30: the former free tier was 25 GB of S3-compatible storage and 250 GB of outbound transfer | capture: sha256:c0ac6c0985cde9a2f08de19b44d46c0d24c723c7ec90328a5ff60ac01da7f2ce | quote: S3 compatibility object storage.Free 25 GB storage and 250GB outbound transfer.
  - [5] 2026-10-30: a 2023 third-party guide says the free tier plan needed a credit card | capture: sha256:f4e66b5fc214a66008b993652a47504bf9e7ad9f377884a13ad429b3f56d442a | quote: Only thing you will need to do is to enter your credit card to get this free tier + Pay As You Go plan.
  - probe:https://8.8.8.8/resolve?name=s3.tebi.io&type=A 2026-11-04: s3.tebi.io still answers NXDOMAIN | capture: sha256:115e9712d25d9a1043ba77a371c14997a783ebe6c0107e9258be8047f8361d0e | quote: "Status":3
- sources:
  - [1] https://github.com/ripienaar/free-for-dev/commit/f92f384412c8fc405963f7c4c033710ed7fcf97b
  - [2] https://tebi.io/pricing
  - [3] https://www.dalao.net/thread-54009.htm
  - [4] https://judis.id/cloud/tebi-io-shutdown-2026-migrasi-cloud-storage/
  - [5] https://www.51sec.org/2023/04/27/integrate-sharex-with-free-forever-s3-compatble-storage-solution-tebi-io-25g-storage-250gb-outbound-traffic/
