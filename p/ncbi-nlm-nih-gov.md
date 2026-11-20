# NCBI GEO

> ncbi.nlm.nih.gov | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ncbi-nlm-nih-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/ncbi-nlm-nih-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NCBI SRA — with anonymous read via AWS Open Data

- `storage/ncbi-sra-with-anonymous-read-via-aws-open-data` | qualifies | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:36.637Z (live) | stale on 2026-12-04
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
- notes: Aspera Connect is software that allows download and upload via a web plugin for popular browsers on machines running Linux, Windows, and Macintosh. The software also includes a command line tool (ascp) that allows scripted data transfer.
- evidence:
  - [1] 2026-10-21: FTP + Aspera ascend commands, 'recommend it for all medium to large submissions'
  - [2] 2026-10-21: 'Uploads in theory would only be limited by bandwidth'; >10s of TB goes through SRA support
  - [3] 2026-10-21: probe: GET -r 0-511 -> 206, Content-Range: bytes 0-511/312527083 (298 MB object), real AWS headers
  - [1] 2026-11-11: the submission documentation names Aspera Connect and its ascp command line tool | capture: sha256:74ba2f3cf78b1861a22705f6b3e543dbb17e30f1ce3532133fe3aa7398b032b1 | quote: Aspera Connect is software that allows download and upload via a web plugin for popular browsers on machines running Linux, Windows, and Macintosh. The software also includes a command line tool (ascp) that allows scripted data transfer.
  - [1] 2026-11-19: the SRA submission documentation describes Aspera's ascp command-line tool for scripted transfers | capture: sha256:66eedf34a62cdf36c9c67de2ea9f9531495889c4cf71abfa6b9587d54c6cdd1c | quote: The software also includes a command line tool (ascp) that allows scripted data transfer.
- sources:
  - [1] https://www.ncbi.nlm.nih.gov/sra/docs/submitfiles/
  - [2] https://www.biostars.org/p/9572863/
  - [3] https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR000001/SRR000001

## NCBI GEO

- `storage/ncbi-geo` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:36.640Z (live) | stale on 2026-12-04
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
- notes: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time.
- evidence:
  - [1] 2026-10-21: 'the maximum allowable limit is four years', forced release if accession cited
  - [2] 2026-10-21: 5 business days for accession, private-until-published policy
  - [3] 2026-11-11: the FAQ states a maximum private-hold limit of four years | capture: sha256:ab0d121328a7fd3e0844fab0dadc8641f135ab7f981d55f3b51f9ca9a04aae81 | quote: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time.
  - probe:https://www.ncbi.nlm.nih.gov/geo/info/faq.html 2026-11-11: the live FAQ answered a Cloudflare challenge page on 2026-11-11 | capture: sha256:89bfbc0e31e51a0719b20725ffc13f90a6df104108f122bef6edd24e2c4a8e6e | quote: "challenge": { "detected": true, "signature": "cloudflare-challenge:title:checking your browser"
  - [3] 2026-11-19: the archived first-party FAQ states a four-year maximum private-hold limit | capture: sha256:f546427672973836007aeb2a8bc3109a72b588f40b4730f746a2836e5f6874ea | quote: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time
- sources:
  - [1] https://www.ncbi.nlm.nih.gov/geo/info/faq.html
  - [2] https://www.ncbi.nlm.nih.gov/geo/info/submission.html
  - [3] https://web.archive.org/web/20260103201412/https://www.ncbi.nlm.nih.gov/geo/info/faq.html
