# CPAN

> perl.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/perl/ | JSON https://fshy.ajam.dev/api/v1/entity/perl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CPAN / PAUSE (pause.perl.org)

- `storage/cpan-pause` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pause.perl.org
- free tier: No published byte quota, and the empirical evidence points to a tight request-body limit rather than a documented number: a 2,072,566-byte distribution was rejected with 'Upload failed (request failed with error code 413 Message: Request Entity Too Large)' in April 2024, and the same upload succeeded shortly after, so the 413 was transient rather than a hard 2 MB cap. Treat the ceiling as a few MB, undocumented. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 2 MB cap | bytes: 2000000 | source: [1] | note: not stated
- retention: per-object-cap: undocumented; 413s observed around 2 MB, transient. retention: permanent and immutable per version | source: [1] | note: not stated
- egress: Free and globally mirrored (CPAN mirror ring); no metering. | metered: no
- identity: email
- interface: rest, ftp
- limits:
  - per-object-cap (binding): 2 MB cap [1]
- limits note: per-object-cap: undocumented; 413s observed around 2 MB, transient. retention: permanent and immutable per version. request-rate: not documented. Account gate: PAUSE registration requires a human-readable full name with a space (historical anti-spam check).
- interface detail: rest
- tooling: `cpan-upload` / `pause upload` (HTTP POST to pause.perl.org/pause/authenquery?ACTION=add_uri), plus the historical FTP path. Read side is plain HTTP from any CPAN mirror.
- composes with: unlimited distributions x unlimited versions, but each must be a valid Perl distribution tarball with a version number in the filename, and 'you will never be able to upload a file with identical' name+version. Cardinality is real; size per unit is tiny.
- reliability: The 413 is emitted by the PAUSE web server as a request-body limit, so it behaves like a surprise ceiling that appears and disappears. Even at a generous reading this is a single-digit-MB store - three orders of magnitude from useful.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published byte quota, and the empirical evidence points to a tight request-body limit rather than a documented number: a 2,072,566-byte distribution was rejected with 'Upload failed (request failed with error code 413 Message: Request Entity Too Large)' in April 2024, and the same upload succeeded shortly after, so the 413 was transient rather than a hard 2 MB cap. Treat the ceiling as a few MB, undocumented.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'I've got a 2Mb distribution which is being rejected ... 413 Message: Request Entity Too Large'
  - [3] 2026-10-21: 'I'm now able to upload the distribution, so that issue seems to have been temporary in nature.'
  - [1] 2026-10-21: 'you will never be able to upload a file with identical' filename/version
  - [4] 2026-10-21: PAUSE signup form live
- sources:
  - [1] https://www.cpan.org/modules/04pause.html
  - [2] https://www.mail-archive.com/modules@perl.org/msg53837.html
  - [3] https://www.mail-archive.com/modules@perl.org/msg53838.html
  - [4] https://pause.perl.org/pause/query?ACTION=request_id
