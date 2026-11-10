# Bluesky

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-bluesky-social/ | JSON https://fshy.ajam.dev/api/v1/entity/github-bluesky-social.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bluesky / AT Protocol PDS — 5 MiB blob default, GC'd unless referenced

- `storage/bluesky-at-protocol-pds-5-mib-blob-default-gc-d-unless-r` | fails-quota | evidence reported | binding per-object-cap | category atproto-pds
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/bluesky-social/atproto/blob/main/packages/pds/src/config/config.ts
- free tier: blobUploadLimit defaults to 5 * 1024 * 1024 = 5 MiB per blob, overridable per-PDS via the BLOB_UPLOAD_LIMIT env var. Per-account: bsky.app's hosted PDS is generous in practice but the protocol layer only guarantees blobs that are REFERENCED by a record. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 5 MiB per blob | bytes: 5242880 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free on bsky.app's PDS and on any self-hosted PDS (it serves blobs directly from /xrpc/com.atproto.sync.getBlob). No egress meter. | metered: no
- identity: email
- interface: cli
- limits:
  - per-object-cap (binding): 5 MiB per blob [1]
- limits note: per-object-cap 5 MiB default (config.ts: `blobUploadLimit: env.blobUploadLimit ?? 5 * 1024 * 1024`); blobs unreferenced within a time window (minutes) are deleted; account-level repo size limits are enforced by the AppView/PDS separately.
- interface detail: http-xrpc
- tooling: XRPC: POST /xrpc/com.atproto.repo.uploadBlob (binary body + Content-Type) -> returns a `blob` ref; must then be referenced by a record (e.g. app.bsky.feed.post embed) or it is garbage-collected. Client libs: @atproto/api, atproto Python SDK, `goat` CLI.
- composes with: Self-hosting a PDS removes the 5 MiB default (it is a config value), so a self-hosted PDS is bounded by YOUR disk, not Bluesky's — that makes it a hosting product, not free storage. On bsky.app's PDS the 5 MiB cap plus the reference requirement makes it useless for bulk. The usable margin is only the 'unreferenced blobs are deleted within minutes' semantics working in reverse: referenced blobs are retained indefinitely.
- reliability: Blob GC is literal and fast. An upload without a referencing record vanishes. That is the single most important fact about this candidate.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: quota
  - dead_end.why: blobUploadLimit defaults to 5 * 1024 * 1024 = 5 MiB per blob, overridable per-PDS via the BLOB_UPLOAD_LIMIT env var. Per-account: bsky.app's hosted PDS is generous in practice but the protocol layer only guarantees blobs that are REFERENCED by a record.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: `blobUploadLimit: env.blobUploadLimit ?? 5 * 1024 * 1024, // 5mb`
  - [2] 2026-10-21: 'The blob will be deleted if it is not referenced within a time window (eg, minutes). Blob restrictions (mimetype, size, etc) are enforced when the reference is created. Requires auth, implemented by PDS.'
- sources:
  - [1] https://raw.githubusercontent.com/bluesky-social/atproto/main/packages/pds/src/config/config.ts
  - [2] https://raw.githubusercontent.com/bluesky-social/atproto/main/lexicons/com/atproto/repo/uploadBlob.json
