# Launchpad PPA

> launchpad.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/launchpad/ | JSON https://fshy.ajam.dev/api/v1/entity/launchpad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Launchpad PPA (Ubuntu Personal Package Archive)

- `storage/launchpad-ppa` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://launchpad.net/ubuntu/+ppas
- free tier: 8 GiB of disk per PPA - current official reference: 'Disk space | 8 GiB; larger quotas considered on request at https://answers.launchpad.net/launchpad'. (Historical: PPAs were raised to a 2 GiB minimum in 2010 per the Launchpad blog; the 8 GiB figure is the current documented one.) 'PPAs per owner: One or more per user or team; each has its own URL.' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: This is the binding constraint - you cannot push an arbitrary tarball; everything must be a signed source package (.dsc + orig.tar.gz + debian.tar.gz), so a 4 GB blob becomes one 4 GB .orig.tar.gz (allowed, but must be a valid Debian source package). retention: indefinite - 'A published package remains available until .. | source: [1] | note: not stated
- egress: Free: 'Data transfer | No fixed cap; unusual volumes may trigger contact from Launchpad.' Served from ppa.launchpadcontent.net with no billing. | metered: no
- identity: email
- interface: rest, ftp, rsync, rclone
- limits:
  - per-ip-shaping (binding): 70 KB/s [1]
- limits note: per-object-cap: 'Uploadable artefacts | Source packages only; pre-built binary uploads are rejected' and 'Package formats | .deb only'. This is the binding constraint - you cannot push an arbitrary tarball; everything must be a signed source package (.dsc + orig.tar.gz + debian.tar.gz), so a 4 GB blob becomes one 4 GB .orig.tar.gz (allowed, but must be a valid Debian source package). retention: indefinite - 'A published package remains available until ... the owner removes it, or a later upload supersedes it.' request-rate: not documented; download is plain HTTP. Measured single-stream throughput on a real PPA .deb was only ~70 KB/s.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: `dput`/`dput-ng` (rsync+ftp upload to ppa.launchpad.net), `apt`/`deb-src` for consumption, Launchpad REST API + `launchpadlib`. No rclone backend.
- composes with: Users and teams can create multiple Personal Package Archives with 8 GiB capacity each. Aggregating capacity scales across distinct PPA repositories and signing keys.
- reliability: The read path works and supports ranges (verified 206 on a 1 MB range of a real .deb) but single-connection speed was poor (~70,666 B/s over 15 s). Batch/sharded fetch needed. Upload requires GPG-signed source packages - no arbitrary blob PUT. help.launchpad.net and blog.launchpad.net returned 503 to the reader all session (used archive captures instead), so the live help site is unreliable to fetch programmatically.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: quotas table: 'Disk space | 8 GiB; larger quotas considered on request'; 'Data transfer | No fixed cap'; 'PPAs per owner | One or more per user or team'
  - withheld 2026-10-21: (captured 2024-12-11) - 'we've gone ahead and upgraded every PPA to a minimum of 2 GiB'
  - [2] 2026-10-21: probe: GET -> 200, directory listing of real .deb files
  - withheld 2026-10-21: probe: ranged GET bytes 0-1048575 on libpython3.12-dbg_3.12.15-1+jammy1_amd64.deb -> 206, 1,048,576 bytes, 70,666 B/s
  - [3] 2026-10-21: probe: GET -> 200, 16,928 bytes (real Release file)
- sources:
  - [1] https://launchpad-help.readthedocs.io/en/latest/how-to/distribute-ubuntu-software.html
  - [2] http://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/pool/main/p/python3.12/
  - [3] http://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/dists/noble/Release

## Launchpad project file releases (+download area)

- `storage/launchpad-project-file-releases` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://launchpad.net
- free tier: 1 GiB PER FILE in the project file release area - a separate, much smaller surface than the PPA. The manual says: 'Each individual file must be no more than 1 GiB and you must be the: project maintainer / project driver / or the series release manager.' There is no published total-per-project cap; the unit of accounting is the individual release file. (The 8 GiB figure widely quoted for Launchpad is the PPA disk quota - it does not govern file releases.) | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GiB PER FILE | bytes: 1073741824 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, no billing. Files are served from launchpadlibrarian.net behind a 303 redirect. No published transfer cap; a measured ~70 KB/s single-stream on a PPA .deb is a throughput problem rather than a quota one. | metered: no
- identity: institution
- interface: rest, sftp, rsync
- limits:
  - per-object-cap (binding): 1 GiB PER FILE [1]
- limits note: per-object-cap: 1 GiB hard per release file. Also content-typed: files must fall into 'code release tarball / installer files / README or other documentation / changelog file / release notes' - arbitrary blobs are off-spec. retention: indefinite per release. request-rate: not documented for the file area; the docs page itself is flagged 'migrated from help.launchpad.net as is, and has not yet been revised'.
- interface detail: rest
- tooling: Web upload per release ('Add download file') is the documented path - no SFTP/rsync equivalent to Savannah or SourceForge for the release area. Automation goes through the Launchpad web service API: `launchpadlib` (Python), the `+download` URL shape, and hardware-bound API tokens. Consumer side is plain HTTPS GET with an MD5 and optional GPG signature per file.
- composes with: unlimited projects x unlimited series x unlimited releases x 1 GiB per file. At 1 GiB granularity 500 GB is 500 files - feasible but operationally noisy, and every upload is a web action unless scripted via launchpadlib. Distinct from the PPA path (8 GiB/PPA, .deb-only, dput/rsync upload).
- reliability: Read path verified working end-to-end (303 -> launchpadlibrarian.net -> 200, 419,427 bytes). Write path is web/API only with no bulk transport, so it is a worse fit than a forge with SFTP. The docs being stale-and-unrevised is a real risk: the 1 GiB number is from a migrated page, not a maintained limits table.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Each individual file must be no more than 1 GiB'; file must be one of code release tarball / installer / README / changelog / release notes
  - withheld 2026-10-21: same page - 'This document has been migrated from help.launchpad.net as is, and has not yet been revised.'
  - [2] 2026-10-21: probe: GET -> 303 to https://launchpadlibrarian.net/188644793/libeatmydata-105.tar.gz -> 200, Content-Length 419427
  - [3] 2026-10-21: round-2 cross-check: PPA quota is 8 GiB/PPA with GPG-signed source packages only ()
- sources:
  - [1] https://documentation.ubuntu.com/launchpad/user/explanation/projects/publishing-files/
  - [2] https://launchpad.net/libeatmydata/trunk/release-105/+download/libeatmydata-105.tar.gz
  - [3] https://launchpad-help.readthedocs.io/en/latest/how-to/distribute-ubuntu-software.html
