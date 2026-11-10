# Open Storage Network

> openstoragenetwork.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openstoragenetwork/ | JSON https://fshy.ajam.dev/api/v1/entity/openstoragenetwork.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open Storage Network (OSN) via NSF ACCESS — 1 to 50 TB of S3 per allocation, 10 TB minimum

- `storage/open-storage-network-via-nsf-access-1-to-50-tb-of-s3-per` | qualifies | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.openstoragenetwork.org/get-involved/get-an-allocation/
- free tier: 'Allocations of a minimum 10 terabytes and max of 50 terabytes supporting up to 1.6 million files can be requested through the ACCESS CI allocation process.' The ACCESS documentation states it as a 10-50 TB project allocation with '1 ACCESS credit = 1 GB' and 'Campus Champions may request 1 TB for testing'. Above 50 TB: 'contact us to discuss the hosting and purchase of your own OSN pod'. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Retention: 'Never purged', 'Not backed up' (support.access-ci.org resource table). Genuinely indefinite, which is unusual in this niche. | source: [1] | note: not stated
- egress: Free and unmetered. This is NSF-funded infrastructure, there is no egress meter anywhere in the docs. Public buckets are readable anonymously, which is the fetch path. | metered: no
- identity: institution
- interface: s3, rclone, cli
- limits:
  - write-gated (binding): review (an Explore project is a 1-page proposal, reviewed, and the PI needs an institu [1]
- limits note: Per-object-cap: not documented; the counted limit is 'up to 1.6 million files' per allocation. Retention: 'Never purged', 'Not backed up' (support.access-ci.org resource table). Genuinely indefinite, which is unusual in this niche. request-rate: not published, but the docs note parallel requests against the inside endpoints spread across OSDs 'and therefore achieve very large training throughput'. Gate: ACCESS allocation review an Explore project is a 1-page proposal, reviewed, and the PI needs an institutional email.
- interface detail: s3
- tooling: rclone with provider = Ceph, aws cli, Cyberduck, restic. Endpoints are per-pod, e.g. https://mghp.osn.xsede.org. Bucket management is via the Coldfront portal (coldfront.osn.mghpcc.org), not the CLI.
- composes with: The multiplier is ACCESS projects, not buckets: 'one project can have many S3 Buckets as long as the total quota doesn't exceed the project network quota'. So 50 TB per ACCESS project. ACCESS allows 'Multiple requests allowed' for Explore, Discover and Accelerate project types, with credit limits of 400,000 / 1,500,000 / 3,000,000 respectively. At 3,000 credits per TB of OSN, a single Explore project (400k credits) can fund ~133 TB if it were all spent on OSN, well above the 50 TB per-project cap, meaning the per-project cap is the binding limit and multiple projects is the way past it.
- reliability: Buckets are 'not backed up' and are created by ticket/portal form, not API. Automation is limited to reads and writes, not bucket provisioning.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Allocations of a minimum 10 terabytes and max of 50 terabytes supporting up to 1.6 million files can be requested through the ACCESS CI allocation process'
  - [1] 2026-10-21: 'Project allocations run from 10 TB to 50 TB through the standard ACCESS process', '1 ACCESS credit = 1 GB', Bucket storage | 50 TB | Never purged | Not backed up
  - [3] 2026-10-21: '3,000 ACCESS credits per 1 TB of OSN storage', total OSN allocation 1-50 TB, and OSN is 'at no cost to researchers'
  - [4] 2026-10-21: public anonymous access is opt-in at bucket request: 'If your bucket should be accessible without authentication, please make a note'
  - [5] 2026-10-21: probe: curl -D - -> HTTP/1.1 200 OK, x-amz-request-id tx000006fe9903f5e55ebe4-...-default, Ceph RGW ListAllMyBucketsResult
  - [6] 2026-10-21: probe: curl '' -> HTTP 200, 1,100 bytes of valid ListBucketResult JSON-equivalent XML, IsTruncated true, real keys (bioconductor AnnotationHub mirror). Anonymous bucket listing works on a real public OSN bucket.
  - withheld 2026-10-21: probe: curl -r 0-99 <690MB object> -> HTTP/1.1 206 Partial Content, Content-Range: bytes 0-99/81066 on the small object and 206 on the large one, Accept-Ranges: bytes, ETag present. Ranged reads work.
  - withheld 2026-10-21: benchmark: single stream 64 MiB ranged GET -> 67,108,864 B in 5.35 s = 12.55 MB/s (97% of this host's 16.67 MB/s Cloudflare baseline). 16 parallel 4 MiB ranged GETs -> 10.16 MiB/s aggregate, 32 parallel -> 6.71 MiB/s. The curve DECREASES: OSN's per-connection throughput is good and the local link is the bottleneck, so parallel ranged GETs buy nothing here — do not condemn OSN with a single-stream test, it is already at line rate.
- sources:
  - [1] https://support.access-ci.org/documentation/resources/osn
  - [2] https://www.openstoragenetwork.org/get-involved/get-an-allocation/
  - [3] https://openstoragenetwork.github.io/docs/allocations/
  - [4] https://openstoragenetwork.github.io/docs/request-bucket/
  - [5] https://mghp.osn.xsede.org/
  - [6] https://mghp.osn.xsede.org/bir190004-bucket01/?list-type=2&max-keys=3
