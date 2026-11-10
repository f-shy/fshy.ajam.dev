# udrop

> udrop.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/udrop/ | JSON https://fshy.ajam.dev/api/v1/entity/udrop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## udrop

- `debrid/udrop` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (free 100 GB account, guest upload) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://www.udrop.com/
- free tier: Every registered free account gets a 100GB free cloud storage pool; guests can upload without an account; downloads are not throttled and carry no countdown timer. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: 5GB per file | source: [1]
- retention: guest uploads expire after 30 days of inactivity; registered files are not swept by an automatic expiry | days: 30 | source: [1]
- egress: No speed cap and no forced countdown for recipients; the site is funded by ads on download pages. No download volume figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: A free account is created from a register form; its fields were not read. Guests can upload without an account and those files expire after 30 days of inactivity.
- interface: webdav, ftps, rest
- limits:
  - per-object-cap: 5GB per file [1]
  - volume-quota (binding): 100GB of storage per free account; uploads pause when the quota is full [1]
  - retention-clamped: guest uploads expire after 30 days of inactivity [1]
- binding note: The 100 GB pool is the ceiling on a free account; the 5 GB per-file cap applies inside it.
- interface detail: WebDAV mount, FTPS (explicit TLS) on port 21 for registered accounts, and a public API, all described on the FAQ page; none was probed.
- tooling: Browser upload, WebDAV mount, FTPS clients such as FileZilla, and a public API (all per the FAQ).
- composes with: A 100 GB free account with WebDAV, FTPS and an API at no charge; no paid plan appears on the pages read.
- reliability: The FAQ states one free account per individual or business.
- notes: The FAQ claims the free tier is sustained by advertising on download pages.
- evidence note: Quota, cap, expiry and interfaces read on the vendor FAQ page. Cheapest paid tier: unverified: no paid plan appears on the pages read.
- evidence:
  - [2] 2026-11-03: the home page advertises 100 GB of free storage | capture: sha256:ead02f606cf2c51f96a7897abf16524b289c153af67a32058b610399edda51f4 | quote: ## Claim your 100GB of free storage!
  - [1] 2026-11-03: the per-file cap is 5 GB | capture: sha256:913932979b7ed637431143f19bf0dd10e820170e4eba2b405953f854c10756f2 | quote: You can upload individual files up to 5GB in size.
  - [1] 2026-11-03: guest uploads expire after 30 days of inactivity | capture: sha256:913932979b7ed637431143f19bf0dd10e820170e4eba2b405953f854c10756f2 | quote: will expire automatically after <strong>30 days of inactivity</strong>
  - [1] 2026-11-03: registered accounts have FTPS on port 21 | capture: sha256:913932979b7ed637431143f19bf0dd10e820170e4eba2b405953f854c10756f2 | quote: Every registered account has access to our high speed data ingest layer via secure FTPS (FTP over Explicit TLS) on Port 21
  - [1] 2026-11-03: a public API is described on the FAQ page | capture: sha256:913932979b7ed637431143f19bf0dd10e820170e4eba2b405953f854c10756f2 | quote: Is there a public API available for automated workflows?
  - [1] 2026-11-03: downloads are not speed-capped | capture: sha256:913932979b7ed637431143f19bf0dd10e820170e4eba2b405953f854c10756f2 | quote: No. We never throttle your bandwidth.
  - [3] 2026-11-03: a register form exists at the register page | capture: sha256:bcc051966d75a5143d082be51cbdd7161cd6cb726888708949571766f958c28a | quote: By registering, you agree to our [Terms](https://www.udrop.com/terms) & [Privacy](https://www.udrop.com/privacy) Policies.
- sources:
  - [1] https://www.udrop.com/faq
  - [2] https://www.udrop.com/
  - [3] https://www.udrop.com/register
