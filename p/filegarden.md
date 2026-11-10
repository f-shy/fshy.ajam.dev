# File Garden

> filegarden.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filegarden/ | JSON https://fshy.ajam.dev/api/v1/entity/filegarden.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File Garden

- `storage/file-garden` | fails-quota | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filegarden.com
- free tier: free, 'forever' retention; per-file and per-account caps not published on the landing page | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: free, 'forever' retention; per-file and per-account caps not published on the landing page | not published on the page reached; account-based (Discord login), so not anonymous despite the free tier. | source: [1] | note: not stated
- egress: unmetered direct links, intended for hotlinking | metered: no
- identity: institution
- interface: rest
- limits note: not published on the page reached; account-based (Discord login), so not anonymous despite the free tier.
- interface detail: rest
- tooling: web UI; login via Discord. No public REST upload API documented.
- composes with: Allows multiple free Discord-authenticated accounts with indefinite retention on hosted files.
- reliability: Only candidate here with indefinite retention, but it is account-gated (Discord OAuth) and has no documented API. A wrapper would have to drive the web session.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: free, 'forever' retention; per-file and per-account caps not published on the landing page
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: GET https://file.garden/ -> 302 -> https://filegarden.com/ -> 200 / 4871 B. Login wall (Discord). Upload not attempted.
- evidence:
  - [1] 2026-10-21: 'File Garden lets you upload any type of file to link elsewhere, forever for free.' + Discord logIn
- sources:
  - [1] https://filegarden.com/
