# YouDebrid

> youdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/youdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/youdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YouDebrid

- `debrid/youdebrid` | qualifies-with-caveat | evidence documented | binding request-rate | category free anonymous premium-link generator (no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://youdebrid.com/
- price EUR 0 (8 files/day)
- free tier: 'YouDebrid premium link generator is free and will stay always free', with the cap in the FAQ: 'you may be able to debrid about 8 files per day.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: 'We don't have irritating file size limitations' | source: [1]
- retention: 'Auto-shred technology permanently destroys your premium links after download completion' | source: [1]
- egress: 'Download your link files as fast as you can, without restrictions!' | metered: no | free allowance: 8 files/day | source: [1]
- identity: anonymous | detail: No account; links are bound to the requesting IP ('Biometric IP-lock system ensures only your device can access the generated premium link').
- interface: unknown
- limits:
  - request-rate (binding): about 8 files per day [1]
- limits note: 'more than +100 cloud file hosting tools' with no list on the home page.
- binding note: Eight files a day, with IP-locked links, is the ceiling; nothing else is documented that could bind first.
- interface detail: Web form with a 'Get Premium Link' button; no API, CLI or plugin documented.
- tooling: Browser only.
- composes with: Identical role to the other anonymous generators; no reason to prefer it except when another in the family is rate-limiting the same IP.
- reliability: The marketing language ('military-grade 256-bit', 'biometric IP-lock') describes an IP check; no status page and no host list on the home page.
- notes: Third member of the 8-a-day template family (AnyDebrid, MaxDebrid, MegaDownloader). The site is the largest build of the four (73,254 bytes), which is consistent with a shared template carrying more article content rather than a different backend.
- evidence note: Cap and no-account flow are vendor-stated and read; enforcement untested.
- evidence:
  - [1] 2026-10-23: 'you may be able to debrid about 8 files per day', 'free and will stay always free', '+100 cloud file hosting tools', the IP lock
- sources:
  - [1] https://youdebrid.com/
