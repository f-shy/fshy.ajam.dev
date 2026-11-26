# gnu ftp

> gnu.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gnu/ | JSON https://fshy.ajam.dev/api/v1/entity/gnu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GNU Savannah download area (download.savannah.gnu.org / .nongnu.org)

- `storage/gnu-savannah-download-area` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T12:15:41.027Z (live) | stale on 2026-12-10
- url https://savannah.gnu.org
- free tier: The space given to you on this server is given for the expressed purpose of advancing free software that can run in free operating systems, documenting such software, or creating free educational textbooks. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The Download Area page states no per-file size limit; uploads are made with scp or rsync into /releases/GROUP_NAME/.
- retention: Our intent is to provide a permanent home for all versions of your project. We do reserve the right, however, to discontinue hosting a project. | source: [1] | note: In order to preserve history and complete transparency, projects that contain anything substantive are not removed.
- egress: Files at download.savannah.nongnu.org/releases/GROUP_NAME/ are multiplexed between all mirrors, and an upload can take up to 24 hours to appear on all mirrors. unverified: no egress charge or volume quota is stated on the page. | metered: no
- identity: email
- interface: scp, rsync, ssh
- limits note: per-object-cap: none published. Structural caps that matter more: (1) SFTP IS DISABLED - announced 2023-11, 'we've found a vulnerability in our SFTP setup, and couldn't fix it otherwise than completely disabling SFTP. This affects uploading files to the download host'. Because OpenSSH >= 9.0 makes scp use SFTP by default, `scp -O` is required or every upload fails. (2) GPG-signing is expected (the docs tell you to upload foo.tar.gz + foo.tar.gz.sig) though not enforced: 'unlike ftp.gnu.org, Savannah doesn't enforce using GPG signatures for releases'. (3) Write access requires a registered SSH key on the account.
- interface detail: part of limits note
- tooling: SSH public-key auth only. Upload via scp (the -O flag is mandatory, see limits) or rsync to download.savannah.nongnu.org releases directory. Removal via restricted SSH commands ssh host rm or rmdir. Gnulib build-aux gnupload script is supported. Read side is plain anonymous HTTP from the mirror ring.
- composes with: Each non-GNU package submitted for hosting is evaluated and approved by Savannah administrators. Limits on files, versions or groups: unverified, not stated on the pages read.
- reliability: Two real breakages. First, SFTP-off is a live trap for any modern client - a naive `scp` on OpenSSH 9+ silently fails. Second, the mirror ring is uneven: the same lzip tarball (123,850 bytes) took 4.6 s once and timed out at 21 s on the redirect target (ftp.cc.uoc.gr) another time, so per-mirror health varies and single-stream fetch is not trustworthy. Site pages also intermittently serve a Kant-quoting anti-scraper page instead of content - the register/ and requirements.php URLs both did this via the reader while the Wayback copy of the same page was clean.
- notes: In order to preserve history and complete transparency, we will not remove projects that contain anything substantive.
- evidence:
  - [2] 2026-10-21: (and the nongnu mirror) - `scp foo.tar.gz ... [address removed]:/releases/GROUP_NAME/`; 'As of 2025-01, SFTP is disabled on Savannah. Please add the -O option'; 'Savannah doesn't enforce using GPG signatures'
  - [3] 2026-10-21: '[download] SFTP disabled ... completely disabling SFTP. This affects uploading files to the download host'
  - [4] 2026-10-21: 'Our intent is to provide a permanent home for all versions of your project'; hosting restricted to free-software purpose; project evaluation by Savannah hackers
  - [5] 2026-10-21: 'Evaluate and approve non-gnu packages submitted for hosting'
  - [6] 2026-10-21: probe: GET -> 302 to https://fosszone.csd.auth.gr/nongnu/lzip/lzip-1.24.tar.gz -> 200, Content-Length 123850
  - [7] 2026-10-21: backend moved to nfs1/ceph: 'This increases the disk space'
  - [1] 2026-11-09: the live requirements URL served an unrelated text page, not the hosting requirements | capture: sha256:bb8f82c246f0e644027fcb5bece6a83781760d51e9bbc3fa398209b3fd7ff102 | quote: Denied it. But this rule becomes.
  - [4] 2026-11-09: the archived requirements page states the purpose clause | capture: sha256:2741040125e43085fffff2acf04671600ca58c8598fdc4c17176ce94bafbfb47 | quote: The space given to you on this server is given for the expressed purpose of advancing free software that can run in free operating systems, documenting such software, or creating free educational textbooks.
  - [4] 2026-11-09: the page states the permanence intent and the right to discontinue hosting | capture: sha256:2741040125e43085fffff2acf04671600ca58c8598fdc4c17176ce94bafbfb47 | quote: Our intent is to provide a permanent home for all versions of your project. We do reserve the right, however, to discontinue hosting a project.
  - [1] 2026-11-11: the requirements page states that projects containing anything substantive are not removed | capture: sha256:674b38d654b53b88391a24e941b683f6c12ba2858ad89d94a93a2f4e2043c247 | quote: In order to preserve history and complete transparency, we will not remove projects that contain anything substantive.
  - [1] 2026-11-11: the requirements page states the purpose the granted space may serve | capture: sha256:674b38d654b53b88391a24e941b683f6c12ba2858ad89d94a93a2f4e2043c247 | quote: The space given to you on this server is given for the expressed purpose of advancing free software that can run in free operating systems, documenting such software, or creating free educational textbooks.
  - [1] 2026-11-11: the requirements page states the permanence intent and the right to discontinue hosting | capture: sha256:674b38d654b53b88391a24e941b683f6c12ba2858ad89d94a93a2f4e2043c247 | quote: Our intent is to provide a permanent home for all versions of your project. We do reserve the right, however, to discontinue hosting a project.
  - [2] 2026-11-19: the first-party download-area page confirms SFTP is disabled and scp -O is required | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: As of 2025-01, SFTP is disabled on Savannah. Please add the -O option to scp command line if you use OpenSSH 9.0 or later:
  - [4] 2026-11-19: the archived first-party requirements page states the permanence intent | capture: sha256:2741040125e43085fffff2acf04671600ca58c8598fdc4c17176ce94bafbfb47 | quote: Our intent is to provide a permanent home for all versions of your project. We do reserve the right, however, to discontinue hosting a project.
  - [2] 2026-11-25: uploads use scp | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: On Savannah, you can use scp to upload your GPG signed files.
  - [2] 2026-11-25: uploads can use rsync | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: > Alternatively, you can [use rsync](https://savannah.gnu.org/maintenance/DownloadArea/#rsync).
  - [2] 2026-11-25: removal uses ssh rm and ssh rmdir | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: For removing wrongly uploaded files and directories, use `ssh rm` and `ssh rmdir`.
  - [2] 2026-11-25: downloads are multiplexed between mirrors; uploads take up to 24 hours to appear | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: This is multiplexed between all mirrors, hopefully picking a nearby and up-to-date one. Please expect a delay of up to 24 hours for an upload on Savannah to appear on all mirrors.
  - [5] 2026-11-25: non-GNU packages are evaluated and approved before hosting | capture: sha256:b3383e330177e24735dc2dfd7e8b319ba165690fa6a22b686627bff9a30abf89 | quote: 1. Evaluate and approve non-gnu packages submitted for hosting.
  - [4] 2026-11-25: substantive projects are not removed | capture: sha256:2741040125e43085fffff2acf04671600ca58c8598fdc4c17176ce94bafbfb47 | quote: In order to preserve history and complete transparency, we will not remove projects that contain anything substantive.
  - [4] 2026-11-25: permanence intent and the right to discontinue hosting | capture: sha256:2741040125e43085fffff2acf04671600ca58c8598fdc4c17176ce94bafbfb47 | quote: Our intent is to provide a permanent home for all versions of your project. We do reserve the right, however, to discontinue hosting a project.
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
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:41.638Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: mirroring ftp.gnu.org is an inbound rsync commitment of about 169 GB, not a place to put data | capture: sha256:2d5ec237efe90f3dd927a5d8850972a5b2be94ddd1409caccd13d56e3c4c4842 | quote: Mirroring the GNU FTP server requires approximately 169GB disk space (as of June 2024). You can rsync directly from ftp.gnu.org:
  - [2] 2026-11-19: uploading to ftp.gnu.org requires prior registration, so it is not an open write target | capture: sha256:0ab94f6015dbee3f76005959fe5d936efb1db8063a8deb7f47bdca8b1e1923ab | quote: In order to upload new releases to `ftp.gnu.org` or `alpha.gnu.org`, you first need to register the necessary information.
- sources:
  - [1] https://www.gnu.org/server/mirror.html
  - [2] https://www.gnu.org/prep/maintain/html_node/Automated-FTP-Uploads.html
