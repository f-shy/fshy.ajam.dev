# ena

> ebi.ac.uk | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ebi-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/ebi-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BioStudies / ArrayExpress (EMBL-EBI)

- `storage/biostudies-arrayexpress` | qualifies | evidence reported | binding per-ip-shaping | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:17.591Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ebi.ac.uk/biostudies
- free tier: Free deposit, no published cap. 'Is there a cost to deposit data in BioStudies? No, both deposition of data to BioStudies and data access are free of charge.' Docs discuss 'larger data volumes (hundreds of GiB)' as routine. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Binding constraint on read is per-ip-shaping. 1 stream 7 KB/s, 16 parallel 25 KB/s against the EBI FTP edge. Retention: permanent, DOI auto-assigned; files can sit 'hold until published' indefinitely before release. | source: [1] | note: not stated
- egress: Free and anonymous. 'Anonymous downloads are enabled' over FTP; also HTTPS. No egress meter anywhere in the docs. | metered: no
- identity: email | detail: depositing needs a BioStudies submission-tool account, created with a name, an email address and a password; the ORCID field is optional. No card and no phone number is asked for. Reading published data needs no account at all.
- interface: ftp, nfs
- limits:
  - per-ip-shaping (binding): 7 KB/s [1]
  - per-ip-shaping (binding): 25 KB/s [1]
- limits note: Per-object-cap: none stated; Aspera recommended above 10 GiB. Binding constraint on read is per-ip-shaping. 1 stream 7 KB/s, 16 parallel 25 KB/s against the EBI FTP edge. Retention: permanent, DOI auto-assigned; files can sit 'hold until published' indefinitely before release.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: ftp
- tooling: Submission Tool + FTP + Aspera (ascp) in; anonymous FTP/HTTPS out. Path is predictable: /biostudies/<mode>/<COLL>/<COLL0-99>/<ACC>/Files/ where mode is `fire` or `nfs`.
- composes with: ArrayExpress is a BioStudies collection, so one account covers both. Unlimited accessions per account; each accession gets its own directory tree. Read side anonymous per-file HTTP, so it fronts to a CDN trivially.
- reliability: Read edge is slow per connection and stalls connections under parallel load (one of 16 timed out with 0 bytes). Fetches from the same EBI edge as ENA/PRIDE, so they are one throughput pool, not three.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'both deposition of data to BioStudies and data access are free of charge', 'Aspera transfer for medium to large (10 GiB+)', 'hundreds of GiB'
  - [2] 2026-10-21: 'Anonymous downloads are enabled', exact FTP path scheme
  - [3] 2026-10-21: probe: GET -> 200, Apache directory index listing 10 files
  - withheld 2026-10-21: probe: GET .../Files/1_TCGA_signature_A_top_10percent.txt -> 200, Content-Length 1282965, downloaded 1282965 bytes, sha256 aff47b60a0ccec2bbf433186a933627f01f54f43a2c2d326fac431a3a961e028, body is the real TSV
  - [4] 2026-11-01: the registration form's fields are name, email, password and an optional ORCID, with no card or phone field | capture: sha256:0f274ec07c71a074be80d6d34613cecf7ee8a8d2da4aa33b9233748bd7754204 | quote: Note that ORCID field is optional.
  - [4] 2026-11-01: the submission tool serves a self-service registration form, which is the only gate on deposition | capture: sha256:0f274ec07c71a074be80d6d34613cecf7ee8a8d2da4aa33b9233748bd7754204 | quote: Please provide the information below to create a new account.
  - [1] 2026-11-01: deposition and access are both free of charge, and the only gate on deposition is the registration form | capture: sha256:34bb0cfe538eaeaf07e9049557b0e1973cce33cc837e3f4f7edc6cfc3a03da15 | quote: both deposition of data to BioStudies and data access are free of charge
- sources:
  - [1] https://www.ebi.ac.uk/biostudies/submit
  - [2] https://www.ebi.ac.uk/biostudies/help#download
  - [3] https://ftp.ebi.ac.uk/biostudies/fire/S-BSST/S-BSST0-99/S-BSST7/Files/
  - [4] https://www.ebi.ac.uk/biostudies/submissions/signup

