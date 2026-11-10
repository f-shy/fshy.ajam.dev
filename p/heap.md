# Heap

> heap.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/heap/ | JSON https://fshy.ajam.dev/api/v1/entity/heap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Heap

- `dev-services/heap` | qualifies-with-caveat | evidence documented | binding volume-quota | category product analytics with autocapture (hosted, by Contentsquare) | tier Free
- needs card no, phone yes, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://www.heap.io/pricing
- free tier: Free plan: up to 10k monthly sessions with core analytics charts, unlimited enrichment sources, guides integrations, 6 months of data history and SSO; no CSV exports; past the monthly limit data is neither dropped nor throttled but stays hidden until the account upgrades | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The unit is the session, a period of activity of one user that ends after 30 minutes of pageview inactivity on the web and 5 minutes on mobile; the vocabulary has no sessions term, so mixed is the nearest. The sign-up button reads Start Free Trial, and whether the Free plan has an end date is unverified: not stated on the pricing page.
- per-object cap: unverified: no per-event size is stated on the pages read
- retention: 6 months of data history on Free, against 12 months on Growth; 3 years is an add-on for Pro and Premier | source: [1]
- egress: CSV exports start on the Growth plan and are not part of Free; the server-side APIs send data in and delete users, and no read API is named for Free | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for a first name, a last name, a work email address, a password, a company name, a company size and a storage region in the US or the EU, with an optional phone number; no card field appears on it. The button reads Start Free Trial.
- interface: rest
- limits:
  - volume-quota (binding): up to 10k monthly sessions on Free [1]
  - retention-clamped: 6 months of data history on Free [1]
- limits note: Free has no CSV exports, no unlimited users and reports and no chart customization, which start on Growth.
- binding note: The 10k monthly sessions are the ceiling, and past it the data is hidden until the account upgrades.
- interface detail: Server-side APIs send server-side data, including user and account properties, into Heap and delete users with an auth token; an EU datacenter needs the calls sent to c.eu.heap-api.com. Events from sites and apps come from the web snippet and SDKs. Which APIs are open to the Free plan is unverified: the pricing page's APIs row did not keep its marks.
- endpoint: https://heapanalytics.com
- tooling: the web snippet and mobile SDKs with autocapture, the server-side APIs and the web app
- composes with: Autocaptured product analytics for the front end of a free-hosted app, up to 10k sessions a month, with 6 months of history and no event tagging.
- reliability: past the monthly session limit data is not dropped or throttled, and the owner receives an email asking to upgrade before the data can be viewed again
- evidence note: Plan limits are quoted from the first-party pricing page, read through a pinned page reader, and the sign-up fields from the sign-up page. No account was opened, so later steps are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Free plan includes core analytics charts, unlimited enrichment sources, guides integrations, 6 months of data history and SSO | capture: sha256:07fa8bb0cc11a3d24dd27c5c1da2952507d73f553622c6e2ae978c59228b55b9 | quote: • Core analytics charts • Unlimited enrichment sources • Guides integrations • 6 months data history • SSO
  - [1] 2026-11-01: the Free plan is limited to 10k monthly sessions | capture: sha256:07fa8bb0cc11a3d24dd27c5c1da2952507d73f553622c6e2ae978c59228b55b9 | quote: Up to 10k monthly sessions
  - [1] 2026-11-01: Growth adds CSV exports and 12 months of data history to Free | capture: sha256:07fa8bb0cc11a3d24dd27c5c1da2952507d73f553622c6e2ae978c59228b55b9 | quote: • Unlimited users & reports • Chart customization • CSV exports • 12 months data history
  - [1] 2026-11-01: past the plan limit data is not dropped or throttled but cannot be viewed until the account upgrades | capture: sha256:07fa8bb0cc11a3d24dd27c5c1da2952507d73f553622c6e2ae978c59228b55b9 | quote: Don’t worry — we won’t drop or throttle your data! Once you exceed your plan’s monthly limit, you’ll receive an email asking you to upgrade to the appropriate tier. You’ll need to do this before you can view your data again.
  - [1] 2026-11-01: a session ends after 30 minutes of pageview inactivity on the web and 5 minutes on mobile | capture: sha256:07fa8bb0cc11a3d24dd27c5c1da2952507d73f553622c6e2ae978c59228b55b9 | quote: On web, a session ends after 30 minutes of pageview inactivity from the user. On mobile, a session ends after 5 minutes of inactivity
  - [1] 2026-11-01: 3 years of data history is an add-on for Pro and Premier | capture: sha256:07fa8bb0cc11a3d24dd27c5c1da2952507d73f553622c6e2ae978c59228b55b9 | quote: Extend your analysis capabilities out to 3 years. Unlock seasonal insights and compare year on year product updates. Add-on for Pro and Premier
  - [2] 2026-11-01: the server-side APIs send server-side data into Heap and delete users with an auth token | capture: sha256:045ce810a5f57fdd34f0130e456d75984d5262f20e015395e9dc982265d65200 | quote: Send server-side data into Heap, including user and account properties, to enrich your autocaptured dataset
  - [2] 2026-11-01: an EU datacenter needs server-side calls sent to c.eu.heap-api.com | capture: sha256:045ce810a5f57fdd34f0130e456d75984d5262f20e015395e9dc982265d65200 | quote: If your Heap data is in an EU datacenter, you must send server-side API calls to
  - [3] 2026-11-01: the sign-up form asks for a name, work email, password, company, size and region with an optional phone number | capture: sha256:90190459a624d3501752f5a2a31ebb3e090fd622f66026a8551e24d27c85880d | quote: Work Email \* Password \* Phone Number (optional) Company Name \* Company Size \*
  - [3] 2026-11-01: the storage region is chosen at sign-up between the US and the EU | capture: sha256:90190459a624d3501752f5a2a31ebb3e090fd622f66026a8551e24d27c85880d | quote: Storage Region \* United States (us-east-1)Europe (eu-west-1)
- sources:
  - [1] https://www.heap.io/pricing
  - [2] https://developers.heap.io/reference/server-side-apis-overview
  - [3] https://heapanalytics.com/signup
