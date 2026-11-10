# NewsLeecher

> newsleecher.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/newsleecher/ | JSON https://fshy.ajam.dev/api/v1/entity/newsleecher.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NewsLeecher

- `debrid/newsleecher` | trial-only | evidence documented | binding none | category usenet provider (bundled newsreader, search and unlimited access) | tier Ready to Go
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.newsleecher.com/
- free tier: A free trial is offered ('Free Trial Signup') on each of the three plans; a third-party index states 14 days. Its data allowance is not stated on the pages read. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The trial length is third-party and the allowance is unverified: behind a sign-up.
- per-object cap: source: [1]
- retention: Close to 6,775 days | source: [1]
- egress: No speed limits and no download limits on the plans that include Usenet access | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the trial signup form was not opened, so the fields it asks for are behind a sign-up; a third-party index lists PayPal and card payments.
- interface: nntp
- limits:
  - retention-clamped: close to 6,775 days [1]
- limits note: Prices of the three plans are not on the pages read: unverified: behind a sign-up.
- binding note: No download, speed or volume limit is stated on the access plans; the cap on connections was not read.
- interface detail: NNTP with 256-bit SSL; the vendor also ships its own client with SuperSearch and SuperLeech automation
- composes with: Three plans: Pure Usenet is access only, Ready to Go adds the vendor newsreader and search, and Client Plus is software and search without access, so it adds nothing on its own to a retrieval path.
- reliability: The status of support is unmeasured.
- notes: Price unread; verdict rests on the free trial being the only stated entry.
- evidence note: The trial offer, retention and absence of limits are from the vendor pages read on 2026-11-03; prices and the 14-day length are unverified or third-party.
- evidence:
  - [1] 2026-11-03: retention is close to 6,775 days | capture: sha256:5f2b76c8069211a65797dcbdfd7e03fe616492453bbb04f78229a088895f1b07 | quote: World Leading Retention. Close to 6,775 Days
  - [1] 2026-11-03: access is unlimited | capture: sha256:5f2b76c8069211a65797dcbdfd7e03fe616492453bbb04f78229a088895f1b07 | quote: Unlimited Usenet access to our premium Usenet servers
  - [2] 2026-11-03: the Ready to Go plan is offered with a free trial | capture: sha256:ee530f44151548e7b4640a4ebae7411d023f33cb4ba7b3c4ef9292b8a6bfd422 | quote: [Sign Up Now - Free Trial](https://www.newsleecher.com/signup?ref=r2g)
  - [3] 2026-11-03: a third-party index states a 14-day free trial | capture: sha256:cd69ed0a0cfdfacc8ec636adf4771b3ceec457be5d84fdfe8d0105fed5d20f21 | quote: Nearly over 6,600 days retention, 500+ Mbps, unlimited downloads, 14-day free trial.
- sources:
  - [1] https://www.newsleecher.com/usenet-access
  - [2] https://www.newsleecher.com/readytogo/
  - [3] https://www.usenet.org/providers/newsleecher
