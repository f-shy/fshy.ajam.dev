# Puffbin

> puffbin.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/puffbin/ | JSON https://fshy.ajam.dev/api/v1/entity/puffbin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Puffbin

- `debrid/puffbin-com` | qualifies-with-caveat | evidence documented | binding pull-count | category anonymous file host with password and burn-after-reading | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:36.943Z (live) | stale on 2026-12-04
- url https://puffbin.com/
- price USD 0
- free tier: Upload files up to 10GB each. Password protect, burn after reading, or just share. No account needed. | unit: GB | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Upload files up to 10GB each | bytes: 10000000000 | source: [1]
- retention: The uploader chooses how long a file exists, and when the timer runs out the file is permanently deleted; there is no early delete, only the chosen timer. unverified: the selectable timer values and their maximum are not listed on the page. | source: [1] | note: Burn-after-read is a pull-count of one, not a retention period.
- egress: No byte allowance stated; a burn-after-reading option makes the first read the last. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'No account needed' on the page and the FAQ says no registration or personal details are required; request IP addresses are logged temporarily to prevent abuse. No upload was attempted.
- interface: unknown
- limits:
  - per-object-cap: 10 GB per file [1]
  - pull-count (binding): 1 when burn-after-reading is set [1]
- limits note: Retention is a timer the uploader selects at upload, and early deletion is not offered; the selectable timer values and any rate limit are not published. Whether a datacenter address is accepted: not published.
- binding note: With burn-after-reading a link is spent on the first read and with 10 GB objects 1 TiB of monthly transfer is 100 transfers; the pull count breaks before the size does.
- interface detail: Browser drop zone. /api/upload returned 400 (a validation answer) so a JSON endpoint answers, but no contract is published.
- tooling: Browser only as observed; the 400 on /api/upload is the opening for a wrapper.
- composes with: Burn-after-read is the right primitive for handing a credential or a one-shot dataset to a reader without leaving a copy; it is the opposite of an archive.
- reliability: A single-screen drop zone with an FAQ; no rate limit, maximum timer or datacenter-address policy is published, and request IP addresses are logged temporarily to prevent abuse.
- notes: Named for the burn-after-read primitive; the number that matters (retention) is still missing.
- evidence note: The offer sentence and the FAQ are quoted from the vendor page. Retention is a timer chosen at upload whose selectable values are not published, and the upload path contract is not published; no upload was attempted.
- extras:
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload
- evidence:
  - [1] 2026-10-23: 'Upload files up to 10GB each', 'Password protect, burn after reading, or just share', 'No account needed'
  - probe:https://puffbin.com/api/upload 2026-10-23: HTTP 400 from /api/upload, 404 from /upload, /api/files, /v1/upload
  - [1] 2026-11-03: the uploader picks a lifetime and the file is permanently deleted when the timer ends | capture: sha256:f74749c935c3e1fba8ebf2866d9b7fe7aafab7234f0ce9845527cbb2e396b806 | quote: Simply drag and drop your file, choose how long you want it to exist, and get a secure link. Once the timer runs out, the file is permanently deleted from our servers.
  - [1] 2026-11-03: no registration or personal details; request IP addresses are logged temporarily | capture: sha256:f74749c935c3e1fba8ebf2866d9b7fe7aafab7234f0ce9845527cbb2e396b806 | quote: Yes. We do not require any registration or personal details. We do log basic request information (like IP addresses) temporarily to prevent abuse.
  - [1] 2026-11-03: no early deletion; expiry is by the chosen timer only | capture: sha256:f74749c935c3e1fba8ebf2866d9b7fe7aafab7234f0ce9845527cbb2e396b806 | quote: Currently, files only expire automatically based on the time you selected.
  - [1] 2026-11-03: 10 GB per file, no account, password and burn-after-reading options | capture: sha256:33164bf1d394f2b578f03e643fd1f2e41da7ca4d45c1a80dfd38d95cb1fac0e6 | quote: Upload files up to 10GB each. Password protect, burn after reading, or just share. No account needed.
- sources:
  - [1] https://puffbin.com/
