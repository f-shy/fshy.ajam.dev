# Meawfy

> meawfy.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meawfy/ | JSON https://fshy.ajam.dev/api/v1/entity/meawfy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Meawfy

- `debrid/meawfy` | fails-identity | evidence documented | binding none | category file-host search engine (MEGA.nz public links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://meawfy.com/
- price USD 0
- free tier: 'Create an account and get 3 credits to unlock real links from day one.' The index itself is browsable, with 42M+ entries claimed on the page. | unit: requests | metered on: identity-count | read on: 2026-10-23 | source: [1] | note: 3 credits is what an account buys before any purchase; the page does not publish a per-credit price on the surface read.
- per-object cap: not applicable: a search result | source: [1]
- retention: 'The index updates continuously, so new public links show up quickly and broken ones drop out of the results.' | source: [1]
- egress: no byte allowance: the site returns MEGA links, and the bytes come from mega.nz under the account's own MEGA transfer quota | metered: no | free allowance: none | source: [1]
- identity: email | detail: An account is required before a real link is revealed: the home page says an account gets 3 credits to unlock real links. Whether email alone is enough was not established, because the signup flow was not entered.
- interface: unknown
- limits:
  - request-rate: credits, not requests: an account starts with 3 credits and each unlocked link spends one [1]
- limits note: The credit model is the limit that binds, and it is counted per identity rather than per IP or per byte.
- binding note: The constraint that stops a caller is the account and its credit balance, which is identity, not one of the seven byte or rate constraints.
- interface detail: HTML search only. /api and /documentation both return 404 on the same host, so no machine interface is advertised. A Telegram bot exists per the site's own documentation paths.
- tooling: Browser or the Telegram bot. There is no documented REST endpoint; a client would have to drive the search page.
- composes with: Use it to find a public MEGA link by filename, then hand that link to a debrid service that accepts MEGA, or to the MEGA client under the account's own transfer quota.
- reliability: The index only sees links that were shared publicly; a link that the uploader deleted disappears from results, and the page itself frames results as 'no dead ends' without saying how often it re-checks.
- notes: One of three MEGA search fronts found in a single query (meganz.net, meawfy, zippysharedjs). All three are link indexes over publicly shared MEGA folders, so none can see a private file; the distinction between them is whether the link costs an account, which here it does.
- evidence note: The home page was read on 2026-10-23 and the two plausible API paths returned 404. Creating an account and spending a credit confirms the real per-link behaviour and the true index size.
- extras:
  - index_claim: 42M+
  - credit_start: 3
  - telegram_bot: yes
- evidence:
  - [1] 2026-10-23: 'Find MEGA links, files & folders across 42M+ indexed entries' and 'Create an account and get 3 credits to unlock real links from day one'
  - [2] 2026-10-23: HTTP 404, so no API is served at that path
  - [3] 2026-10-23: HTTP 404, so the documentation path the site implies is not at that address
- sources:
  - [1] https://meawfy.com/
  - [2] https://meawfy.com/api
  - [3] https://meawfy.com/documentation
