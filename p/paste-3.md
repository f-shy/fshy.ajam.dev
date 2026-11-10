# paste.rs

> paste.rs | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/paste-3/ | JSON https://fshy.ajam.dev/api/v1/entity/paste-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## paste.rs

- `storage/paste-rs` | fails-quota | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://paste.rs
- free tier: 393,216 bytes per paste (measured). 373,336 chars -> 201 Created; 426,668 chars -> 206 Partial Content with 393,216 bytes stored. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free direct GET, plain text, no metering. | metered: no
- identity: anonymous
- interface: rest
- limits note: 393,216 bytes hard; 'Pasting is heavily rate limited' (explicit in docs, no numeric limit published); no expiry documented; DELETE requires only the URL.
- interface detail: rest
- tooling: curl --data-binary @file https://paste.rs/ returns the URL on stdout; DELETE /<id> works; documented shell function for .bashrc. No wrapper ecosystem needed.
- composes with: unlimited pastes x 384 KiB. 1 TiB = ~2.7M pastes. Only useful if an encoder pipeline is allowed to fan out aggressively; otherwise a control-plane store.
- reliability: Silent truncation: it returns 206 Partial Content rather than an error, so a naive client will believe the full object was stored. Docs also state pasting is heavily rate limited.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 393,216 bytes per paste (measured). 373,336 chars -> 201 Created; 426,668 chars -> 206 Partial Content with 393,216 bytes stored.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'If the response is 206 (PARTIAL), then the paste exceeded the server's maximum upload size ... Pasting is heavily rate limited'
  - withheld 2026-10-21: probe: POST 373,336 bytes -> 201; POST 426,668 bytes -> 206; GET the 206 result -> 393,216 bytes stored
  - [2] 2026-10-21: probe: POST 5,000-byte payload -> 201 (round trip confirmed with matching body)
- sources:
  - [1] https://paste.rs/
  - [2] https://paste.rs/<id>
