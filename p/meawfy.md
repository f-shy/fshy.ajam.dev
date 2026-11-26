# Meawfy

> meawfy.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meawfy/ | JSON https://fshy.ajam.dev/api/v1/entity/meawfy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Meawfy

- `debrid/meawfy` | fails-identity | evidence documented | binding none | category file-host search engine (MEGA.nz public links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:42.463Z (live) | stale on 2026-12-26
- url https://meawfy.com/
- price USD 0
- free tier: 'Create an account and get 3 credits to unlock real links from day one.' The index itself is browsable, with 42M+ entries claimed on the page. | unit: requests | metered on: identity-count | read on: 2026-10-23 | source: [1] | note: 3 credits is what an account buys before any purchase; the page does not publish a per-credit price on the surface read.
- per-object cap: not applicable: a search result | source: [1]
- retention: 'The index updates continuously, so new public links show up quickly and broken ones drop out of the results.' | source: [1]
- egress: no byte allowance: the site returns MEGA links, and the bytes come from mega.nz under the account's own MEGA transfer quota | metered: no | free allowance: none | source: [1]
- identity: email | detail: An account is required before a real link is revealed: the home page says an account gets 3 credits to unlock real links. The signup page asks for an email address and password, or Google sign-in, and requires email verification; no phone number or ID document is shown.
- interface: rest
- limits:
  - request-rate: credits, not requests: an account starts with 3 credits and each unlocked link spends one [1]
- limits note: The credit model is the limit that binds, and it is counted per identity rather than per IP or per byte.
- binding note: The constraint that stops a caller is the account and its credit balance, which is identity, not one of the seven byte or rate constraints.
- interface detail: HTML search plus a documented public POST endpoint at https://meawfy.com/api/submit-link for submitting MEGA links, with no authentication. The shorter /api and /documentation paths do not serve a page; the docs live at /documentation/api/submit-link.
- tooling: Browser or the Telegram bot for search; a documented POST endpoint at /api/submit-link for submitting links needs no authentication. Unlocking a real link still needs an account.
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
  - [4] 2026-11-25: the API documentation names an authentication field for a REST submission endpoint | capture: sha256:8f0ce94fd3f27938021d33fcffaea272a485c1bb073674f1d443a255250a97ce | quote: Authentication
  - [4] 2026-11-25: the vendor documents a REST submission endpoint at that path | capture: sha256:8f0ce94fd3f27938021d33fcffaea272a485c1bb073674f1d443a255250a97ce | quote: `https://meawfy.com/api/submit-link`
  - [4] 2026-11-25: the documented submission API needs no authentication | capture: sha256:8f0ce94fd3f27938021d33fcffaea272a485c1bb073674f1d443a255250a97ce | quote: Free to use** with no authentication flow.
  - [4] 2026-11-25: the public submission API needs no authentication | capture: sha256:8f0ce94fd3f27938021d33fcffaea272a485c1bb073674f1d443a255250a97ce | quote: None required
  - [5] 2026-11-25: signup requires an email address that must be verified | capture: sha256:084020a9d6f2b873306144d2cb8a548c5e8dd919a168ad1557f121e0f10acfcb | quote: Email verification is required.
  - [5] 2026-11-25: the signup gate is an email address, with no phone or ID document asked for | capture: sha256:084020a9d6f2b873306144d2cb8a548c5e8dd919a168ad1557f121e0f10acfcb | quote: or create your account with email
  - [1] 2026-11-25: an account still gets 3 free credits and a dead link is refunded within 5 days | capture: sha256:63b6d0ed5b2fb8d838bd7572aad0fa9878fd385f8799efe428c6b8e4b450ae28 | quote: 🎁 Get 3 free credits when you sign up🛡️ If a link dies within 5 days of unlock, we refund the credit automatically
  - [1] 2026-11-25: the index still claims 42M+ entries | capture: sha256:63b6d0ed5b2fb8d838bd7572aad0fa9878fd385f8799efe428c6b8e4b450ae28 | quote: 42M+ indexed entries. Search across courses, software, datasets, and media. No dead links or guesswork.
- sources:
  - [1] https://meawfy.com/
  - [2] https://meawfy.com/api
  - [3] https://meawfy.com/documentation
  - [4] https://meawfy.com/documentation/api/submit-link
  - [5] https://meawfy.com/signup
