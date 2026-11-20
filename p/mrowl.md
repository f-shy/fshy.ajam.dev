# MrOwl

> mrowl.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mrowl/ | JSON https://fshy.ajam.dev/api/v1/entity/mrowl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MrOwl (mrowl.com)

- `storage/mrowl` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:01.149Z (live) | stale on 2026-12-04
- url https://www.mrowl.com
- free tier: 'Free unlimited storage for content that is shared to the world' plus 10GB of private storage; 'Free unlimited files stored in public branches up to 20MB per file.' | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20MB per file | bytes: 20000000 | source: [1] | note: not stated
- retention: 'free unlimited storage for content that is shared to the world' + 10 GB private. The asterisk is the whole story: 'Free unlimited files stored in public branches up to 20MB per file' | source: [1] | note: not stated
- egress: No egress meter documented. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 20MB per file [1]
- limits note: per-object-cap 20 MB on the unlimited public tier; anything over 20 MB draws down the 10 GB private quota instead.
- interface detail: rest
- tooling: Web + iOS/Android app. No API, no rclone backend. The only path to the unlimited pool is publishing into a public 'branch'.
- composes with: Unlimited public bytes x N accounts, but 20 MB per file. A 20 TiB corpus would be 1,000,000 objects, which is a metadata problem before it is a storage problem.
- reliability: Front page returned HTTP 504 gateway timeout during testing. Archived help documentation specifies a 20 MB file limit footnote.
- notes: 'free unlimited storage for content that is shared to the world' + 10 GB private. The asterisk is the whole story: 'Free unlimited files stored in public branches up to 20MB per file'.
- evidence:
  - [2] 2026-10-21: > capture 20260109172404: 'Free unlimited files stored in public branches up to 20MB per file. Plus, 10GB of free private storage.'
  - [3] 2026-10-21: probe: GET direct -> connection timed out, 0 bytes; via reader -> 504
  - [4] 2026-10-21: (search snippet) — 'free tier with up to 10GB of private storage and free unlimited storage for content that is sha[red]'
  - [1] 2026-11-11: the help page states 10GB of private storage, unlimited public storage and a 20MB per-file cap | capture: sha256:2624301799420651d868537e7a16d31182d81123b94789abc05e3c57adf45ee0 | quote: MrOwl offers a free tier with up to 10GB of private storage and free unlimited storage for content that is shared to the world ... *Free unlimited files stored in public branches up to 20MB per file.
  - [1] 2026-11-19: the help page states 10 GB private and unlimited public storage | capture: sha256:8d2a52d8933f2a1c4bae017ce1be82ad8abde2860e23e9de89d7e43933f76011 | quote: MrOwl offers a free tier with up to 10GB of private storage and free unlimited storage for content that is shared to the world.*
  - [1] 2026-11-19: the help page states a 20 MB per-file cap on public branches | capture: sha256:8d2a52d8933f2a1c4bae017ce1be82ad8abde2860e23e9de89d7e43933f76011 | quote: Free unlimited files stored in public branches up to 20MB per file. See terms for full details.
  - [1] 2026-11-19: registration requires a cell phone number | capture: sha256:8d2a52d8933f2a1c4bae017ce1be82ad8abde2860e23e9de89d7e43933f76011 | quote: When you register, you will need to provide your cell phone number in order to validate your account which will be texted to you.
  - probe:https://www.mrowl.com/ 2026-11-19: the site root answered HTTP 200 with real bytes | capture: sha256:35338c3c535603466a5e8c084a41636a72b9cdd2f613df5bbf539c433292b61c | quote: "status": 200
- sources:
  - [1] https://www.mrowl.com/help.jsp
  - [2] https://web.archive.org/web/202601/mrowl.com/help.jsp
  - [3] https://mrowl.com/
  - [4] https://www.mrowl.com/settings.jsp
