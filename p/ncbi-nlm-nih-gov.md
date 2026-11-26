# NCBI GEO

> ncbi.nlm.nih.gov | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ncbi-nlm-nih-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/ncbi-nlm-nih-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NCBI SRA — with anonymous read via AWS Open Data

- `storage/ncbi-sra-with-anonymous-read-via-aws-open-data` | qualifies | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:15.501Z (live) | stale on 2026-12-10
- url https://www.ncbi.nlm.nih.gov/sra
- free tier: No per-account quota published. Submission is genuinely bulk: FTP, Aspera (`ascp -QT -l 100m -k1 -d`), or Aspermera; operator guidance for 'tens or more terabytes' is to contact SRA support directly. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Maximum individual file size: 100 GB; maximum total per submission: 5 TB. | source: [1] | note: Studies larger than 5 TB should be split across multiple submissions, keeping each submission under this limit.
- retention: Your preload folder and its contents will be automatically deleted after 30 days of inactivity. | source: [1] | note: unverified: no retention period for archived runs is stated on the submission pages; the upload preload folder is deleted after 30 days of inactivity
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
  - [4] 2026-11-25: the submission standards cap an individual file at 100 GB and a submission at 5 TB | capture: sha256:c7c3ca47458edd7d2a8626f29dfd3a7766a45eadbea79f1d9f7c51405a6fa5b9 | quote: | Maximum individual file size | 100 GB | ... | Maximum total per submission | 5 TB |
  - [4] 2026-11-25: studies above 5 TB must be split across submissions | capture: sha256:c7c3ca47458edd7d2a8626f29dfd3a7766a45eadbea79f1d9f7c51405a6fa5b9 | quote: Studies larger than 5 TB should be split across multiple submissions, keeping each submission under this limit.
  - [5] 2026-11-25: the upload preload folder is deleted after 30 days of inactivity | capture: sha256:511cb63273b744936e808ecf25d0ae61a226c578280a6f9a6e443c85bdc677e9 | quote: Please complete your submission within 30 days of creating a preload folder. Your preload folder and its contents will be automatically deleted after 30 days of inactivity.
- sources:
  - [1] https://www.ncbi.nlm.nih.gov/sra/docs/submitfiles/
  - [2] https://www.biostars.org/p/9572863/
  - [3] https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR000001/SRR000001
  - [4] https://www.ncbi.nlm.nih.gov/sra/docs/sra-data-submission-standards/
  - [5] https://submit.ncbi.nlm.nih.gov/subs/sra/

## NCBI GEO

- `storage/ncbi-geo` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:15.500Z (live) | stale on 2026-12-10
- url https://www.ncbi.nlm.nih.gov/geo
- free tier: No published volume cap; raw sequence data is redirected to SRA. Notable for retention rather than size. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: no per-object size limit is stated in the GEO FAQ; submitter-supplied raw data are loaded to SRA
- retention: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time | source: [1] | note: unverified: no retention period for released records is stated; the maximum private-hold limit is four years
- egress: Free and anonymous. | metered: no
- identity: anonymous
- interface: rest, ftp
- limits:
  - write-gated (binding): approval step (~5 business days for accession) [1]
- limits note: per-object-cap: not stated (defer to SRA for raw reads). Retention: 'the maximum allowable limit is four years' for private hold, then mandatory public release; records can be edited after release. Binding constraint is the human curation/approval step (~5 business days for accession).
- interface detail: rest
- tooling: GEO FTP/HTTPS plus the GEOmetadb / GEOquery R packages.
- composes with: Reviewer token allows collaborators or reviewers confidential, read-only access to private data before manuscript publication.
- reliability: Records cannot stay private once an accession is cited in a manuscript or preprint. GEO staff release unilaterally.
- notes: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time.
- evidence:
  - [1] 2026-10-21: 'the maximum allowable limit is four years', forced release if accession cited
  - [2] 2026-10-21: 5 business days for accession, private-until-published policy
  - [3] 2026-11-11: the FAQ states a maximum private-hold limit of four years | capture: sha256:ab0d121328a7fd3e0844fab0dadc8641f135ab7f981d55f3b51f9ca9a04aae81 | quote: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time.
  - probe:https://www.ncbi.nlm.nih.gov/geo/info/faq.html 2026-11-11: the live FAQ answered a Cloudflare challenge page on 2026-11-11 | capture: sha256:89bfbc0e31e51a0719b20725ffc13f90a6df104108f122bef6edd24e2c4a8e6e | quote: "challenge": { "detected": true, "signature": "cloudflare-challenge:title:checking your browser"
  - [3] 2026-11-19: the archived first-party FAQ states a four-year maximum private-hold limit | capture: sha256:f546427672973836007aeb2a8bc3109a72b588f40b4730f746a2836e5f6874ea | quote: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time
  - [1] 2026-11-25: the maximum private-hold limit is four years and the date can change | capture: sha256:bf35ccb036fbdd28c4fca36ecde7fc89a1a81bc3975618d911e7080eafed3852 | quote: Although the maximum allowable limit is four years, this date may be brought forward or pushed back at any time
  - [1] 2026-11-25: GEO loads submitter-supplied raw data into SRA | capture: sha256:bf35ccb036fbdd28c4fca36ecde7fc89a1a81bc3975618d911e7080eafed3852 | quote: Submitter-supplied raw data are loaded to NCBI's [Sequence Read Archive](https://www.ncbi.nlm.nih.gov/sra/) (SRA) database.
  - [1] 2026-11-25:  | capture: sha256:bf35ccb036fbdd28c4fca36ecde7fc89a1a81bc3975618d911e7080eafed3852
- sources:
  - [1] https://www.ncbi.nlm.nih.gov/geo/info/faq.html
  - [2] https://www.ncbi.nlm.nih.gov/geo/info/submission.html
  - [3] https://web.archive.org/web/20260103201412/https://www.ncbi.nlm.nih.gov/geo/info/faq.html
