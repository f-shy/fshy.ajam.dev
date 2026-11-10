# Nitroflare

> nitroflare.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nitroflare/ | JSON https://fshy.ajam.dev/api/v1/entity/nitroflare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nitroflare

- `storage/nitroflare` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nitroflare.com
- free tier: Free: 'You can upload up to 10 GB files, for free!'. No free total-storage figure published anywhere on the site. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads are throttled and ad-gated; no free CDN path, no published allowance. | metered: no
- identity: anonymous
- interface: unknown
- limits:
  - per-ip-shaping: 10 GB/day [1]
  - per-ip-shaping: 100 GB/day [1]
  - per-object-cap (binding): 10 GB per file [1]
- limits note: 10 GB per file free. Retention not published on the pages reachable (its /faq and /pricing paths both return 404). Paid = 10 GB/day, 100 GB/day on Max, per the sister brand TezFiles.
- interface detail: wrapper-only
- tooling: JDownloader, Mipony and other multihost downloaders; no documented open API.
- composes with: 10 GB per file with no stated total. Chaining is bounded by an unpublished retention policy, so it cannot be sized.
- reliability: The canonical /pricing and /faq URLs 404 on nginx, so any scraper or blog citing 'Nitroflare limits at /pricing' is pointing at a dead path. Numbers here come from the homepage meta only.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Free: 'You can upload up to 10 GB files, for free!'. No free total-storage figure published anywhere on the site.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'You can upload up to 10 GB files, for free!'
  - withheld 2026-10-21: probe: GET /pricing -> 404 Not Found (nginx); GET /faq -> 404 Not Found
- sources:
  - [1] https://nitroflare.com/
