# Pixeldrain

> pixeldrain.com | Storage; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pixeldrain/ | JSON https://fshy.ajam.dev/api/v1/entity/pixeldrain.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pixeldrain

- `storage/pixeldrain` | qualifies-with-caveat | evidence reported | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:38.525Z (live) | stale on 2026-12-04
- url https://pixeldrain.com
- disagrees on identity_kind: `storage/pixeldrain` says institution, `storage/pixeldrain-2` says email
- disagrees on verdict: `storage/pixeldrain` says qualifies-with-caveat, `storage/pixeldrain-2` says fails-quota
- free tier: Storage: No limit. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Max file size: 10 GB per file (free), 100 GB per file (pro) | source: [1] | note: not stated
- retention: Files expire 60 days after last download; a download only counts if >10% of the file was transferred in one request, and the timer only updates once per 24h | days: 60 | source: [1] | note: not stated
- egress: Free egress capped at 6 GB/day per IP address (sliding 24h window, IP-bound even when logged in); over the cap the speed drops to 1 MiB/s and max 3 concurrent downloads. Pro: 4 TB per 30 days. Prepaid: EUR 1/TB metered. So free egress is metered, not unusable. 6 GB/day x N IPs. | metered: no | price per TB: EUR 1/TB
- identity: institution
- interface: rest, rclone
- limits:
  - per-ip-shaping: 6 GB/day [1]
  - per-ip-shaping: 1 MiB/s [1]
  - retention-clamped (binding): expire 60 days [1]
- limits note: Free uploads require an API key (anonymous server-side PUT returned 401 authentication_required). 6 GB/day/IP download cap; 1 MiB/s throttle and 3 concurrent downloads after that. Files expire 60 days after last download; a download only counts if >10% of the file was transferred in one request, and the timer only updates once per 24h. Hotlinking not supported on free.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Full REST API at /api with HTTP Basic (api key as password). rclone has no official backend; the API is simple enough that wrappers abound (Atlas electron/downloads/hosts/pixeldrain.js). PUT https://pixeldrain.com/api/file/ with -u :APIKEY.
- composes with: API keys are free and per-account, but the real multiplier is IP: the 6 GB/day download cap is per IP, so egress scales with egress IPs (proxies/CF Workers) not accounts. Storage itself is 'No limit' on free, which is the interesting half.
- reliability: Operator states plainly that free-plan 'unlimited' is not for storage: 'If you are (ab)using pixeldrain for free storage, you should not be surprised when the rules change at some point and all your stuff suddenly disappears.' The 6 GB/day free cap and 10%-of-file rule make this a poor serving tier unless fronted by something that fans out across IPs.
- notes: Free plan: storage 'No limit' for regular uploads (2 TB limit only on the paid filesystem product). Pro: no limit, with a 100 GB per-file ceiling; Prepaid: EUR 4 per TB per month storage and EUR 1 per TB egress, and files expire after 60 days.
- evidence note: part of reliability
- evidence:
  - [1] 2026-10-21: pricing table: Free 'Storage: No limit'; 'Egress transfer limit - 6 GB per day ... linked to your IP address'; 'When the download limit is exceeded the download speed is reduced to 1 MiB/s. You can have at most three concurrent downloads'
  - [2] 2026-10-21: 'Files will be removed if they have not been accessed for 60 days ... This only happens when someone downloads more than 10% of the whole file in a single request'
  - [3] 2026-10-21: 'All methods which create, modify or delete a resource require an API key'; base URL /api, Basic auth
  - [4] 2026-10-21: probe: PUT (no key) -> 401 {"success":false,"value":"authentication_required"}
  - [5] 2026-11-11: the pricing table states the free storage, the per-file ceiling and both tiers | capture: sha256:8f9c457ed6ff2809e2aa3766ad2281fe96db9cc10c0b4404980ba4164bcd992d | quote: Storage ... free_feat ... No limit ... Max file size ... free_feat ... 10 GB ... per file ... pro_feat ... 100 GB ... per file
  - [5] 2026-11-11: the Max file size row states 10 GB per file on free and 100 GB per file on pro | capture: sha256:8f9c457ed6ff2809e2aa3766ad2281fe96db9cc10c0b4404980ba4164bcd992d | quote: Max file size ... free_feat ... 10 GB ... per file ... pro_feat ... 100 GB ... per file
  - [2] 2026-11-11: the about page warns that free storage is not durable because the rules can change and the files can disappear | capture: sha256:4f99f1455e61e3bc02d3c87e9dfd1688784e0379bbbe5292b112f773f367923d | quote: If you are (ab)using pixeldrain for free storage, you should not be surprised when the rules change at some point and all your stuff suddenly disappears.
  - [1] 2026-11-19: the pricing table still lists no storage limit for regular uploads and a 2 TB filesystem limit | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: Storage ... No limit ... No limit for regular uploads ... 2 TB limit for filesystem uploads ... €4 / TB / month
  - [1] 2026-11-19: the pricing table states the free and Pro storage terms and the EUR 4/TB/month prepaid storage price | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: Storage ... No limit ... No limit for regular uploads ... 2 TB limit for filesystem uploads ... €4 / TB / month
  - [1] 2026-11-19: the pricing table still states the 6 GB/day free egress cap and EUR 1/TB prepaid egress | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: Egress transfer limit ... 6 GB per day ... 4 TB per 30 days ... €1 per TB transferred
