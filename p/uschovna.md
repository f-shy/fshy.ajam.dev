# Úschovna

> uschovna.cz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uschovna/ | JSON https://fshy.ajam.dev/api/v1/entity/uschovna.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Úschovna (uschovna.cz)

- `storage/schovna` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.uschovna.cz
- free tier: Anonymous transfer: 30 GB per shipment, free, 14 days, 30 downloads per recipient. Paid (40 CZK): 50 GB, 90 days, unlimited downloads. Registered 'úschovna+' adds 50 GB of permanent storage on top of unlimited 50 GB sends. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 30 GB | bytes: 30000000000 | source: [1] | note: not stated
- retention: Retention 14 days free, 90 days paid | days: 14 | source: [1] | note: not stated
- egress: Not metered; the paid upsell is retention and download count, not bandwidth. | metered: yes
- identity: anonymous
- interface: rest
- limits:
  - retention-clamped: Retention 14 days [1]
  - per-object-cap (binding): per-object-cap 30 GB [1]
- limits note: per-object-cap 30 GB free / 50 GB paid. Retention 14 days free, 90 days paid. 30 downloads per recipient on free.
- interface detail: rest
- tooling: Web only; no API.
- composes with: Allows 30 GB per shipment with 14-day expiration. Persistent storage options require paid tiers starting at 50 GB.
- reliability: Clean and honest pricing page (0 Kč explicitly listed next to 40 Kč), long-running CZ service. Nowhere near the volume needed.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Anonymous transfer: 30 GB per shipment, free, 14 days, 30 downloads per recipient. Paid (40 CZK): 50 GB, 90 days, unlimited downloads. Registered 'úschovna+' adds 50 GB of permanent storage on top of unlimited 50 GB sends.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Posílejte zdarma až 30 GB ... Zůstanou u nás online k vyzvednutí po dobu 14 dní', 'do 30 GB / 14 dní / 30x / 0 Kč', 'do 50 GB / 90 dní / NEOMEZENĚ / 40 Kč'
  - [1] 2026-10-21: úschovna+ includes '50 GB prostoru pro trvalé uložení zásilek'
- sources:
  - [1] https://www.uschovna.cz/cenik
