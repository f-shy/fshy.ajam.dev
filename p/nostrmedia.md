# nostrmedia.com

> nostrmedia.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nostrmedia/ | JSON https://fshy.ajam.dev/api/v1/entity/nostrmedia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nostrmedia.com (NIP-96 file host)

- `storage/nostrmedia-com` | qualifies-with-caveat | evidence reported | binding per-object-cap | category p2p-blob-storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nostrmedia.com/
- free tier: free plan max_byte_size 26,214,400 (25 MiB); paid 'purple'/'onyx' 104,857,600 (100 MiB). `file_expiration: [0,0]` on every plan = never expires. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 25 MiB | bytes: 26214400 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered, Cloudflare-fronted (Server: cloudflare, Cache-Control public max-age=14400). | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits:
  - per-object-cap (binding): per-object-cap 25 MiB [1]
- limits note: Per-object-cap 25 MiB free. 125 MB on the direct /upload, 5 GB via /presigned (per llms.txt). The /presigned path is the one that matters and it is far above the free plan's advertised 25 MiB.
- interface detail: NIP-96 HTTP file storage. Discoverable at /.well-known/nostr/nip96.json; POST /upload; /presigned 'handles up to 5 GB'.
- tooling: curl; NIP-98 Authorization header (signed event). The llms.txt documents the /presigned path for large objects.
- composes with: Machine-readable plan manifest means the cap is queryable rather than scraped. One GET tells you the size ceiling per plan.
- reliability: Transforms media at ingest on some paths (resizing, format_conversion, compression, metadata_stripping are all listed in the manifest). Verify that originals come back byte-identical.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [1] 2026-10-21: literal body: api_url https://nostrmedia.com/upload, download_url https://file.nostrmedia.com, supported_nips [94,96,98], plans.free.max_byte_size 26214400, file_expiration [0,0], media_transformations image [resizing, format_conversion, compression, metadata_stripping]
  - [2] 2026-10-21: 'A single POST to /upload accepts files up to 125 MB; /presigned handles up to 5 GB', 'Uploads never expire while the subscription is active'
  - [3] 2026-10-21: '/upload answers 413 above 125 MB because the request would outlive the worker'
- sources:
  - [1] https://nostrmedia.com/.well-known/nostr/nip96.json
  - [2] https://nostrmedia.com/llms.txt
  - [3] https://nostrmedia.com/docs/api.md
