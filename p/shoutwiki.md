# ShoutWiki

> shoutwiki.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shoutwiki/ | JSON https://fshy.ajam.dev/api/v1/entity/shoutwiki.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ShoutWiki (wiki farm, MediaWiki)

- `storage/shoutwiki` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.shoutwiki.com
- free tier: No published per-wiki storage cap; per-file ceiling is 100 MB (live siteinfo). Free, ad-supported; paid tiers exist for custom domains. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-file ceiling is 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter; images served from `images.shoutwiki.com`. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-file ceiling is 100 MB [1]
- limits note: Per-object-cap: 100 MB (104,857,600 B, from siteinfo). request-rate: the wiki HTML and the Action API are behind an Anubis proof-of-work challenge. A POST to `/w/api.php` returned the 'Making sure you're not a bot!' page instead of JSON, so programmatic access needs a PoW-capable client. Retention: no expiry published.
- interface detail: rest
- tooling: Standard MediaWiki Action API (1.43.6) + Pywikibot. No rclone backend.
- composes with: 100 MB/file x unlimited files x unlimited free wikis. Per-file cap is 10x Fandom's.
- reliability: Read path splits: the file CDN (`images.shoutwiki.com`) answers plainly (probe: 200, 12,472 B, real PNG 150x150) while the API is Anubis-gated. Browse/upload programmatically is the blocker, not retrieval.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: probe: GET (via fetch proxy) -> 200, MediaWiki 1.43.6, maxuploadsize = 104857600
  - [2] 2026-10-21: probe: GET -> 200, 12,472 bytes, PNG 150x150 — read path open
  - [3] 2026-10-21: probe: POST (action=upload) -> 200 but body is the Anubis PoW interstitial, not JSON
  - [4] 2026-10-21: ShoutWiki listed as a free wiki farm, 'free (with ads)'
- sources:
  - [1] https://www.shoutwiki.com/w/api.php?action=query&meta=siteinfo&siprop=general&format=json
  - [2] https://images.shoutwiki.com/hub/b/bc/Wiki.png
  - [3] https://www.shoutwiki.com/w/api.php
  - [4] https://www.mediawiki.org/wiki/Hosting_services