## ENA (European Nucleotide Archive) — Webin

- `storage/ena-webin` | qualifies | evidence reported | binding retention-clamped | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ebi.ac.uk/ena
- disagrees on identity_kind: `storage/ena` says email, `storage/ena-webin` says anonymous
- disagrees on verdict: `storage/ena` says fails-quota, `storage/ena-webin` says qualifies
- free tier: No fixed quota. Own fair-use policy: 'We place no absolute limit within the 2-month period on the total volume of user data that may exist in a data upload area at any one time' and 'we ... expect that volumes would not exceed 10 Terabytes under normal circumstances.' | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Retention: transit area purged after 2 months if not submitted; once submitted, ENA is permanent | days: 60 | source: [1] | note: not stated
- egress: Unmetered and anonymous. ftp.sra.ebi.ac.uk is CORS-open (`Access-Control-Allow-Origin: *`) and already served through Cloudflare (`Server: cloudflare`), so CF is in front by default. | metered: no
- identity: anonymous
- interface: sftp, ftp, rclone, cli
- limits:
  - per-ip-shaping: 45 KB/s [1]
  - per-ip-shaping: 430 KB/s [1]
  - retention-clamped (binding): Retention: transit area purged after 2 months [1]
- limits note: per-object-cap: none documented per file; per-request volume soft-capped at ~10 TB per 2-month window per upload area, and upload areas are not backed up. Retention: transit area purged after 2 months if not submitted; once submitted, ENA is permanent. Binding constraint on READ is per-ip-shaping: single stream 45 KB/s, 8 parallel ranged GETs 430 KB/s (9.6x).
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: sftp
- tooling: Webin-CLI (github.com/enasequence/webin-cli), plus plain FTP/Aspera. Read side is plain HTTPS/FTP with HTTP range support. Works with rclone's http/`sftp` remotes and curl.
- composes with: One Webin account = unlimited studies. The upload area is a transit buffer (10 TB documented expectation), while published accessions are permanent and unmetered on the read side. Multiply across accounts/centres; read side needs no account at all, so the fetch workload is uncapped regardless of how many deposit accounts exist.
- reliability: Upload path is the weak side. FTP sessions drop out, Aspera recommended; upload area is explicitly 'not backed up'.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: quotes 'no absolute limit within the 2-month period', 'would not exceed 10 Terabytes under normal circumstances', 'temporary transit area which is not backed up'
  - [2] 2026-10-21: probe: GET -r 0-1023 -> 206 Partial Content, Content-Range: bytes 0-1023/23319983, body starts 1f 8b 08 00 (real gzip magic), Server: cloudflare
  - withheld 2026-10-21: probe: 8 parallel ranged GETs -> 8,000,000 bytes in 18.6s (430 KB/s) vs 1 connection 1,001,024 bytes in 22.2s (45 KB/s)
- sources:
  - [1] https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html
  - [2] https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR000/SRR000001/SRR000001_1.fastq.gz

## ena (european nucleotide archive)

- `storage/ena` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ebi.ac.uk/ena/browser/submit
- disagrees on identity_kind: `storage/ena` says email, `storage/ena-webin` says anonymous
- disagrees on verdict: `storage/ena` says fails-quota, `storage/ena-webin` says qualifies
- free tier: none reachable: Free and effectively unlimited, but Webin accounts are for nucleotide sequence submission only; the upload area is 'a temporary transit area which is not backed up and subject to a fair use | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free and effectively unlimited, but Webin accounts are for nucleotide sequence submission only; the upload area is 'a temporary transit area which is not backed up and subject to a fair use
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free and effectively unlimited, but Webin accounts are for nucleotide sequence submission only; the upload area is 'a temporary transit area which is not backed up and subject to a fair use
  - [2] 2026-10-21: cited as the basis of the rejection: Free and effectively unlimited, but Webin accounts are for nucleotide sequence submission only; the upload area is 'a temporary transit area which is not backed up and subject to a fair use
- sources:
  - [1] https://www.ebi.ac.uk/ena/browser/submit
  - [2] https://ena-docs.readthedocs.io/en/latest/submit/general-guide/programmatic.html
