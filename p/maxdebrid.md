# MaxDebrid

> maxdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/maxdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/maxdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MaxDebrid

- `debrid/maxdebrid` | qualifies-with-caveat | evidence documented | binding request-rate | category free anonymous premium-link generator (no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://maxdebrid.com/
- price EUR 0 (8 links/day)
- free tier: 'MaxDebrid premium link generator is cost free' and '100% unlimited download speed', with the cap in the FAQ: 'You can generate upto 8 premium links per day.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: 'Our leech debrid service is unrestriced. No boring file size limitations.' | source: [1]
- retention: 'Your links are removed after you finish downloading your file' | source: [1]
- egress: '100% unlimited download speed! Grab your links as fast as you can.' | metered: no | free allowance: 8 links/day | source: [1]
- identity: anonymous | detail: No account and no email on the generator. Generated files are IP-bound: 'Generated files are linked to a single IP, only you may start download.'
- interface: unknown
- limits:
  - request-rate (binding): up to 8 premium links per day [1]
- limits note: 'Over +100 cloud service providers are supported' with no list on the home page.
- binding note: The daily link count binds long before any byte cap: 8 links a day cannot carry 1 TiB of monthly transfer unless every link is over 4 GB and none fails.
- interface detail: One web form with a 'Get Premium Link' button; no API, CLI or plugin documented.
- tooling: Browser only.
- composes with: Same slot as AnyDebrid: a no-identity one-off fetch, useful only when a file exists on one of its hundred hosts and nowhere else in the stack.
- reliability: IP-bound links plus a hard daily count mean a retry is expensive; no status page.
- notes: Same template family and same 8/day cap as AnyDebrid, YouDebrid and MegaDownloader; the builds differ (51,723 bytes here against 53,436 on AnyDebrid) so one operator is likely but unproven. Count it once with that group, not as a separate provider.
- evidence note: The cap, the no-account flow and the IP binding are vendor-stated and read. No generation was attempted, so enforcement is untested.
- evidence:
  - [1] 2026-10-23: 'You can generate upto 8 premium links per day', 'Over +100 cloud service providers', 'Generated files are linked to a single IP', '100% cost free'
- sources:
  - [1] https://maxdebrid.com/
