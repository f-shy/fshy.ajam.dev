# DeepStorage

> deepstorage.dev | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deepstorage/ | JSON https://fshy.ajam.dev/api/v1/entity/deepstorage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DeepStorage (deepstorage.dev)

- `storage/deepstorage` | fails-quota | evidence documented | binding volume-quota | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:11.231Z (live) | stale on 2026-12-05
- url https://deepstorage.dev
- free tier: Free: 2 TB of storage and 50 GB of new uploads a month. Community (free while in their Telegram channel): unlimited storage and 200 GB of new uploads a month. Paid plans start at $9 a month and add the API. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file size limit for uploads from the browser, saves from a link, torrents or cloud imports; imports from video sites stop at 2 GB a video and files sent through the Telegram bot are limited by Telegram. | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress fee on any plan: 'Browsing, streaming, sharing and downloading never cost credits on any plan.' No bandwidth meter is documented. | metered: no
- identity: email | detail: Sign up with Google, GitHub or an e-mail address; no credit card is needed. Unlimited storage also needs a linked Telegram account and membership of the Telegram channel.
- interface: rest
- limits:
  - volume-quota (binding): new uploads: 50 GB a month on Free and 200 GB a month on Community; Community storage is unlimited only while the account is in the Telegram channel, otherwise the cap is 2 TB [1]
