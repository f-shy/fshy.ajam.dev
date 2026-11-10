# CTAN

> ctan.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ctan/ | JSON https://fshy.ajam.dev/api/v1/entity/ctan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ctan

- `storage/ctan-2` | fails-quota | evidence documented | binding write-gated | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:34:58.622Z (live) | stale on 2026-12-04
- url https://www.ctan.org/upload
- disagrees on identity_kind: `storage/ctan` says institution, `storage/ctan-2` says email
- free tier: Uploads are write-gated: every upload is unpacked and checked by an upload manager before installation, and the archive holds material around TeX; no upload price is stated on the pages… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: no archive size limit is stated on the pages read; the upload is a single .zip, .tgz or .tar.gz archive | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: an email address of the uploader is required on the upload form; it is not published and is used to contact the uploader
- interface: rest
- limits:
  - write-gated (binding): every upload is unpacked and checked by an upload manager (volunteers); TeX packages as a .zip, .tgz or .tar.gz archive [2]
- binding note: writes pass a manual review by volunteer upload managers; the API submits into the same review workflow
- interface detail: not documented
- tooling: documented HTTP upload interface (POST /submit/validate and POST /submit/upload) in addition to the web form; the upload is passed to the CTAN upload workflow for review
- composes with: not recorded
- reliability: Every upload is unpacked and checked by an upload manager; the team are volunteers, so processing time varies
- notes: the same as reliability
- evidence note: the vendor pages of the 2026-11-03 evidence rows were read and captured (https://www.ctan.org/file/help/ctan/CTAN-upload-addendum, https://www.ctan.org/help/submit, https://www.ctan.org/upload, https://www.ctan.org/); every field that decides the verdict cites one of those captures
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: Web-form upload with manual editorial review; no API, no programmatic path regardless of size.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Web-form upload with manual editorial review; no API, no programmatic path regardless of size.
  - [2] 2026-11-03: each upload passes a manual check | capture: sha256:4c6e24a08eba87733e1d3ada6d31dca442d2448fd81535910e04edf7ae250bec | quote: Every upload will be unpacked and checked by an upload manager.
  - [2] 2026-11-03: upload management is done by volunteers | capture: sha256:4c6e24a08eba87733e1d3ada6d31dca442d2448fd81535910e04edf7ae250bec | quote: All these people are acting as volunteers in their spare time
  - [3] 2026-11-03: a programmatic upload API exists | capture: sha256:08d2953c7a4208bfe2c0e3f2887bbe3dc755b8f6388203f4dffa0e5730e7e79a | quote: CTAN provides an interface to programmatically upload submissions.
  - [1] 2026-11-03: the upload is a single archive of a fixed set of types | capture: sha256:999f31bb896c01a405056f6c34bf9d1c04a56b11c0d43a3125276b0908aaeb19 | quote: We only accept a single archive file for upload: the file name must end in .zip, .tgz, or .tar.gz.
  - [1] 2026-11-03: the form asks for an email address that is not published | capture: sha256:999f31bb896c01a405056f6c34bf9d1c04a56b11c0d43a3125276b0908aaeb19 | quote: Your email | This email address will not be published. It is meant for contacting you in case of questions.
  - [2] 2026-11-03: each upload is manually unpacked and checked before installation | capture: sha256:4c6e24a08eba87733e1d3ada6d31dca442d2448fd81535910e04edf7ae250bec | quote: Every upload will be unpacked and checked by an upload manager.
  - [4] 2026-11-03: the archive scope is material around TeX, not packages only | capture: sha256:2d6b568996e7a5b7700a700276e9b53cb36fcbaa83fd373e5053b3a75c0b05fe | quote: The Comprehensive TeX Archive Network (CTAN) is the central place for all kinds of material around TeX.
  - [2] 2026-11-03: the write gate is unchanged | capture: sha256:4c6e24a08eba87733e1d3ada6d31dca442d2448fd81535910e04edf7ae250bec | quote: Every upload will be unpacked and checked by an upload manager.
- sources:
  - [1] https://www.ctan.org/upload
  - [2] https://www.ctan.org/file/help/ctan/CTAN-upload-addendum
  - [3] https://www.ctan.org/help/submit
  - [4] https://www.ctan.org/

## CTAN (Comprehensive TeX Archive Network)

- `storage/ctan` | fails-quota | evidence reported | binding write-gated | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ctan.org
- disagrees on identity_kind: `storage/ctan` says institution, `storage/ctan-2` says email
- free tier: No numeric quota published, but upload is a manual web form reviewed by the CTAN team, with extensive packaging rules (TDS layout, no .git, no editor backups, symlinks preferred over copies). There is no API and no programmatic publish path. A real package (beamer.zip) is 3,298,392 bytes. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: per-object-cap: none published; upload is a browser form. retention: indefinite ('CTAN keeps all versions') | source: [1] | note: not stated
- egress: Free, heavily mirrored (mirror.ctan.org redirects to a national mirror, e.g. mirrors.ustc.edu.cn). No metering. | metered: no
- identity: institution
- interface: rclone
- limits:
  - write-gated (binding): reviewed by the CTAN team, with extensive packaging rules (TDS layout, no [1]
  - write-gated (binding): review [1]
- limits note: per-object-cap: none published; upload is a browser form. retention: indefinite ('CTAN keeps all versions'). request-rate: N/A, human review.
- interface detail: wrapper-only
- tooling: Manual upload form + email-based review. `tlmgr` for consumption. No upload API, no rclone.
- composes with: unlimited packages x unlimited versions, but every one is human-reviewed and must be TeX-archive-shaped. Not multiplicable in any meaningful automated way.
- reliability: Write access requires web form submission with editorial review, lacking programmatic upload endpoints. Read access is supported via global HTTP mirror networks.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: No numeric quota published, but upload is a manual web form reviewed by the CTAN team, with extensive packaging rules (TDS layout, no .git, no editor backups, symlinks preferred over copies). There is no API and no programmatic publish path. A real package (beamer.zip) is 3,298,392 bytes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET with -L -> 200, 3,298,392 bytes, final URL mirrors.ustc.edu.cn/CTAN/...
  - [1] 2026-10-21: upload form, no API
  - [3] 2026-10-21: 'Never try to upload (or re-upload) by email, always use the upload form'
- sources:
  - [1] https://www.ctan.org/upload
  - [2] https://mirror.ctan.org/macros/latex/contrib/beamer.zip
  - [3] https://www.ctan.org/file/help/ctan/CTAN-upload-addendum
