# paste.gg

> paste.gg | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/paste-2/ | JSON https://fshy.ajam.dev/api/v1/entity/paste-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## paste.gg

- `storage/paste-gg` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://paste.gg
- free tier: 10 MiB total per paste, 5 MiB per file. Anonymous pastes expire after 7 days; signed-in pastes can be permanent. Built on Cloudflare Workers. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 5 MiB per file | bytes: 5242880 | source: [1] | note: not stated
- retention: Anonymous pastes expire after 7 days; signed-in pastes can be permanent | days: 7 | source: [1] | note: not stated
- egress: Free outbound transfer served from Cloudflare Workers edge nodes with cacheable responses and no egress billing. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 5 MiB per file [1]
  - retention-clamped: expire after 7 days [1]
- limits note: 10 MiB total / 5 MiB per file; 7-day expiry anonymous; visibility public or unlisted when anonymous.
- interface detail: rest
- tooling: https://api.paste.gg/v1/pastes, JSON body {name, files:[{name, content:{format:'text', value}}]}; no key needed for anonymous, returns a deletion key. API keys available at Settings -> API keys.
- composes with: Unlimited anonymous pastes x up to 10 MiB, but 7-day anonymous expiry makes it a hot/cache tier only. With free accounts: permanent pastes x unlimited per account. That is the only archive-shaped path.
- reliability: CF Workers edge means fast global reads and no egress bill. Anonymous content is dropped at 7 days by design; signed-in is required for anything you want to keep.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: retention
  - dead_end.why: 10 MiB total per paste, 5 MiB per file. Anonymous pastes expire after 7 days; signed-in pastes can be permanent. Built on Cloudflare Workers.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'All pastes: up to 10 MiB total and 5 MiB per file', 'Anonymous: public or unlisted, with expiration after 7 days'
  - [2] 2026-10-21: probe: POST with 1 file -> {"status":"success","result":{"id":"89d9c016...","visibility":"unlisted"}}; GET /p/anonymous/89d9c016... -> 200
- sources:
  - [1] https://paste.gg/
  - [2] https://api.paste.gg/v1/pastes