- sources:
  - [1] https://pixeldrain.com/
  - [2] https://pixeldrain.com/about
  - [3] https://pixeldrain.com/api
  - [4] https://pixeldrain.com/api/file/
  - [5] https://pixeldrain.com/res/svelte/home_page.js?v498422

## pixeldrain pro / prepaid

- `storage/pixeldrain-pro-prepaid` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:22:32.525Z (live) | stale on 2026-11-19
- url https://docs.pixeldrain.com/filesystem/
- free tier: None reachable: Prepaid storage is genuinely €4/TB/mo but egress is metered at €1/TB with NO free download allowance on the filesystem. 'Downloads from the filesystem are charged at €1 / TB for prepaid.' A. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Prepaid filesystem downloads are charged at EUR 1 per TB with no cap stated; Patreon plans have a monthly transfer limit instead; the free filesystem download limit is 6 GB per day. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: reported: the page read on 2026-11-03 is https://docs.pixeldrain.com/filesystem/, which states that the filesystem is open to accounts with a paid subscription (Patreon or Prepaid), that prepaid storage is charged at €4 per TB per month, that prepaid filesystem downloads are charged at €1 / TB (Patreon plans have a monthly limit), and that the filesystem allows up to 6 GB of downloads per day against 5 GB per day for regular files, with speed limited to 1 MiB/s beyond it. The page therefore states a daily download allowance, which free_tier.stated and reliability_note deny, so the rung stays reported.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Prepaid storage is genuinely €4/TB/mo but egress is metered at €1/TB with NO free download allowance on the filesystem — 'Downloads from the filesystem are charged at €1 / TB for prepaid.'…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Prepaid storage is genuinely €4/TB/mo but egress is metered at €1/TB with NO free download allowance on the filesystem — 'Downloads from the filesystem are charged at €1 / TB for prepaid.'…
  - [2] 2026-10-21: cited as the basis of the rejection: Prepaid storage is genuinely €4/TB/mo but egress is metered at €1/TB with NO free download allowance on the filesystem — 'Downloads from the filesystem are charged at €1 / TB for prepaid.' A
  - [1] 2026-11-03: prepaid filesystem egress is priced at EUR 1 per TB | capture: sha256:b0e35f3ff0dfc70d8954013e6399b4b3103f0c20a7e76ea6f54c94fb16f261c5 | quote: Downloads from the filesystem are charged at €1 / TB for prepaid.
  - [1] 2026-11-03: free filesystem download limit | capture: sha256:b0e35f3ff0dfc70d8954013e6399b4b3103f0c20a7e76ea6f54c94fb16f261c5 | quote: you can download up to 6 GB per day from the filesystem.
  - [1] 2026-11-03: prepaid storage price | capture: sha256:b0e35f3ff0dfc70d8954013e6399b4b3103f0c20a7e76ea6f54c94fb16f261c5 | quote: For Prepaid plans the storage is charged at €4 per TB per month.
  - [1] 2026-11-04: prepaid filesystem downloads are charged at EUR 1 per TB | capture: sha256:b0e35f3ff0dfc70d8954013e6399b4b3103f0c20a7e76ea6f54c94fb16f261c5 | quote: Downloads from the filesystem are charged at €1 / TB for prepaid.
- sources:
  - [1] https://docs.pixeldrain.com/filesystem/
  - [2] https://www.patreon.com/pixeldrain/join

## pixeldrain (as a transport-tier finding)

