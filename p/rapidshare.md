# RapidShare.io

> rapidshare.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rapidshare/ | JSON https://fshy.ajam.dev/api/v1/entity/rapidshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RapidShare.io

- `debrid/rapidshare-io` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (free upload, premium day passes) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://rapidshare.io/
- free tier: Uploading and downloading are free for all users, including without an account; free or non-account files are kept 90 days and each file must be under 1 GB. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 1 GB per file for free or non-account uploads; 10 GB per file on premium | source: [1]
- retention: 90 days for free or non-account files; unlimited on premium | days: 90 | source: [1]
- egress: Premium is sold as a pass: $1.99 for 1 day, $9.99 for 1 month, $30.99 for 6 months, $99.99 forever; it removes waiting, ads and speed limits. No download volume figure is published on the pages read. | metered: no | free allowance: not published | source: [2]
- identity: anonymous | detail: Upload works without registering; a registered account is created with an email address, to which the password is sent. Premium is paid through an on-site payment selector.
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB per file for free or non-account uploads; 10 GB on premium [1]
  - retention-clamped: free or non-account files are kept 90 days [1]
- binding note: The 1 GB per-file ceiling stops anything larger before retention or speed matter.
- interface detail: Web upload form with a no-registration route; no API page was read.
- tooling: Browser upload; premium links resolve through any debrid service that lists the host. No API or client is documented on the pages read.
- composes with: A 1 GB-per-file anonymous drop with a 90-day clock; the cheapest paid access is a $1.99 one-day pass.
- reliability: No status page; the free tier is ad-supported and files expire after 90 days.
- notes: Cheapest paid tier is the $1.99 one-day pass.
- evidence note: Limits and prices read on the vendor FAQ and upgrade pages. Download speed on the free tier and the payment methods behind the selector are unread.
- evidence:
  - [1] 2026-11-03: the free or non-account cap is 1 GB per file, 10 GB on premium | capture: sha256:dc3ce4d85bb78c9d7541e08a924ead9943e4f0dc24449f863ec47a7da86abbc6 | quote: Each file you upload must be less than 1 GB in size for free/non accounts or less than 10 GB in size for premium accounts.
  - [1] 2026-11-03: free retention is 90 days, premium is unlimited | capture: sha256:dc3ce4d85bb78c9d7541e08a924ead9943e4f0dc24449f863ec47a7da86abbc6 | quote: Free/non accounts files are kept for 90 days. Premium accounts files are kept for unlimited days.
  - [2] 2026-11-03: the cheapest paid tier is a $1.99 one-day pass | capture: sha256:7bcf0b317ad41ce33a14e0459f576baea0de2700c33958ca9bc2e77113a36107 | quote: Starting from just $1.99 for a 1 day access pass, RapidShare is one of the most affordable file hosts in the universe!!!
  - [2] 2026-11-03: the forever premium plan is $99.99 | capture: sha256:7bcf0b317ad41ce33a14e0459f576baea0de2700c33958ca9bc2e77113a36107 | quote: $99.99
  - [3] 2026-11-03: uploads are possible without an account | capture: sha256:e25d0a395c141a3b93000c17a3907a790c0c23db8d6609620cd405e8d27d8583 | quote: Upload without registering!
  - [4] 2026-11-03: an account is created with an email address | capture: sha256:35cd113c3f932d0bae82bbd8e45d2254b302fa269a7e55ffa2896db87d5e5d17 | quote: Your new account password will be sent to your email address.
- sources:
  - [1] https://rapidshare.io/faq
  - [2] https://rapidshare.io/upgrade
  - [3] https://rapidshare.io/
  - [4] https://rapidshare.io/register
