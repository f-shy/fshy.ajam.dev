# gnu ftp

> gnu.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gnu/ | JSON https://fshy.ajam.dev/api/v1/entity/gnu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GNU Savannah download area (download.savannah.gnu.org / .nongnu.org)

- `storage/gnu-savannah-download-area` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://savannah.gnu.org
- free tier: No published byte quota found on any Savannah page - the hosting-requirements doc speaks only in terms of purpose ('The space given to you on this server is given for the expressed purpose of advancing free software') and permanence ('Our intent is to provide a permanent home for all versions of your project'), never a number. Disk was moved to Ceph/NFS precisely to remove the old ceiling (savannah-hackers-public, 2019-04: 'This increases the disk space and moves onto the new cephs storage'). | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: No published byte quota found on any Savannah page - the hosting-requirements doc speaks only in terms of purpose ('The space given to you on this server is given for the expressed purpose of advancing free software') and permanence ('Our intent is to provide a permanent home for all versions of your project'), never a number | source: [1] | note: not stated
- egress: Free and mirrored: `download.savannah.{gnu,nongnu}.org` redirect to a world-wide mirror ring. Verified live: a GET 302s to a national mirror (fosszone.csd.auth.gr) which serves 200 with real bytes. No metering, no billing. | metered: no
- identity: email
- interface: scp, rsync, ssh
- limits note: per-object-cap: none published. Structural caps that matter more: (1) SFTP IS DISABLED - announced 2023-11, 'we've found a vulnerability in our SFTP setup, and couldn't fix it otherwise than completely disabling SFTP. This affects uploading files to the download host'. Because OpenSSH >= 9.0 makes scp use SFTP by default, `scp -O` is required or every upload fails. (2) GPG-signing is expected (the docs tell you to upload foo.tar.gz + foo.tar.gz.sig) though not enforced: 'unlike ftp.gnu.org, Savannah doesn't enforce using GPG signatures for releases'. (3) Write access requires a registered SSH key on the account.
- interface detail: part of limits note
- tooling: SSH public-key auth only. Upload via scp (the -O flag is mandatory, see limits) or rsync to download.savannah.nongnu.org releases directory. Removal via restricted SSH commands ssh host rm or rmdir. Gnulib build-aux gnupload script is supported. Read side is plain anonymous HTTP from the mirror ring.
- composes with: One Savannah group per project, unlimited files per group, unlimited versions retained forever. Accounts are free; the gate is that a human evaluates the package ('Evaluate and approve non-gnu packages submitted for hosting'), so cardinality is bounded by reviewer throughput, not by quota. For GNU packages ftp.gnu.org/alpha.gnu.org is a second surface with an automated signed-upload path.
- reliability: Two real breakages. First, SFTP-off is a live trap for any modern client - a naive `scp` on OpenSSH 9+ silently fails. Second, the mirror ring is uneven: the same lzip tarball (123,850 bytes) took 4.6 s once and timed out at 21 s on the redirect target (ftp.cc.uoc.gr) another time, so per-mirror health varies and single-stream fetch is not trustworthy. Site pages also intermittently serve a Kant-quoting anti-scraper page instead of content - the register/ and requirements.php URLs both did this via the reader while the Wayback copy of the same page was clean.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: (and the nongnu mirror) - `scp foo.tar.gz ... [address removed]:/releases/GROUP_NAME/`; 'As of 2025-01, SFTP is disabled on Savannah. Please add the -O option'; 'Savannah doesn't enforce using GPG signatures'
  - [3] 2026-10-21: '[download] SFTP disabled ... completely disabling SFTP. This affects uploading files to the download host'
  - [4] 2026-10-21: 'Our intent is to provide a permanent home for all versions of your project'; hosting restricted to free-software purpose; project evaluation by Savannah hackers
  - [5] 2026-10-21: 'Evaluate and approve non-gnu packages submitted for hosting'
  - [6] 2026-10-21: probe: GET -> 302 to https://fosszone.csd.auth.gr/nongnu/lzip/lzip-1.24.tar.gz -> 200, Content-Length 123850
  - [7] 2026-10-21: backend moved to nfs1/ceph: 'This increases the disk space'
- sources:
  - [1] https://savannah.gnu.org/register/requirements.php
  - [2] https://savannah.gnu.org/maintenance/DownloadArea/
  - [3] https://lists.defectivebydesign.org/archive/html/savannah-announce/2023-11/msg00000.html
  - [4] https://web.archive.org/web/20251221133733/https://savannah.gnu.org/register/requirements.php
  - [5] https://savannah.gnu.org/maintenance/HowToBecomeASavannahHacker/
  - [6] https://download.savannah.nongnu.org/releases/lzip/lzip-1.24.tar.gz
  - [7] https://lists.libreplanet.org/archive/html/savannah-hackers-public/2019-04/msg00000.html

## gnu ftp / ftp.gnu.org (mirroring side)

- `storage/gnu-ftp-ftp-gnu-org` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.gnu.org/server/mirror.html
- free tier: none reachable: Not a place to put data - ftp.gnu.org is the canonical GNU release server, and mirroring it is a 169 GB inbound commitment in the wrong direction. The upload registration path exists only… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Not a place to put data - ftp.gnu.org is the canonical GNU release server, and mirroring it is a 169 GB inbound commitment in the wrong direction. The upload registration path exists only…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a place to put data - ftp.gnu.org is the canonical GNU release server, and mirroring it is a 169 GB inbound commitment in the wrong direction. The upload registration path exists only…
  - [2] 2026-10-21: cited as the basis of the rejection: Not a place to put data - ftp.gnu.org is the canonical GNU release server, and mirroring it is a 169 GB inbound commitment in the wrong direction. The upload registration path exists only fo
- sources:
  - [1] https://www.gnu.org/server/mirror.html
  - [2] https://www.gnu.org/prep/maintain/html_node/Automated-FTP-Uploads.html