- `storage/pixeldrain-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.981Z (live) | stale on 2026-12-04
- url https://pixeldrain.com/
- disagrees on identity_kind: `storage/pixeldrain` says institution, `storage/pixeldrain-2` says email
- disagrees on verdict: `storage/pixeldrain` says qualifies-with-caveat, `storage/pixeldrain-2` says fails-quota
- free tier: none reachable: Re-checked because rclone has a native `pixeldrain` backend and the free tier says storage 'No limit'. But free egress is 6 GB/day per IP, files expire 60 days after last download… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: Re-checked because rclone has a native `pixeldrain` backend and the free tier says storage 'No limit'. But free egress is 6 GB/day per IP, files expire 60 days after last download…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Re-checked because rclone has a native `pixeldrain` backend and the free tier says storage 'No limit'. But free egress is 6 GB/day per IP, files expire 60 days after last download, hotlink
  - [2] 2026-10-21: cited as the basis of the rejection: Re-checked because rclone has a native `pixeldrain` backend and the free tier says storage 'No limit'. But free egress is 6 GB/day per IP, files expire 60 days after last download, hotlink
  - [1] 2026-11-19: free egress is capped at 6 GB per day | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: 6 GB per day
  - [1] 2026-11-19: free storage is stated as no limit | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: No limit
  - [1] 2026-11-19: free files expire 60 days after last download | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: 60 days (2 months)
  - [1] 2026-11-19: free file size cap is 10 GB per file | capture: sha256:f744b87fae35585f28ae0a96da73fe93a0352b9071ee9b24e91003c953ae6f47 | quote: 10 GB per file
- sources:
  - [1] https://pixeldrain.com/
  - [2] https://rclone.org/pixeldrain/

## ipfs / arweave / filecoin pinning as the hidden upstream

- `storage/ipfs-arweave-filecoin-pinning-as-the-hidden-upstream` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:13.424Z (live) | stale on 2026-12-04
- url https://pixeldrain.com/hosting
- free tier: none: No evidence of a hidden pinning upstream at any of the seven, and free pinning is <=6 GB or dead. pixeldrain's one decentralised dependency is Sia, not IPFS, and it is a cost-control measure. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: No evidence of a hidden pinning upstream at any of the seven, and free pinning is <=6 GB or dead. pixeldrain's one decentralised dependency is Sia, not IPFS, and it is a cost-control measure.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No evidence of a hidden pinning upstream at any of the seven, and free pinning is <=6 GB or dead. pixeldrain's one decentralised dependency is Sia, not IPFS, and it is a cost-control measure.
  - [1] 2026-11-19: the decentralised dependency is Sia, not IPFS/Arweave/Filecoin, confirming the rejection | capture: sha256:dfde89c40bab31b49fbe7ad0f089f5d8f7d216dbe9867c59319df2b7c02c556e | quote: Pixeldrain uses [Sia](https://sia.tech/) to offload files which are not requested often, but still need to be kept.
- sources:
  - [1] https://pixeldrain.com/hosting

## pixeldrain.com

- `storage/pixeldrain-com` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:05.887Z (live) | stale on 2026-12-04
- url https://pixeldrain.com/api/file/probe.bin
- free tier: none reachable: Anonymous uploading is not supported; all methods that create, modify or delete a resource require an API key. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Anonymous uploading is not supported; every create, modify or delete method requires an API key.
- notes: Anonymous uploads are gone: PUT /api/file/{name} returns HTTP 401 authentication_required ('Please provide an API key in the password field of HTTP Basic Access Authentication'). The file…
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Anonymous uploads are gone: PUT /api/file/{name} returns HTTP 401 authentication_required ('Please provide an API key in the password field of HTTP Basic Access Authentication'). The file…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Anonymous uploads are gone: PUT /api/file/{name} returns HTTP 401 authentication_required ('Please provide an API key in the password field of HTTP Basic Access Authentication'). The file…
  - [2] 2026-11-19: the current first-party API reference still requires an API key for every write method | capture: sha256:8edb904edaf44b0e9e93b87ac91cc4a38d8017f1d71e607c2c5c09c155939b94 | quote: All methods which create, modify or delete a resource require an API key.
  - [2] 2026-11-19: the live API reference still rules out anonymous uploads | capture: sha256:8edb904edaf44b0e9e93b87ac91cc4a38d8017f1d71e607c2c5c09c155939b94 | quote: This API requires authentication with an API key. Anonymous uploading is not supported.
  - [2] 2026-11-19: pixeldrain still gates programmatic uploads behind an API key | capture: sha256:8edb904edaf44b0e9e93b87ac91cc4a38d8017f1d71e607c2c5c09c155939b94 | quote: This API requires authentication with an API key. Anonymous uploading is not supported.
- sources:
  - [1] https://pixeldrain.com/api/file/probe.bin
  - [2] https://pixeldrain.com/api
