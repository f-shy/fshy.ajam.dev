# nostrmedia.com

> nostrmedia.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nostrmedia/ | JSON https://fshy.ajam.dev/api/v1/entity/nostrmedia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nostrmedia.com (NIP-96 file host)

- `storage/nostrmedia-com` | paid-only | evidence reported | binding per-object-cap | category p2p-blob-storage
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:27.597Z (live) | stale on 2026-11-25
- url https://nostrmedia.com/
- free tier: Nostr Media has no free tier. | unit: none | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per file on every tier. | bytes: 5000000000 | source: [2] | note: not stated
- retention: Uploads never expire while the subscription is active. | source: [3] | note: not stated
- egress: unmetered, Cloudflare-fronted (Server: cloudflare, Cache-Control public max-age=14400). | metered: no
- identity: anonymous | detail: Subscriptions are tied to a Nostr public key, not to an email address.
- interface: unknown
- limits:
  - per-object-cap (binding): 5 GB per file [2]
- limits note: Per-object-cap 25 MiB free. 125 MB on the direct /upload, 5 GB via /presigned (per llms.txt). The /presigned path is the one that matters and it is far above the free plan's advertised 25 MiB.
- interface detail: NIP-96 HTTP file storage. Discoverable at /.well-known/nostr/nip96.json; POST /upload; /presigned 'handles up to 5 GB'.
- tooling: curl; NIP-98 Authorization header (signed event). The llms.txt documents the /presigned path for large objects.
- composes with: Machine-readable plan manifest means the cap is queryable rather than scraped. One GET tells you the size ceiling per plan.
- reliability: Transforms media at ingest on some paths (resizing, format_conversion, compression, metadata_stripping are all listed in the manifest). Verify that originals come back byte-identical.
- notes: An active subscription is required to upload or store files.
- evidence note: the pricing page states there is no free tier and an active subscription is required
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [4] 2026-10-21: literal body: api_url https://nostrmedia.com/upload, download_url https://file.nostrmedia.com, supported_nips [94,96,98], plans.free.max_byte_size 26214400, file_expiration [0,0], media_transformations image [resizing, format_conversion, compression, metadata_stripping]
  - [3] 2026-10-21: 'A single POST to /upload accepts files up to 125 MB; /presigned handles up to 5 GB', 'Uploads never expire while the subscription is active'
  - [2] 2026-10-21: '/upload answers 413 above 125 MB because the request would outlive the worker'
  - [1] 2026-11-09: the pricing page is the source that states no free tier | capture: sha256:26a750e973db1cb247d6a575ce823b746ed32e860e64db6184eea20a6bdc273b | quote: Nostr Media has no free tier.
  - [2] 2026-11-09: the stated 5 GB ceiling converts to 5,000,000,000 bytes | capture: sha256:aa7f77e4860f489cba62005396e54910efed78e4d31902f45bf3691a0f2e762f | quote: Per-file ceiling on every tier is 5 GB.
  - [3] 2026-11-09: the llms.txt page is the source that states the retention | capture: sha256:17ed3d34cbb82dbb863535abd7a22bb504f032581f9efb5a815b1bf6dac864b4 | quote: Uploads never expire while the subscription is active.
  - [1] 2026-11-09: a subscription is keyed to a Nostr public key, not an email address | capture: sha256:26a750e973db1cb247d6a575ce823b746ed32e860e64db6184eea20a6bdc273b | quote: Subscriptions are tied to a Nostr public key, not to an email address.
  - [1] 2026-11-09: an active paid subscription is required to upload or store files | capture: sha256:26a750e973db1cb247d6a575ce823b746ed32e860e64db6184eea20a6bdc273b | quote: An active subscription is required to upload or store files.
- sources:
  - [1] https://nostrmedia.com/docs/pricing.md
  - [2] https://nostrmedia.com/docs/api.md
  - [3] https://nostrmedia.com/llms.txt
  - [4] https://nostrmedia.com/.well-known/nostr/nip96.json
