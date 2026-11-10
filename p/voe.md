# VOE

> voe.sx | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/voe/ | JSON https://fshy.ajam.dev/api/v1/entity/voe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VOE

- `debrid/voe-sx` | qualifies-with-caveat | evidence documented | binding retention-clamped | category video host (free, Premium and Premium Plus) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://voe.sx/
- free tier: Free plan at 0$ monthly: 3TB of storage, 480p or 720p quality, limited download and watch speed, files kept 60 days without a view. | unit: TB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the pages read state no per-file cap | source: [1]
- retention: files are stored 60 days without a view; the counter resets on each view and the system may extend it to 120 days or infinite | days: 60 | source: [2]
- egress: Download and watch speed is Limited on Free and Unlimited on Premium and Premium Plus. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: An account is implied by the plan table and the account deletion route in the FAQ; the sign-up form fields were not read.
- interface: unknown
- limits:
  - volume-quota: 3TB of storage on Free, 5TB on Premium, 6TB on Premium Plus [1]
  - retention-clamped (binding): 60 days without a view on Free and Premium; unlimited on Premium Plus [1]
  - per-ip-shaping: download and watch speed is limited on Free [1]
- binding note: The 60-day inactivity window binds a stored video before the 3TB storage does.
- interface detail: Web upload; no API was read.
- tooling: Browser only on the pages read.
- composes with: Premium is $9.99 monthly and Premium Plus $12.00 monthly: unlimited download and watch speed, 5TB and 6TB of storage.
- reliability: Storage space is recalculated every 5 to 7 days per the FAQ.
- notes: Cheapest paid tier is Premium at $9.99 monthly.
- evidence note: Plans read on the vendor home page and FAQ. The per-file cap is unverified: not on the pages read.
- evidence:
  - [1] 2026-11-03: plan prices: Free 0$, Premium $9.99, Premium Plus $12.00 per month | capture: sha256:5e6ffa5d1239d8196d455b2a22691bfe9df562c4e610570ac1a678fe5d586ca8 | quote: Free 0$ monthly Premium $9.99 monthly Premium Plus $12.00 monthly
  - [1] 2026-11-03: storage by plan: 3TB, 5TB, 6TB | capture: sha256:5e6ffa5d1239d8196d455b2a22691bfe9df562c4e610570ac1a678fe5d586ca8 | quote: Storage Space 3TB 5TB 6TB
  - [1] 2026-11-03: inactivity window by plan: 60 days on Free | capture: sha256:5e6ffa5d1239d8196d455b2a22691bfe9df562c4e610570ac1a678fe5d586ca8 | quote: File Inactivity 60 days 60 days Unlimited
  - [2] 2026-11-03: every account receives 3TB of storage | capture: sha256:96b1ff5a12abc2acd4ca5ed36bb4a01127cb8a787b989312f3fc38c1617a5927 | quote: All accounts receive 3TB of free storage as a base volume.
  - [2] 2026-11-03: files are stored 60 days without a view | capture: sha256:96b1ff5a12abc2acd4ca5ed36bb4a01127cb8a787b989312f3fc38c1617a5927 | quote: We store the files for 60 days without a view.
- sources:
  - [1] https://voe.sx/
  - [2] https://voe.sx/faq
