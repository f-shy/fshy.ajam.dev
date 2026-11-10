# GDFlix

> gdflix.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gdflix/ | JSON https://fshy.ajam.dev/api/v1/entity/gdflix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GDFlix

- `debrid/gdflix` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category Google Drive sharing front end (Indian DDL ecosystem), DriveSeed template twin | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:42:17.546Z (live) | stale on 2026-11-23
- url https://gdflix.net/
- price USD 0
- free tier: "UNLIMITED - No quota limit. No annoying waiting times, Share & Download as many files as you want." Free, no account needed to download. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Same sentence, same layout and same claim as DriveSeed v5.1; this instance reports v4.6.
- per-object cap: Not stated. | source: [1]
- retention: Not stated; links resolve to a Google Drive id whose life decides theirs. | source: [1]
- egress: One-click download from the site, no wait. No price, allowance or meter printed. | metered: no | source: [1]
- identity: anonymous | detail: Downloaders need no account. A publisher needs a Google account to grant the app Drive access; the sign-in is the same OAuth flow as DriveSeed.
- interface: unknown
- limits:
  - per-ip-shaping (binding): unstated; governed by Google Drive per file [1]
- limits note: No site-side counter is published. The only meaningful throttle is the one Drive applies, documented by the twin service's changelog as '403: User Rate Limit Exceeded'.
- binding note: At 1 TiB a month the bytes come from Google and Google shapes them; GDFlix adds nothing that could bind first.
- interface detail: Web only. Google OAuth sign-in, TeamDrive and shared-drive browsing, short-link creation. No first-party API was found; third-party bypass scripts exist for the family.
- tooling: Bypass scripts (for example gdflix.py in Bypass-Scripts, keyed to new.gdflix.ink) are the practical client. No SDK, no rclone backend.
- composes with: Interchangeable with DriveSeed at the bottom of the same chain: the index site can post either, and both end at a Google Drive object. Running two of them gives the operator two hosts for one Drive, which is the resilience the chain relies on.
- reliability: An instance of a copied template: three hosts were tried on 2026-10-23 and only gdflix.net answered a site (gdflix.pro was refused by network requests, and the live page itself redirects to new7.gdflix.io). Instances vanish and renumber; a link outlives the hostname that served it.
- notes: Google Drive wrapper service operating under the GDFlix brand, resolving links to hosted files.
- evidence note: The live page was read and carries the same marketing as DriveSeed. The record is deliberately thin where the vendor is: no byte number exists to record. One measured download would move it.
- extras:
  - version_seen: GDFlix v4.6 at new7.gdflix.io
- evidence:
  - [1] 2026-10-23: live GDFlix v4.6 at new7.gdflix.io with the 'UNLIMITED - No quota limit' claim, TeamDrive support and the share-link flow
  - [2] 2026-10-23: gdflix.pro is listed with appdrive.in, driveapp.in, drivehub.in, drivesharer.in and driveseed as the same lookalike family, which is why this record does not treat any one hostname as the service
- sources:
  - [1] https://gdflix.net/
  - [2] https://github.com/askfriends/Link-Bypasser-Colab
