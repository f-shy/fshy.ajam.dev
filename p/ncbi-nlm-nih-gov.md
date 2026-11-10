# NCBI GEO

> ncbi.nlm.nih.gov | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ncbi-nlm-nih-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/ncbi-nlm-nih-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NCBI SRA — with anonymous read via AWS Open Data

- `storage/ncbi-sra-with-anonymous-read-via-aws-open-data` | qualifies | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ncbi.nlm.nih.gov/sra
- free tier: No per-account quota published. Submission is genuinely bulk: FTP, Aspera (`ascp -QT -l 100m -k1 -d`), or Aspermera; operator guidance for 'tens or more terabytes' is to contact SRA support directly. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: per-object-cap: none on deposit; individual runs of hundreds of GB are normal. Retention: permanent, no expiry | source: [1] | note: not stated
- egress: Free. Read side is mirrored to AWS Open Data (`sra-pub-run-odp.s3.amazonaws.com`) with anonymous, ranged, CORS-open access. No requester-pays, no auth. | metered: no
- identity: anonymous
- interface: s3, sftp
- limits note: Per-object-cap: none on deposit; individual runs of hundreds of GB are normal. Retention: permanent, no expiry. Binding limit on read is per-ip-shaping from S3. Not a storage cap.
- interface detail: sftp
- tooling: Aspera Connect / ascp, sra-tools (prefetch/fasterq-dump), and the AWS Open Data mirror which behaves like any public S3 bucket.
- composes with: Deposit is per-submission and effectively unbounded; the AWS mirror means the fetch workload does not touch NCBI's own edge at all, so read capacity is Amazon's, not NCBI's. Each public run is an independently addressable anonymous object.
- reliability: Historically flaky FTP uploads ('frequent drop-outs, you only have a few minutes from logging in'); Aspera is the working path. Anonymous S3 mirror can lag NCBI's own copy.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: FTP + Aspera ascend commands, 'recommend it for all medium to large submissions'
  - [2] 2026-10-21: 'Uploads in theory would only be limited by bandwidth'; >10s of TB goes through SRA support
  - [3] 2026-10-21: probe: GET -r 0-511 -> 206, Content-Range: bytes 0-511/312527083 (298 MB object), real AWS headers
- sources:
  - [1] https://www.ncbi.nlm.nih.gov/sra/docs/submitfiles/
  - [2] https://www.biostars.org/p/9572863/
  - [3] https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR000001/SRR000001

## NCBI GEO

- `storage/ncbi-geo` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ncbi.nlm.nih.gov/geo
- free tier: No published volume cap; raw sequence data is redirected to SRA. Notable for retention rather than size. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and anonymous. | metered: no
- identity: anonymous
- interface: rest, ftp
- limits:
  - write-gated (binding): approval step (~5 business days for accession) [1]
- limits note: per-object-cap: not stated (defer to SRA for raw reads). Retention: 'the maximum allowable limit is four years' for private hold, then mandatory public release; records can be edited after release. Binding constraint is the human curation/approval step (~5 business days for accession).
- interface detail: rest
- tooling: GEO FTP/HTTPS plus the GEOmetadb / GEOquery R packages.
- composes with: Not a volume play. The interesting property is private-retention: records may stay private for up to four years before release, with reviewer tokens for anonymous read-only access.
- reliability: Records cannot stay private once an accession is cited in a manuscript or preprint. GEO staff release unilaterally.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'the maximum allowable limit is four years', forced release if accession cited
  - [2] 2026-10-21: 5 business days for accession, private-until-published policy
- sources:
  - [1] https://www.ncbi.nlm.nih.gov/geo/info/faq.html
  - [2] https://www.ncbi.nlm.nih.gov/geo/info/submission.html
