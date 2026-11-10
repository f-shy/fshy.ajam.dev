# SourceForge File

> sourceforge.net | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sourceforge/ | JSON https://fshy.ajam.dev/api/v1/entity/sourceforge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SourceForge File Release System (FRS) + project web space

- `storage/sourceforge-file-release-system-project-web-space` | qualifies | evidence documented | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://sourceforge.net
- disagrees on identity_kind: `storage/sourceforge-file-release-system-frs-sourceforge-net` says institution, `storage/sourceforge-file-release-system-project-web-space` says any-phone
- disagrees on verdict: `storage/sourceforge-file-release-system-frs-sourceforge-net` says qualifies-with-caveat, `storage/sourceforge-file-release-system-project-web-space` says qualifies
- free tier: NO PUBLISHED QUOTA. The Service Quotas page says verbatim: 'There are currently no fixed capacity limits around usage of our services. In lieu of specific disk usage caps (quotas), we may contact projects if they are using significant storage.' It then gives a soft expectation rather than a cap: 'Keep disk usage to a reasonable level: 5GB or less is ideal. 20-30GB may be permissible. (limits may vary and be flexible depending on the situation)'. So the real number is 20-30 GB of tolerated storage per project, soft, and multiplied by unlimited projects per account. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 'Individual files larger than 10 GB | bytes: 10000000000 | source: [1] | note: not stated
- retention: per-object-cap: 'Individual files larger than 10 GB will not replicate out to our mirrors and can not be downloaded.' That is the hard number and it is published. retention: indefinite - download stats are keyed to path+filename and files are never pruned for age; but the docs warn 'Users are responsible for backing up all of their files | source: [1] | note: not stated
- egress: Free and genuinely CDN'd: 'Unlimited bandwidth for Open Source projects' (create page) plus 'a geographically-distributed network of mirror servers, which receive copies of the files and dispense them to users'. No billing relationship anywhere. Downloads 302 to a geo-selected mirror (zenlayer.dl.sourceforge.net from this vantage) and are served by nginx. | metered: no
- identity: any-phone
- interface: sftp, scp, rsync, ssh
- limits:
  - per-object-cap (binding): per-object-cap: 'Individual files larger than 10 GB [1]
