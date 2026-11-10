# put.io

> put.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/put/ | JSON https://fshy.ajam.dev/api/v1/entity/put.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## put.io

- `storage/put-io` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T10:28:56.581Z (inherited) | stale on 2026-11-19
- url https://put.io/plan/trial/
- free tier: No permanent free tier. The entry offer is a one-day trial of every feature at $0.99 (a prepaid plan); paid plans start at $9.99/month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: Files are held while the plan is active. When a plan ends the account is deactivated: files are kept 15 more days (no download or streaming) and then deleted for good. | days: 15 | source: [1] | note: Deleted files go to Trash and stay there for 14 days by default; Trash can be disabled in Account > Settings > Storage.
- egress: Downloads from put.io to a device have a monthly bandwidth cap: 1 TB on the 100G plan and 3 TB on the 1T plan, after which speed drops to 1.5 MB/s until the month resets on the first. Uploads and transfers into put.io do not count. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: No free tier. The trial is $0.99 for 24 hours ('Try every put.io feature for a day for $0.99. Ends after 24 hours'). Does not clear even the trial bar for storage use.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier. The trial is $0.99 for 24 hours ('Try every put.io feature for a day for $0.99. Ends after 24 hours'). Does not clear even the trial bar for storage use.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free tier. The trial is $0.99 for 24 hours ('Try every put.io feature for a day for $0.99. Ends after 24 hours'). Does not clear even the trial bar for storage use.
  - [2] 2026-11-03: paid plans start at $9.99/month | capture: sha256:29dbe6cbf8a315d0d2945b30256311373ffb5dcbce4edf63e8ce742a51cc7f29 | quote: Plans from $9.99/month when you're sure.
  - [3] 2026-11-03: there is no permanent free tier; the entry offer is a $0.99 one-day trial | capture: sha256:00de0e8925d4baba8ce07eb975c8f71c7ab5f46ed02626bb2f0bf56d972397e0 | quote: No permanent free tier. The way in is the [$0.99 one-day trial](https://put.io/plan/trial).
  - [4] 2026-11-03: after a plan ends, files are kept 15 more days, with no download or streaming, then deleted | capture: sha256:66e30654c54c8138d4c71e013f16fc8286531d34771574b797258490651e673f | quote: After your account is deactivated, we keep your files for **15 more days **- but you won't be able to download or stream them during this period.
  - [5] 2026-11-03: Trash holds deleted files 14 days by default | capture: sha256:52b15fdd8e2614a1f0166684d52d46e3c9f205c6bb7057d44836370b1aea76ed | quote: Trash is the default place where your unwanted files go and stay for 14 days unless you decide to restore them or remove them completely before their due date.
  - [6] 2026-11-03: 100G plan: 1 TB of downloads a month, then 1.5 MB/s | capture: sha256:683b7ca3e20d2faf75813119d806251b05f69fa8abbc41a86a20611bfea69022 | quote: 100G plan: 1 TB of downloads per month. After that, speed drops to 1.5 MB/s.
  - [6] 2026-11-03: 1T plan: 3 TB of downloads a month, then 1.5 MB/s | capture: sha256:683b7ca3e20d2faf75813119d806251b05f69fa8abbc41a86a20611bfea69022 | quote: 1T plan: 3 TB of downloads per month. After that, speed drops to 1.5 MB/s.
  - [6] 2026-11-03: transfers into put.io are not counted against the cap | capture: sha256:683b7ca3e20d2faf75813119d806251b05f69fa8abbc41a86a20611bfea69022 | quote: Uploading or transferring files into put.io does not count toward this limit.
  - [4] 2026-11-04: files are kept 15 days after deactivation, with no download or streaming | capture: sha256:66e30654c54c8138d4c71e013f16fc8286531d34771574b797258490651e673f | quote: After your account is deactivated, we keep your files for **15 more days **- but you won't be able to download or stream them during this period.
  - [7] 2026-11-04: 100G plan downloads are capped at 1 TB a month, then 1.5 MB/s | capture: sha256:683b7ca3e20d2faf75813119d806251b05f69fa8abbc41a86a20611bfea69022 | quote: 100G plan: 1 TB of downloads per month. After that, speed drops to 1.5 MB/s.
  - [3] 2026-11-04: no permanent free tier; $0.99 one-day trial | capture: sha256:00de0e8925d4baba8ce07eb975c8f71c7ab5f46ed02626bb2f0bf56d972397e0 | quote: No permanent free tier. The way in is the [$0.99 one-day trial](https://put.io/plan/trial).
- sources:
  - [1] https://put.io/plan/trial/
  - [2] https://put.io/
  - [3] https://put.io/plans/
  - [4] https://help.put.io/en/articles/8006232-what-happens-if-my-account-gets-deactivated
  - [5] https://help.put.io/en/articles/964524-how-do-i-disable-trash
  - [6] http://help.put.io/en/articles/13376199-do-we-throttle
  - [7] https://help.put.io/en/articles/13376199-do-we-throttle
