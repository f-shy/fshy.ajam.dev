# AnyDebrid

> anydebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anydebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/anydebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnyDebrid

- `debrid/anydebrid` | qualifies-with-caveat | evidence documented | binding request-rate | category free anonymous premium-link generator (no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://anydebrid.com/
- price EUR 0 (8 links/day)
- free tier: 'Our premium link generator is 100% unlimited and free.' The FAQ then states the real cap: 'With our debrid tool you can generate almost 8 premium links per day.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: No account, no email, no card. The counter is link generations per day, not bytes.
- per-object cap: 'No annoying file size limits' - no ceiling published, and none can be verified without generating a link | source: [1]
- retention: 'All generated premium links are eliminated after download has finished.' | source: [1]
- egress: 'We never limit or restrict your download bandwidth. Full speed 100% guaranteed!' | metered: no | free allowance: 8 links/day | source: [1]
- identity: anonymous | detail: No registration form, no login, no email field on the generator. The only identifier is the caller IP, and generated links are bound to it ('only the user that started the process can download it').
- interface: unknown
- limits:
  - request-rate (binding): 8 premium links per day per user [1]
- limits note: The page also claims '+100 unrestricted file hosters' with no list on the home page; the host list is a separate page that was not read.
- binding note: Eight links a day is the first wall: 1 TiB of monthly transfer spread over 30 days needs roughly 35 GB per link at 8 links a day, and any link that fails or is retried spends one of the eight.
- interface detail: A single web form: paste a host link, press Generate link, receive a time-limited download URL. No API, CLI or plugin is documented.
- tooling: Browser only; the site names no download-manager integration.
- composes with: With no account it is the only option among debrid providers that leaves no identity trail, so it works as a one-off fetch for a file otherwise unreachable - not as infrastructure.
- reliability: Generated links are IP-locked and deleted on completion, so a failed or interrupted transfer costs one of the eight daily slots; the site publishes no status page.
- notes: The 'unlimited' headline and the 8-a-day FAQ contradict each other on the same page; the FAQ is the enforceable one. Common template with MaxDebrid, YouDebrid and MegaDownloader (same cap, same section order, same generator-container class) but different builds and different article content, so common ownership is plausible and not established - do not count these four as four independent providers until one backend is demonstrated.
- evidence note: Two conflicting claims on one vendor page (unlimited vs 8 links/day), read. No link was generated, so whether the cap is enforced and whether any host resolves is untested; a successful generation would raise this to measured.
- evidence:
  - [1] 2026-10-23: '100% unlimited and free' in the feature list against 'you can generate almost 8 premium links per day' in the FAQ; '+100 unrestricted file hosters'; the single-IP link binding
  - probe:html-fingerprint https://anydebrid.com/ 2026-10-23: a 'generator-container' block and the same section order as MaxDebrid, YouDebrid and MegaDownloader, which is a shared front-end template rather than a shared build (different title, different article slugs, 53,436 bytes against 51,723 on MaxDebrid)
- sources:
  - [1] https://anydebrid.com/