- limits note: Free: 2 TB, 50 GB of uploads a month, 1 upload at a time, 100 files per torrent. Community: unlimited storage, 200 GB of uploads a month, 1 upload at a time, 500 files per torrent. Credits: 50 to start, plus 200 once for linking Telegram and joining the channel; torrent add 2, cloud import 1, zip extract 2, copy 10. Leaving the channel returns the account to Free; nothing is deleted and new uploads stop while the account holds more than 2 TB.
- binding note: new-upload volume is capped at 200 GB a month on Community (50 GB on Free), so filling a large archive takes years even though stored bytes are unlimited
- interface detail: rest
- tooling: No API on Free or Community ('API No' in the plan table). Pro is $9 a month ($90 for 12 months) with unlimited storage, 2 TB of uploads a month and the API; Max is $50 a month ($500 for 12 months) with unlimited storage and unlimited monthly uploads. Bulk paths on Free are torrent import and URL or cloud-drive import, both credit-metered.
- composes with: Community tier provides unlimited cumulative storage with a limit of 200 GB of new uploads per month after joining the vendor Telegram channel.
- reliability: The unlimited tier lasts only while the account is in the Telegram channel; leaving returns it to Free (2 TB) and new uploads stop while the account holds more than 2 TB, with nothing deleted. At 200 GB of new uploads a month, 20 TiB needs about 110 months. The API is not on Free or Community. A POST to /createAcc answered HTTP 400 'Verification required. Please verify your identity first.' on 2026-10-21.
- notes: Free: 2 TB. Community (join their Telegram channel): storage becomes 'Unlimited, while you are in the channel'. Both have no per-file size limit.
- evidence note: https://deepstorage.dev/pricing and https://deepstorage.dev/, re-read on 2026-11-03, state the Free row (2 TB, 50 GB of monthly uploads), the Community row (unlimited while in the channel, 200 GB of monthly uploads), that leaving the channel returns the account to Free, and sign-up by Google, GitHub or e-mail with no card.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 2 TB. Community (join their Telegram channel): storage becomes 'Unlimited, while you are in the channel'. Both have no per-file size limit.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: table row 'Community | $0 | Unlimited, while you are in the channel | 200 GB | API No'
  - [2] 2026-10-21: 'Every account starts with 2 TB, and linking your Telegram account and joining our channel makes storage unlimited, free. ... there is no per-file limit'
  - [3] 2026-10-21: probe: POST -> 400 text/plain 'Verification required. Please verify your identity first.' (aiohttp origin)
  - [1] 2026-11-03: the Community row lists unlimited storage while in the channel and 200 GB of monthly uploads | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: Unlimited, while you are in the channel | 200 GB | 1 | 500 | 1 | No | 200 to start
  - [1] 2026-11-03: the Free row lists 2 TB of storage, 50 GB of monthly uploads and no API | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: $0 | $0 | 2 TB | 50 GB | 1 | 100 | 1 | No | 50 to start
  - [2] 2026-11-03: the site states no file size limit for browser, link, torrent and cloud imports | capture: sha256:1a3541ded33375e3edb98f08f69fb94b84c2dff816105134533f0fcaa45b6cb8 | quote: Not for uploads from your browser, saves from a link, torrents or cloud imports.
  - [1] 2026-11-03: Community lists 200 GB of monthly uploads | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: Unlimited, while you are in the channel | 200 GB | 1 | 500 | 1 | No | 200 to start
  - [1] 2026-11-03: leaving the channel returns the account to Free | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: We re-check membership, and if you leave, the account returns to Free.
  - [1] 2026-11-03: the plan table lists the monthly uploads, uploads at once, files per torrent and starting credits | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: Unlimited, while you are in the channel | 200 GB | 1 | 500 | 1 | No | 200 to start
  - [1] 2026-11-03: new uploads are capped at 200 GB a month on Community | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: Unlimited, while you are in the channel | 200 GB | 1 | 500 | 1 | No | 200 to start
  - [1] 2026-11-03: membership of the channel is re-checked and leaving returns the account to Free | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: We re-check membership, and if you leave, the account returns to Free.
  - [1] 2026-11-03: the Pro row lists $9 a month, $90 for 12 months, unlimited storage, 2 TB of monthly uploads and the API | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: | Pro | $9 | $90 | Unlimited | 2 TB | 3 | 5,000 | 3 | Yes | Unlimited |
  - [1] 2026-11-03: the Max row lists $50 a month, unlimited storage and unlimited monthly uploads | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: | Max | $50 | $500 | Unlimited | Unlimited | 6 | 20,000 | 3 | Yes | Unlimited |
  - [2] 2026-11-03: the site states sign-up by Google, GitHub or e-mail with no credit card | capture: sha256:1a3541ded33375e3edb98f08f69fb94b84c2dff816105134533f0fcaa45b6cb8 | quote: Sign up with Google, GitHub or your email. No credit card and no trial: your account is ready in seconds.
  - [1] 2026-11-03: the plan table still lists Free 2 TB and Community unlimited storage | capture: sha256:470033ea96907a84a8b0441d6d71a50cd361fbbe7813b7083745d352e57df66d | quote: Unlimited, while you are in the channel | 200 GB | 1 | 500 | 1 | No | 200 to start
  - [1] 2026-11-04: the Free row lists 2 TB of storage, 50 GB of monthly uploads and no API | capture: sha256:a82eb0cafe9cc895f87fd39dca83fd218d250a8a608fd1ab413a53bcb4d95669 | quote: | FreeWhere every account starts. | $0 | $0 | 2 TB | 50 GB | 1 | 100 | 1 | No | 50 to start | [Create an account](https://deepstorage.dev/browse-files) |
  - [1] 2026-11-04: the Community row lists unlimited storage while in the channel and 200 GB of monthly uploads | capture: sha256:a82eb0cafe9cc895f87fd39dca83fd218d250a8a608fd1ab413a53bcb4d95669 | quote: | CommunityFree while you are in our Telegram channel. | $0 | $0 | Unlimited, while you are in the channel | 200 GB | 1 | 500 | 1 | No | 200 to start | [Link Telegram](https://deepstorage.dev/browse-files) |
  - [1] 2026-11-04: leaving the channel returns the account to Free | capture: sha256:a82eb0cafe9cc895f87fd39dca83fd218d250a8a608fd1ab413a53bcb4d95669 | quote: We re-check membership, and if you leave, the account returns to Free.
  - [2] 2026-11-04: sign-up by Google, GitHub or e-mail with no credit card | capture: sha256:1a3541ded33375e3edb98f08f69fb94b84c2dff816105134533f0fcaa45b6cb8 | quote: Sign up with Google, GitHub or your email. No credit card and no trial: your account is ready in seconds.
- sources:
  - [1] https://deepstorage.dev/pricing
  - [2] https://deepstorage.dev/
  - [3] https://deepstorage.dev/createAcc
