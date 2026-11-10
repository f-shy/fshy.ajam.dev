# ASUS WebStorage

> asuswebstorage.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/asuswebstorage/ | JSON https://fshy.ajam.dev/api/v1/entity/asuswebstorage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ASUS WebStorage

- `netdisk-pan/asus-webstorage` | fails-quota | evidence reported | binding per-object-cap | category hardware-vendor cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:56.366Z (inherited) | stale on 2026-11-19
- url https://www.asuswebstorage.com/
- free tier: 5 GB on the plan listed as Free Trial, priced 'Lifetime Free'; paid Lite 100 GB, Pro 1 TB, Enterprise 5 TB | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [1]
- retention: Not published | source: [2]
- egress: Not published; FTP is offered on paid tiers with a bandwidth limit | metered: no | source: [1]
- identity: email | detail: an email address
- interface: unknown
- limits:
  - request-rate: API calls are a paid-tier entitlement: 10 million a month on Pro, 50 million on Enterprise [1]
  - per-object-cap (binding): 5 GB is the free tier total, which is the cap in practice [1]
- binding note: 5 GB free, and the API is metered by a paid-tier entitlement, so there is no free programmatic path at any capacity.
- tooling: reverse-engineered. A draft rclone backend, pull request 6808, whose description states 'API is not publicly available. Protocol and API were discovered with official Linux client.', was opened 2023-03-06 and closed unmerged on 2026-02-26; it is in no release
- composes with: Had the rclone backend landed this would be a clean one-line remote. It did not: the pull request was closed unmerged on 2026-02-26, and rclone's maintainer required someone to commit to maintaining a backend whose API is not public
- reliability: The draft rclone backend was closed unmerged on 2026-02-26 and the API is not public. Do not plan on it
- notes: Both a quota failure and a tooling failure, recorded as fails-quota because the quota is the first thing a reader checks. The API being a paid-tier entitlement is the part that would surprise a reader who assumed the draft rclone backend implied free access.
- extras:
  - access_mode: registration-gated
  - rclone_backend: PR 6808, closed unmerged on 2026-02-26, not in any release
  - api_included_free: no
- evidence:
  - [1] 2026-10-21: plan table Free Trial 5 GB, Lite 100 GB, Pro 1 TB, Enterprise 5 TB, and 'API Function: Pro 10 million per month'
  - [3] 2026-10-21: 'API is not publicly available. Protocol and API were discovered with official Linux client', state Draft since 2023-03-06
  - probe:https://www.asuswebstorage.com/navigate/price/ 2026-10-21: HTTP 404 with a 774-byte body, so that path is dead and the live price page is service.asuswebstorage.com/store/
  - [1] 2026-11-03: the Free Trial column is priced Lifetime Free; its storage row is 5GB | capture: sha256:0cb2ecfe6ef114ac6b32d8747a5f0958baeefdc71920c188209d0803535bb869 | quote: | Price/Year | Lifetime Free | -- | -- | -- |
  - [3] 2026-11-03: the rclone maintainer closed the pull request on 2026-02-26 | capture: sha256:a16b294e58891192480d91ea9d204b69745721f5341e48ec4f6944629ef0c5bf | quote: I'm going to close this now - feel free to submit again if you have more time to work on it.
  - [3] 2026-11-03: rclone's condition for merging a backend with no public API | capture: sha256:a16b294e58891192480d91ea9d204b69745721f5341e48ec4f6944629ef0c5bf | quote: I've decided that in order to merge a backend with no public API I need to get someone else to maintain it indefinitely.
  - [4] 2026-11-03: the first-party service page offers 5 GB free for an account number, password and email address | capture: sha256:345deed73c2db43df9e450356caf0d39f2bf416bd0c89e4540554348c77aee63 | quote: please go to ASUS WebStorage website to apply for 5GB free storage. In turn, please set your personal account number, password and email address to formally start the
  - [1] 2026-11-03: API calls are a Pro and Enterprise entitlement, 10 million and 50 million per month | capture: sha256:0cb2ecfe6ef114ac6b32d8747a5f0958baeefdc71920c188209d0803535bb869 | quote: | API Function | | | ● (10 million per month) | ● (50 million per month) |
  - [1] 2026-11-03: plan storage: Free Trial 5GB, Lite 100GB, Pro 1TB, Enterprise 5TB | capture: sha256:0cb2ecfe6ef114ac6b32d8747a5f0958baeefdc71920c188209d0803535bb869 | quote: | Cloud Storage | 5GB | 100GB | 1TB | 5TB |
  - probe:https://www.asuswebstorage.com/navigate/price/ 2026-11-03: the old price path still answers HTTP 404 with a 774-byte body | capture: sha256:bebc4154eb8c63b69f50ad584e36a71facfc51c07810c611710738d63bd1b1dc | quote: "status": 404
- sources:
  - [1] https://service.asuswebstorage.com/store/?bp=_t
  - [2] https://www.asuswebstorage.com/
  - [3] https://github.com/rclone/rclone/pull/6808
  - [4] https://service.asuswebstorage.com/service/
