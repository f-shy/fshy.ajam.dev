# MegaDownloader

> megadownloader.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/megadownloader/ | JSON https://fshy.ajam.dev/api/v1/entity/megadownloader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MegaDownloader

- `debrid/megadownloader` | qualifies-with-caveat | evidence documented | binding request-rate | category free anonymous premium-link generator (no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://megadownloader.net/
- price EUR 0 (8 links/day)
- free tier: 'completely cost-free forever', capped in the FAQ: 'Our advanced web app allows you to generate up to 8 premium links daily'. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: 'Zero file size restrictions - process files of any size immediately.' | source: [1]
- retention: 'Auto-purge technology rapidly eliminates your links after completion' | source: [1]
- egress: '100% unlimited bandwidth with rapid processing technology' | metered: no | free allowance: 8 links/day | source: [1]
- identity: anonymous | detail: No account, no email; 'Unique session-based links with one-time access tokens'.
- interface: unknown
- limits:
  - request-rate (binding): up to 8 premium links daily [1]
- limits note: '+100 cloud providers' with no list on the home page.
- binding note: Eight links a day with session-token links; no byte cap is documented, so the link count is the only named limit.
- interface detail: Web form with a 'Get Premium Link' button; no API, CLI or plugin documented.
- tooling: Browser only.
- composes with: Same slot as the rest of the family; the name collides with the unrelated open-source Mega downloader, so a client searching for tooling finds the wrong project first.
- reliability: One-time session tokens mean an interrupted download cannot be resumed from the same link; no status page.
- notes: Fourth member of the 8-a-day template family.
- evidence note: Cap and flow vendor-stated, read; enforcement untested.
- evidence:
  - [1] 2026-10-23: 'generate up to 8 premium links daily', 'completely cost-free forever', '+100 cloud providers', 'one-time access tokens'
- sources:
  - [1] https://megadownloader.net/