- limits note: per-object-cap: 'Individual files larger than 10 GB will not replicate out to our mirrors and can not be downloaded.' That is the hard number and it is published. retention: indefinite - download stats are keyed to path+filename and files are never pruned for age; but the docs warn 'Users are responsible for backing up all of their files. SourceForge.net will not restore individual files.' request-rate: none published; the docs instead route large uploads to rsync for resume. Filename charset is restricted (no & : % ? / * $, may not start with space or dot).
- interface detail: sftp
- tooling: Native sftp/scp/rsync-over-ssh, no wrapper needed. FRS host `frs.sourceforge.net` path `/home/frs/project/PROJECT_UNIX_NAME/`; web host `web.sourceforge.net` path `/home/project-web/PROJECT_UNIX_NAME/htdocs`. SFTP is batch-scriptable with key auth ('Use key-based authentication, since password entry can't safely be automated'). rsync is the documented path for anything over 100 MB because it resumes. Read side has machine APIs: `/projects/<name>/best_release.json` (JSON with bytes/md5sum), `/projects/<name>/rss?path=/` (per-file size in `files:size`), and `downloads.sourceforge.net/project/...`.
- composes with: Each account can register unlimited projects ('you automatically are given administrator rights for that particular project'; the only gate is ODF-compliant OSS licensing + a one-time phone/SMS PIN). At the tolerated 20-30 GB/project that is 20-30 GB x N projects x N accounts. The real find is that the number is NEGOTIABLE and unpublished - 'If you are planning to do something which consumes huge amounts of disk, please ask first' - so the ceiling is a support ticket, not a wall. Two independent storage surfaces per project (FRS + project web htdocs), plus git/hg/svn repos, plus wiki/ticket attachments.
- reliability: The only fragile part is the soft quota: 20-30 GB 'may be permissible' means a project that grows to hundreds of GB gets an email, not a hard stop - enforcement is discretionary. SFTP is reachable and live (banner SSH-2.0-OpenSSH_7.4 on port 22). One structural caution: the FRS host deliberately does not list the project directory over SFTP ('your project directory is available, even if you cannot see it listed'), so clients must use absolute paths and cannot enumerate.
- notes: the same as the free tier
- evidence note: The absence of a fixed cap is stated on the page as re-read. Was reported; now documented.
- evidence:
  - [1] 2026-10-21: 'There are currently no fixed capacity limits around usage of our services... 5GB or less is ideal. 20-30GB may be permissible.'
  - [2] 2026-10-21: 'Individual files larger than 10 GB will not replicate out to our mirrors and can not be downloaded.'
  - [3] 2026-10-21: host frs.sourceforge.net, path /home/frs/project/PROJECT_UNIX_NAME/, key-based batch mode
  - [4] 2026-10-21: 'rsync over SSH is a supported file transfer method for our File management service'
  - withheld 2026-10-21: probe: TCP connect frs.sourceforge.net:22 -> 'SSH-2.0-OpenSSH_7.4' (SFTP endpoint live, anonymous banner)
  - [5] 2026-10-21: probe: GET -> 302 to zenlayer.dl.sourceforge.net/?viasf=1&fid=... then 200, Content-Length 1637343, downloaded and sha256 bdd1a33de78618d16ee4ce148b849932c05d0015491c34887846d431d29f308e
  - withheld 2026-10-21: probe: ranged GET bytes 0-1048575 on /project/clonezilla/.../clonezilla-live-20261018-resolute-amd64.iso -> 206, Content-Range: bytes 0-1048575/640679936 (a 640 MB object, ranges honoured, mirror path works)
  - [6] 2026-10-21: probe: GET -> JSON with bytes 1868068, md5sum, filename (machine-readable release metadata, anonymous)
  - [7] 2026-10-21: gate is 'all projects must be Open Source Software, with a license compliant with the Open Source Definition' plus a phone PIN; no editorial review step
  - [1] 2026-10-22: 200, 3,189 B on 2026-10-22: 'There are currently no fixed capacity limits around usage of our services'
- sources:
  - [1] https://sourceforge.net/p/forge/documentation/Disk%20Quotas/
  - [2] https://sourceforge.net/p/forge/documentation/Release%20Files%20for%20Download
  - [3] https://sourceforge.net/p/forge/documentation/SFTP/
  - [4] https://sourceforge.net/p/forge/documentation/rsync/
  - [5] https://downloads.sourceforge.net/project/sevenzip/7-Zip/24.09/7z2409-x64.exe
  - [6] https://sourceforge.net/projects/sevenzip/best_release.json
  - [7] https://sourceforge.net/p/forge/documentation/Create%20a%20New%20Project/

## SourceForge File Release System (FRS) — frs.sourceforge.net

- `storage/sourceforge-file-release-system-frs-sourceforge-net` | qualifies-with-caveat | evidence documented | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://sourceforge.net/p/forge/documentation/Release%20Files%20for%20Download/
- disagrees on identity_kind: `storage/sourceforge-file-release-system-frs-sourceforge-net` says institution, `storage/sourceforge-file-release-system-project-web-space` says any-phone
- disagrees on verdict: `storage/sourceforge-file-release-system-frs-sourceforge-net` says qualifies-with-caveat, `storage/sourceforge-file-release-system-project-web-space` says qualifies
- free tier: No fixed quota. SourceForge's own docs: 'There are currently no fixed capacity limits around usage of our services. In lieu of specific disk usage caps (quotas), we may contact projects if they are using significant storage.' Guidance: '5GB or less is ideal. 20-30GB may be permissible (limits may vary and be flexible depending on the situation)'. So ~20-30 GB per project as a practical band, with no hard number. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: SourceForge.net will not restore individual files', and releases persist indefinitely (OpenOffice's mirror alone carries 166.4 MB files from 2015) | source: [1] | note: not stated
- egress: Free and unmetered. Every release is 'automatically distributed to our worldwide network of download mirrors'. Downloads are served from per-mirror hostnames (zenlayer.dl / twds.dl / cfhcable.dl).sourceforge.net behind Cloudflare. Project Web states 'Unlimited bandwidth for Open Source projects' and 'Our project web servers frequently handle more than 50M hits per day'. | metered: no
- identity: institution
- interface: sftp, scp, rsync, rclone
- limits:
  - per-object-cap (binding): 10 GB per file [1]
- limits note: Per-object-cap: 10 GB per file. 'Individual files larger than 10 GB will not replicate out to our mirrors and can not be downloaded', so the only way past it is to shard. Request-rate: none published; upload is plain SFTP so it is limited by SSH session count, not an API quota. Retention: none. 'Users are responsible for backing up all of their files. SourceForge.net will not restore individual files', and releases persist indefinitely (OpenOffice's mirror alone carries 166.4 MB files from 2015). Reliability: signed mirror redirects are short-lived (see reliability_note).
- interface detail: sftp
- tooling: Native SFTP, SCP, and rsync protocols are supported with documentation on the file release system page. Integrates with rclone via its native SFTP backend, and connects directly to restic, borg, or rsync. TCP port 22 to frs.sourceforge.net is open.
- composes with: One account, many projects. Each project gets an independent tree at /home/frs/project/<unixname>/ and its own mirror distribution; one project admin can hold release-technician rights on many projects. Chained: (20-30 GB practical per project) x (N projects per account) x (N accounts). At 20 projects that is already 400-600 GB; the 10 GB/file mirror limit forces sharding, which is free because FRS is directory-based. Second chain: the same upload endpoint feeds project web space at /home/project-web/<unixname>/htdocs served as <unixname>.sourceforge.io, which is a separate quota-less static origin.
- reliability: Two real hazards found by probing. (1) The signed mirror URL from downloads.sourceforge.net 301s to a per-mirror host with an expiring token; You must re-resolve the redirect per session, or the mirror silently returns HTML. (2) There is no hard cap, which means the cap is discretionary — SourceForge mails 'over-quota' notices (the 2006 Inkscape notice shows a 100 MB soft quota on the shell/group dir) and can contact projects using 'significant storage'. Treat it as a soft ceiling that a human can raise or lower.
- notes: the same as the free tier
- evidence note: The page states the number in the record; the claim is documented, not measured.
- extras:
  - verified[0].url: https://sourceforge.net/p/forge/documentation/Disk%20Quotas/
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 3189
  - verified[0].sha256: 5e5877b1fd03b2c60d57741e1636a2a8ac1e848dfaab19f9f5a0a02f00054ea2
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [1] 2026-10-22: no fixed capacity limits, 10 GB per file soft. Re-read https://sourceforge.net/p/forge/documentation/Disk%20Quotas/: HTTP 200, 3189 bytes, sha256 5e5877b1fd03b2c6. Quoted: sourceforge.net/p/forge/documentation/Disk%20Quotas/feed.atom 'RSS') [Search](https://sourceforge.net/p/forge/documentation/search 'Search') # Service Quotas There are currently no fixed capacity limits around usage of our services. In lieu of specific disk usage caps (quotas), we may contact projects if they are using significant storage. Projects should: - Keep disk usage to a reasonable level: 5GB or less is ideal. 20-30GB may be permissible. (limits may
  - [1] 2026-10-21: 'There are currently no fixed capacity limits around usage of our services... 5GB or less is ideal. 20-30GB may be permissible'
  - [2] 2026-10-21: SFTP/SCP/rsync example commands; 'Individual files larger than 10 GB will not replicate out to our mirrors and can not be downloaded'
  - [3] 2026-10-21: probe: GET -> 302 -> zenlayer.dl.sourceforge.net -> 206 Partial Content, Content-Range: bytes 0-1023/1637343, body starts 4d5a 9000 ('MZ') — real PE bytes, not an error page
  - withheld 2026-10-21: probe: 32 parallel ranged GETs on Apache_OpenOffice_4.1.15 (4000000-byte ranges) -> 68,311,515 bytes in 4632 ms = 14.06 MB/s aggregate
  - withheld 2026-10-21: probe concurrency curve on the same file: N=4 -> 2.52 MB/s, N=8 -> 8.18 MB/s, N=16 -> 7.77 MB/s, N=32 -> 14.06 MB/s. Non-linear and still climbing at 32; the cap is per-connection, not per-IP.
  - withheld 2026-10-21: probe: TCP connect frs.sourceforge.net:22 -> open (SFTP/SCP/rsync upload path live); :873 (plain rsync) -> timeout, so use rsync-over-SSH
  - withheld 2026-10-21: probe: one 166.4 MB release listed on sourceforge.net/projects/openofficeorg.mirror/files/ (200) — large files really are hosted, not theoretical
- sources:
  - [1] https://sourceforge.net/p/forge/documentation/Disk%20Quotas/
  - [2] https://sourceforge.net/p/forge/documentation/Release%20Files%20for%20Download/
  - [3] https://downloads.sourceforge.net/project/sevenzip/7-Zip/24.09/7z2409-x64.exe

## SourceForge Project Web (<project>.sourceforge.io)

- `storage/sourceforge-project-web` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://sourceforge.net/p/forge/documentation/Project%20Web%20Services/
- free tier: No quota stated anywhere on the page. The docs grant each project a vhost and say nothing about a byte limit. Practically it is the same filesystem family as FRS (uploaded over the same SFTP), so expect the same discretionary 20-30 GB band. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Unlimited bandwidth for Open Source projects' (sourceforge.net/create). 'Our project web servers frequently handle more than 50M hits per day; we handle server scaling, caching, load balancing, and performance tuning.' Served through Cloudflare. | metered: no
- identity: email
- interface: sftp, scp, rsync
- limits note: Per-object-cap: none published (it is a web root, not an artefact store). Request-rate: none published. Retention: 'always-on' service, files persist while the project exists. Practical caveat: it is a web root. Directory indexes are not guaranteed, so you index your own paths.
- interface detail: sftp
- tooling: Same SFTP/SCP/rsync upload path as FRS but to /home/project-web/<unixname>/htdocs. Static files come back over plain HTTPS on <unixname>.sourceforge.io. No client, no API, just a web origin. Custom domains supported via the Custom VHOST service.
- composes with: A second independent quota-less origin per project, free once you already have the project. Because it is a static web origin rather than a download mirror, it is the natural Cloudflare-fronted serving layer for anything in FRS: serves as the hot/serving tier while FRS holds the archive. N projects -> N vhosts.
- reliability: Probed live: https://libreoffice.sourceforge.io/ -> 200 with 134,123 bytes of real HTML; https://gimp.sourceforge.io/ -> 403 (project redirects elsewhere). https://gparted.sourceforge.io/ -> 302 to the project's own domain. Expect some projects to 403/302 depending on their custom-VHOST config; a fresh project should serve its own root.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'each project is provided the PROJECT.sourceforge.io subdomain'; 'frequently handle more than 50M hits per day'; SFTP path /home/project-web/PROJECT/htdocs
  - [2] 2026-10-21: 'Unlimited bandwidth for Open Source projects'
  - [3] 2026-10-21: probe: GET -> 200, 134123 bytes, text/html
  - [4] 2026-10-21: probe: GET -> 302 Location: https://gparted.org/ ; GET https://gimp.sourceforge.io/ -> 403
- sources:
  - [1] https://sourceforge.net/p/forge/documentation/Project%20Web%20Services/
  - [2] https://sourceforge.net/create/
  - [3] https://libreoffice.sourceforge.io/
  - [4] https://gparted.sourceforge.io/
