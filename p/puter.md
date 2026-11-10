# Puter.js AI

> puter.com | Inference, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/puter/ | JSON https://fshy.ajam.dev/api/v1/entity/puter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Puter.js AI (user-pays)

- `inference/puter-js-ai` | qualifies-with-caveat | evidence documented | binding request-rate | category inference SDK, user-pays, guest accounts
- identity a placeholder: card and phone unknown | verified 2026-11-10T01:21:21.471Z (live) | stale on 2026-12-11
- url https://docs.puter.com/
- free tier: Every account gets a free monthly allowance, shown in the dashboard; AI requests per 10 s are 20 for an anonymous (guest) account, 30 for a free account and 200 for a paid one | unit: mixed | metered on: unstated | read on: 2026-10-28 | source: [1] | note: the size of the monthly allowance is not stated on the pages read: unverified
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: unverified: the rate-limit page names an anonymous tier that is a temporary (guest) account, and the tutorial says users authenticate with their Puter account; whether a guest account can spend the monthly allowance on chat, and what a full signup collects, were not read
- interface: unknown
- limits:
  - request-rate (binding): AI requests per 10 s: 20 anonymous, 30 free, 200 paid; concurrent AI requests: 2 anonymous, 3 free, 20 paid [1]
- binding note: the guest-account ceiling of 20 requests per 10 s and 2 concurrent binds; the monthly credit is a second, unquantified gate
- endpoint: https://js.puter.com/v2/
- tooling: Puter.js, puter.ai.chat(prompt, {model}) from a browser or Node.js; there are no API keys, and each user's own Puter account carries the cost. A REST route for a non-browser client was not read
- composes with: pairs with browser apps; the cost lands on the signed-in or guest account, not on a developer key
- reliability: a call that runs out of credit answers 402 insufficient_funds and the SDK shows the user an upgrade prompt
- evidence note: all values are from first-party documentation; no request was sent to a Puter endpoint
- evidence:
  - [2] 2026-10-28: AI calls are made under each user's Puter account with no developer API key | capture: sha256:6472bbdfdf3d310105e64b4ec90b2710b58fcf654ce227b4bf6f388d5dceab34 | quote: Puter.js uses the [User-Pays model](https://docs.puter.com/user-pays-model/), where users authenticate with their Puter account and cover their own AI costs.
  - [3] 2026-10-28: every user has a free monthly allowance, with no number given | capture: sha256:bbeb4a70ef8aaefe5efe2636806db07dc6afa0a131b36aad91dcc77bddc45e3f | quote: - Every user starts with a free monthly allowance, enough to test out the platform and use apps built with Puter.js.
  - [1] 2026-10-28: anonymous means a temporary guest account | capture: sha256:4acd635f608b6867c358d6ffa8dcbe66ccc7cc47b85030d3d9275cacba4edaa2 | quote: Where a table shows three numbers, they are paid / free / anonymous. Paid is any subscription tier. Anonymous is a temporary (guest) account.
  - [1] 2026-10-28: AI requests per 10 s are 200 paid, 30 free and 20 anonymous | capture: sha256:4acd635f608b6867c358d6ffa8dcbe66ccc7cc47b85030d3d9275cacba4edaa2 | quote: | Requests per 10 s | 200 | 30 | 20 |
  - [1] 2026-10-28: concurrent AI requests are 20 paid, 3 free and 2 anonymous | capture: sha256:4acd635f608b6867c358d6ffa8dcbe66ccc7cc47b85030d3d9275cacba4edaa2 | quote: | Concurrent requests | 20 | 3 | 2 |
  - probe:https://js.puter.com/v2/ 2026-11-10: a keyless POST on 2026-11-10 answered 200 with an empty body, so the recorded base URL is not a completion route | capture: sha256:1e20106cef83d9091926fa2ba2ae3d3f2fdbc38766b2192e6ffab102a634b135 | quote: "status": 200
- sources:
  - [1] https://docs.puter.com/rate-limits-and-quotas/
  - [2] https://developer.puter.com/tutorials/free-unlimited-ai-api/
  - [3] https://docs.puter.com/user-pays-model/

## Puter (puter.com / Puter.js) — user-pays cloud storage

- `storage/puter-user-pays-cloud-storage` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developer.puter.com/pricing/
- free tier: Free tier shown on puter.com as '25 MB Storage' (the 100 GB / 500 GB / 2 TB figures on that page are the paid tiers. Verified by reading the raw HTML, not the rendered summary). Developer-side cost is $0: 'Puter doesn't charge developers for infrastructure. Storage, database, and AI usage are metered to each signed-in user's own Puter account.'. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: not documented, but the free allowance is 25 MB | bytes: 25000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered per-GB to the developer; metered to the end user's Puter allowance. No egress line found. | metered: yes
- identity: card
- interface: s3, rest, webdav, sftp
- limits:
  - per-object-cap (binding): per-object-cap: not documented, but the free allowance is 25 MB [1]
- limits note: per-object-cap: not documented, but the free allowance is 25 MB total, which is the real cap. Request-rate: the vendor states that 'Anti-abuse, rate limiting, and fraud detection are also built into the Puter account layer, so bots and fake sign-ups are filtered before they reach your app'. In neutral terms, its signup layer screens for excess use and automated signups, so free identities are NOT unlimited here. Retention: not documented.
- interface detail: rest
- tooling: Puter.js. A single <script> tag or the @heyputer/puter.js npm module, keyless. puter.fs.write / read / mkdir give a browser-side filesystem API; auth is 'sign in with Puter'. No S3/WebDAV/SFTP shim.
- composes with: The interesting multiplier is the opposite of the usual one: because storage is metered to each signed-in user's account, an app with N users gets N x (that user's allowance) and the developer pays nothing. But the free allowance per user is 25 MB, so the chain only works if the app also controls the user accounts. I.e. it is a way to make storage free for an app's users, not a way to get 10 TiB.
- reliability: Explicitly blocks the several-accounts route: Puter markets that 'usage is metered to each user's own account, so a bad actor has no free resources to farm', plus automated-signup filtering. That removes the second-account allowance this niche usually relies on.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free tier shown on puter.com as '25 MB Storage' (the 100 GB / 500 GB / 2 TB figures on that page are the paid tiers — verified by reading the raw HTML, not the rendered summary). Developer-side cost is $0: 'Puter doesn't charge developers for infrastructure. Storage, database, and AI usage are metered to each signed-in user's own Puter account.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: free tier '25 MB Storage'; paid tiers 100 GB / 500 GB / 2 TB
  - [2] 2026-10-21: 'Storage, database, and AI usage are metered to each signed-in user's own Puter account, so your costs don't grow with your user count'
  - [3] 2026-10-21: puter.fs.write / puter.fs.read / puter.fs.mkdir cloud storage API
- sources:
  - [1] https://puter.com/
  - [2] https://developer.puter.com/pricing/
  - [3] https://docs.puter.com/
