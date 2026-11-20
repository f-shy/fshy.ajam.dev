# Uqload

> uqload.is | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uqload/ | JSON https://fshy.ajam.dev/api/v1/entity/uqload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uqload

- `debrid/uqload` | qualifies-with-caveat | evidence documented | binding per-object-cap | category video host (free account, premium days) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://uqload.is/
- free tier: Free limits: uploads up to 5000 MB, 10000 GB of storage, files deleted 90 days after the last download; playback has no bandwidth limits. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: 5000 MB per file on Free; 30000 MB on Premium | source: [1]
- retention: 90 days after the last download on Free; 365 days on Premium | days: 90 | source: [1]
- egress: Playback has no bandwidth limits; Premium is sold for a fixed number of days with no automatic renewal, and bandwidth packs cover traffic served to viewers. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: The premium page states that Premium is attached to a Uqload account and that a free account is created first; the form fields were not read.
- interface: rest, ftp
- limits:
  - per-object-cap (binding): 5000 MB per file on Free, 30000 MB on Premium [1]
  - volume-quota: 10000 GB of storage on Free, Unlimited on Premium [1]
  - retention-clamped: files are deleted 90 days after the last download on Free, 365 days on Premium [1]
- binding note: A 5000 MB file ceiling is the first limit; the 10000 GB storage is far above any other free figure.
- interface detail: Uploads by browser, FTP, remote URL or the API are stated on the home page; Premium adds torrent upload.
- tooling: Browser, FTP, remote URL upload and an API (per the home page FAQ).
- composes with: Premium is bought for a fixed number of days and raises uploads to 30000 MB and unlimited storage; the price list is not on the pages read.
- reliability: The vendor serves the same site on more than one domain (uqload.is and uqload.vc).
- evidence note: Limits read on the vendor premium page. Cheapest paid tier: unverified: the plan prices are not in the captured text of the premium page.
- evidence:
  - [1] 2026-11-03: free limits: 5000 MB uploads, 10000 GB storage, 90 days after last download | capture: sha256:889541f33a466d6f784eca7e39996e69b74e985fc9e5044712de8a1b5712dd9d | quote: Your account returns to the free limits: uploads up to 5000 MB, 10000 GB storage, and the free deletion rule (90 days after last download).
  - [1] 2026-11-03: Premium raises uploads to 30000 MB | capture: sha256:889541f33a466d6f784eca7e39996e69b74e985fc9e5044712de8a1b5712dd9d | quote: uploads up to 30000 MB, Unlimited storage
  - [1] 2026-11-03: Premium needs an account | capture: sha256:889541f33a466d6f784eca7e39996e69b74e985fc9e5044712de8a1b5712dd9d | quote: Yes. Premium is attached to a Uqload account.
  - [2] 2026-11-03: playback has no bandwidth limit | capture: sha256:c0c7bf3f5b2ebdd26f9194ae3e39ee506ebc0f66ec5093a945e7577df939adfb | quote: There are no bandwidth limits on playback.
  - [2] 2026-11-03: uploads work by browser, FTP, remote URL and API | capture: sha256:c0c7bf3f5b2ebdd26f9194ae3e39ee506ebc0f66ec5093a945e7577df939adfb | quote: Drag and drop files in your browser, or send them over FTP, from a remote URL or through the API.
- sources:
  - [1] https://uqload.is/premium
  - [2] https://uqload.is/
