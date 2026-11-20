# CSC Allas

> csc.fi | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/csc/ | JSON https://fshy.ajam.dev/api/v1/entity/csc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CSC Allas (Finland) — 10 TiB default per project, S3 + Swift on Ceph

- `storage/csc-allas-10-tib-default-per-project-s3-swift-on-ceph` | fails-identity | evidence documented | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://docs.csc.fi/data/Allas/introduction/
- free tier: 10 TiB per CSC project by default. The quota table lists 'Allas / Storage / 10 TiB' with the increase path 'Contact CSC Service Desk'. There is no per-file or per-object size cap documented; the counted limits are 1,000 buckets per project and 500,000 objects per bucket. Above 200 TiB for free-of-charge users, CSC asks you to 'agree with CSC about storage terms and possible costs'. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered. Objects are served from the a3s.fi S3 endpoint; public buckets are readable by anyone over HTTPS with no key and no egress meter. Quoted rule: 'Making a bucket public means that every file and directory on the bucket will be accessible without any kind of authentication from anywhere on the internet using the HTTPS protocol.' | metered: no
- identity: institution
- interface: s3, rclone, cli
- limits note: Per-object-cap: none documented for size; 500,000 objects per bucket and 1,000 buckets per project are the real ceilings. request-rate: not published; the S3 front end is Ceph RGW behind a load balancer. Storage is billed in Storage BUs (1 TiB = 1.05 Storage BU/hour) but academic projects receive BUs free. The constraint is the 10 TiB allowance, not money. Retention: 'Allas can be used to host data for as long as the CSC project is active'; Academic projects 'are usually valid for one year at a time, but they can be extended'. Objects are immutable in place. You overwrite, you do not edit.
- binding note: 10 TiB per project is real and the door has a gatekeeper: CSC accounts come through Haka/Virtu or a Finnish organisation's contract. Identity binds before any limit does.
- interface detail: s3
- tooling: rclone (s3 backend, endpoint a3s.fi), s3cmd, aws cli, Swift/OpenStack CLI, a-commands suite (github.com/CSCfi/allas-cli-utils), Allas web UI at allas.csc.fi. The a-publish helper makes a bucket world-readable and prints the public URL.
- composes with: One project = 10 TiB. Self-service is the multiplier: a CSC account holder in the Haka/Virtu federation can create additional Academic projects in MyCSC without a human gate ('Academic project category ... can be created only by members of Finnish higher education institutions, state research institutes and CSC', and project creation is a MyCSC button, not a review). Each new project brings its own 10 TiB Allas bucket quota, its own 1,000 buckets and its own 500k-object/bucket ceiling. Ten projects = 100 TiB with no conversation with anyone.
- reliability: Storage-BU exhaustion closes the project; project lapse is what deletes data, not a retention timer.
- notes: 10 TiB per CSC project by default. The quota table lists 'Allas / Storage / 10 TiB' with the increase path 'Contact CSC Service Desk'. There is no per-file or per-object size cap documented; the counted limits are 1,000 buckets per project and 500,000 objects per bucket. Above 200 TiB for free-of-charge users, CSC asks you to 'agree with CSC about storage terms and possible costs'. VERDICT: fails-identity. Quota and gate in one sentence: 10 TiB per CSC project by default, reachable only through a Haka or Virtu login or a home organisation with a CSC contract, so the quota is real and unreachable.
- evidence note: re-read 2026-10-22 (HTTP 200, 5,580 bytes). Documented quota; the eligibility question is not answered by this page. The verdict is fails-identity on the registration gate; the quota is documented and the gate is documented.
- extras:
  - verified[0].url: https://docs.csc.fi/data/Allas/introduction/
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 11527
  - verified[0].sha256: f3af3ac5029670108cc3c319270360bfa09f7e2fd0b02d6dc2a1ea1693d09f10
  - verified[0].pattern_found: no
  - verified[0].what_changed: the expected sentence did not appear on re-read
  - verified[1].url: https://research.csc.fi/resources/quotas/
  - verified[1].date: 2026-10-22
  - verified[1].http_status: 200
  - verified[1].bytes: 5580
  - verified[1].pattern_found: yes
  - unconfirmed[0].url: https://docs.csc.fi/data/Allas/introduction/
  - unconfirmed[0].status: 200
  - unconfirmed[0].bytes: 11527
  - unconfirmed[0].why: the expected sentence did not appear on re-read
- evidence:
  - [1] 2026-10-22: Allas default quota is 10 TiB per project. The quota table's Allas row reads 'Storage | 10 TiB | Contact CSC Service Desk'. The page also states 'if you are using CSC's services free-of-charge and need to store more than 200 TiB in Allas, please contact Service Desk'. The record cited the introduction page, which carries the protocol and billing prose but not the quota table.
  - [1] 2026-10-21: 'Allas | Storage | 10 TiB', 'Buckets per project 1 000', 'Objects per bucket 500 000', 'if you are using CSC's services free-of-charge and need to store more than 200 TiB in Allas, please contact Service Desk'
  - [2] 2026-10-21: 'A CSC project is required to import data to Allas. Allas can be used to host data for as long as the CSC project is active.' S3 and Swift interfaces on Ceph.
  - [3] 2026-10-21: public bucket = anonymous HTTPS read of every object
  - [4] 2026-10-21: public URL form is https://a3s.fi/username-projectNumber-pub/object_name
  - [5] 2026-10-21: probe: curl -D - -> HTTP/1.1 200 OK, content-type application/xml, x-amz-request-id tx00000000000000fa81fe7-...-allas-prod-kaj, body <ListAllMyBucketsResult ... Owner anonymous, Buckets empty>. Live S3 endpoint, Ceph RGW, anonymous listing allowed and correctly returning zero buckets rather than an auth error.
  - [6] 2026-10-21: probe: curl -X PUT --data x -> 404; curl https://a3s.fi/probe-bucket-xyz/?list-type=2 -> 404 NoSuchBucket. Write path correctly closed to anonymous users (this is a working S3, not an open dump).
  - [2] 2026-10-22: 10 TiB per project. Re-read https://docs.csc.fi/data/Allas/introduction/: HTTP 200, 11527 bytes, sha256 f3af3ac502967010, but the expected phrase '10 TiB' did not appear, so the claim is not confirmed by this read.
- sources:
  - [1] https://research.csc.fi/resources/quotas/
  - [2] https://docs.csc.fi/data/Allas/introduction/
  - [3] https://docs.csc.fi/support/faq/how-to-make-a-bucket-public/
  - [4] https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/help/a-publish.md
  - [5] https://a3s.fi/
  - [6] https://a3s.fi/probe-bucket-xyz/probe.txt
