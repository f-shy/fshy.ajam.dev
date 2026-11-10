# Blossom servers

> blossom.band | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blossom/ | JSON https://fshy.ajam.dev/api/v1/entity/blossom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blossom servers (blossom.band / blossom.nostr.build, run by nostr.build)

- `storage/blossom-servers` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blossom.band/
- free tier: 'Free uploads for everyone, from any Blossom-capable client.' 'A hard cap of 100 MiB per upload (20 MiB for free uploads), with no limit on the number of uploads or retention.' | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MiB per upload | bytes: 104857600 | source: [1] | note: not stated
- retention: 'Free uploads for everyone, from any Blossom-capable client.' 'A hard cap of 100 MiB per upload (20 MiB for free uploads), with no limit on the number of uploads or retention.' | source: [1] | note: not stated
- egress: unmetered, direct CDN URLs, CORS '*'. Reads 307-redirect to image.nostr.build which serves with Accept-Ranges and 206. | metered: no
- identity: card
- interface: rest, cli
- limits:
  - per-object-cap (binding): 100 MiB per upload [1]
  - write-gated: application/zip and application/octet-stream were both 415 'File type not allowed' [1]
  - write-gated: application/octet-stream got 400 'Content-Type header does not match the file content' [1]
- limits note: Per-object cap is 20 MiB for free uploads and 100 MiB on the paid plan. Observed 15 MiB accepted and 25 MiB rejected with HTTP 413 'File size exceeds the maximum allowed size of 20 MiB'. Content-Type headers are validated against file content, rejecting application/zip and application/octet-stream with HTTP 415. No retention limit is stated.
- interface detail: rest
- tooling: Blossom protocol: PUT /upload with an 'Authorization: Nostr <base64 kind-24242 event>' header signed by any self-generated secp256k1 key. No signup, no account, no email. Any Nostr client (Amethyst, Coracle, nak, blossom-server CLI) speaks it.
- composes with: Identity is a pubkey you generate offline in one line of code. Unlimited free identities, zero cost, zero email. Each pubkey gets its own npub1..blossom.band hostname at upload time. 20 MiB x unlimited uploads x unlimited pubkeys. At 19 MiB per object, 10 TiB = ~550,000 uploads across ~550k keys, or a few thousand keys each doing 100 uploads.
- reliability: A ~19 MiB upload returned HTTP 500 'Error uploading the file: unknown error' while 5 and 15 MiB succeeded, so the usable ceiling is somewhat below the advertised 20 MiB; one 5 MiB upload took 14 s from a user.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [1] 2026-10-21: 'Free uploads for everyone, from any Blossom-capable client'; 'A hard cap of 100 MiB per upload (20 MiB for free uploads), with no limit on the number of uploads or retention'
  - [2] 2026-10-21: probe: PUT with self-signed kind-24242 auth -> 201 CREATED, url https://npub1n33yj...blossom.band/<sha256>.png, then GET -L -> 200, 1266 bytes, sha256 identical to uploaded file
  - withheld 2026-10-21: probe: 15,728,509-byte PNG -> 201; 26,214,269-byte PNG -> 413 'File size exceeds the maximum allowed size of 20 MiB'; probe GET with Range: bytes=1000-1099 -> 206 Content-Range: bytes 1000-1099/5242749
- sources:
  - [1] https://blossom.band/
  - [2] https://blossom.band/upload

## blossom.band / nostr.build blossom (free tier)

- `storage/blossom-band-nostr-build-blossom` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blossom.band/
- free tier: none reachable: Free uploads are 20 MiB per file with no retention guarantee ('A hard cap of 100 MiB per upload (20 MiB for free uploads)'), and the BUD-06 pre-flight is actively refused to non-browser… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Free uploads are 20 MiB per file with no retention guarantee ('A hard cap of 100 MiB per upload (20 MiB for free uploads)'), and the BUD-06 pre-flight is actively refused to non-browser…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free uploads are 20 MiB per file with no retention guarantee ('A hard cap of 100 MiB per upload (20 MiB for free uploads)'), and the BUD-06 pre-flight is actively refused to non-browser…
  - [2] 2026-10-21: cited as the basis of the rejection: Free uploads are 20 MiB per file with no retention guarantee ('A hard cap of 100 MiB per upload (20 MiB for free uploads)'), and the BUD-06 pre-flight is actively refused to non-browser clie
  - [3] 2026-10-21: cited as the basis of the rejection: Free uploads are 20 MiB per file with no retention guarantee ('A hard cap of 100 MiB per upload (20 MiB for free uploads)'), and the BUD-06 pre-flight is actively refused to non-browser clie
- sources:
  - [1] https://blossom.band/
  - [2] https://b.nostr.build/
  - [3] https://blossom.band/upload
