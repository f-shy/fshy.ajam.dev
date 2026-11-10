# Ulož.to Disk

> ulozto.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ulozto/ | JSON https://fshy.ajam.dev/api/v1/entity/ulozto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ulož.to Disk

- `debrid/ulozto` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud disk (free account, monthly plans) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://ulozto.net/
- price EUR 6 per month for 3 TB of storage and 30 TB of transfer (Premium)
- free tier: FREE25 plan: 25 GB of storage at 0 EUR per month with 150 GB of data transfer per month; a FREE plan of 1 GB with the same transfer is also listed. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the plan pages state no per-file cap | source: [1]
- retention: unverified: the plan pages state no expiry for stored files | source: [1]
- egress: Data transfer per month: 150 GB on the free plans, 30 TB on Premium, 150 TB on Max, 300 TB on Ultra, 600 TB on Ultimate. | metered: yes | free allowance: 150 GB per month | source: [1]
- identity: email | detail: Registration asks for an e-mail (used as the username), a password, agreement to the conditions and a user verification step.
- interface: unknown
- limits:
  - volume-quota (binding): 25 GB of storage and 150 GB of data transfer per month on FREE25 [1]
- binding note: The 150 GB monthly transfer and the 25 GB storage are the stated free ceilings; no per-file or rate figure is published on the plan pages.
- interface detail: Web, Android, iOS and Windows apps, a file manager and an API are linked from the page; none was read.
- tooling: Browser and first-party apps; an API link exists and was not read.
- composes with: Premium is 6 EUR per month for 3 TB of storage and 30 TB of monthly transfer; the monthly transfer allowance scales with the plan.
- reliability: No status page was read.
- notes: The cheapest paid tier is Premium at 6 EUR per month.
- evidence note: Plans read on the vendor plans page and the home page. The per-file cap and the retention of free files are unread.
- evidence:
  - [2] 2026-11-03: a free plan stores up to 25 GB | capture: sha256:4312b57dea265cbd189f011c45b1df5806889c9d91a1d13c6a24d1a521f640ec | quote: Uloz.to Disk also offers a FREE plan, which is no charge and can store up to 25 GB of files.
  - [1] 2026-11-03: FREE25 includes 150 GB of data transfer per month | capture: sha256:63920a2e76e5b5f4d6ad930048ce8bde67f248c4653b9007ebf67de05359c55a | quote: More space for your memories, files, and your first projects. - 150 GB for data transfer/month
  - [1] 2026-11-03: Premium is 3 TB for 6 EUR per month | capture: sha256:63920a2e76e5b5f4d6ad930048ce8bde67f248c4653b9007ebf67de05359c55a | quote: PREMIUM Storage size 3 TB Price for month ** 6 € **
  - [3] 2026-11-03: registration asks for an e-mail, a password and a user verification | capture: sha256:faf49455da45cf0eaf492944ef0ffe83169aaeeb96826892db2c3ab0fac581d6 | quote: E-mail (will be used as Username) Password I agree with conditions Verify the user
- sources:
  - [1] https://ulozto.net/koupit-disk
  - [2] https://ulozto.net/
  - [3] https://ulozto.net/registrace
