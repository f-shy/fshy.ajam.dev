# RepOD

> repod.icm.edu.pl | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/repod-icm-edu-pl/ | JSON https://fshy.ajam.dev/api/v1/entity/repod-icm-edu-pl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RepOD — Repository for Open Data (ICM, University of Warsaw)

- `storage/repod-repository-for-open-data` | qualifies | evidence documented | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:19.657Z (live) | stale on 2026-12-26
- url https://repod.icm.edu.pl
- free tier: Repozytorium akceptuje zbiory danych o dowolnej wielkości. Jedynym ograniczeniem jest limit wielkości pojedynczego pliku, wynoszący 5GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per single file | bytes: 5000000000 | source: [1] | note: The size limit of a single file is 5.0 GB, and the size limit for the sum of files being transferred at the same time is 20.0 GB. The size of the entire dataset is not limited.
- retention: Publication assigns a DOI and freezes that version. Versions are immutable after publish, so this is write-once-per-version, not mutable working storage. | source: [1] | note: Po opublikowaniu danej wersji zbioru danych nie ma możliwości jej usunięcia.
- egress: Repozytorium nie pobiera opłat od użytkowników deponujących oraz pobierających dane. | metered: no
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
- notes: No dataset-size limit at all: 'Repozytorium akceptuje zbiory danych o dowolnej wielkości. Jedynym ograniczeniem jest limit wielkości pojedynczego pliku, wynoszący 5GB' (the repository accepts datasets of any size; the only limit is 5 GB per single file). A sibling UW deposit guide adds '20 GB for the sum of files transferred simultaneously'. Storage itself is unpriced: 'Korzystanie z repozytorium nie wiąże się z żadnymi opłatami' (using the repository involves no fees).
- evidence note: the deposit page states that datasets may be of any size and that the only limit is 5 GB per single file
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
  - [1] 2026-11-09: the deposit page states that datasets may be of any size and that the only limit is 5 GB per single file | capture: sha256:a8461eb8b153c15fe91472a3aaf63b8a0135fbcc7694a9ff09192e4d5157fed3 | quote: Repozytorium akceptuje zbiory danych o dowolnej wielkości. Jedynym ograniczeniem jest limit wielkości pojedynczego pliku, wynoszący 5GB.
  - [1] 2026-11-09: the page states that no fee is charged to users who deposit or download data | capture: sha256:a8461eb8b153c15fe91472a3aaf63b8a0135fbcc7694a9ff09192e4d5157fed3 | quote: Repozytorium nie pobiera opłat od użytkowników deponujących oraz pobierających dane.
  - [1] 2026-11-09: the page states a 5 GB limit on a single file | capture: sha256:a8461eb8b153c15fe91472a3aaf63b8a0135fbcc7694a9ff09192e4d5157fed3 | quote: Jedynym ograniczeniem jest limit wielkości pojedynczego pliku, wynoszący 5GB.
  - [4] 2026-11-25: the deposit guide states the per-file cap, the simultaneous-transfer cap and no dataset-size cap | capture: sha256:35ffc6a21b3c5bf2f694884b0ed92975c63d268b1f31d2bf5f58ebaede00c642 | quote: The size limit of a single file is 5.0 GB, and the size limit for the sum of files being transferred at the same time is 20.0 GB. The size of the entire dataset is not limited.
  - [1] 2026-11-25: the preservation policy says a published dataset version cannot be deleted | capture: sha256:a8461eb8b153c15fe91472a3aaf63b8a0135fbcc7694a9ff09192e4d5157fed3 | quote: Po opublikowaniu danej wersji zbioru danych nie ma możliwości jej usunięcia.
  - [1] 2026-11-25: the preservation policy says depositors and downloaders are not charged | capture: sha256:a8461eb8b153c15fe91472a3aaf63b8a0135fbcc7694a9ff09192e4d5157fed3 | quote: Repozytorium nie pobiera opłat od użytkowników deponujących oraz pobierających dane.
- sources:
  - [1] https://info.repod.icm.edu.pl/?page_id=354
  - [2] https://repod.icm.edu.pl/api/info/version
  - [3] https://info.repod.icm.edu.pl/
  - [4] https://info.repod.icm.edu.pl/?lang=en&page_id=534
