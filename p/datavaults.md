# Data Vaults

> datavaults.co | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datavaults/ | JSON https://fshy.ajam.dev/api/v1/entity/datavaults.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Data Vaults

- `debrid/data-vaults` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (freemium, XFileSharing script) | tier registered
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://datavaults.co/premium/
- price USD 10.99 per 30 days for 2000 GB of storage and unlimited download volume | parsed USD 5.5/TB-mo
- free tier: Registered, $0.00: max upload file size 5 GB, storage space 15 GB, download volume 100 GB, files deleted after 7 days. Anonymous, $0.00: 1 GB upload, 1 GB storage, 15 GB download volume, deleted after 3 days. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The page prints the download volume without a period.
- per-object cap: Registered 5 GB; Anonymous 1 GB; Premium 100 GB; Premium PRO Unlimited. | bytes: 5368709120 | source: [1] | note: bytes = 5 x 1024^3 for the registered free tier.
- retention: Registered files are deleted after 7 days; anonymous after 3 days; premium never. | days: 7 | source: [1]
- egress: Download volume: 15 GB anonymous, 100 GB registered, Unlimited on Premium and Premium PRO. | metered: yes | free allowance: 100 GB registered, 15 GB anonymous (period not printed) | source: [1]
- identity: email | detail: The registered tier is reached with a 'Get yourself Registered' button; the form fields were not read, so the identity is unverified beyond an account. The anonymous tier needs no account.
- interface: unknown
- limits:
  - volume-quota: download volume 100 GB registered, 15 GB anonymous, unlimited premium [1]
  - per-object-cap: 5 GB registered, 1 GB anonymous, 100 GB premium [1]
  - retention-clamped (binding): 7 days registered, 3 days anonymous, never premium [1]
- binding note: A 7-day deletion on registered and 3 days on anonymous bounds the pull window before any byte cap matters.
- interface detail: Web upload with remote URL upload on the plan table; no API page was read.
- tooling: Browser only as read.
- composes with: 100 GB of download volume on a free registered account is a large free allowance, but files live only 7 days.
- reliability: The page prices Premium at $10.99 for 30 days with auto-renew No.
- evidence note: Plan table read on the vendor premium page on 2026-11-03; the registration form was not read.
- extras:
  - plans: Anonymous $0; Registered $0; Premium $10.99 / 30 days; Premium PRO $14.99 / 30 days
- evidence:
  - [1] 2026-11-03: the cheapest paid plan is $10.99 for 30 days | capture: sha256:164d7689a1cfb545b5760b923b44db15815686e437a90c74e286d102e6ec18af | quote: $10.99 for 30 days
  - [1] 2026-11-03: the plan table lists a per-file upload cap for each plan | capture: sha256:164d7689a1cfb545b5760b923b44db15815686e437a90c74e286d102e6ec18af | quote: Max upload file size
- sources:
  - [1] https://datavaults.co/premium/
