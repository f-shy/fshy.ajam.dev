# Up2Share

> up2sha.re | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/up2sha/ | JSON https://fshy.ajam.dev/api/v1/entity/up2sha.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Up2Share

- `debrid/up2share` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (free account, monthly plans) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://up2sha.re/
- price EUR 7.49 per month for 1 TB of storage (Pro) | parsed USD 8.39/TB-mo
- free tier: Free plan: 1 GB per file, unlimited uploads, files kept 30 days, 20 GB of total storage, created with a free account. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: 1 GB per file on Free; 5 GB Basic, 10 GB Plus, 20 GB Pro, 30 GB Business | source: [1]
- retention: 30 days on Free; 90 days Basic, 365 days Plus, unlimited Pro | days: 30 | source: [1]
- egress: No download volume is published; the plan table lists price, file size, expiry and total storage only. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: The free plan needs an account (Create account on the pricing block); the form fields were not read. Paid plans are bought through an account subscription page.
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB per file on Free [1]
  - volume-quota: 20 GB of total storage on Free [1]
  - retention-clamped: files expire after 30 days on Free [1]
- binding note: A 1 GB file ceiling on the free plan is below what a large archive needs; the 20 GB total is second.
- interface detail: Web upload; the Plus plan lists unlimited API quota, so an API exists on paid plans; its documentation was not read.
- tooling: Browser upload; an API is listed on the Plus plan and above.
- composes with: Basic at 0.99 EUR per month is the cheapest paid tier: 5 GB per file, 150 GB of storage, 90-day expiry.
- reliability: The vendor page answered HTTP 403 to the page reader while still returning its full content. A cookie consent prompt is shown on the page.
- notes: Prices are per month; the Plus price is shown with a struck-through 3.49 EUR list price.
- evidence note: Plan table read on the vendor home page. The registration form fields and the payment methods are unread.
- evidence:
  - [1] 2026-11-03: per-file caps by plan: 1 GB free, 5 GB Basic, 10 GB Plus, 20 GB Pro | capture: sha256:7368a6880795d122e7d2f22e6cc9dd28331ca8782db97118468cf5e1573989b5 | quote: | Max File Size | 1 GB | 5 GB | 10 GB | 20 GB |
  - [1] 2026-11-03: retention by plan: 30 days free | capture: sha256:7368a6880795d122e7d2f22e6cc9dd28331ca8782db97118468cf5e1573989b5 | quote: | Files Expiry | 30 days | 90 days | 365 days | Unlimited |
  - [1] 2026-11-03: storage by plan: 20 GB free | capture: sha256:7368a6880795d122e7d2f22e6cc9dd28331ca8782db97118468cf5e1573989b5 | quote: | Total Storage | 20 GB | 150 GB | 500 GB | 1 TB |
  - [1] 2026-11-03: the cheapest paid plan is 0.99 EUR per month | capture: sha256:7368a6880795d122e7d2f22e6cc9dd28331ca8782db97118468cf5e1573989b5 | quote: | Price | Free | 0.99€/m | 2.49€/m ~~3.49€~~ | 7.49€/m |
  - [1] 2026-11-03: hosting needs an account | capture: sha256:7368a6880795d122e7d2f22e6cc9dd28331ca8782db97118468cf5e1573989b5 | quote: Create an account and host as many files as you want, without expiration.
- sources:
  - [1] https://up2sha.re/
