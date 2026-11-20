# gnu savannah as an sftp target

> defectivebydesign.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/defectivebydesign/ | JSON https://fshy.ajam.dev/api/v1/entity/defectivebydesign.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gnu savannah as an sftp target

- `storage/gnu-savannah-as-an-sftp-target` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:41.638Z (live) | stale on 2026-12-04
- url https://lists.defectivebydesign.org/archive/html/savannah-announce/2023-11/msg00000.html
- free tier: none reachable: The transport everybody assumes works does not: SFTP was disabled outright in 2023-11 after a vulnerability, and scp only works with `-O` (legacy protocol) on OpenSSH >= 9.0. A modern… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The transport everybody assumes works does not: SFTP was disabled outright in 2023-11 after a vulnerability, and scp only works with `-O` (legacy protocol) on OpenSSH >= 9.0. A modern…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The transport everybody assumes works does not: SFTP was disabled outright in 2023-11 after a vulnerability, and scp only works with `-O` (legacy protocol) on OpenSSH >= 9.0. A modern…
  - [2] 2026-10-21: cited as the basis of the rejection: The transport everybody assumes works does not: SFTP was disabled outright in 2023-11 after a vulnerability, and scp only works with `-O` (legacy protocol) on OpenSSH >= 9.0. A modern client
  - [2] 2026-11-19: SFTP is disabled on Savannah and only legacy scp -O works, so the assumed SFTP transport is unavailable | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: Starting with OpenSSH 9.0, scp uses the SFTP protocol by default. As of 2025-01, SFTP is disabled on Savannah. Please add the -O option to scp command line if you use OpenSSH 9.0 or later:
  - [2] 2026-11-19: uploads require a registered SSH public key tied to a Savannah account | capture: sha256:9a8a33b68bcfdf5f226d0ea2b6b6e087c97a82c54c7f34fc4517d351784ba378 | quote: The authentication method to use with scp is SSH public key (one of those that you registered in your Savannah account).
- sources:
  - [1] https://lists.defectivebydesign.org/archive/html/savannah-announce/2023-11/msg00000.html
  - [2] https://savannah.gnu.org/maintenance/DownloadArea/
