# RepOD

> repod.icm.edu.pl | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/repod-icm-edu-pl/ | JSON https://fshy.ajam.dev/api/v1/entity/repod-icm-edu-pl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RepOD — Repository for Open Data (ICM, University of Warsaw)

- `storage/repod-repository-for-open-data` | qualifies | evidence documented | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://repod.icm.edu.pl
- free tier: No dataset-size limit at all: 'Repozytorium akceptuje zbiory danych o dowolnej wielkości. Jedynym ograniczeniem jest limit wielkości pojedynczego pliku, wynoszący 5GB' (the repository accepts datasets of any size; the only limit is 5 GB per single file). A sibling UW deposit guide adds '20 GB for the sum of files transferred simultaneously'. Storage itself is unpriced: 'Korzystanie z repozytorium nie wiąże się z żadnymi opłatami' (using the repository involves no fees). | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per single file | bytes: 5000000000 | source: [1] | note: not stated
- retention: Publication assigns a DOI and freezes that version. Versions are immutable after publish, so this is write-once-per-version, not mutable working storage. | source: [1] | note: not stated
- egress: Free and unmetered. Public files are plain HTTP from repod.icm.edu.pl with no egress pricing anywhere in the product; downloads are the same Dataverse /api/access/datafile path used by Harvard. Probe: GET /api/access/datafile/39782 -> 200, 7,459 bytes returned, MD5 published per file for verification. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 5 GB per single file [1]
  - per-object-cap (binding): 5 GB/file [1]
- limits note: Per-object-cap 5 GB/file and 20 GB per simultaneous transfer batch are the only hard numbers; there is NO per-dataset and NO per-account byte ceiling. 1,000 files per zip ingest (Dataverse default). Publication assigns a DOI and freezes that version. Versions are immutable after publish, so this is write-once-per-version, not mutable working storage. Embargo up to 36 months.
- interface detail: rest
- tooling: Native Dataverse 4.11 REST API, live and unauthenticated for reads: GET /api/info/version -> {"version":"1.3.2-05b9a3acf7fe552a849e874762b86d0605e47186"}; GET /api/search?q=*&type=dataset -> total_count 4545; type=file -> 65370 items. The repository's own policy page states uploads work 'zarowno przez graficzny interfejs ... jak i za pomocą interfejsu API' (both GUI and API). Standard Dataverse ingest: DVUploader (github.com/GlobalDataverseCommunityConsortium/dataverse-uploader), pyDataverse, SWORD v2. No rclone backend, but the REST loop is ~15 lines.
- composes with: Per-record cap is the unit, not per-account: unlimited datasets x unlimited size each, so 500 GB is 100 files of 5 GB inside one dataset. No account multiplication needed. Multiple datasets multiply further. One email/password account is enough; signup is self-service ('Sign up for an account to log in with your email or username and password').
- reliability: Institutional (ICM UW, Polish national open-science infrastructure since 2020), CoreTrustSeal-lineage Dataverse with per-file MD5 published; the real friction is moderation-by-metadata-quality, not bytes, and published versions cannot be edited in place.
- notes: the same as the free tier
- evidence note: The conditional range behaviour was reproduced, both legs. Was documented; now documented.
- extras:
  - verified[0].url: https://repod.icm.edu.pl/api/info/version
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 83
  - verified[0].sha256: 06a6ec2a82903eca9e6937ee2c251d1894a8ff9418910e5a77806885e80dcd05
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [2] 2026-10-22: the Dataverse version, which decides whether the quota endpoint exists. Re-read https://repod.icm.edu.pl/api/info/version: HTTP 200, 83 bytes, sha256 06a6ec2a82903eca. Quoted: {"status":"OK","data":{"version":"1.3.2-05b9a3acf7fe552a849e874762b86d0605e47186"}}
  - [1] 2026-10-21: 'Repozytorium akceptuje zbiory danych o dowolnej wielkości. Jedynym ograniczeniem jest limit wielkości pojedynczego pliku, wynoszący 5GB' + same page states API upload is supported
  - [3] 2026-10-21: 'powstałym z myślą o wszystkich naukowcach i instytucjach' (built for all scientists and institutions); 'Korzystanie z repozytorium nie wiąże się z żadnymi opłatami'
  - withheld 2026-10-21: probe: GET /api/info/version -> 200 Dataverse 1.3.2; GET /api/access/datafile/39782 -> 200 7,459 bytes; GET /api/search?q=*&type=dataset -> 4,545 datasets live
  - probe:https://repod.icm.edu.pl/api/access/datafile/39782 2026-10-22: ranged GET 2026-10-22 on /api/access/datafile/39782: 206 Partial Content, Content-Range bytes 0-1023/7459; same request on /api/access/datafile/18: 200 OK, full Content-Length, no Content-Range
- sources:
  - [1] https://info.repod.icm.edu.pl/?page_id=354
  - [2] https://repod.icm.edu.pl/api/info/version
  - [3] https://info.repod.icm.edu.pl/
